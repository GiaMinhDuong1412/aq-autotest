# -*- coding: utf-8 -*-
"""
AQ Autotest Console – bản chạy trên server công ty (MỘT file duy nhất, tự cập nhật).

Đặt file này vào một thư mục trống trên server rồi chạy:

    python aq-console-server.py            # chạy (cửa sổ dòng lệnh để mở)
    python aq-console-server.py --tu-chay  # Windows, quyền admin: tự chạy nền mỗi khi bật máy + mở cổng tường lửa

Lần đầu chạy, file tạo aq-console-server.json (cấu hình) và báo nếu cần token GitHub (repo riêng tư).
Sau đó nó tự làm hết:
  * tải code mới nhất của repo (nhánh "branch") về aq-console/app và chạy console ở cổng "port";
  * cứ "checkMinutes" phút hỏi GitHub có commit mới không – có thì tải về, kiểm tra, thay và khởi động lại
    (gián đoạn 1–2 giây); bản mới lỗi không chạy được thì tự quay lại bản cũ. Chính file này cũng tự cập nhật;
  * dữ liệu (kịch bản, lượt chạy, lỗi, release, ảnh) ở aq-console/du-lieu – không bị ghi đè khi cập nhật code.
    Kịch bản sửa trong repo được đưa vào nếu bản trong repo mới hơn (theo updatedAt);
  * tài khoản đăng nhập ở aq-console/rieng – lần đầu tạo admin, mật khẩu ở aq-console/rieng/mat-khau-admin-lan-dau.txt;
  * sao lưu dữ liệu mỗi ngày vào aq-console/sao-luu (giữ "keepBackups" bản), nhật ký ở aq-console/nhat-ky.txt.

Gắn domain: trỏ domain về server, mở cổng "port" (hoặc đặt port 80). Muốn https: điền "cert"/"key" (file .pem)
và đặt port 443, hoặc để IIS/nginx/Cloudflare lo https rồi chuyển về cổng này.
Linux (systemd): ExecStart=/usr/bin/python3 /đường/dẫn/aq-console-server.py, Restart=always.
Chỉ dùng thư viện chuẩn Python 3.8+.
"""
import json, os, sys, time, shutil, zipfile, io, hashlib, subprocess, datetime, urllib.request, urllib.error
from pathlib import Path
from urllib.parse import quote

SELF = Path(__file__).resolve()
HERE = SELF.parent
CONF = HERE / "aq-console-server.json"
HOME = HERE / "aq-console"
APP, DATA, PRIV, BAK = HOME / "app", HOME / "du-lieu", HOME / "rieng", HOME / "sao-luu"
LOG = HOME / "nhat-ky.txt"
TASK = "AQ Autotest Console"
DEFAULTS = {
    "repo": "giaminhduong1412/aq-autotest",
    "branch": "main",
    "token": "",
    "port": 8787,
    "host": "0.0.0.0",
    "checkMinutes": 2,
    "cert": "",
    "key": "",
    "keepBackups": 14,
}
HELP = ("token: repo GitHub riêng tư cần token chỉ-đọc. Tạo ở github.com → Settings → Developer settings → "
        "Fine-grained tokens → Generate: Repository access = Only select repositories (chọn repo này), "
        "Permissions → Contents = Read-only. Dán token vào \"token\", lưu file – không cần khởi động lại. "
        "branch: nhánh lấy code. port/host/cert/key: đổi xong phải khởi động lại file này.")


def log(*a):
    msg = time.strftime("%Y-%m-%d %H:%M:%S ") + " ".join(str(x) for x in a)
    try:
        print(msg, flush=True)
    except Exception:
        pass
    try:
        HOME.mkdir(parents=True, exist_ok=True)
        if LOG.exists() and LOG.stat().st_size > 2 * 1024 * 1024:
            os.replace(LOG, LOG.with_suffix(".cu.txt"))
        with LOG.open("a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass


def load_conf():
    cfg = dict(DEFAULTS)
    if not CONF.exists():
        CONF.write_text(json.dumps(dict(DEFAULTS, _huong_dan=HELP), ensure_ascii=False, indent=2), "utf-8")
        log("Đã tạo file cấu hình", CONF)
    try:
        cfg.update(json.loads(CONF.read_text("utf-8-sig")))
    except Exception as e:
        log("Không đọc được %s (%s) – dùng cấu hình mặc định" % (CONF.name, e))
    return cfg


# ------------------------------------------------------------------ GitHub
def gh(cfg, path, accept, timeout=60):
    h = {"Accept": accept, "User-Agent": "aq-console-server", "X-GitHub-Api-Version": "2022-11-28"}
    if (cfg.get("token") or "").strip():
        h["Authorization"] = "Bearer " + cfg["token"].strip()
    req = urllib.request.Request("https://api.github.com/repos/%s/%s" % (cfg["repo"], path), headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def latest_sha(cfg):
    return gh(cfg, "commits/" + quote(cfg["branch"], safe=""), "application/vnd.github.sha").decode().strip()


def download(cfg, sha, dest):
    z = zipfile.ZipFile(io.BytesIO(gh(cfg, "zipball/" + sha, "application/vnd.github+json", timeout=300)))
    if dest.exists():
        shutil.rmtree(dest)
    for info in z.infolist():
        parts = info.filename.split("/")[1:]              # bỏ thư mục gốc <owner>-<repo>-<sha>/
        if not parts or info.is_dir() or any(p in ("", ".", "..") for p in parts) or ":" in info.filename:
            continue
        out = dest.joinpath(*parts)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(z.read(info))


# ------------------------------------------------------------------ dữ liệu: đưa thay đổi trong repo vào, giữ dữ liệu của server
def digest(b):
    return hashlib.sha256(b).hexdigest()


def updated_at(b):
    try:
        return str(json.loads(b.decode("utf-8")).get("updatedAt") or "")
    except Exception:
        return ""


def sync_data(app):
    src = app / "data"
    if not src.is_dir():
        return
    man_f = PRIV / "repo-data.json"           # dấu vân tay từng file data/ của repo ở lần cập nhật trước
    try:
        old = json.loads(man_f.read_text("utf-8"))
    except Exception:
        old = {}
    first = not DATA.is_dir() or not any(DATA.rglob("*.json"))
    new, taken, kept = {}, 0, []
    for f in sorted(src.rglob("*")):
        if not f.is_file():
            continue
        rel = f.relative_to(src).as_posix()
        b = f.read_bytes()
        new[rel] = h = digest(b)
        if old.get(rel) == h and not first:
            continue                              # repo không đổi file này từ lần trước
        dst = DATA / rel
        if dst.exists():
            cur = dst.read_bytes()
            if cur == b:
                continue
            untouched = old.get(rel) == digest(cur)   # server chưa sửa file này → lấy bản repo
            if not untouched:
                if not rel.endswith(".json") or not (updated_at(b) > updated_at(cur)):
                    kept.append(rel)
                    continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        tmp = dst.with_name(dst.name + ".tmp")
        tmp.write_bytes(b)
        os.replace(tmp, dst)
        taken += 1
    PRIV.mkdir(parents=True, exist_ok=True)
    man_f.write_text(json.dumps(new, indent=0), "utf-8")
    if taken or kept:
        log("Dữ liệu từ repo: lấy %d file%s" % (taken, ("; giữ bản trên server (mới hơn): " + ", ".join(kept[:10])) if kept else ""))


def backup(cfg):
    BAK.mkdir(parents=True, exist_ok=True)
    z = BAK / (datetime.date.today().strftime("%Y%m%d") + ".zip")
    if z.exists() or not DATA.is_dir():
        return
    tmp = z.with_suffix(".tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zf:
        for base, name in ((DATA, "du-lieu"), (PRIV, "rieng")):
            for f in base.rglob("*"):
                if f.is_file() and "assets" not in f.relative_to(base).parts and not f.name.endswith(".tmp"):
                    zf.write(f, name + "/" + f.relative_to(base).as_posix())
    os.replace(tmp, z)
    if (DATA / "assets").is_dir():                # ảnh không bao giờ sửa → chỉ chép thêm ảnh mới
        (BAK / "assets").mkdir(exist_ok=True)
        for f in (DATA / "assets").iterdir():
            if f.is_file() and not (BAK / "assets" / f.name).exists():
                shutil.copy2(f, BAK / "assets" / f.name)
    for old in sorted(BAK.glob("*.zip"))[: -max(1, int(cfg.get("keepBackups") or 14))]:
        old.unlink()
    log("Đã sao lưu dữ liệu:", z.name)


# ------------------------------------------------------------------ chạy console (server.py --public)
class Console:
    p = None

    def start(self, cfg):
        cmd = [sys.executable, str(APP / "server.py"), "--public", "--no-browser", "--host", str(cfg["host"]),
               "--port", str(cfg["port"]), "--data", str(DATA), "--local", str(PRIV)]
        if cfg.get("cert"):
            cmd += ["--cert", str(cfg["cert"])] + (["--key", str(cfg["key"])] if cfg.get("key") else [])
        self.p = subprocess.Popen(cmd, cwd=str(APP))
        log("Console chạy ở cổng %s (bản %s)" % (cfg["port"], current_sha()[:7] or "?"))

    def stop(self):
        if self.p and self.p.poll() is None:
            self.p.terminate()
            try:
                self.p.wait(10)
            except subprocess.TimeoutExpired:
                self.p.kill()
        self.p = None

    def alive(self, wait=0):
        time.sleep(wait)
        return bool(self.p) and self.p.poll() is None


def current_sha():
    try:
        return (APP / ".sha").read_text("utf-8").strip()
    except Exception:
        return ""


def update(cfg, sha, con):
    log("Có bản mới %s – đang tải…" % sha[:7])
    new, old = HOME / "app.moi", HOME / "app.cu"
    download(cfg, sha, new)
    if not (new / "server.py").is_file():
        raise RuntimeError("bản tải về không có server.py")
    r = subprocess.run([sys.executable, "-m", "py_compile", str(new / "server.py")], capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError("server.py bản mới lỗi cú pháp: " + (r.stderr or r.stdout).strip()[-400:])
    sync_data(new)
    con.stop()
    if old.exists():
        shutil.rmtree(old)
    if APP.exists():
        APP.rename(old)
    new.rename(APP)
    (APP / ".sha").write_text(sha, "utf-8")
    con.start(cfg)
    if not con.alive(wait=4):
        log("Bản %s không chạy được – quay lại bản cũ" % sha[:7])
        con.stop()
        shutil.rmtree(APP)
        if old.exists():
            old.rename(APP)
            con.start(cfg)
        return False
    if old.exists():
        shutil.rmtree(old, ignore_errors=True)
    log("Đã cập nhật lên bản", sha[:7])
    return True


def self_update(con):
    """Repo có bản aq-console-server.py khác file đang chạy → chép đè rồi chạy lại chính nó."""
    src = APP / "aq-console-server.py"
    if not src.is_file() or src.read_bytes() == SELF.read_bytes():
        return
    tmp = SELF.with_name(SELF.name + ".tmp")
    tmp.write_bytes(src.read_bytes())
    os.replace(tmp, SELF)
    log("Đã cập nhật chính file", SELF.name, "– chạy lại")
    con.stop()
    if os.name == "nt":
        subprocess.Popen([sys.executable, str(SELF)] + sys.argv[1:], cwd=str(HERE))
        sys.exit(0)
    os.execv(sys.executable, [sys.executable, str(SELF)] + sys.argv[1:])


def install_task(cfg):
    if os.name != "nt":
        print("--tu-chay chỉ dành cho Windows. Linux: tạo dịch vụ systemd (xem đầu file).")
        return
    pyw = Path(sys.executable).with_name("pythonw.exe")
    exe = pyw if pyw.exists() else Path(sys.executable)
    tr = '"%s" "%s"' % (exe, SELF)
    r = subprocess.run(["schtasks", "/create", "/tn", TASK, "/tr", tr, "/sc", "onstart", "/ru", "SYSTEM", "/rl", "highest", "/f"],
                       capture_output=True, text=True)
    if r.returncode:
        print("Không tạo được tác vụ tự chạy (cần mở cửa sổ dòng lệnh bằng quyền admin):", (r.stderr or r.stdout).strip())
        return
    subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule", "name=" + TASK, "dir=in", "action=allow",
                    "protocol=TCP", "localport=%s" % cfg["port"]], capture_output=True)
    subprocess.run(["schtasks", "/run", "/tn", TASK], capture_output=True)
    print("Đã cài: console tự chạy nền mỗi khi bật máy (tác vụ \"%s\"), mở cổng %s trên tường lửa." % (TASK, cfg["port"]))
    print("Nhật ký:", LOG)


def main():
    cfg = load_conf()
    if "--tu-chay" in sys.argv:
        install_task(cfg)
        return
    HOME.mkdir(parents=True, exist_ok=True)
    log("AQ Autotest Console (server) – repo %s, nhánh %s" % (cfg["repo"], cfg["branch"]))
    con, bad, last_check, warned = Console(), set(), 0.0, ""
    if (APP / "server.py").is_file():
        con.start(cfg)
    try:
        while True:
            if time.time() - last_check >= max(0.5, float(cfg.get("checkMinutes") or 2)) * 60:
                last_check = time.time()
                cfg = load_conf()
                sha = None
                try:
                    sha = latest_sha(cfg)
                    warned = ""
                    if sha != current_sha() and sha not in bad:
                        if update(cfg, sha, con):
                            self_update(con)
                        else:
                            bad.add(sha)
                except urllib.error.HTTPError as e:
                    msg = ("GitHub từ chối (%s): repo riêng tư cần token chỉ-đọc – điền \"token\" trong %s"
                           % (e.code, CONF.name)) if e.code in (401, 403, 404) else "GitHub lỗi %s" % e.code
                    if msg != warned:
                        log(msg)
                        warned = msg
                except Exception as e:
                    log("Không cập nhật được:", e)
                    if sha and isinstance(e, RuntimeError):
                        bad.add(sha)
            if (APP / "server.py").is_file() and not con.alive():
                if con.p is not None:
                    log("Console dừng (mã %s) – khởi động lại" % con.p.returncode)
                    time.sleep(3)
                con.start(cfg)
            try:
                backup(cfg)
            except Exception as e:
                log("Không sao lưu được:", e)
            time.sleep(5)
    except KeyboardInterrupt:
        con.stop()


if __name__ == "__main__":
    main()

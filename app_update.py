# -*- coding: utf-8 -*-
"""Cập nhật phiên bản cho bản app AQ Auto Test (server.py nạp module này khi chạy dưới app/launcher.py, biến môi trường
AQ_APP_HOME = thư mục cài app). Chỉ thư viện chuẩn.

Phiên bản phát hành = GitHub Release của repo (do .github/workflows/release.yml tạo mỗi lần merge vào main), gồm
  aq-autotest-code-<ver>.zip (+ .sha256)  – mã nguồn để cập nhật
  AQ-AutoTest-<ver>-windows.zip            – bộ cài đầy đủ (kèm Python nhúng) cho máy mới.
Repo riêng tư nên cần token GitHub chỉ-đọc (Contents: Read-only), lưu ở <app>/rieng/app.json – không ghi vào log.
Cập nhật: tải gói mã → kiểm sha256 → giải nén vào phien-ban/<ver> → kiểm cú pháp server.py → ghi phien-ban/hien-tai.txt →
server thoát với mã 75, launcher khởi động lại bằng bản mới (dữ liệu ở du-lieu/ giữ nguyên, kịch bản mới được gộp theo updatedAt).
"""
import hashlib
import io
import json
import os
import py_compile
import re
import shutil
import threading
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

HOME = Path(os.environ.get("AQ_APP_HOME") or ".").resolve()
VERSION = os.environ.get("AQ_APP_VERSION") or "dev"
CONF = HOME / "rieng" / "app.json"
REPO_MAC_DINH = "giaminhduong1412/aq-autotest"
RESTART_CODE = 75
API = os.environ.get("AQ_APP_API") or "https://api.github.com"  # đổi được để thử nghiệm
STATE = {"busy": False, "msg": "", "latest": None}
PAGES = {}            # id trang console đang mở -> lần ping cuối (launcher dựa vào đây để biết cửa sổ app đã đóng)
PAGE_TTL = 150        # giây; trang ẩn/thu nhỏ bị trình duyệt giãn hẹn giờ tới ~1 phút


def conf():
    try:
        c = json.loads(CONF.read_text("utf-8"))
    except Exception:
        c = {}
    c.setdefault("repo", REPO_MAC_DINH)
    c.setdefault("token", "")
    return c


def save_conf(c):
    CONF.parent.mkdir(parents=True, exist_ok=True)
    CONF.write_text(json.dumps(c, ensure_ascii=False, indent=1), "utf-8")


def ver_key(v):
    return tuple(int(x) for x in re.findall(r"\d+", v or "")) or (0,)


def _req(url, token, accept="application/vnd.github+json", timeout=30):
    r = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": "aq-autotest-app"})
    if token:
        r.add_unredirected_header("Authorization", "Bearer " + token)  # không gửi token sang máy chủ tải file (S3)
    return urllib.request.urlopen(r, timeout=timeout)


def _loi(e):
    if isinstance(e, urllib.error.HTTPError):
        if e.code in (401, 403):
            return "GitHub từ chối (mã %d): token sai/hết hạn hoặc chưa có quyền đọc repo." % e.code
        if e.code == 404:
            return "Không thấy bản phát hành – repo riêng tư cần token chỉ-đọc, hoặc chưa có Release nào."
        return "GitHub báo lỗi %d." % e.code
    return "Không kết nối được GitHub: %s" % (getattr(e, "reason", None) or e)


def pages():
    now = time.time()
    for k in [k for k, t in PAGES.items() if now - t > PAGE_TTL]:
        PAGES.pop(k, None)
    return len(PAGES)


def ping(pid):
    if pid:
        PAGES[str(pid)[:40]] = time.time()
    return {"ok": True, "pages": pages()}


def bye(body):
    PAGES.pop(str(body.get("id") or "")[:40], None)
    return {"ok": True, "pages": pages()}


def info():
    c = conf()
    return {"app": True, "version": VERSION, "repo": c["repo"], "hasToken": bool(c["token"]), "busy": STATE["busy"],
            "msg": STATE["msg"], "latest": STATE["latest"], "pages": pages()}


def set_token(body):
    c = conf()
    if "token" in body:
        c["token"] = (body.get("token") or "").strip()
    if body.get("repo"):
        c["repo"] = body["repo"].strip()
    save_conf(c)
    return info()


def check():
    c = conf()
    try:
        with _req(API + "/repos/%s/releases/latest" % c["repo"], c["token"]) as r:
            rel = json.loads(r.read().decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(_loi(e))
    tag = (rel.get("tag_name") or "").lstrip("v")
    assets = {a["name"]: a for a in rel.get("assets") or []}
    code = next((a for n, a in assets.items() if n.startswith("aq-autotest-code-") and n.endswith(".zip")), None)
    full = next((a for n, a in assets.items() if n.endswith("-windows.zip")), None)
    STATE["latest"] = {"version": tag, "name": rel.get("name") or tag, "notes": (rel.get("body") or "")[:4000],
                       "publishedAt": rel.get("published_at"), "page": rel.get("html_url"),
                       "hasCode": bool(code), "fullUrl": full and full.get("browser_download_url")}
    out = info()
    out["newer"] = bool(code) and ver_key(tag) > ver_key(VERSION) and VERSION != "dev"
    return out


def _tai(c, asset):
    with _req(asset["url"], c["token"], accept="application/octet-stream", timeout=300) as r:
        return r.read()


def gop_du_lieu(seed, data):
    """Đưa dữ liệu mẫu của bản mới (data/ trong gói) vào du-lieu/: bản ghi chưa có thì chép, có rồi thì chỉ thay khi updatedAt mới hơn."""
    seed, data = Path(seed), Path(data)
    n = 0
    if not seed.is_dir():
        return 0
    for f in seed.rglob("*"):
        if not f.is_file():
            continue
        d = data / f.relative_to(seed)
        if d.exists():
            if f.suffix != ".json":
                continue
            try:
                a = json.loads(f.read_text("utf-8"))
                b = json.loads(d.read_text("utf-8"))
                if str(a.get("updatedAt") or "") <= str(b.get("updatedAt") or ""):
                    continue
            except Exception:
                continue
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, d)
        n += 1
    return n


def _cap_nhat():
    c = conf()
    try:
        STATE["msg"] = "Đang kiểm tra bản mới…"
        with _req(API + "/repos/%s/releases/latest" % c["repo"], c["token"]) as r:
            rel = json.loads(r.read().decode("utf-8"))
        tag = (rel.get("tag_name") or "").lstrip("v")
        assets = {a["name"]: a for a in rel.get("assets") or []}
        name = next((n for n in assets if n.startswith("aq-autotest-code-") and n.endswith(".zip")), None)
        if not name:
            raise RuntimeError("Bản phát hành %s không có gói mã aq-autotest-code-*.zip." % tag)
        STATE["msg"] = "Đang tải bản %s…" % tag
        b = _tai(c, assets[name])
        if name + ".sha256" in assets:
            want = _tai(c, assets[name + ".sha256"]).decode("ascii", "replace").split()[0].lower()
            if hashlib.sha256(b).hexdigest() != want:
                raise RuntimeError("Gói tải về hỏng (sai sha256) – thử lại.")
        dst = HOME / "phien-ban" / tag
        tmp = HOME / "phien-ban" / (tag + ".tmp")
        shutil.rmtree(tmp, ignore_errors=True)
        with zipfile.ZipFile(io.BytesIO(b)) as z:
            for m in z.namelist():
                p = Path(m)
                if p.is_absolute() or ".." in p.parts:
                    raise RuntimeError("Gói có đường dẫn lạ: " + m)
            z.extractall(tmp)
        py_compile.compile(str(tmp / "server.py"), doraise=True)
        shutil.rmtree(dst, ignore_errors=True)
        tmp.rename(dst)
        if (dst / "launcher.py").exists():
            shutil.copy2(dst / "launcher.py", HOME / "launcher.py")
        gop_du_lieu(dst / "data", HOME / "du-lieu")
        (HOME / "phien-ban" / "hien-tai.txt").write_text(tag, "utf-8")
        for cu in (HOME / "phien-ban").iterdir():  # giữ bản mới + bản đang chạy (để quay lại khi cần), xoá bản cũ hơn
            if cu.is_dir() and cu.name not in (tag, VERSION):
                shutil.rmtree(cu, ignore_errors=True)
        STATE["msg"] = "Đã cài bản %s – đang khởi động lại…" % tag
        threading.Timer(1.0, lambda: os._exit(RESTART_CODE)).start()
    except Exception as e:  # noqa: BLE001
        STATE["msg"] = "Cập nhật lỗi: " + (str(e) if isinstance(e, RuntimeError) else _loi(e))
    finally:
        STATE["busy"] = False


def update():
    if STATE["busy"]:
        return info()
    STATE["busy"] = True
    STATE["msg"] = "Bắt đầu cập nhật…"
    threading.Thread(target=_cap_nhat, daemon=True).start()
    time.sleep(0.2)
    return info()


def quit_app():
    threading.Timer(0.5, lambda: os._exit(0)).start()
    return {"ok": True}

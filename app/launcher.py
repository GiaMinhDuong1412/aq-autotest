# -*- coding: utf-8 -*-
"""AQ Auto Test – app chạy trên máy cá nhân (Windows). Chạy bằng "AQ Auto Test.cmd" (Python nhúng trong thư mục python/).

Thư mục cài (giải nén AQ-AutoTest-<ver>-windows.zip ở đâu cũng được, vd D:\\AQ-AutoTest):
  launcher.py            file này – khởi động console, tự khởi động lại sau khi cập nhật
  python/                Python nhúng (không cài vào Windows)
  phien-ban/<ver>/       mã nguồn từng phiên bản; phien-ban/hien-tai.txt = bản đang dùng
  du-lieu/               dữ liệu của máy này (kịch bản, lượt chạy, lỗi, ảnh) – giữ nguyên khi cập nhật
  rieng/                 cấu hình riêng (config.json, app.json: cổng, token GitHub chỉ-đọc)
  nhat-ky.txt            nhật ký

Console mở trong CỬA SỔ APP RIÊNG (Microsoft Edge/Chrome chế độ --app: không thanh địa chỉ, không tab, hồ sơ riêng ở
rieng/cua-so) – không phải tab trình duyệt. Đóng cửa sổ = thoát app (server tắt theo). Máy không có Edge/Chrome thì mở
trình duyệt mặc định; rieng/app.json {"window": false} để luôn mở bằng trình duyệt.
Nút "Cập nhật" trên console tải bản mới từ GitHub Release, server thoát với mã 75 và file này chạy lại bằng bản mới
(cửa sổ giữ nguyên, trang tự tải lại). Đang chạy rồi mà bấm lối tắt lần nữa thì mở thêm một cửa sổ.
Chỉ thư viện chuẩn.
"""
import json
import os
import shutil
import socket
import subprocess
import sys
import time
import urllib.request
import webbrowser
from pathlib import Path

HOME = Path(__file__).resolve().parent
DATA, RIENG, VERS = HOME / "du-lieu", HOME / "rieng", HOME / "phien-ban"
LOG = HOME / "nhat-ky.txt"
RESTART_CODE = 75


def log(*a):
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S ") + " ".join(str(x) for x in a) + "\n")
    except OSError:
        pass


def cau_hinh():
    try:
        c = json.loads((RIENG / "app.json").read_text("utf-8"))
    except Exception:
        c = {}
    return c


def khoa(v):
    return [int(x) if x.isdigit() else 0 for x in v.replace("-", ".").split(".")]


def ban_hien_tai():
    """Bản ghi trong hien-tai.txt, nhưng nếu có bản mới hơn đã cài đủ (vd cài đè bằng Setup.exe mới / bản tự cập nhật) thì lấy bản mới nhất."""
    ds = sorted((p.name for p in VERS.iterdir() if p.is_dir() and not p.name.endswith(".tmp") and (p / "server.py").exists()),
                key=khoa) if VERS.is_dir() else []
    try:
        v = (VERS / "hien-tai.txt").read_text("utf-8").strip()
    except OSError:
        v = ""
    if v in ds and khoa(v) >= khoa(ds[-1]):
        return v
    return ds[-1] if ds else None


def dang_chay(port):
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=1):
            pass
    except OSError:
        return False
    try:
        with urllib.request.urlopen("http://127.0.0.1:%d/api/app/info" % port, timeout=3) as r:
            return bool(json.loads(r.read().decode("utf-8")).get("app"))
    except Exception:
        return True  # cổng bị chương trình khác giữ


def gop_du_lieu(seed):
    """Lần đầu / sau khi đổi phiên bản: đưa dữ liệu mẫu (kịch bản, danh mục…) của bản mới vào du-lieu/ theo updatedAt."""
    if not seed.is_dir():
        return 0
    n = 0
    for f in seed.rglob("*"):
        if not f.is_file():
            continue
        d = DATA / f.relative_to(seed)
        if d.exists():
            if f.suffix != ".json":
                continue
            try:
                if str(json.loads(f.read_text("utf-8")).get("updatedAt") or "") <= str(json.loads(d.read_text("utf-8")).get("updatedAt") or ""):
                    continue
            except Exception:
                continue
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, d)
        n += 1
    return n


def tao_loi_tat():
    """Lần đầu: tạo lối tắt "AQ Auto Test" trên Desktop (bỏ qua nếu không được)."""
    dau = RIENG / "da-tao-loi-tat"
    if dau.exists() or os.name != "nt" or list(HOME.glob("unins*.exe")):  # cài bằng Setup.exe thì bộ cài đã tạo lối tắt
        return
    cmd = HOME / "AQ Auto Test.cmd"
    ps = ("$s=(New-Object -ComObject WScript.Shell).CreateShortcut([Environment]::GetFolderPath('Desktop')+'\\AQ Auto Test.lnk');"
          "$s.TargetPath='%s';$s.WorkingDirectory='%s';$s.WindowStyle=7;$s.Save()" % (str(cmd).replace("'", "''"), str(HOME).replace("'", "''")))
    try:
        subprocess.run(["powershell", "-NoProfile", "-Command", ps], timeout=30, creationflags=0x08000000)
        dau.parent.mkdir(parents=True, exist_ok=True)
        dau.write_text("1", "utf-8")
    except Exception as e:  # noqa: BLE001
        log("Không tạo được lối tắt:", e)


def tim_trinh_duyet():
    """msedge.exe (có sẵn trên Windows 10/11) hoặc chrome.exe."""
    if os.name != "nt":
        for n in ("microsoft-edge", "google-chrome", "chromium", "chromium-browser"):
            f = shutil.which(n)
            if f:
                return f
        return None
    try:
        import winreg
        for exe in ("msedge.exe", "chrome.exe"):
            for root in (winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE):
                try:
                    with winreg.OpenKey(root, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\" + exe) as k:
                        f = winreg.QueryValue(k, None).strip('"')
                    if f and Path(f).is_file():
                        return f
                except OSError:
                    pass
    except ImportError:
        pass
    for base in (os.environ.get("ProgramFiles(x86)"), os.environ.get("ProgramFiles"), os.environ.get("LOCALAPPDATA")):
        for rel in (r"Microsoft\Edge\Application\msedge.exe", r"Google\Chrome\Application\chrome.exe"):
            if base and (Path(base) / rel).is_file():
                return str(Path(base) / rel)
    return None


def mo_cua_so(url, c):
    """Mở console trong cửa sổ app riêng. Trả về tiến trình trình duyệt (None nếu phải mở bằng trình duyệt mặc định)."""
    exe = tim_trinh_duyet() if c.get("window", True) else None
    if exe:
        try:
            return subprocess.Popen([exe, "--app=" + url, "--user-data-dir=" + str(RIENG / "cua-so"), "--no-first-run",
                                     "--no-default-browser-check", "--disable-sync", "--window-size=1440,900"],
                                    stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except OSError as e:
            log("Không mở được cửa sổ app bằng", exe, ":", e)
    webbrowser.open(url)
    return None


def so_trang(port):
    """Số trang console đang mở (trang ping server 30 giây/lần, đóng thì báo 'bye'); None nếu server chưa trả lời."""
    try:
        with urllib.request.urlopen("http://127.0.0.1:%d/api/app/info" % port, timeout=3) as r:
            return int(json.loads(r.read().decode("utf-8")).get("pages") or 0)
    except Exception:
        return None


def thong_bao_loi(msg):
    log(msg)
    if os.name == "nt":
        try:
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, msg, "AQ Auto Test", 0x10)
        except Exception:
            pass


def main():
    c = cau_hinh()
    port = int(c.get("port") or 8788)
    url = "http://localhost:%d/" % port
    if dang_chay(port):
        mo_cua_so(url, c)
        return 0
    for d in (DATA, RIENG):
        d.mkdir(parents=True, exist_ok=True)
    tao_loi_tat()
    cua_so, mo_luc = None, 0.0
    while True:
        ver = ban_hien_tai()
        if not ver:
            thong_bao_loi("Không thấy phiên bản nào trong %s – cài lại AQ Auto Test." % VERS)
            return 1
        code = VERS / ver
        dau = DATA / ".phien-ban-du-lieu"
        if not dau.exists() or dau.read_text("utf-8").strip() != ver:
            log("Gộp dữ liệu mẫu bản", ver, ":", gop_du_lieu(code / "data"), "file")
            dau.write_text(ver, "utf-8")
        env = dict(os.environ, AQ_APP_HOME=str(HOME), AQ_APP_VERSION=ver, PYTHONIOENCODING="utf-8")
        args = [sys.executable, str(code / "server.py"), "--port", str(port), "--data", str(DATA), "--local", str(RIENG),
                "--no-browser"]
        log("Chạy bản", ver, "cổng", port)
        bat_dau = time.time()
        with open(LOG, "a", encoding="utf-8") as out:
            p = subprocess.Popen(args, cwd=str(code), env=env, stdout=out, stderr=out,
                                 creationflags=0x08000000 if os.name == "nt" else 0)
            # chờ server sẵn sàng rồi mới mở cửa sổ (lần đầu); khởi động lại sau cập nhật thì cửa sổ cũ tự tải lại trang
            while p.poll() is None and so_trang(port) is None and time.time() - bat_dau < 60:
                time.sleep(0.3)
            if p.poll() is None and cua_so is None and not mo_luc:
                cua_so, mo_luc = mo_cua_so(url, c), time.time()
            da_thay, vang_tu, dong = False, None, False
            while p.poll() is None:
                time.sleep(1)
                # 1) tiến trình cửa sổ app kết thúc = người dùng đóng cửa sổ (thoát ngay sau khi mở = trình duyệt chuyển
                #    sang phiên đang chạy sẵn → không theo dõi được tiến trình, dựa vào số trang)
                if cua_so is not None and cua_so.poll() is not None:
                    if time.time() - mo_luc > 8:
                        log("Cửa sổ app đã đóng – tắt server")
                        dong = True
                        break
                    cua_so = None
                # 2) không còn trang console nào mở (đã từng có) quá 20 giây
                n = so_trang(port)
                if n:
                    da_thay, vang_tu = True, None
                elif n == 0 and da_thay:
                    vang_tu = vang_tu or time.time()
                    if time.time() - vang_tu > 20:
                        log("Không còn trang console nào mở – tắt server")
                        dong = True
                        break
            if dong:
                p.terminate()
                try:
                    p.wait(10)
                except subprocess.TimeoutExpired:
                    p.kill()
                return 0
            rc = p.wait()
        log("Server dừng, mã", rc)
        if rc == RESTART_CODE:
            time.sleep(1)
            continue
        if cua_so is not None and cua_so.poll() is None:
            cua_so.terminate()   # bấm "Thoát app" (mã 0) hoặc server lỗi: đóng cửa sổ theo
        if rc not in (0, None) and time.time() - bat_dau < 30:
            thong_bao_loi("AQ Auto Test không khởi động được (mã %s). Xem nhật ký: %s" % (rc, LOG))
        return rc


if __name__ == "__main__":
    sys.exit(main())

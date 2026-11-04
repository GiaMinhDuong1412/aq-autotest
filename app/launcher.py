# -*- coding: utf-8 -*-
"""AQ Auto Test – app chạy trên máy cá nhân (Windows). Chạy bằng "AQ Auto Test.cmd" (Python nhúng trong thư mục python/).

Thư mục cài (giải nén AQ-AutoTest-<ver>-windows.zip ở đâu cũng được, vd D:\\AQ-AutoTest):
  launcher.py            file này – khởi động console, tự khởi động lại sau khi cập nhật
  python/                Python nhúng (không cài vào Windows)
  phien-ban/<ver>/       mã nguồn từng phiên bản; phien-ban/hien-tai.txt = bản đang dùng
  du-lieu/               dữ liệu của máy này (kịch bản, lượt chạy, lỗi, ảnh) – giữ nguyên khi cập nhật
  rieng/                 cấu hình riêng (config.json, app.json: cổng, token GitHub chỉ-đọc)
  nhat-ky.txt            nhật ký

Mở console ở http://localhost:<cổng> (mặc định 8788). Nút "Cập nhật" trên console tải bản mới từ GitHub Release, server thoát
với mã 75 và file này chạy lại bằng bản mới. Đang chạy rồi mà bấm lại thì chỉ mở trình duyệt.
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


def main():
    c = cau_hinh()
    port = int(c.get("port") or 8788)
    url = "http://localhost:%d/" % port
    if dang_chay(port):
        webbrowser.open(url)
        return 0
    for d in (DATA, RIENG):
        d.mkdir(parents=True, exist_ok=True)
    tao_loi_tat()
    lan_dau = True
    while True:
        ver = ban_hien_tai()
        if not ver:
            log("Không thấy phiên bản nào trong", VERS)
            return 1
        code = VERS / ver
        dau = DATA / ".phien-ban-du-lieu"
        if not dau.exists() or dau.read_text("utf-8").strip() != ver:
            log("Gộp dữ liệu mẫu bản", ver, ":", gop_du_lieu(code / "data"), "file")
            dau.write_text(ver, "utf-8")
        env = dict(os.environ, AQ_APP_HOME=str(HOME), AQ_APP_VERSION=ver, PYTHONIOENCODING="utf-8")
        args = [sys.executable, str(code / "server.py"), "--port", str(port), "--data", str(DATA), "--local", str(RIENG)]
        if not lan_dau:
            args.append("--no-browser")
        log("Chạy bản", ver, "cổng", port)
        with open(LOG, "a", encoding="utf-8") as out:
            p = subprocess.Popen(args, cwd=str(code), env=env, stdout=out, stderr=out,
                                 creationflags=0x08000000 if os.name == "nt" else 0)
            rc = p.wait()
        log("Server dừng, mã", rc)
        if rc == RESTART_CODE:
            lan_dau = False
            time.sleep(1)
            continue
        return rc


if __name__ == "__main__":
    sys.exit(main())

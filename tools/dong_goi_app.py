# -*- coding: utf-8 -*-
"""Đóng gói app AQ Auto Test cho một phiên bản (GitHub Actions gọi khi merge vào main; chạy tay được).

    python tools/dong_goi_app.py --phien-ban 2026.11.04-1 [--ra dist] [--python <zip Python nhúng | URL>] [--khong-python]

Tạo trong thư mục --ra:
  aq-autotest-code-<ver>.zip (+ .sha256)  gói mã để app tự cập nhật (server.py, app_update.py, launcher.py, web/, kit/, data mẫu)
  AQ-AutoTest-<ver>-windows.zip           bộ cài đầy đủ: AQ-AutoTest/{AQ Auto Test.cmd, launcher.py, python/, phien-ban/<ver>/}
Chỉ thư viện chuẩn.
"""
import argparse
import hashlib
import io
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY_URL = "https://www.python.org/ftp/python/3.12.10/python-3.12.10-embed-amd64.zip"
DATA_MAU = ("scenarios", "testPlans", "releases", "releaseItems", "members", "settings")  # không gồm runs/bugs/runners (riêng từng máy)


def ds_ma(ver):
    """[(đường dẫn trong gói, bytes)] của gói mã."""
    out = [("PHIEN-BAN.txt", ver.encode("utf-8"))]
    for f in ("server.py", "app_update.py"):
        out.append((f, (ROOT / f).read_bytes()))
    out.append(("launcher.py", (ROOT / "app" / "launcher.py").read_bytes()))
    for f in ("index.html", "claude-shim.js", "edusoft-catalog.json"):
        if (ROOT / "web" / f).exists():
            out.append(("web/" + f, (ROOT / "web" / f).read_bytes()))
    for p in sorted((ROOT / "kit").rglob("*")):
        if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc":
            out.append(("kit/" + p.relative_to(ROOT / "kit").as_posix(), p.read_bytes()))
    for col in DATA_MAU:
        d = ROOT / "data" / col
        if d.is_dir():
            for p in sorted(d.rglob("*.json")):
                out.append(("data/" + p.relative_to(ROOT / "data").as_posix(), p.read_bytes()))
    return out


def lay_python(nguon):
    if nguon.startswith(("http://", "https://")):
        print("Tải Python nhúng:", nguon)
        with urllib.request.urlopen(nguon, timeout=300) as r:
            return r.read()
    return Path(nguon).read_bytes()


def main():
    ap = argparse.ArgumentParser(description="Đóng gói app AQ Auto Test")
    ap.add_argument("--phien-ban", required=True)
    ap.add_argument("--ra", default="dist")
    ap.add_argument("--python", default=PY_URL, help="zip Python nhúng (đường dẫn hoặc URL)")
    ap.add_argument("--khong-python", action="store_true", help="chỉ tạo gói mã (thử nhanh)")
    a = ap.parse_args()
    ver = a.phien_ban.lstrip("v")
    ra = Path(a.ra)
    ra.mkdir(parents=True, exist_ok=True)

    files = ds_ma(ver)
    code = ra / ("aq-autotest-code-%s.zip" % ver)
    with zipfile.ZipFile(code, "w", zipfile.ZIP_DEFLATED) as z:
        for n, b in files:
            z.writestr(n, b)
    h = hashlib.sha256(code.read_bytes()).hexdigest()
    (ra / (code.name + ".sha256")).write_text("%s  %s\n" % (h, code.name), "ascii")
    print("Gói mã:", code, "(%d file, %d KB)" % (len(files), code.stat().st_size // 1024))
    if a.khong_python:
        return 0

    py = zipfile.ZipFile(io.BytesIO(lay_python(a.python)))
    full = ra / ("AQ-AutoTest-%s-windows.zip" % ver)
    g = "AQ-AutoTest/"
    with zipfile.ZipFile(full, "w", zipfile.ZIP_DEFLATED) as z:
        for n in py.namelist():
            if not n.endswith("/"):
                z.writestr(g + "python/" + n, py.read(n))
        z.writestr(g + "AQ Auto Test.cmd", (ROOT / "app" / "AQ Auto Test.cmd").read_bytes())
        z.writestr(g + "HUONG-DAN.txt", (ROOT / "app" / "HUONG-DAN.txt").read_bytes())
        z.writestr(g + "launcher.py", (ROOT / "app" / "launcher.py").read_bytes())
        z.writestr(g + "phien-ban/hien-tai.txt", ver)
        for n, b in files:
            z.writestr(g + "phien-ban/%s/%s" % (ver, n), b)
    print("Bộ cài:", full, "(%d KB)" % (full.stat().st_size // 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())

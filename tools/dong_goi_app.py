# -*- coding: utf-8 -*-
"""Chuẩn bị tài nguyên cho app AQ Auto Test (desktop/, Electron) trước khi electron-builder đóng gói.
GitHub Actions gọi khi merge vào main (và khi kiểm tra PR); chạy tay được.

    python tools/dong_goi_app.py [--ra desktop/res] [--python <zip Python nhúng | URL>] [--khong-python]

Tạo trong thư mục --ra:
  app/      mã server: server.py, app_update.py, web/ (index.html, claude-shim.js, edusoft-catalog.json), kit/, data/ mẫu
  python/   Python nhúng (python.org, bản embed amd64) – app chạy app/server.py bằng python/pythonw.exe
Chỉ thư viện chuẩn.
"""
import argparse
import io
import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY_URL = "https://www.python.org/ftp/python/3.12.10/python-3.12.10-embed-amd64.zip"
DATA_MAU = ("scenarios", "testPlans", "releases", "releaseItems", "members", "settings")  # không gồm runs/bugs/runners (riêng từng máy)


def ds_ma():
    """[(đường dẫn trong app/, bytes)]."""
    out = []
    for f in ("server.py", "app_update.py"):
        out.append((f, (ROOT / f).read_bytes()))
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
    ap = argparse.ArgumentParser(description="Chuẩn bị tài nguyên app AQ Auto Test")
    ap.add_argument("--ra", default=str(ROOT / "desktop" / "res"))
    ap.add_argument("--python", default=PY_URL, help="zip Python nhúng (đường dẫn hoặc URL)")
    ap.add_argument("--khong-python", action="store_true", help="chỉ chép mã (thử nhanh)")
    a = ap.parse_args()
    ra = Path(a.ra)
    app = ra / "app"
    shutil.rmtree(app, ignore_errors=True)
    files = ds_ma()
    for n, b in files:
        f = app / n
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(b)
    print("Mã:", app, "(%d file)" % len(files))
    if a.khong_python:
        return 0
    py = ra / "python"
    shutil.rmtree(py, ignore_errors=True)
    with zipfile.ZipFile(io.BytesIO(lay_python(a.python))) as z:
        z.extractall(py)
    if not (py / "pythonw.exe").exists():
        print("Gói Python nhúng thiếu pythonw.exe")
        return 1
    print("Python nhúng:", py)
    return 0


if __name__ == "__main__":
    sys.exit(main())

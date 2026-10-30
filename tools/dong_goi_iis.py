# -*- coding: utf-8 -*-
"""Đóng gói bộ cài IIS: server-iis/* + aq-console-server.py → AQAutotest-IIS-cai-dat.zip (đưa lên server, giải nén, chạy CAI-DAT.cmd).
    python tools/dong_goi_iis.py [thư mục ra]"""
import sys, zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
out = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT) / "AQAutotest-IIS-cai-dat.zip"
files = [p for p in sorted((ROOT / "server-iis").iterdir()) if p.is_file() and p.name != "cai-dat-log.txt"]
files.append(ROOT / "aq-console-server.py")
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for p in files:
        z.write(p, "AQAutotest-IIS-cai-dat/" + p.name)
print("Đã tạo", out, "–", len(files), "file")

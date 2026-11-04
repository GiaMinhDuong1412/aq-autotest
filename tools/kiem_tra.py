# -*- coding: utf-8 -*-
"""Kiểm tra nhanh trước khi phát hành (GitHub Actions chạy; chạy tay được): cú pháp Python, JS trang console (node --check nếu có),
web/index.html đã nhúng đúng kit/ (tools/embed_kit.py). Lỗi thì thoát mã 1.
    python tools/kiem_tra.py"""
import py_compile, re, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
loi = []
for f in ["server.py", "app_update.py", "aq-console-server.py", "kit/aqrun.py", "kit/aq-agent.py"] + \
        [p.relative_to(ROOT).as_posix() for p in (ROOT / "tools").glob("*.py")]:
    try:
        py_compile.compile(str(ROOT / f), doraise=True)
    except py_compile.PyCompileError as e:
        loi.append("Cú pháp %s: %s" % (f, e.msg))
html = (ROOT / "web" / "index.html").read_text("utf-8")
from server import KIT_BLOCKS, KIT  # noqa: E402
for bid, fn in KIT_BLOCKS.items():
    tag = '<script type="text/plain" id="%s">\n' % bid
    i = html.find(tag)
    if i < 0 or html[i + len(tag): html.index("</script>", i)] != (KIT / fn).read_text("utf-8").replace("\r\n", "\n"):
        loi.append("web/index.html chưa nhúng bản mới của kit/%s – chạy python tools/embed_kit.py" % fn)
if shutil.which("node"):
    js = html[html.rindex("<script>") + 8: html.rindex("</script>")]
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as t:
        t.write(js)
    r = subprocess.run(["node", "--check", t.name], capture_output=True, text=True)
    if r.returncode:
        loi.append("JS trang console: " + (r.stderr or r.stdout)[:800])
    for f in sorted((ROOT / "desktop" / "src").glob("*.js")):     # app Electron
        r = subprocess.run(["node", "--check", str(f)], capture_output=True, text=True)
        if r.returncode:
            loi.append("JS %s: %s" % (f.relative_to(ROOT).as_posix(), (r.stderr or r.stdout)[:800]))
import json  # noqa: E402
try:
    json.loads((ROOT / "desktop" / "package.json").read_text("utf-8"))
except Exception as e:  # noqa: BLE001
    loi.append("desktop/package.json lỗi: %s" % e)
if not (ROOT / "web" / "edusoft-catalog.json").exists():
    loi.append("Thiếu web/edusoft-catalog.json (tools/lap_danh_muc.py --json)")
print("\n".join(loi) or "Kiểm tra: OK")
sys.exit(1 if loi else 0)

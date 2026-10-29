# -*- coding: utf-8 -*-
"""Nhúng lại các file trong kit/ vào web/index.html và đặt KITVER theo kit/aqrun.py.
server.py đã tự nhúng khi phục vụ trang; chạy script này trước khi commit để web/index.html
(bản một file, dùng được cho artifact claude.ai) luôn khớp mã bộ test."""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from server import KIT_BLOCKS, KIT, WEB, kit_version  # noqa: E402

p = WEB / "index.html"
html = p.read_text("utf-8")
for bid, fn in KIT_BLOCKS.items():
    body = (KIT / fn).read_text("utf-8").replace("\r\n", "\n")
    if "</script" in body:
        raise SystemExit("%s chứa chuỗi </script – không nhúng được" % fn)
    tag = '<script type="text/plain" id="%s">\n' % bid
    i = html.index(tag)
    j = html.index("</script>", i)
    html = html[: i + len(tag)] + body + html[j:]
ver = kit_version(KIT)
html = re.sub(r"var KITVER='[^']*';", "var KITVER='%s';" % ver, html, count=1)
p.write_text(html, "utf-8")
print("Đã nhúng %d file bộ test, KITVER = %s" % (len(KIT_BLOCKS), ver))

# -*- coding: utf-8 -*-
"""
AQ Autotest Console – bản chạy trên máy (localhost).

    python server.py            # mở http://localhost:8787
    python server.py --port 9000 --no-browser

Chỉ dùng thư viện chuẩn của Python 3.8+. Server:
  * phục vụ giao diện console (web/index.html) – các file bộ test trong kit/ được nhúng
    vào trang lúc phục vụ, sửa kit/*.py là trang thấy ngay;
  * thay "window.claude" của claude.ai bằng web/claude-shim.js: dữ liệu lưu ở data/
    (mỗi bản ghi một file JSON – đồng bộ giữa các máy bằng git), ảnh ở data/assets/;
  * làm luôn "cầu nối" tới thư mục bộ test trên máy này: nút Chạy ghi lệnh thẳng vào
    thư mục bộ test (AQ Autotest Agent nhận và chạy), kết quả đọc thẳng từ results\\.
Dữ liệu riêng của máy (cấu hình, mật khẩu Netweb nếu có) nằm ở local/ – KHÔNG đưa lên git.
"""
import json, os, re, sys, time, uuid, base64, mimetypes, threading, webbrowser, argparse, shutil
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote

ROOT = Path(__file__).resolve().parent
WEB, KIT, DATA, LOCAL = ROOT / "web", ROOT / "kit", ROOT / "data", ROOT / "local"
ASSETS = DATA / "assets"
CFG_FILE = LOCAL / "config.json"
DEFAULT_USER = "u_L8VJITzyuU54eIqCAl0PKQ"     # người dùng trên console claude.ai (giữ nguyên để dữ liệu cũ khớp)
SEG = re.compile(r"^[A-Za-z0-9_\-.~:@+]{1,200}$")
RUN_ID = re.compile(r"^sc-[a-z0-9][a-z0-9-]{3,80}$")
FILE_NAME = re.compile(r"^[^\\/:*?\"<>|]{1,120}$")
KIT_BLOCKS = {"kit-aqrun": "aqrun.py", "kit-agent": "aq-agent.py", "kit-caidat": "cai-dat.bat", "kit-chaytest": "chay-test.bat",
              "kit-quenmk": "quen-mat-khau.bat", "kit-huongdan": "HUONG-DAN.txt"}
LOCK = threading.Lock()
REV = {"n": 0}


# ------------------------------------------------------------------ cấu hình máy
def load_cfg():
    cfg = {"port": 8787, "kitDir": "", "userId": DEFAULT_USER, "userName": os.environ.get("USERNAME", "") or "Tôi"}
    try:
        cfg.update(json.loads(CFG_FILE.read_text("utf-8")))
    except Exception:
        pass
    return cfg


def save_cfg(cfg):
    LOCAL.mkdir(parents=True, exist_ok=True)
    CFG_FILE.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), "utf-8")


CFG = load_cfg()


# ------------------------------------------------------------------ kho dữ liệu JSON
def col_dir(path):
    segs = [s for s in str(path or "").split("/") if s]
    if not segs or len(segs) % 2 == 0 or not all(SEG.match(s) and s not in (".", "..") for s in segs):
        raise ValueError("Đường dẫn collection không hợp lệ: %s" % path)
    if segs[0] == "data" and len(segs) >= 3 and segs[1] == "users":
        if segs[2] == "me":
            segs[2] = CFG["userId"]
        return LOCAL.joinpath(*segs)           # dữ liệu riêng từng người: chỉ ở máy này
    return DATA.joinpath(*segs)


def doc_file(path, doc_id):
    if not SEG.match(str(doc_id or "")) or doc_id in (".", ".."):
        raise ValueError("Mã bản ghi không hợp lệ")
    return col_dir(path) / (fname(doc_id) + ".json")


def fname(doc_id):          # Windows không cho ":" trong tên file
    return doc_id.replace("%", "%25").replace(":", "%3A")


def unfname(stem):
    return stem.replace("%3A", ":").replace("%25", "%")


def read_doc(f):
    try:
        return json.loads(f.read_text("utf-8"))
    except Exception:
        return None


def write_doc(f, data):
    f.parent.mkdir(parents=True, exist_ok=True)
    tmp = f.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True) + "\n", "utf-8")
    os.replace(tmp, f)
    REV["n"] += 1


def list_docs(path):
    d = col_dir(path)
    out = []
    if d.is_dir():
        for f in sorted(d.glob("*.json")):
            v = read_doc(f)
            if isinstance(v, dict):
                out.append({"id": unfname(f.stem), "data": v})
    return out


def data_signature():
    n, newest = 0, 0.0
    for base in (DATA, LOCAL):
        if base.is_dir():
            for dp, dn, fn in os.walk(base):
                if "assets" in Path(dp).parts:
                    continue
                for x in fn:
                    if x.endswith(".json"):
                        n += 1
                        try:
                            newest = max(newest, os.path.getmtime(os.path.join(dp, x)))
                        except OSError:
                            pass
    return "%d-%d-%.3f" % (REV["n"], n, newest)


# ------------------------------------------------------------------ ảnh / file đính kèm
def asset_path(aid):
    if not re.match(r"^[0-9a-f]{32}$", aid or ""):
        return None
    for p in ASSETS.glob(aid + "*"):
        if p.is_file() and not p.name.endswith(".tmp"):
            return p
    return None


def save_asset(body, ctype):
    ASSETS.mkdir(parents=True, exist_ok=True)
    aid = uuid.uuid4().hex
    ext = mimetypes.guess_extension((ctype or "").split(";")[0].strip()) or ".bin"
    if ext == ".jpe":
        ext = ".jpg"
    (ASSETS / (aid + ext)).write_bytes(body)
    return {"id": aid, "url": "/_blob/" + aid, "sizeBytes": len(body), "contentType": ctype or "application/octet-stream"}


# ------------------------------------------------------------------ bộ test trên máy (thay cầu nối)
def kit_dir():
    d = (CFG.get("kitDir") or "").strip()
    if not d:
        raise RuntimeError("Chưa khai báo thư mục bộ test trên máy này – nhập đường dẫn (vd D:\\AQ-Autotest) rồi bấm Lưu thư mục.")
    p = Path(d)
    if not p.is_dir():
        raise RuntimeError("Không thấy thư mục bộ test: %s" % d)
    return p


def kit_version(base):
    try:
        m = re.search(r'KIT_VERSION = "([^"]+)"', (base / "aqrun.py").read_text("utf-8"))
        return m.group(1) if m else ""
    except Exception:
        return ""


def agent_running():
    if os.name != "nt":
        return None
    try:
        import ctypes
        h = ctypes.windll.kernel32.OpenMutexW(0x00100000, False, "AQAutotestAgentMutex")
        if h:
            ctypes.windll.kernel32.CloseHandle(h)
            return True
    except Exception:
        return None
    return False


def k_status(a):
    base = kit_dir()
    log = []
    try:
        log = (base / "agent.log").read_text("utf-8", errors="replace").splitlines()[-6:]
    except Exception:
        pass
    cfg = {}
    try:
        c = json.loads((base / "config.json").read_text("utf-8"))
        cfg = {k: c.get(k) for k in ("exe", "account", "machine", "env", "kitVersion")}
    except Exception:
        pass
    return {"kitDir": str(base), "kitVersion": kit_version(base), "config": cfg, "agent": {"running": agent_running(), "log": log},
            "computer": os.environ.get("COMPUTERNAME", ""), "local": True,
            "scenarios": sorted(p.stem for p in (base / "scenarios").glob("*.json")) if (base / "scenarios").is_dir() else []}


def k_send(a):
    base = kit_dir()
    payload = a.get("payload")
    if not isinstance(payload, dict) or payload.get("format") not in ("aq-autotest-update/1", "aq-autotest-run-request/1"):
        raise ValueError("Lệnh không đúng định dạng")
    name = "aq-autotest-update-run.json" if payload["format"] == "aq-autotest-update/1" else "aq-autotest-run.json"
    tmp = base / (name + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False), "utf-8")
    os.replace(tmp, base / name)
    return {"ok": True, "file": str(base / name), "agent": agent_running() is not False}


def k_list(a):
    base = kit_dir() / "results"
    runs = []
    if base.is_dir():
        dirs = sorted([d for d in base.iterdir() if d.is_dir() and RUN_ID.match(d.name)], key=lambda d: d.stat().st_mtime, reverse=True)
        for d in dirs[: int(a.get("limit") or 30)]:
            it = {"runId": d.name, "complete": (d / "result.json").exists(), "files": sorted(p.name for p in d.iterdir() if p.is_file())}
            if it["complete"]:
                r = read_doc(d / "result.json") or {}
                it.update(scenarioCode=r.get("scenarioCode"), status=r.get("status"), finishedAt=r.get("finishedAt"))
            runs.append(it)
    return {"kitDir": str(kit_dir()), "runs": runs}


def run_dir(a):
    rid = str(a.get("runId") or "")
    if not RUN_ID.match(rid):
        raise ValueError("runId không hợp lệ")
    d = kit_dir() / "results" / rid
    if not d.is_dir():
        raise ValueError("Không có lượt chạy " + rid)
    return d


def k_read_result(a):
    return json.loads((run_dir(a) / "result.json").read_text("utf-8"))


def k_read_file(a):
    name = str(a.get("name") or "")
    if not FILE_NAME.match(name) or name.startswith("."):
        raise ValueError("Tên file không hợp lệ")
    p = run_dir(a) / name
    if not p.is_file():
        raise ValueError("Không có file " + name)
    if p.stat().st_size > 20 * 1024 * 1024:
        return {"name": name, "size": p.stat().st_size, "tooLarge": True}
    return {"name": name, "size": p.stat().st_size, "mimeType": mimetypes.guess_type(name)[0] or "application/octet-stream",
            "base64": base64.b64encode(p.read_bytes()).decode("ascii")}


def k_set_kit_dir(a):
    d = str(a.get("dir") or "").strip().strip('"')
    if d and not Path(d).is_dir():
        raise ValueError("Không thấy thư mục: " + d)
    CFG["kitDir"] = d
    save_cfg(CFG)
    return {"ok": True, "kitDir": d}


def k_install(a):
    """Chép mã bộ test (kit/) vào thư mục bộ test – dùng khi cài trên máy mới."""
    d = str(a.get("dir") or CFG.get("kitDir") or "").strip().strip('"')
    if not d:
        raise ValueError("Chưa có thư mục bộ test")
    base = Path(d)
    base.mkdir(parents=True, exist_ok=True)
    for f in KIT.iterdir():
        if f.is_file() and f.suffix in (".py", ".bat", ".txt"):
            dest = base / f.name
            if f.suffix == ".bat":
                dest.write_bytes(f.read_text("utf-8").replace("\r\n", "\n").replace("\n", "\r\n").encode("utf-8"))
            else:
                shutil.copyfile(f, dest)
    (base / "results").mkdir(exist_ok=True)
    (base / "scenarios").mkdir(exist_ok=True)
    CFG["kitDir"] = str(base)
    save_cfg(CFG)
    return {"ok": True, "kitDir": str(base)}


KIT_TOOLS = {"status": k_status, "send": k_send, "list_results": k_list, "read_result": k_read_result, "read_file": k_read_file,
             "set_kit_dir": k_set_kit_dir, "install": k_install}


# ------------------------------------------------------------------ trang
def page_html():
    html = (WEB / "index.html").read_text("utf-8")
    for bid, fn in KIT_BLOCKS.items():
        f = KIT / fn
        if not f.exists():
            continue
        body = f.read_text("utf-8").replace("\r\n", "\n")
        tag = '<script type="text/plain" id="%s">\n' % bid
        i = html.find(tag)
        if i < 0:
            continue
        j = html.find("</script>", i)
        html = html[: i + len(tag)] + body + html[j:]
    ver = kit_version(KIT)
    if ver:
        html = re.sub(r"var KITVER='[^']*';", "var KITVER='%s';" % ver, html, count=1)
    head = ('<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<script>window.AQ_LOCAL={userId:%s,userName:%s};</script><script src="/claude-shim.js"></script></head><body>'
            % (json.dumps(CFG["userId"]), json.dumps(CFG.get("userName") or "")))
    return head + html + "</body></html>"


class H(BaseHTTPRequestHandler):
    server_version = "AQAutotest/1"

    def log_message(self, fmt, *args):
        if os.environ.get("AQ_DEBUG"):
            sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def send(self, code, body, ctype="application/json; charset=utf-8", extra=None):
        if isinstance(body, (dict, list)):
            body = json.dumps(body, ensure_ascii=False).encode("utf-8")
        elif isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def body(self):
        n = int(self.headers.get("Content-Length") or 0)
        return self.rfile.read(n) if n else b""

    def jbody(self):
        b = self.body()
        return json.loads(b.decode("utf-8")) if b else {}

    def guard(self):
        """Chỉ nhận yêu cầu từ chính trang localhost (chặn trang web lạ gọi API qua trình duyệt)."""
        host = (self.headers.get("Host") or "").split(":")[0]
        if host not in ("localhost", "127.0.0.1"):
            self.send(403, {"error": "forbidden"})
            return False
        if self.command != "GET" and self.headers.get("X-AQ") != "1":
            self.send(403, {"error": "forbidden"})
            return False
        return True

    def do_GET(self):
        if not self.guard():
            return
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            if u.path in ("/", "/index.html"):
                return self.send(200, page_html(), "text/html; charset=utf-8")
            if u.path == "/claude-shim.js":
                return self.send(200, (WEB / "claude-shim.js").read_bytes(), "text/javascript; charset=utf-8")
            if u.path.startswith("/_blob/"):
                p = asset_path(unquote(u.path[7:]))
                if not p:
                    return self.send(404, {"error": "not found"})
                return self.send(200, p.read_bytes(), mimetypes.guess_type(p.name)[0] or "application/octet-stream",
                                 {"Cache-Control": "max-age=31536000, immutable"})
            if u.path == "/api/rev":
                return self.send(200, {"rev": data_signature()})
            if u.path == "/api/db":
                return self.send(200, {"docs": list_docs(q.get("path"))})
            if u.path == "/api/doc":
                f = doc_file(q.get("path"), q.get("id"))
                v = read_doc(f) if f.exists() else None
                return self.send(200, {"exists": v is not None, "data": v})
            if u.path == "/api/me":
                return self.send(200, {"id": CFG["userId"], "name": CFG.get("userName") or ""})
            return self.send(404, {"error": "not found"})
        except ValueError as e:
            return self.send(400, {"error": str(e)})

    def do_POST(self):
        if not self.guard():
            return
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            if u.path == "/api/db":                       # add
                doc_id = uuid.uuid4().hex[:20]
                with LOCK:
                    write_doc(doc_file(q.get("path"), doc_id), self.jbody())
                return self.send(200, {"id": doc_id})
            if u.path == "/api/assets":
                return self.send(200, save_asset(self.body(), self.headers.get("Content-Type")))
            if u.path.startswith("/api/kit/"):
                tool = u.path[9:]
                if tool not in KIT_TOOLS:
                    return self.send(404, {"error": "Không có công cụ " + tool})
                try:
                    return self.send(200, KIT_TOOLS[tool](self.jbody()))
                except (RuntimeError, ValueError, OSError) as e:
                    return self.send(422, {"error": str(e)})
            return self.send(404, {"error": "not found"})
        except ValueError as e:
            return self.send(400, {"error": str(e)})

    def do_PUT(self):                                    # set
        if not self.guard():
            return
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            data = self.jbody()
            with LOCK:
                write_doc(doc_file(q.get("path"), q.get("id")), data)
            return self.send(200, {"ok": True})
        except ValueError as e:
            return self.send(400, {"error": str(e)})

    def do_PATCH(self):                                  # update (gộp trường cấp 1)
        if not self.guard():
            return
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            patch = self.jbody()
            with LOCK:
                f = doc_file(q.get("path"), q.get("id"))
                cur = read_doc(f) if f.exists() else None
                if cur is None:
                    return self.send(404, {"error": "Không có bản ghi", "code": "not_found"})
                for k, v in patch.items():
                    if isinstance(v, dict) and v.get("__delete__") is True:
                        cur.pop(k, None)
                    else:
                        cur[k] = v
                write_doc(f, cur)
            return self.send(200, {"ok": True})
        except ValueError as e:
            return self.send(400, {"error": str(e)})

    def do_DELETE(self):
        if not self.guard():
            return
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            with LOCK:
                f = doc_file(q.get("path"), q.get("id"))
                if f.exists():
                    f.unlink()
                    REV["n"] += 1
            return self.send(200, {"ok": True})
        except ValueError as e:
            return self.send(400, {"error": str(e)})


def main():
    ap = argparse.ArgumentParser(description="AQ Autotest Console trên localhost")
    ap.add_argument("--port", type=int, default=int(CFG.get("port") or 8787))
    ap.add_argument("--no-browser", action="store_true")
    a = ap.parse_args()
    if not CFG_FILE.exists():
        save_cfg(CFG)
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), H)
    url = "http://localhost:%d/" % a.port
    print("AQ Autotest Console: %s   (Ctrl+C để dừng)" % url)
    print("Dữ liệu: %s   ·   Thư mục bộ test: %s" % (DATA, CFG.get("kitDir") or "(chưa khai báo)"))
    if not a.no_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

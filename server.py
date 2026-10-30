# -*- coding: utf-8 -*-
"""
AQ Autotest Console – bản chạy trên máy (localhost).

    python server.py            # mở http://localhost:8787
    python server.py --port 9000 --no-browser
    python server.py --public --host 0.0.0.0 --data D:\\du-lieu --local D:\\rieng   # chạy trên server có domain

Chế độ --public (server công ty, thường do aq-console-server.py khởi động): bắt đăng nhập (tài khoản ở
<local>/auth.json, lần đầu tạo admin và ghi mật khẩu vào <local>/mat-khau-admin-lan-dau.txt), nhận mọi tên miền,
tắt các công cụ /api/kit (server không phải máy chạy test – nút Chạy sẽ tải file lệnh về máy người bấm).

Chỉ dùng thư viện chuẩn của Python 3.8+. Server:
  * phục vụ giao diện console (web/index.html) – các file bộ test trong kit/ được nhúng
    vào trang lúc phục vụ, sửa kit/*.py là trang thấy ngay;
  * thay "window.claude" của claude.ai bằng web/claude-shim.js: dữ liệu lưu ở data/
    (mỗi bản ghi một file JSON – đồng bộ giữa các máy bằng git), ảnh ở data/assets/;
  * làm luôn "cầu nối" tới thư mục bộ test trên máy này: nút Chạy ghi lệnh thẳng vào
    thư mục bộ test (AQ Autotest Agent nhận và chạy), kết quả đọc thẳng từ results\\.
Dữ liệu riêng của máy (cấu hình, mật khẩu Netweb nếu có) nằm ở local/ – KHÔNG đưa lên git.
"""
import json, os, re, sys, time, uuid, base64, mimetypes, threading, webbrowser, argparse, shutil, hmac, hashlib, secrets, ssl
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote
from http.cookies import SimpleCookie

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
MODE = {"public": False, "https": False, "base": ""}     # base: đường dẫn con khi chạy dưới IIS, vd /aqautotest
CUR = threading.local()                         # người dùng của yêu cầu đang xử lý (chế độ --public)


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
        me = getattr(CUR, "uid", None) or CFG["userId"]
        if segs[2] == "me":
            segs[2] = me
        elif MODE["public"] and segs[2] != me:
            raise ValueError("Không được đọc dữ liệu riêng của người khác")
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
    return {"id": aid, "url": "_blob/" + aid, "sizeBytes": len(body), "contentType": ctype or "application/octet-stream"}


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
    stamp = time.strftime("%Y%m%d-%H%M%S") + "-%03d" % (int(time.time() * 1000) % 1000)   # mỗi lần bấm Chạy một file riêng
    name = ("aq-autotest-update-run-%s.json" if payload["format"] == "aq-autotest-update/1" else "aq-autotest-run-%s.json") % stamp
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


# ------------------------------------------------------------------ tài khoản (chế độ --public)
AUTH = {"data": None}
FAILS = {}                                      # tên đăng nhập -> [số lần sai, khoá đến]
COOKIE = "aq_s"
LOGIN_RE = re.compile(r"^[a-z0-9._-]{2,40}$")


def auth_file():
    return LOCAL / "auth.json"


def pw_hash(pw, salt=None):
    salt = salt or secrets.token_hex(16)
    return "pbkdf2$200000$%s$%s" % (salt, hashlib.pbkdf2_hmac("sha256", pw.encode("utf-8"), salt.encode(), 200000).hex())


def pw_ok(pw, h):
    try:
        _, n, salt, dig = h.split("$")
        got = hashlib.pbkdf2_hmac("sha256", pw.encode("utf-8"), salt.encode(), int(n)).hex()
        return hmac.compare_digest(got, dig)
    except Exception:
        return False


def save_auth():
    LOCAL.mkdir(parents=True, exist_ok=True)
    tmp = auth_file().with_suffix(".tmp")
    tmp.write_text(json.dumps(AUTH["data"], ensure_ascii=False, indent=1), "utf-8")
    os.replace(tmp, auth_file())


def load_auth():
    try:
        AUTH["data"] = json.loads(auth_file().read_text("utf-8"))
        return
    except FileNotFoundError:
        pass
    pw = secrets.token_urlsafe(9)
    # admin đầu tiên giữ mã người dùng cũ để dữ liệu đã có (người tạo kịch bản, máy chạy test…) vẫn khớp
    AUTH["data"] = {"secret": secrets.token_hex(32), "users": {DEFAULT_USER: {
        "login": "admin", "name": CFG.get("userName") or "Quản trị", "admin": True, "pw": pw_hash(pw), "ver": 1}}}
    save_auth()
    (LOCAL / "mat-khau-admin-lan-dau.txt").write_text(
        "Tài khoản quản trị AQ Autotest Console\r\nTên đăng nhập: admin\r\nMật khẩu: %s\r\n"
        "Đăng nhập xong vào trang Tài khoản (/quan-tri) để đổi mật khẩu, thêm người dùng – rồi xoá file này.\r\n" % pw, "utf-8")
    print("Đã tạo tài khoản admin – mật khẩu ghi trong", LOCAL / "mat-khau-admin-lan-dau.txt")


def users():
    return AUTH["data"]["users"]


def find_login(login):
    for uid, u in users().items():
        if u.get("login") == login:
            return uid, u
    return None, None


def make_token(uid, u, days=30):
    body = "%s|%d|%d" % (uid, int(time.time()) + days * 86400, u.get("ver", 1))
    sig = hmac.new(AUTH["data"]["secret"].encode(), body.encode(), hashlib.sha256).hexdigest()
    return base64.urlsafe_b64encode(body.encode()).decode().rstrip("=") + "." + sig


def check_token(tok):
    try:
        b64, sig = tok.split(".")
        body = base64.urlsafe_b64decode(b64 + "=" * (-len(b64) % 4)).decode()
        if not hmac.compare_digest(hmac.new(AUTH["data"]["secret"].encode(), body.encode(), hashlib.sha256).hexdigest(), sig):
            return None
        uid, exp, ver = body.split("|")
        u = users().get(uid)
        if not u or int(exp) < time.time() or int(ver) != u.get("ver", 1):
            return None
        return uid
    except Exception:
        return None


def user_public(uid, u):
    return {"id": uid, "login": u.get("login"), "name": u.get("name") or u.get("login"), "admin": bool(u.get("admin"))}


def a_login(h, a):
    login = str(a.get("login") or "").strip().lower()
    pw = str(a.get("password") or "")
    f = FAILS.get(login)
    if f and f[1] > time.time():
        return h.send(429, {"error": "Sai quá nhiều lần – thử lại sau %d phút." % (int(f[1] - time.time()) // 60 + 1)})
    uid, u = find_login(login)
    if not u or not pw_ok(pw, u.get("pw", "")):
        f = FAILS.setdefault(login, [0, 0])
        f[0] += 1
        if f[0] >= 8:
            FAILS[login] = [0, time.time() + 600]
        time.sleep(0.6)
        return h.send(401, {"error": "Sai tên đăng nhập hoặc mật khẩu"})
    FAILS.pop(login, None)
    return h.send(200, {"ok": True}, extra={"Set-Cookie": h.cookie(make_token(uid, u), 30 * 86400)})


def a_account(h, a):
    """Đổi mật khẩu của mình; admin thêm / đặt lại mật khẩu / xoá người dùng."""
    me = users()[CUR.uid]
    act = a.get("action")
    with LOCK:
        if act == "password":
            if not pw_ok(str(a.get("old") or ""), me["pw"]):
                return h.send(400, {"error": "Mật khẩu hiện tại không đúng"})
            new = str(a.get("new") or "")
            if len(new) < 8:
                return h.send(400, {"error": "Mật khẩu mới phải từ 8 ký tự"})
            me["pw"], me["ver"] = pw_hash(new), me.get("ver", 1) + 1
            save_auth()
            return h.send(200, {"ok": True}, extra={"Set-Cookie": h.cookie(make_token(CUR.uid, me), 30 * 86400)})
        if act == "name":
            me["name"] = str(a.get("name") or "").strip()[:60] or me["login"]
            save_auth()
            return h.send(200, {"ok": True})
        if not me.get("admin"):
            return h.send(403, {"error": "Chỉ quản trị mới làm được việc này"})
        if act == "add":
            login = str(a.get("login") or "").strip().lower()
            if not LOGIN_RE.match(login):
                return h.send(400, {"error": "Tên đăng nhập 2–40 ký tự: chữ thường không dấu, số, . _ -"})
            if find_login(login)[1]:
                return h.send(400, {"error": "Đã có tên đăng nhập " + login})
            pw = secrets.token_urlsafe(9)
            uid = "u_" + secrets.token_urlsafe(16).replace("-", "x").replace("_", "y")
            users()[uid] = {"login": login, "name": str(a.get("name") or "").strip()[:60] or login, "admin": bool(a.get("admin")),
                            "pw": pw_hash(pw), "ver": 1}
            save_auth()
            return h.send(200, {"ok": True, "password": pw})
        uid = str(a.get("id") or "")
        u = users().get(uid)
        if not u:
            return h.send(404, {"error": "Không có người dùng"})
        if act == "reset":
            pw = secrets.token_urlsafe(9)
            u["pw"], u["ver"] = pw_hash(pw), u.get("ver", 1) + 1
            save_auth()
            return h.send(200, {"ok": True, "password": pw})
        if act in ("delete", "admin"):
            if uid == CUR.uid:
                return h.send(400, {"error": "Không tự xoá / bỏ quyền quản trị của chính mình"})
            if act == "delete":
                users().pop(uid)
            else:
                u["admin"] = bool(a.get("admin"))
            save_auth()
            return h.send(200, {"ok": True})
    return h.send(400, {"error": "Thao tác không hợp lệ"})


LOGIN_HTML = """<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Đăng nhập – AQ Autotest</title><style>
:root{--bg:#f4f6f8;--card:#fff;--fg:#1d2733;--mute:#5f6b78;--line:#d6dce3;--acc:#0b6bcb;--err:#b42318}
@media (prefers-color-scheme:dark){:root{--bg:#12161b;--card:#1b2128;--fg:#e6ebf0;--mute:#9aa6b2;--line:#2c3540;--acc:#4ea1f3;--err:#f97066}}
*{box-sizing:border-box}body{margin:0;min-height:100vh;display:grid;place-items:center;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,Segoe UI,sans-serif;padding:16px}
form,.box{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:28px;width:100%%;max-width:%s}
h1{font-size:20px;margin:0 0 4px}p{color:var(--mute);margin:0 0 18px}label{display:block;font-size:13px;color:var(--mute);margin:12px 0 4px}
input{width:100%%;padding:9px 11px;border:1px solid var(--line);border-radius:8px;background:transparent;color:inherit;font:inherit}
button{margin-top:16px;padding:9px 14px;border:0;border-radius:8px;background:var(--acc);color:#fff;font:inherit;font-weight:600;cursor:pointer}
button.ghost{background:transparent;color:var(--acc);border:1px solid var(--line);margin-top:0;padding:5px 10px;font-size:13px}
.err{color:var(--err);min-height:1.5em;margin-top:10px}table{width:100%%;border-collapse:collapse;margin-top:8px}td,th{text-align:left;padding:7px 6px;border-top:1px solid var(--line);font-size:14px}
h2{font-size:16px;margin:24px 0 4px}a{color:var(--acc)}.row{display:flex;gap:8px;flex-wrap:wrap;align-items:end}.row>div{flex:1;min-width:140px}
</style></head><body>%s</body></html>"""

LOGIN_BODY = """<form id="f"><h1>AQ Autotest Console</h1><p>Đăng nhập để vào console</p>
<label for="l">Tên đăng nhập</label><input id="l" autocomplete="username" autofocus required>
<label for="p">Mật khẩu</label><input id="p" type="password" autocomplete="current-password" required>
<button>Đăng nhập</button><div class="err" id="e"></div></form><script>
document.getElementById('f').onsubmit=async function(ev){ev.preventDefault();var e=document.getElementById('e');e.textContent='';
var r=await fetch('login',{method:'POST',headers:{'Content-Type':'application/json','X-AQ':'1'},body:JSON.stringify({login:l.value,password:p.value})});
if(r.ok){location.href='./';return;}try{e.textContent=(await r.json()).error;}catch(x){e.textContent='Lỗi '+r.status;}};</script>"""

ACCOUNT_BODY = """<div class="box"><h1>Tài khoản</h1><p><a href="./">← Về console</a> · <a href="#" id="out">Đăng xuất</a></p>
<h2>Tên hiển thị</h2><div class="row"><div><input id="nm"></div><button class="ghost" id="nmb">Lưu</button></div>
<h2>Đổi mật khẩu</h2><div class="row"><div><label for="o">Mật khẩu hiện tại</label><input id="o" type="password" autocomplete="current-password"></div>
<div><label for="n">Mật khẩu mới (từ 8 ký tự)</label><input id="n" type="password" autocomplete="new-password"></div><button class="ghost" id="pwb">Đổi</button></div>
<div id="adm" hidden><h2>Người dùng</h2><table id="t"></table><h2>Thêm người dùng</h2>
<div class="row"><div><label for="al">Tên đăng nhập</label><input id="al" placeholder="vd: thuy.nt"></div><div><label for="an">Tên hiển thị</label><input id="an"></div>
<button class="ghost" id="ab">Thêm</button></div></div><div class="err" id="e"></div></div><script>
var E=document.getElementById('e'),ME=null;function say(t){E.textContent=t||'';}
async function call(a){var r=await fetch('api/account',{method:'POST',headers:{'Content-Type':'application/json','X-AQ':'1'},body:JSON.stringify(a)});
var j={};try{j=await r.json();}catch(x){}if(!r.ok)throw new Error(j.error||('Lỗi '+r.status));return j;}
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
async function load(){ME=await (await fetch('api/me')).json();nm.value=ME.name||'';if(!ME.admin)return;adm.hidden=false;
var us=(await (await fetch('api/users')).json()).users;t.innerHTML='<tr><th>Đăng nhập</th><th>Tên</th><th>Quyền</th><th></th></tr>'+us.map(function(u){
return '<tr><td>'+esc(u.login)+'</td><td>'+esc(u.name)+'</td><td>'+(u.admin?'Quản trị':'Thành viên')+'</td><td>'+(u.id===ME.id?'(bạn)':
'<button class="ghost" data-a="reset" data-id="'+u.id+'">Đặt lại mật khẩu</button> <button class="ghost" data-a="admin" data-v="'+(u.admin?'':'1')+'" data-id="'+u.id+'">'+(u.admin?'Bỏ quản trị':'Cho quản trị')+'</button> <button class="ghost" data-a="delete" data-id="'+u.id+'">Xoá</button>')+'</td></tr>';}).join('');}
function newPw(who,pw){say('');alert('Mật khẩu của '+who+': '+pw+'\\n\\nGửi riêng cho người đó; họ đổi lại ở trang Tài khoản sau khi đăng nhập.');}
t.onclick=async function(ev){var b=ev.target.closest('button');if(!b)return;var a=b.dataset.a,id=b.dataset.id;
if(a==='delete'&&!confirm('Xoá người dùng này?'))return;try{var j=await call({action:a,id:id,admin:!!b.dataset.v});if(j.password)newPw('người dùng',j.password);load();}catch(x){say(x.message);}};
ab.onclick=async function(){try{var j=await call({action:'add',login:al.value,name:an.value});newPw(al.value,j.password);al.value=an.value='';load();}catch(x){say(x.message);}};
nmb.onclick=async function(){try{await call({action:'name',name:nm.value});say('Đã lưu tên.');}catch(x){say(x.message);}};
pwb.onclick=async function(){try{await call({action:'password',old:o.value,new:n.value});o.value=n.value='';say('Đã đổi mật khẩu.');}catch(x){say(x.message);}};
out.onclick=async function(ev){ev.preventDefault();await fetch('logout',{method:'POST',headers:{'X-AQ':'1'}});location.href='login';};
load().catch(function(x){say(x.message);});</script>"""


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
    js = lambda v: json.dumps(v).replace("<", "\\u003c")
    if MODE["public"]:
        u = users()[CUR.uid]
        boot = "window.AQ_SERVER={userId:%s,userName:%s};" % (js(CUR.uid), js(u.get("name") or u.get("login")))
    else:
        boot = "window.AQ_LOCAL={userId:%s,userName:%s};" % (js(CFG["userId"]), js(CFG.get("userName") or ""))
    head = ('<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<script>%s</script><script src="claude-shim.js"></script></head><body>' % boot)
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
        self.send_header("X-Content-Type-Options", "nosniff")
        if MODE["public"]:
            self.send_header("X-Frame-Options", "SAMEORIGIN")
            self.send_header("Referrer-Policy", "same-origin")
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

    def cookie(self, value, max_age):
        https = MODE["https"] or (self.headers.get("X-Forwarded-Proto") or "").lower() == "https"
        return "%s=%s; Path=%s/; Max-Age=%d; HttpOnly; SameSite=Lax%s" % (COOKIE, value, MODE["base"], max_age, "; Secure" if https else "")

    def guard(self):
        """Localhost: chỉ nhận yêu cầu từ chính trang localhost. --public: bắt đăng nhập.
        Lệnh ghi phải có header X-AQ (trang web lạ không gửi được header này qua trình duyệt)."""
        CUR.uid = None
        base = MODE["base"]
        if base:                                       # dưới IIS: bỏ đường dẫn con, trang dùng URL tương đối
            raw = urlparse(self.path).path
            if raw == base:
                self.send(301, "", "text/plain; charset=utf-8", {"Location": base + "/"})
                return False
            if raw.startswith(base + "/"):
                self.path = self.path[len(base):]
        if self.command != "GET" and self.headers.get("X-AQ") != "1":
            self.send(403, {"error": "forbidden"})
            return False
        if not MODE["public"]:
            host = (self.headers.get("Host") or "").split(":")[0]
            if host not in ("localhost", "127.0.0.1"):
                self.send(403, {"error": "forbidden"})
                return False
            return True
        path = urlparse(self.path).path
        try:
            c = SimpleCookie(self.headers.get("Cookie") or "")
            CUR.uid = check_token(c[COOKIE].value) if COOKIE in c else None
        except Exception:
            CUR.uid = None
        if CUR.uid or path in ("/login", "/logout", "/favicon.ico"):
            return True
        if self.command == "GET" and not path.startswith(("/api/", "/_blob/")):
            self.send(302, "", "text/plain; charset=utf-8", {"Location": MODE["base"] + "/login"})
        else:
            self.send(401, {"error": "Cần đăng nhập lại", "code": "login"})
        return False

    def do_GET(self):
        if not self.guard():
            return
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            if u.path in ("/", "/index.html"):
                return self.send(200, page_html(), "text/html; charset=utf-8")
            if MODE["public"] and u.path == "/login":
                if CUR.uid:
                    return self.send(302, "", "text/plain; charset=utf-8", {"Location": MODE["base"] + "/"})
                return self.send(200, LOGIN_HTML % ("380px", LOGIN_BODY), "text/html; charset=utf-8")
            if MODE["public"] and u.path == "/quan-tri":
                return self.send(200, LOGIN_HTML % ("760px", ACCOUNT_BODY), "text/html; charset=utf-8")
            if u.path == "/api/users":
                if not MODE["public"]:
                    return self.send(200, {"users": [{"id": CFG["userId"], "name": CFG.get("userName") or ""}]})
                return self.send(200, {"users": [user_public(k, v) for k, v in users().items()]})
            if u.path == "/claude-shim.js":
                return self.send(200, (WEB / "claude-shim.js").read_bytes(), "text/javascript; charset=utf-8")
            if u.path.startswith("/_blob/"):
                p = asset_path(unquote(u.path[7:]))
                if not p:
                    return self.send(404, {"error": "not found"})
                ct = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
                extra = {"Cache-Control": "private, max-age=31536000, immutable", "Content-Security-Policy": "sandbox"}
                if not (ct.startswith(("image/", "video/", "audio/")) and ct != "image/svg+xml" or ct == "application/pdf"):
                    ct = "application/octet-stream"            # file đính kèm lạ (html, svg…): tải về, không mở trong trang
                    extra["Content-Disposition"] = 'attachment; filename="%s"' % p.name
                return self.send(200, p.read_bytes(), ct, extra)
            if u.path == "/api/rev":
                return self.send(200, {"rev": data_signature()})
            if u.path == "/api/db":
                return self.send(200, {"docs": list_docs(q.get("path"))})
            if u.path == "/api/doc":
                f = doc_file(q.get("path"), q.get("id"))
                v = read_doc(f) if f.exists() else None
                return self.send(200, {"exists": v is not None, "data": v})
            if u.path == "/api/me":
                if MODE["public"]:
                    return self.send(200, user_public(CUR.uid, users()[CUR.uid]))
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
            if MODE["public"] and u.path == "/login":
                return a_login(self, self.jbody())
            if MODE["public"] and u.path == "/logout":
                return self.send(200, {"ok": True}, extra={"Set-Cookie": self.cookie("", 0)})
            if MODE["public"] and u.path == "/api/account":
                return a_account(self, self.jbody())
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
                if MODE["public"]:                         # server không phải máy chạy test
                    return self.send(422, {"error": "Bản console trên server không điều khiển trực tiếp máy chạy test."})
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
    global DATA, LOCAL, ASSETS, CFG_FILE, CFG
    ap = argparse.ArgumentParser(description="AQ Autotest Console")
    ap.add_argument("--port", type=int, default=int(CFG.get("port") or 8787))
    ap.add_argument("--no-browser", action="store_true")
    ap.add_argument("--public", action="store_true", help="chạy trên server có domain: bắt đăng nhập, nhận mọi tên miền")
    ap.add_argument("--host", default=None, help="địa chỉ nghe (mặc định 127.0.0.1; --public mặc định 0.0.0.0)")
    ap.add_argument("--data", help="thư mục dữ liệu (mặc định data/ cạnh server.py)")
    ap.add_argument("--local", help="thư mục riêng của máy (mặc định local/)")
    ap.add_argument("--cert", help="file chứng chỉ HTTPS (.pem) – chạy https trực tiếp")
    ap.add_argument("--key", help="file khoá riêng của chứng chỉ (.pem)")
    ap.add_argument("--base", default="", help="đường dẫn con khi chạy sau IIS, vd /aqautotest")
    a = ap.parse_args()
    if a.data:
        DATA = Path(a.data).resolve()
        ASSETS = DATA / "assets"
    if a.local:
        LOCAL = Path(a.local).resolve()
        CFG_FILE = LOCAL / "config.json"
        CFG = load_cfg()
    MODE["public"] = a.public
    MODE["base"] = "/" + a.base.strip("/") if a.base.strip("/") else ""
    if not CFG_FILE.exists():
        save_cfg(CFG)
    if a.public:
        load_auth()
    host = a.host or ("0.0.0.0" if a.public else "127.0.0.1")
    srv = ThreadingHTTPServer((host, a.port), H)
    if a.cert:
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ctx.load_cert_chain(a.cert, a.key or None)
        srv.socket = ctx.wrap_socket(srv.socket, server_side=True, do_handshake_on_connect=False)
        MODE["https"] = True
    url = "%s://%s:%d/" % ("https" if a.cert else "http", "localhost" if host in ("127.0.0.1", "0.0.0.0") else host, a.port)
    print("AQ Autotest Console%s: %s   (Ctrl+C để dừng)" % (" (server, cần đăng nhập)" if a.public else "", url))
    print("Dữ liệu: %s   ·   Thư mục bộ test: %s" % (DATA, CFG.get("kitDir") or "(chưa khai báo)"))
    if not a.no_browser and not a.public:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

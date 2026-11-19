# -*- coding: utf-8 -*-
"""MCP của app AQ Auto Test – Claude Desktop trên máy người dùng đọc KB, đọc case ACS, ghi plan test nháp vào app.

Đường đi:  Claude Desktop ──stdio──▶ aq_mcp.py ──HTTP 127.0.0.1──▶ server.py POST api/mcp (file này)
                                                                   └─▶ ACS qua cầu nối của app Electron (AQ_ACS_RELAY, chỉ đọc)
Công cụ:
  kb_tim, kb_doc, kb_ghi, kb_phan_tich, kb_du_lieu   – knowledge base (vault Obsidian, thư mục kbDir hoặc kb/ cạnh server.py)
  acs_toi, acs_tim_case, acs_case                    – ACS CHỈ ĐỌC (phiên người dùng đã đăng nhập trong app); không có công cụ ghi lên ACS
  retest_ds, retest_doc_plan, retest_ghi_plan        – plan test NHÁP (collection retestDrafts) – người test duyệt trên trang Test sau sửa lỗi
An toàn: chỉ nghe 127.0.0.1 + token trong <local>/mcp.json; kb_ghi chỉ ghi .md trong thư mục KB, từ chối nội dung giống mật khẩu / token / chuỗi kết nối.
Chỉ thư viện chuẩn.
"""
import json, os, re, time, datetime, urllib.request, urllib.error
from pathlib import Path

import kb_graph

PROTO = "2025-06-18"
RT_COLS = ['case_id', 'title', 'school_code', 'module', 'case_type', 'priority', 'status', 'assignee_raw', 'analyst_raw', 'req_state',
           'tester_raw', 'test_state', 'received_at', 'due_date', 'resolved_at', 'changed']
GROUPS = {'prep': 'Chuẩn bị', 'repro': 'Tái hiện như KH', 'check': 'Kiểm tra theo yêu cầu KH', 'reg': 'Kiểm tra không ảnh hưởng'}
PLATFORMS = ('web', 'edusoft', 'app', 'api', 'report')
KINDS = ('ui', 'data', 'report', 'perm', 'add')
SECRET = re.compile(r'(mật\s*khẩu|password|passwd|pwd|token|secret|api[_\- ]?key)\s*[:=]\s*\S{4,}|data source\s*=|initial catalog\s*=|;\s*password\s*=', re.I)

INSTRUCTIONS = """Bạn đang nối với app AQ Auto Test (máy người test của AQTech) – kiểm thử phần mềm Edusoft.NET (Windows) và Netweb (cổng web SV/GV).
Khi được nhờ đọc / phân tích case ACS hoặc dựng plan test:
1. acs_case lấy nội dung case (lời khách hàng, BA, ghi chú coder, diễn biến). Không đọc được thì nhờ người dùng đăng nhập ACS trong app.
2. kb_phan_tich trên tiêu đề + lời khách hàng (+ menu nếu có) → dữ liệu case đụng tới, dữ liệu PHẢI CÓ TRƯỚC, dữ liệu / phân hệ BỊ ẢNH HƯỞNG.
   Đọc thêm ghi chú bằng kb_doc (Phan-he/<mã>.md, Du-lieu/<tên>.md, Cach-test/…, Truong/<mã trường>.md).
3. Chọn nơi test theo NGHIỆP VỤ, không theo mã phân hệ: sửa giao diện / hiển thị web → test trên web (không gán kịch bản Edusoft);
   sửa cách tính / lưu số liệu của dữ liệu tạo ở Edusoft → test trên Edusoft rồi kiểm nơi hiển thị; mẫu in → in / xuất trên bản test.
4. retest_ghi_plan ghi plan NHÁP vào app: prep = môi trường + dữ liệu phải có trước (ghi rõ menu tạo); repro = các bước khách hàng làm;
   check = mỗi yêu cầu của khách hàng một mục, viết thành điều kiện kiểm được; reg = dữ liệu / phân hệ bị ảnh hưởng cần kiểm lại.
   Báo người dùng mở trang Test sau sửa lỗi trong app để duyệt rồi bấm Nhận test.
Quy tắc: KHÔNG ghi gì lên ACS (không có công cụ ghi). Chỉ dùng môi trường test/demo, dữ liệu test có tiền tố AUTO… / TEST_….
Không ghi mật khẩu, token, chuỗi kết nối vào KB. Liên kết Netweb trong Truong/ là site THẬT – chỉ để nhận biết trường, không thao tác.
Sửa KB (kb_ghi) khi người dùng dạy kiến thức mới hoặc xác nhận / sửa một liên kết: giữ đúng Properties (can_co, tao_o, dung_o, tu_khoa…), viết tiếng Việt."""


def _s(o, n=None):
    return {"type": "string", "description": o} if n is None else {"type": "string", "description": o, "enum": n}


TOOLS = [
    {"name": "kb_tim", "description": "Tìm ghi chú trong knowledge base nghiệp vụ (vault Obsidian) theo từ khoá – trả đường dẫn, tiêu đề, dòng khớp.",
     "inputSchema": {"type": "object", "properties": {"tu_khoa": _s("từ khoá, vd 'học phí', 'đăng ký môn học', 'DHNT'"),
                                                      "gioi_han": {"type": "integer", "description": "số ghi chú tối đa (mặc định 12)"}}, "required": ["tu_khoa"]}},
    {"name": "kb_doc", "description": "Đọc nguyên văn một ghi chú KB, vd '00 Logic nghiệp vụ.md', 'Du-lieu/KQ DKMH.md', 'Phan-he/CSHP.md', 'Menu/DKMH.md'.",
     "inputSchema": {"type": "object", "properties": {"duong_dan": _s("đường dẫn tương đối trong KB, đuôi .md")}, "required": ["duong_dan"]}},
    {"name": "kb_ghi", "description": "Ghi / sửa một ghi chú KB (.md) – khi người dùng dạy kiến thức mới, xác nhận hoặc sửa liên kết. "
                                      "che_do 'thay' = thay toàn bộ nội dung, 'them' = thêm vào cuối. Giữ Properties ở đầu file. Không ghi mật khẩu/token.",
     "inputSchema": {"type": "object", "properties": {"duong_dan": _s("đường dẫn tương đối trong KB, đuôi .md"), "noi_dung": _s("nội dung Markdown"),
                                                      "che_do": _s("thay | them", ["thay", "them"])}, "required": ["duong_dan", "noi_dung"]}},
    {"name": "kb_phan_tich", "description": "Đọc một đoạn văn (tiêu đề + lời khách hàng + menu của case) theo bản đồ nghiệp vụ: dữ liệu case đụng tới, "
                                            "menu Edusoft khớp, dữ liệu PHẢI CÓ TRƯỚC (chuẩn bị test), dữ liệu / phân hệ BỊ ẢNH HƯỞNG (kiểm không ảnh hưởng).",
     "inputSchema": {"type": "object", "properties": {"van_ban": _s("tiêu đề + nội dung case"), "phan_he": _s("mã phân hệ của case trên ACS (vd CSHP) – tuỳ chọn")},
                     "required": ["van_ban"]}},
    {"name": "kb_du_lieu", "description": "Chi tiết một loại dữ liệu trong bản đồ (vd 'KQ DKMH', 'Học phí'): tạo ở đâu, phải có trước gì (cả chuỗi), là điều kiện cho gì, dùng ở phân hệ nào.",
     "inputSchema": {"type": "object", "properties": {"ten": _s("tên file trong Du-lieu/ hoặc tên dữ liệu")}, "required": ["ten"]}},
    {"name": "acs_toi", "description": "Tài khoản ACS (AQ Support Hub) đang đăng nhập trong app – kiểm tra kết nối.",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "acs_tim_case", "description": "Tìm case trên ACS (chỉ đọc). Không truyền dieu_kien = case 'Đã xử lý', chưa test đạt. "
                                            "dieu_kien: [{truong, phep: eq|neq|in, gia_tri}], truong là một trong: " + ", ".join(RT_COLS) + ".",
     "inputSchema": {"type": "object", "properties": {
         "dieu_kien": {"type": "array", "items": {"type": "object", "properties": {"truong": {"type": "string"}, "phep": {"type": "string", "enum": ["eq", "neq", "in"]},
                                                                                   "gia_tri": {"type": "string"}}, "required": ["truong", "phep", "gia_tri"]}},
         "gioi_han": {"type": "integer", "description": "tối đa (mặc định 50, tối đa 200)"}}}},
    {"name": "acs_case", "description": "Đọc đầy đủ một case ACS (chỉ đọc): các trường, lời khách hàng, BA, ghi chú coder, diễn biến.",
     "inputSchema": {"type": "object", "properties": {"ma_case": _s("mã case, vd 64501")}, "required": ["ma_case"]}},
    {"name": "retest_ds", "description": "Danh sách phiếu test sau sửa lỗi trong app (case, trạng thái, nền tảng, tiến độ) và các plan nháp Claude đã ghi.",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "retest_doc_plan", "description": "Đọc plan test của một case trong app: plan nháp (Claude ghi) và phiếu đang test (nếu đã nhận test).",
     "inputSchema": {"type": "object", "properties": {"ma_case": _s("mã case")}, "required": ["ma_case"]}},
    {"name": "retest_ghi_plan", "description": "Ghi plan test NHÁP cho một case vào app (trang Test sau sửa lỗi) – người test xem, sửa rồi bấm Nhận test. "
                                               "Không thay phiếu đã nhận test. nhom: prep (chuẩn bị: môi trường, dữ liệu phải có trước) | repro (tái hiện như KH) | "
                                               "check (mỗi yêu cầu KH một mục) | reg (không ảnh hưởng).",
     "inputSchema": {"type": "object", "properties": {
         "ma_case": _s("mã case"), "nen_tang": _s("nơi test", list(PLATFORMS)), "loai_sua": _s("ui=giao diện, data=xử lý/số liệu, report=mẫu in, perm=tài khoản/quyền, add=thêm chức năng", list(KINDS)),
         "moi_truong": _s("môi trường test, vd 'Edusoft bản test của trường KTTC – bản 2026.11J.18'"),
         "cac_muc": {"type": "array", "items": {"type": "object", "properties": {"nhom": {"type": "string", "enum": list(GROUPS)}, "noi_dung": {"type": "string"}},
                                                "required": ["nhom", "noi_dung"]}},
         "ly_do": _s("vì sao chọn nền tảng / các mục này (ngắn) – hiện cho người test")},
         "required": ["ma_case", "nen_tang", "cac_muc"]}},
]


class ToolError(Exception):
    pass


# ------------------------------------------------------------------ KB
def kb_dir(S):
    d = (S.CFG.get("kbDir") or "").strip()
    if d and Path(d).is_dir():
        return Path(d).resolve(), True
    p = S.ROOT / "kb"
    return p.resolve(), (S.ROOT / ".git").exists()       # repo: ghi được; bản app chưa chọn vault: chỉ đọc


def kb_path(S, rel, must_exist=True):
    base, _ = kb_dir(S)
    rel = str(rel or "").replace("\\", "/").strip().lstrip("/")
    if not rel.lower().endswith(".md") or ".." in rel.split("/") or rel.split("/")[0].startswith("."):
        raise ToolError("Đường dẫn ghi chú phải là file .md trong KB, vd 'Du-lieu/KQ DKMH.md'")
    p = (base / rel).resolve()
    if base not in p.parents:
        raise ToolError("Đường dẫn ra ngoài thư mục KB")
    if must_exist and not p.is_file():
        raise ToolError("Không có ghi chú " + rel + " – dùng kb_tim để tìm")
    return p


def t_kb_tim(S, a):
    base, _ = kb_dir(S)
    words = [w for w in re.split(r'\s+', str(a.get("tu_khoa") or "").lower().strip()) if w]
    if not words:
        raise ToolError("Cần từ khoá")
    lim = max(1, min(40, int(a.get("gioi_han") or 12)))
    res = []
    for f in base.rglob("*.md"):
        if any(x.startswith(".") for x in f.relative_to(base).parts):
            continue
        try:
            t = f.read_text("utf-8", errors="replace")
        except OSError:
            continue
        low, name = t.lower(), f.stem.lower()
        sc = sum(low.count(w) for w in words) + sum(5 for w in words if w in name)
        if f.relative_to(base).parts[0] == "Menu":
            sc = sc * 0.3                      # danh sách menu dài – xếp sau ghi chú dữ liệu / phân hệ
        if not sc or not all(w in low or w in name for w in words):
            continue
        lines = [ln.strip() for ln in t.split("\n") if any(w in ln.lower() for w in words) and not ln.startswith("---")][:3]
        res.append((sc, f.relative_to(base).as_posix(), lines))
    res.sort(key=lambda x: -x[0])
    return {"ket_qua": [{"duong_dan": r[1], "dong_khop": [x[:220] for x in r[2]]} for r in res[:lim]], "tong": len(res)}


def t_kb_doc(S, a):
    p = kb_path(S, a.get("duong_dan"))
    t = p.read_text("utf-8", errors="replace")
    return t if len(t) < 60000 else t[:60000] + "\n…(cắt bớt)"


def t_kb_ghi(S, a):
    base, writable = kb_dir(S)
    if not writable:
        raise ToolError("KB đang là bản chỉ đọc đi kèm app. Người dùng chọn thư mục vault Obsidian (thư mục kb của repo) ở app: "
                        "Test sau sửa lỗi → Thiết lập ACS → Kết nối Claude Desktop → Thư mục KB.")
    body = str(a.get("noi_dung") or "")
    if not body.strip():
        raise ToolError("Nội dung trống")
    if len(body) > 200000:
        raise ToolError("Nội dung quá dài")
    if SECRET.search(body):
        raise ToolError("Nội dung có vẻ chứa mật khẩu / token / chuỗi kết nối – không ghi vào KB (KB nằm trong git).")
    p = kb_path(S, a.get("duong_dan"), must_exist=False)
    mode = a.get("che_do") or "thay"
    p.parent.mkdir(parents=True, exist_ok=True)
    if mode == "them" and p.exists():
        cur = p.read_text("utf-8", errors="replace")
        body = cur.rstrip("\n") + "\n\n" + body.strip("\n") + "\n"
    elif not body.endswith("\n"):
        body += "\n"
    existed = p.exists()
    p.write_text(body, "utf-8")
    return {"ok": True, "duong_dan": p.relative_to(base).as_posix(), "tao_moi": not existed,
            "nhac": "Người dùng chạy dong-bo.bat để đưa thay đổi KB lên git cho máy khác."}


def _catalog(S):
    c = getattr(S, "_CAT", None)
    if c is None:
        try:
            c = json.loads((S.WEB / "edusoft-catalog.json").read_text("utf-8"))["menus"]
        except Exception:
            c = []
        S._CAT = c
    return c


def find_menu(S, text, mod):
    low = str(text or "").lower()
    best = None
    for m in _catalog(S):
        leaf = m["path"].split("/")[-1].strip().lower()
        ph = kb_graph.CAT_PH.get(m["ph"], m["ph"])
        if len(leaf) < 8 or leaf not in low or (mod and ph != mod and len(leaf) < 18):
            continue
        s = len(leaf) + (20 if mod and ph == mod else 0)
        if not best or s > best[0]:
            best = (s, {"ma": m["ma"], "phan_he": ph, "duong_dan": m["path"]})
    return best[1] if best else None


def _node(g, fn):
    d = g["data"][fn]
    return {"ten_file": fn, "ten": d["t"], "tao_o": d["src"], "menu_tao": d["menu"], "ghi_chu": "Du-lieu/" + fn + ".md"}


def t_kb_phan_tich(S, a):
    base, _ = kb_dir(S)
    g = kb_graph.build(base)
    mod = str(a.get("phan_he") or "").upper().strip()
    mod = kb_graph.CAT_PH.get(mod, mod)
    text = str(a.get("van_ban") or "")
    menu = find_menu(S, text, mod)
    hits = kb_graph.query_text(g, text + ("\n" + menu["duong_dan"].split("/")[-1] if menu else ""), mod)
    top = hits[0][1] if hits else 0
    focus = [h for h in hits if h[1] >= max(3, top * 0.6)][:3]
    F = [h[0] for h in focus]
    F = [x for x in F if not any(o != x and x in kb_graph.walk(g, o, True) for o in F)]
    guess = False
    if not F and mod:
        own = sorted([k for k, d in g["data"].items() if d["src"] == mod], key=lambda k: -g["data"][k]["lv"])
        F, guess = own[:1], bool(own)
    req, seen = [], set()
    for fn in F:
        for r, why in g["data"][fn]["req"]:
            if r not in F and r not in seen:
                seen.add(r)
                req.append(dict(_node(g, r), vi_sao=why, cho=fn))
    chain = []
    for fn in F:
        for x in kb_graph.walk(g, fn, True):
            if x not in F and x not in chain:
                chain.append(x)
    chain.sort(key=lambda x: (g["data"][x]["lv"], x))
    nxt = []
    for fn in F:
        for x in kb_graph.walk(g, fn, False):
            if x not in F and x not in nxt and any(r[0] == fn for r in g["data"][x]["req"]):
                nxt.append(x)
    uses = []
    for fn in F:
        for m, why in g["data"][fn]["use"]:
            if m != g["data"][fn]["src"] and not any(u["phan_he"] == m for u in uses):
                uses.append({"phan_he": m, "viec": why, "du_lieu": fn})
    mods = g["mods"]
    return {
        "phan_he": {"ma": mod, "ten": mods.get(mod, [""])[0], "test_tren": mods.get(mod, ["", []])[1]} if mod else None,
        "menu_khop": menu,
        "du_lieu_case": [dict(_node(g, fn), web=g["data"][fn]["web"]) for fn in F],
        "doan_theo_phan_he": guess,
        "phai_co_truoc": req,
        "chuoi_chuan_bi": [dict(_node(g, x)) for x in chain],
        "anh_huong_du_lieu": [dict(_node(g, x), lay_tu=[r[0] for r in g["data"][x]["req"] if r[0] in F]) for x in nxt],
        "anh_huong_phan_he": uses,
        "goi_y": "prep = môi trường + phai_co_truoc (ghi menu_tao); reg = anh_huong_du_lieu (nếu sửa số liệu) hoặc các trang web hiện cùng dữ liệu (nếu sửa giao diện web). "
                 "Đọc thêm Phan-he/<mã>.md và Cach-test/ trước khi chốt.",
    }


def t_kb_du_lieu(S, a):
    base, _ = kb_dir(S)
    g = kb_graph.build(base)
    q = str(a.get("ten") or "").strip()
    fn = q if q in g["data"] else next((k for k, d in g["data"].items() if q.lower() in (k + " " + d["t"]).lower()), None)
    if not fn:
        raise ToolError("Không thấy dữ liệu '" + q + "'. Có: " + ", ".join(sorted(g["data"])))
    d = g["data"][fn]
    return dict(_node(g, fn), tang=d["lv"], tren_web=d["web"], phai_co_truoc=[{"ten_file": r, "vi_sao": w} for r, w in d["req"]],
                chuoi_chuan_bi=kb_graph.walk(g, fn, True), la_dieu_kien_cho=[k for k, x in g["data"].items() if any(r[0] == fn for r in x["req"])],
                sinh_ra_ve_sau=kb_graph.walk(g, fn, False), dung_o=[{"phan_he": m, "viec": w} for m, w in d["use"]])


# ------------------------------------------------------------------ ACS (chỉ đọc, qua cầu nối của app)
def acs(method, path, body=None):
    url, tok = os.environ.get("AQ_ACS_RELAY"), os.environ.get("AQ_ACS_TOKEN")
    if not url or not tok:
        raise ToolError("Đọc ACS chỉ có khi chạy trong app AQ Auto Test (máy cá nhân).")
    req = urllib.request.Request(url.rstrip("/") + "/acs", data=json.dumps({"method": method, "path": path, "body": body}).encode("utf-8"),
                                 headers={"Content-Type": "application/json", "X-AQ-Token": tok}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            res = json.loads(r.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as e:
        raise ToolError("Cầu nối ACS từ chối: " + e.read().decode("utf-8", errors="replace")[:300])
    except OSError as e:
        raise ToolError("Không gọi được cầu nối ACS của app: %s" % e)
    if res.get("error"):
        raise ToolError(res["error"])
    if res.get("status") in (401, 403):
        raise ToolError("Chưa đăng nhập ACS – mở app AQ Auto Test → Test sau sửa lỗi → bấm Đăng nhập ACS, rồi thử lại.")
    return res


def html_text(v):
    v = str(v or "")
    if not re.search(r'<[a-z!/][^>]*>', v, re.I):
        return v.strip()
    v = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', v)
    v = re.sub(r'(?i)<br\s*/?>|</(p|div|li|tr|h\d)>', '\n', v)
    v = re.sub(r'<[^>]+>', ' ', v)
    for k, x in (("&nbsp;", " "), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&#39;", "'"), ("&amp;", "&")):
        v = v.replace(k, x)
    return re.sub(r'[ \t]+', ' ', re.sub(r'\n\s*\n+', '\n\n', v)).strip()


def _flat(o, pre="", dep=0, out=None):
    out = {} if out is None else out
    if isinstance(o, dict) and dep <= 2:
        for k, v in o.items():
            if re.search(r'pass|token|secret|cookie', k, re.I):
                continue
            _flat(v, (pre + "." + k) if pre else k, dep + 1, out)
    elif isinstance(o, list):
        if o and all(not isinstance(x, (dict, list)) for x in o):
            out[pre] = ", ".join(str(x) for x in o)
    elif o is not None and o != "":
        t = html_text(o) if isinstance(o, str) else str(o)
        if t:
            out[pre] = t[:8000]
    return out


def acs_settings(S):
    f = S.doc_file("settings", "acs")
    return (S.read_doc(f) if f.exists() else None) or {}


def t_acs_toi(S, a):
    r = acs("GET", "/auth/me")
    d = r.get("data") or {}
    return {"ten": d.get("display_name") or d.get("username"), "tai_khoan": d.get("username")}


def t_acs_tim_case(S, a):
    cl = [{"op": c.get("phep"), "conj": "AND", "field": c.get("truong"), "value": c.get("gia_tri")} for c in (a.get("dieu_kien") or [])]
    for c in cl:
        if c["field"] not in RT_COLS or c["op"] not in ("eq", "neq", "in"):
            raise ToolError("Điều kiện không hợp lệ: %s" % c)
    if not cl:
        cl = [{"op": "eq", "conj": "AND", "field": "status", "value": "Đã xử lý"}, {"op": "neq", "conj": "AND", "field": "test_state", "value": "Đúng"}]
    lim = max(1, min(200, int(a.get("gioi_han") or 50)))
    r = acs("POST", "/cs/query", {"clauses": cl, "columns": RT_COLS, "sort": "case_id", "desc": True, "offset": 0, "limit": lim})
    d = r.get("data") or {}
    rows = d.get("rows") if isinstance(d, dict) else d
    if r.get("status") != 200 or not isinstance(rows, list):
        raise ToolError("ACS trả về mã %s" % r.get("status"))
    keep = ("case_id", "title", "school_code", "module", "status", "test_state", "assignee_raw", "tester_raw", "resolved_at", "due_date", "priority")
    return {"tong": d.get("total", len(rows)) if isinstance(d, dict) else len(rows), "case": [{k: x.get(k) for k in keep if x.get(k) not in (None, "")} for x in rows]}


def t_acs_case(S, a):
    cid = str(a.get("ma_case") or "").strip()
    if not re.match(r'^\d{1,10}$', cid):
        raise ToolError("Mã case phải là số")
    st = acs_settings(S)
    paths = [st["casePath"]] if st.get("casePath") else ["/cs/cases/{id}", "/cs/case/{id}", "/cs/cases/{id}/detail"]
    det, last = None, None
    for p in paths:
        r = acs("GET", p.replace("{id}", cid))
        last = r.get("status")
        if r.get("status") == 200 and isinstance(r.get("data"), dict):
            det = r["data"]
            break
    if det is None:
        raise ToolError("Không đọc được chi tiết case %s (mã %s). Quản trị khai báo 'đường dẫn API chi tiết case' ở tab Thiết lập ACS." % (cid, last))
    hist = []
    try:
        h = acs("GET", "/cs/cases/%s/history" % cid)
        hd = h.get("data")
        hl = hd.get("history") if isinstance(hd, dict) else hd
        for x in (hl or [])[:40]:
            if isinstance(x, dict):
                hist.append({"luc": x.get("changed_at"), "boi": x.get("changed_by"), "thay_doi": _flat(x.get("changes") or {})})
    except ToolError:
        pass
    return {"ma_case": cid, "truong": _flat(det), "dien_bien": hist,
            "nhac": "Lời khách hàng thường ở trường customer/description/content; ghi chú coder ở dev_comment/resolution. Không ghi gì lên ACS."}


# ------------------------------------------------------------------ plan test nháp
def latest_retest(S, cid):
    best = None
    for x in S.list_docs("retests"):
        d = x["data"]
        if str(d.get("caseId")) == cid and (best is None or (d.get("round") or 1) > (best["data"].get("round") or 1)):
            best = x
    return best


def t_retest_ds(S, a):
    seen = {}
    for x in S.list_docs("retests"):
        d = x["data"]
        k = str(d.get("caseId"))
        if k not in seen or (d.get("round") or 1) > (seen[k].get("round") or 1):
            seen[k] = d
    items = []
    for k, d in sorted(seen.items(), key=lambda kv: str(kv[1].get("updatedAt") or ""), reverse=True)[:80]:
        it = (d.get("plan") or {}).get("items") or []
        items.append({"ma_case": k, "tieu_de": d.get("title"), "truong": d.get("school"), "phan_he": d.get("module"), "trang_thai": d.get("state"),
                      "nen_tang": d.get("platform"), "lan": d.get("round"), "da_test": sum(1 for i in it if i.get("res")), "so_muc": len(it)})
    drafts = [{"ma_case": str(x["data"].get("caseId")), "luc": x["data"].get("updatedAt"), "so_muc": len(x["data"].get("items") or [])}
              for x in S.list_docs("retestDrafts")]
    return {"phieu": items, "plan_nhap": drafts}


def t_retest_doc_plan(S, a):
    cid = str(a.get("ma_case") or "").strip()
    f = S.doc_file("retestDrafts", "c" + cid)
    cur = latest_retest(S, cid)
    return {"plan_nhap": S.read_doc(f) if f.exists() else None, "phieu": cur["data"] if cur else None}


def t_retest_ghi_plan(S, a):
    cid = str(a.get("ma_case") or "").strip()
    if not re.match(r'^\d{1,10}$', cid):
        raise ToolError("Mã case phải là số")
    pf, kind = a.get("nen_tang"), a.get("loai_sua") or ""
    if pf not in PLATFORMS:
        raise ToolError("nen_tang phải là một trong " + ", ".join(PLATFORMS))
    if kind and kind not in KINDS:
        raise ToolError("loai_sua phải là một trong " + ", ".join(KINDS))
    items = []
    for x in a.get("cac_muc") or []:
        g, t = x.get("nhom"), re.sub(r'\s+', ' ', str(x.get("noi_dung") or "")).strip()
        if g not in GROUPS or not t:
            continue
        items.append({"g": g, "t": t[:800]})
    if not any(i["g"] == "check" for i in items):
        raise ToolError("Plan cần ít nhất một mục nhom='check' (kiểm tra theo yêu cầu khách hàng).")
    if len(items) > 40:
        raise ToolError("Tối đa 40 mục")
    order = list(GROUPS)
    items.sort(key=lambda i: order.index(i["g"]))
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    doc = {"caseId": cid, "platform": pf, "kind": kind, "env": str(a.get("moi_truong") or "")[:400], "items": items,
           "why": str(a.get("ly_do") or "")[:1200], "by": "claude", "at": now, "updatedAt": now}
    with S.LOCK:
        S.write_doc(S.doc_file("retestDrafts", "c" + cid), doc)
    cur = latest_retest(S, cid)
    note = "Đã ghi plan nháp cho case #%s (%d mục). Người test mở app → Test sau sửa lỗi → chọn case #%s → bước 2 Plan test để duyệt rồi Nhận test." % (cid, len(items), cid)
    if cur and cur["data"].get("state") in ("testing", "queued", "running", "review"):
        note += " Lưu ý: case đang có phiếu test (" + str(cur["data"].get("state")) + ") – plan nháp không thay phiếu đang test; nói người test đối chiếu và sửa plan của phiếu nếu cần."
    return {"ok": True, "thong_bao": note}


HANDLERS = {"kb_tim": t_kb_tim, "kb_doc": t_kb_doc, "kb_ghi": t_kb_ghi, "kb_phan_tich": t_kb_phan_tich, "kb_du_lieu": t_kb_du_lieu,
            "acs_toi": t_acs_toi, "acs_tim_case": t_acs_tim_case, "acs_case": t_acs_case,
            "retest_ds": t_retest_ds, "retest_doc_plan": t_retest_doc_plan, "retest_ghi_plan": t_retest_ghi_plan}


# ------------------------------------------------------------------ JSON-RPC
def handle(S, msg, version=""):
    if isinstance(msg, list):
        out = [r for r in (handle(S, m, version) for m in msg) if r is not None]
        return out or None
    if not isinstance(msg, dict):
        return {"jsonrpc": "2.0", "id": None, "error": {"code": -32600, "message": "Invalid Request"}}
    mid, method, p = msg.get("id"), msg.get("method"), msg.get("params") or {}
    if mid is None:                       # thông báo (notifications/initialized…)
        return None

    def ok(res):
        return {"jsonrpc": "2.0", "id": mid, "result": res}
    if method == "initialize":
        return ok({"protocolVersion": p.get("protocolVersion") or PROTO, "capabilities": {"tools": {"listChanged": False}},
                   "serverInfo": {"name": "aq-auto-test", "title": "AQ Auto Test", "version": version or "dev"}, "instructions": INSTRUCTIONS})
    if method == "ping":
        return ok({})
    if method == "tools/list":
        return ok({"tools": TOOLS})
    if method == "tools/call":
        name, args = p.get("name"), p.get("arguments") or {}
        fn = HANDLERS.get(name)
        if not fn:
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": "Không có công cụ " + str(name)}}
        try:
            res = fn(S, args)
            txt = res if isinstance(res, str) else json.dumps(res, ensure_ascii=False, indent=1)
            return ok({"content": [{"type": "text", "text": txt}], "isError": False})
        except ToolError as e:
            return ok({"content": [{"type": "text", "text": str(e)}], "isError": True})
        except Exception as e:            # lỗi bất ngờ: báo gọn, không lộ đường dẫn máy
            return ok({"content": [{"type": "text", "text": "Lỗi khi chạy %s: %s" % (name, type(e).__name__)}], "isError": True})
    return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": "Method not found: " + str(method)}}


def write_conn_file(S, port):
    """<local>/mcp.json (địa chỉ + token cho aq_mcp.py) và mcp-tools.json (danh sách công cụ khi app chưa mở)."""
    import secrets
    tok = secrets.token_urlsafe(24)
    S.LOCAL.mkdir(parents=True, exist_ok=True)
    f = S.LOCAL / "mcp.json"
    f.write_text(json.dumps({"url": "http://127.0.0.1:%d%s/api/mcp" % (port, S.MODE["base"]), "token": tok, "pid": os.getpid(),
                             "at": time.strftime("%Y-%m-%d %H:%M:%S")}, ensure_ascii=False), "utf-8")
    try:
        os.chmod(f, 0o600)
    except OSError:
        pass
    (S.LOCAL / "mcp-tools.json").write_text(json.dumps({"tools": TOOLS, "instructions": INSTRUCTIONS}, ensure_ascii=False), "utf-8")
    return tok

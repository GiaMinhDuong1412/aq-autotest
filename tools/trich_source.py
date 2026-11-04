#!/usr/bin/env python3
"""Trích tên điều khiển / caption / câu thông báo từ source Edusoft (chạy trên máy có source, chỉ thư viện chuẩn).

Đọc thẳng file .zip (không cần giải nén) hoặc thư mục source. Chỉ đọc *.cs và *.resx; bỏ qua *.config,
bỏ chuỗi giống chuỗi kết nối / mật khẩu. Kết quả là file .txt nhỏ – gửi file đó cho Claude, KHÔNG gửi source.

Cách dùng (PowerShell, trong thư mục repo aq-autotest):
  python tools\\trich_source.py D:\\Source.NET.zip --liet-ke                  -> trich-danh-sach-form.txt
  python tools\\trich_source.py D:\\Source.NET.zip "sinh vien hoc ky"         -> trich-sinh-vien-hoc-ky.txt
  python tools\\trich_source.py D:\\Source.NET.zip --tim "Xóa dữ liệu thành công"
  python tools\\trich_source.py D:\\Source.NET.zip --tat-ca                    -> trich-tat-ca.zip (mọi module)
Từ khóa so khớp không dấu, không phân biệt hoa thường, với đường dẫn file, tên lớp hoặc tiêu đề form.
"""
import argparse
import os
import re
import sys
import unicodedata
import zipfile

BO_QUA = re.compile(r"password|passwd|pwd\s*=|connectionstring|data source=|initial catalog|user id=|"
                    r"server=|smtp|apikey|api_key|secret|token", re.I)
STR = r'"((?:[^"\\\r\n]|\\.)*)"'
RE_DECL = re.compile(r"this\.(\w+)\s*=\s*new\s+([\w\.]+)\s*\(")
RE_PROP = re.compile(r"this\.(\w+)\.(?:Properties\.)?(Text|Caption|NullText|NullValuePrompt|ToolTip|Hint|"
                     r"FieldName|CustomizationFormText)\s*=\s*" + STR)
RE_FORM_TEXT = re.compile(r"this\.Text\s*=\s*" + STR)
RE_RES = re.compile(r"this\.(\w+)\.(Text|Caption)\s*=\s*resources\.GetString\(\"([^\"]+)\"\)")
RE_APPLY = re.compile(r"resources\.ApplyResources\(this\.(\w+),\s*\"([^\"]+)\"\)")
RE_ADD = re.compile(r"this\.(\w+)\.Controls\.Add\(this\.(\w+)\)")
RE_LCI = re.compile(r"this\.(\w+)\.Control\s*=\s*this\.(\w+)\s*;")
RE_COLS = re.compile(r"this\.(\w+)\.Columns\.AddRange\(new [\w\.]+\[\]\s*\{([^}]*)\}", re.S)
RE_MAINVIEW = re.compile(r"this\.(\w+)\.MainView\s*=\s*this\.(\w+)")
RE_CLASS = re.compile(r"partial\s+class\s+(\w+)(?:\s*:\s*([\w\.]+))?")
RE_LIT = re.compile(STR)
RE_RESX = re.compile(r'<data name="([^"]+)"[^>]*>\s*<value>(.*?)</value>', re.S)


def khong_dau(s):
    s = unicodedata.normalize("NFD", s.replace("đ", "d").replace("Đ", "D"))
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


def giai_ma(b):
    for enc in ("utf-8-sig", "cp1258", "cp1252"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            pass
    return b.decode("utf-8", "replace")


class Nguon:
    """Đọc file từ zip hoặc thư mục, chỉ *.cs / *.resx."""

    def __init__(self, duong_dan):
        self.zip = None
        if os.path.isdir(duong_dan):
            self.goc = duong_dan
            self.ds = []
            for r, _, fs in os.walk(duong_dan):
                for f in fs:
                    p = os.path.relpath(os.path.join(r, f), duong_dan).replace("\\", "/")
                    self.ds.append(p)
        else:
            self.zip = zipfile.ZipFile(duong_dan)
            self.ds = [n for n in self.zip.namelist() if not n.endswith("/")]
        self.ds = [p for p in self.ds if p.lower().endswith((".cs", ".resx"))]
        self.co = set(self.ds)

    def doc(self, p):
        if p not in self.co:
            return None
        if self.zip:
            return giai_ma(self.zip.read(p))
        with open(os.path.join(self.goc, p), "rb") as f:
            return giai_ma(f.read())

    def designers(self):
        return [p for p in self.ds if p.lower().endswith(".designer.cs")]


def an_toan(s):
    return not BO_QUA.search(s)


def thong_tin_form(nguon, p):
    src = nguon.doc(p) or ""
    m = RE_CLASS.search(src)
    lop, cha = (m.group(1), m.group(2) or "") if m else (os.path.basename(p), "")
    if not cha:  # lớp cha thường khai ở file .cs, không ở .Designer.cs
        code = nguon.doc(re.sub(r"\.designer\.cs$", ".cs", p, flags=re.I)) or ""
        m2 = re.search(r"partial\s+class\s+" + re.escape(lop) + r"\s*:\s*([\w\.]+)", code)
        cha = m2.group(1) if m2 else ""
    t = RE_FORM_TEXT.search(src)
    return src, lop, cha, (t.group(1) if t else "")


def trich_form(nguon, p, out):
    src, lop, cha, tieu_de = thong_tin_form(nguon, p)
    goc = re.sub(r"\.designer\.cs$", "", p, flags=re.I)
    resx = {}
    rx = nguon.doc(goc + ".resx")
    if rx:
        for k, v in RE_RESX.findall(rx):
            if k.endswith((".Text", ".Caption")) and v.strip() and an_toan(v):
                resx[k] = v.strip()
    loai = {n: t.split(".")[-1] for n, t in RE_DECL.findall(src)}
    props = {}
    for n, k, v in RE_PROP.findall(src):
        if v and an_toan(v):
            props.setdefault(n, {})[k] = v
    for n, k, key in RE_RES.findall(src):
        if key in resx:
            props.setdefault(n, {})[k] = resx[key]
    for n, key in RE_APPLY.findall(src):
        for k in ("Text", "Caption"):
            if key + "." + k in resx:
                props.setdefault(n, {})[k] = resx[key + "." + k]
    cha_cua = {con: ch for ch, con in RE_ADD.findall(src)}
    nhan_cua = {}
    for lci, ctl in RE_LCI.findall(src):
        txt = props.get(lci, {}).get("Text") or props.get(lci, {}).get("CustomizationFormText")
        if txt:
            nhan_cua[ctl] = txt
    cot_cua = {v: re.findall(r"this\.(\w+)", ds) for v, ds in RE_COLS.findall(src)}
    view_cua = dict(RE_MAINVIEW.findall(src))
    la_cot = {c for cs in cot_cua.values() for c in cs}

    out.append("=" * 100)
    out.append(f"FORM {lop}  (kế thừa {cha or '?'})  file {p}")
    if tieu_de:
        out.append(f"  Tiêu đề: {tieu_de}")
    out.append("  -- Điều khiển (tên | loại | nhãn/caption | thuộc vùng) --")
    for n, t in loai.items():
        if n in la_cot or t in ("GridColumn", "BandedGridColumn", "LayoutControlItem", "EmptySpaceItem",
                                "SplitterItem", "LayoutControlGroup"):
            continue
        pr = props.get(n, {})
        nhan = nhan_cua.get(n) or pr.get("Text") or pr.get("Caption") or ""
        them = []
        if pr.get("NullText") or pr.get("NullValuePrompt"):
            them.append("gợi ý=" + (pr.get("NullText") or pr.get("NullValuePrompt")))
        if pr.get("ToolTip") or pr.get("Hint"):
            them.append("tooltip=" + (pr.get("ToolTip") or pr.get("Hint")))
        vung = cha_cua.get(n, "")
        out.append(f"  {n} | {t} | {nhan}" + (f" | {vung}" if vung else "") + (" | " + "; ".join(them) if them else ""))
    for grid, view in view_cua.items():
        cols = cot_cua.get(view, [])
        if not cols:
            continue
        out.append(f"  -- Lưới {grid} (view {view}) – cột: caption [FieldName] --")
        for c in cols:
            pr = props.get(c, {})
            out.append(f"    {c}: {pr.get('Caption', '')} [{pr.get('FieldName', '')}]")
    for view, cols in cot_cua.items():
        if view in view_cua.values():
            continue
        out.append(f"  -- Cột của {view}: caption [FieldName] --")
        for c in cols:
            pr = props.get(c, {})
            out.append(f"    {c}: {pr.get('Caption', '')} [{pr.get('FieldName', '')}]")
    code = nguon.doc(goc + ".cs")
    if code:
        out.append("  -- Câu thông báo / chuỗi tiếng Việt trong " + goc + ".cs (dòng: chuỗi) --")
        for i, dong in enumerate(code.splitlines(), 1):
            if BO_QUA.search(dong):
                continue
            for s in RE_LIT.findall(dong):
                if len(s) >= 3 and (any(ord(c) > 127 for c in s) or "Show(" in dong or "Message" in dong):
                    out.append(f"    {i}: {s}")

CONG_CU = {"Setup", "Test", "ToolPortable", "ReleaseTools", "ToolTrienKhai"}


def module_cua(p):
    parts = p.split("/")
    for x in parts[:-1]:
        if x.startswith("Edusoft.") or x == "AQDataTools":
            return x
    return parts[1] if len(parts) > 2 and parts[0].lower().startswith("trunk") else parts[0]


def trich_tat_ca(nguon, thu_muc, ca_cong_cu=False):
    """Mỗi module 1 file <module>.txt (các form) + <module>-thong-bao.txt (chuỗi tiếng Việt ngoài form), rồi nén zip."""
    os.makedirs(thu_muc, exist_ok=True)
    forms, le = {}, {}
    co_form = {re.sub(r"\.designer\.cs$", ".cs", p, flags=re.I).lower() for p in nguon.designers()}
    for p in nguon.ds:
        m = module_cua(p)
        if m in CONG_CU and not ca_cong_cu:
            continue
        pl = p.lower()
        if pl.endswith(".designer.cs"):
            forms.setdefault(m, []).append(p)
        elif pl.endswith(".cs") and pl not in co_form and "/obj/" not in pl and not pl.endswith("assemblyinfo.cs"):
            le.setdefault(m, []).append(p)
    files = []
    for m in sorted(set(forms) | set(le)):
        out = [f"# Module {m}: {len(forms.get(m, []))} form"]
        for p in sorted(forms.get(m, [])):
            trich_form(nguon, p, out)
        tb = []
        for p in sorted(le.get(m, [])):
            dong_file = []
            for i, dong in enumerate((nguon.doc(p) or "").splitlines(), 1):
                if BO_QUA.search(dong) or dong.lstrip().startswith("//"):
                    continue
                for x in RE_LIT.findall(dong):
                    if len(x) >= 3 and any(ord(c) > 127 for c in x):
                        dong_file.append(f"    {i}: {x}")
            if dong_file:
                tb.append(f"== {p}")
                tb.extend(dong_file)
        for ten, noi_dung in ((m + ".txt", out), (m + "-thong-bao.txt", tb)):
            if len(noi_dung) > (1 if ten == m + ".txt" else 0):
                fp = os.path.join(thu_muc, ten)
                with open(fp, "w", encoding="utf-8") as f:
                    f.write("\n".join(noi_dung) + "\n")
                files.append(fp)
                print(f"  {ten}: {os.path.getsize(fp) // 1024} KB")
    zp = thu_muc.rstrip("/\\") + ".zip"
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for fp in files:
            z.write(fp, os.path.basename(fp))
    print(f"Đã nén {len(files)} file vào {os.path.abspath(zp)} ({os.path.getsize(zp) // 1024} KB) – gửi file zip này cho Claude.")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Trích tên điều khiển / caption / thông báo từ source Edusoft.")
    ap.add_argument("nguon", help="file .zip source hoặc thư mục source")
    ap.add_argument("tu_khoa", nargs="*", help="từ khóa tên form / tiêu đề (không dấu cũng được)")
    ap.add_argument("--liet-ke", action="store_true", help="liệt kê mọi form: file | lớp | tiêu đề")
    ap.add_argument("--tim", help="tìm chuỗi (câu thông báo, caption) trong toàn bộ *.cs / *.resx")
    ap.add_argument("--toi-da", type=int, default=30, help="số form tối đa khi trích (mặc định 30)")
    ap.add_argument("--tat-ca", action="store_true", help="trích mọi module, mỗi module 1 file, nén thành trich-tat-ca.zip")
    ap.add_argument("--ca-cong-cu", action="store_true", help="--tat-ca gồm cả Setup/Test/Tool… (mặc định bỏ)")
    ap.add_argument("-o", "--ra", help="file kết quả (.txt; với --tat-ca là thư mục)")
    a = ap.parse_args()

    nguon = Nguon(a.nguon)
    out = []
    if a.tat_ca:
        return trich_tat_ca(nguon, a.ra or "trich-tat-ca", a.ca_cong_cu)
    if a.tim:
        k = khong_dau(a.tim)
        for p in nguon.ds:
            for i, dong in enumerate((nguon.doc(p) or "").splitlines(), 1):
                if k in khong_dau(dong) and not BO_QUA.search(dong):
                    out.append(f"{p}:{i}: {dong.strip()[:300]}")
        ten = "trich-tim-" + re.sub(r"\W+", "-", k).strip("-")[:40] + ".txt"
    elif a.liet_ke or not a.tu_khoa:
        for p in sorted(nguon.designers()):
            _, lop, cha, td = thong_tin_form(nguon, p)
            out.append(f"{p} | {lop} | {cha} | {td}")
        ten = "trich-danh-sach-form.txt"
    else:
        k = khong_dau(" ".join(a.tu_khoa))
        khop = []
        for p in nguon.designers():
            _, lop, _, td = thong_tin_form(nguon, p)
            if k in khong_dau(p) or k in khong_dau(lop) or k in khong_dau(td) or \
                    k.replace(" ", "") in khong_dau(lop + " " + p).replace(" ", ""):
                khop.append(p)
        if not khop:
            print("Không thấy form nào khớp. Chạy --liet-ke để xem danh sách.")
            return 1
        if len(khop) > a.toi_da:
            out.append(f"!! {len(khop)} form khớp, chỉ trích {a.toi_da} form đầu – thu hẹp từ khóa hoặc tăng --toi-da.")
        for p in sorted(khop)[: a.toi_da]:
            trich_form(nguon, p, out)
        ten = "trich-" + re.sub(r"\W+", "-", k).strip("-")[:40] + ".txt"
    ra = a.ra or ten
    with open(ra, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"Đã ghi {len(out)} dòng vào {os.path.abspath(ra)} ({os.path.getsize(ra) // 1024} KB) – gửi file này cho Claude.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

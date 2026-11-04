#!/usr/bin/env python3
"""Lập danh mục menu → màn hình → cột/ô nhập/nút của Edusoft.NET từ các CSV do tools/doc_aqdata.py xuất (bảng AQ…).

  python tools/lap_danh_muc.py <thư mục aqdata> [--lien-ket trich-ma-view.txt] [--ra .claude/skills/giaodien-edusoft/man-hinh]

Kết quả: mỗi phân hệ một file <MaPhanHe>.md (menu theo đúng đường dẫn hiện trên Edusoft + các màn hình/lưới của phân hệ)
và index.md. Đường dẫn menu dùng tên viết tắt (VtPhanHe / VtChucNang) – đúng chữ hiện trên ribbon/cây chức năng,
viết thẳng vào lệnh `menu:` được. «Tiêu đề lưới» = chữ sau `@` trong lệnh (AQValSetV1 1/14); cột lưới = nhãn đã đổi
(AQValSetV1 2/14) hoặc AQDmField.Tenlabel; ô nhập trên form sửa = #MaField.
Đây là cấu hình gốc của AQ; trường (HVNG) có thể chỉnh lại bằng các bảng H… (HFieldView2, HFieldEdit, HMenuCustom…).
"""
import argparse
import collections
import csv
import glob
import os
import re
import sys

csv.field_size_limit(10 ** 9)

TAT = [("NoneInsert", "Thêm"), ("NoneSua", "Sửa"), ("NoneDelete", "Xóa"), ("NoneImport", "Import"),
       ("NoneExport", "Xuất"), ("NonePrint", "In"), ("NoneRefresh", "Nạp lại"), ("NoneDoiMa", "Đổi mã"),
       ("NoneGopMa", "Gộp mã"), ("NoneEditL", "Sửa trên lưới"), ("NoneEditR", "Sửa bên phải"), ("NoneQuit", "Thoát")]
KIEU_O = {"4": "ngày", "13": "nút …", "7": "chọn", "3": "số"}  # suy từ dữ liệu (NgayLapQDSV=4, MaLopMoi=13…)


def doc(thu_muc, so):
    f = glob.glob(os.path.join(thu_muc, f"aq.data{so}-*.csv"))
    if not f:
        raise SystemExit(f"Thiếu file aq.data{so}-*.csv trong {thu_muc}")
    with open(f[0], encoding="utf-8-sig") as r:
        return list(csv.DictReader(r))


def main():
    ap = argparse.ArgumentParser(description="Lập danh mục màn hình Edusoft từ CSV bảng AQ…")
    ap.add_argument("aqdata", help="thư mục CSV do doc_aqdata.py xuất")
    ap.add_argument("--lien-ket", help="file do trich_source.py --ma-view xuất (lớp màn hình → MaView1)")
    ap.add_argument("--ra", default="man-hinh", help="thư mục kết quả")
    a = ap.parse_args()

    ph = {r["IDPhanHe"]: r for r in doc(a.aqdata, "047")}
    cn = {r["IDChucNang"]: r for r in doc(a.aqdata, "027")}
    fm = {r["IDForm"]: r for r in doc(a.aqdata, "083")}
    v1 = {r["IDView1"]: r for r in doc(a.aqdata, "046")}
    fl = {r["IDFile"]: r for r in doc(a.aqdata, "001")}
    fd = {r["IDField"]: r for r in doc(a.aqdata, "002")}
    views = collections.defaultdict(list)
    for r in doc(a.aqdata, "059"):
        views[r["IDView1"]].append(r)
    fv = collections.defaultdict(list)
    for r in doc(a.aqdata, "055"):
        fv[r["IDView"]].append(r)
    thu_tu = {r["IDFieldView"]: r for r in doc(a.aqdata, "077")}
    sua = {r["IDFieldView"]: r for r in doc(a.aqdata, "030")}
    # AQValSetV/AQValSetV1: cài đặt hiển thị; (1,14) = tiêu đề lưới, (2,14) = nhãn cột đã đổi
    vs1 = collections.defaultdict(dict)
    for r in doc(a.aqdata, "042"):
        vs1[r["IDValSetV"]][(r["Index1"], r["Index2"])] = r["GiaTri"]
    tieu_de, nhan_cot = {}, {}
    for r in doc(a.aqdata, "039"):
        g = vs1.get(r["IDValSetV"], {})
        if not r["IDFieldView"] and g.get(("1", "14")):
            tieu_de[r["IDView"]] = g[("1", "14")].strip()
        if r["IDFieldView"] and g.get(("2", "14")):
            nhan_cot[r["IDFieldView"]] = g[("2", "14")].strip()
    nut = collections.defaultdict(list)
    for r in doc(a.aqdata, "053"):
        nut[r["IDView"]].append(r)

    # lớp màn hình → các MaView1 (từ source), để nối menu với màn hình
    lop_view = collections.defaultdict(list)
    ma_v1 = {r["MaView1"].lower(): r for r in v1.values()}
    if a.lien_ket:
        with open(a.lien_ket, encoding="utf-8") as r:
            for dong in r:
                p = [x.strip() for x in dong.split("|")]
                if len(p) >= 3 and p[2].lower() in ma_v1 and p[2] not in lop_view[p[1]]:
                    lop_view[p[1]].append(p[2])

    def ten(r):
        return (r.get("VtChucNang") or r.get("TenChucNang") or "").strip()

    def duong_dan(r):
        p, da = [], set()
        while r and r["IDChucNang"] not in da:
            da.add(r["IDChucNang"])
            p.append(ten(r))
            cha = r["IDChucNangParent"]
            if cha in ph:
                return cha, "/ ".join(reversed(p))
            r = cn.get(cha)
        return None, "/ ".join(reversed(p))

    def nhom_ph(idph):
        return ph[idph]["MaPhanHe"] if idph in ph else "KHAC"

    menu = collections.defaultdict(list)
    for r in cn.values():
        idph, dd = duong_dan(r)
        f = fm.get(r["iddoituong"])
        lop = f["FormRun"].split(",")[0].strip() if f else ""
        menu[nhom_ph(idph)].append((dd, r, f, lop))

    man = collections.defaultdict(list)
    for r in v1.values():
        man[nhom_ph(r["IDPHChinh"])].append(r)

    def mo_ta_view(r1):
        out = [f"### {r1['MaView1']} – {r1['TenView1'].strip()}"]
        for i, v in enumerate(sorted(views[r1["IDView1"]], key=lambda x: x["IDView"]), 1):
            tat = [t for k, t in TAT if v.get(k) == "1"]
            bang = fl.get(v["MainTable"], {}).get("MaFile", "")
            td = tieu_de.get(v["IDView"])
            out.append(f"- Lưới {i}" + (f" «{td}»" if td else "") + (f" (bảng {bang})" if bang else "") + (f"; tắt: {', '.join(tat)}" if tat else ""))
            cot, an, o_sua = [], [], []
            ds = sorted(fv[v["IDView"]], key=lambda x: (int(float(thu_tu.get(x["IDFieldView"], {}).get("TabOrder") or 9999)),
                                                         fd.get(x["IDField"], {}).get("MaField", "")))
            for x in ds:
                d = fd.get(x["IDField"])
                if not d:
                    continue
                nhan = nhan_cot.get(x["IDFieldView"]) or (d.get("Tenlabel") or d.get("TenField") or d["MaField"]).strip()
                kieu = KIEU_O.get(x.get("CtrlType", ""), "")
                s = f"{nhan} [{d['MaField']}]" + (f"{{{kieu}}}" if kieu else "") + ("(chỉ đọc)" if x.get("ReadOnly") == "1" else "")
                (an if x.get("Hide") == "1" else cot).append(s)
                if x["IDFieldView"] in sua:
                    o_sua.append(f"#{d['MaField']}")
            if cot:
                out.append("  - Cột: " + "; ".join(cot))
            if an:
                out.append("  - Cột ẩn: " + "; ".join(an))
            if o_sua:
                out.append("  - Ô trên form sửa: " + ", ".join(o_sua))
            for b in sorted(nut[v["IDView"]], key=lambda x: x.get("OrderIndex") or ""):
                out.append(f"  - Nút {b['CommandName']}: \"{b['ToolTip'].strip()}\"" + (f" ({b['HotKey']})" if b.get("HotKey") else ""))
        return out

    os.makedirs(a.ra, exist_ok=True)
    idx = ["# Danh mục màn hình Edusoft.NET (cấu hình gốc AQ)", "",
           "Sinh bằng `tools/lap_danh_muc.py` từ dữ liệu hệ thống AQ.Data… của gói server. Đường dẫn menu = chữ hiện trên",
           "ribbon/cây chức năng; «tiêu đề lưới» = chữ sau `@` (vd `click: Thêm @ Danh sách quyết định`); cột lưới = nhãn [MaField];",
           "ô trên form sửa = `#MaField` dùng cho `type:`/`choose:`/`date:`.",
           "Trường có thể chỉnh lại (ẩn cột, đổi nhãn, đổi menu) bằng bảng H… trong CSDL trường – khi lệch thì tin `ui-*.txt`.", "",
           "| Phân hệ | Tên trên ribbon | Số menu | Số màn hình | File |", "|---|---|---|---|---|"]
    for ma in sorted(set(menu) | set(man), key=lambda m: (m == "KHAC", m)):
        p = next((x for x in ph.values() if x["MaPhanHe"] == ma), None)
        ten_ph = f"{p['TenPhanHe']} ({p['VtPhanHe']})" if p else "Chưa gán phân hệ"
        out = [f"# {ma} – {ten_ph}", "", "## Menu (đường dẫn → lớp màn hình)", ""]
        for dd, r, f, lop in sorted(menu.get(ma, []), key=lambda x: x[0].lower()):
            vt = (p["VtPhanHe"] + "/ ") if p else ""
            dong = f"- `{r['MaChucNang']}` {vt}{dd}"
            if lop:
                dong += f" → `{lop}`"
                if r.get("Param1"):
                    dong += f" (Param1={r['Param1']})"
                if lop_view.get(lop):
                    dong += " – màn hình: " + ", ".join(lop_view[lop])
            out.append(dong)
        out += ["", "## Màn hình (view) và lưới", ""]
        for r1 in sorted(man.get(ma, []), key=lambda x: x["MaView1"].lower()):
            out += mo_ta_view(r1)
        with open(os.path.join(a.ra, f"{ma}.md"), "w", encoding="utf-8") as w:
            w.write("\n".join(out) + "\n")
        idx.append(f"| {ma} | {p['VtPhanHe'] if p else ''} | {len(menu.get(ma, []))} | {len(man.get(ma, []))} | [{ma}.md]({ma}.md) |")
    with open(os.path.join(a.ra, "index.md"), "w", encoding="utf-8") as w:
        w.write("\n".join(idx) + "\n")
    print("Đã ghi", os.path.abspath(a.ra))
    return 0


if __name__ == "__main__":
    sys.exit(main())

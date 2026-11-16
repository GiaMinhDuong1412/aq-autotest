#!/usr/bin/env python3
"""Đánh dấu ô BẮT BUỘC (dấu * đỏ trên Edusoft) cho các lưới trong web/edusoft-catalog.json, từ metadata CSDL.

  python tools/gan_bat_buoc.py <thư mục aqdata> [--json web/edusoft-catalog.json]

Edusoft vẽ dấu * cạnh ô khi trường của bảng chính có AQFileField.AllowNull = 0 (đối chiếu 16/11/2026: bảng SDSQD –
Số QĐ, Lý do QĐ, Ngày lập có *, Tên QĐ / Ngày hiệu lực không; SDMSV – Mã SV, Họ lót, Tên). Bỏ trường hệ thống
(khóa chính, khóa liên kết ID…, MaUser, NgayThem, NHHK, IDDVPC…) vì chương trình tự điền.
Ghi vào mỗi lưới: "bb": [FieldName bắt buộc] và "dai": {FieldName: số ký tự tối đa} (chuỗi có LenDB > 0) – dùng cho
luồng thay thế "bỏ trống ô bắt buộc" / "nhập quá dài". Chạy sau lap_danh_muc.py (gan_form_tay.py chạy trước hay sau đều được).
"""
import argparse
import collections
import csv
import glob
import json
import os
import sys

csv.field_size_limit(10 ** 9)
HE_THONG = {"mauser", "ngaythem", "ngaysua", "mausersua", "nhhk", "iddvpc", "idaddin"}


def doc(thu_muc, so):
    f = glob.glob(os.path.join(thu_muc, f"aq.data{so}-*.csv"))
    if not f:
        raise SystemExit(f"Thiếu file aq.data{so}-*.csv trong {thu_muc}")
    with open(f[0], encoding="utf-8-sig") as r:
        return list(csv.DictReader(r))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("aqdata", help="thư mục CSV do doc_aqdata.py xuất")
    ap.add_argument("--json", default="web/edusoft-catalog.json")
    a = ap.parse_args()
    fd = {r["IDField"]: r for r in doc(a.aqdata, "002")}
    bang = {r["IDFile"]: r["MaFile"].strip().upper() for r in doc(a.aqdata, "001")}
    bb, dai = collections.defaultdict(list), collections.defaultdict(dict)
    for r in doc(a.aqdata, "003"):
        b, f = bang.get(r["IDFile"]), fd.get(r["IDField"])
        if not b or not f:
            continue
        ma = f["MaField"].strip()
        try:
            n = int(float(f.get("LenDB") or 0))
        except ValueError:
            n = 0
        if 0 < n < 4000:
            dai[b][ma] = n
        if r["AllowNull"] != "0" or r["IsKhoa"] == "1" or ma.lower() in HE_THONG:
            continue
        if ma.upper().startswith("ID") and (r["IsKhoaPhu"] not in ("", "0") or r["AllowNullSQL"] == "0"):
            continue                                    # khóa liên kết do chương trình gán
        bb[b].append(ma)
    cat = json.load(open(a.json, encoding="utf-8"))
    dem = collections.Counter()
    for v in cat["views"].values():
        for g in v["luoi"]:
            b = (g.get("bang") or "").upper()
            co = {c[1] for c in g["cot"]} | set(g.get("o") or [])
            g.pop("bb", None)
            g.pop("dai", None)
            x = [m for m in bb.get(b, []) if m in co]
            if x:
                g["bb"] = x
                dem["luoi"] += 1
                dem["o"] += len(x)
            d = {m: n for m, n in dai.get(b, {}).items() if m in co and m in set(g.get("o") or [])}
            if d:
                g["dai"] = d
    with open(a.json, "w", encoding="utf-8") as w:
        json.dump(cat, w, ensure_ascii=False, separators=(",", ":"))
    print("Lưới có ô bắt buộc:", dem["luoi"], "· tổng ô bắt buộc:", dem["o"])
    return 0


if __name__ == "__main__":
    sys.exit(main())

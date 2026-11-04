#!/usr/bin/env python3
"""Đọc file dữ liệu hệ thống AQ.Data… của server Edusoft (định nghĩa menu/view/cột/thông báo) và xuất ra CSV.

Theo source (AQData.Business/Common/SystemData.ReadResource): mỗi file = JSON (danh sách bản ghi) nén gzip.
Chỉ giải nén – không giải mã gì. File nào không phải gzip/zlib thì báo "không đọc được" và bỏ qua.
Bảng người dùng/khách hàng/bản quyền không xuất; cột nhạy cảm (mật khẩu, khóa, mã máy…) để trống.

Cách dùng (PowerShell, trong thư mục repo):
  python tools\\doc_aqdata.py D:\\Source.NET.zip --trong edusoft.server.zip      (đọc thẳng trong gói server, không giải nén cả gói)
  python tools\\doc_aqdata.py "D:\\...\\wcf\\bin"                                (thư mục bin của server trường – đúng phiên bản nhất)
Kết quả: thư mục aqdata\\ (mỗi file một CSV + tom-tat.txt) và aqdata.zip để gửi Claude.
"""
import argparse
import csv
import gzip
import io
import json
import os
import re
import sys
import zipfile
import zlib

# Thứ tự DataMap trong source trunk (SystemData.DataMap): AQ.Data001 = mục 1… Gói cũ có thể lệch – tên chỉ là ĐOÁN,
# tom-tat.txt in kèm tên cột để đối chiếu.
DATAMAP = """AQDmFile AQDmField AQFileField AQRelation AQDMTruong AQRelationVirtual AQDMTREE AQTreeCT AQTreeLink
AQDMLHD AQFieldReport AQDMLLL AQDMHC AQOrderReport AQDMPLGV AQDmChucNangPTSL AQOrderView AQValSetField
AQTabColumn AQSpecialScrip AQDMQC AQTabView AQFieldReport3 AQEnumCT AQDmMess AQDMSetting AQDMChucNang AQSettingNodeDV
AQViewMethod AQFieldEdit AQDMReportCtrl AQDMBac AQDGCT AQFieldReport0 AQValSetR AQDMHe AQValueSettingDF1 AQDmDG AQValSetV
AQXHCT AQDMNode AQValSetV1 AQDmBgQDC AQFieldReport2 AQValSetR1 AQDMView1 AQDMPhanHe AQAddinTruong AQDmTChuan AQFileKTHK
AQValueSettingDF AQPhanCap AQViewAddCtrl AQDangkyTruong
AQFieldView AQNhomTChi AQFilePTSL AQDmForm0 AQView AQDMLoaiPC AQViewSpliter AQDieuKienChiSoSetting AQDMAddin
AQDmXH AQDMTTTN AQDmReport0 AQDMLoaiPhep AQDmView0 AQDmFile0 AQDMVBCC AQDmBoTChi AQDMLLCT
AQValSetField1 AQDMTmpWord AQDHCDNg AQDMNH AQFieldView2 AQDMDT AQValueSettingDV AQDMChucVu AQDuLieuMau
AQDMReport1 AQDMForm AQDMNgach AQReport AQDMTG AQDMNgachCT AQDmDB AQDMDCS AQBgQDCT
AQDMNhNgach AQDMLThu AQDMPLNV AQTChi AQDmDHCD AQDMPLThaiSan AQDmENum AQDMLDSDPH AQDMHocHam
AQDMLOAICT AQDMLDQD AQDMTCPHONG AQDMLKH AQDMPLTCHI AQDMMESSERR AQDMLVuc AQDMLBG AQDMHS
AQDMCVBCS AQDMLVB AQDMKTKL AQDMTPRL AQRight AQUser AQDMTCDG AQDMTTHTDG AQDMNhTCDG
AQDMPhieuDG AQFileChucNang AQDeleteKem AQThueTNCN AQQTBienDongTS AQHSUTTKB AQDMNHUT AQDMUTKTX AQCNBODEM
AQDMNHOMSETTING AQHSUTLT AQValSetR1NgonNgu AQDMNgonNgu AQNgonNguTruong AQValSetFieldNgonNgu AQMessNgonNgu AQChucNangNgonNgu
AQValSetV1NgonNgu AQDmLoaiBB AQEEDMMinhChung AQEEDSTieuChuanTuDG AQEEDSTieuChiTuDG AQEEDSMinhChungTieuChi AQDKienPCCoiThi
AQXuatDuLieuLenWEB AQNhomSettingDKMH AQSettingDKMH AQSettingEduWEB AQFileHuongDan AQMenuTheoTruong AQFileNetWEB""".split()

BANG_BO = {"aquser", "aqright", "aqdangkytruong", "aqdmtruong", "aqaddintruong"}  # người dùng / khách hàng / bản quyền
COT_NHAY_CAM = re.compile(r"pass|pwd|matkhau|mat_khau|^key$|licen|productkey|apikey|privatekey|token|secret|serial|machin|"
                          r"banquyen|salt|hash", re.I)  # cột này được để trống khi xuất
TEN_FILE = re.compile(r"(?:^|/)(aq\.data(\d{3}|\.specs))(\.(?:dll|edp))?$", re.I)


def tim_file(nguon, trong):
    """Trả về {tên (aq.data001…): bytes}, ưu tiên wcf/bin."""
    ra, uu_tien = {}, {}
    if os.path.isdir(nguon):
        for goc, _, files in os.walk(nguon):
            for f in files:
                p = os.path.join(goc, f).replace("\\", "/")
                m = TEN_FILE.search(p)
                if m:
                    ten = m.group(1).lower()
                    if ten not in ra or "wcf" in p.lower():
                        with open(p, "rb") as r:
                            ra[ten] = r.read()
        return ra
    if trong:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import xem_goi
        g = xem_goi.Dem(xem_goi.mo_goi(nguon, trong))
        for ten, kt, co, _ in xem_goi.duyet(g):
            m = TEN_FILE.search(ten) if co == "0" else None
            if not m:
                continue
            k = m.group(1).lower()
            if k in ra and uu_tien.get(k):
                continue
            ra[k] = xem_goi.doc_du(g, kt)
            g._da_doc = kt
            uu_tien[k] = "wcf" in ten.lower()
        return ra
    raise SystemExit("Nguồn phải là thư mục bin của server, hoặc file .zip kèm --trong edusoft.server.zip")


def giai_nen(b):
    if b[:2] == b"\x1f\x8b":
        return gzip.decompress(b)
    for w in (zlib.MAX_WBITS, -zlib.MAX_WBITS):
        try:
            return zlib.decompress(b, w)
        except zlib.error:
            pass
    if b[:2] == b"PK":
        with zipfile.ZipFile(io.BytesIO(b)) as z:
            return z.read(z.namelist()[0])
    return None


def o(v):
    if v is None:
        return ""
    if isinstance(v, (dict, list)):
        return json.dumps(v, ensure_ascii=False)
    return str(v)


def main():
    ap = argparse.ArgumentParser(description="Xuất dữ liệu hệ thống AQ.Data… của server Edusoft ra CSV.")
    ap.add_argument("nguon", help="thư mục bin của server, hoặc file .zip source (kèm --trong)")
    ap.add_argument("--trong", help="tên gói server trong file zip, vd edusoft.server.zip")
    ap.add_argument("--ra", default="aqdata", help="thư mục kết quả (mặc định aqdata)")
    ap.add_argument("--chi", help="chỉ xuất các file/bảng này, cách nhau dấu phẩy: số file (027) hoặc tên bảng đoán (AQView)")
    ap.add_argument("--toi-da-mb", type=float, default=20, help="mỗi file zip tối đa bao nhiêu MB (mặc định 20) – lớn hơn thì tách phần")
    a = ap.parse_args()

    files = tim_file(a.nguon, a.trong)
    if not files:
        print("Không thấy file AQ.Data… nào.")
        return 1
    os.makedirs(a.ra, exist_ok=True)
    chi = {x.strip().lower() for x in (a.chi or "").split(",") if x.strip()}
    tt = ["file | đoán tên bảng | số dòng | kết quả | các cột"]
    xuat = []
    for ten in sorted(files):
        b = files[ten]
        so = ten[7:]
        doan = DATAMAP[int(so) - 1] if so.isdigit() and 1 <= int(so) <= len(DATAMAP) else ("specs" if so == ".specs" else "?")
        if chi and not ({so.lstrip("."), so.lstrip(".").lstrip("0"), doan.lower()} & chi):
            continue
        try:
            raw = giai_nen(b)
        except Exception as x:  # noqa: BLE001
            raw, loi = None, str(x)
        else:
            loi = ""
        if raw is None:
            tt.append(f"{ten} | {doan} | - | không đọc được (đầu file {b[:4].hex()} {loi}) | ")
            continue
        try:
            data = json.loads(raw.decode("utf-8-sig"))
        except Exception:  # noqa: BLE001
            tt.append(f"{ten} | {doan} | - | không phải JSON ({len(raw)} byte) | ")
            continue
        if isinstance(data, dict):
            data = [data]
        cot = []
        for r in data:
            if isinstance(r, dict):
                for k in r:
                    if k not in cot:
                        cot.append(k)
        nc = {c for c in cot if COT_NHAY_CAM.search(c)}
        if doan.lower() in BANG_BO or {"username", "password"} <= {c.lower() for c in cot}:
            tt.append(f"{ten} | {doan} | {len(data)} | KHÔNG xuất (bảng người dùng/khách hàng/bản quyền) | ")
            continue
        p = os.path.join(a.ra, f"{ten}-{doan}.csv")
        with open(p, "w", encoding="utf-8-sig", newline="") as w:
            cw = csv.writer(w)
            cw.writerow(cot)
            for r in data:
                if isinstance(r, dict):
                    cw.writerow(["" if c in nc else o(r.get(c)) for c in cot])
        xuat.append(p)
        che = f" (để trống cột {', '.join(sorted(nc))})" if nc else ""
        tt.append(f"{ten} | {doan} | {len(data)} | đã xuất{che} | {', '.join(cot)[:600]}")
    p_tt = os.path.join(a.ra, "tom-tat.txt")
    with open(p_tt, "w", encoding="utf-8") as w:
        w.write("\n".join(tt) + "\n")
    goc = a.ra.rstrip("\\/")
    for cu in os.listdir(os.path.dirname(os.path.abspath(goc))):  # xóa zip cũ của lần chạy trước
        if re.fullmatch(re.escape(os.path.basename(goc)) + r"(-\d+)?\.zip", cu):
            os.remove(os.path.join(os.path.dirname(os.path.abspath(goc)), cu))
    gioi_han = int(a.toi_da_mb * 1048576)
    phan, cur, dung = [], [p_tt], 0
    for p in sorted(xuat, key=os.path.getsize):
        with open(p, "rb") as r:
            uoc = len(zlib.compress(r.read(), 6)) + 200
        if cur and dung + uoc > gioi_han and len(cur) > (1 if cur[0] == p_tt else 0):
            phan.append(cur)
            cur, dung = [], 0
        cur.append(p)
        dung += uoc
    phan.append(cur)
    zips = []
    for i, ds in enumerate(phan, 1):
        zp = goc + (f"-{i}" if len(phan) > 1 else "") + ".zip"
        with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for p in ds:
                z.write(p, os.path.relpath(p, a.ra))
        zips.append(zp)
    print(f"Đọc {len(files)} file, xuất {len(xuat)} bảng ra {os.path.abspath(a.ra)}")
    print(f"Tóm tắt: {os.path.abspath(p_tt)}")
    for zp in zips:
        print(f"Gửi Claude: {os.path.abspath(zp)} ({os.path.getsize(zp) // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

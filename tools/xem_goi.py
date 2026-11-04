#!/usr/bin/env python3
"""Liệt kê / lấy riêng file trong gói tar.gz của bộ cài Edusoft (vd edusoft.server.zip – thật ra là tar.gz, header
không chuẩn nên tar.exe báo "Unrecognized archive format"). Chỉ thư viện chuẩn, đọc tuần tự, không giải nén cả gói.

Cách dùng (PowerShell, trong thư mục repo):
  python tools\\xem_goi.py D:\\Source.NET.zip --trong edusoft.server.zip                 -> goi-ds.txt (tên + dung lượng)
  python tools\\xem_goi.py D:\\Source.NET.zip --trong edusoft.server.zip --lay "dbackup\\*.bak" --ra D:\\goi-lay
  python tools\\xem_goi.py D:\\edusoft.server.tgz                                        (gói đã chép ra ngoài)
--lay nhận mẫu kiểu dir (*, ?), so không phân biệt hoa thường, / và \\ như nhau; file *.config / config.xml không lấy.
"""
import argparse
import fnmatch
import gzip
import os
import sys
import zipfile

KHONG_LAY = ("*.config", "*config.xml", "*.pfx", "*.cer", "*pass*")


def mo_goi(nguon, trong):
    if trong:
        z = zipfile.ZipFile(nguon)
        ten = [n for n in z.namelist() if n.lower().replace("\\", "/").endswith(trong.lower().replace("\\", "/"))]
        if not ten:
            raise SystemExit("Không thấy %s trong %s" % (trong, nguon))
        f = z.open(ten[0])
    else:
        f = open(nguon, "rb")
    dau = f.read(2)
    f.close()
    f = zipfile.ZipFile(nguon).open(ten[0]) if trong else open(nguon, "rb")
    return gzip.GzipFile(fileobj=f) if dau == b"\x1f\x8b" else f


def doc_du(f, n):
    b = bytearray()
    while len(b) < n:
        x = f.read(n - len(b))
        if not x:
            break
        b += x
    return bytes(b)


def so_bat_phan(b):
    s = b.replace(b"\0", b" ").strip()
    if b and b[0] & 0x80:  # dạng nhị phân base-256 của GNU
        return int.from_bytes(b[1:], "big")
    return int(s, 8) if s else 0


def duyet(f):
    ten_dai = None
    while True:
        h = doc_du(f, 512)
        if len(h) < 512 or h == b"\0" * 512:
            return
        ten = h[0:100].split(b"\0")[0]
        tien_to = h[345:500].split(b"\0")[0] if h[257:262] == b"ustar" and h[257:265] != b"ustar  \0" else b""
        co = chr(h[156]) if h[156] else "0"
        kt = so_bat_phan(h[124:136])
        if co in ("L", "K"):  # GNU tên dài
            ten_dai = doc_du(f, kt).split(b"\0")[0]
            doc_du(f, (512 - kt % 512) % 512)
            continue
        if ten_dai:
            ten, ten_dai = ten_dai, None
        elif tien_to:
            ten = tien_to + b"/" + ten
        yield ten.decode("utf-8", "replace").replace("\\", "/"), kt, co, f
        # phần dữ liệu (nếu người gọi chưa đọc) được bỏ qua ở đây
        doc_du(f, (kt + 511) // 512 * 512 - getattr(f, "_da_doc", 0))
        f._da_doc = 0


class Dem:
    """Bọc luồng để biết người gọi đã đọc bao nhiêu byte dữ liệu của mục hiện tại."""

    def __init__(self, f):
        self.f, self._da_doc = f, 0

    def read(self, n):
        return self.f.read(n)


def main():
    ap = argparse.ArgumentParser(description="Liệt kê / lấy file trong gói tar.gz của bộ cài Edusoft.")
    ap.add_argument("nguon", help="file .zip source (kèm --trong) hoặc file gói .tgz/.tar")
    ap.add_argument("--trong", help="tên gói nằm trong file zip nguồn, vd edusoft.server.zip")
    ap.add_argument("--lay", action="append", help="mẫu file cần lấy ra, vd \"dbackup\\*.bak\" (lặp được)")
    ap.add_argument("--ra", default="goi-lay", help="thư mục chứa file lấy ra (mặc định goi-lay)")
    ap.add_argument("-o", default="goi-ds.txt", help="file danh sách (mặc định goi-ds.txt)")
    a = ap.parse_args()

    g = Dem(mo_goi(a.nguon, a.trong))
    mau = [m.replace("\\", "/").lower() for m in (a.lay or [])]
    ds, lay, tong = [], [], 0
    for ten, kt, co, f in duyet(g):
        tong += kt
        ds.append("%12d  %s%s" % (kt, ten, "/" if co == "5" else ""))
        tl = ten.lower()
        if co == "0" and mau and any(fnmatch.fnmatch(tl, m) or fnmatch.fnmatch(tl, "*/" + m) for m in mau):
            if any(fnmatch.fnmatch(tl, k) for k in KHONG_LAY):
                print("Bỏ qua (file cấu hình/khóa):", ten)
                continue
            dich = os.path.join(a.ra, *[p for p in ten.split("/") if p not in ("", ".", "..")])
            os.makedirs(os.path.dirname(dich), exist_ok=True)
            con = kt
            with open(dich, "wb") as w:
                while con:
                    x = g.read(min(con, 1 << 20))
                    if not x:
                        break
                    w.write(x)
                    con -= len(x)
            g._da_doc = kt - con
            lay.append(dich)
    with open(a.o, "w", encoding="utf-8") as w:
        w.write("\n".join(ds) + "\n")
    print("Gói có %d mục, tổng %.1f MB – danh sách ở %s" % (len(ds), tong / 1048576, os.path.abspath(a.o)))
    for p in lay:
        print("Đã lấy:", os.path.abspath(p), "(%.1f MB)" % (os.path.getsize(p) / 1048576))
    return 0


if __name__ == "__main__":
    sys.exit(main())

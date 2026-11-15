#!/usr/bin/env python3
"""Ghép phần VẼ TAY của form Edusoft (từ bản trích source) vào danh mục màn hình web/edusoft-catalog.json.

  python tools/gan_form_tay.py <trich-tat-ca.zip | thư mục trích> [--json web/edusoft-catalog.json]

Đầu vào là kết quả `tools/trich_source.py <source.zip> --tat-ca` (chỉ tên điều khiển, caption, cột lưới, câu thông báo –
không phải source). Mỗi menu có lớp màn hình khớp một form trong bản trích được thêm khóa "fm" trỏ vào "forms":
  forms[<lớp>] = {"td": tiêu đề form, "o": [[tên control, kiểu, nhãn]], "nut": [[tên, chữ trên nút]],
                  "luoi": [{"ten": tên lưới, "cot": [[caption, FieldName]]}], "tb": [câu thông báo]}
Phần dựng từ CSDL (SourceViewBase) đã nằm trong "views" do lap_danh_muc.py lập; ở đây chỉ thêm các ô lọc/nút/lưới vẽ tay
(vd ô "Chọn khóa học:" phía trên lưới) – kit tìm được bằng `#tên control` (automationId của WinForms = Name).
"""
import argparse
import collections
import io
import json
import os
import re
import sys
import zipfile

KIEU = {}
for k, ds in {"chữ": "AQTextBox TextEdit MemoEdit AQRichTextBox TextBox RichTextBox AQMemoEdit",
              "chọn": "AQLockUpEdit AQComboLockUp LookUpEdit GridLookUpEdit SearchLookUpEdit UC_ComboxChonTuDien AQComboBox "
                      "ComboBoxEdit ComboBox ImageComboBoxEdit CheckedComboBoxEdit AQCheckListBox CheckedListBoxControl",
              "ngày": "AQDateTimePicker DateEdit DateTimePicker RangeDateControl TimeEdit",
              "số": "AQSpinEdit SpinEdit NumericUpDown CalcEdit",
              "đánh dấu": "AQCheckBox CheckEdit CheckBox AddCheckBoxAuto",
              "lựa chọn": "AQRadioButton AQRadioButtonWin RadioButton RadioGroup",
              "nút …": "AQButtonEdit ButtonEdit",
              "học kỳ": "UHocKy"}.items():
    for t in ds.split():
        KIEU[t] = k
NUT = {"AQButton", "SimpleButton", "Button", "BarButtonItem", "DropDownButton"}
NHAN = {"AQLabel", "LabelControl", "Label"}
TEN_MA = re.compile(r"^[a-z]\w*\d*$")       # caption trùng kiểu tên control (vd "aqLabel2") – không phải nhãn thật


def doc_trich(nguon):
    """Trả về {tên file: nội dung} các file .txt (bỏ *-thong-bao.txt: câu thông báo đã nằm trong từng FORM)."""
    out = {}
    if os.path.isdir(nguon):
        for f in sorted(os.listdir(nguon)):
            if f.endswith(".txt") and "thong-bao" not in f:
                out[f] = open(os.path.join(nguon, f), encoding="utf-8").read()
    else:
        with zipfile.ZipFile(nguon) as z:
            for f in sorted(z.namelist()):
                if f.endswith(".txt") and "thong-bao" not in f:
                    out[f] = io.TextIOWrapper(z.open(f), encoding="utf-8").read()
    return out


def tach_form(text):
    forms, cur, phan = [], None, ""
    for line in text.splitlines():
        m = re.match(r"FORM (\w+)\s+\(kế thừa ([\w\.]+)\)\s+file (\S+)", line)
        if m:
            cur = {"lop": m.group(1), "base": m.group(2), "file": m.group(3), "td": "", "ctl": [], "luoi": [], "tb": []}
            forms.append(cur)
            phan = ""
            continue
        if cur is None:
            continue
        if line.startswith("  Tiêu đề:"):
            cur["td"] = line.split(":", 1)[1].strip()
        elif line.startswith("  -- Điều khiển"):
            phan = "ctl"
        elif line.startswith("  -- Lưới"):
            m = re.match(r"  -- Lưới (\w+)", line)
            cur["luoi"].append({"ten": m.group(1) if m else "", "cot": []})
            phan = "luoi"
        elif line.startswith("  -- Câu thông báo"):
            phan = "tb"
        elif phan == "ctl" and line.startswith("  ") and " | " in line:
            p = [x.strip() for x in line.split("|")]
            cur["ctl"].append({"ten": p[0], "loai": p[1], "chu": p[2] if len(p) > 2 else "", "vung": p[3] if len(p) > 3 else "",
                               "tip": next((x[8:] for x in p[4:] if x.startswith("tooltip=")), "")})
        elif phan == "luoi":
            m = re.match(r"\s+\w+: (.*?) \[(\w*)\]\s*$", line)
            if m:
                cur["luoi"][-1]["cot"].append([m.group(1).strip(), m.group(2)])
        elif phan == "tb":
            m = re.match(r"\s+\d+: (.+)$", line)
            if m and len(m.group(1).split()) >= 4:     # câu thông báo; bỏ chữ ngắn (tên cột "Mã khóa học"…)
                cur["tb"].append(m.group(1).strip())
    return forms


def gon(f):
    """Rút form trích thành bản ghi danh mục; None nếu không có gì vẽ tay đáng kể."""
    o, nut, vung_o, vung_nhan = [], [], collections.defaultdict(list), collections.defaultdict(list)
    for c in f["ctl"]:
        if c["loai"] in KIEU:
            rec = [c["ten"], KIEU[c["loai"]], c["chu"] if c["loai"] in ("AQCheckBox", "CheckEdit", "CheckBox", "AQRadioButton",
                                                                     "AQRadioButtonWin", "RadioButton", "AddCheckBoxAuto") else ""]
            if c["chu"] and TEN_MA.match(c["chu"]):
                rec[2] = ""
            o.append(rec)
            vung_o[c["vung"]].append(rec)
        elif c["loai"] in NUT and c["chu"] and not TEN_MA.match(c["chu"]):
            nut.append([c["ten"], c["chu"]])
        elif c["loai"] in NHAN and c["chu"] and not TEN_MA.match(c["chu"]):
            vung_nhan[c["vung"]].append(c["chu"].strip())
    for v, ds in vung_o.items():                # nhãn ↔ ô: chỉ ghép khi cùng vùng và số nhãn = số ô (giữ thứ tự khai báo);
        cho = [r for r in ds if not r[2]]       # vùng có thêm nhãn khác (vd "Thông báo") thì chỉ lấy nhãn kết thúc bằng ":"
        nh = vung_nhan.get(v, [])
        if len(nh) != len(cho):
            nh = [t for t in nh if t.endswith(":")]
        if v and nh and len(nh) == len(cho):
            for r, t in zip(cho, nh):
                r[2] = t.rstrip(": ").strip()
    luoi = [g for g in f["luoi"] if g["cot"]]
    if not (o or nut or luoi):
        return None
    out = {"o": o, "nut": nut, "luoi": luoi}
    if f["td"] and not TEN_MA.match(f["td"]):
        out["td"] = f["td"]
    tb = list(dict.fromkeys(f["tb"]))[:40]
    if tb:
        out["tb"] = tb
    return out


def chon(lop, ung_vien):
    """Lớp đầy đủ (vd Edusoft.STM._01.F002_NhapPhongKH) → form trích có đường dẫn file khớp namespace nhiều nhất."""
    if len(ung_vien) == 1:
        return ung_vien[0]
    seg = [s.strip("_").lower() for s in lop.split(".")[:-1]]

    def diem(f):
        ps = [s.strip("_").lower() for s in re.split(r"[/\\]", f["file"])]
        return sum(1 for s in seg if s in ps)
    return max(ung_vien, key=diem)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("trich", help="trich-tat-ca.zip hoặc thư mục đã giải nén")
    ap.add_argument("--json", default="web/edusoft-catalog.json")
    a = ap.parse_args()
    theo_lop = collections.defaultdict(list)
    for _, text in doc_trich(a.trich).items():
        for f in tach_form(text):
            theo_lop[f["lop"]].append(f)
    cat = json.load(open(a.json, encoding="utf-8"))
    cat["forms"], dem = {}, collections.Counter()
    for m in cat["menus"]:
        m.pop("fm", None)
        lop = m.get("lop") or ""
        uv = theo_lop.get(lop.split(".")[-1])
        if not uv:
            dem["khong-co-trong-trich"] += 1
            continue
        if lop not in cat["forms"]:
            g = gon(chon(lop, uv))
            if g is None:
                dem["chi-dung-tu-csdl"] += 1
                continue
            cat["forms"][lop] = g
        m["fm"] = lop
        dem["co-phan-ve-tay" + ("" if m.get("views") else "-chua-co-luoi")] += 1
    cat["formsVer"] = os.path.basename(a.trich)
    with open(a.json, "w", encoding="utf-8") as w:
        json.dump(cat, w, ensure_ascii=False, separators=(",", ":"))
    print("Menu:", len(cat["menus"]), dict(dem))
    print("Form vẽ tay đã ghép:", len(cat["forms"]), "· ô", sum(len(x["o"]) for x in cat["forms"].values()),
          "· nút", sum(len(x["nut"]) for x in cat["forms"].values()), "· lưới", sum(len(x["luoi"]) for x in cat["forms"].values()))


if __name__ == "__main__":
    sys.exit(main())

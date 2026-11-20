---
loai: truong
ma: CTTD
ten: CĐ Công Thương TP.HCM
netweb_that: https://dkmh.hitu.edu.vn/
web_test: 
edusoft_test: 
trang_thai_hd: Actived
phan_cap: []
nguon: sheet-release
trang_thai: can-xac-nhan
aliases:
  - "CĐ Công Thương TP.HCM"
---
# CTTD – CĐ Công Thương TP.HCM

## Netweb của trường
- Trang thật (KH dùng): `https://dkmh.hitu.edu.vn/` – **chỉ để nhận ra trường trong case, KHÔNG thử / ghi dữ liệu trên trang thật.**
- Web test: (điền) · Edusoft test: (điền)

## Chức năng web trường có (sheet ChuyenDoiNetWeb, 2021 – có thể đã đổi)
- DKMH online
- Đóng học phí trực tuyến
- Khảo sát trực tuyến
- SV xem học phí
- GV nhập điểm online
- GV điểm danh online

## Ghi chú
Trang ĐKMH riêng. Ghi chú cũ: không dùng được tool update.


## Khi đọc case của trường này
- Mã trường trên ACS: **`CTTD`** (4 ký tự) = case chung của trường. Mã **dài hơn 4 ký tự** bắt đầu bằng `CTTD` = **phân cấp** (đơn vị phân cấp: hệ / cơ sở) của trường.
- Case làm theo phân cấp thì **chỉ có hiệu lực trên phân cấp đó**: test trên đúng phân cấp (site / dữ liệu của phân cấp), phân cấp khác của cùng trường thường không bị ảnh hưởng – trừ khi sửa phần chung của trường.
- Gặp mã phân cấp mới → thêm vào `phan_cap` (dạng `"MÃ: tên phân cấp"`).
- Coder sửa `VersionSchool/CTTD/…` = bản riêng của trường → kiểm tra trên bản / trang test của chính trường này.
- Case cùng trường (cùng phân cấp) gửi gần nhau thường cùng đợt / cùng bản sửa → xem chung (MCP `acs_case_lien_quan`).

---
Nguồn: sheet Release(TestMenu) – ChuyenDoiNetWeb, Port NetWEB. Trạng thái hợp đồng ghi theo sheet: Actived.

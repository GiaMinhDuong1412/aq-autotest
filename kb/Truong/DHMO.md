---
loai: truong
ma: DHMO
ten: ĐH Mở TP.HCM
netweb_that: https://tienichsv.ou.edu.vn/#/home
web_test: 
edusoft_test: 
trang_thai_hd: Actived
ma_acs:
  - DHMO
nguon: sheet-release
trang_thai: can-xac-nhan
---
# DHMO – ĐH Mở TP.HCM

## Netweb của trường
- Trang thật (KH dùng): `https://tienichsv.ou.edu.vn/#/home` – **chỉ để nhận ra trường trong case, KHÔNG thử / ghi dữ liệu trên trang thật.**
- Web test: (điền) · Edusoft test: (điền)

## Chức năng web trường có (sheet ChuyenDoiNetWeb, 2021 – có thể đã đổi)
- DKMH online
- Đóng học phí trực tuyến
- SV xem học phí
- SV xem CTĐT

## Ghi chú
Trên ACS có mã con DHMOTX (hệ từ xa).


## Khi đọc case của trường này
- Mã trên ACS: `DHMO` (school_code). Mã khác chưa có ở đây → ghi thêm vào `ma_acs` khi đã xác nhận.
- Coder sửa `VersionSchool/DHMO/…` = bản riêng của trường → kiểm tra trên bản / trang test của chính trường này.
- Chức năng web trường có (mục trên) quyết định case web có thuộc chức năng trường dùng không.
- Case cùng trường gửi gần nhau thường cùng đợt / cùng bản sửa → xem chung (MCP `acs_case_lien_quan`).

## Mã ACS cần xác nhận
- `DHMOTX` (thấy ở case 64656 – KLGD "Đào tạo trực…") có thể là hệ đào tạo từ xa / trực tuyến của DHMO – **chưa xác nhận**, chưa ghi vào `ma_acs`.

---
Nguồn: sheet Release(TestMenu) – ChuyenDoiNetWeb, Port NetWEB. Trạng thái hợp đồng ghi theo sheet: Actived.

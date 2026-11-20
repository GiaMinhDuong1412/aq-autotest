---
loai: truong
ma: KTTC
ten: ĐH Kinh tế - Tài chính TP.HCM
netweb_that: 
web_test: 
edusoft_test: 
trang_thai_hd: Chưa nghiệm thu NetWeb (2021)
ma_acs:
  - KTTC
nguon: sheet-release
trang_thai: can-xac-nhan
---
# KTTC – ĐH Kinh tế - Tài chính TP.HCM

## Netweb của trường
- Trang thật (KH dùng): (chưa có trong sheet) – **chỉ để nhận ra trường trong case, KHÔNG thử / ghi dữ liệu trên trang thật.**
- Web test: (điền) · Edusoft test: (điền)

## Chức năng web trường có (sheet ChuyenDoiNetWeb, 2021 – có thể đã đổi)
- DKMH online
- Khảo sát trực tuyến
- SV xem học phí
- SV xem CTĐT
- Kết quả xét tốt nghiệp (web)
- SV xin bảng điểm online

## Ghi chú
Có phiên bản riêng – coder sửa ở `VersionSchool/KTTC/…` (xem [[VersionSchool]]).


## Khi đọc case của trường này
- Mã trên ACS: `KTTC` (school_code). Mã khác chưa có ở đây → ghi thêm vào `ma_acs` khi đã xác nhận.
- Coder sửa `VersionSchool/KTTC/…` = bản riêng của trường → kiểm tra trên bản / trang test của chính trường này.
- Chức năng web trường có (mục trên) quyết định case web có thuộc chức năng trường dùng không.
- Case cùng trường gửi gần nhau thường cùng đợt / cùng bản sửa → xem chung (MCP `acs_case_lien_quan`).

---
Nguồn: sheet Release(TestMenu) – ChuyenDoiNetWeb, Port NetWEB. Trạng thái hợp đồng ghi theo sheet: Chưa nghiệm thu NetWeb (2021).

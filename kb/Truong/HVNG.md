---
loai: truong
ma: HVNG
ten: 
web_test: 
edusoft_test: EDUSOFT - HVNG - Copy (máy chạy thử)
trang_thai: can-xac-nhan
---
# HVNG

## Môi trường test
- Edusoft test: bản **EDUSOFT - HVNG - Copy** trên máy chạy thử (vd `E:\AQ - Works\EDUSOFT_ALL_ENV\EDUSOFT - HVNG - Copy\Edusoft.NET.exe`) – môi trường mặc định của AQ Auto Test.
- Tài khoản test: `admindh` (mật khẩu trong Windows Credential Manager – không ghi ở đây).
- Danh mục màn hình Edusoft của AQ Auto Test (`web/edusoft-catalog.json`) dựng từ bản HVNG.

## Khi đọc case của trường này
- Mã trên ACS: `HVNG` (school_code). Mã khác chưa có ở đây → ghi thêm vào `ma_acs` khi đã xác nhận.
- Coder sửa `VersionSchool/HVNG/…` = bản riêng của trường → kiểm tra trên bản / trang test của chính trường này.
- Chức năng web trường có (mục trên) quyết định case web có thuộc chức năng trường dùng không.
- Case cùng trường gửi gần nhau thường cùng đợt / cùng bản sửa → xem chung (MCP `acs_case_lien_quan`).

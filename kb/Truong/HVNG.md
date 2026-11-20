---
loai: truong
ma: HVNG
ten: 
web_test: 
edusoft_test: EDUSOFT - HVNG - Copy (máy chạy thử)
phan_cap: []
trang_thai: can-xac-nhan
---
# HVNG

## Môi trường test
- Edusoft test: bản **EDUSOFT - HVNG - Copy** trên máy chạy thử (vd `E:\AQ - Works\EDUSOFT_ALL_ENV\EDUSOFT - HVNG - Copy\Edusoft.NET.exe`) – môi trường mặc định của AQ Auto Test.
- Tài khoản test: `admindh` (mật khẩu trong Windows Credential Manager – không ghi ở đây).
- Danh mục màn hình Edusoft của AQ Auto Test (`web/edusoft-catalog.json`) dựng từ bản HVNG.

## Khi đọc case của trường này
- Mã trường trên ACS: **`HVNG`** (4 ký tự) = case chung của trường. Mã **dài hơn 4 ký tự** bắt đầu bằng `HVNG` = **phân cấp** (đơn vị phân cấp: hệ / cơ sở) của trường.
- Case làm theo phân cấp thì **chỉ có hiệu lực trên phân cấp đó**: test trên đúng phân cấp (site / dữ liệu của phân cấp), phân cấp khác của cùng trường thường không bị ảnh hưởng – trừ khi sửa phần chung của trường.
- Gặp mã phân cấp mới → thêm vào `phan_cap` (dạng `"MÃ: tên phân cấp"`).
- Coder sửa `VersionSchool/HVNG/…` = bản riêng của trường → kiểm tra trên bản / trang test của chính trường này.
- Case cùng trường (cùng phân cấp) gửi gần nhau thường cùng đợt / cùng bản sửa → xem chung (MCP `acs_case_lien_quan`).

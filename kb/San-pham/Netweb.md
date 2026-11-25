---
loai: san-pham
ma: web
test_tren: web
trang_thai: can-xac-nhan
---
# Netweb (cổng web SV / GV / phụ huynh)

## Là gì
Trang web của trường cho sinh viên, giảng viên, phụ huynh (đăng ký môn học, xem học phí, điểm…).

## Test ở đâu
Trang web **test** của trường (xem ghi chú từng trường ở `Truong/`), đăng nhập tài khoản test đúng vai trò KH nêu.

## Dấu hiệu nhận biết trong case
- KH nói "trang", "cổng", "summary", "bảng hiển thị", gửi link `https://…`.
- Phân hệ trên ACS có chữ WEB / UI (NETWEB-UI, DKMHUI…) – cần xác nhận ở `Phan-he/`.
- Coder sửa repo `VersionSchool/<trường>/…` – cần xác nhận ở [[VersionSchool]].

## Liên kết với Edusoft
Chung 1 CSDL với Edusoft; sửa Edusoft mà web chưa đổi thì nghi **cache** (đăng xuất / đăng nhập lại, Clear cache ở `/admin`).
Từng trang web đọc / ghi dữ liệu nào, bị biến chỉnh định nào chi phối: [[00 Liên kết Netweb - Edusoft]] và thư mục `Web/`.

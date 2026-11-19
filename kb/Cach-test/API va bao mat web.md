---
loai: cach-test
ap_dung: NETWEB-API, đăng nhập, bảo mật, request giữa các vai trò
test_tren: web
nguon: tai-lieu
---
# API va bao mat web

## Khi nào dùng
Case NETWEB-API, đăng nhập, bảo mật, request giữa các vai trò.

## Chuẩn bị
Tài khoản test các vai trò liên quan (SV, GV-CVHT…), trang web test của trường.
## Các bước kiểm tra
1. Làm đúng thao tác trên web gây ra request KH nêu (rút môn, CVHT gọi sang SV, đăng nhập 2 lớp…).
2. Trường hợp đúng: kết quả đúng, dữ liệu ghi xuống Edusoft đúng.
3. Trường hợp sai: sai mật khẩu / mã xác thực, hết phiên, không đủ quyền → bị chặn đúng thông báo, không lộ dữ liệu.
## Kiểm tra không ảnh hưởng
Đăng nhập / đăng xuất thường của các vai trò khác; tải cao (đợt ĐKMH) nếu case liên quan hiệu năng.

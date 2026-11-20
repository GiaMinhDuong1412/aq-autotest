---
loai: dang-case
ten: Tài khoản – phân quyền – đăng nhập – bảo mật
dau_hieu_kh: "đăng nhập|mật khẩu|tài khoản|phân quyền|quyền|bảo mật|xác thực|2 lớp|otp|token|hết phiên|truy cập"
dau_hieu_ba: "phân quyền|bảo mật|xác thực"
dau_hieu_dev: "auth|login|token|permission|role"
noi_hay_gap:
  - web
  - edusoft
phan_he_hay_gap:
  - "[[QLHT]]"
  - "[[NETWEB-API]]"
  - "[[NETWEB-UI]]"
trang_thai: tu-tai-lieu
---
# Tài khoản – phân quyền – đăng nhập – bảo mật

Không đăng nhập được, thấy / không thấy chức năng sai quyền, lỗ hổng bảo mật, bảo mật 2 lớp.

## Nhận biết
- **Lời KH**: `đăng nhập|mật khẩu|tài khoản|phân quyền|quyền|bảo mật|xác thực|2 lớp|otp|token|hết phiên|truy cập`
- **BA**: `phân quyền|bảo mật|xác thực`
- **Dev**: `auth|login|token|permission|role`
(biểu thức để app gợi ý dạng case – sửa ở Properties `dau_hieu_*`)

## Phải trả lời khi phân tích
- Vai trò nào (SV, GV, CVHT, quản trị), trên Edusoft hay web
- Đúng thiết kế (chưa phân quyền) hay lỗi
- Case bảo mật: trường hợp sai (sai mật khẩu, hết phiên, gọi API khi không đủ quyền) là một phần yêu cầu

## Case liên quan với dạng này là
Các chức năng dùng cùng quyền / cùng API; trường khác dùng cùng cơ chế đăng nhập.

## Hay nhầm
Thiếu quyền do trường chưa gán quyền → [[Xu ly du lieu]] / hướng dẫn, không phải lỗi.

## Phân hệ hay gặp
[[QLHT]], [[NETWEB-API]], [[NETWEB-UI]]

## Case mẫu (tiêu đề từ danh sách ACS – cần đọc nội dung đầy đủ)
- 64724
- 64677
- 64678

Xem cách đọc case: [[00 Cách phân tích case]].

---
loai: phan-he
ma: QLHT
ten: Quản lý hệ thống
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
tab_edusoft: Hệ thống
dau_hieu: tài khoản, phân quyền, khóa sổ, học kỳ, biểu in, import, bảo mật, đăng nhập, chatbot, chỉnh định NetWEB
nguon: tai-lieu
trang_thai: tu-tai-lieu
---
# QLHT – Quản lý hệ thống

## Là gì
Tài khoản & phân quyền người dùng, thông tin học kỳ, khóa sổ dữ liệu, thao tác danh mục / biểu in / import, chỉnh định view, tiến trình tự động, truy vết dữ liệu; **quản trị NetWEB** (chỉnh định menu, chỉnh định chung, cấm SV xem vì nợ học phí).

## Phần trên Edusoft
`Hệ thống/ Thông tin học kỳ/ …`, `Hệ thống/ Quản lý người dùng/ …`, `Hệ thống/ Quản trị hệ thống/ Chỉnh định thông số hệ thống`, `Hệ thống/ An toàn dữ liệu/ Khóa sổ phân hệ theo học kỳ`.

## Phần trên web / app
`Hệ thống/ Quản trị NetWEB/ Chỉnh định menu | Chỉnh định chung | Cấm SV xem vì nợ học phí` – **chỉnh trên Edusoft, kiểm kết quả trên web** (menu/chức năng ẩn-hiện, SV nợ HP không xem được…). Phân quyền quản trị trên web (PhanQuyenQuanTriTrenWeb).

## Test ở đâu
Tuỳ case: edusoft / web – xem lời KH nói về màn hình Edusoft hay trang web (bảng trên).

## Lưu ý khi test
Case bảo mật / đăng nhập (vd [[64724]]) thường là web + hệ thống – đọc kỹ KH nói trang nào. Không đổi phân quyền tài khoản thật.

---
Nguồn: Tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW, sheet Release(TestMenu) – Menu_NEW. Mã ACS ↔ phân hệ tài liệu là suy ra – người test xác nhận rồi đổi `trang_thai: da-xac-nhan`.

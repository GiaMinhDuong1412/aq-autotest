---
loai: trang-web
ten: "Thông báo, góp ý kiến"
vai_tro:
  - "sv"
  - "gv"
menu_web: "Thông báo từ ban quản trị · Góp ý kiến"
du_lieu:
  - "[[Cau hinh NetWEB]]"
ghi: []
phan_he:
  - "[[NETWEB-UI]]"
chinh_dinh:
  - "Trang quản trị /admin → Quản lý hỗ trợ người dùng / DS phân loại ý kiến (phòng ban nhận) · Gửi thông báo (từng SV hoặc từng lớp)"
  - "GH_MAILSERVER (Hệ thống / Quản trị hệ thống / Chỉnh định thông số hệ thống) – gửi mail tới bộ phận"
tu_khoa: "thông báo|góp ý|ý kiến|phản hồi"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NETWEB-QuanTriChung"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Thông báo, góp ý kiến"
tags: [trang-web]
---
# Thông báo, góp ý kiến

**Vai trò:** Sinh viên, Giảng viên · **Menu trên web:** Thông báo từ ban quản trị · Góp ý kiến · Tài liệu: [[HDSD NETWEB]] (`NETWEB-QuanTriChung`)

## Trên web
SV / GV xem thông báo chung của các phòng ban; gửi góp ý theo loại, admin chuyển mail cho phòng ban và trả lời.

## Lấy dữ liệu từ Edusoft
- [[Cau hinh NetWEB]]
- Trang quản trị: Ý kiến người dùng – "Gửi mail đến bộ phận liên quan", cột Trả lời, Xóa

## Ghi ngược về Edusoft
—

## Chỉnh định quyết định trang này
- Trang quản trị `/admin` → Quản lý hỗ trợ người dùng / DS phân loại ý kiến (phòng ban nhận) · Gửi thông báo (từng SV hoặc từng lớp)
- `GH_MAILSERVER` (`Hệ thống / Quản trị hệ thống / Chỉnh định thông số hệ thống`) – gửi mail tới bộ phận

## Kiểm tra liên kết khi test
- Thông báo gửi theo lớp: chỉ SV thuộc lớp đó thấy.
- Câu trả lời của admin phải hiện lại cho người gửi.
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).

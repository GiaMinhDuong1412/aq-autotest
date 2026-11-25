---
loai: trang-web
ten: "Cập nhật thông tin lý lịch"
vai_tro:
  - "sv"
menu_web: "Cập nhật thông tin lý lịch"
du_lieu:
  - "[[Danh muc sinh vien]]"
ghi:
  - "[[Danh muc sinh vien]]"
phan_he:
  - "[[QLSV]]"
chinh_dinh:
  - "Sinh viên / Thông tin sinh viên / Lý lịch sinh viên / Thời gian cập nhật thông tin SV trên Web (Ngày bắt đầu, Ngày kết thúc)"
  - "Sinh viên / Thông tin sinh viên / Lý lịch sinh viên / Chỉnh định thông tin lý lịch SV trên Web (cột Không hiệu chỉnh, Bắt buộc nhập)"
  - "Hệ thống / Quản trị NetWEB / Cấm SV xem khi chưa nhập đủ thông tin SV"
tu_khoa: "lý lịch|thông tin cá nhân|cập nhật thông tin|hồ sơ (sinh viên|sv)|bắt buộc nhập"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NetWEB_NhapLyLichSVTrucTuyen"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Cập nhật thông tin lý lịch"
tags: [trang-web]
---
# Cập nhật thông tin lý lịch

**Vai trò:** Sinh viên · **Menu trên web:** Cập nhật thông tin lý lịch · Tài liệu: [[HDSD NETWEB]] (`NetWEB_NhapLyLichSVTrucTuyen`)

## Trên web
SV sửa lý lịch theo 5 nhóm: Lý lịch, Gia đình, Liên lạc, Tuyển sinh, Hồ sơ (nút "Khác" để chuyển). Ô * bắt buộc, ô xám không sửa được.

## Lấy dữ liệu từ Edusoft
- [[Danh muc sinh vien]]
- Lý lịch sinh viên ở [[QLSV]] (Danh mục sinh viên)

## Ghi ngược về Edusoft
- [[Danh muc sinh vien]]

## Chỉnh định quyết định trang này
- Sinh viên / Thông tin sinh viên / Lý lịch sinh viên / Thời gian cập nhật thông tin SV trên Web (Ngày bắt đầu, Ngày kết thúc)
- Sinh viên / Thông tin sinh viên / Lý lịch sinh viên / Chỉnh định thông tin lý lịch SV trên Web (cột Không hiệu chỉnh, Bắt buộc nhập)
- Hệ thống / Quản trị NetWEB / Cấm SV xem khi chưa nhập đủ thông tin SV

## Kiểm tra liên kết khi test
- Ngoài thời gian: web báo "Ngoài thời gian nhập thông tin lý lịch, vui lòng kiểm tra lại." và **không có nút Lưu**.
- Lưu trên web → kiểm lý lịch SV đó trên Edusoft đã đổi đúng trường.
- Ô đánh dấu Không hiệu chỉnh phải xám; ô Bắt buộc nhập để trống thì không lưu được.
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).

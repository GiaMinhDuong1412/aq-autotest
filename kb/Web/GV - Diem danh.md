---
loai: trang-web
ten: "Điểm danh môn giảng dạy (QR, thủ công)"
vai_tro:
  - "gv"
  - "sv"
menu_web: "Điểm danh môn giảng dạy (cột QRCODE 'Link', cột Điểm danh)"
du_lieu:
  - "[[Thoi khoa bieu]]"
  - "[[KQ DKMH]]"
ghi:
  - "[[Diem danh]]"
phan_he:
  - "[[QLSV]]"
chinh_dinh: []
tu_khoa: "điểm danh|qr ?code|quét mã|vắng"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NetWEB_GiangVienDiemDanhSVTrucTuyen"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Điểm danh môn giảng dạy (QR, thủ công)"
tags: [trang-web]
---
# Điểm danh môn giảng dạy (QR, thủ công)

**Vai trò:** Giảng viên, Sinh viên · **Menu trên web:** Điểm danh môn giảng dạy (cột QRCODE "Link", cột Điểm danh) · Tài liệu: [[HDSD NETWEB]] (`NetWEB_GiangVienDiemDanhSVTrucTuyen`)

## Trên web
GV chọn ngày theo lịch dạy → hiện QR (đổi mỗi 30 giây) để SV quét, SV quét kịp → "Có mặt"; SV không quét được thì GV điểm danh thủ công + ghi chú → Lưu.

## Lấy dữ liệu từ Edusoft
- [[Thoi khoa bieu]]
- [[KQ DKMH]]
- Kết quả điểm danh xem / in ở Sinh viên / Điểm danh và Điểm rèn luyện ([[QLSV]])

## Ghi ngược về Edusoft
- [[Diem danh]]

## Chỉnh định quyết định trang này
— (chỉ phụ thuộc dữ liệu)

## Kiểm tra liên kết khi test
- QR hết hiệu lực sau 30 giây – quét mã cũ phải không điểm danh được.
- SV đã điểm danh bằng QR thì kết quả bị khóa, không đổi được ở điểm danh thủ công.
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).

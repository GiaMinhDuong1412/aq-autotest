---
loai: trang-web
ten: "Đăng ký cấp giấy chứng nhận (đơn từ trực tuyến)"
vai_tro:
  - "sv"
  - "khach"
menu_web: "Đăng ký cấp giấy chứng nhận · Xem giấy chứng nhận đã đăng ký · Tra cứu giấy xác nhận (#/xngiaydientu)"
du_lieu:
  - "[[Danh muc sinh vien]]"
ghi:
  - "[[Don tu truc tuyen]]"
phan_he:
  - "[[QLSV]]"
chinh_dinh:
  - "Hệ thống / Quản trị NetWEB / Chỉnh định chung: nhhk_dk_giay_chung_nhan (xử lý phải vào đúng NHHK đó)"
  - "Sinh viên / Quản lý dịch vụ / Cấp giấy chứng nhận / Danh mục giấy chứng nhận: tick **hiển thị trên Cổng thông tin**, tick **cho in trực tuyến**, gán nhóm (không nhóm = không qua giai đoạn xử lý)"
  - "Sinh viên / Quản lý dịch vụ / Cấp giấy chứng nhận / Danh mục nhóm giấy chứng nhận: tên hiện trên web, mail thông báo, đơn vị xử lý từng giai đoạn + số ngày"
  - "Sinh viên / Quản lý dịch vụ / Cấp giấy chứng nhận / Danh sách mẫu giấy chứng nhận · Định nghĩa bộ đếm GCN sinh viên"
  - "Hệ thống / Quản trị hệ thống / Quản lý danh mục / Quản lý hệ thống / Danh mục template gửi mail (Thư thông báo trễ hạn)"
tu_khoa: "giấy chứng nhận|giấy xác nhận|đơn từ|đơn trực tuyến|xngiaydientu|mã xác minh|phúc tra|in bảng điểm"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NETWEB_QuanLyDonTuTrucTuyen"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Đăng ký cấp giấy chứng nhận (đơn từ trực tuyến)"
tags: [trang-web]
---
# Đăng ký cấp giấy chứng nhận (đơn từ trực tuyến)

**Vai trò:** Sinh viên, Khách · **Menu trên web:** Đăng ký cấp giấy chứng nhận · Xem giấy chứng nhận đã đăng ký · Tra cứu giấy xác nhận (#/xngiaydientu) · Tài liệu: [[HDSD NETWEB]] (`NETWEB_QuanLyDonTuTrucTuyen`)

## Trên web
SV chọn loại giấy, điền thông tin, Lưu; theo dõi trạng thái từng giai đoạn; in trực tuyến nếu loại giấy cho phép. Đơn vị ngoài tra cứu giấy bằng mã xác minh + mã xác thực hoặc quét QR.

## Lấy dữ liệu từ Edusoft
- [[Danh muc sinh vien]]
- `Sinh viên / Quản lý dịch vụ / Cấp giấy chứng nhận` / Cập nhật giấy chứng nhận online – duyệt theo giai đoạn (Đang chờ duyệt / Không duyệt / Đang xử lý / Đã xử lý), phản hồi, gửi mail trễ hạn

## Ghi ngược về Edusoft
- [[Don tu truc tuyen]]

## Chỉnh định quyết định trang này
- `Hệ thống / Quản trị NetWEB / Chỉnh định chung`: `nhhk_dk_giay_chung_nhan` (xử lý phải vào đúng NHHK đó)
- `Sinh viên / Quản lý dịch vụ / Cấp giấy chứng nhận` / Danh mục giấy chứng nhận: tick **hiển thị trên Cổng thông tin**, tick **cho in trực tuyến**, gán nhóm (không nhóm = không qua giai đoạn xử lý)
- `Sinh viên / Quản lý dịch vụ / Cấp giấy chứng nhận` / Danh mục nhóm giấy chứng nhận: tên hiện trên web, mail thông báo, đơn vị xử lý từng giai đoạn + số ngày
- `Sinh viên / Quản lý dịch vụ / Cấp giấy chứng nhận` / Danh sách mẫu giấy chứng nhận · Định nghĩa bộ đếm GCN sinh viên
- Hệ thống / Quản trị hệ thống / Quản lý danh mục / Quản lý hệ thống / Danh mục template gửi mail (Thư thông báo trễ hạn)

## Kiểm tra liên kết khi test
- SV chỉ **hủy** được đơn đang "Đang chờ duyệt".
- Nhiều giai đoạn: giai đoạn trước chưa duyệt thì giai đoạn sau không xử lý được.
- Trạng thái / phản hồi cập nhật trên Edusoft phải hiện đúng trên web.
- Loại giấy bỏ tick hiển thị thì không còn trên web.
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).

---
loai: trang-web
ten: "Đánh giá rèn luyện (SV, CVHT, thư ký khoa)"
vai_tro:
  - "sv"
  - "gv"
menu_web: "Đánh giá kết quả rèn luyện"
du_lieu:
  - "[[Hoc ky]]"
  - "[[Diem ren luyen]]"
  - "[[Lop sinh vien]]"
  - "[[Vien chuc]]"
ghi:
  - "[[Diem ren luyen]]"
phan_he:
  - "[[QLSV]]"
chinh_dinh:
  - "Hệ thống / Quản trị NetWEB / Chỉnh định chung: nhhk_danh_gia_ren_luyen, xl_sv_nhap_hoat_dong_ren_luyen, xl_up_load_file_minh_chung_tieu_chi_danh_gia"
  - "Sinh viên / Quản trị phân hệ / Chỉnh định thông số toàn cục: GS_BOXHDIEMRL (bộ xếp hạng)"
  - "Quản lý điểm / Quản trị phân hệ / Quản lý danh mục / Danh mục đánh giá · Danh mục xếp hạng"
  - "Sinh viên / Điểm danh và Điểm rèn luyện / Quản lý điểm rèn luyện / Điểm rèn luyện thành phần / Danh sách nhóm câu hỏi · Danh sách câu hỏi · **Thời gian đánh giá online** (riêng cho Sinh viên, CVHT, Khoa)"
  - "Nhân sự / Danh sách viên chức / Nhập thông tin thư ký khoa (quyền 'Thư ký / giáo vụ khoa')"
tu_khoa: "rèn luyện|đrl|drl|minh chứng|tự đánh giá|cvht đánh giá|thư ký khoa"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NetWEB_NhapDRLTrucTuyen"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Đánh giá rèn luyện (SV, CVHT, thư ký khoa)"
tags: [trang-web]
---
# Đánh giá rèn luyện (SV, CVHT, thư ký khoa)

**Vai trò:** Sinh viên, Giảng viên · **Menu trên web:** Đánh giá kết quả rèn luyện · Tài liệu: [[HDSD NETWEB]] (`NetWEB_NhapDRLTrucTuyen`)

## Trên web
SV tự chấm từng câu (kèm minh chứng, hoạt động) → CVHT chấm cột "Điểm CVHT" → thư ký khoa chấm cột "Điểm khoa"; có nút copy điểm SV → CVHT → Khoa.

## Lấy dữ liệu từ Edusoft
- [[Hoc ky]]
- [[Diem ren luyen]]
- [[Lop sinh vien]]
- [[Vien chuc]]
- `Sinh viên / Điểm danh và Điểm rèn luyện / Quản lý điểm rèn luyện` / Điểm rèn luyện thành phần / Import điểm rèn luyện · Kết quả đánh giá rèn luyện · In tổng hợp kết quả · Xem tiến độ CVHT đánh giá
- `Sinh viên / Điểm danh và Điểm rèn luyện / Quản lý điểm rèn luyện` / Điểm rèn luyện / Nhập điểm rèn luyện → nút **Đồng bộ ĐRL online** (lấy cột SV / CVHT / Khoa)

## Ghi ngược về Edusoft
- [[Diem ren luyen]]

## Chỉnh định quyết định trang này
- `Hệ thống / Quản trị NetWEB / Chỉnh định chung`: `nhhk_danh_gia_ren_luyen`, `xl_sv_nhap_hoat_dong_ren_luyen`, `xl_up_load_file_minh_chung_tieu_chi_danh_gia`
- Sinh viên / Quản trị phân hệ / Chỉnh định thông số toàn cục: `GS_BOXHDIEMRL` (bộ xếp hạng)
- Quản lý điểm / Quản trị phân hệ / Quản lý danh mục / Danh mục đánh giá · Danh mục xếp hạng
- `Sinh viên / Điểm danh và Điểm rèn luyện / Quản lý điểm rèn luyện` / Điểm rèn luyện thành phần / Danh sách nhóm câu hỏi · Danh sách câu hỏi · **Thời gian đánh giá online** (riêng cho Sinh viên, CVHT, Khoa)
- Nhân sự / Danh sách viên chức / Nhập thông tin thư ký khoa (quyền "Thư ký / giáo vụ khoa")

## Kiểm tra liên kết khi test
- Mỗi vai trò có **thời gian riêng**: ngoài thời gian thì cột của vai trò đó không nhập được.
- CVHT chỉ thấy lớp mình quản lý; thư ký khoa chỉ thấy lớp thuộc khoa.
- Điểm trên web **chưa vào Edusoft** cho tới khi bấm Đồng bộ ĐRL online – kiểm cả bước đồng bộ.
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).

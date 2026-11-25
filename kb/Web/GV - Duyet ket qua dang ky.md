---
loai: trang-web
ten: "Duyệt kết quả đăng ký môn học (CVHT)"
vai_tro:
  - "gv"
menu_web: "Duyệt kết quả đăng ký sinh viên"
du_lieu:
  - "[[KQ DKMH]]"
  - "[[Lop sinh vien]]"
ghi:
  - "[[KQ DKMH]]"
phan_he:
  - "[[DKMH]]"
chinh_dinh:
  - "Đăng ký MH / Đăng ký môn học / Ràng buộc đăng ký online / Chỉnh định chung: xl_so_ngay_gv_duyet_sau_ngay_svdk (số ngày cho CVHT duyệt sau đợt SV đăng ký), xl_cho_cvht_dk (Có = CVHT được thêm / xóa môn cho SV; Không = chỉ xem và góp ý)"
tu_khoa: "duyệt (kết quả|kq) đăng ký|cvht duyệt|cố vấn học tập|duyệt tất cả|duyệt nhanh"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NetWEB_GiangVienDuyetKQDK"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Duyệt kết quả đăng ký môn học (CVHT)"
tags: [trang-web]
---
# Duyệt kết quả đăng ký môn học (CVHT)

**Vai trò:** Giảng viên · **Menu trên web:** Duyệt kết quả đăng ký sinh viên · Tài liệu: [[HDSD NETWEB]] (`NetWEB_GiangVienDuyetKQDK`)

## Trên web
CVHT xem danh sách SV: Trạng thái Chưa duyệt / Đồng ý; Đăng nhập vào từng SV để xem và Đồng ý / Không đồng ý + lời khuyên; Duyệt nhanh từng SV hoặc Duyệt tất cả.

## Lấy dữ liệu từ Edusoft
- [[KQ DKMH]]
- [[Lop sinh vien]]
- `Đăng ký MH / Đăng ký môn học / Ràng buộc đăng ký online` / Thống kê GV duyệt KQDK online

## Ghi ngược về Edusoft
- [[KQ DKMH]]

## Chỉnh định quyết định trang này
- `Đăng ký MH / Đăng ký môn học / Ràng buộc đăng ký online` / Chỉnh định chung: `xl_so_ngay_gv_duyet_sau_ngay_svdk` (số ngày cho CVHT duyệt sau đợt SV đăng ký), `xl_cho_cvht_dk` (Có = CVHT được thêm / xóa môn cho SV; Không = chỉ xem và góp ý)

## Kiểm tra liên kết khi test
- `xl_cho_cvht_dk` = Không thì CVHT **không** được thêm / xóa môn của SV.
- Hết số ngày cho duyệt thì không duyệt được.
- Kết quả duyệt phải lên Thống kê GV duyệt KQDK online trên Edusoft.
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).

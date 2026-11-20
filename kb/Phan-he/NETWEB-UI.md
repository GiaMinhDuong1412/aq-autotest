---
loai: phan-he
ma: NETWEB-UI
ten: Giao diện cổng Netweb
san_pham: "[[Netweb]]"
test_tren:
  - web
tab_edusoft: —
nhan_tu:
  - "[[KHGD]]"
  - "[[QLHT]]"
dua_sang: []
dau_hieu: trang, giao diện, hiển thị, menu web, banner, đơn vị phân cấp / điều hướng cơ sở, demo NetWEB
nguon: tai-lieu
trang_thai: tu-tai-lieu
---
# NETWEB-UI – Giao diện cổng Netweb

## Là gì
Giao diện cổng web của trường cho SV / GV / phụ huynh / khách (link dạng `https://<site>/#/home`). Tài liệu: thư mục NETWEB (QuanTriChung, TaiLieuHuongDanSinhVien, GiangVien…, PhuHuynh, Guest…).

## Nhận dữ liệu từ
- [[Tai khoan va phan quyen|Tài khoản & phân quyền]] từ [[QLHT]] – phân quyền quản trị trên web
- [[Cau hinh NetWEB|Cấu hình NetWEB]] từ [[QLHT]] – menu / chức năng ẩn-hiện, chặn SV nợ học phí
- [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]] từ [[KHGD]] – điều hướng theo khối lớp / cơ sở (DHNT)

## Tạo ra
—

## Đưa sang
—

## Sửa ở đây → kiểm lại
Không có phân hệ nào nhận dữ liệu trực tiếp.
Lỗi có thể do dữ liệu đầu vào từ: [[KHGD]], [[QLHT]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
Cấu hình web nằm ở `Hệ thống/ Quản trị NetWEB/ …` trên Edusoft ([[QLHT]]).

## Phần trên web / app
Test trên **cổng web test** của trường, đăng nhập đúng vai trò. Trường nhiều cơ sở có **điều hướng theo cơ sở / đơn vị phân cấp (DVPC)**: SV/GV đăng nhập ở trang chính rồi được chuyển sang site của cơ sở (xem [[DHNT]]).


## Dạng case thường gặp
[[Hien thi web]], [[Tai khoan phan quyen]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Chỉ web.

## Lưu ý
Không chạy kịch bản Edusoft cho sửa giao diện web.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

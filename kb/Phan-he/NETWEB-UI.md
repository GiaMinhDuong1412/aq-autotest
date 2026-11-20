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
aliases:
  - "Giao diện cổng Netweb"
  - "NetWEB"
  - "Web"
quy_trinh:
  - "[[02 Tuyen sinh - nhap hoc]]"
  - "[[04 Dang ky mon hoc]]"
  - "[[05 Hoc phi - thu - thanh toan]]"
  - "[[07 Diem - hoc vu - hoc bong]]"
  - "[[09 Hoat dong tren lop]]"
  - "[[12 Tai khoan - phan quyen - web]]"
tags: [phan-he]
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

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được NETWEB-UI phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[KHGD]] – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]], [[Mon hoc|Môn học]], [[Phong hoc|Phòng học kỳ]], [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]], [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]], [[Thoi khoa bieu|Thời khóa biểu]]
2. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]], [[Tai khoan va phan quyen|Tài khoản & phân quyền]], [[Cau hinh NetWEB|Cấu hình NetWEB]]
3. [[QLNS]] – [[Vien chuc|Viên chức / cán bộ giảng dạy]]
4. [[QLTS]] – [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]], [[Ho so thi sinh|Hồ sơ thí sinh]], [[DS trung tuyen|Danh sách trúng tuyển]]
5. [[QLSV]] – [[Lop sinh vien|Lớp sinh viên]], [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]], [[DS SV hoc ky|Danh sách sinh viên học kỳ]]
6. [[DKMH]] – [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]], [[KQ DKMH|Kết quả đăng ký môn học]]
7. **NETWEB-UI** – [[Diem danh|Điểm danh (chuyên cần)]]

**Sửa dữ liệu của NETWEB-UI → kiểm lại:** phân hệ dùng trực tiếp [[DIEM]].

## Nằm trong quy trình
- [[02 Tuyen sinh - nhap hoc|Tuyển sinh → nhập học → có sinh viên]]
- [[04 Dang ky mon hoc|Đăng ký môn học]]
- [[05 Hoc phi - thu - thanh toan|Học phí: tính → nợ → thu → thanh toán online]]
- [[07 Diem - hoc vu - hoc bong|Điểm → điểm TB → học vụ, học bổng]]
- [[09 Hoat dong tren lop|Hoạt động trên lớp: điểm danh, nghỉ dạy – dạy bù, khảo sát]]
- [[12 Tai khoan - phan quyen - web|Tài khoản, phân quyền, cấu hình web (dùng chung)]]

## Tài liệu
- [[HDSD NETWEB]]
- [[HDSD NhapHocOnline]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
Không chạy kịch bản Edusoft cho sửa giao diện web.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

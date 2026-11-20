---
loai: phan-he
ma: DKMHUI
ten: Giao diện web đăng ký môn học
san_pham: "[[Netweb]]"
test_tren:
  - web
tab_edusoft: —
nhan_tu:
  - "[[DKMH]]"
dua_sang: []
dau_hieu: trang đăng ký môn học, site ĐKMH, rút môn trên web, thông báo trên trang đăng ký, lặp dòng khi hiển thị
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Giao diện web đăng ký môn học"
  - "Trang ĐKMH riêng"
quy_trinh:
  - "[[04 Dang ky mon hoc]]"
tags: [phan-he]
---
# DKMHUI – Giao diện web đăng ký môn học

## Là gì
Phần **giao diện web** của đăng ký môn học (trang ĐKMH – nhiều trường tách riêng khỏi cổng SV để chịu tải).

## Nhận dữ liệu từ
- [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]] từ [[DKMH]] – web chặn / mở đăng ký theo ràng buộc

## Tạo ra
—

## Đưa sang
—

## Sửa ở đây → kiểm lại
Không có phân hệ nào nhận dữ liệu trực tiếp.
Lỗi có thể do dữ liệu đầu vào từ: [[DKMH]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
Cài đặt nằm ở [[DKMH]] trên Edusoft (thời gian, ràng buộc).

## Phần trên web / app
Test trên **trang ĐKMH / cổng SV test** của trường, tài khoản SV (và GV-CVHT nếu duyệt).


## Dạng case thường gặp
[[Hien thi web]], [[Hieu nang]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Chỉ web.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được DKMHUI phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[KHGD]] – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]], [[Mon hoc|Môn học]]
2. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]]
3. [[QLSV]] – [[Lop sinh vien|Lớp sinh viên]]
4. [[DKMH]] – [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]]
5. **DKMHUI** – dùng dữ liệu trên

## Nằm trong quy trình
- [[04 Dang ky mon hoc|Đăng ký môn học]]

## Tài liệu
- [[HDSD DKMH]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
Thông báo / lặp dòng / hiển thị → test web; nói tới "setting" thì kiểm thêm chỗ cài trên Edusoft ([[DKMH]]).

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

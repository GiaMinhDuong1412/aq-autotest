---
loai: phan-he
ma: QXHV
ten: Xét học vụ
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
tab_edusoft: Quản lý điểm
nhan_tu:
  - "[[DIEM]]"
  - "[[QLSV]]"
dua_sang:
  - "[[QLSV]]"
dau_hieu: học vụ, vi phạm, cảnh báo học tập, buộc thôi học
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Xét học vụ"
  - "Học vụ"
quy_trinh:
  - "[[07 Diem - hoc vu - hoc bong]]"
tags: [phan-he]
---
# QXHV – Xét học vụ

## Là gì
Tiêu chuẩn xét + đợt xét → DS lớp xét → DS SV xét → xét học vụ → DS SV vi phạm (lưu đồ QXHV). Cùng khuôn với xét tốt nghiệp.

## Nhận dữ liệu từ
- [[Lop sinh vien|Lớp sinh viên]] từ [[QLSV]] – DS lớp xét
- [[DS SV hoc ky|Danh sách sinh viên học kỳ]] từ [[QLSV]] – DS SV xét
- [[Diem trung binh|Điểm trung bình – tích lũy]] từ [[DIEM]] – xét học vụ

## Tạo ra
- [[Ket qua hoc vu|Kết quả xét học vụ]]

## Đưa sang
- [[Ket qua hoc vu|Kết quả xét học vụ]] → [[QLSV]]

## Sửa ở đây → kiểm lại
Các phân hệ nhận dữ liệu của QXHV: [[QLSV]].
Lỗi có thể do dữ liệu đầu vào từ: [[DIEM]], [[QLSV]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
`Quản lý điểm/ Xử lý học vụ học kỳ/ …`.

## Phần trên web / app
—


## Dạng case thường gặp
[[So lieu tinh sai]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Chỉ edusoft.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được QXHV phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[KHGD]] – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]], [[Mon hoc|Môn học]], [[Phong hoc|Phòng học kỳ]], [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]], [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]], [[Thoi khoa bieu|Thời khóa biểu]]
2. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]]
3. [[QLNS]] – [[Vien chuc|Viên chức / cán bộ giảng dạy]]
4. [[QLTS]] – [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]], [[Ho so thi sinh|Hồ sơ thí sinh]], [[DS trung tuyen|Danh sách trúng tuyển]]
5. [[QLSV]] – [[Lop sinh vien|Lớp sinh viên]], [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]], [[DS SV hoc ky|Danh sách sinh viên học kỳ]]
6. [[DKMH]] – [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]], [[KQ DKMH|Kết quả đăng ký môn học]]
7. [[LTHI]] – [[Danh sach thi|Danh sách thi – lịch thi]]
8. [[DIEM]] – [[Diem mon hoc|Điểm môn học]], [[Diem trung binh|Điểm trung bình – tích lũy]]
9. **QXHV** – [[Ket qua hoc vu|Kết quả xét học vụ]]

**Sửa dữ liệu của QXHV → kiểm lại:** phân hệ dùng trực tiếp [[QLSV]].

## Nằm trong quy trình
- [[07 Diem - hoc vu - hoc bong|Điểm → điểm TB → học vụ, học bổng]]

## Tài liệu
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
Nằm trong tab Quản lý điểm nhưng là quy trình riêng – mã ACS có thể là DIEM.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

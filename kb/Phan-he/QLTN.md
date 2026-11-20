---
loai: phan-he
ma: QLTN
ten: Tốt nghiệp
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
tab_edusoft: Tốt nghiệp
nhan_tu:
  - "[[DIEM]]"
  - "[[KHGD]]"
  - "[[QLSV]]"
dua_sang:
  - "[[QLSV]]"
dau_hieu: xét tốt nghiệp, tiêu chuẩn, danh sách xét, luận văn, in danh sách tốt nghiệp
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Tốt nghiệp"
  - "Tốt nghiệp"
quy_trinh:
  - "[[08 Tot nghiep - luan van]]"
tags: [phan-he]
---
# QLTN – Tốt nghiệp

## Là gì
Tiêu chuẩn → DS SV xét → xét theo đợt → kết quả / DS không tốt nghiệp → in DS kèm quyết định; luận văn tốt nghiệp (lưu đồ QLTN, BVLV).

## Nhận dữ liệu từ
- [[Mon hoc|Môn học]] từ [[KHGD]] – môn bắt buộc / tự chọn trong tiêu chuẩn
- [[Lop sinh vien|Lớp sinh viên]] từ [[QLSV]] – DS lớp xét
- [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]] từ [[KHGD]] – tiêu chuẩn tốt nghiệp theo chương trình
- [[DS SV hoc ky|Danh sách sinh viên học kỳ]] từ [[QLSV]] – DS SV xét
- [[Diem trung binh|Điểm trung bình – tích lũy]] từ [[DIEM]] – xét tốt nghiệp

## Tạo ra
- [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]]

## Đưa sang
- [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]] → [[QLSV]]

## Sửa ở đây → kiểm lại
Các phân hệ nhận dữ liệu của QLTN: [[QLSV]].
Lỗi có thể do dữ liệu đầu vào từ: [[DIEM]], [[KHGD]], [[QLSV]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
`Tốt nghiệp/ Xét tốt nghiệp/ …`.
Menu: [[Menu/QLTN|272 menu của QLTN]] – menu tạo dữ liệu: [[Menu/Chuyển điểm luận văn vào môn học (QLV04.06)|Chuyển điểm luận văn vào môn học]], [[Menu/Nhập điểm bảo vệ luận văn (QLV04.04)|Nhập điểm bảo vệ luận văn]], [[Menu/Danh sách sinh viên tốt nghiệp (Q56.01)|Danh sách sinh viên tốt nghiệp]].

## Phần trên web / app
NetWEB SV: xem kết quả xét tốt nghiệp / tiền tốt nghiệp; đăng ký đề tài tốt nghiệp (tuỳ trường).


## Dạng case thường gặp
[[Mau in bao cao]], [[So lieu tinh sai]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: edusoft / web – xem KH nói về màn hình Edusoft hay trang web.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được QLTN phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[KHGD]] – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]], [[Mon hoc|Môn học]], [[Phong hoc|Phòng học kỳ]], [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]], [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]], [[Thoi khoa bieu|Thời khóa biểu]]
2. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]]
3. [[QLNS]] – [[Vien chuc|Viên chức / cán bộ giảng dạy]]
4. [[QLTS]] – [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]], [[Ho so thi sinh|Hồ sơ thí sinh]], [[DS trung tuyen|Danh sách trúng tuyển]]
5. [[QLSV]] – [[Lop sinh vien|Lớp sinh viên]], [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]], [[DS SV hoc ky|Danh sách sinh viên học kỳ]]
6. [[DKMH]] – [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]], [[KQ DKMH|Kết quả đăng ký môn học]]
7. [[LTHI]] – [[Danh sach thi|Danh sách thi – lịch thi]]
8. [[DIEM]] – [[Diem mon hoc|Điểm môn học]], [[Diem trung binh|Điểm trung bình – tích lũy]]
9. **QLTN** – [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]]

**Sửa dữ liệu của QLTN → kiểm lại:** phân hệ dùng trực tiếp [[QLSV]].

## Nằm trong quy trình
- [[08 Tot nghiep - luan van|Luận văn → xét tốt nghiệp → quyết định tốt nghiệp]]

## Tài liệu
- [[HDSD QLTN]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
—

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

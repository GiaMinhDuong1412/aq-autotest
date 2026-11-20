---
loai: phan-he
ma: KHGD
ten: Kế hoạch giảng dạy / thời khóa biểu
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
tab_edusoft: Kế hoạch
nhan_tu:
  - "[[QLHT]]"
  - "[[QLNS]]"
  - "[[QLSV]]"
dua_sang:
  - "[[CSHP]]"
  - "[[DIEM]]"
  - "[[DKMH]]"
  - "[[KLGD]]"
  - "[[KSDG]]"
  - "[[LTHI]]"
  - "[[NETWEB-UI]]"
  - "[[QLSV]]"
  - "[[QLTN]]"
dau_hieu: CTĐT, lớp học kỳ, nhóm học phần, nhóm tổ, xếp TKB, phòng học, nghỉ dạy dạy bù
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Kế hoạch giảng dạy / thời khóa biểu"
  - "Kế hoạch giảng dạy"
  - "TKB"
quy_trinh:
  - "[[03 CTDT - TKB]]"
  - "[[04 Dang ky mon hoc]]"
  - "[[06 To chuc thi]]"
  - "[[08 Tot nghiep - luan van]]"
  - "[[09 Hoat dong tren lop]]"
  - "[[10 Nhan su - khoi luong giang day]]"
tags: [phan-he]
---
# KHGD – Kế hoạch giảng dạy / thời khóa biểu

## Là gì
CTĐT (chuẩn → kế hoạch → thực hiện), DS lớp / phòng / viên chức học kỳ, quy hoạch nhóm học phần, xếp TKB tự động, hiệu chỉnh TKB, nghỉ dạy – dạy bù, sử dụng phòng (lưu đồ CTDT, QTKB).

## Nhận dữ liệu từ
- [[Hoc ky|Năm học – học kỳ]] từ [[QLHT]] – lớp / phòng / viên chức / nhóm học / TKB học kỳ
- [[Lop sinh vien|Lớp sinh viên]] từ [[QLSV]] – DS lớp học kỳ, biểu đồ KHHT lớp
- [[Vien chuc|Viên chức / cán bộ giảng dạy]] từ [[QLNS]] – gán giảng viên cho nhóm học

## Tạo ra
- [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]]
- [[Mon hoc|Môn học]]
- [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]]
- [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]]
- [[Phong hoc|Phòng học kỳ]]
- [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]]
- [[Thoi khoa bieu|Thời khóa biểu]]

## Đưa sang
- [[Mon hoc|Môn học]] → [[DKMH]], [[CSHP]], [[DIEM]], [[KLGD]], [[QLTN]]
- [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]] → [[QLSV]], [[DIEM]], [[NETWEB-UI]]
- [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]] → [[QLTN]], [[DKMH]]
- [[Phong hoc|Phòng học kỳ]] → [[LTHI]]
- [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]] → [[DKMH]], [[LTHI]], [[KSDG]], [[KLGD]], [[DIEM]]
- [[Thoi khoa bieu|Thời khóa biểu]] → [[DKMH]], [[LTHI]], [[KLGD]]

## Sửa ở đây → kiểm lại
Các phân hệ nhận dữ liệu của KHGD: [[CSHP]], [[DIEM]], [[DKMH]], [[KLGD]], [[KSDG]], [[LTHI]], [[NETWEB-UI]], [[QLSV]], [[QLTN]].
Lỗi có thể do dữ liệu đầu vào từ: [[QLHT]], [[QLNS]], [[QLSV]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
`Kế hoạch/ Chương trình đào tạo/ …`, `Kế hoạch/ Qui hoạch nhóm học phần/ …`, `Kế hoạch/ Thời khóa biểu/ …`.
Menu: [[Menu/KHGD|213 menu của KHGD]] – menu tạo dữ liệu: [[Menu/CTĐT chuẩn (K41.02)|CTĐT chuẩn]], [[Menu/CTĐT kế hoạch (K41.03)|CTĐT kế hoạch]], [[Menu/CTĐT thực hiện (K41.04)|CTĐT thực hiện]], [[Menu/Danh mục môn học (K4_DMMH)|Danh mục môn học]], [[Menu/Danh sách phòng học kỳ (K0.2)|Danh sách phòng học kỳ]], [[Menu/Danh sách nhóm tổ (K81_1)|Danh sách nhóm tổ]], [[Menu/Xếp thời khóa biểu tự động (K112)|Xếp thời khóa biểu tự động]], [[Menu/Xếp thời khóa biểu tự động (K.105)|Xếp thời khóa biểu tự động]].

## Phần trên web / app
SV + GV xem TKB dạng tuần / học kỳ, SV xem CTĐT và môn tiên quyết, GV đăng ký nghỉ dạy – dạy bù online.


## Dạng case thường gặp
[[Loi EX Edusoft]], [[Luu cap nhat khong duoc]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: edusoft / web – xem KH nói về màn hình Edusoft hay trang web.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được KHGD phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]]
2. [[QLNS]] – [[Vien chuc|Viên chức / cán bộ giảng dạy]]
3. [[QLTS]] – [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]], [[Ho so thi sinh|Hồ sơ thí sinh]], [[DS trung tuyen|Danh sách trúng tuyển]]
4. [[QLSV]] – [[Lop sinh vien|Lớp sinh viên]], [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]], [[DS SV hoc ky|Danh sách sinh viên học kỳ]]
5. **KHGD** – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]], [[Mon hoc|Môn học]], [[Phong hoc|Phòng học kỳ]], [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]], [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]], [[Thoi khoa bieu|Thời khóa biểu]]

**Sửa dữ liệu của KHGD → kiểm lại:** phân hệ dùng trực tiếp [[CSHP]], [[DIEM]], [[DKMH]], [[KLGD]], [[KSDG]], [[LTHI]], [[NETWEB-UI]], [[QLSV]], [[QLTN]]; dữ liệu sinh ra từ đó (theo thứ tự): [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]] (QLTS), [[Ho so thi sinh|Hồ sơ thí sinh]] (QLTS), [[Lop sinh vien|Lớp sinh viên]] (QLSV), [[DS trung tuyen|Danh sách trúng tuyển]] (QLTS), [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]] (DKMH), [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]] (QLSV), [[DS SV hoc ky|Danh sách sinh viên học kỳ]] (QLSV), [[Danh muc sinh vien|Danh mục sinh viên (mọi SV của trường)]] (QLSV), [[Diem luan van|Điểm luận văn]] (BVLV), [[Diem ren luyen|Điểm rèn luyện]] (QLSV), [[Dien chinh sach|Diện chính sách / miễn giảm]] (QLSV), [[Hop dong KTX|Hợp đồng ký túc xá]] (QKTX), [[Ket qua khao sat|Kết quả khảo sát]] (KSDG), [[KQ DKMH|Kết quả đăng ký môn học]] (DKMH), [[Khoi luong giang day|Khối lượng giảng dạy]] (KLGD), [[Danh sach thi|Danh sách thi – lịch thi]] (LTHI), [[Diem danh|Điểm danh (chuyên cần)]] (NETWEB-UI), [[Hoc phi|Học phí phải thu (đã tính)]] (CSHP), [[Diem mon hoc|Điểm môn học]] (DIEM), [[Phieu thu|Phiếu thu học phí]] (QLTV), [[Diem trung binh|Điểm trung bình – tích lũy]] (DIEM), [[No hoc phi|Nợ học phí]] (CSHP), [[Ket qua hoc vu|Kết quả xét học vụ]] (QXHV), [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]] (QLTN).

## Nằm trong quy trình
- [[03 CTDT - TKB|Chương trình đào tạo → nhóm học → thời khoá biểu]]
- [[04 Dang ky mon hoc|Đăng ký môn học]]
- [[06 To chuc thi|Tổ chức thi]]
- [[08 Tot nghiep - luan van|Luận văn → xét tốt nghiệp → quyết định tốt nghiệp]]
- [[09 Hoat dong tren lop|Hoạt động trên lớp: điểm danh, nghỉ dạy – dạy bù, khảo sát]]
- [[10 Nhan su - khoi luong giang day|Nhân sự → phân công giảng dạy → khối lượng giảng dạy]]

## Tài liệu
- [[HDSD KHGD]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
Xếp TKB ảnh hưởng ĐKMH, thi, khảo sát – chỉ thử trên học kỳ test.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

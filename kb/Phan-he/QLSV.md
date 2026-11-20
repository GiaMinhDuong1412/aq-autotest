---
loai: phan-he
ma: QLSV
ten: Quản lý sinh viên
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
tab_edusoft: Sinh viên
nhan_tu:
  - "[[DIEM]]"
  - "[[DKMH]]"
  - "[[KHGD]]"
  - "[[QLHT]]"
  - "[[QLTN]]"
  - "[[QLTS]]"
  - "[[QXHV]]"
dua_sang:
  - "[[CSHP]]"
  - "[[DKMH]]"
  - "[[KHGD]]"
  - "[[KSDG]]"
  - "[[NETWEB-API]]"
  - "[[QKTX]]"
  - "[[QLTN]]"
  - "[[QLTS]]"
  - "[[QXHV]]"
dau_hieu: quyết định vào/ra, lý lịch, hồ sơ văn bằng, khen thưởng, học bổng, miễn giảm chính sách, điểm danh, rèn luyện, tốt nghiệp, giấy chứng nhận, cố vấn
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Quản lý sinh viên"
  - "Quản lý sinh viên"
quy_trinh:
  - "[[02 Tuyen sinh - nhap hoc]]"
  - "[[03 CTDT - TKB]]"
  - "[[04 Dang ky mon hoc]]"
  - "[[05 Hoc phi - thu - thanh toan]]"
  - "[[07 Diem - hoc vu - hoc bong]]"
  - "[[08 Tot nghiep - luan van]]"
  - "[[09 Hoat dong tren lop]]"
  - "[[11 Ky tuc xa]]"
tags: [phan-he]
---
# QLSV – Quản lý sinh viên

## Là gì
Quyết định vào mới / đổi lớp / nghỉ / tạm dừng / học lại, DS SV học kỳ, lý lịch, hồ sơ – văn bằng, khen thưởng, diện chính sách & học bổng, điểm danh, điểm rèn luyện, thông tin tốt nghiệp, cấp giấy chứng nhận, cố vấn học tập (nghiệp vụ: skill `tailieu-edusoft/nghiep-vu/QLSV.md`).

## Nhận dữ liệu từ
- [[Hoc ky|Năm học – học kỳ]] từ [[QLHT]] – DS SV học kỳ, quyết định theo học kỳ
- [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]] từ [[KHGD]] – lớp sinh viên thuộc khối
- [[DS trung tuyen|Danh sách trúng tuyển]] từ [[QLTS]] – SV trúng tuyển → Quyết định vào mới
- [[KQ DKMH|Kết quả đăng ký môn học]] từ [[DKMH]] – điểm danh; xóa kết quả SV đã hủy ĐKMH
- [[Diem trung binh|Điểm trung bình – tích lũy]] từ [[DIEM]] – xét học bổng
- [[Ket qua hoc vu|Kết quả xét học vụ]] từ [[QXHV]] – SV vi phạm (cảnh báo / thôi học) – cần xác nhận cách đưa sang quyết định
- [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]] từ [[QLTN]] – Quyết định tốt nghiệp → xóa tên khỏi DS SV học kỳ kỳ sau, thông tin tốt nghiệp, in bằng

## Tạo ra
- [[Lop sinh vien|Lớp sinh viên]]
- [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]]
- [[Danh muc sinh vien|Danh mục sinh viên (mọi SV của trường)]]
- [[DS SV hoc ky|Danh sách sinh viên học kỳ]]
- [[Dien chinh sach|Diện chính sách / miễn giảm]]
- [[Diem ren luyen|Điểm rèn luyện]]

## Đưa sang
- [[Lop sinh vien|Lớp sinh viên]] → [[QLTS]], [[KHGD]], [[DKMH]], [[QXHV]], [[QLTN]]
- [[Danh muc sinh vien|Danh mục sinh viên (mọi SV của trường)]] → [[NETWEB-API]]
- [[DS SV hoc ky|Danh sách sinh viên học kỳ]] → [[DKMH]], [[CSHP]], [[KSDG]], [[QXHV]], [[QLTN]], [[QKTX]]
- [[Dien chinh sach|Diện chính sách / miễn giảm]] → [[CSHP]]

## Sửa ở đây → kiểm lại
Các phân hệ nhận dữ liệu của QLSV: [[CSHP]], [[DKMH]], [[KHGD]], [[KSDG]], [[NETWEB-API]], [[QKTX]], [[QLTN]], [[QLTS]], [[QXHV]].
Lỗi có thể do dữ liệu đầu vào từ: [[DIEM]], [[DKMH]], [[KHGD]], [[QLHT]], [[QLTN]], [[QLTS]], [[QXHV]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
`Sinh viên/ Sinh viên học kỳ/ …`, `Sinh viên/ Thông tin sinh viên/ …`, `Sinh viên/ Hồ sơ và Văn bằng/ …`, `Sinh viên/ Miễn giảm hoc phí và Học bổng/ …`, `Sinh viên/ Điểm danh và Điểm rèn luyện/ …`.
Menu: [[Menu/QLSV|332 menu của QLSV]] – menu tạo dữ liệu: [[Menu/Diện chính sách sinh viên học kỳ (S163)|Diện chính sách sinh viên học kỳ]], [[Menu/Danh mục lớp (S13)|Danh mục lớp]], [[Menu/Danh mục sinh viên (S11)|Danh mục sinh viên]], [[Menu/Danh sách sinh viên học kỳ (S12)|Danh sách sinh viên học kỳ]], [[Menu/Quyết định vào mới (S15.04)|Quyết định vào mới]], [[Menu/Nhập điểm rèn luyện (S83.05)|Nhập điểm rèn luyện]], [[Menu/Tổng kết điểm rèn luyện (S83.06)|Tổng kết điểm rèn luyện]].

## Phần trên web / app
NetWEB SV: cập nhật lý lịch (theo thời gian mở ở Edusoft), xem kết quả điểm danh, đánh giá điểm rèn luyện, tra cứu tốt nghiệp, đăng ký cấp giấy chứng nhận / bảng điểm. NetWEB GV: điểm danh môn giảng dạy, xem DS SV quản lý (CVHT).


## Dạng case thường gặp
[[Hien thi web]], [[Loi EX Edusoft]], [[Luu cap nhat khong duoc]], [[Xu ly du lieu]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: edusoft / web – xem KH nói về màn hình Edusoft hay trang web.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được QLSV phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[KHGD]] – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]]
2. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]]
3. [[QLTS]] – [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]], [[Ho so thi sinh|Hồ sơ thí sinh]], [[DS trung tuyen|Danh sách trúng tuyển]]
4. **QLSV** – [[Lop sinh vien|Lớp sinh viên]], [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]], [[DS SV hoc ky|Danh sách sinh viên học kỳ]], [[Danh muc sinh vien|Danh mục sinh viên (mọi SV của trường)]], [[Diem ren luyen|Điểm rèn luyện]], [[Dien chinh sach|Diện chính sách / miễn giảm]]

**Ràng buộc quay ngược** (dữ liệu sinh ra *sau* QLSV nhưng quay lại chặn / ảnh hưởng nó, thường từ kỳ trước): [[Diem trung binh|Điểm trung bình – tích lũy]] (DIEM), [[KQ DKMH|Kết quả đăng ký môn học]] (DKMH), [[Ket qua hoc vu|Kết quả xét học vụ]] (QXHV), [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]] (QLTN)

**Sửa dữ liệu của QLSV → kiểm lại:** phân hệ dùng trực tiếp [[CSHP]], [[DKMH]], [[KHGD]], [[KSDG]], [[NETWEB-API]], [[QKTX]], [[QLTN]], [[QLTS]], [[QXHV]]; dữ liệu sinh ra từ đó (theo thứ tự): [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]] (DKMH), [[Diem luan van|Điểm luận văn]] (BVLV), [[Hop dong KTX|Hợp đồng ký túc xá]] (QKTX), [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]] (KHGD), [[Ket qua khao sat|Kết quả khảo sát]] (KSDG), [[Thoi khoa bieu|Thời khóa biểu]] (KHGD), [[KQ DKMH|Kết quả đăng ký môn học]] (DKMH), [[Khoi luong giang day|Khối lượng giảng dạy]] (KLGD), [[Danh sach thi|Danh sách thi – lịch thi]] (LTHI), [[Diem danh|Điểm danh (chuyên cần)]] (NETWEB-UI), [[Hoc phi|Học phí phải thu (đã tính)]] (CSHP), [[Diem mon hoc|Điểm môn học]] (DIEM), [[Phieu thu|Phiếu thu học phí]] (QLTV), [[Diem trung binh|Điểm trung bình – tích lũy]] (DIEM), [[No hoc phi|Nợ học phí]] (CSHP), [[Ket qua hoc vu|Kết quả xét học vụ]] (QXHV), [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]] (QLTN).

## Nằm trong quy trình
- [[02 Tuyen sinh - nhap hoc|Tuyển sinh → nhập học → có sinh viên]]
- [[03 CTDT - TKB|Chương trình đào tạo → nhóm học → thời khoá biểu]]
- [[04 Dang ky mon hoc|Đăng ký môn học]]
- [[05 Hoc phi - thu - thanh toan|Học phí: tính → nợ → thu → thanh toán online]]
- [[07 Diem - hoc vu - hoc bong|Điểm → điểm TB → học vụ, học bổng]]
- [[08 Tot nghiep - luan van|Luận văn → xét tốt nghiệp → quyết định tốt nghiệp]]
- [[09 Hoat dong tren lop|Hoạt động trên lớp: điểm danh, nghỉ dạy – dạy bù, khảo sát]]
- [[11 Ky tuc xa|Ký túc xá]]

## Tài liệu
- [[HDSD QLSV]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
DS SV học kỳ là đầu vào của hầu hết phân hệ đào tạo. Mẫu kịch bản ghi dữ liệu: QLSV-001.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

---
loai: phan-he
ma: KSDG
ten: Khảo sát đánh giá
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
  - mau-in
tab_edusoft: Khảo sát đánh giá
nhan_tu:
  - "[[KHGD]]"
  - "[[QLHT]]"
  - "[[QLNS]]"
  - "[[QLSV]]"
dua_sang:
  - "[[DIEM]]"
dau_hieu: form đánh giá, câu hỏi, thang đo, kỳ đánh giá, đáp viên, khảo sát trước khi xem điểm, mẫu in KS
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Khảo sát đánh giá"
  - "Khảo sát"
quy_trinh:
  - "[[07 Diem - hoc vu - hoc bong]]"
  - "[[09 Hoat dong tren lop]]"
  - "[[10 Nhan su - khoi luong giang day]]"
tags: [phan-he]
---
# KSDG – Khảo sát đánh giá

## Là gì
Chuẩn bị form (form, thang đo, nhóm câu hỏi, câu hỏi) → kỳ đánh giá → DS được đánh giá → DS đáp viên → **đáp viên trả lời trên web** → in kết quả (lưu đồ KSDG).

## Nhận dữ liệu từ
- [[Hoc ky|Năm học – học kỳ]] từ [[QLHT]] – kỳ đánh giá
- [[DS SV hoc ky|Danh sách sinh viên học kỳ]] từ [[QLSV]] – đáp viên
- [[Vien chuc|Viên chức / cán bộ giảng dạy]] từ [[QLNS]] – giảng viên được đánh giá
- [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]] từ [[KHGD]] – dữ liệu đánh giá (nhóm tổ, GV)

## Tạo ra
- [[Ket qua khao sat|Kết quả khảo sát]]

## Đưa sang
- [[Ket qua khao sat|Kết quả khảo sát]] → [[DIEM]]

## Sửa ở đây → kiểm lại
Các phân hệ nhận dữ liệu của KSDG: [[DIEM]].
Lỗi có thể do dữ liệu đầu vào từ: [[KHGD]], [[QLHT]], [[QLNS]], [[QLSV]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
`Khảo sát đánh giá/ Chuẩn bị form/ …`, `Khảo sát đánh giá/ Danh sách đánh giá/ …`, `Khảo sát đánh giá/ Khai thác báo biểu/ In kết quả`.
Menu: [[Menu/KSDG|42 menu của KSDG]] – menu tạo dữ liệu: [[Menu/Tạo và cập nhật danh sách đáp viên (Z3.01.02)|Tạo và cập nhật danh sách đáp viên]], [[Menu/Nhập trả lời từng đáp viên (Z4.01.01)|Nhập trả lời từng đáp viên]].

## Phần trên web / app
NetWEB SV + GV + khách: làm khảo sát; GV: xem kết quả khảo sát; DHNT: **đánh giá GV trước khi xem điểm**.


## Dạng case thường gặp
[[Hien thi web]], [[Mau in bao cao]], [[Thiet lap khong hieu luc]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: edusoft / web / mau-in – xem KH nói về màn hình Edusoft hay trang web.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được KSDG phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[KHGD]] – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]], [[Mon hoc|Môn học]], [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]], [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]]
2. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]]
3. [[QLNS]] – [[Vien chuc|Viên chức / cán bộ giảng dạy]]
4. [[QLTS]] – [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]], [[Ho so thi sinh|Hồ sơ thí sinh]], [[DS trung tuyen|Danh sách trúng tuyển]]
5. [[QLSV]] – [[Lop sinh vien|Lớp sinh viên]], [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]], [[DS SV hoc ky|Danh sách sinh viên học kỳ]]
6. **KSDG** – [[Ket qua khao sat|Kết quả khảo sát]]

**Sửa dữ liệu của KSDG → kiểm lại:** phân hệ dùng trực tiếp [[DIEM]].

## Nằm trong quy trình
- [[07 Diem - hoc vu - hoc bong|Điểm → điểm TB → học vụ, học bổng]]
- [[09 Hoat dong tren lop|Hoạt động trên lớp: điểm danh, nghỉ dạy – dạy bù, khảo sát]]
- [[10 Nhan su - khoi luong giang day|Nhân sự → phân công giảng dạy → khối lượng giảng dạy]]

## Tài liệu
- [[HDSD KSDG]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
Phần form / mẫu in kết quả trên Edusoft, phần trả lời trên web; DHNT bắt khảo sát trước khi xem điểm (liên quan [[DIEM]] trên web).

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

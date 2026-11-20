---
loai: phan-he
ma: LTHI
ten: Tổ chức thi
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
tab_edusoft: Tổ chức thi
nhan_tu:
  - "[[DKMH]]"
  - "[[KHGD]]"
  - "[[QLHT]]"
  - "[[QLNS]]"
dua_sang:
  - "[[DIEM]]"
dau_hieu: hoãn thi, nhóm thi, đợt thi, tổ thi, lịch thi, số báo danh, coi thi, trùng lịch
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Tổ chức thi"
  - "Lịch thi"
  - "Tổ chức thi"
quy_trinh:
  - "[[06 To chuc thi]]"
  - "[[10 Nhan su - khoi luong giang day]]"
tags: [phan-he]
---
# LTHI – Tổ chức thi

## Là gì
Hoãn thi / thi cải thiện, tính chất thi, nhóm thi, đợt thi, tổ thi, xếp & hiệu chỉnh lịch thi, số báo danh, phân công coi thi, báo biểu kiểm tra trùng (lưu đồ LTHI).

## Nhận dữ liệu từ
- [[Hoc ky|Năm học – học kỳ]] từ [[QLHT]] – đợt thi
- [[Vien chuc|Viên chức / cán bộ giảng dạy]] từ [[QLNS]] – phân công coi thi
- [[Phong hoc|Phòng học kỳ]] từ [[KHGD]] – nhập phòng sử dụng trong đợt thi
- [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]] từ [[KHGD]] – tạo nhóm thi
- [[Thoi khoa bieu|Thời khóa biểu]] từ [[KHGD]] – kiểm trùng TKB học với lịch thi
- [[KQ DKMH|Kết quả đăng ký môn học]] từ [[DKMH]] – nguồn danh sách thi

## Tạo ra
- [[Danh sach thi|Danh sách thi – lịch thi]]

## Đưa sang
- [[Danh sach thi|Danh sách thi – lịch thi]] → [[DIEM]]

## Sửa ở đây → kiểm lại
Các phân hệ nhận dữ liệu của LTHI: [[DIEM]].
Lỗi có thể do dữ liệu đầu vào từ: [[DKMH]], [[KHGD]], [[QLHT]], [[QLNS]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
`Tổ chức thi/ …`.
Menu: [[Menu/LTHI|125 menu của LTHI]] – menu tạo dữ liệu: [[Menu/Xếp lịch thi theo đợt thi (L39.03)|Xếp lịch thi theo đợt thi]].

## Phần trên web / app
NetWEB SV + GV: xem lịch thi; GV: xem lịch coi thi; CBCNV đăng ký coi thi (tuỳ trường).


## Dạng case thường gặp
[[Mau in bao cao]], [[So lieu tinh sai]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: edusoft / web – xem KH nói về màn hình Edusoft hay trang web.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được LTHI phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[KHGD]] – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]], [[Mon hoc|Môn học]], [[Phong hoc|Phòng học kỳ]], [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]], [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]], [[Thoi khoa bieu|Thời khóa biểu]]
2. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]]
3. [[QLNS]] – [[Vien chuc|Viên chức / cán bộ giảng dạy]]
4. [[QLTS]] – [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]], [[Ho so thi sinh|Hồ sơ thí sinh]], [[DS trung tuyen|Danh sách trúng tuyển]]
5. [[QLSV]] – [[Lop sinh vien|Lớp sinh viên]], [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]], [[DS SV hoc ky|Danh sách sinh viên học kỳ]]
6. [[DKMH]] – [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]], [[KQ DKMH|Kết quả đăng ký môn học]]
7. **LTHI** – [[Danh sach thi|Danh sách thi – lịch thi]]

**Sửa dữ liệu của LTHI → kiểm lại:** phân hệ dùng trực tiếp [[DIEM]]; dữ liệu sinh ra từ đó (theo thứ tự): [[Diem mon hoc|Điểm môn học]] (DIEM), [[Diem trung binh|Điểm trung bình – tích lũy]] (DIEM), [[Ket qua hoc vu|Kết quả xét học vụ]] (QXHV), [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]] (QLTN).

## Nằm trong quy trình
- [[06 To chuc thi|Tổ chức thi]]
- [[10 Nhan su - khoi luong giang day|Nhân sự → phân công giảng dạy → khối lượng giảng dạy]]

## Tài liệu
- [[HDSD LTHI]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
—

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

---
loai: phan-he
ma: DIEM
ten: Quản lý điểm
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
  - mau-in
tab_edusoft: Quản lý điểm, Quản lý nhập điểm
nhan_tu:
  - "[[BVLV]]"
  - "[[DKMH]]"
  - "[[KHGD]]"
  - "[[KSDG]]"
  - "[[LTHI]]"
  - "[[QLHT]]"
dua_sang:
  - "[[QLSV]]"
  - "[[QLTN]]"
  - "[[QXHV]]"
dau_hieu: bảng ghi điểm, nhập điểm, phách, phúc khảo, điểm TB, phiếu điểm, xét học vụ, chứng chỉ
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Quản lý điểm"
  - "Quản lý điểm"
quy_trinh:
  - "[[07 Diem - hoc vu - hoc bong]]"
  - "[[08 Tot nghiep - luan van]]"
tags: [phan-he]
---
# DIEM – Quản lý điểm

## Là gì
KQ ĐKMH → bảng ghi điểm → nhập điểm (danh sách / import / phách / bảo lưu / phúc khảo) → tính điểm TB → phiếu điểm; xét học vụ, xét chứng chỉ (lưu đồ DIEM, QXHV).

## Nhận dữ liệu từ
- [[Hoc ky|Năm học – học kỳ]] từ [[QLHT]] – điểm, xét học vụ học kỳ
- [[Mon hoc|Môn học]] từ [[KHGD]] – môn thay thế
- [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]] từ [[KHGD]] – môn thay thế theo khối
- [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]] từ [[KHGD]] – bảng ghi điểm / nhập điểm theo nhóm học
- [[KQ DKMH|Kết quả đăng ký môn học]] từ [[DKMH]] – bảng ghi điểm, nhập điểm
- [[Danh sach thi|Danh sách thi – lịch thi]] từ [[LTHI]] – tạo phách, bảng ghi điểm theo tổ thi
- [[Diem luan van|Điểm luận văn]] từ [[BVLV]] – thành điểm môn học
- [[Ket qua khao sat|Kết quả khảo sát]] từ [[KSDG]] – DHNT: phải khảo sát xong mới xem điểm (web)

## Tạo ra
- [[Diem mon hoc|Điểm môn học]]
- [[Diem trung binh|Điểm trung bình – tích lũy]]

## Đưa sang
- [[Diem trung binh|Điểm trung bình – tích lũy]] → [[QXHV]], [[QLTN]], [[QLSV]]

## Sửa ở đây → kiểm lại
Các phân hệ nhận dữ liệu của DIEM: [[QLSV]], [[QLTN]], [[QXHV]].
Lỗi có thể do dữ liệu đầu vào từ: [[BVLV]], [[DKMH]], [[KHGD]], [[KSDG]], [[LTHI]], [[QLHT]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
`Quản lý điểm/ …`, `Quản lý nhập điểm/ …`.
Menu: [[Menu/DIEM|394 menu của DIEM]] – menu tạo dữ liệu: [[Menu/Cộng điểm TB - theo lớp (D52.06)|Cộng điểm TB - theo lớp]], [[Menu/Cộng điểm TB - từng sinh viên (D52.03)|Cộng điểm TB - từng sinh viên]], [[Menu/Xét theo lớp (HK) (D73.03)|Xét theo lớp (HK)]], [[Menu/Xét theo đợt (HK) (D73.01)|Xét theo đợt (HK)]], [[Menu/Nhập điểm theo lớp (D21.01)|Nhập điểm theo lớp]], [[Menu/Nhập điểm theo nhóm học (D21.03)|Nhập điểm theo nhóm học]].

## Phần trên web / app
NetWEB SV: xem điểm; NetWEB GV: nhập điểm theo nhóm học / tổ thi / phách, xem điểm môn giảng dạy. Phúc tra điểm trực tuyến: [[GAM]].


## Dạng case thường gặp
[[Hien thi web]], [[Hieu nang]], [[Loi EX Edusoft]], [[Luu cap nhat khong duoc]], [[Mau in bao cao]], [[So lieu tinh sai]], [[Thiet lap khong hieu luc]], [[Xu ly du lieu]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: edusoft / web / mau-in – xem KH nói về màn hình Edusoft hay trang web.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được DIEM phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[KHGD]] – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]], [[Mon hoc|Môn học]], [[Phong hoc|Phòng học kỳ]], [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]], [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]], [[Thoi khoa bieu|Thời khóa biểu]]
2. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]]
3. [[QLNS]] – [[Vien chuc|Viên chức / cán bộ giảng dạy]]
4. [[QLTS]] – [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]], [[Ho so thi sinh|Hồ sơ thí sinh]], [[DS trung tuyen|Danh sách trúng tuyển]]
5. [[QLSV]] – [[Lop sinh vien|Lớp sinh viên]], [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]], [[DS SV hoc ky|Danh sách sinh viên học kỳ]]
6. [[DKMH]] – [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]], [[KQ DKMH|Kết quả đăng ký môn học]]
7. [[BVLV]] – [[Diem luan van|Điểm luận văn]]
8. [[KSDG]] – [[Ket qua khao sat|Kết quả khảo sát]]
9. [[LTHI]] – [[Danh sach thi|Danh sách thi – lịch thi]]
10. [[NETWEB-UI]] – [[Diem danh|Điểm danh (chuyên cần)]]
11. **DIEM** – [[Diem mon hoc|Điểm môn học]], [[Diem trung binh|Điểm trung bình – tích lũy]]

**Sửa dữ liệu của DIEM → kiểm lại:** phân hệ dùng trực tiếp [[QLSV]], [[QLTN]], [[QXHV]]; dữ liệu sinh ra từ đó (theo thứ tự): [[Ket qua hoc vu|Kết quả xét học vụ]] (QXHV), [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]] (QLTN).

## Nằm trong quy trình
- [[07 Diem - hoc vu - hoc bong|Điểm → điểm TB → học vụ, học bổng]]
- [[08 Tot nghiep - luan van|Luận văn → xét tốt nghiệp → quyết định tốt nghiệp]]

## Tài liệu
- [[HDSD DIEM]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
Điểm TB là đầu vào của xét học vụ, tốt nghiệp, học bổng – sửa cách tính điểm phải kiểm lại các phân hệ đó.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

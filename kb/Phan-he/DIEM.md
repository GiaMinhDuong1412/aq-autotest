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

## Test ở đâu
Tuỳ yêu cầu: edusoft / web / mau-in – xem KH nói về màn hình Edusoft hay trang web.

## Lưu ý
Điểm TB là đầu vào của xét học vụ, tốt nghiệp, học bổng – sửa cách tính điểm phải kiểm lại các phân hệ đó.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

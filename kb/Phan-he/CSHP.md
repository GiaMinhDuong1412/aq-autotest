---
loai: phan-he
ma: CSHP
ten: Chính sách học phí
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
tab_edusoft: Chính sách HP
nhan_tu:
  - "[[DKMH]]"
  - "[[KHGD]]"
  - "[[QLHT]]"
  - "[[QLSV]]"
  - "[[QLTV]]"
dua_sang:
  - "[[DKMH]]"
  - "[[EDUBILL]]"
  - "[[QLHT]]"
  - "[[QLTV]]"
dau_hieu: miễn giảm, đơn giá, tính học phí, công nợ, tồn nợ, phụ thu, khoản thu khác, học phí tạm tính
nguon: tai-lieu
trang_thai: tu-tai-lieu
---
# CSHP – Chính sách học phí

## Là gì
Loại hình thu + công thức thu → nhóm công thức; đơn giá / số TCHP / đơn giá đặc biệt; hình thức thu theo đối tượng; **miễn giảm chính sách**; phụ thu; KQ ĐKMH → **tính học phí** → nợ học phí → thu ([[QLTV]]) (lưu đồ CSHP).

## Nhận dữ liệu từ
- [[Hoc ky|Năm học – học kỳ]] từ [[QLHT]] – tính học phí học kỳ
- [[Mon hoc|Môn học]] từ [[KHGD]] – mức đơn giá và số TCHP môn học
- [[DS SV hoc ky|Danh sách sinh viên học kỳ]] từ [[QLSV]] – SV tính học phí
- [[Dien chinh sach|Diện chính sách / miễn giảm]] từ [[QLSV]] – miễn giảm khi tính học phí
- [[KQ DKMH|Kết quả đăng ký môn học]] từ [[DKMH]] – tính học phí
- [[Phieu thu|Phiếu thu học phí]] từ [[QLTV]] – giảm nợ học phí

## Tạo ra
- [[Hoc phi|Học phí phải thu (đã tính)]]
- [[No hoc phi|Nợ học phí]]

## Đưa sang
- [[Hoc phi|Học phí phải thu (đã tính)]] → [[QLTV]], [[EDUBILL]]
- [[No hoc phi|Nợ học phí]] → [[DKMH]], [[QLHT]], [[QLTV]]

## Sửa ở đây → kiểm lại
Các phân hệ nhận dữ liệu của CSHP: [[DKMH]], [[EDUBILL]], [[QLHT]], [[QLTV]].
Lỗi có thể do dữ liệu đầu vào từ: [[DKMH]], [[KHGD]], [[QLHT]], [[QLSV]], [[QLTV]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
`Chính sách HP/ Chính sách học phí/ …`, `Chính sách HP/ Tính và In học phí/ …`, `Chính sách HP/ Chính sách các khoản thu khác/ …`.
Menu: [[Menu/CSHP|93 menu của CSHP]] – menu tạo dữ liệu: [[Menu/Cập nhật tồn nợ (D27.01)|Cập nhật tồn nợ]], [[Menu/Danh sách SV tồn nợ HP (D27.03)|Danh sách SV tồn nợ HP]], [[Menu/Tính theo lớp (P21.03)|Tính theo lớp]], [[Menu/Tính theo từng sinh viên (P21.01)|Tính theo từng sinh viên]].

## Phần trên web / app
NetWEB SV: **xem học phí** (summary + bảng chi tiết, miễn giảm), học phí tạm tính khi ĐKMH; đóng học phí trực tuyến ([[EDUBILL]]).


## Dạng case thường gặp
[[Hien thi web]], [[So lieu tinh sai]], [[Thiet lap khong hieu luc]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: edusoft / web – xem KH nói về màn hình Edusoft hay trang web.

## Lưu ý
Mã CSHP trên ACS gồm cả phần Edusoft lẫn phần SV xem trên web – **đọc lời KH**: nói "trang / summary / bảng hiển thị" → web; nói menu Chính sách HP / tính / đơn giá → Edusoft.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

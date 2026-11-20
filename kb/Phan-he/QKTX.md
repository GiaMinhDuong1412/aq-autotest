---
loai: phan-he
ma: QKTX
ten: Ký túc xá
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
tab_edusoft: Ký túc xá
nhan_tu:
  - "[[QLSV]]"
dua_sang: []
dau_hieu: phòng lưu trú, đơn giá, hợp đồng, thanh lý, thu phí lưu trú, điện nước
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Ký túc xá"
  - "Ký túc xá"
  - "KTX"
quy_trinh:
  - "[[05 Hoc phi - thu - thanh toan]]"
  - "[[11 Ky tuc xa]]"
tags: [phan-he]
---
# QKTX – Ký túc xá

## Là gì
Danh mục phòng, đơn giá phòng / dịch vụ, hợp đồng theo phòng, thanh lý, thu tiền lưu trú, chỉ số điện nước.

## Nhận dữ liệu từ
- [[DS SV hoc ky|Danh sách sinh viên học kỳ]] từ [[QLSV]] – SV ở ký túc xá

## Tạo ra
- [[Hop dong KTX|Hợp đồng ký túc xá]]

## Đưa sang
—

## Sửa ở đây → kiểm lại
Không có phân hệ nào nhận dữ liệu trực tiếp.
Lỗi có thể do dữ liệu đầu vào từ: [[QLSV]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
`Ký túc xá/ Định nghĩa dữ liệu/ …`, `Ký túc xá/ Quản lý hợp đồng/ …`, `Ký túc xá/ Quản lý thanh toán/ …` (tài liệu còn menu cũ "Lưu trú / Quyết định vào|ra KTX").
Menu: [[Menu/QKTX|103 menu của QKTX]] – menu tạo dữ liệu: [[Menu/Hợp đồng theo phòng (X20.10.12)|Hợp đồng theo phòng]].

## Phần trên web / app
NetWEB SV: đăng ký ký túc xá (đăng ký trực tuyến / gia hạn).


## Dạng case thường gặp
(chưa ghi – thêm khi gặp)
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: edusoft / web – xem KH nói về màn hình Edusoft hay trang web.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được QKTX phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[KHGD]] – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]]
2. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]]
3. [[QLTS]] – [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]], [[Ho so thi sinh|Hồ sơ thí sinh]], [[DS trung tuyen|Danh sách trúng tuyển]]
4. [[QLSV]] – [[Lop sinh vien|Lớp sinh viên]], [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]], [[DS SV hoc ky|Danh sách sinh viên học kỳ]], [[Danh muc sinh vien|Danh mục sinh viên (mọi SV của trường)]]
5. **QKTX** – [[Hop dong KTX|Hợp đồng ký túc xá]]

**Sửa dữ liệu của QKTX → kiểm lại:** phân hệ dùng trực tiếp —.

## Nằm trong quy trình
- [[05 Hoc phi - thu - thanh toan|Học phí: tính → nợ → thu → thanh toán online]]
- [[11 Ky tuc xa|Ký túc xá]]

## Tài liệu
- [[HDSD QKTX]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
Thu phí là dữ liệu tiền – chỉ dùng SV test.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

---
loai: phan-he
ma: NETWEB-API
ten: API của Netweb
san_pham: "[[Netweb]]"
test_tren:
  - web
  - api
tab_edusoft: —
nhan_tu:
  - "[[QLHT]]"
  - "[[QLSV]]"
dua_sang: []
dau_hieu: request, API, đăng nhập, bảo mật 2 lớp, token, rút môn online, gọi từ CVHT, edusoft-api
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "API của Netweb"
quy_trinh:
  - "[[12 Tai khoan - phan quyen - web]]"
tags: [phan-he]
---
# NETWEB-API – API của Netweb

## Là gì
Phần xử lý phía máy chủ của Netweb (vd `https://edusoft-api.<trường>/…`): đăng nhập, phân quyền, nghiệp vụ web (rút môn, CVHT duyệt…).

## Nhận dữ liệu từ
- [[Tai khoan va phan quyen|Tài khoản & phân quyền]] từ [[QLHT]] – đăng nhập web
- [[Danh muc sinh vien|Danh mục sinh viên (mọi SV của trường)]] từ [[QLSV]] – tài khoản SV đăng nhập web

## Tạo ra
—

## Đưa sang
—

## Sửa ở đây → kiểm lại
Không có phân hệ nào nhận dữ liệu trực tiếp.
Lỗi có thể do dữ liệu đầu vào từ: [[QLHT]], [[QLSV]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
Dữ liệu gốc nằm ở Edusoft – kiểm lại kết quả ghi xuống (vd KQ ĐKMH sau khi rút môn).

## Phần trên web / app
Test **qua trang web** (thao tác đúng chức năng) + kiểm dữ liệu ghi xuống Edusoft.


## Dạng case thường gặp
[[Tai khoan phan quyen]], [[Tich hop thanh toan]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: web / api – xem KH nói về màn hình Edusoft hay trang web.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được NETWEB-API phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[KHGD]] – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]]
2. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]], [[Tai khoan va phan quyen|Tài khoản & phân quyền]]
3. [[QLTS]] – [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]], [[Ho so thi sinh|Hồ sơ thí sinh]], [[DS trung tuyen|Danh sách trúng tuyển]]
4. [[QLSV]] – [[Lop sinh vien|Lớp sinh viên]], [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]], [[Danh muc sinh vien|Danh mục sinh viên (mọi SV của trường)]]
5. **NETWEB-API** – dùng dữ liệu trên

## Nằm trong quy trình
- [[12 Tai khoan - phan quyen - web|Tài khoản, phân quyền, cấu hình web (dùng chung)]]

## Tài liệu
- [[HDSD NETWEB]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
Đăng nhập / bảo mật: thử cả trường hợp sai (sai mật khẩu, hết phiên, không đủ quyền).

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

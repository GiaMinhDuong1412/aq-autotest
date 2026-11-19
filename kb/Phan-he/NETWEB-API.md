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

## Test ở đâu
Tuỳ yêu cầu: web / api – xem KH nói về màn hình Edusoft hay trang web.

## Lưu ý
Đăng nhập / bảo mật: thử cả trường hợp sai (sai mật khẩu, hết phiên, không đủ quyền).

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

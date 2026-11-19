---
loai: trang-chu
---
# Knowledge base nghiệp vụ (AQ Auto Test)

Kho kiến thức để **Claude và app AQ Auto Test hiểu đúng nghiệp vụ**: các phân hệ Edusoft / web **liên kết với nhau qua dữ liệu** –
phân hệ này tạo dữ liệu, phân hệ khác dùng. Sửa / lỗi ở đâu thì biết phải kiểm lại những phân hệ nào, test trên Edusoft hay web.

**Bắt đầu từ [[00 Bản đồ phân hệ]]** – chuỗi dữ liệu chính và sơ đồ toàn bộ liên kết.

## Các ngăn
| Thư mục | Ghi gì |
|---|---|
| `Phan-he/` | Mỗi phân hệ (mã như trên ACS): là gì, **nhận dữ liệu từ**, **tạo ra**, **đưa sang**, sửa ở đây → kiểm lại đâu, phần Edusoft / phần web |
| `Du-lieu/` | Mỗi loại dữ liệu chảy giữa phân hệ (DS SV học kỳ, KQ ĐKMH, nhóm học, điểm TB…): tạo ở đâu (menu), dùng ở đâu, hiện trên web ra sao |
| `San-pham/` | Edusoft, Netweb, App: là gì, test ở đâu |
| `Truong/` | Từng trường: tên, link Netweb thật, chức năng web trường có, môi trường test |
| `Repo-coder/` | Quy ước repo / nhánh coder → sửa ở web hay Edusoft |
| `Cach-test/` | Cách test theo loại sửa (lỗi EX, số liệu, mẫu in, web theo trường, API / bảo mật, hiển thị web) |

## Quy tắc
- Mỗi ghi chú có **Properties** (đầu file) – app đọc các trường này, **giữ đúng tên trường**:
  `nhan_tu` / `dua_sang` (phân hệ), `tao_o` / `dung_o` (dữ liệu), `test_tren`: `web` | `edusoft` | `app` | `api` | `mau-in`.
- `trang_thai`: `can-xac-nhan` (đoán / thiếu) → `tu-tai-lieu` (Claude điền từ tài liệu) → `da-xac-nhan` (người test đã kiểm). Claude chỉ coi `da-xac-nhan` là chắc chắn.
- Thêm liên kết mới: ghi vào `Du-lieu/` (tạo ở `[[…]]`, dùng ở `[[…]]`) và mục "Nhận dữ liệu từ / Đưa sang" của hai phân hệ.
- **Không** ghi mật khẩu, token, chuỗi kết nối vào kho này (kho nằm trong git).

## Nguồn đã dùng (Claude, 19/11/2026)
Tài liệu HDSD SharePoint "1. Tài liệu Edusoft", lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), nghiệp vụ QLSV, sheet Release(TestMenu)
(Menu_NEW, ChuyenDoiNetWeb, Port NetWEB, DHNT Điều hướng DVPC, NetWeb_DKMH).

## Việc người test cần làm
- [ ] Mở [[00 Bản đồ phân hệ]] và Graph view – thấy liên kết nào sai / thiếu thì sửa ghi chú `Du-lieu/` tương ứng
- [ ] Liếc `Phan-he/` (nhất là NETWEB-UI, NETWEB-API, DKMHUI, CSHP, QXHV, BVLV) – đúng thì đổi `trang_thai: da-xac-nhan`
- [ ] Điền **web test / Edusoft test** trong `Truong/` cho các trường hay test

---
loai: trang-chu
---
# Knowledge base nghiệp vụ (AQ Auto Test)

Kho kiến thức để **Claude và app AQ Auto Test hiểu đúng nghiệp vụ**: các phân hệ Edusoft / web **liên kết với nhau qua dữ liệu** –
phân hệ này tạo dữ liệu, phân hệ khác dùng. Sửa / lỗi ở đâu thì biết phải kiểm lại những phân hệ nào, test trên Edusoft hay web.

**Bắt đầu từ [[00 Logic nghiệp vụ]]** – *muốn có X thì phải có Y*: muốn có sinh viên phải tuyển sinh; có sinh viên + giảng viên + CTĐT mới có
kế hoạch giảng dạy → TKB → đăng ký môn học → học phí, lịch thi, điểm → học vụ, tốt nghiệp. Sau đó xem [[00 Bản đồ phân hệ]] (phân hệ nào đưa dữ liệu sang phân hệ nào).

Cách đọc một case ACS bằng KB: case nói tới **menu / dữ liệu** nào → mở ghi chú dữ liệu đó → *Chuẩn bị dữ liệu test* = các dữ liệu phải có trước;
*Kiểm tra không ảnh hưởng* = dữ liệu sinh ra từ nó + phân hệ dùng nó; case khác chạm cùng dữ liệu (hoặc dữ liệu cha – con) là **case liên quan**.
App AQ Auto Test (trang Test sau sửa lỗi) làm đúng việc này tự động – khung **Sơ đồ liên kết** ở bước 1, plan test ở bước 2.

## Các ngăn
| Thư mục | Ghi gì |
|---|---|
| `Phan-he/` | Mỗi phân hệ (mã như trên ACS): là gì, **nhận dữ liệu từ**, **tạo ra**, **đưa sang**, sửa ở đây → kiểm lại đâu, phần Edusoft / phần web |
| `Du-lieu/` | Mỗi loại dữ liệu (DS SV học kỳ, KQ ĐKMH, nhóm học, điểm TB…): **phải có trước** gì (`can_co`), **là điều kiện cho** gì, tầng, tạo ở đâu (menu), dùng ở đâu, trên web, chuẩn bị dữ liệu test theo thứ tự |
| `Menu/` | `Menu/<phân hệ>.md` = toàn bộ menu Edusoft của phân hệ, mỗi menu nối tới dữ liệu nó đụng tới; menu **tạo** dữ liệu có ghi chú riêng (trước khi dùng phải có gì, lưu xong ảnh hưởng tới đâu) |
| `San-pham/` | Edusoft, Netweb, App: là gì, test ở đâu |
| `Truong/` | Từng trường: tên, link Netweb thật, chức năng web trường có, môi trường test |
| `Repo-coder/` | Quy ước repo / nhánh coder → sửa ở web hay Edusoft |
| `Cach-test/` | Cách test theo loại sửa (lỗi EX, số liệu, mẫu in, web theo trường, API / bảo mật, hiển thị web) |

## Quy tắc
- Mỗi ghi chú có **Properties** (đầu file) – app đọc các trường này, **giữ đúng tên trường**:
  `nhan_tu` / `dua_sang` (phân hệ), `tao_o` / `dung_o` / `can_co` / `la_dieu_kien_cho` (dữ liệu), `test_tren`: `web` | `edusoft` | `app` | `api` | `mau-in`.
- `trang_thai`: `can-xac-nhan` (đoán / thiếu) → `tu-tai-lieu` (Claude điền từ tài liệu) → `da-xac-nhan` (người test đã kiểm). Claude chỉ coi `da-xac-nhan` là chắc chắn.
- **Ghi chú là nguồn**: sửa thẳng trong Obsidian (Properties `can_co`, `tao_o`, `dung_o`, `tu_khoa`… và các dòng `- [[…]] – vì sao`). App đọc lại khi bạn quay về cửa sổ app
  (đã chọn vault ở Test sau sửa lỗi → Thiết lập ACS → Kết nối Claude Desktop → Chọn vault…). Claude Desktop cũng sửa được qua MCP khi bạn dạy kiến thức mới.
  Chạy `dong-bo.bat` để chia sẻ cho máy khác. (`tools/kb_lien_ket.py` chỉ dùng để dựng lần đầu – chạy lại sẽ ghi đè.)
- **Không** ghi mật khẩu, token, chuỗi kết nối vào kho này (kho nằm trong git).

## Nguồn đã dùng (Claude, 19/11/2026)
Tài liệu HDSD SharePoint "1. Tài liệu Edusoft", lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), nghiệp vụ QLSV, sheet Release(TestMenu)
(Menu_NEW, ChuyenDoiNetWeb, Port NetWEB, DHNT Điều hướng DVPC, NetWeb_DKMH).

## Việc người test cần làm
- [ ] Đọc [[00 Logic nghiệp vụ]] – khẳng định nào sai ("muốn có X phải có Y") thì sửa `can_co` trong ghi chú `Du-lieu/` tương ứng
- [ ] Mở [[00 Bản đồ phân hệ]] và Graph view – liên kết nào sai / thiếu thì ghi lại
- [ ] Liếc `Phan-he/` (nhất là NETWEB-UI, NETWEB-API, DKMHUI, CSHP, QXHV, BVLV) – đúng thì đổi `trang_thai: da-xac-nhan`
- [ ] Điền **web test / Edusoft test** trong `Truong/` cho các trường hay test

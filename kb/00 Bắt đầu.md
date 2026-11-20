---
loai: trang-chu
---
# Knowledge base nghiệp vụ (AQ Auto Test)

Kho kiến thức để **Claude và app AQ Auto Test hiểu đúng nghiệp vụ**: các phân hệ Edusoft / web **liên kết với nhau qua dữ liệu** –
phân hệ này tạo dữ liệu, phân hệ khác dùng. Sửa / lỗi ở đâu thì biết phải kiểm lại những phân hệ nào, test trên Edusoft hay web.

**Đọc case: [[00 Cách phân tích case]]** – trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case (`Dang-case/`) → dữ liệu → case liên quan. Phải đúng trước, test sau.

**Nghiệp vụ: [[00 Logic nghiệp vụ]]** – *muốn có X thì phải có Y*: muốn có sinh viên phải tuyển sinh; có sinh viên + giảng viên + CTĐT mới có
kế hoạch giảng dạy → TKB → đăng ký môn học → học phí, lịch thi, điểm → học vụ, tốt nghiệp. Sau đó xem [[00 Bản đồ phân hệ]] (phân hệ nào đưa dữ liệu sang phân hệ nào).

Cách đọc một case ACS bằng KB: case nói tới **menu / dữ liệu** nào → mở ghi chú dữ liệu đó → *Chuẩn bị dữ liệu test* = các dữ liệu phải có trước;
*Kiểm tra không ảnh hưởng* = dữ liệu sinh ra từ nó + phân hệ dùng nó; case khác chạm cùng dữ liệu (hoặc dữ liệu cha – con) là **case liên quan**.
App AQ Auto Test (trang Test case ACS) làm đúng việc này tự động: Claude đọc KB để phân tích case và soạn plan test ở bước 2 (bản đồ KB không hiện cho người dùng).

## Bắt đầu từ đâu
| Muốn | Mở |
|---|---|
| Đọc một case ACS | [[00 Cách phân tích case]] |
| Biết một năm học đi qua phân hệ nào, bước nào cần gì | [[00 Quy trình xuyên phân hệ]] · Canvas [[00 Vòng đời đào tạo.canvas\|vòng đời đào tạo]] |
| Phân hệ nào đưa dữ liệu cho phân hệ nào | [[00 Bản đồ phân hệ]] · Canvas [[00 Bản đồ phân hệ.canvas\|bản đồ phân hệ]] |
| Muốn có dữ liệu X phải có gì trước | [[00 Logic nghiệp vụ]] |
| Trường này hay có case gì, làm khác bản chung ra sao | [[00 Mô hình trường]] (`Case-truong/`) |
| Tài liệu gốc ở đâu (HDSD, lưu đồ, source, ACS) | [[00 Tài liệu nguồn]] |

## Dùng Obsidian cho hiệu quả
- **Bases** (bảng lọc / sắp xếp theo Properties, có sẵn trong Obsidian ≥ 1.9): `_bases/` – Phân hệ, Dữ liệu, Trường, Tài liệu, Quy trình, Case theo trường; đã nhúng vào các trang 00.
- **Canvas**: [[00 Vòng đời đào tạo.canvas]] (quy trình theo thời gian một năm học), [[00 Bản đồ phân hệ.canvas]] (cột = tầng dữ liệu, mũi tên = dữ liệu đưa sang) – kéo thả, mở thẻ để đọc.
- **Aliases**: gõ `[[Đăng ký môn học` hay `[[ĐKMH` đều ra ghi chú DKMH; tên dữ liệu / trường có dấu cũng tìm được.
- **Backlinks** (khung phải): mở một dữ liệu / phân hệ / quy trình → thấy mọi tài liệu, quy trình, mô hình trường nhắc tới nó.
- **Graph view** – nhóm màu gợi ý (Graph → Groups, thêm 1 lần trên máy bạn): `path:Phan-he` · `path:Du-lieu` · `path:Quy-trinh` · `path:Truong OR path:Case-truong` · `path:Tai-lieu` · `path:Dang-case`; lọc bỏ menu: `-path:Menu`.
- **Callout** `[!warning] Hay gây case` trong quy trình = chỗ cài đặt / dữ liệu hay làm người test kết luận sai.

## Các ngăn
| Thư mục | Ghi gì |
|---|---|
| `Phan-he/` | Mỗi phân hệ (mã như trên ACS): là gì, **nhận dữ liệu từ**, **tạo ra**, **đưa sang**, sửa ở đây → kiểm lại đâu, phần Edusoft / phần web |
| `Du-lieu/` | Mỗi loại dữ liệu (DS SV học kỳ, KQ ĐKMH, nhóm học, điểm TB…): **phải có trước** gì (`can_co`), **là điều kiện cho** gì, tầng, tạo ở đâu (menu), dùng ở đâu, trên web, chuẩn bị dữ liệu test theo thứ tự |
| `Menu/` | `Menu/<phân hệ>.md` = toàn bộ menu Edusoft của phân hệ, mỗi menu nối tới dữ liệu nó đụng tới; menu **tạo** dữ liệu có ghi chú riêng (trước khi dùng phải có gì, lưu xong ảnh hưởng tới đâu) |
| `Dang-case/` | Mô hình case (hiển thị web, lỗi EX, số liệu sai, thiết lập, mẫu in, yêu cầu bổ sung, case tiếp nối…): nhận biết qua lời KH / BA / Dev, phải trả lời gì, case liên quan là gì, hay nhầm gì |
| `San-pham/` | Edusoft, Netweb, App: là gì, test ở đâu |
| `Truong/` | Từng trường: tên, **mã trên ACS**: 4 ký tự = trường, dài hơn = phân cấp (`phan_cap`, vd DHMOTX = DHMO từ xa), bản riêng VersionSchool, link Netweb thật, chức năng web; `AQ` = case nội bộ |
| `Repo-coder/` | Quy ước repo / nhánh coder → sửa ở web hay Edusoft |
| `Quy-trinh/` | Quy trình xuyên phân hệ (mở học kỳ, tuyển sinh, CTĐT – TKB, ĐKMH, học phí, thi, điểm, tốt nghiệp…): bảng bước – phân hệ – menu – phải có trước, cài đặt hay gây case, sửa thì kiểm gì |
| `Tai-lieu/` | Tài liệu nguồn: HDSD SharePoint theo phân hệ (từng file nói gì), lưu đồ, sheet, danh mục màn hình, source, ACS – độ tin cậy |
| `Case-truong/` | Mô hình từng trường học từ case ACS (tự động + nhận xét) |
| `Cach-test/` (Test - …) | Cách test theo loại sửa (lỗi EX, số liệu, mẫu in, web theo trường, API / bảo mật, hiển thị web) |

## Quy tắc
- Mỗi ghi chú có **Properties** (đầu file) – app đọc các trường này, **giữ đúng tên trường**:
  `nhan_tu` / `dua_sang` (phân hệ), `tao_o` / `dung_o` / `can_co` / `la_dieu_kien_cho` (dữ liệu), `test_tren`: `web` | `edusoft` | `app` | `api` | `mau-in`.
- `trang_thai`: `can-xac-nhan` (đoán / thiếu) → `tu-tai-lieu` (Claude điền từ tài liệu) → `da-xac-nhan` (người test đã kiểm). Claude chỉ coi `da-xac-nhan` là chắc chắn.
- **Ghi chú là nguồn**: sửa thẳng trong Obsidian (Properties `can_co`, `tao_o`, `dung_o`, `tu_khoa`… và các dòng `- [[…]] – vì sao`). App đọc lại khi bạn quay về cửa sổ app
  (đã chọn vault ở Test case ACS → Thiết lập ACS → Kết nối Claude Desktop → Chọn vault…). Claude Desktop cũng sửa được qua MCP khi bạn dạy kiến thức mới.
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

- [ ] `Truong/`: thêm `phan_cap` khi gặp mã phân cấp mới (mã > 4 ký tự)
- [ ] `Dang-case/`: sửa dấu hiệu / thêm case mẫu khi gặp case thật

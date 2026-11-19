---
loai: trang-chu
---
# Knowledge base test case (AQ Auto Test)

Kho kiến thức để **Claude và app AQ Auto Test hiểu đúng nghiệp vụ** khi test case coder đã xử lý trên ACS:
case này test ở đâu (Web / Edusoft / App / API / Mẫu in), khách hàng cần gì, test thế nào.

## Các ngăn
| Thư mục | Ghi gì | Mẫu |
|---|---|---|
| `San-pham/` | Từng sản phẩm: là gì, test ở đâu, dấu hiệu nhận biết trong case | `_templates/San pham` |
| `Phan-he/` | **Mỗi mã phân hệ trên ACS một ghi chú** (CSHP, DKMHUI, NETWEB-UI…): thuộc sản phẩm nào, test trên đâu | `_templates/Phan he` |
| `Truong/` | Môi trường test của từng trường: link web test, bản Edusoft test – **không ghi mật khẩu** | `_templates/Truong` |
| `Repo-coder/` | Quy ước repo / nhánh coder (vd `VersionSchool/<trường>/…`) → sửa ở web hay Edusoft | `_templates/Repo coder` |
| `Cach-test/` | Cách test theo loại case (sửa hiển thị web, sửa số liệu, mẫu in…) | `_templates/Cach test` |
| `Case/` | **Mỗi case đã test một ghi chú**: yêu cầu KH → hiểu đúng là → test ở đâu → plan → kết quả → bài học | `_templates/Case` |

## Quy tắc
- Mỗi ghi chú có phần **Properties** (đầu file, giữa hai dòng `---`) – app đọc các trường này, **giữ đúng tên trường**.
- `test_tren` chỉ dùng: `web`, `edusoft`, `app`, `api`, `mau-in` (nhiều giá trị thì viết dạng danh sách).
- `trang_thai`: `can-xac-nhan` (đoán / thiếu thông tin) → `tu-tai-lieu` (Claude điền từ tài liệu, người test liếc lại) → `da-xac-nhan` (người test đã kiểm).
  Claude coi `da-xac-nhan` là chắc chắn, hai mức còn lại chỉ là gợi ý.
- Nối các ghi chú bằng `[[...]]` (gõ `[[` rồi chọn) – vd case nối tới `[[KTTC]]`, `[[CSHP]]`.
- **Không** ghi mật khẩu, token, chuỗi kết nối vào kho này (kho nằm trong git).

## Đã điền sẵn (Claude, 19/11/2026)
Nguồn: tài liệu HDSD trên SharePoint "1. Tài liệu Edusoft", lưu đồ LuuDo_NEW (skill `tailieu-edusoft`), sheet Release(TestMenu)
(Menu_NEW, ChuyenDoiNetWeb, Port NetWEB, DHNT Điều hướng DVPC, NetWeb_DKMH, các sheet "(case)").
- `Phan-he/`: 24 mã – phân hệ Edusoft + NETWEB-UI, NETWEB-API, DKMHUI, CSHP, EDUGO, EDUBILL, GAM; mỗi mã tách **phần Edusoft / phần web**.
- `Truong/`: 21 trường theo sheet (tên, link Netweb thật, chức năng web trường có) + HVNG (môi trường test mặc định).
- `Case/`: 6 case lấy từ sheet release (có menu + kết quả test) + 15 case từ danh sách ACS (mới có tiêu đề – Claude đoán nơi test) + 64457.
- `Cach-test/`: lỗi EX Edusoft, sửa số liệu Edusoft, mẫu in, chức năng web theo trường, API & bảo mật web, sửa hiển thị web.

## Việc người test cần làm
- [ ] Liếc `Phan-he/` (nhất là NETWEB-UI, NETWEB-API, DKMHUI, CSHP) – đúng thì đổi `trang_thai: da-xac-nhan`
- [ ] Điền **web test / Edusoft test** cho các trường hay test trong `Truong/` (hiện mới có link trang thật)
- [ ] Mở các case trong `Case/` có "(chưa có – chép từ ACS)": dán yêu cầu KH, sửa phần "Test ở đâu" nếu Claude đoán sai, ghi **Bài học**

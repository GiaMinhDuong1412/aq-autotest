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
- Chưa chắc thì ghi `trang_thai: can-xac-nhan` – Claude sẽ không coi là chắc chắn.
- Nối các ghi chú bằng `[[...]]` (gõ `[[` rồi chọn) – vd case nối tới `[[KTTC]]`, `[[CSHP]]`.
- **Không** ghi mật khẩu, token, chuỗi kết nối vào kho này (kho nằm trong git).

## Việc cần làm trước
- [ ] Điền đủ `Phan-he/` cho các mã phân hệ hay gặp trên ACS
- [ ] Điền `Truong/` cho các trường hay test
- [ ] Chép 5–10 case test "đúng nghiệp vụ" vào `Case/`

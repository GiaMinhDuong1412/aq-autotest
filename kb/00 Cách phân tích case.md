---
loai: phuong-phap
trang_thai: tu-tai-lieu
---
# Cách phân tích một case ACS – phải ĐÚNG trước, test sau

Không đoán từ tiêu đề hay mã phân hệ. Đọc **theo thứ tự**, mỗi bước trả lời được câu hỏi của nó rồi mới sang bước sau.

## 0. Trường – case của ai?
- Lấy `school_code` trên ACS → tìm ghi chú `Truong/` có `ma_acs` chứa mã đó (DHNT có 5 mã ACS theo hệ / cơ sở: DHNTDHCQ, DHNTCHCQ…).
- Trả lời: trường nào, hệ / cơ sở nào; trường có **bản riêng** không (coder sửa `VersionSchool/<trường>` → [[VersionSchool]]); trường có những chức năng web nào.
- Mã `AQ` = case nội bộ / sản phẩm chung (không phải trường) → [[AQ]].
- Mã chưa có ghi chú → ghi lại "chưa biết trường", **không đoán tên trường**.

## 1. Phân hệ – case thuộc nghiệp vụ nào?
- `module` trên ACS → `Phan-he/<mã>`: phân hệ làm gì, phần Edusoft / phần web, nhận dữ liệu từ đâu, đưa sang đâu, **dạng case thường gặp**.
- Mã phân hệ là nơi case được **xếp**, không phải nơi lỗi xảy ra: CSHP có cả trang học phí trên web, DKMH có cả trang đăng ký trên web.

## 2. Yêu cầu khách hàng – KH thấy gì, muốn gì?
Tách thành 4 ý (bỏ chào hỏi, chữ ký, thư trích dẫn):
1. **Hiện trạng**: KH đang thấy gì, **ở đâu** (menu Edusoft / trang web / app / mẫu in), **ai** gặp (phòng đào tạo, SV, GV, CVHT…).
2. **Mong muốn**: các câu "cần / phải / mong muốn / đề nghị / bổ sung" – mỗi câu là một yêu cầu.
3. **Dữ liệu cụ thể**: MSSV, mã lớp, học kỳ, đợt, số tiền, ảnh chụp – để tái hiện đúng trường hợp.
4. **Loại**: lỗi phần mềm / yêu cầu thay đổi – bổ sung / hỏi cách dùng / nhờ xử lý dữ liệu → chọn [[#6. Dạng case|dạng case]].

## 3. BA đã phân tích gì?
- BA chốt: **lỗi hay yêu cầu mới**, phạm vi (màn hình / trang nào, trường nào, đối tượng nào), **quy tắc nghiệp vụ đúng** (vd thứ tự ưu tiên miễn giảm).
- BA chốt khác cách KH viết → **theo BA** (BA đã thống nhất với KH); ghi rõ chỗ khác.
- Không có phần BA → ghi "chưa có BA" và đánh dấu câu hỏi mở – không tự suy ra quy tắc nghiệp vụ.

## 4. Dev đã xử lý gì?
- **Sửa ở đâu**: `VersionSchool/<trường>/<case>-…` = bản riêng của trường (đa số là web); Source.NET / store / procedure = Edusoft; report / biểu mẫu = mẫu in.
- **Bản nào**: số bản dạng `2026.11J.18` – môi trường test phải có đúng bản này.
- **Sửa gì / không sửa gì**: dev chỉ xử lý một phần → phần còn lại là câu hỏi mở, không được ghi "đạt".

## 5. Đối chiếu KH ↔ BA ↔ Dev
Bảng: mỗi ý KH muốn → BA chốt thế nào → Dev đã làm chưa. Ý nào **không khớp / thiếu** → câu hỏi mở cho BA / Dev **trước** khi test.

## 6. Dạng case
Xếp vào một mô hình trong `Dang-case/` (có thể 2 dạng): [[Hien thi web]], [[Loi EX Edusoft]], [[So lieu tinh sai]], [[Luu cap nhat khong duoc]], [[Mau in bao cao]],
[[Thiet lap khong hieu luc]], [[Tai khoan phan quyen]], [[Yeu cau bo sung]], [[Xu ly du lieu]], [[Hieu nang]], [[Tich hop thanh toan]], [[Hoi dap nghiep vu]], [[Case tiep noi]].
Dạng case quyết định: đọc thêm gì, case liên quan là gì, sau này test ở đâu.

## 7. Dữ liệu và ảnh hưởng
Case đụng dữ liệu nào (`Du-lieu/`) → **muốn tái hiện phải có dữ liệu gì trước** ([[00 Logic nghiệp vụ]]) → sửa xong **ảnh hưởng tới** dữ liệu / phân hệ nào.

## 8. Case liên quan / tương tự → gợi ý cho người test
Tìm trên ACS (MCP `acs_case_lien_quan`, hoặc khung Case liên quan trong app):
- **Case gốc / lần trước**: tiêu đề có `[mã]` (vd `[64184]: Hiển thị miễn giảm – lần 2`) → đọc case gốc trước: lần 1 sửa gì, lần này còn thiếu gì.
- **Cùng trường + cùng phân hệ / cùng dữ liệu**: thường cùng đợt KH gửi, cùng bản sửa → test cùng lúc.
- **Cùng mô hình ở trường khác**: cùng dạng case + cùng dữ liệu (vd hiển thị miễn giảm trên trang học phí) → cách sửa / lỗi có thể lặp lại; nếu là phần dùng chung (không phải VersionSchool) thì sửa ở đây có thể ảnh hưởng trường khác.
- **Dữ liệu cha – con**: case đang chờ test chạm dữ liệu phải có trước / sinh ra sau → dùng chung dữ liệu chuẩn bị.
Gợi ý ghi rõ **vì sao** liên quan và **nên làm gì** (đọc trước / test chung / hỏi BA).

## 9. Chỉ khi 0–8 rõ mới soạn plan test

## Phiếu phân tích (mẫu)
| Mục | Ghi |
|---|---|
| Trường | mã ACS → trường, hệ / cơ sở, bản riêng? |
| Phân hệ | mã → tên, phần nào (Edusoft / web) |
| KH thấy | ở đâu, ai, hiện trạng |
| KH muốn | từng ý |
| Dữ liệu KH đưa | MSSV, lớp, học kỳ… |
| BA chốt | lỗi / yêu cầu mới, phạm vi, quy tắc |
| Dev đã làm | repo, bản, nội dung sửa |
| Đối chiếu | ý nào đủ, ý nào thiếu → câu hỏi mở |
| Dạng case | [[…]] |
| Dữ liệu / ảnh hưởng | phải có trước, ảnh hưởng tới |
| Case liên quan | mã – vì sao – nên làm gì |

## Ví dụ – case 64457 (đúng / sai)
- **Trường** KTTC (có bản riêng VersionSchool/KTTC). **Phân hệ** CSHP.
- **KH**: phần summary và cột miễn giảm trên bảng phải tương ứng; diện chính sách hiển thị trước miễn giảm theo SV → hiện trạng ở **trang học phí của SV trên web**.
- **Dev**: `VersionSchool/KTTC/64457-hien-thi-mien-giam-hoc-phi-lan-2`, bản 2026.11J.18 → sửa giao diện web riêng KTTC.
- **Dạng**: [[Hien thi web]] + [[Case tiep noi]] (tiêu đề `[64184]` → đọc case 64184: lần 1 sửa gì).
- **Dữ liệu**: Diện chính sách / miễn giảm, Học phí phải thu – SV test phải **có cả hai loại miễn giảm** mới kiểm được thứ tự.
- **Sai đã mắc**: gán kịch bản Edusoft QLSV-018 vì cùng "học phí" – bỏ qua KH nói trang web và Dev sửa VersionSchool.

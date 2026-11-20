---
loai: phuong-phap
trang_thai: tu-tai-lieu
---
# Cách phân tích một case ACS – phải ĐÚNG trước, test sau

Không đoán từ tiêu đề hay mã phân hệ. Đọc **theo thứ tự**, mỗi bước trả lời được câu hỏi của nó rồi mới sang bước sau.

## Trước hết: phiếu case ACS đủ thông tin chưa?
Đọc đủ các trường như màn hình case trên ACS: **đầu case** (trạng thái, phân công, hạn trả, cổng CST, liên quan), **quy trình 5 bước**
(Tiếp nhận → BA phân tích → DEV xử lý → Kiểm thử → Gửi email & Đóng: ai, lúc nào, đang ở bước nào), **khách hàng** (khách hàng / đơn vị, phân hệ,
danh xưng – tên, mail, loại hợp đồng – vd HĐ bảo trì, số / ngày hợp đồng), tab **Gửi mail / Lịch sử / Đính kèm**.
Kiểm đủ: trường – phân cấp, phân hệ, yêu cầu KH, BA đã phân tích, Dev đã xử lý, **bản sửa**, hạn trả, người test, ảnh / đính kèm.
Thiếu mục nào → nói ngay, hỏi BA / Dev trước khi phân tích tiếp. (App: khung **Phiếu case ACS** ở bước 1; MCP: `phieu_acs`, `kiem_tra_du` của `acs_case`.)

## 0. Trường – case của ai, phân cấp nào?
- `school_code` trên ACS: **4 ký tự = trường** (case chung của trường), **dài hơn 4 ký tự = phân cấp** (đơn vị phân cấp: hệ / cơ sở) của trường có 4 ký tự đầu đó.
  Ví dụ `DHMO` = ĐH Mở (chung); `DHMOTX` = DHMO – đào tạo từ xa; `DHMODH` = DHMO – đại học; `DHNTCHCQ` = Ngoại Thương – cao học.
- **Case làm theo phân cấp chỉ có hiệu lực trên phân cấp đó**: test trên đúng site / dữ liệu của phân cấp; phân cấp khác của cùng trường thường không bị ảnh hưởng (trừ khi sửa phần chung).
- Mở ghi chú `Truong/<4 ký tự>`: tên trường, `phan_cap` đã biết, bản riêng (coder sửa `VersionSchool/<trường>` → [[VersionSchool]]), chức năng web.
- Mã `AQ` = case nội bộ / sản phẩm chung (không phải trường) → [[AQ]].
- Mã chưa có ghi chú → ghi "chưa biết trường", **không đoán tên trường**; phân cấp chưa có tên → hỏi rồi thêm vào `phan_cap`.
- **Mô hình trường**: mở `Case-truong/<4 ký tự>` ([[00 Mô hình trường]]) – trường này hay có case ở phân hệ nào, dạng gì, chủ đề lặp lại, chuỗi case tiếp nối, *Nhận xét* (cách trường dùng phần mềm, BA hay chốt gì). Case mới giống case cũ → đọc lại case cũ trước.

## 1. Phân hệ – case thuộc nghiệp vụ nào?
- `module` trên ACS → `Phan-he/<mã>`: phân hệ làm gì, phần Edusoft / phần web, nhận dữ liệu từ đâu, đưa sang đâu, **dạng case thường gặp**.
- Mã phân hệ là nơi case được **xếp**, không phải nơi lỗi xảy ra: CSHP có cả trang học phí trên web, DKMH có cả trang đăng ký trên web.
- Đặt case vào **quy trình** ([[00 Quy trình xuyên phân hệ]], mục *Nằm trong quy trình* của phân hệ): bước trước cung cấp gì (lỗi có thể do đầu vào), **cài đặt / biến chỉnh định hay gây case** ở bước đó (vd thời gian ĐKMH online: 4 biến + restart IIS; EduBILL: học kỳ thanh toán phải trùng học kỳ thu học phí), bước sau phải kiểm.
- Cần cách thao tác chuẩn / tên biến → [[00 Tài liệu nguồn]] (HDSD theo phân hệ trên SharePoint, lưu đồ LuuDo_NEW).

## 2. Yêu cầu khách hàng – KH thấy gì, muốn gì?
Tách thành 4 ý (bỏ chào hỏi, chữ ký, thư trích dẫn):
1. **Hiện trạng**: KH đang thấy gì, **ở đâu** (menu Edusoft / trang web / app / mẫu in), **ai** gặp (phòng đào tạo, SV, GV, CVHT…).
2. **Mong muốn**: các câu "cần / phải / mong muốn / đề nghị / bổ sung" – mỗi câu là một yêu cầu.
3. **Dữ liệu cụ thể**: MSSV, mã lớp, học kỳ, đợt, số tiền, ảnh chụp – để tái hiện đúng trường hợp.
4. **Loại**: lỗi phần mềm / yêu cầu thay đổi – bổ sung / hỏi cách dùng / nhờ xử lý dữ liệu → chọn [[#6. Dạng case|dạng case]].

**Ảnh – xem trước khi kết luận.** Ảnh KH / BA / Dev chụp nói nhiều hơn lời: đúng màn hình / menu / trang web nào, cột nào, số liệu nào, câu báo lỗi, chỗ khoanh đỏ.
- MCP: `acs_case` trả danh sách `anh` (chỗ `[ảnh]` trong lời KH là nơi chèn ảnh) → `acs_anh` để xem. App: bước 1 có khung **Ảnh trong case**.
- Lời KH và ảnh khác nhau → **tin ảnh**, ghi rõ chỗ khác. Ảnh cho biết nơi lỗi (trang web hay màn hình Edusoft) → quyết định test ở đâu.
- Ghi điều thấy trong từng ảnh vào phiếu (mục **Ảnh**) để lần sau tra được (`kb_tim` tìm cả mô tả ảnh của phiếu cũ).
- Ảnh đáng giữ làm mẫu (không lộ thông tin cá nhân) → `kb_luu_anh` (ảnh vào `Anh/`, chỉ ở máy – không lên git; mô tả trong ghi chú .md).

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
- **Cùng trường (cùng phân cấp) + cùng phân hệ / cùng dữ liệu**: thường cùng đợt KH gửi, cùng bản sửa → test cùng lúc. Cùng trường nhưng **khác phân cấp** → chỉ tham khảo.
- **Cùng mô hình ở trường khác**: cùng dạng case + cùng dữ liệu (vd hiển thị miễn giảm trên trang học phí) → cách sửa / lỗi có thể lặp lại; nếu là phần dùng chung (không phải VersionSchool) thì sửa ở đây có thể ảnh hưởng trường khác.
- **Dữ liệu cha – con**: case đang chờ test chạm dữ liệu phải có trước / sinh ra sau → dùng chung dữ liệu chuẩn bị.
Gợi ý ghi rõ **vì sao** liên quan và **nên làm gì** (đọc trước / test chung / hỏi BA).

## 9. Chỉ khi 0–8 rõ mới soạn plan test
- Plan = **luồng thao tác thật, ngắn**: ai đăng nhập → làm gì → kết quả đúng là gì → kiểm từng ý KH. Luồng có sẵn ở `Luong-test/` (vd [[Diem danh QR]]).
- **Nhờ người dùng cung cấp tài khoản test theo ngữ cảnh** (chỉ mã, không mật khẩu): điểm danh QR → mã GV có lớp đang dạy + MSSV thuộc lớp đó;
  trang học phí → MSSV có miễn giảm… Bước ghi `{Mã GV}`, app thay bằng giá trị người dùng nhập.
- Không thêm mục chung chung hay dữ liệu không liên quan (vd case điểm danh không phải "điểm rèn luyện").

## Phiếu phân tích (mẫu)
| Mục | Ghi |
|---|---|
| Trường | mã ACS → trường (4 ký tự) + phân cấp (nếu có), bản riêng? |
| Phân hệ | mã → tên, phần nào (Edusoft / web) |
| KH thấy | ở đâu, ai, hiện trạng |
| Ảnh | từng ảnh: thấy gì (màn hình, cột, số liệu, câu báo) |
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

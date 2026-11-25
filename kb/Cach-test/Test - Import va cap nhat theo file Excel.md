---
loai: cach-test
ten: "Test - Import và cập nhật theo file Excel"
trang_thai: tu-tai-lieu
nguon: tai-lieu
tai_lieu: "[[HDSD QLHT]]"
tags: [cach-test, import, excel]
aliases:
  - "Import Excel"
  - "Cập nhật theo file"
  - "Tool Import"
---
# Test – Import và cập nhật theo file Excel

> [!info] Nguồn
> `QLHT_HuongDanImport` (SharePoint › TaiLieuTrienKhai_EduSoft.NET › QLHT-MoiTruong; DOC/QLHT) – "Qui trình hướng dẫn các bước sử dụng Tool Import để đổ dữ liệu vào Edusoft".
> Danh sách menu "theo file / từ file / Import" lấy từ danh mục màn hình (`web/edusoft-catalog.json`). Dùng chung cho mọi case có import / cập nhật theo file.

## 1. Hai kiểu "theo file" trên Edusoft
| Kiểu | Nhận biết | File cần |
|---|---|---|
| **Tool Import chung** – nút **Import** trên màn hình nhập liệu (gần như mọi màn hình nhập tay đều có) | cửa sổ Import 3 vùng: cấu hình · lưới dữ liệu · nút Quay lại / Xuất cấu trúc import / Xem dữ liệu / Tiếp tục / Đóng | file theo **Xuất cấu trúc import** (khuyên dùng) hoặc file bất kỳ rồi **map cột** |
| **Menu chuyên "… theo file / từ file"** (bảng cuối trang) | tên menu có "theo file", "từ file", "Import …", "Cập nhật … từ file" | thường là danh sách **khóa** (mã SV, mã nhóm, mã CB…) + cột cần cập nhật; cấu trúc lấy bằng Xuất cấu trúc import của chính menu đó |

## 2. Cửa sổ Import – các ô cấu hình (vùng 1)
- **Chọn tập tin** (file phải **đóng** trước khi chọn) hoặc **Dán từ bộ nhớ (clipboard)** / Ctrl+V một vùng copy từ Excel.
- **Chọn sheet** (file nhiều sheet), **Có tiêu đề**, **Dòng tiêu đề** (dòng số mấy), **Dữ liệu từ dòng**.
- **Chuyển sang bảng mã chuẩn** (về Unicode), **Bảng mã gốc**, **Kiểm tra mã font tất cả dữ liệu** (TCVN3 / VNI → font chuẩn).
- **Định dạng ngày** của file (dd/MM/yyyy …) – sai là lỗi format ngày.

## 3. File Excel cần thế nào
- Lấy mẫu bằng **Xuất cấu trúc import** của đúng màn hình → app tự **map đúng cột** khi Tiếp tục (không phải map tay).
- **Giữ nguyên 2 dòng đầu** (dòng 1–2 để chương trình nhận dạng trường); dữ liệu từ dòng 3.
- Cột **tô vàng** = bắt buộc / quan trọng (khóa chính, khóa ngoại, tên); cột **trắng** = tùy chọn.
- Mã tham chiếu (lớp, ngành, môn, CB…) phải **đã có** trong danh mục – nếu không là lỗi sai khóa ngoại.
- Độ dài / kiểu từng cột: xem màn hình trong trang **Màn hình Edusoft** của app (lưới → cột: kiểu, bắt buộc *, độ dài tối đa – từ `AQFileField`).
- File tự soạn (không theo cấu trúc): Chọn tập tin → Tiếp tục → **map** từng trường chương trình ↔ cột file (trường không map thì không truyền).

## 4. Kết quả kiểm tra trước khi Thực hiện (Tiếp tục)
| Thông báo | Nghĩa | Xử lý |
|---|---|---|
| Dữ liệu có thể thêm mới / hợp lệ | sẽ được import | – |
| Dữ liệu cập nhật | dòng trùng khóa ở chức năng cho cập nhật | kiểm cột nào bị ghi đè |
| Lỗi sai format dữ liệu | sai kiểu (ngày, số…) | sửa file |
| Lỗi dữ liệu quá độ dài cho phép | vượt độ dài field | rút ngắn / nhờ admin tăng |
| Lỗi sai khóa ngoại | mã tham chiếu chưa có | nhập danh mục trước |
| Lỗi trùng khóa trên file | 2 dòng cùng khóa | xóa dòng trùng |
| Lỗi đã tồn tại khóa trong database | trùng dữ liệu đã có | bỏ qua được – dòng đó **không** import |
Mỗi loại có **Số dòng** + **Xem chi tiết** (lưu ra Excel để sửa rồi import lại). Cuối cùng bấm **Thực hiện**.

## 5. Cách test một case import / cập nhật theo file
1. **Đọc case**: menu nào, thêm mới hay **cập nhật**, khóa là gì, cột nào được cập nhật, KH gửi file mẫu chưa (tab Đính kèm).
2. **Lấy file mẫu**: Xuất cấu trúc import ở đúng menu trên bản test; ghi tên cột + cột vàng vào plan.
3. **Soạn file test** (dữ liệu tiền tố `AUTO…` / `TEST_…`, hoặc chọn SV / mã có sẵn trên bản test – **không** dùng file thật của KH chứa dữ liệu cá nhân):
   - 2–3 dòng **hợp lệ** (đúng điều kiện case sửa);
   - mỗi loại lỗi 1 dòng: sai format (ngày / số), quá độ dài, sai khóa ngoại, trùng trong file, đã tồn tại;
   - với **cập nhật**: 1 dòng để trống cột tùy chọn → kiểm "trống = xóa giá trị" hay "giữ nguyên" (hay là chỗ case sai);
   - nếu case nói về font / ngày: thêm dòng TCVN3 / định dạng ngày khác.
4. **Chạy**: Import → chọn file → kiểm map → Tiếp tục → **đối chiếu số dòng từng loại** với file → chụp ảnh → Thực hiện.
5. **Kiểm sau import**: lọc lưới theo khóa từng dòng – giá trị đúng, cột không có trong file **không bị ghi đè**, dòng lỗi **không** vào; kiểm màn hình / báo cáo dùng dữ liệu đó (kb `Du-lieu/` → "Dùng ở") và trang web nếu dữ liệu hiện trên Netweb ([[00 Liên kết Netweb - Edusoft]]).
6. **Không ảnh hưởng**: import tay 1 dòng (nút Thêm) vẫn chạy; menu import khác của cùng màn hình.
7. **Dọn dữ liệu**: xóa / khôi phục các dòng test (cập nhật thì ghi lại giá trị cũ trước khi import).

## 5b. Bài học từ case thật – cập nhật theo file làm đè cột liên quan
Case S38.01 *Xem/sửa thẩm tra văn bằng* (DHMOTX, thêm cột **Nơi cấp VB trước sáp nhập** `MaNCVBTSN` cạnh **Nơi cấp VB** `MaNCVB`):
sửa tay thì đúng, nhưng **Cập nhật theo file** chỉ có cột mới → chương trình thấy ô `MaNCVB` trống nên **tự điền** Nơi cấp VB theo văn bằng
của SV (hoặc bằng giá trị cột mới) → hai cột thành một. Mở lại 2 lần vì lỗi này. Áp dụng cho mọi case thêm cột / sửa import:
- **Ô trống trong file ≠ không đụng tới**: màn hình có thể tự suy ra giá trị (lấy theo dữ liệu gốc, đồng bộ). Luôn có dòng test *chỉ điền cột mới,
  cột liên quan để trống* trên bản ghi **đã có** giá trị cột liên quan → sau Thực hiện cột liên quan phải giữ nguyên.
- Trước khi bấm Thực hiện: **Xem chi tiết** nhóm "Dữ liệu có thể cập nhật" (lưới *Thông tin dữ liệu*) – cột nào sẽ được ghi hiện ở đây; cột liên quan
  hiện giá trị trong khi file để trống = chương trình tự điền → chụp ảnh, đó là lỗi.
- Ghi giá trị **trước** của từng bản ghi test (ảnh hoặc Xuất Excel) để so và để trả lại khi dọn.
- Kiểm cả các đường ghi khác cùng cột: **Import** (thêm mới), **Đồng bộ** (tất cả / chưa có), **Sửa** tay, màn hình nhập kết quả liên quan.
- **Cột mới không hiện khi Xuất Excel**: lưới đã *Lưu giao diện* riêng thì cột thêm sau bị ẩn – mở Column Chooser (chuột phải tiêu đề cột) kéo cột vào,
  lưu giao diện rồi xuất lại; kiểm cả 2 tuỳ chọn xuất (theo kiểu dữ liệu database / như trên màn hình). Không phải lỗi code nhưng phải ghi vào trả lời KH.
- Case theo **phân cấp** (view riêng của DHMOTX): mở cùng menu ở trường gốc (DHMO) để chắc không lỗi.
- Bảng dòng test mẫu (7 dòng A–G: chỉ cột mới / cả hai / chỉ cột cũ / bản ghi trống cột cũ / không có cột mới – hành vi cũ / mã sai danh mục / hai cột trùng nhau)
  dùng lại được cho case "thêm cột thứ hai cùng danh mục" khác.

## 6. Bộ test tự động (đề xuất – chưa có lệnh)
Hiện `aqrun.py` chưa có lệnh import file. Đề xuất: `xlsx:` (openpyxl tạo file từ mẫu Xuất cấu trúc + dòng test), `import: <file> @ <Màn hình>` (bấm Import → hộp chọn file → Tiếp tục), `import_check: hợp lệ=2, sai khóa ngoại=1 …` (đọc Số dòng từng loại), `import_do` (Thực hiện) rồi `find_row:` kiểm từng dòng.

## 7. Menu "theo file / từ file / Import" trên Edusoft (danh mục màn hình)
| Phân hệ | Menu (mã · tên) |
|---|---|
| AQ | `AQ03_15` Import dữ liệu phân tích số liệu · `AQ03_6` Cập nhật database từ file · `AQ03_7` Xóa field từ file import |
| CSHP | `P24.04` In hóa đơn học phí và TKB - Theo file |
| DIEM | `DQT31.06` Hủy điểm không đạt SV - theo file · `D63.06` In điểm tích lũy theo file sinh viên · `D68.03` In giấy xác nhận theo file · `D64.07` In phiếu điểm sinh viên TN - Theo file · `D62.04` In phiếu điểm sinh viên - Theo file · `D52.12` Cộng điểm TB - mở  khóa số theo file SV · `D52.05` Cộng điểm TB - theo file sinh viên |
| DKMH | `MAT1.02` Khóa kết quả đăng ký theo file · `MAT1.03` Mở khóa kết quả đăng ký theo file · `M27` Chuyển KQĐK khác học kỳ theo file · `M4.12` Thống kê TKB SV theo file mã sv |
| DMKT | `D25.10` Download điểm từ EduWEB · `D25.01` File Excel dạng hàng dọc · `D25.03` Import Excel nhiều file · `D25.13` Import ghi chú điểm · `D25.02` Import từ file excel · `D25.09` Import điểm + nhóm học · `D25.12` Import điểm + ĐKMH + Tạo nhóm học · `D25.08` Import điểm nhiều học kỳ · `D25.11` Import điểm quá trình · `D25.07` Từ phần mềm McScanner · `D25.30` Xem ảnh file scan · `D25.31` Xem/sửa lý do vào sai điểm · `D22.01` Import từ phần mềm McScanner · `D31.05.1` In điểm bảo lưu sinh viên - theo file · `D31.36` Tạo file import từ Bộ bảo lưu · `D41.07` Cập nhật điểm theo file |
| HTQL | `H97` Import file report |
| KHGD | `K8.10.1` Cập nhật thông tin nhóm tổ · `K8.10.2` Import CBGD cho tổ hợp · `K8.10.3` Import thêm lớp cho nhóm tổ · `K.110` Cập nhật thời khóa biểu · `K.106` Import nhóm/tổ học & TKB · `K.104` Import nhóm/tổ học không TKB · `K.112` Import tổ hợp |
| KSDG | `Z2.03.01` Định nghĩa file import excel · `Z2.03.02` Định nghĩa file import scan |
| LTHI | `L23.04` Hủy theo file · `L34.09` Phân tổ thi theo file |
| QKTX | `X50.30.02` Nhập/import điểm đánh giá · `X20.10.11` Import hợp đồng · `X30.30.05` Import phiếu thu |
| QLMC | `EE2.06` Import bộ tiêu chuẩn mẫu từ BGD |
| QLNS | `N8.04` Cập nhật lý lịch viên chức theo file · `N0.1` Import ảnh CBCNV |
| QLSV | `STV3` Truy vết đổi mã sinh viên theo file · `S32A` Cập nhật hồ sơ SV từ file · `S32B` Hủy hồ sơ SV từ file · `S401` Cập nhật văn bằng từ file · `S400` Thêm văn bằng SV từ file · `S67` In DSSV khen thưởng/kỷ luật theo file · `S.19.07` In giấy chứng nhận theo file · `S15.09A` Nhập QĐ tốt nghiệp từ file xét TN · `S2.04` Cập nhật lý lịch SV từ file · `S2.02` Import ảnh sinh viên · `S2.03A` Cập nhật thông tin nội trú/ngoại trú theo file · `S.10.3.06` In bằng tốt nghiệp theo file · `S.10.2.05` In giấy chứng nhận theo file · `S904` In phiếu điểm rèn luyện theo file · `S70` Import sinh viên vắng · `S81.20` Import điểm rèn luyện · `S83.03` Import điểm rèn luyện · `S83.15` In điểm rèn luyện toàn khóa theo file |
| QLTN | `QGD13.05` Xét theo file mã SV (HTGĐ) · `Q62.01` Kiểm tra dữ liệu liên quan của sinh viên theo file · `Q53.06A` Xét tạm theo file SV và tiêu chuẩn (TN) · `Q81.01` Xóa theo file sinh viên |
| QLTS | `T9.06.02` Theo File · `T9.03.02.A` Gán tên lớp theo file bởi MaSV · `T2.06` Import ảnh thí sinh · `T10.00.0` Import ảnh thí sinh · `T4.17.02` Theo File · `T6.17.02` Theo File |
| QLTV | `V0.01.28` Import hóa đơn điện tử · `V13` In chi tiết học phí 1 SV theo file · `V13A` In chi tiết học phí 1 SV theo file (Mẫu 2) · `V07` In phiếu hoàn theo file SV · `V14` In tổng hợp học phí 1 SV theo file · `V0.03.03` Kiểm tra tính học phí theo file · `V0.1.23` Import học phí và vãng lai · `V0.1.10` Import phiếu hoàn · `V04` Import phiếu thu · `H90.14` Trích xuất SV từ file ngân hàng |

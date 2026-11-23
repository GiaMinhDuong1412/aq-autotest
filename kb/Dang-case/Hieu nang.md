---
loai: dang-case
ten: Chậm / treo / quá tải
dau_hieu_kh: "chậm|treo|lâu|quá tải|timeout|không phản hồi|đứng|nghẽn|nhiều (sinh viên|người) cùng lúc"
dau_hieu_ba: "hiệu năng|tải|tối ưu"
dau_hieu_dev: "index|tối ưu|cache|query"
noi_hay_gap:
  - web
  - edusoft
phan_he_hay_gap:
  - "[[DKMH]]"
  - "[[DKMHUI]]"
  - "[[DIEM]]"
trang_thai: tu-tai-lieu
---
# Chậm / treo / quá tải

Chức năng chạy được nhưng chậm, treo – thường vào đợt cao điểm (ĐKMH hàng nghìn SV cùng lúc, xem điểm, tính học phí toàn trường).

## Nhận biết
- **Lời KH**: `chậm|treo|lâu|quá tải|timeout|không phản hồi|đứng|nghẽn|nhiều (sinh viên|người) cùng lúc`
- **BA**: `hiệu năng|tải|tối ưu`
- **Dev**: `index|tối ưu|cache|query`
(biểu thức để app gợi ý dạng case – sửa ở Properties `dau_hieu_*`)

## Phải trả lời khi phân tích
- Thời điểm, số người dùng cùng lúc, chức năng nào
- Chậm ở Edusoft (tính toán) hay web (truy cập đông)
- Dev tối ưu gì – kết quả có giữ đúng không (không chỉ nhanh hơn)

## Case liên quan với dạng này là
Cùng chức năng ở trường lớn khác; đợt ĐKMH sắp tới (sheet NetWeb_DKMH).

## Đo thời gian mở form trên Edusoft (người dùng dạy 23/11)
- Nhấn **Ctrl+Shift+T** trước khi mở menu → Edusoft hiện **"Thời gian mở form: Ns"** ở **thanh dưới đáy** cửa sổ chính (cạnh Năm học / Học kỳ).
- **Đo như người dùng thao tác** (người dùng dạy 23/11): chậm thường không phải lúc mở menu mà lúc **ra dữ liệu**. Ví dụ #63652 *Thu/chi HP › An toàn dữ liệu › Nhật ký thu học phí của sinh viên*:
  1. Ctrl+Shift+T → mở menu;
  2. bấm nút **…** cạnh ô **Mã SV** (khung Thông tin sinh viên) → form *Danh sách sinh viên* → chọn mã SV → bấm **Chọn**;
  3. dữ liệu (Nhật ký phiếu thu) hiện ra → đọc **Thời gian mở form** ở thanh dưới đáy → chụp ảnh.
  Đầu ra = số giây đó sau khi Dev sửa (so với lúc KH báo), dữ liệu đủ, không treo.
- Bộ test (máy test thao tác như người dùng, không phải đo tự động lúc mở menu): `menu_time:` (Ctrl+Shift+T + mở menu) → `fieldbtn: Mã SV` (nút …) → `find_row: {MSSV} @ Mã SV` (hoặc `pick:` chọn ngẫu nhiên) → `time_click: Chọn` (bấm, chờ dữ liệu, đọc "Thời gian mở form", chụp ảnh) → đầu ra `time_check: 10` (≤ 10 giây = Đạt, bộ test tự so – người test chỉ xem lại ảnh).

## Hay nhầm
Chậm do mạng / máy chủ của trường → không phải lỗi phần mềm.

## Phân hệ hay gặp
[[DKMH]], [[DKMHUI]], [[DIEM]]

## Case mẫu (tiêu đề từ danh sách ACS – cần đọc nội dung đầy đủ)
- 63194 (Site đăng ký môn học mới)

Xem cách đọc case: [[00 Cách phân tích case]].

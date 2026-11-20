---
loai: dang-case
ten: Thiết lập / cấu hình ở một nơi – tác dụng ở nơi khác
dau_hieu_kh: "thiết lập|setting|cài đặt|cấu hình|chỉnh định|thời gian (đăng ký|nhập điểm|rút)|ràng buộc|mở cho|khóa|cho phép|không cho"
dau_hieu_ba: "thiết lập|cấu hình|chỉnh định"
dau_hieu_dev: "config|setting|chỉnh định"
noi_hay_gap:
  - edusoft
  - web
phan_he_hay_gap:
  - "[[DKMH]]"
  - "[[QLHT]]"
  - "[[KSDG]]"
  - "[[DIEM]]"
  - "[[CSHP]]"
trang_thai: tu-tai-lieu
---
# Thiết lập / cấu hình ở một nơi – tác dụng ở nơi khác

Phòng đào tạo **cài** trên Edusoft (thời gian ĐKMH, ràng buộc, chỉnh định NetWEB, cấm SV nợ học phí…) nhưng **hiệu lực** sai ở nơi dùng (thường là web của SV / GV).

## Nhận biết
- **Lời KH**: `thiết lập|setting|cài đặt|cấu hình|chỉnh định|thời gian (đăng ký|nhập điểm|rút)|ràng buộc|mở cho|khóa|cho phép|không cho`
- **BA**: `thiết lập|cấu hình|chỉnh định`
- **Dev**: `config|setting|chỉnh định`
(biểu thức để app gợi ý dạng case – sửa ở Properties `dau_hieu_*`)

## Phải trả lời khi phân tích
- Cài ở đâu (menu Edusoft) – có hiệu lực ở đâu (trang web / chức năng nào)
- Cài cho đối tượng nào (lớp, SV, khối) – đối tượng ngoài phạm vi phải không bị ảnh hưởng
- Lỗi ở phần **cài** (lưu sai, lặp dòng) hay phần **áp dụng** (web không theo cài đặt)?

## Case liên quan với dạng này là
Cùng thiết lập ở đợt / học kỳ khác; các trang web đọc thiết lập này; case cùng thiết lập ở trường khác.

## Hay nhầm
Lặp dòng / sai trên màn hình cài đặt Edusoft là lỗi phía Edusoft; web không theo thiết lập là lỗi phía web – thường phải xem **cả hai**.

## Phân hệ hay gặp
[[DKMH]], [[QLHT]], [[KSDG]], [[DIEM]], [[CSHP]]

## Case mẫu (tiêu đề từ danh sách ACS – cần đọc nội dung đầy đủ)
- 64693 (lặp dòng khi setting thời gian ĐKMH từng SV)
- 63722 (khảo sát trước khi xem điểm)

Xem cách đọc case: [[00 Cách phân tích case]].

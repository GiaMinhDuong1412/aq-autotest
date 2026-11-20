---
loai: dang-case
ten: Tích hợp – thanh toán – đồng bộ với hệ thống ngoài
dau_hieu_kh: "ngân hàng|thanh toán|bill|hóa đơn|đồng bộ|tích hợp|api|kết nối (với|hệ thống)|sso|lms|moodle"
dau_hieu_ba: "tích hợp|đối tác|ngân hàng"
dau_hieu_dev: "api|webhook|bill|integration"
noi_hay_gap:
  - api
  - web
phan_he_hay_gap:
  - "[[EDUBILL]]"
  - "[[QLTV]]"
  - "[[NETWEB-API]]"
trang_thai: tu-tai-lieu
---
# Tích hợp – thanh toán – đồng bộ với hệ thống ngoài

Dữ liệu đi / về giữa Edusoft – Netweb và hệ thống ngoài: ngân hàng, hóa đơn điện tử (Bill), LMS, SSO.

## Nhận biết
- **Lời KH**: `ngân hàng|thanh toán|bill|hóa đơn|đồng bộ|tích hợp|api|kết nối (với|hệ thống)|sso|lms|moodle`
- **BA**: `tích hợp|đối tác|ngân hàng`
- **Dev**: `api|webhook|bill|integration`
(biểu thức để app gợi ý dạng case – sửa ở Properties `dau_hieu_*`)

## Phải trả lời khi phân tích
- Hai đầu là gì, dữ liệu nào đi chiều nào
- Lỗi ở phía AQ hay phía đối tác
- Có môi trường test của đối tác không – **không** thanh toán thật

## Case liên quan với dạng này là
Phiếu thu / nợ học phí sau khi thanh toán; các trường dùng cùng ngân hàng / đối tác.

## Hay nhầm
Thanh toán xong nhưng nợ không giảm → xem cả [[So lieu tinh sai]] (công nợ).

## Phân hệ hay gặp
[[EDUBILL]], [[QLTV]], [[NETWEB-API]]

## Case mẫu (tiêu đề từ danh sách ACS – cần đọc nội dung đầy đủ)
- (chưa có)

Xem cách đọc case: [[00 Cách phân tích case]].

---
loai: trang-web
ten: "Xem học phí, hóa đơn điện tử"
vai_tro:
  - "sv"
  - "ph"
menu_web: "Xem học phí · Hóa đơn điện tử"
du_lieu:
  - "[[Hoc phi]]"
  - "[[Phieu thu]]"
  - "[[No hoc phi]]"
ghi: []
phan_he:
  - "[[CSHP]]"
  - "[[EDUBILL]]"
chinh_dinh:
  - "Hệ thống / Quản trị NetWEB / Cấm SV xem vì nợ học phí – chặn SV còn nợ xem một số chức năng"
tu_khoa: "xem học phí|học phí|hóa đơn điện tử|hoá đơn|biên lai|miễn giảm|số tiền (đã|cần) đóng|summary"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NetWEB_SinhVienXemThongTinCaNhan"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Xem học phí, hóa đơn điện tử"
tags: [trang-web]
---
# Xem học phí, hóa đơn điện tử

**Vai trò:** Sinh viên, Phụ huynh · **Menu trên web:** Xem học phí · Hóa đơn điện tử · Tài liệu: [[HDSD NETWEB]] (`NetWEB_SinhVienXemThongTinCaNhan`)

## Trên web
SV xem theo từng học kỳ: tổng tiền cần đóng, đã đóng, % miễn giảm, chi tiết các khoản thu; tải hóa đơn điện tử ứng với biên lai thu học phí.

## Lấy dữ liệu từ Edusoft
- [[Hoc phi]]
- [[Phieu thu]]
- [[No hoc phi]]
- Học phí phải nộp / miễn giảm ở [[CSHP]]; phiếu thu, hóa đơn điện tử (biên lai) ở [[EDUBILL]]

## Ghi ngược về Edusoft
—

## Chỉnh định quyết định trang này
- Hệ thống / Quản trị NetWEB / Cấm SV xem vì nợ học phí – chặn SV còn nợ xem một số chức năng

## Kiểm tra liên kết khi test
- Thu tiền / hủy phiếu thu / đổi miễn giảm trên Edusoft → kiểm lại số "đã đóng", "còn nợ" trên web cùng học kỳ.
- SV còn nợ có thể bị chặn chức năng khác (Cấm SV xem vì nợ học phí, ĐKMH khi `xl_dk_neu_no_hp`).
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).

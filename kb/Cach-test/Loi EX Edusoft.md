---
loai: cach-test
ap_dung: lỗi EX (hộp lỗi hệ thống) trên màn hình Edusoft
test_tren: edusoft
nguon: tai-lieu
---
# Loi EX Edusoft

## Khi nào dùng
Case lỗi EX (hộp lỗi hệ thống) trên màn hình Edusoft.

## Chuẩn bị
Edusoft bản test có bản sửa, đúng menu ghi trong case; dữ liệu giống lúc lỗi (mã SV, nhóm học…) trên môi trường test.
## Các bước kiểm tra
1. Làm lại **đúng chuỗi thao tác** gây lỗi (case thường ghi: chọn … → bấm … → lỗi).
2. Không còn hộp lỗi; nếu còn: **Ctrl+Shift+E** hiện chi tiết lỗi → chụp kèm màn hình; **Ctrl+Shift+F** lấy menu code → ghi vào nội dung test lỗi.
3. Kiểm kết quả của thao tác (dữ liệu được lưu / tính đúng – mở lại màn hình).
## Kiểm tra không ảnh hưởng
Thao tác khác trên cùng màn hình (thêm / sửa / xóa / import) vẫn chạy; ví dụ lỗi cũ trong sheet: import đổi mã báo `Cannot perform '=' operation on System.Int32 and System.String` ở bước kiểm tra; thêm SV trùng mã + môn khác bị lặp 2 dòng; sau import/xóa lưới không tự nạp lại.

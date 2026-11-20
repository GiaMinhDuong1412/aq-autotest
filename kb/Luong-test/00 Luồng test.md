---
loai: huong-dan
---
# Luồng test theo nghiệp vụ

Mỗi ghi chú trong thư mục này = **một luồng thao tác thật** để test một chức năng (ai đăng nhập, làm gì, kết quả đúng là gì).
App (bước 2 Plan test) và Claude dùng luồng khớp với case để soạn plan **ngắn, đúng ngữ cảnh**, và **nhờ người dùng cung cấp tài khoản test**.

Properties:
- `dau_hieu`: regex nhận ra case (tiêu đề + lời KH), vd `điểm danh|quét mã|mã qr`.
- `can_cung_cap`: tài khoản / dữ liệu cần người dùng đưa, dạng `"Tên: vì sao"` (vd `Mã GV: …`, `MSSV: …`). **Chỉ mã tài khoản – không hỏi mật khẩu.**
- `buoc`: các bước, dùng `{Tên}` để chèn giá trị người dùng nhập (vd `{Mã GV}`).
- `khong_anh_huong`: 1–2 mục kiểm không ảnh hưởng đúng trọng tâm (không thêm mục chung chung).

Mục **Kiểm tra theo yêu cầu KH** luôn lấy từ chính case (mỗi ý KH một mục).

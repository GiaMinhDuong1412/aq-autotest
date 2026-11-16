# Lưu đồ CHÍNH SÁCH HỌC PHÍ (CSHP) – LuuDo_NEW/CSHP.pdf (bản mới nhất, 16/11/2026)

Khai báo (Chính sách HP/ Chính sách học phí/ Qui hoạch học phí/ …):
1. DM loại hình thu học phí (các khoản thu của trường) – `…/ DM loại hình thu học phí`.
2. DM công thức thu học phí – `…/ DM công thức thu`.
   (1) + (2) **kết hợp** →
3. Nhóm công thức thu (phiếu thu gồm các khoản phải thu) – `…/ ĐN nhóm công thức thu`.

Đầu vào tính học phí (đổ vào 12):
5. Mức đơn giá và số tín chỉ học phí (nhóm môn khác nhau → mức thu khác cho cùng số TC) – `…/ ĐN mức đơn giá và số TCHP môn học`.
61. Đơn giá học phí (số tiền / 1 đơn vị) – `…/ ĐN đơn giá học phí (danh sách)` hoặc `…/ ĐN đơn giá học phí`.
7. Đơn giá đặc biệt (mức thu riêng cho một số đối tượng) – `…/ ĐN đơn giá đặc biệt …`.
11. Các biến setting – `Chính sách HP/ Quản trị phân hệ/ Chỉnh định thông số học kỳ`.
4. Hình thức thu học phí (cách tính cho từng đối tượng) – `…/ ĐN hình thức thu theo đối tượng`.
8. Miễn giảm chính sách (SV hưởng chính sách) – `Chính sách HP/ Chính sách học phí/ Miễn giảm học phí/ Diện chính sách sinh viên học kỳ`.
9. Phụ thu (khoản thu/chi ngoài công thức) – `Chính sách HP/ Chính sách học phí/ Phụ thu học phí/ Phụ thu theo sinh viên`.
10. Kết quả ĐKMH – `Đăng ký MH/ Khai thác báo biểu/ Kết quả đăng ký/ Xem file MH đã đăng ký`.

Tính và thu:
12. **Tính học phí** – `Chính sách HP/ Tính và In học phí/ Tính học phí/ Tính …`.
13. → Danh sách SV nợ học phí.
14. **Thu học phí** (nhiều kênh) – thu trực tiếp `Thu/chi HP/ Hoạt động thu/chi/ Thu học phí/ Thu học phí 1 SV`;
    thu ngân hàng; import chuyển khoản `Thu/chi HP/ Hoạt động thu/chi/ Thu học phí/ Import phiếu thu`.
15. → Bảng kê thu chi học phí – `Thu/chi HP/ Khai thác báo biểu/ Thu/Chi học phí/ In bảng kê thu/chi học phí`.

Gợi ý kịch bản: tính HP (12) cần SV có kết quả ĐKMH (10) + đơn giá (5/61/7); kiểm tra: SV xuất hiện ở DS nợ (13) đúng số tiền,
thu 1 SV (14) xong thì hết nợ và có dòng trong bảng kê (15). Thu học phí là dữ liệu tiền – chỉ dùng SV test, có luồng hủy phiếu.

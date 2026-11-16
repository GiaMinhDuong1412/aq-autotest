# Lưu đồ nghiệp vụ Edusoft (bản mới nhất – LuuDo_NEW.zip người dùng gửi 16/11/2026)

Người dùng chốt: **dùng các lưu đồ PDF này**, KHÔNG dùng bản Visio `QuiTrinhMotTrangViSio/*.vsdx` trên SharePoint (cũ, có thể sai quy trình).
Mỗi PDF: trang 1 = ô + ghi chú nghiệp vụ, trang 2 = ô + **menu** từng bước (đã chép vào file từng phân hệ dưới đây).
Hình vẽ không có lớp chữ (trừ KSDG/QLTS) → đọc bằng cách render ảnh (`pdftoppm -r 95 -png`).

| File | Phân hệ |
|---|---|
| QLTS.md | Xét tuyển sinh + Tiếp sinh trúng tuyển |
| [../nghiep-vu/QLSV.md](../nghiep-vu/QLSV.md) | Quản lý sinh viên (lưu đồ ở đầu file) |
| CTDT.md | Chương trình đào tạo |
| QTKB.md | Xếp thời khóa biểu |
| DKMH.md | Đăng ký môn học offline / online |
| CSHP.md | Chính sách học phí, thu học phí |
| LTHI.md | Tổ chức thi |
| DIEM.md | Quản lý điểm |
| QXHV.md | Xét học vụ |
| QLTN.md | Xét tốt nghiệp |
| BVLV.md | Bảo vệ luận văn |
| KSDG.md | Khảo sát đánh giá |

## Chuỗi giữa các phân hệ (dữ liệu chảy theo thứ tự này – dùng để chọn điều kiện đầu vào của kịch bản)
```
Xét tuyển → DS trúng tuyển → Tiếp sinh ─┬─► QLSV (QĐ vào mới → DS SV học kỳ)
                                        └─► Thu/Chi HP (học phí nhập học)
CTĐT chuẩn → kế hoạch → thực hiện → Xếp TKB (nhóm học) ─┐
DS SV học kỳ ───────────────────────────────────────────┴─► Đăng ký môn học → KQ ĐKMH ─┬─► Chính sách HP (tính/thu HP)
                                                                                     ├─► Tổ chức thi (DS thi → lịch thi)
                                                                                     └─► Quản lý điểm (nhập → tính TB → phiếu điểm)
Điểm TB → Xét học vụ · Xét tốt nghiệp (→ QĐ tốt nghiệp ở QLSV) · Bảo vệ luận văn (→ chuyển điểm vào môn học)
Khảo sát đánh giá: dựa trên nhóm tổ / GV của học kỳ (TKB) – đáp viên đánh giá trên web.
```
Kịch bản một phân hệ cần dữ liệu có sẵn của phân hệ đứng trước (chỉ đọc / `pick:`), không tự tạo chuỗi dài – trừ kịch bản xuyên suốt
được người dùng yêu cầu.

## Đối chiếu menu lưu đồ ↔ danh mục màn hình HVNG (`web/edusoft-catalog.json`, 16/11/2026)
80/91 đường dẫn menu trên lưu đồ khớp danh mục. Lệch:
- Menu báo biểu (`Đăng ký MH/ Khai thác báo biểu/ …`, `Thu/chi HP/ Khai thác báo biểu/ …`, `Khảo sát đánh giá/ Khai thác báo biểu/ In kết quả`,
  `Sinh viên/ Danh sách sinh viên/ Hủy sinh viên trong DSSV học kỳ`, `…/ Danh mục phiên bản CTDT chuẩn`) không có trong danh mục
  (danh mục chỉ lập được menu nối với màn hình/lưới) – khi viết `menu:` dùng đúng chữ trên lưu đồ, kiểm lại bằng `ui-*.txt`.
- HVNG đặt tên khác:
  - Diện chính sách SV học kỳ → `Sinh viên/ Miễn giảm hoc phí và Học bổng/ Sinh viên diện chính sách/ Diện chính sách sinh viên học kỳ`.
  - Ghép danh sách thi lại → `Tổ chức thi/ Đăng ký thi lại & cải thiện/ Đăng ký thi lại & cải thiện`.
  - Dữ liệu bận giờ → `Kế hoạch/ Tài nguyên và ràng buộc/ Ràng buộc xếp TKB/ Quản lý dữ liệu {cán bộ|lớp|phòng} bận giờ`.

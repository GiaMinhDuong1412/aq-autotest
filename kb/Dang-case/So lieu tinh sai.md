---
loai: dang-case
ten: Số liệu / kết quả tính sai
dau_hieu_kh: "tính (sai|không đúng|chưa đúng)|sai số|số tiền|không khớp|chênh lệch|tổng|công thức|điểm trung bình|học phí.*sai|sai.*học phí|làm tròn|tích lũy"
dau_hieu_ba: "công thức|quy tắc tính|cách tính|nguyên nhân"
dau_hieu_dev: "store|procedure|sp_|công thức|tính|calc"
noi_hay_gap:
  - edusoft
  - web
phan_he_hay_gap:
  - "[[CSHP]]"
  - "[[DIEM]]"
  - "[[KLGD]]"
  - "[[QLTV]]"
  - "[[QXHV]]"
  - "[[QLTN]]"
  - "[[LTHI]]"
trang_thai: tu-tai-lieu
---
# Số liệu / kết quả tính sai

Kết quả một phép **tính / xét** ra sai: học phí, miễn giảm, điểm TB, tín chỉ tích lũy, khối lượng giảng dạy, xét học vụ / tốt nghiệp, công nợ.

## Nhận biết
- **Lời KH**: `tính (sai|không đúng|chưa đúng)|sai số|số tiền|không khớp|chênh lệch|tổng|công thức|điểm trung bình|học phí.*sai|sai.*học phí|làm tròn|tích lũy`
- **BA**: `công thức|quy tắc tính|cách tính|nguyên nhân`
- **Dev**: `store|procedure|sp_|công thức|tính|calc`
(biểu thức để app gợi ý dạng case – sửa ở Properties `dau_hieu_*`)

## Phải trả lời khi phân tích
- Tính ở đâu (menu Edusoft nào) – hiển thị ở đâu (Edusoft, web, mẫu in)
- Trường hợp cụ thể KH đưa: số đúng phải là bao nhiêu, vì sao (BA chốt quy tắc)
- Dữ liệu đầu vào của phép tính (xem `phai_co_truoc`) có đúng không – sai đầu vào thì không phải lỗi tính
- Sửa cách tính có phải **tính lại** dữ liệu cũ không?

## Case liên quan với dạng này là
Dữ liệu sinh ra **sau** phép tính (nợ học phí sau học phí, học vụ sau điểm TB…); cùng phép tính ở trường khác (dùng chung store).

## Hay nhầm
Hiển thị sai nhưng số trong Edusoft đúng → [[Hien thi web]].

## Phân hệ hay gặp
[[CSHP]], [[DIEM]], [[KLGD]], [[QLTV]], [[QXHV]], [[QLTN]], [[LTHI]]

## Case mẫu (tiêu đề từ danh sách ACS – cần đọc nội dung đầy đủ)
- 64501 (mẫu: tính học phí môn cải thiện)

Xem cách đọc case: [[00 Cách phân tích case]].

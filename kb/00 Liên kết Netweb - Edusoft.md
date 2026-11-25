---
loai: tong-quan
ten: Liên kết Netweb – Edusoft
tags: [tong-quan, netweb]
aliases:
  - "Liên kết Netweb"
  - "Netweb – Edusoft"
---
# Liên kết Netweb – Edusoft

> [!info] Nguyên tắc
> Netweb và Edusoft.NET dùng **chung 1 CSDL** (theo tài liệu Quản trị NetWEB). Sửa dữ liệu trên Edusoft là web đổi ngay – thứ duy nhất làm web "chưa đổi" là **cache** của Netweb.
> Ngược lại, nhiều trang web **ghi thẳng** về Edusoft (điểm GV nhập, KQ ĐKMH, lý lịch, điểm danh, nghỉ dạy). Riêng điểm rèn luyện phải bấm **Đồng bộ ĐRL online** mới vào Edusoft.

Mỗi trang web là một ghi chú trong `Web/` (Properties `du_lieu` = đọc, `ghi` = ghi ngược, `chinh_dinh` = biến / menu Edusoft quyết định trang, `tu_khoa` = nhận ra trong lời KH).
Kiểm tra liên kết trong KB: `python tools/kb_kiem_lien_ket.py kb`.

## Cache – vì sao sửa Edusoft mà web chưa đổi
- `Hệ thống / Quản trị NetWEB / Chỉnh định chung`: khai **`url_netweb` / BaseUrl** = link Netweb của trường → Edusoft tự gọi API clear cache khi đổi chỉnh định (từ bản 26/4/2022).
- Vẫn còn **3 biến** phải Clear cache tay ở trang quản trị (`/admin` → Quản lý App → Clear data App).
- Chỉnh định ĐKMH (thêm sĩ số, mở thêm nhóm…): SV phải **đăng xuất và đăng nhập lại** mới hiệu lực.
- Khi test: sửa trên Edusoft → đăng xuất / đăng nhập lại web (hoặc clear cache) **rồi** mới kết luận.

## Trang web theo vai trò
| Vai trò | Trang (ghi chú) | Đọc dữ liệu | Ghi về Edusoft |
|---|---|---|---|
| SV, GV | [[SV - Dang nhap va quen mat khau]] | [[Tai khoan va phan quyen]], email trong [[Danh muc sinh vien]] | mật khẩu |
| SV | [[SV - Xem chuong trinh dao tao]] | [[CTDT]], [[Mon hoc]] | — |
| SV, PH | [[SV - Xem hoc phi va hoa don]] | [[Hoc phi]], [[Phieu thu]], [[No hoc phi]] | — |
| SV, GV | [[SV GV - Xem thoi khoa bieu]] | [[Thoi khoa bieu]], [[Nhom hoc]], [[KQ DKMH]] | — |
| SV, GV | [[SV GV - Xem lich thi]] | [[Danh sach thi]] | — |
| SV, PH | [[SV - Xem diem]] | [[Diem mon hoc]], [[Diem trung binh]] | — |
| SV | [[SV - Xem ket qua xet tot nghiep]] | [[Ket qua tot nghiep]] | — |
| SV | [[SV - Dang ky mon hoc]] | [[Rang buoc DKMH]], [[Nhom hoc]], [[CTDT]], [[No hoc phi]] | [[KQ DKMH]] |
| SV | [[SV - Cap nhat ly lich]] | [[Danh muc sinh vien]] | [[Danh muc sinh vien]] |
| SV, GV | [[SV GV - Danh gia ren luyen]] | [[Diem ren luyen]] | [[Diem ren luyen]] (sau Đồng bộ ĐRL online) |
| SV, khách | [[SV - Dang ky cap giay chung nhan]] | [[Danh muc sinh vien]] | [[Don tu truc tuyen]] |
| SV, GV | [[SV GV - Thong bao va gop y]] | [[Cau hinh NetWEB]] | — |
| GV | [[GV - Nhap diem online]] | [[Nhom hoc]], [[Danh sach thi]] | [[Diem mon hoc]] |
| GV | [[GV - Duyet ket qua dang ky]] | [[KQ DKMH]] | [[KQ DKMH]] |
| GV | [[GV - Xem diem va sinh vien quan ly]] | [[Diem mon hoc]], [[Lop sinh vien]] | — |
| GV | [[GV - Diem danh]] | [[Thoi khoa bieu]] | [[Diem danh]] |
| GV | [[GV - Dang ky nghi day va day bu]] | [[Thoi khoa bieu]], [[Phong hoc]] | [[Thoi khoa bieu]] |
| PH | [[PH - Phu huynh]] | [[Danh muc sinh vien]] | — |
| Quản trị | [[Admin - Trang quan tri Netweb]] | [[Cau hinh NetWEB]] | [[Cau hinh NetWEB]], [[Tai khoan va phan quyen]] |

## Biến chỉnh định Edusoft → trang web
| Biến / menu Edusoft | Trang web chịu ảnh hưởng |
|---|---|
| `url_netweb` / BaseUrl (Chỉnh định chung NetWEB) | mọi trang – tự clear cache |
| Chỉnh định menu (Quản trị NetWEB) | ẩn / hiện menu web |
| Cấm SV xem vì nợ học phí · Cấm SV xem khi chưa nhập đủ thông tin SV | các menu SV bị chặn |
| `hk_cho_phep_nhap_diem` + phân công / gán thời gian / khóa điểm | [[GV - Nhap diem online]] |
| `xl_so_ngay_gv_duyet_sau_ngay_svdk`, `xl_cho_cvht_dk` | [[GV - Duyet ket qua dang ky]] |
| Thời gian đăng ký (lớp / SV / lớp – giờ), `xl_nghiep_vu_dang_ky`, `xl_dk_neu_no_hp`, `xl_xet_tien_quyet`… | [[SV - Dang ky mon hoc]] |
| `nhhk_danh_gia_ren_luyen`, thời gian đánh giá online, `GS_BOXHDIEMRL` | [[SV GV - Danh gia ren luyen]] |
| Thời gian cập nhật / chỉnh định thông tin lý lịch SV trên Web | [[SV - Cap nhat ly lich]] |
| `nhhk_dk_giay_chung_nhan`, danh mục giấy chứng nhận (hiển thị web, in trực tuyến) | [[SV - Dang ky cap giay chung nhan]] |
| Danh sách đợt xét (TN) – công bố kết quả | [[SV - Xem ket qua xet tot nghiep]] |
| `GH_MAILSERVER` | quên mật khẩu, góp ý, đơn từ |

## Kiểm tra liên kết khi test case
1. **Case sửa ở Edusoft** (dữ liệu / chỉnh định): tìm dữ liệu trong bảng trên → mở trang web đọc dữ liệu đó → đăng xuất / đăng nhập lại → kiểm hiển thị đúng **đúng vai trò** (SV, GV, phụ huynh).
2. **Case sửa trang web**: kiểm chỉnh định của trang (mục "Chỉnh định quyết định trang này") trước khi kết luận lỗi; trang có `ghi` → lưu trên web rồi kiểm ngược menu Edusoft.
3. **Thời gian / NHHK** là nguyên nhân hay gặp nhất của "web không cho nhập": kiểm biến NHHK + thời gian của vai trò đó.
4. Case "web hiển thị sai" mà Edusoft đúng → nghi cache trước, rồi mới nghi code web ([[Hien thi web]]).

## Tài liệu chưa đọc vào KB
Khảo sát đánh giá (SV, GV), Điểm danh bằng QR (chi tiết SV), Khách tra cứu luận văn / văn bằng, Chăm sóc thí sinh xét tuyển, Lưu học sinh, Nhập học online – xem [[HDSD NETWEB]], [[HDSD NhapHocOnline]].

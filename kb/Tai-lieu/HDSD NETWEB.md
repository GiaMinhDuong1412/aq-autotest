---
loai: tai-lieu
ten: "Hướng dẫn sử dụng NETWEB"
nguon_loai: hdsd
phan_he:
  - "[[NETWEB-UI]]"
  - "[[NETWEB-API]]"
du_lieu:
  - "[[Cau hinh NetWEB]]"
  - "[[Diem danh]]"
  - "[[KQ DKMH]]"
  - "[[Diem mon hoc]]"
  - "[[Ket qua khao sat]]"
  - "[[Vien chuc]]"
  - "[[Thoi khoa bieu]]"
  - "[[Diem ren luyen]]"
  - "[[Danh muc sinh vien]]"
  - "[[Tai khoan va phan quyen]]"
  - "[[Ket qua tot nghiep]]"
  - "[[Ho so thi sinh]]"
noi_luu: "SharePoint AQ › Shared Documents › 1. Tài liệu EduSoft › DOC › NETWEB"
so_file: 19
do_tin_cay: tai-lieu-chinh-thuc
tags: [tai-lieu, hdsd]
---

# Hướng dẫn sử dụng – NETWEB

> [!info] Nơi lưu
> SharePoint AQ › Shared Documents › 1. Tài liệu EduSoft › DOC › **NETWEB** (bản PDF cùng tên ở thư mục `PDF/NETWEB`). Mở bằng SharePoint / công cụ Microsoft 365 của Claude.

Phân hệ: [[NETWEB-UI]], [[NETWEB-API]]

## Tài liệu trong thư mục
| File | Nội dung – điều cần nhớ khi đọc case | Dữ liệu KB |
|---|---|---|
| `NETWEB_QuanTriChung.docx` | Quản trị NetWEB chung (Chỉnh định chung, cấu hình hiển thị, học kỳ web) | [[Cau hinh NetWEB]] |
| `NetWEB_DiemDanhBangQr.doc` | Điểm danh bằng mã QR (GV hiện mã, SV quét) – xem [[Diem danh QR]] | [[Diem danh]] |
| `NetWEB_GiangVienDiemDanhSVTrucTuyen.doc` | GV điểm danh SV trực tuyến | [[Diem danh]] |
| `NetWEB_GiangVienDuyetKQDK.doc` | CVHT / GV duyệt kết quả đăng ký | [[KQ DKMH]] |
| `NetWEB_GiangVienNhapDiemOnline.doc` | GV nhập điểm online | [[Diem mon hoc]] |
| `NetWEB_GiangVienXemKhaoSatDanhGia.doc` | GV xem kết quả khảo sát | [[Ket qua khao sat]] |
| `NetWEB_GiangVienXemThongTinCaNhan.doc` | GV xem thông tin cá nhân, lịch dạy | [[Vien chuc]] |
| `NETWEB_HuongDanDangKyNghiDay_DayBuOnline.docx` | GV đăng ký nghỉ dạy / dạy bù | [[Thoi khoa bieu]] |
| `NetWEB_NhapDRLTrucTuyen.doc` | Nhập điểm rèn luyện trực tuyến (SV tự đánh giá, GV/CVHT duyệt) | [[Diem ren luyen]] |
| `NetWEB_NhapLyLichSVTrucTuyen.doc` | SV nhập lý lịch trực tuyến | [[Danh muc sinh vien]] |
| `NetWEB_PhuHuynh.doc` | Trang phụ huynh | — |
| `NETWEB_QuanLyDonTuTrucTuyen.doc` | Đơn từ trực tuyến | — |
| `NetWEB_QuanlyLuuHocSinh_NEW.doc` | Lưu học sinh | — |
| `NetWEB_SinhVienKhaoSatDanhGia.doc` | SV làm khảo sát đánh giá | [[Ket qua khao sat]] |
| `NETWEB_SinhVienQuenMatKhau.doc` | SV quên mật khẩu | [[Tai khoan va phan quyen]] |
| `NetWEB_SinhVienXemThongTinCaNhan.doc` | SV xem thông tin cá nhân (TKB, điểm, học phí…) | — |
| `NETWEB_XemKetQuaXetTotNghiep.docx` | Xem kết quả xét tốt nghiệp | [[Ket qua tot nghiep]] |
| `NETWEB_ChamSocThiSinhXetTuyen.docx` | Chăm sóc thí sinh xét tuyển | [[Ho so thi sinh]] |
| `NetWEB_Guest_TraCuuLuanVan_VanBangChungChi.doc` | Khách tra cứu luận văn, văn bằng | — |

## Bộ tài liệu triển khai (PDF)
SharePoint **sp** › Shared Documents › ALL DOCS › TaiLieuTrienKhai_EduSoft.NET › **NetWeb**: bản PDF dùng khi triển khai cho trường –
`NETWEB-QuanTriChung`, `NetWEB_SinhVienXemThongTinCaNhan`, `NetWEB_GiangVienXemThongTinCaNhan`, `NetWEB_GiangVienNhapDiemOnline`,
`NetWEB_GiangVienDuyetKQDK`, `NetWEB_NhapDRLTrucTuyen`, `NetWEB_NhapLyLichSVTrucTuyen` và **`DKMH_HuongDanDangKyMonHocOnline_chinhthuc`**
(quy trình tổ chức đợt ĐKMH online: thời gian 3 cấp, ràng buộc `xl_…`, cache, khuyến nghị cấu hình server – chịu ~3000 truy cập đồng thời, ≤1500 SV/ngày).

## Đã đọc vào KB (25/11)
Từng trang web: `Web/` – tổng hợp ở [[00 Liên kết Netweb - Edusoft]] (dữ liệu đọc / ghi, biến chỉnh định Edusoft, cache, cách kiểm liên kết).

## Dùng khi nào
- Đọc case có tên menu / chức năng trong bảng trên → mở đúng tài liệu để biết **cách làm chuẩn** và các **biến chỉnh định** liên quan.
- Soạn plan test: lấy bước thao tác + điều kiện (menu, biến setting) từ tài liệu, không đoán.
- Tài liệu viết theo bản chung – trường có bản riêng (VersionSchool) có thể khác: đối chiếu thêm case cũ của trường ([[00 Mô hình trường]]).

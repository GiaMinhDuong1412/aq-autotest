---
loai: tai-lieu
ten: "Hướng dẫn sử dụng DKMH"
nguon_loai: hdsd
phan_he:
  - "[[DKMH]]"
  - "[[DKMHUI]]"
du_lieu:
  - "[[Rang buoc DKMH]]"
  - "[[KQ DKMH]]"
  - "[[Mon hoc]]"
noi_luu: "SharePoint AQ › Shared Documents › 1. Tài liệu EduSoft › DOC › DKMH"
so_file: 6
do_tin_cay: tai-lieu-chinh-thuc
tags: [tai-lieu, hdsd]
---

# Hướng dẫn sử dụng – DKMH

> [!info] Nơi lưu
> SharePoint AQ › Shared Documents › 1. Tài liệu EduSoft › DOC › **DKMH** (bản PDF cùng tên ở thư mục `PDF/DKMH`). Mở bằng SharePoint / công cụ Microsoft 365 của Claude.

Phân hệ: [[DKMH]], [[DKMHUI]]

## Tài liệu trong thư mục
| File | Nội dung – điều cần nhớ khi đọc case | Dữ liệu KB |
|---|---|---|
| `DKMH_ChinhDinhThoiGianDangKyOnline.docx` | Chỉnh định thời gian ĐKMH online: biến SM00_CAMDKTT_DIEN (cấm ĐK online = Không), SM00_TGCPDK (giới hạn thời gian – Edusoft.Web, biến theo học kỳ), GH_THOIGIANDKTRONGNGAYEDUWEB (giờ trong ngày), menu Chỉnh định thời gian đăng ký theo đối tượng; **phải restart IIS** để áp dụng | [[Rang buoc DKMH]] |
| `DKMH_DangKyMonHocOFFLINE.docx` | Đăng ký offline (phòng đào tạo đăng ký thay: tự động / theo lớp / từng SV) | [[KQ DKMH]] |
| `DKMH_DangKyMonHocTuFileSV-MH.docx` | Đăng ký môn học từ file Excel SV – MH | [[KQ DKMH]] |
| `DKMH_DinhNghiaMonTienQuyet.docx` | Định nghĩa môn tiên quyết / học trước / song hành | [[Rang buoc DKMH]], [[Mon hoc]] |
| `DKMH_HuongDanDangKyMonHocOnline.doc` | SV đăng ký môn học online trên web | [[KQ DKMH]] |
| `DKMH_RutMonHoc.doc` | Rút môn học (thời gian rút theo lớp, SV rút online) | [[KQ DKMH]] |

## Dùng khi nào
- Đọc case có tên menu / chức năng trong bảng trên → mở đúng tài liệu để biết **cách làm chuẩn** và các **biến chỉnh định** liên quan.
- Soạn plan test: lấy bước thao tác + điều kiện (menu, biến setting) từ tài liệu, không đoán.
- Tài liệu viết theo bản chung – trường có bản riêng (VersionSchool) có thể khác: đối chiếu thêm case cũ của trường ([[00 Mô hình trường]]).

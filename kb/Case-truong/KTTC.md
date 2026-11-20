---
loai: case-truong
ma: KTTC
truong: "[[KTTC]]"
tong_case: 2
tu_ngay: 
den_ngay: 
phan_cap:
  - "KTTC (2)"
phan_he_nhieu:
  - "NETWEB-UI (1)"
  - "CSHP (1)"
dang_nhieu:
  - "Hien thi web (1)"
du_lieu_nhieu:
  - "Diem danh (1)"
  - "Dien chinh sach (1)"
  - "Hoc phi (1)"
cap_nhat: 2026-11-20
nguon: seed (case đã gặp – chạy Học case để cập nhật)
tags: [case-truong]
---

# KTTC – mô hình trường từ case ACS

Trường: [[KTTC]] – ĐH Kinh tế - Tài chính TP.HCM · quy trình: [[00 Quy trình xuyên phân hệ]] · cách đọc case: [[00 Cách phân tích case]]

## Nhận xét – mô hình trường (người test / Claude viết, công cụ không ghi đè)
- **Khởi tạo từ các case đã gặp khi làm việc (20/11/2026)** – bấm *Học case → KB* trong app (hoặc nhờ Claude `truong_hoc_case KTTC`) để lấy đủ lịch sử case.
- Có **bản riêng**: Dev sửa ở `VersionSchool/KTTC/…` → test trên bản / web test của chính KTTC (bản sửa ghi trong ghi chú Dev, vd 2026.11J.20).
- Trường hay yêu cầu chỉnh **hiển thị trên web** (học phí – miễn giảm, điểm danh): case dạng [[Hien thi web]] → test trên web theo vai trò (SV / GV), đối chiếu số liệu Edusoft trước.
- Có chuỗi case tiếp nối về **hiển thị miễn giảm học phí** (#64184 → #64457 "lần 2") – đọc case gốc trước, kiểm lại điều lần 1 đã sửa ([[05 Hoc phi - thu - thanh toan]]).
- Điểm danh QR trên web: ô ghi chú sau khi SV quét mã phải còn sửa được (#64755) – luồng [[Diem danh QR]].

<!-- tu-dong:bat-dau – phần dưới do công cụ truong_hoc_case ghi lại mỗi lần học case, đừng sửa tay -->
## Tổng quan (2 case)
| Phân hệ | Số case | Quy trình | Dạng hay gặp | Case gần nhất |
|---|---|---|---|---|
| [[NETWEB-UI]] | 1 | [[09 Hoat dong tren lop]] | — | #64755 |
| [[CSHP]] | 1 | [[05 Hoc phi - thu - thanh toan]] | [[Hien thi web]] (1) | #64457 |

**Dữ liệu hay đụng tới:** [[Diem danh]] (1), [[Dien chinh sach]] (1), [[Hoc phi]] (1)

**Case tiếp nối** (case gốc → case sau): #64184 → #64457

## Danh sách case (mới nhất trước, tối đa 150)
| Case | Ngày | Phân cấp | Phân hệ | Tiêu đề | Dạng | Trạng thái | Test |
|---|---|---|---|---|---|---|---|
| #64755 |  | KTTC | NETWEB-UI | Hiệu chỉnh có thể nhập ghi chú khi sinh viên quét mã điểm danh | — | Đã xử lý |  |
| #64457 |  | KTTC | CSHP | [64184]: Hiển thị miễn giảm học phí - lần 2 | [[Hien thi web]] | Đã xử lý |  |

📝 = đã có phiếu phân tích trong app (MCP `case_doc_phan_tich`). Tiêu đề đã che email / số điện thoại / mã ≥ 7 số / tên sau SV, GV.
<!-- tu-dong:het -->

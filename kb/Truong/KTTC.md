---
loai: truong
ma: KTTC
ten: ĐH Kinh tế - Tài chính TP.HCM
netweb_that: 
web_test: 
edusoft_test: 
trang_thai_hd: Chưa nghiệm thu NetWeb (2021)
phan_cap: []
nguon: sheet-release
trang_thai: can-xac-nhan
aliases:
  - "ĐH Kinh tế - Tài chính TP.HCM"
---
# KTTC – ĐH Kinh tế - Tài chính TP.HCM

## Netweb của trường
- Trang thật (KH dùng): (chưa có trong sheet) – **chỉ để nhận ra trường trong case, KHÔNG thử / ghi dữ liệu trên trang thật.**
- Web test: (điền) · Edusoft test: (điền)

## Chức năng web trường có (sheet ChuyenDoiNetWeb, 2021 – có thể đã đổi)
- DKMH online
- Khảo sát trực tuyến
- SV xem học phí
- SV xem CTĐT
- Kết quả xét tốt nghiệp (web)
- SV xin bảng điểm online

## Ghi chú
Có phiên bản riêng – coder sửa ở `VersionSchool/KTTC/…` (xem [[VersionSchool]]).


## Mô hình trường (từ case ACS)
[[Case-truong/KTTC|2 case]] – phân hệ hay có case: NETWEB-UI (1), CSHP (1); dạng hay gặp: Hien thi web (1).
## Khi đọc case của trường này
- Mã trường trên ACS: **`KTTC`** (4 ký tự) = case chung của trường. Mã **dài hơn 4 ký tự** bắt đầu bằng `KTTC` = **phân cấp** (đơn vị phân cấp: hệ / cơ sở) của trường.
- Case làm theo phân cấp thì **chỉ có hiệu lực trên phân cấp đó**: test trên đúng phân cấp (site / dữ liệu của phân cấp), phân cấp khác của cùng trường thường không bị ảnh hưởng – trừ khi sửa phần chung của trường.
- Gặp mã phân cấp mới → thêm vào `phan_cap` (dạng `"MÃ: tên phân cấp"`).
- Coder sửa `VersionSchool/KTTC/…` = bản riêng của trường → kiểm tra trên bản / trang test của chính trường này.
- Case cùng trường (cùng phân cấp) gửi gần nhau thường cùng đợt / cùng bản sửa → xem chung (MCP `acs_case_lien_quan`).

---
Nguồn: sheet Release(TestMenu) – ChuyenDoiNetWeb, Port NetWEB. Trạng thái hợp đồng ghi theo sheet: Chưa nghiệm thu NetWeb (2021).

---
loai: truong
ma: DHNT
ten: ĐH Ngoại Thương
netweb_that: http://ftugate.ftu.edu.vn/#/home
web_test: 
edusoft_test: 
trang_thai_hd: Actived
ma_acs:
  - DHNT
  - DHNTDHCQ
  - DHNTCHCQ
  - DHNTDHTC
  - DHNTNTC2
nguon: sheet-release
trang_thai: can-xac-nhan
---
# DHNT – ĐH Ngoại Thương

## Netweb của trường
- Trang thật (KH dùng): `http://ftugate.ftu.edu.vn/#/home` – **chỉ để nhận ra trường trong case, KHÔNG thử / ghi dữ liệu trên trang thật.**
- Web test: (điền) · Edusoft test: (điền)

## Chức năng web trường có (sheet ChuyenDoiNetWeb, 2021 – có thể đã đổi)
- DKMH online
- Đóng học phí trực tuyến
- SV xem học phí
- SV xem CTĐT
- Kết quả xét tốt nghiệp (web)
- CVHT duyệt ĐKMH
- GV nhập điểm online
- Nhập lý lịch SV online
- Đánh giá GV trước khi xem điểm

## Nhiều hệ / cơ sở – điều hướng theo đơn vị phân cấp (DVPC)
Mã trên ACS: `DHNTDHCQ` (ĐH chính quy – ftugate.ftu.edu.vn), `DHNTCHCQ` (cao học – qlsdh.ftu.edu.vn), `DHNTDHTC` (tại chức – dttt.ftu.edu.vn),
`DHNTNTC2` (cơ sở 2 – qldt.cs2.ftu.edu.vn).
Điều hướng (sheet "DHNT Điều hướng DVPC"): đăng nhập ở trang chính rồi **chuyển sang site theo cơ sở** của SV / GV / khối lớp
– DHNTDHCQ: Hà Nội / Quảng Ninh; DHNTDHTC: Feretco / Trực tuyến. Bảng thử có cột "Login / Logout có chuyển đúng không (Y/N)" cho SV và GV.
Bản thử trên máy chủ `http://edusoft.net.vn:12344/<site>` (vd `dhntdhcq.netweb`, `dhntdhcq.hanoi`, `dhntdhtc.feretco`) – **cần xác nhận** đây có phải môi trường test hiện tại.

## Ghi chú
—


## Khi đọc case của trường này
- Mã trên ACS: `DHNT`, `DHNTDHCQ`, `DHNTCHCQ`, `DHNTDHTC`, `DHNTNTC2` (school_code). Mã khác chưa có ở đây → ghi thêm vào `ma_acs` khi đã xác nhận.
- Coder sửa `VersionSchool/DHNT/…` = bản riêng của trường → kiểm tra trên bản / trang test của chính trường này.
- Chức năng web trường có (mục trên) quyết định case web có thuộc chức năng trường dùng không.
- Case cùng trường gửi gần nhau thường cùng đợt / cùng bản sửa → xem chung (MCP `acs_case_lien_quan`).

---
Nguồn: sheet Release(TestMenu) – ChuyenDoiNetWeb, Port NetWEB, DHNT Điều hướng DVPC. Trạng thái hợp đồng ghi theo sheet: Actived.

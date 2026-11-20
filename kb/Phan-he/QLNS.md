---
loai: phan-he
ma: QLNS
ten: Quản lý nhân sự
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
tab_edusoft: Nhân sự
nhan_tu: []
dua_sang:
  - "[[KHGD]]"
  - "[[KLGD]]"
  - "[[KSDG]]"
  - "[[LTHI]]"
dau_hieu: lý lịch CBCNV, quyết định, hợp đồng, học hàm học vị, khen thưởng, nghỉ phép
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Quản lý nhân sự"
quy_trinh:
  - "[[03 CTDT - TKB]]"
  - "[[06 To chuc thi]]"
  - "[[10 Nhan su - khoi luong giang day]]"
tags: [phan-he]
---
# QLNS – Quản lý nhân sự

## Là gì
Lý lịch CBCNV, quyết định vào/ra, tuyển dụng – hợp đồng, học hàm học vị, văn bằng chứng chỉ, công tác – phép, bảo hiểm, khen thưởng kỷ luật.

## Nhận dữ liệu từ
—

## Tạo ra
- [[Vien chuc|Viên chức / cán bộ giảng dạy]]

## Đưa sang
- [[Vien chuc|Viên chức / cán bộ giảng dạy]] → [[KHGD]], [[KLGD]], [[KSDG]], [[LTHI]]

## Sửa ở đây → kiểm lại
Các phân hệ nhận dữ liệu của QLNS: [[KHGD]], [[KLGD]], [[KSDG]], [[LTHI]].

## Phần trên Edusoft
Tab **Nhân sự**.
Menu: [[Menu/QLNS|169 menu của QLNS]] – menu tạo dữ liệu: [[Menu/Danh sách viên chức học kỳ (N02)|Danh sách viên chức học kỳ]].

## Phần trên web / app
GV xem thông tin cá nhân; CBCNV đăng ký nghỉ phép, nhập lý lịch khoa học trực tuyến (tuỳ trường).


## Dạng case thường gặp
(chưa ghi – thêm khi gặp)
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: edusoft / web – xem KH nói về màn hình Edusoft hay trang web.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được QLNS phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]]
2. **QLNS** – [[Vien chuc|Viên chức / cán bộ giảng dạy]]

**Sửa dữ liệu của QLNS → kiểm lại:** phân hệ dùng trực tiếp [[KHGD]], [[KLGD]], [[KSDG]], [[LTHI]]; dữ liệu sinh ra từ đó (theo thứ tự): [[Diem luan van|Điểm luận văn]] (BVLV), [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]] (KHGD), [[Ket qua khao sat|Kết quả khảo sát]] (KSDG), [[Thoi khoa bieu|Thời khóa biểu]] (KHGD), [[KQ DKMH|Kết quả đăng ký môn học]] (DKMH), [[Khoi luong giang day|Khối lượng giảng dạy]] (KLGD), [[Danh sach thi|Danh sách thi – lịch thi]] (LTHI), [[Diem danh|Điểm danh (chuyên cần)]] (NETWEB-UI), [[Hoc phi|Học phí phải thu (đã tính)]] (CSHP), [[Diem mon hoc|Điểm môn học]] (DIEM), [[Phieu thu|Phiếu thu học phí]] (QLTV), [[Diem trung binh|Điểm trung bình – tích lũy]] (DIEM), [[No hoc phi|Nợ học phí]] (CSHP), [[Ket qua hoc vu|Kết quả xét học vụ]] (QXHV), [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]] (QLTN).

## Nằm trong quy trình
- [[03 CTDT - TKB|Chương trình đào tạo → nhóm học → thời khoá biểu]]
- [[06 To chuc thi|Tổ chức thi]]
- [[10 Nhan su - khoi luong giang day|Nhân sự → phân công giảng dạy → khối lượng giảng dạy]]

## Tài liệu
- [[HDSD QLNS]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
—

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.

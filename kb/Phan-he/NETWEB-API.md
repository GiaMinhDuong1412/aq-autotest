---
loai: phan-he
ma: NETWEB-API
ten: API của Netweb
san_pham: "[[Netweb]]"
test_tren:
  - web
  - api
tab_edusoft: —
dau_hieu: request, API, đăng nhập, bảo mật 2 lớp, token, rút môn online, gọi từ CVHT, edusoft-api
nguon: tai-lieu
trang_thai: tu-tai-lieu
---
# NETWEB-API – API của Netweb

## Là gì
Phần xử lý phía máy chủ của Netweb (vd `https://edusoft-api.<trường>/…`): đăng nhập, phân quyền, nghiệp vụ web (rút môn, CVHT duyệt…).

## Phần trên Edusoft
Dữ liệu gốc nằm ở Edusoft – kiểm lại kết quả ghi xuống (vd KQ ĐKMH sau khi rút môn).

## Phần trên web / app
Test **qua trang web** (thao tác đúng chức năng KH nêu) + kiểm dữ liệu trên Edusoft; case bảo mật thì thử cả trường hợp sai (sai mật khẩu, hết phiên…).

## Test ở đâu
Tuỳ case: web / api – xem lời KH nói về màn hình Edusoft hay trang web (bảng trên).

## Lưu ý khi test
Case [[64677]], [[64678]], [[62219]].

---
Nguồn: Tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW, sheet Release(TestMenu) – Menu_NEW. Mã ACS ↔ phân hệ tài liệu là suy ra – người test xác nhận rồi đổi `trang_thai: da-xac-nhan`.

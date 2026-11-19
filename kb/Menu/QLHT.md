---
loai: danh-sach-menu
phan_he: "[[QLHT]]"
so_menu: 75
nguon: danh-muc-menu
---
# Menu QLHT – Quản lý hệ thống

75 menu Edusoft (từ `web/edusoft-catalog.json`). Tên **có liên kết** = menu **tạo** dữ liệu (có ghi chú riêng); → [[…]] = dữ liệu menu đó đụng tới.
Phân hệ: [[QLHT]].

## An toàn dữ liệu
- [[Menu/Khóa sổ phân hệ theo học kỳ (H2.3)|Khóa sổ phân hệ theo học kỳ]] `H2.3` → [[Hoc ky]]
- Lưu vết hiệu chỉnh report <small>(Lưu vết dữ liệu)</small> `H77`
- Lưu vết thao tác dữ liệu <small>(Lưu vết dữ liệu)</small> `H21`
- Nhật ký view trả về mặc định <small>(Lưu vết dữ liệu)</small> `H79`
- Nhật ký đăng nhập <small>(Lưu vết dữ liệu)</small> `H71` → [[Tai khoan va phan quyen]]
- Thống kê nhập dữ liệu sinh viên <small>(Lưu vết dữ liệu)</small> `H78`

## Quản lý người dùng
- Phân quyền quản lý bảng điểm & giấy CN <small>(Phân quyền khai thác)</small> `H69` → [[Tai khoan va phan quyen]]
- Phân quyền quản trị phân hệ <small>(Phân quyền khai thác)</small> `H61_A` → [[Tai khoan va phan quyen]]
- Phân quyền quản trị phân hệ <small>(Phân quyền khai thác)</small> `H61` → [[Tai khoan va phan quyen]]
- [[Menu/Phân quyền theo chức năng (H62)|Phân quyền theo chức năng]] <small>(Phân quyền khai thác)</small> `H62` → [[Tai khoan va phan quyen]]
- [[Menu/Phân quyền theo người dùng (H67)|Phân quyền theo người dùng]] <small>(Phân quyền khai thác)</small> `H67` → [[Tai khoan va phan quyen]]
- Phân quyền user theo bậc hệ <small>(Phân quyền khai thác)</small> `H61.00` → [[Tai khoan va phan quyen]], [[Danh muc dao tao]]
- Phân quyền user theo giấy chứng nhận <small>(Phân quyền khai thác)</small> `H70` → [[Tai khoan va phan quyen]]
- Phân quyền user theo đơn vị phân cấp <small>(Phân quyền khai thác)</small> `H70A` → [[Tai khoan va phan quyen]]
- Ủy quyền quản trị phân hệ <small>(Phân quyền khai thác)</small> `H68` → [[Tai khoan va phan quyen]]
- Danh sách tài khoản & nhóm tài khoản <small>(Quản lý người dùng.)</small> `H01` → [[Tai khoan va phan quyen]]
- Liên kết tài khoản Net và viên chức <small>(Quản lý người dùng.)</small> `H03` → [[Tai khoan va phan quyen]], [[Vien chuc]]
- Ủy quyền user chỉnh định biến <small>(Quản lý người dùng.)</small> `H04` → [[Tai khoan va phan quyen]]
- Định nghĩa file được xóa `H60(1)` → [[Tai khoan va phan quyen]]

## Quản trị EduWEB
- Cấm sinh viên xem thông tin vì nợ học phí `H99.3` → [[No hoc phi]]
- Danh sách sinh viên cập nhật hồ sơ `H100.7`
- Gửi mail thời gian ĐKMH SV `H99.4` → [[KQ DKMH]]
- Tạo đối tượng giảng viên thông báo <small>(Nội dung thông báo)</small> `H100.2.3` → [[Vien chuc]]
- Tạo đối tượng sinh viên thông báo <small>(Nội dung thông báo)</small> `H100.2.2`
- Định nghĩa nội dung thông báo <small>(Nội dung thông báo)</small> `H100.2.1`
- Danh sách hỗ trợ online <small>(Quản lý trang chủ)</small> `H99.6`
- Danh sách web liên kết <small>(Quản lý trang chủ)</small> `H99.5`
- Sắp xếp trang chủ <small>(Quản lý trang chủ)</small> `H99.7`
- Ẩn menu web <small>(Quản lý trang chủ)</small> `H99.9`

## Quản trị NetWEB
- [[Menu/Chỉnh định chung (H101.3)|Chỉnh định chung]] `H101.3` → [[Cau hinh NetWEB]]
- [[Menu/Chỉnh định menu (H101.1)|Chỉnh định menu]] `H101.1` → [[Cau hinh NetWEB]]
- Cấm SV xem khi chưa nhập đủ thông tin SV `H101.5` → [[Cau hinh NetWEB]]
- Cấm SV xem menu theo DSSV `H99.8` → [[Cau hinh NetWEB]]
- [[Menu/Cấm SV xem vì nợ học phí (H101.4)|Cấm SV xem vì nợ học phí]] `H101.4` → [[Cau hinh NetWEB]], [[No hoc phi]]
- Yêu cầu SV xác nhận năm học mới `H101.6` → [[Cau hinh NetWEB]]
- Đồng bộ thông tin người dùng `H101.2` → [[Tai khoan va phan quyen]], [[Cau hinh NetWEB]]

## Quản trị hệ thống
- Báo biểu chung <small>(Chỉnh định báo biểu hệ thống)</small> `H56.02`
- tên báo biểu <small>(Chỉnh định báo biểu hệ thống / Mã)</small> `H55.04`
- Mẫu in mặc định theo user <small>(Chỉnh định báo biểu hệ thống)</small> `H55.06`
- Phòng ban quản lý phân hệ <small>(Chỉnh định báo biểu hệ thống)</small> `H55.05`
- Giao diện chung <small>(Chỉnh định giao diện hệ thống)</small> `H56.01`
- tên giao diện <small>(Chỉnh định giao diện hệ thống / Mã)</small> `H54`
- Chỉnh định thông số hệ thống `H51`
- Chỉnh định thông tin cột `H56.03`
- Chỉnh định thông tin đơn vị `H58`
- Tính học phí <small>(Chỉnh định tiến trình tự động)</small> `H57.02`
- Tính điểm trung bình <small>(Chỉnh định tiến trình tự động)</small> `H57.01`
- Upload EduWeb tự động <small>(Chỉnh định tiến trình tự động)</small> `D57.03`
- Chỉnh định từ khóa sử dụng `H42`
- Chỉnh định định dạng hệ thống `H59`
- Gán số đếm bắt đầu `H56.04`
- Gửi email đến sinh viên <small>(Gửi Email đến sinh viên)</small> `H5.1.2`

## Thông tin học kỳ
- Bổ sung dữ liệu học kỳ `H33` → [[Hoc ky]]
- Danh mục chương trình học `H30` → [[Hoc ky]]
- [[Menu/Danh mục năm học học kỳ (H31)|Danh mục năm học học kỳ]] `H31` → [[Hoc ky]]
- [[Menu/Khởi tạo dữ liệu học kỳ (H32)|Khởi tạo dữ liệu học kỳ]] `H32` → [[Hoc ky]]
- Xóa dữ liệu học kỳ `H34` → [[Hoc ky]]

## Tiện ích người sử dụng
- Chuyển đổi chuỗi Unicode tổ hợp qua dựng sẵn `H93`
- Chuyển đổi đầu số điện thoại sinh viên `H90.13`
- Chuẩn hóa họ và tên sinh viên `H95`
- [[Menu/Chỉnh định menu (HTI01)|Chỉnh định menu]] `HTI01` → [[Cau hinh NetWEB]]
- Tìm hiểu báo biểu mẫu <small>(Giao diện & báo biểu)</small> `TestRP`
- Tìm hiểu giao diện mẫu <small>(Giao diện & báo biểu)</small> `TestView`
- Import file report `H97`
- In cấu trúc file EduSoft.NET `H96`
- Kiểm tra thông tin họ tên sinh viên `H98A`
- Kiểm tra thông tin ngày sinh sinh viên `H98`
- Phiên bản report `H90.12`
- Phục hồi theo Transaction `H90.15`
- Report mặc định theo user `H90.09`
- Tạo file danh sách sinh viên `H94`

## Trao đổi dữ liệu với EduWEB
- Nhật ký tải dữ liệu từ EduWEB `H99.05`
- Tải dữ liệu đăng ký từ EduWEB `H99.2`
- Xuất dữ liệu lên EduWEB `H99.1`

## Xem file hướng dẫn
- Tài liệu hướng dẫn EduSoft.NET `HHD1`

---
loai: danh-sach-menu
phan_he: "[[QLTS]]"
so_menu: 234
nguon: danh-muc-menu
---
# Menu QLTS – Tuyển sinh

234 menu Edusoft (từ `web/edusoft-catalog.json`). Tên **có liên kết** = menu **tạo** dữ liệu (có ghi chú riêng); → [[…]] = dữ liệu menu đó đụng tới.
Phân hệ: [[QLTS]].

## Chuẩn bị
- Danh sách cụm thi `T1.05`
- Danh sách cụm thi phổ thông `T1.10`
- [[Menu/Danh sách khối tuyển sinh (T1.02)|Danh sách khối tuyển sinh]] `T1.02` → [[Ky tuyen sinh]]
- [[Menu/Danh sách kỳ tuyển sinh (T1.01)|Danh sách kỳ tuyển sinh]] `T1.01` → [[Ky tuyen sinh]]
- Danh sách môn thi tuyển sinh `T1.04`
- [[Menu/Danh sách ngành tuyển sinh (T1.03)|Danh sách ngành tuyển sinh]] `T1.03` → [[Ky tuyen sinh]]
- Danh sách phòng thi `T1.06A`
- Danh sách trung tâm thi `T1.06`
- [[Menu/Danh sách đợt tuyển sinh (T1.09)|Danh sách đợt tuyển sinh]] `T1.09` → [[Ky tuyen sinh]]
- khối tuyển sinh <small>(Nhập ngành)</small> `T1.07` → [[Ky tuyen sinh]]
- [[Menu/Định nghĩa phương thức hồ sơ XT (T1.12)|Định nghĩa phương thức hồ sơ XT]] `T1.12` → [[Ky tuyen sinh]]
- Định nghĩa phương án nhập điểm `T1.11`

## Danh sách xét tuyển
- đợt xét tuyển <small>(Danh sách thí sinh)</small> `T8.02` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Gán đợt xét tuyển `T8.04` → [[DS trung tuyen]]
- In DS thí sinh chưa gán đợt `T08.04A` → [[Ho so thi sinh]], [[DS trung tuyen]]
- In DS thí sinh xét tuyển `T8.06` → [[Ho so thi sinh]], [[DS trung tuyen]]
- In DS thí sinh xét tuyển kiểm dò `T8.06A` → [[Ho so thi sinh]], [[DS trung tuyen]]
- In danh sách trúng tuyển dự kiến `T8.08` → [[DS trung tuyen]]
- Có tên trong danh sách nhưng chưa có trong DS nguyện vọng <small>(In kiểm tra dữ liệu)</small> `T8.2B.05` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Có tên trong danh sách nhưng chưa nhập điểm môn học <small>(In kiểm tra dữ liệu)</small> `T8.2B.04` → [[DS trung tuyen]]
- DS thí sinh có khu vực đối tượng không hợp lệ <small>(In kiểm tra dữ liệu)</small> `T8.2B.02` → [[Ho so thi sinh]], [[DS trung tuyen]]
- khối không hợp lệ <small>(In kiểm tra dữ liệu / DS thí sinh có ngành)</small> `T8.2B.01` → [[Ho so thi sinh]], [[DS trung tuyen]]
- In các môn chưa nhập điểm thi của ngành khối xét tuyển <small>(In kiểm tra dữ liệu)</small> `T8.2B.03` → [[DS trung tuyen]]
- Đã chuyển thí sinh vào NV1 thi tuyển <small>(In kiểm tra đã chuyển DS thí sinh)</small> `T8.02A.01` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Đã chuyển thí sinh vào NV1 xét tuyển <small>(In kiểm tra đã chuyển DS thí sinh)</small> `T8.02A.02` → [[Ho so thi sinh]], [[DS trung tuyen]]
- In thống kê thí sinh xét tuyển `T8.07` → [[Ho so thi sinh]], [[DS trung tuyen]]
- In thống kê thí sinh xét tuyển biểu đồ `T8.07.A` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Nhập nguyện vọng của từng thí sinh `T8.01` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Thống kê điểm xét tuyển `T8.09` → [[DS trung tuyen]]
- khối xét tuyển nguyện vọng 1B <small>(Đăng ký tự động NV cho thí sinh / Nhập ngành)</small> `T8.03.02` → [[Ho so thi sinh]], [[DS trung tuyen]]
- khối xét tuyển nguyện vọng 2 xét tuyển <small>(Đăng ký tự động NV cho thí sinh / Nhập ngành)</small> `T8.03.04` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Đăng ký tự động NV 1 cho thí sinh thi tuyển <small>(Đăng ký tự động NV cho thí sinh)</small> `T8.03.01` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Đăng ký tự động NV 1 cho thí sinh xét tuyển <small>(Đăng ký tự động NV cho thí sinh)</small> `T8.03.03A` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Đăng ký tự động NV 1B thi tuyển <small>(Đăng ký tự động NV cho thí sinh)</small> `T8.03.03` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Đăng ký tự động nguyện vọng 2 xét tuyển <small>(Đăng ký tự động NV cho thí sinh)</small> `T8.03.05` → [[Ho so thi sinh]], [[DS trung tuyen]]

## Hồ sơ nhập học
- [[Menu/Danh sách trúng tuyển (T9.00)|Danh sách trúng tuyển]] `T9.00` → [[DS trung tuyen]]
- Gán số giấy báo trúng tuyển `T9.01` → [[DS trung tuyen]]
- Theo File <small>(In phiếu báo trúng tuyển)</small> `T9.06.02` → [[DS trung tuyen]]
- Theo SBD <small>(In phiếu báo trúng tuyển)</small> `T9.06.03` → [[DS trung tuyen]]
- Định nghĩa mẫu in trúng tuyển <small>(In phiếu báo trúng tuyển)</small> `T9.06.00` → [[DS trung tuyen]]
- Gán mã cho  sinh viên trúng tuyển <small>(Mã SV cho thí sinh trúng tuyển)</small> `T9.04.01` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Hủy mã số cho thí sinh trúng tuyển <small>(Mã SV cho thí sinh trúng tuyển)</small> `T9.04.03` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Nhập mã số cho thí sinh trúng tuyển <small>(Mã SV cho thí sinh trúng tuyển)</small> `T9.04.02` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Nhập mã số sinh viên theo đối tượng <small>(Mã SV cho thí sinh trúng tuyển)</small> `T9.04.00` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Gán phòng KTX cho sv trúng tuyển <small>(Phòng KTX cho sv trúng tuyển)</small> `T9.05.01` → [[DS trung tuyen]]
- Hủy phòng KTX cho thí sinh trúng tuyển <small>(Phòng KTX cho sv trúng tuyển)</small> `T9.05.03` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Nhập phòng KTX cho thí sinh trúng tuyển <small>(Phòng KTX cho sv trúng tuyển)</small> `T9.05.02` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Gán tên lớp cho thí sinh trúng tuyển <small>(Tên lớp cho thì sinh trúng tuyển)</small> `T9.03.01` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Gán tên lớp theo file bởi MaSV <small>(Tên lớp cho thì sinh trúng tuyển)</small> `T9.03.02.A` → [[DS trung tuyen]]
- Hủy tên lớp cho thí sinh trúng tuyển <small>(Tên lớp cho thì sinh trúng tuyển)</small> `T9.03.03` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Nhập tên lớp cho thí sinh trúng tuyển <small>(Tên lớp cho thì sinh trúng tuyển)</small> `T9.03.02` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Phân bổ sĩ số các lớp trúng tuyển <small>(Tên lớp cho thì sinh trúng tuyển)</small> `T9.02` → [[DS trung tuyen]]
- đã xác nhận nhập học <small>(Xác nhận nhập học / In DS trúng tuyển)</small> `T9.06.A1` → [[DS trung tuyen]]
- Nhập thí sinh nhập học <small>(Xác nhận nhập học)</small> `T9.07` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Xác nhận nhập học của bộ <small>(Xác nhận nhập học)</small> `T9.07A` → [[DS trung tuyen]]
- Định nghĩa học phí môn học theo ngành `T9.00A` → [[DS trung tuyen]]

## Kiểm tra dữ liệu
- In kiểm tra chung dữ liệu chuẩn bị phân hệ `T20.01`
- In kiểm tra hợp lệ dữ liiệu trước khi xét tuyển `T20.06` → [[DS trung tuyen]]
- In kiểm tra hợp lệ file DS thí sinh `T20.02` → [[Ho so thi sinh]]
- In kiểm tra khả năng trùng hồ sơ tuyển sinh `T20.03`
- In kiểm tra điểm thi và phách vắng `T20.05`

## Nhập liệu hồ sơ
- Bộ đếm hồ sơ thí sinh và xét tuyển NV `T2.00` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Chuẩn hóa họ tên thí sinh `T2.07` → [[Ho so thi sinh]]
- File hồ sơ thí sinh của BGD `T2.02` → [[Ho so thi sinh]]
- Gán giá trị bộ đếm `T2.00_1` → [[Ho so thi sinh]]
- Import ảnh thí sinh `T2.06` → [[Ho so thi sinh]]
- In kiểm tra chung `T2.01` → [[Ho so thi sinh]]
- In kiểm tra hợp lệ dữ liệu `T2.04` → [[Ho so thi sinh]]
- In kiểm tra khả năng trùng hồ sơ `T2.05` → [[Ho so thi sinh]]
- Chuẩn bị khoản thu lệ phí <small>(Lệ  phí xét tuyển)</small> `T2.03_2.01` → [[Ho so thi sinh]], [[DS trung tuyen]]
- In liệt kê sinh viên đóng lệ phí xét tuyển <small>(Lệ  phí xét tuyển)</small> `T2.03_2.03` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Nhập lệ phí xét tuyển <small>(Lệ  phí xét tuyển)</small> `T2.03_2.02` → [[Ho so thi sinh]], [[DS trung tuyen]]
- In các mẫu thống kê số hồ sơ <small>(Nhập hồ sơ thí sinh)</small> `T2.03.04` → [[Ho so thi sinh]]
- In danh sách trùng <small>(Nhập hồ sơ thí sinh)</small> `T2.03.08` → [[Ho so thi sinh]]
- ths <small>(Nhập hồ sơ thí sinh / Nhập hồ sơ ĐKXT bằng đại học)</small> `T2.03.10` → [[Ho so thi sinh]]
- Nhập hồ sơ đăng ký XT năng lực <small>(Nhập hồ sơ thí sinh)</small> `T2.03.09` → [[Ho so thi sinh]]
- [[Menu/Nhập hồ sơ đăng ký thi tuyển (T2.03.01)|Nhập hồ sơ đăng ký thi tuyển]] <small>(Nhập hồ sơ thí sinh)</small> `T2.03.01` → [[Ho so thi sinh]]
- [[Menu/Nhập hồ sơ đăng ký xét tuyển (T2.03.00A)|Nhập hồ sơ đăng ký xét tuyển]] <small>(Nhập hồ sơ thí sinh)</small> `T2.03.00A` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Nhập hồ sơ đăng ký xét tuyển <small>(Nhập hồ sơ thí sinh)</small> `T2.03.02` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Nhập hồ sơ đăng ký xét tuyển khác <small>(Nhập hồ sơ thí sinh)</small> `T2.03.05` → [[Ho so thi sinh]], [[DS trung tuyen]]
- thi <small>(Nhập hồ sơ thí sinh / Nhập hồ sơ đăng ký xét tuyển)</small> `T2.03.00` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Nhập riêng theo user theo ngày <small>(Nhập hồ sơ thí sinh)</small> `T2.03.03` → [[Ho so thi sinh]]
- Nhập thí sinh tuyển thẳng <small>(Nhập hồ sơ thí sinh)</small> `T2.03.07` → [[Ho so thi sinh]]
- Nhập thông tin thí sinh không hợp lệ <small>(Nhập hồ sơ thí sinh)</small> `T2.03.06` → [[Ho so thi sinh]]

## Phách thi
- Gán tiếp số phách cho thí sinh <small>(Gán)</small> `T5.04` → [[Ho so thi sinh]]
- Hủy số phách đã gán `T5.06`
- In mẫu ghi điểm theo phòng thi <small>(In biểu ghi điểm theo SBD)</small> `T5.10.1`
- In mẫu scan điểm dùng máy quét điểm <small>(In biểu ghi điểm theo SBD)</small> `T5.10.2`
- In mẫu ghi điểm theo túi phách <small>(In biểu ghi điểm theo số phách)</small> `T5.09.1`
- In mẫu scan điểm dùng máy quét điểm <small>(In biểu ghi điểm theo số phách)</small> `T5.09.2`
- In hướng dẫn dồn túi `T5.07`
- In hướng dẫn ghi phách `T5.08`
- In kiểm tra DS thí sinh vắng hợp lệ `T5.03` → [[Ho so thi sinh]]
- mở khóa số phách đã gán <small>(Khóa)</small> `T5.05`
- Nhập File SBD-Phách `T5.11`
- Nhập số báo danh vắng `T5.02`
- Nhập thông tin phách cho nhóm thi chung `T5.01`

## Phúc Tra
- Chuyển điểm phúc tra về điểm tuyển sinh `T11.08`
- In bảng ghi điểm phúc tra `T11.04`
- túi phúc tra <small>(In bảng phách)</small> `T11.03`
- In kết quả phúc tra thí sinh `T11.07` → [[Ho so thi sinh]]
- In thay đổi kết quả tuyển sinh sau phúc tra `T11.09`
- In tổng hợp ds thí sinh xin phúc tra `T11.02` → [[Ho so thi sinh]]
- In tổng hợp kết quả phúc tra `T11.06`
- Nhập hồ sơ xin phúc tra `T11.01`
- Nhập điểm phúc tra `T11.05`

## Quản trị phân hệ
- Bổ sung dữ liệu học kỳ mang sang `TBS`
- Chỉnh định thông số học kỳ `TQT3`
- Chỉnh định thông số toàn cục `TQT2`
- Gán số bắt đầu cho bộ đếm chung phân hệ `TQT.04`
- Danh mục ngành tuyển sinh <small>(Quản lý danh mục)</small> `TQT0.4` → [[Ky tuyen sinh]]
- Danh mục địa bàn <small>(Quản lý danh mục)</small> `TQT0.1`
- Nhập môn thi cho khối <small>(Quản lý danh mục)</small> `T1.08`

## Tiếp sinh
- Bộ đếm số phiếu học phí `T10.00` → [[DS trung tuyen]]
- Chi HP <small>(Chuyển danh sách thí sinh đã đóng học phí sang phân hệ Thu)</small> `T10.07` → [[Ho so thi sinh]], [[DS trung tuyen]]
- [[Menu/Chuyển danh sách trúng tuyển sang phân hệ QLSV (T10.06)|Chuyển danh sách trúng tuyển sang phân hệ QLSV]] `T10.06` → [[DS trung tuyen]]
- Chuẩn bị khoản thu nhập học `T10.01.B` → [[DS trung tuyen]]
- Import ảnh thí sinh `T10.00.0` → [[Ho so thi sinh]], [[DS trung tuyen]]
- In danh sách sinh viên nhập học <small>(Mẫu in nhập học)</small> `T10.04.03` → [[DS trung tuyen]]
- In danh sách sinh viên nộp hồ sơ <small>(Mẫu in nhập học)</small> `T10.04.05` → [[DS trung tuyen]]
- In liệt kê học phí nhập học <small>(Mẫu in nhập học)</small> `T10.04.01` → [[DS trung tuyen]]
- lệ phí nhập học <small>(Mẫu in nhập học / In thống kê học phí)</small> `T10.04.04` → [[DS trung tuyen]]
- In thống kê nhập học <small>(Mẫu in nhập học)</small> `T10.04.02` → [[DS trung tuyen]]
- In thống kê nhập học biểu đồ <small>(Mẫu in nhập học)</small> `T10.04.02.A` → [[DS trung tuyen]]
- Nhập học phí nhập học <small>(Nhập hồ sơ & học phí nhập học)</small> `T10.02.02` → [[DS trung tuyen]]
- Nhập hồ sơ nhập học <small>(Nhập hồ sơ & học phí nhập học)</small> `T10.02.01` → [[DS trung tuyen]]
- Phân loại hs nhập học phương thức `T10.01.A1` → [[Ky tuyen sinh]], [[DS trung tuyen]]
- Phân loại hồ sơ nhập học diện trúng tuyển `T10.01.A` → [[DS trung tuyen]]
- Phân loại khoản thu theo đối tượng `T10.01.C` → [[DS trung tuyen]]
- Tạo file báo cáo nhập học gởi Bộ GD & ĐT `T10.05` → [[DS trung tuyen]]

## Tổ chức thi
- Gán môn tổ chức thi chung `T4.05`
- In DS thí sinh phòng thi `T4.14` → [[Ho so thi sinh]]
- In DS thí sinh trung tâm thi `T4.13` → [[Ho so thi sinh]]
- In biên bản phỏng vấn <small>(In biên bản / phiểu phỏng vấn)</small> `T4.20.00`
- In phiếu chấm phỏng vấn <small>(In biên bản / phiểu phỏng vấn)</small> `T4.20.01`
- In phiếu tổng hợp <small>(In biên bản / phiểu phỏng vấn)</small> `T4.20.02`
- In danh sách dán ảnh phòng thi `T4.18`
- In danh sách nhóm thi chung `T4.08`
- Theo File <small>(In phiếu báo dự thi)</small> `T4.17.02`
- Theo SBD <small>(In phiếu báo dự thi)</small> `T4.17.03`
- Theo cụm thi <small>(In phiếu báo dự thi)</small> `T4.17.01`
- In thống kê số lượng thí sinh đặc biệt `T4.10` → [[Ho so thi sinh]]
- Nhập hội đồng cho buổi thi vấn đáp `T4.07`
- Nhập hội đồng giám khảo `T4.00`
- Nhập hội đồng giám khảo `T4.03`
- Nhập hội đồng thi vấn đáp `T4.07A`
- Nhập nhóm môn thi tự chọn `T4.01` → [[Nhom hoc]]
- Nhập phòng thi `T4.04`
- Nhập thí sinh và môn tự chọn `T4.02` → [[Ho so thi sinh]]
- Nhập danh sách cấm thi <small>(Nhập thí sinh đặc biệt)</small> `T4.09.1` → [[Ho so thi sinh]]
- Nhập danh sách miễn thi theo môn <small>(Nhập thí sinh đặc biệt)</small> `T4.09.3` → [[Ho so thi sinh]]
- Nhập danh sách tuyển thằng <small>(Nhập thí sinh đặc biệt)</small> `T4.09.2` → [[Ho so thi sinh]]
- Nhập thông tin nhóm thi chung `T4.06`
- Hủy phòng thi đã gán <small>(Phòng thi thí sinh)</small> `T4.12.4` → [[Ho so thi sinh]]
- In dự kiến thí sinh & phòng thi <small>(Phòng thi thí sinh)</small> `T4.12.1` → [[Ho so thi sinh]]
- In thống kê sử dụng phòng theo cụm thi <small>(Phòng thi thí sinh)</small> `T4.12.8` → [[Ho so thi sinh]]
- In thống kê sử dụng phòng theo môn <small>(Phòng thi thí sinh)</small> `T4.12.7` → [[Ho so thi sinh]]
- mở khóa phòng thi đã gán <small>(Phòng thi thí sinh / Khóa)</small> `T4.12.3` → [[Ho so thi sinh]]
- Kiểm tra hợp lệ phòng thi <small>(Phòng thi thí sinh)</small> `T4.12.5` → [[Ho so thi sinh]]
- Nhập phòng thi cho thí sinh <small>(Phòng thi thí sinh)</small> `T4.12.6` → [[Ho so thi sinh]]
- Phân bố phòng thi cho thí sinh <small>(Phòng thi thí sinh)</small> `T4.12.2` → [[Ho so thi sinh]]
- Gán SBD min cho khối + cụm thi <small>(Số báo danh thí sinh)</small> `T4.11.1` → [[Ho so thi sinh]]
- gán tiếp số SBD <small>(Số báo danh thí sinh / Gán)</small> `T4.11.2` → [[Ho so thi sinh]]
- Hủy số báo danh đã gán <small>(Số báo danh thí sinh)</small> `T4.11.4` → [[Ho so thi sinh]]
- mở khóa sổ SBD đã gán <small>(Số báo danh thí sinh / Khóa sổ)</small> `T4.11.3` → [[Ho so thi sinh]]
- Kiểm tra hợp lệ số báo danh <small>(Số báo danh thí sinh)</small> `T4.11.5` → [[Ho so thi sinh]]
- Nhập số báo danh cho thí sinh <small>(Số báo danh thí sinh)</small> `T4.11.6` → [[Ho so thi sinh]]
- Đồng bộ danh sách môn thi theo ngành khối `T4.19`

## Xem file hướng dẫn
- Tài liệu hướng dẫn EduSoft.NET `THD1`

## Xét tuyển
- Bộ đếm phiếu báo trúng tuyển `T8.00` → [[DS trung tuyen]]
- Hủy kết quả trúng tuyển theo đợt `T12.1.3` → [[DS trung tuyen]]
- Theo SBD <small>(In bảng liệt kê kết quả trúng tuyển)</small> `T13.4.1` → [[DS trung tuyen]]
- Theo cụm thi <small>(In bảng liệt kê kết quả trúng tuyển)</small> `T13.4.5` → [[DS trung tuyen]]
- Theo khối <small>(In bảng liệt kê kết quả trúng tuyển)</small> `T13.4.4` → [[DS trung tuyen]]
- Theo ngành <small>(In bảng liệt kê kết quả trúng tuyển)</small> `T13.4.3` → [[DS trung tuyen]]
- khối <small>(In bảng liệt kê kết quả trúng tuyển / Theo ngành)</small> `T13.4.2` → [[DS trung tuyen]]
- In danh sách thủ khoa `T13.6` → [[DS trung tuyen]]
- In danh sách trúng tuyển `T13.3A` → [[DS trung tuyen]]
- In thống kê trúng tuyển `T13.3` → [[DS trung tuyen]]
- In thống kê trúng tuyển biểu đồ `T13.3B` → [[DS trung tuyen]]
- Tạo file báo cáo trúng tuyển gởi Bộ GD & ĐT `T13.5` → [[DS trung tuyen]]
- Xét tuyển theo thí sinh `T12.2` → [[Ho so thi sinh]], [[DS trung tuyen]]
- mở khóa sổ đợt <small>(Xét tuyển theo đợt / Khóa sổ)</small> `T12.1.2` → [[DS trung tuyen]]
- xét lại trúng tuyển <small>(Xét tuyển theo đợt / Xét)</small> `T12.1.1` → [[DS trung tuyen]]

## Ôn thi
- In danh sách nộp hồ sơ ôn thi theo môn `T3.03`
- In danh sách rút hồ sơ ôn thi theo môn `T3.02`
- khối <small>(In danh sách tổng hợp nộp hồ sơ theo ngành)</small> `T3.04`
- Nhập danh sách đăng ký ôn thi `T3.01`
- Nhập điểm thi cho các môn ôn thi `T3.05`

## Điểm chuẩn
- Theo nguyện vọng <small>(In thống kê điểm)</small> `T7.01.1` → [[Ho so thi sinh]], [[DS trung tuyen]]
- đơt <small>(In thống kê điểm / Theo nguyện vọng)</small> `T7.01.2` → [[Ho so thi sinh]], [[DS trung tuyen]]
- Nhập điểm chuẩn xét tuyển `T7.03` → [[DS trung tuyen]]
- Điểm ưu tiên khác với qui định `T7.02` → [[DS trung tuyen]]

## Điểm thi
- cộng lại điểm thi các môn <small>(Cộng)</small> `T6.14`
- In DS thí sinh có điểm liệt `T6.11` → [[Ho so thi sinh]]
- Theo SBD <small>(In bảng liệt kê kết quả thi)</small> `T6.16.01`
- Theo cụm thi <small>(In bảng liệt kê kết quả thi)</small> `T6.16.06`
- Theo khối <small>(In bảng liệt kê kết quả thi)</small> `T6.16.05`
- Theo ngành <small>(In bảng liệt kê kết quả thi)</small> `T6.16.04`
- khối <small>(In bảng liệt kê kết quả thi / Theo ngành)</small> `T6.16.03`
- Theo phách - Theo SBD <small>(In bảng liệt kê kết quả thi)</small> `T6.16.02`
- In DS ghi điểm các môn không tạo phách theo hội đồng thi vấn đáp <small>(In bảng điểm thi không theo phách)</small> `T6.01.2`
- In DS ghi điểm các môn không tạo phách theo phòng thi <small>(In bảng điểm thi không theo phách)</small> `T6.01.1`
- In DS ghi điểm các môn nhập điểm bằng McSCANNER <small>(In bảng điểm thi không theo phách)</small> `T6.01.3`
- In theo bảng ghi điểm nhận dạng bằng scanner <small>(In bảng điểm đã nhập để kiểm dò)</small> `T6.04.4`
- In theo hội đồng <small>(In bảng điểm đã nhập để kiểm dò)</small> `T6.04.3`
- In theo phòng thi <small>(In bảng điểm đã nhập để kiểm dò)</small> `T6.04.2`
- số phách <small>(In bảng điểm đã nhập để kiểm dò / In theo số túi)</small> `T6.04.1`
- In theo bảng ghi điểm nhận dạng bằng scanner <small>(In các bảng điểm chưa nhập)</small> `T6.03.4`
- In theo hội đồng <small>(In các bảng điểm chưa nhập)</small> `T6.03.3`
- In theo phòng thi <small>(In các bảng điểm chưa nhập)</small> `T6.03.2`
- số phách <small>(In các bảng điểm chưa nhập / In theo số túi)</small> `T6.03.1`
- In kiểm tra điểm thi và danh sách cấm thi `T6.07C`
- In kiểm tra điểm thi và danh sách miễn `T6.07A`
- In kiểm tra điểm thi và danh sách tuyển thẳng `T6.07B`
- In kiểm tra điểm thi và danh sách vắng `T6.07`
- In kiểm tra điểm thi và phách vắng `T6.06`
- Theo File <small>(In phiếu báo điểm thi)</small> `T6.17.02`
- Theo SBD <small>(In phiếu báo điểm thi)</small> `T6.17.03`
- Theo cụm thi <small>(In phiếu báo điểm thi)</small> `T6.17.01`
- In thống kê số thí sinh dự thi `T6.13` → [[Ho so thi sinh]]
- -) điểm môn thi của thí sinh <small>(In điểm hiệu chỉnh (+)</small> `T6.09` → [[Ho so thi sinh]]
- Kiểm tra theo bảng ghi điểm nhận dạng bằng scanner <small>(Kiểm dò điểm thi bằng giọng nói)</small> `T6.05.4`
- Kiểm tra theo hội đồng <small>(Kiểm dò điểm thi bằng giọng nói)</small> `T6.05.3`
- Kiểm tra theo phòng thi <small>(Kiểm dò điểm thi bằng giọng nói)</small> `T6.05.2`
- số phách <small>(Kiểm dò điểm thi bằng giọng nói / Kiểm tra theo số túi)</small> `T6.05.1`
- -) điểm môn thi <small>(Nhập hiệu chỉnh (+)</small> `T6.10`
- Theo bảng điểm thi trắc nghiệm (nhận dạng bằng McSCANNER) <small>(Nhập điểm thi)</small> `T6.02.4`
- Theo hội đồng thi <small>(Nhập điểm thi)</small> `T6.02.3`
- Theo phòng thi và số báo danh <small>(Nhập điểm thi)</small> `T6.02.2`
- Theo số phách <small>(Nhập điểm thi)</small> `T6.02.1`
- Xem điểm thi `T6.15`
- Xử lý việc chấm lại theo xác suất bài thi `T6.12`
- Đồng bộ danh sách vắng từ điểm thi `T6.08`

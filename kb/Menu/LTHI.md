---
loai: danh-sach-menu
phan_he: "[[LTHI]]"
so_menu: 125
nguon: danh-muc-menu
---
# Menu LTHI – Tổ chức thi

125 menu Edusoft (từ `web/edusoft-catalog.json`). Tên **có liên kết** = menu **tạo** dữ liệu (có ghi chú riêng); → [[…]] = dữ liệu menu đó đụng tới.
Phân hệ: [[LTHI]].

## An toàn dữ liệu
- Khóa thông tin nhóm thi theo đợt <small>(Khóa và mở khóa dữ liệu)</small> `LKDL.01` → [[Danh sach thi]]
- Khác biệt giữa danh sách ĐKMH và ds thi <small>(Kiểm tra dữ liệu / Danh sách thi)</small> `LKT1.02` → [[KQ DKMH]], [[Danh sach thi]]
- Sinh viên thi nhiều môn học <small>(Kiểm tra dữ liệu / Danh sách thi)</small> `LKT1.01` → [[Danh sach thi]]
- Danh sách MH chưa xếp lịch thi <small>(Kiểm tra dữ liệu / Lịch thi)</small> `LKT3.01` → [[Danh sach thi]]
- In kiểm tra trùng lịch sử dụng phòng <small>(Kiểm tra dữ liệu / Lịch thi)</small> `LKT3.05` → [[Danh sach thi]]
- ngày <small>(Kiểm tra dữ liệu / Lịch thi / Sinh viên thi nhiều hơn n MH)</small> `LKT3.04` → [[Danh sach thi]]
- Trùng thời khóa biểu phòng <small>(Kiểm tra dữ liệu / Lịch thi)</small> `LKT3.02` → [[Thoi khoa bieu]], [[Danh sach thi]]
- Trùng thời khóa biểu sinh viên <small>(Kiểm tra dữ liệu / Lịch thi)</small> `LKT3.03` → [[Thoi khoa bieu]], [[Danh sach thi]]
- Danh sách MH có SV chưa phân tổ <small>(Kiểm tra dữ liệu / Tổ thi)</small> `LKT2.01` → [[Danh sach thi]]
- tổ <small>(Truy vết dữ liệu / Nhật ký biến động lịch thi theo nhóm)</small> `LTV1` → [[Danh sach thi]]
- Nhật ký hiệu chỉnh lịch thi <small>(Truy vết dữ liệu)</small> `LTV2` → [[Danh sach thi]]
- Xem log lịch thi <small>(Truy vết dữ liệu)</small> `LTV3` → [[Danh sach thi]]

## Chính sách lịch thi
- Nhập tính chất thi môn học <small>(Tính chất thi môn học)</small> `L12.02` → [[Danh sach thi]]
- Định nghĩa tên gọi ca thi `L15` → [[Danh sach thi]]
- Định nghĩa thời gian `L14` → [[Danh sach thi]]

## Hiệu chỉnh lịch thi
- Danh sách sinh viên trong tổ thi `L311.07` → [[Danh sach thi]]
- Ghép sinh viên hoãn thi vào tổ thi `L311.12` → [[Danh sach thi]]
- Ghép phòng thi cùng Ngày & Tiết `L311.09` → [[Phong hoc]], [[Danh sach thi]]
- Gán SV có ĐKMH vào tổ thi - theo DS sinh viên `L22.06.CT` → [[KQ DKMH]], [[Danh sach thi]]
- Gán SV có ĐKMH vào tổ thi - theo sinh viên `L22.06` → [[KQ DKMH]], [[Danh sach thi]]
- Hiệu chỉnh SV trong tổ thi - theo sinh viên `L22.05` → [[Danh sach thi]]
- Hiệu chỉnh SV trong tổ thi - theo tổ thi `L22.02` → [[Danh sach thi]]
- Hiệu chỉnh lịch thi `L311.05` → [[Danh sach thi]]
- Hủy ghép phòng thi cùng Ngày & Tiết `L31.10` → [[Phong hoc]], [[Danh sach thi]]
- Lịch thi sinh viên đặc thù `L311.11` → [[Danh sach thi]]
- Nhóm học không xét cấm thi học lực `L311.10` → [[Nhom hoc]], [[Danh sach thi]]
- Nhập danh sách sinh viên vắng thi `L311.88` → [[Danh sach thi]]
- Nhập danh sách sinh viên vắng thi `L311.08` → [[Danh sach thi]]

## Hoạt động coi thi
- Theo cán bộ coi thi <small>(In danh sách coi thi)</small> `L44.02` → [[Vien chuc]], [[Danh sach thi]]
- Theo ngày thi (từ ngày...đến ngày) <small>(In danh sách coi thi)</small> `L44.04` → [[Danh sach thi]]
- Theo tổ thi <small>(In danh sách coi thi)</small> `L44.01` → [[Danh sach thi]]
- Theo đợt thi <small>(In danh sách coi thi)</small> `L44.03` → [[Danh sach thi]]
- Cán bộ coi thi giảng dạy môn thi <small>(In kiểm tra dữ liệu)</small> `L46.04` → [[Vien chuc]], [[Danh sach thi]]
- Cán bộ coi thi không có trong đợt thi <small>(In kiểm tra dữ liệu)</small> `L46.01` → [[Vien chuc]], [[Danh sach thi]]
- Cán bộ trùng lịch coi thi <small>(In kiểm tra dữ liệu)</small> `L46.03` → [[Vien chuc]], [[Danh sach thi]]
- Cán bộ vượt cấp coi thi <small>(In kiểm tra dữ liệu)</small> `L46.02` → [[Vien chuc]], [[Danh sach thi]]
- Theo cán bộ coi thi <small>(In thù lao cán bộ coi thi)</small> `L45.03` → [[Vien chuc]], [[Danh sach thi]]
- Theo ngày thi <small>(In thù lao cán bộ coi thi)</small> `L45.04` → [[Vien chuc]], [[Danh sach thi]]
- Theo tổ thi <small>(In thù lao cán bộ coi thi)</small> `L45.02` → [[Vien chuc]], [[Danh sach thi]]
- Theo đợt thi <small>(In thù lao cán bộ coi thi)</small> `L45.01` → [[Vien chuc]], [[Danh sach thi]]
- Nhập SL cán bộ coi thi cho tổ thi `L42` → [[Vien chuc]], [[Danh sach thi]]
- Nhập danh sách coi thi vãng lai `L49` → [[Danh sach thi]]
- Nhập danh sách cán bộ coi thi `L47` → [[Vien chuc]], [[Danh sach thi]]
- Phân công coi thi `L43` → [[Danh sach thi]]
- Danh mục quyền coi thi <small>(Phân công coi thi khác)</small> `L48.01` → [[Danh sach thi]]
- Nhập phân công coi thi khác <small>(Phân công coi thi khác)</small> `L48.02` → [[Danh sach thi]]
- Quy định thời gian ngoài giờ <small>(Định mức thù lao coi thi)</small> `L41.03` → [[Danh sach thi]]
- Định mức thù lao coi thi <small>(Định mức thù lao coi thi)</small> `L41.02` → [[Danh sach thi]]
- Định mức thù lao coi thi ra giờ chuẩn <small>(Định mức thù lao coi thi)</small> `L41.04` → [[Danh sach thi]]

## Hủy danh sách dự thi
- Hủy theo danh sách sinh viên `L23.05`
- Hủy theo file `L23.04`
- Hủy theo môn học `L23.02`
- Hủy theo sinh viên rút môn học `L23.03` → [[KQ DKMH]]
- Hủy theo đợt thi `L23.01` → [[Danh sach thi]]

## Hủy lịch thi
- Hủy theo sinh viên `L31.05` → [[Danh sach thi]]
- Hủy theo đợt - môn học `L311.03` → [[Danh sach thi]]
- Hủy theo đợt - nhóm thi `L311.06` → [[Danh sach thi]]
- Hủy tất cả `L311.04` → [[Danh sach thi]]

## In giấy vào phòng thi
- In giấy vào phòng thi `L102` → [[Phong hoc]]
- Sinh viên in giấy vào phòng thi `L104` → [[Phong hoc]]
- Thống kê số lượng in giấy `L103` → [[Phong hoc]]

## Quản lý hoãn thi
- Ghép SV hoãn vào kỳ thi `L52` → [[Danh sach thi]]
- In danh sách thi hoãn thi `L54` → [[Danh sach thi]]
- In thống kê thi hoãn thi `L53` → [[Danh sach thi]]
- Sinh viên đăng ký hoãn thi `L51` → [[Danh sach thi]]

## Quản lý nhóm thi
- In danh sách thi theo nhóm thi `L22.04` → [[Danh sach thi]]
- In thống kê sinh viên theo nhóm thi `L22.03` → [[Danh sach thi]]
- Cập nhật thông tin nhóm thi <small>(Tạo nhóm thi)</small> `L21.02` → [[Danh sach thi]]
- Cập nhật thông tin trạm thi <small>(Tạo nhóm thi)</small> `L21.06` → [[Danh sach thi]]
- Danh sách nhóm thi <small>(Tạo nhóm thi)</small> `L21.01` → [[Danh sach thi]]
- Hiệu chỉnh SV trong nhóm thi <small>(Tạo nhóm thi)</small> `L21.10` → [[Danh sach thi]]
- Khóa thông tin tin nhóm thi <small>(Tạo nhóm thi)</small> `L21.07A` → [[Danh sach thi]]
- Nhóm môn học không tổ chức thi <small>(Tạo nhóm thi)</small> `L21.05` → [[Nhom hoc]], [[Danh sach thi]]
- Tách nhóm thi theo lớp sinh viên <small>(Tạo nhóm thi)</small> `L21.03` → [[Danh sach thi]]
- Xem KHGD môn học trong học kỳ <small>(Tạo nhóm thi)</small> `L21.04` → [[Danh sach thi]]
- sửa nhóm thi không in bảng ghi điểm <small>(Tạo nhóm thi / Xem)</small> `L21.11` → [[Danh sach thi]]
- Xem danh sách theo nhóm thi `L22.07` → [[Danh sach thi]]
- Đồng bộ sĩ số dự thi `L22.01` → [[Danh sach thi]]

## Quản lý nộp điểm
- In tổng hợp nộp điểm theo khoa `L55.02`
- Nhập thời gian nộp điểm `L55.01`

## Quản lý thi cải thiện
- Ghép sinh viên cải thiện vào kỳ thi `L62`
- In danh sách thi cải thiện `L64` → [[Danh sach thi]]
- In thống kê thi cải thiện `L63`
- Sinh viên đăng ký thi cải thiện `L61`

## Quản lý tổ thi
- Ghép tổ thi thủ công <small>(Ghép tách tổ thi)</small> `L35.02` → [[Danh sach thi]]
- Ghép tổ thi tự động <small>(Ghép tách tổ thi)</small> `L35.01` → [[Danh sach thi]]
- Tách tổ thi thủ công <small>(Ghép tách tổ thi)</small> `L35.03` → [[Danh sach thi]]
- In thống kê cung cầu phòng thi `L36` → [[Phong hoc]], [[Danh sach thi]]
- Danh sách tổ thi đã tạo <small>(Tạo danh sách tổ thi)</small> `L34.05` → [[Danh sach thi]]
- In danh sách thi theo tổ thi <small>(Tạo danh sách tổ thi)</small> `L34.04` → [[Danh sach thi]]
- In thống kê sinh viên theo tổ thi <small>(Tạo danh sách tổ thi)</small> `L34.03` → [[Danh sach thi]]
- Nhập cán bộ trạm thi <small>(Tạo danh sách tổ thi)</small> `L21.07` → [[Vien chuc]], [[Danh sach thi]]
- Phân công chấm thi <small>(Tạo danh sách tổ thi)</small> `L34.08` → [[Danh sach thi]]
- Phân tổ thi theo file <small>(Tạo danh sách tổ thi)</small> `L34.09` → [[Danh sach thi]]
- Phân tổ thi tự động <small>(Tạo danh sách tổ thi)</small> `L34.01` → [[Danh sach thi]]
- Sửa tổ thi không in bảng ghi điểm <small>(Tạo danh sách tổ thi / Xem)</small> `L34.10` → [[Danh sach thi]]

## Quản trị phân hệ
- Bổ sung dữ liệu học kỳ mang sang `LBS`
- Chỉnh định thông số học kỳ `LQT3`
- Chỉnh định thông số toàn cục `LQT2`
- Phân quyền xếp  theo nhóm thi <small>(Phân quyền xếp lịch thi)</small> `LQY3` → [[Danh sach thi]]
- Định nghĩa trạm cho môn thi <small>(Quản lý danh mục)</small> `LQT01`

## Tài nguyên và ràng buộc
- DS sinh viên học cùng lúc 2 chương trình <small>(Ràng buộc xếp lịch thi)</small> `L8.03` → [[Danh sach thi]]
- Nhóm thi thi chung thời gian <small>(Ràng buộc xếp lịch thi)</small> `L37` → [[Danh sach thi]]
- Tiết bắt đầu được xếp lịch thi <small>(Ràng buộc xếp lịch thi)</small> `L8.02.1` → [[Danh sach thi]]
- Tổ thi thi chung phòng <small>(Ràng buộc xếp lịch thi)</small> `L34.02` → [[Danh sach thi]]
- Ngày & tiết bắt đầu thi ưu tiên <small>(Tài nguyên xếp lịch thi)</small> `L38` → [[Danh sach thi]]
- Phòng thi ưu tiên <small>(Tài nguyên xếp lịch thi)</small> `L313` → [[Phong hoc]], [[Danh sach thi]]

## Vi phạm Qui chế thi
- Chuyển điểm trừ vào phân hệ điểm `L56.04`
- DSSV vi phạm Quy chế thi `L56.03`
- In DSSV vi phạm quy chế thi `L56.05`

## Xem file hướng dẫn
- Tài liệu hướng dẫn EduSoft.NET `LHD1`

## Xếp lịch thi
- Hệ số ưu tiên xếp lịch thi tự động <small>(Chỉnh định)</small> `L91` → [[Danh sach thi]]
- Xếp lịch thi cho 1 nhóm thi `L39.02` → [[Danh sach thi]]
- Xếp lịch thi theo TKB `L39.04` → [[Thoi khoa bieu]], [[Danh sach thi]]
- Xếp lịch thi theo TKB - Không gán phòng `L39.05` → [[Thoi khoa bieu]], [[Danh sach thi]]
- [[Menu/Xếp lịch thi theo đợt thi (L39.03)|Xếp lịch thi theo đợt thi]] `L39.03` → [[Danh sach thi]]

## Đánh số báo danh
- Nhập ký hiệu phòng `L20.1` → [[Danh sach thi]]
- Đánh số báo danh `L20.2` → [[Danh sach thi]]

## Đăng ký thi lại & cải thiện
- Đăng ký thi lại & cải thiện `DTL01.01`

## Định nghĩa đợt thi
- Ghép nhóm thi tự động `L31.04` → [[Danh sach thi]]
- Gán đối tượng thi `L31.02` → [[Danh sach thi]]
- Gán đợt thi cho nhóm thi `L31.03` → [[Danh sach thi]]
- Nhập phòng sử dụng trong đợt `L33.01` → [[Danh sach thi]]
- Nhập thời gian không thi `L32.01` → [[Danh sach thi]]
- Định nghĩa đợt thi & gán nhóm thi `L31.01` → [[Danh sach thi]]

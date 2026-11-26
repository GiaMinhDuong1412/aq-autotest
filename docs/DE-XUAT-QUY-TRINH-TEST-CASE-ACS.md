# Đề xuất: làm lại quy trình Test case ACS

> Bản nháp để duyệt – 26/11/2026. Chưa làm gì theo đề xuất này cho tới khi chốt.
> Ví dụ xuyên suốt: case **#64781** (DHMOTX – thêm "Nơi cấp VB trước sáp nhập", cập nhật theo file).

---

## 1. Vì sao phải làm lại

| # | Vấn đề hiện tại | Hậu quả thấy được |
|---|---|---|
| 1 | Plan **sinh tự động bằng dò chữ** (câu KH, ghi chú dev, KB) | 30 mục chung chung, trùng; có lúc chép nguyên câu KH ("Vào chỗ KH phản ánh…") |
| 2 | Không có bước **thiết kế test**: chưa chốt "test những trường hợp nào, vì sao" | Thiếu nhánh dev đã sửa; thừa mục không liên quan |
| 3 | **Đầu ra không có giá trị cụ thể** ("giữ nguyên", "đúng") | Không bắt được lỗi; người test vẫn phải tự nghĩ |
| 4 | **Dữ liệu test** không chọn theo điều kiện (lấy mã SV trong bình luận cũ) | Bước "Hồ sơ test" vô nghĩa, bộ test bấm Đạt mà không kiểm gì |
| 5 | Không có **cổng duyệt** – plan sinh ra là chạy | Chạy cả plan sai |
| 6 | Thứ tự **hiển thị ≠ thứ tự chạy** (nhóm Chuẩn bị / Thao tác / Đầu ra) | Bộ test báo "Bước 3/16" không khớp số trên trang |
| 7 | Bước tay và bước tự động **lẫn lộn**, không biết bước nào máy tự kiểm | Người test không tin kết quả |
| 8 | Claude trên cloud **không đưa plan vào app được** (chỉ Claude Desktop qua MCP) | Phân tích đúng ở chat nhưng app vẫn hiện plan dò chữ |
| 9 | Lỗi kỹ thuật: vào thẳng bước 2 thì app chưa đọc chi tiết case → "soạn lại" ra plan cũ; hai hàm trùng tên `rtDetail` (gây "422 – [object Promise]") | *Đã sửa trong PR kèm đề xuất này* |

**Gốc rễ:** đang để *máy đoán plan*, trong khi việc khó nhất – **thiết kế test** – cần người/Claude làm có chủ đích, máy chỉ nên **chạy và so**.

---

## 2. Các công cụ autotest khác làm thế nào

| Công cụ | Cách họ làm | Lấy gì cho AQ Auto Test |
|---|---|---|
| **TestRail / Xray / Zephyr** (quản lý test case) | Test case = *Điều kiện trước* + *Các bước* + *Kết quả mong đợi*; gắn với yêu cầu (traceability); Test Run ghi Đạt/Lỗi từng case | Mỗi dòng test có đủ 3 phần; mỗi dòng **gắn với một ý dev đã sửa** |
| **Cucumber / Gherkin (BDD)** | `Cho` (Given) – `Khi` (When) – `Thì` (Then); **Scenario Outline + bảng Examples** = một kịch bản, nhiều bộ dữ liệu | **Bảng ma trận** = Scenario Outline: một khuôn, mỗi dòng một bộ dữ liệu + kỳ vọng |
| **Robot Framework** | **Keyword-driven** (từ khoá: Mở menu, Tìm dòng, Kiểm ô…) + **data-driven** (Test Template chạy một keyword với nhiều dòng dữ liệu) | Bộ test đã có keyword (`menu:`, `row:`, `row_check:`…) → plan chỉ cần ghép keyword theo từng dòng bảng |
| **Tricentis Tosca** | **Thiết kế test trước** (phân lớp tương đương, tổ hợp, bảng quyết định), **Test Data Service** tìm dữ liệu thoả điều kiện, ưu tiên theo rủi ro | Bước **Thiết kế** riêng; bộ test **tự tìm hồ sơ thoả điều kiện** thay vì người test đi tìm |
| **TestComplete / Ranorex / UFT One** (desktop) | **Object repository** (tên điều khiển), **checkpoint** so giá trị ô/bảng, vòng lặp data-driven, ảnh + log mỗi checkpoint | `edusoft-catalog.json` = object repository; checkpoint = `row_check:` có **giá trị kỳ vọng cụ thể**, ghi kỳ vọng ↔ thực tế |
| **Playwright** (web) | Assertion tự chờ, **trace** (ảnh + DOM từng bước), báo cáo HTML | Case Netweb: mỗi đầu ra = một assertion; lưu trace làm bằng chứng gửi ACS |
| **Kiểm thử khám phá (session-based)** | "Charter" có thời hạn: mục tiêu, phạm vi, ghi chú phát hiện | Phần không tự động được → một **charter ngắn** thay cho chục bước tay mơ hồ |

**Điểm chung của các công cụ tốt:** *thiết kế test → dữ liệu → chạy → so kỳ vọng cụ thể → bằng chứng*, có **duyệt** giữa thiết kế và chạy; máy không tự nghĩ ra test case.

---

## 3. Quy trình mới (6 bước, 1 cổng duyệt)

```
 ① Phân tích ──► ② Thiết kế test ──► ③ Dữ liệu test ──► [DUYỆT] ──► ④ Chạy ──► ⑤ Kết quả & lỗi ──► ⑥ Ghi ACS + học lại
   (Claude)        (Claude)            (bộ test tìm)      (người test)   (bộ test + tay)  (tự soạn)          (app)
```

### ① Phân tích – "đúng trước"
Claude đọc theo thứ tự (đã có trong `kb/00 Cách phân tích case.md`): trường/phân cấp → phân hệ → KH → BA → **Dev (từng LẦN, từng nhánh điều kiện đã sửa)**
→ trao đổi test + **ảnh các lần test trước** → case gốc / liên quan → KB (dữ liệu chảy đi đâu, "đường ghi khác").

Đầu ra: **Phiếu phân tích** gồm
- **Điều thay đổi** (mỗi nhánh dev sửa một dòng), vd #64781:
  1. Thêm ô / cột "trước SN" (combobox Danh mục nơi cấp VB).
  2. Cập nhật theo file: có "trước SN" (trong file hoặc đã lưu) thì **không** tự lấy Nơi cấp VB theo văn bằng SV; ô trống trong file = giữ nguyên.
  3. Đồng bộ tất cả / chưa có: có "trước SN" thì không tự điền Nơi cấp VB.
  4. Xuất Excel: không sửa code – Column Chooser.
- **Lỗi các lần trước** (kèm hồ sơ, ảnh): 3 lần "đồng hoá" khi cập nhật theo file.
- **Rủi ro / ảnh hưởng**: Import, Nhập kết quả thẩm tra, In phiếu, trường gốc DHMO.

### ② Thiết kế test – bảng điều kiện (Gherkin / Scenario Outline)
Mỗi **điều thay đổi** → một hoặc vài **kịch bản mẫu**; mỗi kịch bản là một **bảng**: *Cho* (điều kiện dữ liệu) / *Khi* (thao tác) / *Thì* (giá trị cụ thể).
Kỹ thuật chọn dòng: **bảng quyết định** theo nhánh code dev sửa, **phân lớp tương đương** (có / trống / sai mã), **hồi quy lỗi cũ**, **hành vi cũ không đổi**.

Ví dụ #64781 – Kịch bản "Cập nhật theo file không đè cột cũ":

| Dòng | Cho (hồ sơ trước) | Khi (trong file) | Thì (sau Thực hiện) | Vì sao có dòng này |
|---|---|---|---|---|
| A | cũ **có**, mới **trống** | cũ trống, mới = M1 | cũ **= giá trị trước**, mới = M1 | lỗi 3 lần trước |
| B | cũ có | cũ = M2, mới = M1 | cũ = M2, mới = M1 | hai cột không đè nhau |
| C | cũ có, mới có | cũ = M2, mới trống | cũ = M2, mới **= giá trị trước** | ô trống = giữ nguyên |
| D | cũ **trống** (văn bằng SV có nơi cấp) | cũ trống, mới = M1 | cũ **trống**, mới = M1 | nhánh "không lấy theo văn bằng" |
| E | cũ trống, mới trống | cả hai trống | cũ **= nơi cấp văn bằng SV**, mới trống | hành vi cũ giữ nguyên |
| F | bất kỳ | mới = mã sai | **không đổi**, dòng ở nhóm lỗi | mã sai danh mục |
| G | cũ có | cũ = M1, mới = M1 | cả hai = M1 | cho phép trùng |

Các kịch bản khác của #64781 (mỗi cái 1–3 dòng): Sửa tay · Đồng bộ tất cả / chưa có · Xuất Excel (Column Chooser) · Nhập kết quả thẩm tra (ô khoá) · Mở ở DHMO.
**Độ phủ**: mỗi "điều thay đổi" ở ① phải có ≥ 1 dòng; lỗi cũ phải có dòng riêng.

### ③ Dữ liệu test – máy tìm, người duyệt
- Mỗi dòng nêu **điều kiện hồ sơ** (cột nào có / trống). **Bộ test tự tìm** hồ sơ thoả điều kiện trên lưới (lệnh mới `find_data:`), đề xuất mã; người test đổi được.
- Ghi **ảnh chụp dữ liệu trước** (snapshot) mọi hồ sơ dùng → để so "= giá trị trước" và để **dọn / trả lại** sau test.
- Hằng số (M1, M2, mã sai) chọn từ danh mục, ghi rõ trên phiếu.

### [DUYỆT] – cổng bắt buộc
Người test xem **Phiếu phân tích + bảng test + dữ liệu**, sửa nếu cần, bấm **Duyệt**. Chưa duyệt thì **không** chạy được.
(Giống "review test case" trong TestRail / Xray.)

### ④ Chạy – keyword theo từng dòng bảng
- Mỗi dòng bảng → chuỗi keyword: *mở menu → tìm hồ sơ → (thao tác) → checkpoint*. Bước bộ test làm được thì tự làm; bước chưa có keyword thì
  **bước tay có hướng dẫn cụ thể** (vd "Điền file: A 75251128TPE1 – cũ trống, mới 0105") rồi bộ test **tự so** ngay sau đó.
- **Thứ tự chạy = thứ tự hiển thị** (không chia nhóm Chuẩn bị / Thao tác / Đầu ra nữa – mỗi dòng bảng tự đủ Cho / Khi / Thì).
- Mỗi checkpoint ghi **Kỳ vọng ↔ Thực tế** + ảnh (như TestComplete / Playwright trace).
- Phần không tự động được và không viết thành bước rõ ràng → **charter khám phá** 10–15 phút, ghi chú phát hiện.

### ⑤ Kết quả & lỗi – tự soạn
- Báo cáo theo **dòng bảng**: Đạt / Lỗi, kỳ vọng – thực tế, ảnh.
- Dòng Lỗi → **tự soạn lỗi**: bước tái hiện = *Cho + Khi*, kỳ vọng = *Thì*, thực tế = giá trị bộ test đọc được, hồ sơ, ảnh.

### ⑥ Ghi ACS + học lại
- Nội dung test gửi ACS soạn từ bảng (giữ quy trình ghi ACS hiện có: Đạt / Không đạt, Save, merge Mức 1).
- **Dọn dữ liệu**: trả các hồ sơ về snapshot ở ③.
- **Học lại**: bảng (khuôn, không mã SV) lưu vào KB `Cach-test/` để case cùng dạng dùng lại (như `ma_tran` hiện có).

---

## 4. Định dạng phiếu test (file `.md` / `.json` – Claude ở đâu cũng đưa vào app được)

```markdown
# Test case #64781 – Nơi cấp VB trước sáp nhập (DHMOTX)
Môi trường: Edusoft bản test 2026.11L.23 · Menu: Sinh viên / Thẩm tra văn bằng / Xem/sửa thẩm tra văn bằng
Cột: cũ = "Mã nơi cấp VB" · mới = "Mã nơi cấp VB trước SN" · khoá = "Mã SV" · M1 = 0105 · M2 = 0120

## Thay đổi cần kiểm
1. Cập nhật theo file không tự lấy Nơi cấp VB khi có "trước SN"; ô trống = giữ nguyên
2. Đồng bộ tất cả / chưa có không tự điền …

## Kịch bản: Cập nhật theo file không đè cột cũ   (thay đổi 1)
Khi: Cập nhật theo file → điền file theo cột "Khi" → Xem chi tiết → Thực hiện
| Dòng | Hồ sơ | Cho | Khi | Thì |
| A | 75251128TPE1 | cũ != trống; mới = trống | cũ = ; mới = M1 | cũ = trước; mới = M1 |
…
```

- App có nút **"Nhập phiếu test (.md / .json)"** ở bước 2 → Claude trên cloud, Claude Desktop hay người test đều đưa phiếu vào được (giải quyết vấn đề #8).
- Phiếu là văn bản → đọc được, sửa được, lưu được vào KB / đính kèm ACS.

---

## 5. Ai làm gì

| | Việc |
|---|---|
| **Claude** | ① Phân tích, ② thiết kế bảng (chọn kỹ thuật, độ phủ), viết phiếu `.md`; học lại vào KB |
| **Người test** | Duyệt phiếu, đổi dữ liệu nếu cần, làm bước tay khi được nhắc, xác nhận kết luận |
| **Bộ test** | ③ tìm hồ sơ + snapshot, ④ chạy keyword, đọc / so checkpoint, chụp ảnh, ⑤ ghi kỳ vọng ↔ thực tế |
| **App** | Hiển thị phiếu dạng bảng, cổng duyệt, gửi bộ test, báo cáo, soạn lỗi, ghi ACS |

---

## 6. Thay đổi cần làm (theo thứ tự)

| Ưu tiên | Việc | Ghi chú |
|---|---|---|
| **P0** | Sửa lỗi: vào thẳng bước 2 / "soạn lại từ case" không đọc chi tiết case; trùng tên `rtDetail` | **Đã làm** trong PR kèm đề xuất |
| **P1** | Bước 2 = **Phiếu test dạng bảng** (Thay đổi → Kịch bản → dòng Cho/Khi/Thì) thay danh sách bước; **thứ tự chạy = hiển thị** | Phần sinh tự động hiện tại giữ lại làm **gợi ý nháp**, không còn là plan chính |
| **P1** | Nút **Nhập phiếu test (.md/.json)**; MCP `retest_ghi_plan` ghi cùng định dạng | Claude cloud đưa phiếu vào app được |
| **P1** | **Cổng Duyệt** trước khi chạy | |
| **P2** | Bộ test: `find_data:` (tìm hồ sơ theo điều kiện cột có / trống), snapshot + dọn trả lại | Bỏ việc người test tự đi tìm mã SV |
| **P2** | Bộ test: `import:` – tạo file Excel từ cột "Khi" của bảng và chạy Cập nhật theo file | Bước tay lớn nhất của #64781 |
| **P2** | Báo cáo theo dòng bảng + **tự soạn lỗi** từ dòng Lỗi | |
| **P3** | Độ phủ: cảnh báo "thay đổi chưa có dòng test"; thư viện khuôn bảng trong KB | |
| **P3** | Netweb: chạy bằng Playwright, trace làm bằng chứng | |

---

## 7. Áp dụng thử
Làm thử trọn quy trình với **#64781**: Claude viết phiếu `.md` (đã có bảng ở mục 2), người test duyệt, chạy, so sánh với cách làm tay hôm 25/11.
Đo: số mục tay còn lại, số lỗi bắt được, thời gian.

## 8. Cần chốt
1. Đồng ý bỏ "plan dạng danh sách bước" chuyển sang **phiếu dạng bảng Cho / Khi / Thì**?
2. Cổng **Duyệt** bắt buộc cho mọi case, hay chỉ case có thay đổi dữ liệu?
3. Phiếu test lưu ở đâu: chỉ trong app, hay thêm file `.md` đính kèm vào case ACS?
4. Ưu tiên P2 nào trước: `find_data:` (tìm hồ sơ) hay `import:` (tự điền file + cập nhật theo file)?

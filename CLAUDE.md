# AQ Autotest – hướng dẫn cho Claude Code

Console quản lý kịch bản test Edusoft.NET / Netweb của AQTech, chạy trên **localhost**, kèm **bộ test** (Python + pywinauto)
chạy kịch bản thật trên Edusoft ở máy Windows. Người dùng nói tiếng Việt – trả lời tiếng Việt, ngắn gọn.

## Cấu trúc
- `server.py` – server Python **chỉ thư viện chuẩn** (không thêm dependency). Phục vụ `web/index.html`, API dữ liệu,
  ảnh (`/_blob/<id>`) và thao tác thư mục bộ test (`/api/kit/<tool>`: status, send, list_results, read_result,
  read_file, set_kit_dir, install). Chỉ nghe `127.0.0.1`; POST/PUT/PATCH/DELETE phải có header `X-AQ: 1`.
- `web/index.html` – trang console (một file, cũng là bản artifact trên claude.ai). Mã JS nằm trong `<script>` cuối file.
  Các khối `<script type="text/plain" id="kit-…">` là bản nhúng của `kit/*`; server tự nhúng lại khi phục vụ,
  trước khi commit chạy `python tools/embed_kit.py` để file luôn khớp.
- `web/claude-shim.js` – thay `window.claude` của claude.ai: db (Firestore-like: collection/doc/get/set/update/delete/add/
  orderBy/where/limit/onSnapshot), user, assets, downloads, permissions, mcp (`host:aq-autotest` → `/api/kit`).
  Biến `window.AQ_LOCAL` có nghĩa đang chạy localhost.
- `kit/` – bộ test cài trên máy chạy test: `aqrun.py` (chạy kịch bản, `KIT_VERSION` ở đầu file – **tăng mỗi lần sửa kit**),
  `aq-agent.py` (chạy nền quyền admin, nhận file lệnh `aq-autotest-update-run*.json` trong thư mục bộ test / Tải về:
  chuyển ngay vào `lenh-da-xu-ly/` với tên kèm thời gian, xử lý lần lượt – đang chạy thì xếp hàng; không đổi sang tên cố định),
  `cai-dat.bat` (tự xin quyền admin nhưng giữ APPDATA/LOCALAPPDATA/USERPROFILE gốc qua `AQ_USER_*`; chép bộ test vào thư mục cài
  cố định – `thu-muc-cai.txt` từ ô "Thư mục cài bộ test" trên console, trống = `%USERPROFILE%\AQ-Autotest`; cuối chạy
  `aqrun.py --chan-doan` in bảng kiểm tra + `chan-doan.txt`, bản claude.ai hỏi rồi tự khởi động lại Claude app),
  `chay-test.bat`, `quen-mat-khau.bat`, `HUONG-DAN.txt`. Chạy xong `aqrun.py` gói các lượt vừa chạy thành `AQ-ket-qua-<giờ>.zip`
  trong Tải về – cách chạy không cần cầu nối: console tải file lệnh → Agent/`chay-test.bat` chạy → "Nhập kết quả…" chọn file .zip.
  **Desktop ẩn (thử nghiệm)**: `chay-test.bat --thu-desktop-an` tạo desktop `AQTest` (CreateDesktop), chạy `aqrun.py --ben-trong`
  trên đó, thử gõ không cần phím thật (WM_KEYDOWN/WM_CHAR, WM_SETTEXT, ValuePattern), bấm Đăng nhập, chụp PrintWindow → gói
  `AQ-desktop-an-*.zip`. Cửa sổ xem (`hd_viewer`, tkinter) ở màn hình phụ hiện `xem.jpg` do tiến trình con ghép ~1,5 hình/giây (`hd_frame`). Trên desktop ẩn **không** dùng `pkb.send_keys`/`click_input` (phím/chuột thật đi vào màn hình người dùng).
- `data/` – dữ liệu dùng chung, đồng bộ qua git: `scenarios/`, `runs/`, `bugs/`, `runners/`, `releases/`, `releaseItems/`,
  `testPlans/`, `settings/`, `members/` (Danh mục user: tên gọi = tên ở cột Phân công, `modules` = phân hệ phụ trách dạng
  `edusoft:QLSV`, menu mới đưa vào phân công tự giao cho người phụ trách), `assets/` (ảnh). Mỗi bản ghi = `data/<collection>/<doc_id>.json`.
- `local/` – riêng từng máy, **gitignore**: `config.json` (`port`, `kitDir`, `userId`, `userName`), `users/<id>/secrets.json`.
- `aq-console-server.py` – bản server một file: tải zip repo (nhánh `branch`, token chỉ-đọc) về `aq-console/app`, chạy
  `server.py --public` (bắt đăng nhập, tài khoản ở `<local>/auth.json`, trang `/login`, `/quan-tri`; tắt `/api/kit`),
  2 phút kiểm tra commit mới → tự thay, lỗi thì quay lại bản cũ. Code đẩy lên `main` là server tự cập nhật – **giữ `server.py`
  chạy được bằng thư viện chuẩn và qua `py_compile`**. Dữ liệu server ở `aq-console/du-lieu`, không nằm trong git.
  Dưới IIS: `server-iis/` (CAI-DAT.cmd), `--iis` lấy cổng `ASPNETCORE_PORT`, đường dẫn con `ASPNETCORE_APPL_PATH` → `server.py --base`;
  vì vậy trang/shim chỉ dùng URL **tương đối** (`api/…`, `_blob/…`, `login`), không dùng `/api/…`.
- **App AQ Auto Test** (máy cá nhân, `desktop/`, Electron – làm theo mẫu repo `aq-case-widget`): `src/main.js` chạy `server.py`
  bằng Python nhúng (`resources/python`, mã ở `resources/app` do `tools/dong_goi_app.py` chuẩn bị vào `desktop/res/`), dữ liệu ở
  `%APPDATA%\AQ Auto Test\{du-lieu,rieng}`, cửa sổ riêng (đóng = thoát), file tải về vào Downloads; `--smoke` để CI chạy thử.
  App bắt **đăng nhập** (`MODE["auth"]`, tài khoản ở `rieng/auth.json`, mặc định `admin`/`1234`, trang `/quan-tri`), trang nhận
  `window.AQ_AUTH`; vẫn là máy chạy test (có `/api/kit`, khác `--public`). Cập nhật: `src/updater.js` (electron-updater) đọc
  repo **public** `aq-autotest-releases` – không token; trang nhận trạng thái qua `window.aqDesktop` và hiện hộp "Có phiên bản mới".
  **Merge vào `main` = phát hành**: `.github/workflows/release.yml` (Windows) kiểm tra, build Setup/Portable, chạy `--smoke`, tạo
  Release `v<năm>.<tháng>.<run>` ở repo này + repo public (secret `RELEASES_TOKEN`); nhánh khác/PR chạy `kiem-tra.yml` (build thử).
  Trước khi merge chạy `python tools/kiem_tra.py`.
  Dữ liệu console claude.ai (DB artifact + ảnh) **không** tự sang app: chuyển bằng gói `.zip` (`<collection>/<id>.json` + `assets/<id>.<đuôi>`)
  → menu tài khoản **Nhập dữ liệu (.zip)…** (`POST api/data/import`, gộp theo `updatedAt`, chỉ quản trị); **Xuất dữ liệu (.zip)** = `GET api/data/export`.
  App chỉ chép sẵn từ repo các collection mẫu (`DATA_MAU` trong `tools/dong_goi_app.py`), không có lượt chạy/lỗi/ảnh.
  **Cài bộ test tự động** (app/localhost trên Windows): nút "Cài tự động" → `api/kit/auto_setup` chép kit vào thư mục cài (trống =
  `%USERPROFILE%\AQ-Autotest`) rồi chạy `cai-dat.bat --tu-dong` (không hỏi, không pause, tự xin admin – người dùng chỉ bấm Yes; thiếu
  Python thì winget, không có winget thì tải bộ cài python.org) – tiến độ ghi `cai-dat-trang-thai.txt` (`<bước>|<mã>`, lỗi `loi|<mã>`),
  trang đọc qua `status.setup`. Bước 1 có "Chọn file…" (`aqDesktop.pickFile`) và gợi ý bản HVNG - Copy nếu máy có (`find_edusoft`); bấm Lưu = ghi
  `config.json` của bộ test ngay (`api/kit/save_config`), "Cài tự động" cũng gửi kèm cấu hình.
  **Popup app**: màn hình chờ khi mở (`showSplash` trong `desktop/src/main.js`), hộp cập nhật giữ mở có thanh tiến trình, "Có gì mới"
  sau khi cập nhật (`thay-doi.json` = tên các PR, `dong_goi_app.py` tạo lúc build; `aqDesktop.getInfo` → bản trước), hướng dẫn người mới
  (màn chào mừng 4 bước lần đầu, thẻ "Bắt đầu" trên Tổng quan, menu tài khoản: Hướng dẫn sử dụng / Có gì mới).
- Trang **Test sau sửa lỗi** (`page-retest`, khối JS `RT`, collection `retests/c<caseId>-<lần>`): lấy case coder đã xử lý từ ACS theo
  Query của người dùng → giao máy test (máy chạy thử / máy ảo khai báo ở Máy chạy thử) → chạy kịch bản (script: `kitRunReq`, tay: `startRun`,
  lượt chạy gắn phiếu qua `SC.run.retest` / `rtLink`) → duyệt ảnh từng bước → **Đạt**: điền nội dung test vào case; **Không đạt**: mở lại case,
  gán `tiepnhanadmin`, điền nội dung test lỗi. Kết nối ACS "cách 2" như app `aq-case-widget`: `desktop/src/acs.js` mở cửa sổ ACS (partition
  `persist:acs`), người dùng tự đăng nhập, app gọi API cùng phiên (`/auth/me`, `/cs/lookups`, `/cs/query`…) qua `aqDesktop.acs.call`
  (chỉ đường dẫn `/auth/me`, `/cs/…`). Cách ghi kết quả (`settings/acs.write`: method, path `{id}`, tên trường, giá trị) và đường dẫn Query đã lưu
  (`settings/acs.queriesPath`) cấu hình ở tab Thiết lập ACS, có **Khảo sát ACS** ghi lại lời gọi khi người dùng tự thao tác; chỉ ghi thẳng lên ACS
  khi `write.verified` (chưa xác nhận thì chép nội dung + mở case để dán tay). Bản claude.ai/không có app: chỉ xem phiếu.
  **Query của tôi** (`rtNormQ`): nhận người tạo từ các trường `RT_QOWN` (owner, created_by…), cờ `mine/is_owner`, nhóm `mine`/`shared` trong
  phản hồi, đường dẫn dò dạng `…/mine` trả ít hơn, hoặc thử `?mine=true|scope=mine|owner=me` – so với `RT.users` + `/auth/me`. Thanh Query chỉ hiện
  **tối đa 5** (`RT_QMAX`, `rtShownQ`): Query ghim (☆, localStorage `aq-rt-qpin:<user>`) trước, còn lại tự chọn theo `rtQScore` (của tôi, có tên tôi,
  tester_raw/test_state, "Đã xử lý"); Query đang chọn luôn có mặt; còn lại ở nút "Query khác" (tìm + nhóm Của tôi / Chia sẻ / Dựng sẵn).
  Danh sách case (`rtCaseList`): ô lọc, sắp xếp (mới xử lý / hạn gần / mã), nhóm theo trạng thái ACS (Đã xử lý trước), dòng gọn `rtTicket`, 40 dòng rồi "Xem thêm".
  Cột phải **chi tiết case** (`rtDetailPane`, chọn ở mục "Case đang test" / hàng đợi máy / Vừa kết luận – `RT.sel`): 1 Yêu cầu KH (đọc
  `GET ACS.casePath` – mặc định dò `/cs/cases/{id}`, lấy trường `RT_REQK`/dài nhất, chọn được trường khác, lưu vào phiếu `request`), 2 Phiên bản
  Edusoft của máy test (`runners.check.version`, cảnh báo nếu ghi nhận trước khi coder xử lý xong), 3 Plan test (bước kịch bản, đổi kịch bản khi
  chờ chạy), 4 Kết quả (trạng thái, ảnh, kết luận, nút Chạy / Duyệt ảnh).
- Trang **Màn hình Edusoft** (`page-screens`, khối JS `MH`): tra menu → lưới → cột/ô/nút từ `web/edusoft-catalog.json` và kiểm tra
  lệnh `auto` của kịch bản; sinh lại bằng `tools/lap_danh_muc.py <aqdata> --lien-ket … --truong … --ra .claude/skills/giaodien-edusoft/man-hinh --json web/edusoft-catalog.json`.
  Phần vẽ tay của form (ô lọc, nút, **ràng buộc**: ô bắt buộc / điều kiện chặn + câu báo) ghép từ bản trích source:
  `tools/gan_form_tay.py <trich-tat-ca.zip>` (chạy sau `lap_danh_muc.py`); ô bắt buộc (*) + độ dài tối đa của lưới dựng từ CSDL:
  `tools/gan_bat_buoc.py <aqdata>` (AQFileField.AllowNull = 0). Nghiệp vụ từng phân hệ: skill `tailieu-edusoft/nghiep-vu/`.
  Bản claude.ai publish kèm file này (`files: {"edusoft-catalog.json": "web/edusoft-catalog.json"}`).
- `.claude/skills/tailieu-edusoft/` – kiến thức nghiệp vụ: tài liệu Edusoft, cách dựng kịch bản, schema dữ liệu, release.
- `.claude/skills/giaodien-edusoft/` – sổ tay nhận diện giao diện Edusoft (button, ô tìm kiếm, lưới…) do người dùng dạy;
  đọc trước khi viết/sửa `auto`, ghi thêm mỗi khi người dùng dạy.

## Đồng bộ sau mỗi thay đổi (người dùng yêu cầu)
- Mỗi lần sửa: commit + push nhánh đang làm **và** cập nhật console trên claude.ai
  (artifact https://claude.ai/artifact/7pKLZXYm4eqELvrqs8P6QG). Dữ liệu sửa tay cũng làm cả hai nơi: `data/` và DB của artifact (ArtifactData).
- Bản claude.ai là biến thể của `web/index.html`: có cầu nối Claude app (khối `kit-mcp`, `aqrun.py` tự **đăng ký** cầu nối,
  ảnh ở `/_blob/`), còn bản repo/localhost gỡ cầu nối. Bản claude.ai lưu ở `web/console-claudeai.html`; cập nhật bằng gộp ba chiều
  `git merge-file web/console-claudeai.html <index.html cũ> web/index.html`, giữ phần cầu nối và `/_blob/`, rồi publish file đó lên artifact.

## Chạy & kiểm tra
- Chạy console: `python server.py` (hoặc `chay-console.bat`) → http://localhost:8787. `--port`, `--no-browser`.
- Kiểm tra: `python tools/kiem_tra.py` (cú pháp Python, `node --check` JS trang, kit đã nhúng, có danh mục màn hình).
- Đồng bộ 2 máy: `dong-bo.bat` (commit tất cả → `git pull --rebase --autostash` → `git push`). Gặp xung đột trong
  `data/*.json`: giữ bản có `updatedAt` mới hơn, hoặc gộp trường nếu hai máy sửa trường khác nhau.

## Kịch bản chạy bằng script
- Kịch bản có `scriptReady: true` (và CHUNG-001) mới hiện ở mục "Kịch bản chạy bằng script" trên trang Máy chạy thử.
- `vars` – biến dùng trong bước, vd `{"MSSV": "AUTO{ddHHMM}"}` (có sẵn `{ddHHMM}`, `{yymmdd}`, `{HHMMSS}`, `{ddmmyyyy}`).
- `auto[i]` – danh sách lệnh cho bước i (xem docstring `Run.do_actions` trong `kit/aqrun.py`): `menu:`, `click:`, `type:`,
  `select:`, `choose:`, `cell:`, `cellbtn:`, `close:`, `date:`, `save:`, `expect:`, `expect_dialog:`, `find_row:`, `delete_row:`, `cancel`, `dump:`, `key:`, `wait:`,
  `unique:` (giá trị test có sẵn thì tự đổi), `pick:` (chọn ngẫu nhiên một dòng danh mục, ghi vào biến), `absent:`, `shot:`;
  lệnh tìm dòng (`find_row`/`delete_row`/`unique`/`absent`) ghi cột sau `@` để gõ vào ô tìm kiếm (dòng lọc) của cột đó;
  ô tra cứu phải **chọn** dòng trong danh sách thả xuống: `choose: #Ô = giá trị` (mở rồi chọn) / `select: #Ô = giá trị` (gõ rồi chọn);
  gỡ dòng khỏi lưới con bằng nút riêng `delete_row: {MSSV} @ Mã SV => Xóa sinh viên @ Danh sách sinh viên` (vẫn kiểm mã khi xác nhận,
  không đòi thanh trạng thái – sau đó `save: Lưu`); nhập trên lưới `cell: Cột = giá trị @ Lưới`, nút "…" của ô `cellbtn: Cột @ Lưới`; nút trùng tên ghi vùng `click: Thêm @ Danh sách sinh viên`;
  test xong chức năng nào tắt màn hình đó bằng nút X trên tab: `close: Tên màn hình`;
  thêm `?` sau tên lệnh (vd `select?:`) để bỏ qua khi không thấy phần tử. Nhiều tên thay thế cách nhau `|`.
- Mỗi bước tự mở menu của nó (`menu:`) – có `menu:` trong `auto` thì không mở trước menu chính; quy trình chuẩn thêm–sửa–xóa
  (kiểm tra trùng → thu thập danh mục → thêm → kiểm tra → sửa → xóa) ở skill `tailieu-edusoft`, mẫu QLSV-001.
- Luồng thay thế: `auto`, `needs: "main"` (chỉ chạy khi luồng chính đạt), `always: true`, `after: [lệnh dọn]`.
- Giao diện Edusoft HVNG: ribbon (TabItem "Sinh viên"…) → nút ribbon (vd "Sinh viên học kỳ") → cây "Danh mục chức năng"
  bên trái (TreeItem tên `NodeN`, chữ nằm ở Value) → màn hình mở trong tab MDI. Khi script dừng, nó ghi `ui-*.txt`
  (cây UI Automation) vào thư mục lượt chạy – đọc file đó để sửa tên ô/nút trong `auto`.
- Ô nhập DevExpress: phải gõ phím thật sau khi đặt focus bằng UIA (`set_field`); xóa bằng End + Backspace (Ctrl+A không chạy);
  không dùng Invoke cho nút mở hộp thoại; Edusoft chạy quyền admin nên bộ test phải chạy quyền admin (Agent lo việc này).
- **Không gửi phím Esc** trên màn hình Edusoft: Esc đóng màn hình chức năng, ở cửa sổ chính hỏi "Thoát khỏi chương trình?"
  (kit tự bấm Không). Tìm dòng bằng ô tìm kiếm của cột, không dùng Ctrl+F.
- Kết quả Lưu/Xóa thường hiện ở **thanh trạng thái** dưới đáy (vd "Xóa dữ liệu thành công"), không phải hộp thoại; xóa xong
  lưới có thể chưa nạp lại – `absent:` tự tắt màn hình (X), mở lại menu rồi kiểm tra lần nữa.

## Quy tắc an toàn (bắt buộc)
- Tài khoản test `admindh` chỉ dùng cho môi trường demo/test. **Không** ghi mật khẩu vào `data/`, kịch bản, log hay commit;
  mật khẩu Edusoft nằm trong Windows Credential Manager trên máy chạy test (do `aqrun.py` hỏi), mật khẩu Netweb ở `local/`.
- Không đọc/hiển thị mật khẩu email SMTP trong `client.config` của Edusoft.
- Chỉ thao tác bản Edusoft **test/demo** mà người dùng khai báo ở bước 1 trang Máy chạy thử – **mỗi người/máy một đường dẫn**
  (vd máy gốc `E:\AQ - Works\EDUSOFT_ALL_ENV\EDUSOFT - HVNG - Copy\Edusoft.NET.exe`), không cứng một đường dẫn; không đụng
  môi trường Edusoft thật (production). Dữ liệu test có tiền tố rõ ràng (`AUTO…`, `TEST_…`) và có luồng dọn dữ liệu; xóa chỉ khi hộp
  thoại xác nhận nêu đúng mã dữ liệu test (hoặc danh sách xác nhận xóa "Danh sách đang chọn để xóa" chỉ có dòng mang mã test).
- Hỏi người dùng trước khi thêm thao tác làm thay đổi dữ liệu ngoài phạm vi kịch bản. Không sửa file Excel gốc trừ khi được yêu cầu.
- Source Edusoft trên TFS (`$TFS_URL` = https://portal.aqtech.vn:1443/tfs/AQ, repo Git `Source.NET`, token ở biến môi trường `TFS_TOKEN`,
  quyền Code (Read)): **chỉ đọc** qua REST API (GET) để lấy tên điều khiển, câu thông báo, ràng buộc nghiệp vụ cho `auto`/kịch bản.
  Không push/commit/sửa gì trên TFS; không chép source vào repo này (chỉ ghi tên điều khiển, câu thông báo vào skill `giaodien-edusoft`);
  bỏ qua chuỗi kết nối, mật khẩu, file `*.config`. Không in token ra log/chat; người dùng dán token vào chat thì nhắc thu hồi.
- Gõ phím thật nên chuỗi nhập tránh tổ hợp Telex (dd, aa, s/f/r/x/j sau nguyên âm…) và nhắc tắt Unikey/EVKey khi chạy.

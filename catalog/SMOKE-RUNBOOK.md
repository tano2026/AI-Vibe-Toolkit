# Sổ tay chạy thử cách ly công cụ bên thứ ba

Dành cho NGƯỜI DÙNG (không phải agent). Mục tiêu: kiểm xem các công cụ cần cài trong kho (npm, pip, docker...) có cài và chạy được không, mà không đụng vào máy thật của bạn.

**Luật của kho:** không agent nào được tự cài hay chạy mã bên thứ ba lấy từ internet trên máy người dùng. Bộ chạy `tools/smoke_sandbox.py` được viết để bạn chạy, sau khi bạn đã đọc. Agent chỉ chuẩn bị file và chạy `--dry-run`.

## Đọc trước: rủi ro còn lại

- Cài một công cụ lạ luôn có rủi ro, kể cả trong container. Container giảm thiệt hại (không root, không thấy ổ đĩa máy bạn, giới hạn tài nguyên, giai đoạn chạy thử không có mạng) nhưng KHÔNG chống được mọi thứ: lỗi trong Docker hay nhân hệ điều hành có thể cho mã thoát ra ngoài, và ở giai đoạn cài (có mạng) mã lạ vẫn có thể tải thêm hay gửi dữ liệu trong container đó ra ngoài.
- Bộ chạy đã bỏ hết biến môi trường của máy bạn và chỉ mount một thư mục tạm trống, nên không có khoá hay file của bạn để lấy. Nhưng đừng đặt khoá thật vào bất kỳ lần thử nào.
- Mục nào cần khoá API, trả phí hay có lệnh nguy hiểm (curl | sh, sudo, `--break-system-packages`...) thì bộ chạy luôn bỏ qua. Nếu muốn thử, bạn tự đọc và tự quyết, ngoài phạm vi bộ chạy.
- **Khuyên: không chạy trên máy có dữ liệu nhạy cảm** (khoá, dữ liệu khách, tài khoản đăng nhập sẵn). Tốt nhất dùng một máy phụ, máy ảo hoặc máy chỉ chứa việc thử.
- Kiểm này chỉ chứng minh "cài được và lệnh nhẹ chạy được" (`--help`, `--version`, `npm ls`, `pip show`). Nó KHÔNG chứng minh công cụ làm đúng việc cho khách. Với mục Docker, chỉ kéo image về và kiểm image tồn tại; không chạy container của họ.

## Bước 1. Cài Docker

Bộ chạy từ chối chạy thật nếu không thấy Docker. Không bao giờ chạy thẳng trên máy chủ.

- Windows: cài Docker Desktop (bật WSL2 khi được hỏi), hoặc cài WSL2 rồi cài Docker Engine trong đó. Khởi động Docker Desktop và chờ biểu tượng báo "running".
- macOS: cài Docker Desktop.
- Linux: cài Docker Engine theo hướng dẫn chính thức của bản phân phối.
- Kiểm: mở terminal, gõ `docker version`. Phải thấy cả phần Client và Server. Nếu chỉ thấy Client thì Docker chưa chạy.
- Cần trống ổ đĩa vài GB cho image (một số mục như crawl4ai, vieneu-tts khá nặng).

## Bước 2. Đọc `catalog/smoke-specs.json` và duyệt từng mục

Mỗi mục là một spec. Đọc kỹ các trường sau:

| Trường | Ý nghĩa |
|---|---|
| `lenh_cai` | Lệnh cài trích từ entry gốc (để bạn đọc). Bộ chạy KHÔNG chạy nguyên văn lệnh này mà dịch sang lệnh an toàn hơn (npm có `--ignore-scripts`, pip có `--only-binary=:all:`) |
| `goi`, `buoc_cai`, `image` | Tên gói/image sẽ cài, các bước clone/cài (nếu có), image nền của container |
| `lenh_thu_nhe`, `mau_pass` | Lệnh nhẹ chạy sau khi cài (không mạng) và mẫu đầu ra phải khớp để tính pass |
| `can_mang_khi_cai`, `timeout_giay`, `ram` | Quyền mạng ở giai đoạn cài, giới hạn thời gian và bộ nhớ |
| `can_khoa_api`, `tra_phi`, `co_co_do` | Cần khoá, tốn tiền, lệnh nguy hiểm. Cái nào bật thì mục đó không chạy tự động |
| `ghi_chu` | Chỗ đoán, chỗ chưa kiểm, cảnh báo riêng của mục |
| `trang_thai_duyet` | `chua-duyet` (mặc định), `da-duyet` (bạn tự đổi), `can-nguoi-doc-ky` (luôn bị bỏ qua) |

Cách duyệt:

1. Mở entry gốc của mục (đường dẫn trong `catalog/catalog.json`, trường `duong_dan`) và đọc phần cài đặt cùng phần cảnh báo. Đọc xem tên gói trong spec có đúng là gói bạn muốn chạy (tránh gói nhái tên).
2. Nếu chấp nhận chạy mục đó trong container, sửa tay `"trang_thai_duyet": "chua-duyet"` thành `"da-duyet"`. Chỉ đổi những mục bạn thật sự đã đọc.
3. Mục `can-nguoi-doc-ky` dù bị đổi thành `da-duyet` vẫn bị bỏ qua nếu spec ghi cờ đỏ, cần khoá hay trả phí. Muốn thử thì tự đọc và tự chạy tay ngoài bộ này.
4. Nếu bạn sửa spec (thêm cờ, đổi gói), bộ chạy kiểm lại: tên gói bắt đầu bằng `-`, ký tự shell trong lệnh thử, lệnh thử không "nhẹ" đều bị từ chối.

## Bước 3. Chạy `--dry-run` (an toàn, chỉ in)

```
python tools/smoke_sandbox.py
python tools/smoke_sandbox.py --xem-ca-chua-duyet     # in cả lệnh docker của mục chưa duyệt để bạn đọc
python tools/smoke_sandbox.py --ids repos/markitdown --xem-ca-chua-duyet
```

Mặc định là dry-run: không gọi docker, không gọi mạng, chỉ in kế hoạch. Đọc từng lệnh `docker run` và kiểm các điểm này:

- giai đoạn 1 (cài) có `--network bridge`, giai đoạn 2 (chạy thử) có `--network none`
- `--user 1000:1000` (không root), `--cap-drop ALL`, `--read-only`
- chỉ một `--mount` tới thư mục tạm (`...\Temp\smoke-...`), không có thư mục nào của bạn
- chỉ có `-e KEY=VALUE` hằng số, không có biến lấy từ máy bạn
- giới hạn `--cpus`, `--memory`, `--pids-limit`

(Tên thư mục tạm in ra ở dry-run chỉ là ví dụ; khi chạy thật bộ chạy tạo thư mục tạm ngẫu nhiên riêng cho từng mục và xoá sau đó.)

## Bước 4. Chạy thật 3 mục đầu

Chỉ chạy được khi có Docker và bạn thêm CẢ HAI cờ:

```
python tools/smoke_sandbox.py --chay-that --toi-da-doc-spec --limit 3
```

`--toi-da-doc-spec` là lời xác nhận bạn đã đọc `catalog/smoke-specs.json`. `--limit 3` chỉ chạy 3 mục `da-duyet` đầu tiên. Nên bắt đầu với các mục nhẹ như `repos/mcp-use`, `repos/markitdown`, `repos/gsap-skills`. Muốn chọn đích danh: `--ids repos/mcp-use,repos/markitdown`.

Mỗi mục: giai đoạn 1 cài trong container có mạng; giai đoạn 2 chạy lệnh nhẹ trong container khác với `--network none`; sau đó container bị xoá (`--rm` và `docker rm -f` dự phòng) và thư mục tạm bị xoá. Mục Docker: kéo image, kiểm tồn tại, xoá image nếu do lần chạy này kéo về.

Nếu bị treo hay muốn dừng: Ctrl+C, rồi `docker ps -a --filter name=smoke-` để xem còn container sót, xoá bằng `docker rm -f <tên>`.

## Bước 5. Đọc kết quả

Kết quả ghi vào `catalog/smoke/third-party.json` (thư mục `smoke/` được tạo khi chạy). Mỗi dòng có dạng:

```
{"id": "...", "verdict": "pass|fail|bo-qua", "bang_chung": "...", "thoi_gian": 12.3}
```

- `pass`: lệnh nhẹ thoát mã 0 và đầu ra khớp `mau_pass`. Nghĩa là cài và chạy được lệnh nhẹ, chưa phải "dùng tốt".
- `fail`: cài lỗi, hết thời gian, mã thoát khác 0 hoặc đầu ra không khớp. Đọc `bang_chung` (đã rút gọn, đã che giá trị giống khoá). Lỗi hay gặp: gói cần script cài (npm `--ignore-scripts` làm hỏng), gói chỉ có bản nguồn (pip `--only-binary` từ chối), mẫu `mau_pass` đoán sai. Mẫu `mau_pass` là phỏng đoán từ cách các CLI thường in, nên một số `fail` là lỗi của spec chứ không phải của công cụ. Khi đó đọc đầu ra, sửa `mau_pass` hay `lenh_thu_nhe` rồi chạy lại mục đó; đừng bật `cho_phep_script` hay `cho_phep_sdist` khi chưa đọc gói.
- `bo-qua`: không chạy, `bang_chung` ghi lý do (chưa duyệt, cần khoá, có cờ đỏ...).

File kết quả có `spec_sha256`: mã băm của bản spec lúc chạy, để biết kết quả ứng với bản spec nào.

## Bước 6. Đưa kết quả sang catalog

1. Gửi file `catalog/smoke/third-party.json` cho người phụ trách kho (hoặc agent Thủ Kho / người gộp kết quả) để gộp vào `catalog/audit` hay nhãn mục. Việc sửa `catalog.json`, `curation.json` và các file danh mục khác thuộc quy trình gộp của kho, không do bộ chạy này làm.
2. Khi gộp, ghi rõ phương pháp là chạy cách ly bằng Docker, kiểm "cài được và lệnh nhẹ chạy được", không phải dùng thật.

**Vì sao KHÔNG ghi `catalog/USAGE-LOG.md`:** nhật ký sử dụng ghi việc dùng thật một mục trong một dự án hay khách thật (hàm `thu_kho.usage_line` bắt buộc có tên dự án thật và, nếu kết quả là "dùng được", phải ghi tiết kiệm được gì). Chạy cách ly trong container với dữ liệu giả là một phép kiểm khác, nên không được ghi vào đó, nếu không nhật ký sẽ phình ra bằng chứng giả. Khi bạn đã dùng thật một mục trong dự án, bộ chạy in sẵn mẫu lệnh để bạn tự tạo dòng nhật ký:

```
python -c "import sys; sys.path.insert(0,'tools'); import thu_kho; print(thu_kho.usage_line('repos/markitdown', '<dự án thật>', 'dùng được', '<tiết kiệm gì>', ''))"
```

Lệnh chỉ in ra một dòng Markdown; bạn tự dán vào `catalog/USAGE-LOG.md` sau khi thật sự đã dùng.

## Dọn dẹp

- Container: bộ chạy tự xoá. Kiểm bằng `docker ps -a --filter name=smoke-`.
- Image nền (`node:22-bookworm-slim`, `python:3.12-slim`...) được giữ lại để lần sau nhanh; xoá bằng `docker image prune -a` nếu muốn thu hồi ổ đĩa (lệnh này xoá mọi image không dùng, kể cả của việc khác của bạn, nên cân nhắc).
- Thư mục tạm `smoke-*` trong thư mục Temp: bộ chạy tự xoá; nếu sót thì xoá tay.

## Giới hạn cần biết

- Spec là bản nháp do agent lập từ entry gốc. Tên image/gói trong entry có thể đã cũ (ví dụ `frooodle/s-pdf` của Stirling-PDF). Một số lệnh nhẹ và mẫu pass là phỏng đoán.
- 22 spec hiện có là toàn bộ mục chính và dự phòng cần cài trong bộ khởi đầu cộng các mục `cai-duoc-o-day` + `cai-ngay-duoc` + đã đọc entry gốc; kho hiện không có đủ 40 mục như vậy. Mục chỉ là prompt (chép file skill) không có trong danh sách vì không có gì để cài.
- Mục kiểu plugin Claude Code (`/plugin install`), cụm nhiều container (`docker compose`) và dịch vụ cần khoá API không kiểm được trong bộ này; chúng nằm trong danh sách ở trạng thái `can-nguoi-doc-ky` để bạn biết là có và vì sao chưa kiểm.

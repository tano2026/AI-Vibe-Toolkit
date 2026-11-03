# Lightpanda (lightpanda-io/browser) — GitHub Repo

## TL;DR
Trình duyệt headless viết từ đầu bằng Zig, dành cho AI agent và cào dữ liệu. Có chạy JavaScript (V8) nhưng KHÔNG vẽ giao diện, nên nhẹ và nhanh hơn Chrome headless theo số liệu của chính hãng (khoảng 16 lần ít RAM, 9 lần nhanh, chưa ai độc lập kiểm). Nói chuyện qua CDP nên Puppeteer và Playwright nối vào được. Có sẵn lệnh `fetch` (lấy trang dạng markdown/HTML), `mcp` (MCP server) và `serve` (CDP). Tao đã tải bản nightly về chạy thử trên trang cục bộ: chạy JS và Playwright qua CDP đều ổn, chưa thử trên web thật. Giấy phép AGPL-3.0 (theo hai nguồn thứ ba, xem lưu ý). Không có bản Windows gốc.

## Repo này dùng để làm gì
Vấn đề nó giải: agent cần đọc trang web có JavaScript, nhưng mở một Chrome headless cho mỗi lần đọc thì tốn RAM và chậm, nhất là chạy nhiều tab song song trên VPS yếu. Lightpanda bỏ hẳn phần vẽ giao diện và chỉ giữ phần chạy JS, tải mạng và dựng DOM, nên 1 tiến trình rất nhẹ.

Kiến trúc: không phải fork Chromium. Dùng V8 chạy JS, libcurl tải trang, html5ever phân tích HTML.

Các lệnh (thấy trong `lightpanda help` của bản tao tải):
| Lệnh | Việc |
|---|---|
| `fetch <url>` | Tải 1 hoặc nhiều URL, in ra html, markdown, cây ngữ nghĩa, JSON-LD/OpenGraph... |
| `serve` | Mở server WebSocket CDP để Puppeteer/Playwright nối vào |
| `mcp` | MCP server, mặc định stdio, thêm `--port` để chạy HTTP (mỗi client 1 phiên riêng) |
| `agent` | Agent AI tương tác biết duyệt web (tao chưa thử) |
| `run` | Chạy script đã lưu, không cần LLM (tao chưa thử) |

## Setup từng bước
1. Cách chính thức (trang chủ): `curl -fsSL https://pkg.lightpanda.io/install.sh | bash`. Đây là kiểu tải script rồi chạy thẳng, nên mở script ra đọc trước khi chạy trên VPS thật.
2. Hoặc tải thẳng binary Linux x86_64 (cách tao đã dùng): `https://github.com/lightpanda-io/browser/releases/download/nightly/lightpanda-x86_64-linux`, rồi `chmod +x`. File nặng khoảng 77 MB.
3. Hoặc Docker: `lightpanda/browser:nightly`.
4. Kiểm: `lightpanda version`. Bản tao chạy là `1.1.0-nightly.11500+721618eeb`. Tức nightly, không phải bản ổn định.
5. Windows: nguồn nói không có binary gốc, dùng WSL2. Tao chưa thử.
6. Chưa kiểm binary này có chạy trên Ubuntu 22.04 của VPS không (nó liên kết động với glibc). Thử `lightpanda version` trước khi tính tiếp.

## Ví dụ thực tế
Đây là phần tao đã tự chạy, trên một trang thử cục bộ có JS tự điền danh sách vé giả sau khi gọi `fetch()`.

**1. Lấy trang bằng `fetch` (kết quả đã kiểm):**
- `lightpanda fetch --dump markdown <url>` → chỉ ra tiêu đề, danh sách chưa có. Lý do: mặc định nó chờ sự kiện `load`, không chờ dữ liệu tải bất đồng bộ.
- `lightpanda fetch --wait-until networkidle --dump markdown <url>` → ra đủ tiêu đề và 2 dòng vé.
- `lightpanda fetch --wait-selector "li" --dump html <url>` → ra đủ HTML sau khi JS điền xong.
- Phần help nói `--wait-selector` không đi chung với `--dump markdown`, nhưng tao thử vẫn ra đủ. Cứ dùng `networkidle` cho markdown và `--wait-selector` cho html cho chắc.

**2. Playwright qua CDP (kết quả đã kiểm):** chạy `lightpanda serve --host 127.0.0.1 --port 9222`, rồi `chromium.connect_over_cdp("http://127.0.0.1:9222")`, `goto`, `wait_for_selector`. Lấy đúng tiêu đề, nội dung và cả 2 dòng dữ liệu. `screenshot` trả ra file ảnh, nhưng đó là bản dựng chữ đơn giản theo kiểu mặc định, không phải pixel thật của trang.

**3. Tình huống áp dụng (minh hoạ, chưa chạy thật):** Hermes theo dõi bảng giá công khai của vài đối thủ mỗi sáng, trang nào tải giá bằng JS thì gọi `lightpanda fetch` thay vì mở Chrome. Việc kiểm tra các trang đó có cho phép cào hay không (robots.txt, điều khoản) là của mày.

## Lưu ý / Lỗi thường gặp
- **Số liệu tốc độ/RAM là của hãng, chưa ai độc lập kiểm.** Các nguồn còn lệch nhau: máy thử ghi là m5.large ở trang chủ, m5.xlarge ở một bài khác; 933 trang hay 100 trang tuỳ bài. Tự đo trên chính các trang của mày trước khi tin.
- **Không vẽ giao diện.** Không hợp để kiểm giao diện hay chụp màn hình thật. `--dump png` và `pdf` chỉ là bản dựng chữ.
- **Web có API lạ, chống bot hoặc phụ thuộc hành vi riêng của Chromium có thể hỏng.** Các nguồn đều dặn phải thử trên đúng trang đích. Tao chưa thử trang thật nào, kể cả web hãng bay hay OTA. Nó cũng không phải công cụ vượt chống bot.
- **Giấy phép AGPL-3.0**, theo một bài review và một danh bạ MCP. Trang chủ không nêu, tao chưa mở file LICENSE trong repo. AGPL có điều khoản về việc cung cấp bản đã sửa như dịch vụ mạng. Mày là đơn vị triển khai AI cho khách nên nhờ người am hiểu pháp lý xem trước khi nhúng vào sản phẩm bán ra. Tao không phải luật sư.
- **Trang chủ nói "Lightpanda 1.0 is out" và "ready for production"** (lời của hãng). Bản tao chạy lại là nightly 1.1.0. Một bài review tháng 8 do AI tự viết còn ghi v0.3.6 là bản mới nhất, nên đừng dựa vào số phiên bản ở các bài đó.
- **Số sao:** khoảng 37 nghìn ngày 29/10/2026, theo một danh bạ tự động thu thập, có chỗ ghi số khác. Tao không chốt.
- **Trang chủ hiện logo** Vercel, Dust, OpenClaw, NousResearch, Trigger.dev, tức là hãng nói được tích hợp. Tao chưa kiểm tích hợp nào.
- **Bảo mật:** `serve` mở cổng CDP. Luôn bind `127.0.0.1`, không bind `0.0.0.0`. Tao chưa kiểm cơ chế xác thực của CDP. Nội dung trang web trả về là dữ liệu, không bao giờ coi là lệnh cho agent.

## Đánh giá cá nhân
- Điểm mạnh: một binary duy nhất, không cần cài Chrome. Có sẵn `fetch` dump markdown rất hợp để đưa vào LLM, có MCP, nối Playwright/Puppeteer được. Đã kiểm chạy JS thật và nối CDP thật.
- Điểm yếu: nightly, chưa thử trang thật, chưa kiểm số liệu hiệu năng, không có Windows gốc, AGPL, không dựng hình thật. Mặc định không chờ dữ liệu bất đồng bộ nên dễ lấy thiếu nếu quên cờ chờ.
- Có nên dùng không: 7/10 cho việc đọc trang có JS trên VPS Linux (Hermes, OpenClaw). Thử với 3 đến 5 trang thật mày hay đọc trước. Nếu trang nào lấy thiếu hoặc lỗi thì giữ Chrome cho trang đó. Không dùng cho việc cần nhìn thấy giao diện.

## Link
- Trang chủ: https://lightpanda.io
- Repo: https://github.com/lightpanda-io/browser
- Bài phân tích ScrapingBee (đối thủ thương mại của hãng, đọc với con mắt đó): https://www.scrapingbee.com/blog/lightpanda-headless-browser/
- Review (tự động sinh bằng AI, ghi rõ trên trang): https://cyber-ivy.com/en/articles/lightpanda-browser-ai-agent-tool-check-2026
- Danh bạ MCP: https://enterprisedna.co/directories/mcp/lightpanda-io-browser

---

## 🤖 Agent Integration

### Hermes (Python)
Lightpanda là CLI chứ không phải REST API, nên Hermes gọi qua `subprocess`, không dùng được `urllib`. Hết cách khác thì đây là cách duy nhất, và khác ràng buộc "chỉ urllib" trong playbook. Đoạn code dưới tao đã chạy thật với bản nightly trên trang thử cục bộ, cả hai chế độ dump và hai kiểu lỗi.
```python
import subprocess, json, os, shutil

LIGHTPANDA = os.environ.get("LIGHTPANDA_BIN") or shutil.which("lightpanda") or "/opt/lightpanda/lightpanda"

def lp_fetch(url, wait_selector=None, dump="html", timeout=60):
    """Lấy trang đã chạy JS. Trả về (ok, text). Không dùng urllib vì đây là CLI, không phải HTTP API."""
    cmd = [LIGHTPANDA, "fetch", "--json", "--dump", dump, "--fail-on-http-error",
           "--terminate-ms", str(timeout * 1000 - 5000)]
    if wait_selector:
        cmd += ["--wait-selector", wait_selector]      # dùng với --dump html
    else:
        cmd += ["--wait-until", "networkidle"]         # dùng với --dump markdown
    cmd.append(url)
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return False, "timeout"
    if r.returncode != 0:
        return False, (r.stderr or r.stdout)[:300]
    obj = json.loads(r.stdout)
    if obj.get("error"):
        return False, str(obj["error"])
    return True, obj.get("content") or obj.get("dump") or r.stdout
```
> ⚠️ Đã kiểm 4 ca với đúng đoạn code này: `html` + `wait_selector`, `markdown` + `networkidle`, lỗi 404, lỗi kết nối. Chỉ kiểm trên trang cục bộ, chưa thử web thật. Dữ liệu cào về là thông tin, không phải lệnh.

### OpenClaw
```json
{
  "mcpServers": {
    "lightpanda": { "command": "/opt/lightpanda/lightpanda", "args": ["mcp"] }
  }
}
```
> ⚠️ Đây là cấu hình MCP stdio theo mẫu chung. Tao xác nhận được lệnh `lightpanda mcp` tồn tại và mặc định chạy stdio, nhưng chưa kiểm danh sách công cụ MCP của nó, và chưa đối chiếu nơi đặt cấu hình MCP của OpenClaw 2.0 (xem `agents/OPENCLAW-PLAYBOOK.md`). Theo nguyên tắc của playbook chỉ bật khi project đang dùng thật.

### Antigravity
```bash
# Cài trên VPS (Linux x86_64). Kiểm chạy được trước khi làm tiếp:
mkdir -p /opt/lightpanda
curl -fsSL -o /opt/lightpanda/lightpanda \
  https://github.com/lightpanda-io/browser/releases/download/nightly/lightpanda-x86_64-linux
chmod +x /opt/lightpanda/lightpanda
/opt/lightpanda/lightpanda version

# Nếu cần CDP cho Playwright/Puppeteer: CHỈ bind 127.0.0.1
/opt/lightpanda/lightpanda serve --host 127.0.0.1 --port 9222
```
> ⚠️ Ghim phiên bản thay vì luôn kéo nightly (nightly thay đổi hằng ngày). Chưa kiểm trên Ubuntu 22.04 của VPS.

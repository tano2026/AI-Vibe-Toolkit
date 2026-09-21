# Browser Harness — GitHub Repo

## TL;DR
Của team Browser Use (cùng team làm `browser-use` nổi tiếng) — nối thẳng 1 LLM vào trình duyệt Chrome thật qua 1 websocket CDP duy nhất, không qua lớp trung gian nào. Điểm khác biệt: agent **tự viết code helper còn thiếu ngay trong lúc chạy** (self-healing) — task lần sau gặp lại tình huống tương tự sẽ nhanh hơn vì code đã có sẵn từ lần trước. Chỉ ~592 dòng Python, cực nhẹ.

## Repo này dùng để làm gì
Khác Playwright/Selenium (viết code cố định trước), và khác Skyvern (dùng Vision LLM để "nhìn" trang) — Browser Harness cho agent quyền tự do hoàn toàn trên browser thật, khi thiếu 1 helper function nào đó (vd "upload file"), agent tự viết ngay function đó vào `agent-workspace/agent_helpers.py`, lưu lại dùng cho task sau. Harness ngày càng "khoẻ" hơn qua mỗi lần chạy — đúng nghĩa "tự chữa lành" (self-healing) thay vì lặp lại lỗi cũ.

## Setup từng bước
1. Cách nhanh nhất — dán prompt này vào Claude Code hoặc Codex, để chính coding agent tự cài hộ:
   ```
   Set up https://github.com/browser-use/browser-harness for me.
   Read install.md first to install and connect this repo to my real browser.
   Then read SKILL.md for normal usage.
   ```
2. Cài thủ công (yêu cầu Python 3.12, khuyến nghị dùng `uv`):
   ```bash
   git clone https://github.com/browser-use/browser-harness.git
   cd browser-harness
   uv sync
   ```
3. Đăng ký skill và kết nối vào trình duyệt thật đang mở: agent sẽ tự mở `chrome://inspect/#remote-debugging`, tick checkbox cho phép kết nối remote debugging.
4. Đọc `install.md` nếu setup/connect thất bại (có hướng dẫn xử lý lỗi kết nối chi tiết).
5. Dùng thường ngày: đọc `SKILL.md` — mọi chỉnh sửa task cụ thể nằm ở `agent-workspace/agent_helpers.py` và `agent-workspace/domain-skills/` (đây là 2 file agent được phép tự sửa, phần lõi `src/browser_harness/` được bảo vệ, agent không đụng vào).
6. Không muốn chạy browser trên máy mình (tốn RAM/CPU, không parallel) — dùng **Browser Use Cloud**: free tier 3 browser chạy song song, có proxy + giải CAPTCHA sẵn, không cần thẻ tín dụng.

## Ví dụ thực tế
Giao cho agent việc tự động điền form đặt vé/đăng ký trên site chưa từng tự động hoá trước đây (vd site đại lý ABTRIP hay dùng) — lần đầu agent gặp bước "upload chứng từ" chưa có sẵn helper, nó tự viết function upload file ngay trong lúc chạy, lưu vào `agent_helpers.py`; lần sau gặp lại bước tương tự (dù ở site khác có cùng pattern), agent dùng lại helper đã viết, nhanh hơn hẳn lần đầu.

## Lưu ý / Lỗi thường gặp
- Có **2 repo cùng tên "browser-harness"** dễ nhầm: bản chính chủ tổ chức **`browser-use/browser-harness`** (17.9k star, MIT) và bản `dwnmf/browser-harness` (có vẻ là bản gốc/fork độc lập trước khi vào tổ chức browser-use, mô tả gần giống hệt) — ưu tiên theo dõi bản `browser-use/browser-harness` vì đứng sau tổ chức lớn, cập nhật đều.
- Chạy trên máy cá nhân thì **1 browser/1 máy, không parallel** — muốn scrape/automation nhiều site cùng lúc bắt buộc phải dùng Browser Use Cloud hoặc tự dựng nhiều máy, không có cách nào chạy song song trên 1 máy với setup mặc định.
- Agent được cấp quyền **tự viết code** vào `agent_helpers.py` — đây vừa là điểm mạnh (tự học) vừa là rủi ro cần để ý: nên review code agent tự viết định kỳ, không để chạy hoàn toàn không giám sát trên tác vụ nhạy cảm (đăng nhập, thanh toán).
- Không có cơ chế "nhìn hiểu" trang như Skyvern (Vision LLM) — Browser Harness dựa vào DOM/CDP thuần, nên với trang web cực kỳ phức tạp về layout, đôi khi vẫn cần agent tự dò nhiều lần mới ra helper đúng.

## Đánh giá cá nhân
- **Điểm mạnh:** Ý tưởng "self-healing" (agent tự vá lỗ hổng code của chính nó) rất thực tế và tiết kiệm thời gian về dài hạn — không phải viết lại từ đầu mỗi lần gặp pattern mới. Codebase cực nhẹ (~592 dòng), dễ đọc hiểu toàn bộ nếu cần tự audit. Có sẵn cloud free tier để test không tốn máy cá nhân.
- **Điểm yếu:** Quyền tự viết code của agent là con dao 2 lưỡi, cần review định kỳ. Không có lớp "hiểu ý nghĩa trang" bằng Vision như Skyvern nên với web đổi layout mạnh vẫn có thể vấp, phải để agent tự học lại.
- **Có nên dùng không:** 8/10 cho automation trình duyệt lặp đi lặp lại nhiều loại task khác nhau (điểm mạnh nhất là "học" qua từng lần chạy) — nếu chỉ cần automation 1 task cố định 1 lần, Playwright/Selenium viết tay vẫn đơn giản hơn.

## Link
- Repo: https://github.com/browser-use/browser-harness
- Docs/Demo: https://github.com/browser-use/browser-harness/blob/main/install.md · https://browser-use.com

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Cài: git clone + uv sync (xem phần Setup)
# Harness expose Python API trực tiếp qua CDP, không phải REST API độc lập
from browser_harness import BrowserSession   # tên module tham khảo, kiểm tra lại theo version thật

async def run_browser_task(task_description: str):
    session = BrowserSession()
    await session.connect()   # nối vào Chrome đang bật remote debugging
    result = await session.run(task_description)
    return result
```
> ⚠️ Cần Chrome đã bật `chrome://inspect/#remote-debugging` từ trước — không tự động bật hộ nếu chạy headless trên VPS không có Chrome cài sẵn.

### OpenClaw
Không có MCP/connector sẵn — nếu OpenClaw (Node.js) cần dùng, gọi qua subprocess CLI hoặc dựng 1 service Python nhỏ bọc quanh `browser_harness`, expose lại qua HTTP endpoint để OpenClaw gọi.

### Antigravity
```bash
# Deploy trên VPS — cần Chrome/Chromium cài sẵn hoặc dùng Browser Use Cloud thay vì browser local
git clone https://github.com/browser-use/browser-harness.git
cd browser-harness
uv sync
```
> ⚠️ VPS không có GUI thì Chrome phải chạy headless — cân nhắc dùng Browser Use Cloud (free tier 3 browser song song) thay vì tự quản lý Chrome headless trên VPS, đỡ phải lo RAM/CPU và không parallel được.

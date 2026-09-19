# Skyvern — GitHub Repo

## TL;DR
Tự động hoá trình duyệt bằng Vision LLM + computer vision thay vì XPath/DOM parsing truyền thống — nghĩa là script không vỡ mỗi khi website đổi layout. SDK tương thích Playwright, kèm no-code workflow builder cho người không biết code.

## Repo này dùng để làm gì
Automation trình duyệt kiểu cũ (Selenium/Playwright thuần) phải viết XPath cụ thể cho từng website, đổi layout là vỡ script. Skyvern cho AI "nhìn" trang web như người thật nhìn (qua Vision LLM) rồi tự quyết định click vào đâu, điền gì — nên hoạt động được cả trên website chưa từng thấy. Mạnh nhất ở "WRITE tasks" (điền form, đăng nhập, tải file) — nhóm việc RPA (Robotic Process Automation) truyền thống hay dùng.

## Setup từng bước
1. Cài Docker Desktop (bản self-host chạy qua Docker).
2. Cài SDK Python:
   ```bash
   pip install skyvern
   ```
   hoặc Playwright-compatible SDK cho Node/TS.
3. Chạy task đơn giản (Python):
   ```python
   from skyvern import Skyvern

   skyvern = Skyvern()
   task = await skyvern.run_task(prompt="Tìm bài viết top trên Hacker News hôm nay")
   print(task)
   ```
4. Muốn AI điều khiển đúng Chrome đang dùng thật (giữ cookie/login sẵn có) — bật remote debugging: mở `chrome://inspect/#remote-debugging`, bấm Enable (hoặc chạy `skyvern init browser` để tự làm hộ), rồi trỏ Skyvern vào browser đó.
5. Cách dùng kiểu Playwright (TypeScript):
   ```ts
   await page.agent.login("skyvern", { credentialId: "cred_123" });        // AI login
   await page.click({ prompt: "Add first item to cart" });                  // AI-augmented click
   await page.agent.runTask("Complete checkout with: John Snow, 12345");    // AI task
   ```
6. Không muốn tự quản hạ tầng — dùng Skyvern Cloud (bản quản lý sẵn, có anti-bot detection, proxy network, giải CAPTCHA — hiện đang private beta, cần liên hệ để dùng).

## Ví dụ thực tế
Tự động điền form booking/checkout cho ABTRIP hoặc kiểm tra giá vé trên nhiều site đại lý khác nhau mà không cần viết XPath riêng cho từng site — chỉ cần mô tả bằng tiếng thường ("điền thông tin khách X, chọn ngày Y, bấm đặt") và Skyvern tự nhìn trang mà làm, kể cả khi site đổi giao diện.

## Lưu ý / Lỗi thường gặp
- Từ Chrome 136, Chrome chặn kết nối CDP (remote debugging) vào `user_data_dir` mặc định — Skyvern tự copy `user_data_dir` sang `./tmp/user_data_dir` lần đầu kết nối để né lỗi này, không phải bug, là cơ chế xử lý sẵn.
- Vision LLM + computer vision tốn tài nguyên/API hơn script XPath truyền thống — không hợp cho task lặp lại hàng nghìn lần trên 1 website ổn định (lúc đó viết script cứng vẫn rẻ hơn); Skyvern hợp nhất khi website hay đổi hoặc chưa từng gặp.
- Skyvern Cloud (bản quản lý, có giải CAPTCHA/proxy) đang **private beta**, phải liên hệ qua email mới dùng được, không tự đăng ký online ngay.
- Nhiều fork/mirror trùng tên trên GitHub (litertiger, sfast, jfontestad, bhardwajRahul...) — bản chính chủ là **Skyvern-AI/skyvern**.

## Đánh giá cá nhân
- **Điểm mạnh:** Giải quyết đúng điểm yếu lớn nhất của automation truyền thống (vỡ khi web đổi layout) bằng Vision LLM, tương thích Playwright nên dev quen Playwright chuyển sang nhanh, có cả lớp no-code cho người không biết code.
- **Điểm yếu:** Tốn chi phí/API hơn hẳn XPath thuần cho việc lặp lại ổn định, bản Cloud (tiện nhất, có giải CAPTCHA) vẫn đang private beta chưa mở rộng công khai.
- **Có nên dùng không:** 8/10 cho automation trên website hay đổi hoặc nhiều site khác nhau (đúng bài cho RPA đại lý du lịch, kiểm tra giá nhiều site) — 5/10 nếu chỉ cần automation 1 website cố định, ổn định lâu dài (Playwright/Selenium thuần vẫn rẻ hơn).

## Link
- Repo: https://github.com/Skyvern-AI/skyvern
- Docs/Demo: https://www.skyvern.com

---

## 🤖 Agent Integration

### Hermes (Python)
```python
from skyvern import Skyvern

skyvern = Skyvern()  # cần bản self-host chạy qua Docker hoặc Skyvern Cloud

async def run_web_task(prompt: str):
    task = await skyvern.run_task(prompt=prompt)
    return task
```
> ⚠️ Nếu muốn dùng browser thật đang có sẵn cookie/login, phải bật remote debugging trước (`skyvern init browser` tự làm hộ) — không thì Skyvern mở browser trắng, mất hết session cũ.

### OpenClaw
Không có MCP/connector sẵn — nếu OpenClaw (Node.js) cần dùng, dùng bản SDK Playwright-compatible (TypeScript) trực tiếp, gọi `page.agent.runTask(...)` như ví dụ trong phần Setup.

### Antigravity
```bash
# Deploy bản self-host qua Docker trên VPS
git clone https://github.com/Skyvern-AI/skyvern.git
cd skyvern
docker compose up -d
```
> ⚠️ Cần cấu hình API key model (Vision LLM) trong `.env` trước khi chạy — không có key thì task tự động chạy được vẫn thất bại ở bước "nhìn" trang web.

# browser-use — AI agent điều khiển browser như người thật, 95k stars

**GitHub:** https://github.com/browser-use/browser-use
**Stars:** 95k+ | **License:** MIT
**Tác giả:** browser-use team (YC W25)
**Language:** Python | **MCP:** Có sẵn

---

## Vấn đề nó giải quyết

Selenium và Playwright viết automation bằng CSS selector và XPath — chính xác nhưng cực kỳ giòn. Website đổi tên class là script gãy. Thêm field vào form là test fail.

browser-use thay cách tiếp cận: thay vì script từng bước cứng nhắc, mày **mô tả task bằng ngôn ngữ tự nhiên** — AI tự tìm cách thực thi trên bất kỳ website nào, kể cả website nó chưa từng thấy.

```python
agent = Agent(
    task="Tìm vé máy bay Hà Nội → TP.HCM ngày mai rẻ nhất, chụp screenshot kết quả",
    llm=ChatAnthropic(model="claude-opus-4-6"),
)
await agent.run()
```

---

## Tại sao 95k stars

Timing hoàn hảo: ra mắt đúng lúc "AI agent" trở thành từ khóa hot nhất. Nhưng không chỉ là hype — sản phẩm thực sự work:

- **BU 2.0** (Jan 2026): +12% accuracy, 200 tasks/$
- **SOC 2 Type 2** certified (Oct 2025)
- **YC W25** — có backing thực sự
- Community lớn, active development

---

## Cài & Dùng

```bash
pip install browser-use
playwright install
```

**Task đơn giản:**
```python
from browser_use import Agent
from langchain_anthropic import ChatAnthropic
import asyncio

async def main():
    agent = Agent(
        task="Vào Google, search 'AI news today', tóm tắt 3 tin đầu tiên",
        llm=ChatAnthropic(model="claude-sonnet-4-6"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
```

**Với memory và custom actions:**
```python
from browser_use import Agent, Controller
from browser_use.browser import BrowserProfile

agent = Agent(
    task="...",
    llm=llm,
    browser_profile=BrowserProfile(
        headless=False,  # xem browser hoạt động
        allowed_domains=["*.google.com"],  # giới hạn domain
    ),
)
```

---

## Các Tính Năng Chính

**Self-healing automation** — khi website thay đổi layout, agent tự adapt thay vì crash

**Vision-based** — "nhìn" trang web như người dùng, không phụ thuộc DOM structure

**Memory** — nhớ context trong session dài

**MCP server** — tích hợp thẳng vào Claude Code, Cursor

**Multi-LLM** — Claude, GPT, Gemini, model local đều được

---

## Use Cases

- **Research automation**: Đọc nhiều trang web, tổng hợp thông tin
- **Form filling**: Điền form tự động với dữ liệu có sẵn
- **Price monitoring**: Theo dõi giá trên nhiều trang
- **Testing**: E2E test mà không cần viết selector
- **Data collection**: Scrape web app có JavaScript động

---

## Lưu ý Quan Trọng

**Chi phí LLM:** Browser agent gọi LLM nhiều lần per task → tốn token hơn script thông thường. Dùng model rẻ (Claude Haiku, Gemini Flash) cho task đơn giản.

**Tốc độ:** Chậm hơn Playwright thuần ~3-5x vì phải chờ LLM inference.

**Không phải silver bullet:** Website có CAPTCHA, rate limit, hoặc login phức tạp vẫn khó. Dùng cho automation tasks mà scripting truyền thống quá tốn công.

**Bảo mật:** Không để agent access vào tài khoản quan trọng nếu task không rõ ràng.

---

## Đánh Giá Cá Nhân

browser-use là repo đáng watch nhất trong category browser automation 2025-2026. 95k stars không phải hype thuần — codebase active, team có YC backing, roadmap rõ ràng.

Điểm mạnh thực sự là lowering the barrier: trước đây cần biết Playwright/Selenium mới làm được browser automation, giờ chỉ cần viết task description là xong. Với vibe coders đây là game changer.

Nhưng đừng nghĩ nó replace Playwright hoàn toàn. Với task cần precision cao, tốc độ nhanh, hoặc scale lớn — Playwright script vẫn tốt hơn. browser-use ngon nhất cho "one-off automation" và task mà logic phức tạp, website hay thay đổi.

**Rating: 8.5/10** — trừ điểm vì chi phí LLM và tốc độ so với scripting thuần.

---

*Nguồn: github.com/browser-use/browser-use*
*Cập nhật: tháng 6/2026*

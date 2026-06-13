# Script Video #20 — browser-use: Thay Vì Viết Script, Mày Nói Chuyện Với Browser

**Format:** TikTok / YouTube Shorts (~80s)
**Hook type:** Before/After — code cũ vs cách mới
**Style:** Không lộ mặt, demo live browser automation

---

## 🎬 SCRIPT

**[0s - 8s] HOOK**
> "Automation script Selenium của mày gãy lần thứ 5 chỉ vì website đổi tên class CSS. Có cách khác — mày chỉ cần nói với AI mày muốn làm gì."

*[Show: error message Selenium trên terminal]*

**[8s - 22s] VẤN ĐỀ VỚI CÁCH CŨ**
> "Playwright, Selenium — powerful nhưng giòn. Website update layout là script gãy. Mày phải inspect lại, update selector, test lại. Lặp đi lặp lại mãi."

*[Show: CSS selector cũ → website thay đổi → script fail]*

**[22s - 45s] DEMO browser-use**
> "browser-use — 95 nghìn stars, YC W25. Thay vì viết selector, mày mô tả task:"

```python
from browser_use import Agent
from langchain_anthropic import ChatAnthropic

agent = Agent(
    task="Vào trang web này, tìm sản phẩm rẻ nhất dưới 500k, thêm vào giỏ hàng",
    llm=ChatAnthropic(model="claude-sonnet-4-6"),
)
await agent.run()
```

*[Show: browser tự mở, tự navigate, tự click — real demo]*

> "AI nhìn trang web như người dùng — không cần CSS selector, không cần XPath."

**[45s - 62s] USE CASES**
> "Mày dùng được cho:"
> "— Research: đọc 20 trang web, tổng hợp thông tin"
> "— Monitoring: check giá sản phẩm mỗi ngày tự động"
> "— Testing: E2E test mà không viết một dòng selector"

**[62s - 80s] LƯU Ý + CTA**
> "Lưu ý: tốn token LLM hơn script thường — dùng Claude Haiku hoặc Gemini Flash cho task đơn giản để tiết kiệm chi phí."

> "95k stars trong chưa đầy 1 năm. Link GitHub trong bio."

*[Show: github.com/browser-use/browser-use]*

---

## 📝 CAPTION
```
Automation script gãy vì website đổi CSS? Cách này không bao giờ gãy 🤖

browser-use — nói với AI mày muốn làm gì trên browser, nó tự làm

95k ⭐ MIT License YC W25

#automation #python #vibecoding #ai #selenium #playwright #github
```

## 🎯 B-ROLL
1. Selenium error message → contrast với browser-use chạy mượt
2. Browser tự navigate — screenrecord live demo quan trọng nhất
3. Code so sánh: Playwright (nhiều dòng selector) vs browser-use (1 câu task)
4. Stars counter GitHub

---
*Script v1 — tháng 6/2026*

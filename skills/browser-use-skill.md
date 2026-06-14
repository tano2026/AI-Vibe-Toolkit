# browser-use — Skill Dùng Ngay (95k⭐)

**Repo:** github.com/browser-use/browser-use | MIT | YC W25
**Dùng với:** Python, Claude, OpenAI, Gemini

---

## Cài Nhanh

```bash
pip install browser-use playwright
playwright install chromium
export ANTHROPIC_API_KEY="..."
```

## Dùng Như MCP

```json
{
  "mcpServers": {
    "browser-use": {
      "command": "uvx",
      "args": ["browser-use-mcp"]
    }
  }
}
```

## 5 Use Cases Thực Tế

```python
from browser_use import Agent
from langchain_anthropic import ChatAnthropic

agent = Agent(
    task="...",
    llm=ChatAnthropic(model="claude-sonnet-4-5"),
)

# 1. Điền form tự động
agent = Agent(task="Vào gmail.com, compose email tới test@test.com subject 'Hello', body 'Test email'")

# 2. Scrape dữ liệu có auth
agent = Agent(task="Login vào site X với user/pass, lấy danh sách orders tháng này, export ra CSV")

# 3. Research tự động
agent = Agent(task="Search Google 'AI agent frameworks 2026', vào 5 link đầu, tổng hợp key points")

# 4. Monitor & alert
agent = Agent(task="Vào trang pricing của competitor, screenshot, so sánh với lần trước")

# 5. Social media automation
agent = Agent(task="Vào LinkedIn, like + comment 'Great post!' vào 5 posts về AI mới nhất")

import asyncio
asyncio.run(agent.run())
```

## Tips Tiết Kiệm Token

```python
# Dùng model rẻ cho simple browser tasks
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")  # rẻ hơn Claude 10x

# Chỉ dùng Claude cho tasks cần reasoning phức tạp
llm = ChatAnthropic(model="claude-haiku-4-5")  # rẻ nhất của Anthropic
```

## Khi Nào Dùng browser-use vs Playwright/Selenium

| Situation | Dùng gì |
|-----------|---------|
| Task phức tạp, dynamic UI | browser-use |
| Task đơn giản, lặp đi lặp lại | Playwright script |
| Cần speed tối đa | Selenium headless |
| Không biết code | browser-use |

---
*skills/browser-use-skill.md | AI Vibe Toolkit | tháng 6/2026*

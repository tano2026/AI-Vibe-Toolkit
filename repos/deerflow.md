# DeerFlow — Super Agent Harness Của ByteDance (71k⭐)

**GitHub:** https://github.com/bytedance/deer-flow
**Stars:** 71k⭐ | **License:** MIT | **By:** ByteDance
**#1 GitHub Trending** 28/2/2026 sau v2.0
**Stack:** Python 3.12+ + Node.js 22+

---

## Đây Là Gì

Open-source super agent harness — orchestrate sub-agents, memory, sandboxes để làm gần như bất cứ thứ gì. Tasks từ vài phút đến vài tiếng.

Không phải chatbot. Không phải Copilot. AI nhân viên thật sự.

---

## Core Components

### Sub-agents
- Research Agent: tìm kiếm và tổng hợp thông tin
- Code Agent: viết và chạy code trong sandbox
- Create Agent: tạo content, reports, documents

### Memory System
- Short-term: conversation context
- Long-term: persistent knowledge base
- Episodic: past task experiences

### Sandboxes
- Code execution: Python, JS, Shell
- File operations: read, write, transform
- Web browsing: navigate, extract, interact

### Message Gateway
Kết nối với Telegram, Slack, Discord, Email

---

## Cài Đặt

```bash
git clone https://github.com/bytedance/deer-flow
cd deer-flow
cp .env.example .env
# Điền API keys
docker-compose up
```

---

## Use Cases

```bash
# Deep research
"Research AI agent frameworks 2026, so sanh top 10, viet bao cao"

# Code project
"Build Python web scraper for GitHub trending, test, fix bugs"

# Content
"Analyze YouTube channel top 20 videos, suggest 10 video ideas with hooks"
```

---

## DeerFlow v1 vs v2

v1: Deep Research framework (1.x branch)
v2: Ground-up rewrite — super agent harness, không share code v1

---

## Kết Hợp Với Kho

DeerFlow phù hợp cho long-horizon tasks:
- Research sâu nhiều tiếng
- Code + test + iterate tự động
- Multi-source synthesis
- Autonomous execution với sandbox

**Rating: 9/10** — Top tier. Theo dõi skills ecosystem phát triển.

*github.com/bytedance/deer-flow | 71k⭐ | MIT | ByteDance | tháng 6/2026*

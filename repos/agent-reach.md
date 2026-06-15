# Agent-Reach — Cho AI Đọc Twitter/LinkedIn Không Cần API Key (29k⭐)

**GitHub:** https://github.com/Panniantong/Agent-Reach
**Stars:** 29k⭐ | **License:** MIT | **Language:** Python
**Platforms:** Twitter/X · LinkedIn · YouTube · Reddit · Bilibili · và hơn nữa

---

## Đây Là Gì

Cho phép AI agents đọc content từ internet mà **không cần API keys**. Giải quyết bài toán authentication và rate limiting cho web scraping.

---

## Cài & Dùng

```bash
pip install agent-reach
```

```python
from agent_reach import Reach
reach = Reach()

# Twitter/X — không cần $100/tháng API
tweets = reach.twitter("claude code review", limit=50)
user_tweets = reach.twitter_user("@addyosmani", limit=30)

# LinkedIn — không có free API, dùng Agent-Reach
posts = reach.linkedin("AI tools 2026", limit=10)

# YouTube
videos = reach.youtube("vibe coding tutorial", limit=10)
transcript = reach.youtube_transcript("video_id")

# Reddit
posts = reach.reddit("r/MachineLearning", limit=20)
comments = reach.reddit_post("post_url")
```

---

## Workflow Research Cho AI Vibe Toolkit

```python
# Trước khi viết .md về tool mới
reach = Reach()
tool = "hermes-agent"

# Twitter sentiment thật
tweets = reach.twitter(f"{tool} review", limit=50)

# YouTube coverage
videos = reach.youtube(tool, limit=10)

# Reddit discussions
posts = reach.reddit_search(tool, limit=20)

# → Real user opinions, pain points thật
# → Hook video mạnh hơn
```

---

## Đánh Giá: 8.5/10

LinkedIn + Bilibili không có free API → Agent-Reach là giải pháp duy nhất. Tích hợp với last30days skill để research không bỏ sót gì.

---
*github.com/Panniantong/Agent-Reach | 29k⭐ | MIT | tháng 6/2026*

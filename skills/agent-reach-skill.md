# Agent-Reach — Skill Dùng Ngay + Tối Ưu Token

**Repo:** github.com/Panniantong/Agent-Reach | 29k⭐ | MIT
**Cost:** $0 scrape | Chỉ tốn token khi feed vào Claude
**Cập nhật:** tháng 6/2026

---

## Cài

```bash
pip install agent-reach
```

---

## Pattern Chuẩn — Thu Thập Trước, Analyze Sau

```python
from agent_reach import Reach
reach = Reach()

# BƯỚC 1: Thu thập ($0 — không gọi LLM)
tweets = reach.twitter("claude code skills", limit=50)
posts  = reach.reddit("r/LocalLLaMA", limit=30)
videos = reach.youtube("vibe coding tutorial", limit=10)

# BƯỚC 2: Filter trước khi feed vào Claude
# Chỉ lấy signal mạnh — tiết kiệm 80% token
hot_tweets = [t for t in tweets if t.get('likes', 0) > 100]
top_posts  = [p for p in posts  if p.get('upvotes', 0) > 50]

# BƯỚC 3: Feed vào Claude (tốn token — nhưng ít hơn nhiều)
# hot_tweets thường còn 5-10 cái thay vì 50
```

---

## Use Cases Cho AI Vibe Toolkit

### 1. Research Trước Khi Làm Video

```python
tool = "hermes-agent"

# Thu thập signal thật từ community
tweets    = reach.twitter(f"{tool} review", limit=50)
reddit    = reach.reddit_search(tool, limit=20)
youtube   = reach.youtube(tool, limit=10)

# Filter signal mạnh
hot = [t for t in tweets if t.get('likes',0) > 50]

# Feed vào Claude — hỏi:
# "Từ data này, pain points nào hay nhất để làm hook video?"
```

### 2. Tìm Angle Video Chưa Ai Làm

```python
# Check YouTube đã có ai cover chưa
videos = reach.youtube("agent-skills addyosmani", limit=20)

# Nếu < 5 videos tiếng Việt → blue ocean
vi_videos = [v for v in videos if 'việt' in v.get('title','').lower()
             or 'viet' in v.get('channel','').lower()]
print(f"Videos tiếng Việt: {len(vi_videos)}")
# → 0-2 = làm ngay, angle chưa ai khai phá
```

### 3. Morning Signal Loop (SAMS style)

```python
# Chạy mỗi sáng 7h — không tốn token
from agent_reach import Reach
reach = Reach()

# Collect signals ($0)
trending = reach.twitter("AI tools 2026", limit=30)
reddit   = reach.reddit("r/MachineLearning", limit=20)
hn       = reach.hackernews(limit=20)

# Filter hot items
hot = [t for t in trending if t.get('likes',0) > 200]
hot += [p for p in reddit  if p.get('upvotes',0) > 100]

# Save vào VAULT — KHÔNG gọi Claude ở đây
import json
with open('VAULT/morning-signals.json', 'w') as f:
    json.dump(hot, f, ensure_ascii=False)

# Claude chỉ đọc VAULT khi mày cần → tiết kiệm token tối đa
```

### 4. Monitor Brand Mentions

```python
# Check ai đang nhắc đến kênh/tool của mày
mentions = reach.twitter("AI Vibe Toolkit", limit=100)
mentions += reach.reddit_search("AI Vibe Toolkit", limit=50)

# Filter mentions thật (không phải bot)
real = [m for m in mentions if m.get('likes',0) > 0
        or m.get('comments',0) > 0]

print(f"Brand mentions thật: {len(real)}")
```

---

## Tối Ưu Token — 3 Rules

### Rule 1: Filter trước, feed sau
```python
# ❌ Tốn token
claude.analyze(tweets)  # 50 tweets × 280 chars = 14k tokens

# ✅ Tiết kiệm
hot = [t for t in tweets if t['likes'] > 100]  # còn 5 tweets
claude.analyze(hot)  # ~700 tokens — tiết kiệm 95%
```

### Rule 2: Extract chỉ field cần thiết
```python
# ❌ Feed raw JSON
claude.analyze(str(tweets))

# ✅ Chỉ lấy text + engagement
summary = [{"text": t['text'], "likes": t['likes']} for t in hot]
claude.analyze(str(summary))  # nhỏ hơn 10x
```

### Rule 3: Batch analyze, không call từng cái
```python
# ❌ Gọi Claude 50 lần
for tweet in tweets:
    claude.analyze(tweet)  # 50 API calls

# ✅ Gọi 1 lần với batch
claude.analyze(f"Analyze these {len(hot)} tweets: {hot}")
```

---

## Kết Hợp Với Kho

```
Agent-Reach → collect signals
last30days skill → validate với Reddit/X/YouTube
Brave Search MCP → verify thông tin
→ Feed tổng hợp vào Claude
→ Hermes viết .md + script
→ Push lên kho
```

---

## Platforms & Methods

```python
reach.twitter(query, limit=50)
reach.twitter_user("@username", limit=30)
reach.linkedin(query, limit=10)
reach.linkedin_profile("username")
reach.youtube(query, limit=10)
reach.youtube_transcript("video_id")
reach.reddit("r/subreddit", limit=20)
reach.reddit_search(query, limit=20)
reach.reddit_post("post_url")
reach.bilibili(query, limit=10)  # Chinese YouTube
reach.hackernews(limit=20)
```

---

*skills/agent-reach-skill.md | AI Vibe Toolkit | tháng 6/2026*

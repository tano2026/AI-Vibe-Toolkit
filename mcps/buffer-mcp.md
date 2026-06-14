# buffer-mcp — Schedule Social Media Posts Qua Claude (Buffer GraphQL)

**GitHub:** https://github.com/jakemeany523/buffer-mcp
**License:** MIT | **Language:** Python
**Platforms:** Twitter/X, LinkedIn, Facebook, Instagram, TikTok, Pinterest, Mastodon

---

## Cài Đặt

```bash
git clone https://github.com/jakemeany523/buffer-mcp
cd buffer-mcp
pip install mcp httpx pydantic
export BUFFER_ACCESS_TOKEN="your-token"
python3 server.py
```

**Lấy token:** buffer.com → Settings → Apps and Integrations → Create App

```json
{
  "mcpServers": {
    "buffer": {
      "command": "python3",
      "args": ["/path/to/buffer-mcp/server.py"],
      "env": { "BUFFER_ACCESS_TOKEN": "your-token" }
    }
  }
}
```

---

## Dùng Ngay

```bash
# Schedule 1 post
"Schedule post lên X/Twitter lúc 9am sáng mai:
 'Vừa khám phá agent-skills của @addyosmani — 
 24 skills senior engineer distilled thành Claude Code plugin.
 Link trong bio #vibecoding #claudecode'"

# Cross-platform scheduling
"Schedule video announcement cho tất cả channels lúc 7pm:
 Facebook: [caption dài, formal]
 Instagram: [caption ngắn + hashtags]  
 X: [thread 3 tweets]
 LinkedIn: [professional angle]"

# Content calendar
"Lấy content calendar tuần này từ Airtable/Notion → 
 schedule tất cả posts lên Buffer theo đúng time"

# Analytics
"Get top 5 posts performance tuần trước trên từng platform"
"Platform nào có engagement rate cao nhất tháng này?"
```

---

## Workflow Publishing AI Vibe Toolkit

```bash
# Sau khi upload video
"Tạo và schedule posts cho video '[TOOL NAME]':

Facebook: Caption 200 words, educational tone, 1 link
Instagram: Caption 100 words + 20 hashtags relevant, no link
X/Twitter: Thread 3 tweets — hook + value + CTA
LinkedIn: Professional angle, tag relevant people

Schedule: Stagger 15 phút, bắt đầu 9am"
```

---
*Nguồn: github.com/jakemeany523/buffer-mcp | MIT | tháng 6/2026*

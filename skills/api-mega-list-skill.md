# api-mega-list — Tìm API Trước Khi Build Tool (~6k⭐)

**Repo:** github.com/cporter202/API-mega-list
**Nội dung:** 6,000+ APIs categorized, nhiều cái free

---

## Rule Số 1

**Trước khi build tool gì → tìm API ở đây trước.**
80% chance đã có API làm được → không cần build từ đầu.

## Categories Hay Nhất

### AI & ML APIs (Free tiers)
- **Groq** — Llama 3.1 free, cực nhanh
- **Together AI** — 200+ models, $5 free credit
- **Hugging Face Inference** — 1000+ models free
- **Google Gemini** — free tier generous
- **Cohere** — embed + generate free

### Search APIs
- **Brave Search** — $3/1000 queries, privacy-first
- **Serper** — Google results $0.001/query
- **Exa** — semantic search, free 1000/month
- **Tavily** — research-optimized, free tier

### Data & Content
- **NewsAPI** — 100 requests/day free
- **Reddit API** — free với rate limits
- **Wikipedia API** — completely free
- **OpenLibrary** — books data, free

### Automation
- **Zapier** — free tier 100 tasks/month
- **n8n** — self-hosted free
- **Make.com** — 1000 operations/month free

### Communication
- **Telegram Bot API** — completely free
- **Discord API** — completely free
- **Resend** — email 3000/month free
- **Twilio** — $15 free credit

## Cách Tìm Nhanh

```bash
# Clone repo
git clone https://github.com/cporter202/API-mega-list
cd API-mega-list

# Search file
grep -i "email" README.md | head -20
grep -i "search" README.md | head -20
grep -i "free" README.md | head -30
```

## Workflow Trước Khi Build Bất Kỳ Feature

```
1. Mày có idea: "cần send email khi user signup"
2. → Search "email" trong api-mega-list
3. → Thấy: Resend free 3000/month, Mailgun free 5000/month
4. → Chọn Resend, implement trong 30 phút
5. → Không cần build email service từ đầu
```

---
*skills/api-mega-list-skill.md | AI Vibe Toolkit | tháng 6/2026*

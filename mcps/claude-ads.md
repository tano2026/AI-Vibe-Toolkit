# claude-ads — Audit Quảng Cáo Google/Meta/TikTok/YouTube Trong 15 Phút (6033⭐)

**GitHub:** https://github.com/AgriciDaniel/claude-seo (cùng tác giả claude-seo)
**Repo:** github.com/AgriciDaniel/claude-ads
**Stars:** 6033⭐ | **License:** MIT | **Trending hôm nay**
**Dùng với:** Claude Code

---

## Đây Là Gì

Skill audit paid advertising cho Claude Code — **250+ checks** trên Google, Meta (Facebook/Instagram), YouTube, TikTok, LinkedIn, Microsoft, Apple, Amazon Ads.

Manual audit 1 account: **4-6 tiếng senior PPC**.
Claude Ads: **10-15 phút**, score 0-100, prioritized action plan.

---

## Cài Đặt

```bash
# Claude Code (public release, MIT)
/plugin marketplace add AgriciDaniel/claude-ads
/plugin install claude-ads@agricidaniel-claude-ads
```

---

## Slash Commands

```bash
# Full audit toàn bộ account
/ads audit --platform google https://ads.google.com/aw/...
/ads audit --platform meta https://business.facebook.com/...
/ads audit --platform tiktok https://ads.tiktok.com/...

# Audit theo platform cụ thể
/ads google audit           # Google Ads 250+ checks
/ads meta audit             # Facebook + Instagram Ads
/ads tiktok audit           # TikTok Ads
/ads youtube audit          # YouTube Ads
/ads linkedin audit         # LinkedIn Ads

# Deep dives
/ads creative audit         # Review ad creatives
/ads audience audit         # Audience targeting analysis
/ads bidding audit          # Bidding strategy review
/ads budget audit           # Budget allocation check

# Reports
/ads report weekly          # Weekly performance report
/ads report monthly         # Monthly summary
/ads compare [period1] [period2]  # Period comparison
```

---

## 250+ Checks Cover Gì

### Google Ads
- Campaign structure (SKAGs vs STAGs, ad group hygiene)
- Quality Score optimization
- Bidding strategy alignment với goals
- Negative keywords gaps
- Search term waste analysis
- Ad copy A/B test coverage
- Extensions completeness
- Conversion tracking accuracy

### Meta (Facebook/Instagram)
- Audience overlap và fatigue
- Creative frequency capping
- Budget pacing vs objectives
- Pixel event firing
- Campaign objective alignment
- Ad set audience sizing
- Creative format diversity

### TikTok & YouTube
- Audience targeting reach
- Creative length optimization
- In-feed vs TopView mix
- Retargeting setup
- Brand safety settings

---

## Kết Hợp Với claude-seo

```bash
# Full digital marketing audit stack
/seo audit https://your-site.com     # SEO: organic
/ads audit --platform google         # Paid: Google
/ads audit --platform meta           # Paid: Social

# Tao có cùng tác giả → cùng workflow pattern
# Action plan từ cả 2 → prioritize theo ROI
```

---
*Nguồn: github.com/AgriciDaniel/claude-ads | 6033⭐ | MIT | tháng 6/2026*

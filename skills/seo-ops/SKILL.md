---
name: seo-ops
description: "AI-powered SEO operations: keyword intelligence, competitor gap analysis, GSC optimization, trend detection. Từ ai-marketing-skills repo."
allowed-tools:
  - Bash
  - Python
user-invocable: true
---

# SEO Ops — Keyword Intelligence & GSC Optimization

SEO toolkit từ ai-marketing-skills.

## Tools

### Content Attack Brief
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/seo-ops/content_attack_brief.py"
```
Produces: keyword ranking, competitor gaps, trending topics, decaying pages.

### GSC Client
```bash
# Top queries
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/seo-ops/gsc_client.py" --queries 50 --days 28

# Striking distance keywords (pos 4-20)
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/seo-ops/gsc_client.py" --striking

# Trend
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/seo-ops/gsc_client.py" --trend
```

### Trend Scout (no API keys needed)
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/seo-ops/trend_scout.py"
```
Sources: Google Trends, HN, Reddit, X, YouTube.

## Scoring
- **Impact (0-10)**: Volume + CPC + Funnel + Trend
- **Confidence (0-10)**: Difficulty + Rank + Authority
- **Priority = Impact × Confidence** (max 100)

## Config
Set in `.env` or env vars:
- `GSC_SITE_URL` — Google Search Console property
- `AHREFS_TOKEN` — for competitor analysis
- `COMPETITORS` — comma-separated domains
- `BRAVE_API_KEY` — for X trend scanning

## Workflow
1. **Weekly**: `content_attack_brief.py` for full report
2. **Daily**: `gsc_client.py --striking` for quick wins
3. **2x/week**: `trend_scout.py` for trending topics
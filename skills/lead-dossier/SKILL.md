---
name: lead-dossier
description: "Multi-source lead research, cascade enrichment, and pipeline management. Website scraping, tech stack detection, CRM enrichment, hiring/news signals into structured dossiers."
allowed-tools:
  - Bash
  - Python
user-invocable: true
---

# Lead Dossier — Multi-Source Account Research

Từ ai-marketing-skills repo.

## Quick Start
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/lead-dossier/scripts/lead_dossier.py" --company example.com
```

## Workflows
1. **Account Research** — scrape website + tech stack (BuiltWith) + CRM data → structured dossier
2. **Cascade Enrichment** — search → verify → dedupe → upload pipeline
3. **Lead Scoring** — intent signals + firmographics → priority score
4. **Email Verification** — validate + normalize + MX check

## Environment Variables
| Variable | Description |
|----------|-------------|
| `LEAD_SOURCE_API_KEY` | People/company search API |
| `EMAIL_VALIDATION_API_KEY` | Email verification service |
| `BUILTWITH_API_KEY` | Tech detection (free tier ok) |
| `CRM_API_KEY` | CRM API key |

## Output
- Structured JSON file per lead
- CSV for CRM import
- Score: Hot/Warm/Cold + priority number
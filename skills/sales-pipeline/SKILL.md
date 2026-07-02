---
name: sales-pipeline
description: "Complete sales pipeline automation: visitor → suppression → routing → dead deal resurrection → trigger prospecting → ICP optimization. Từ ai-marketing-skills repo."
allowed-tools:
  - Bash
  - Python
user-invocable: true
---

# Sales Pipeline — Full Stack Automation

Từ ai-marketing-skills repo.

## Tools

### RB2B Pipeline (Visitor → Outbound)
```bash
# Webhook server + intent scoring
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/sales-pipeline/rb2b_webhook_ingest.py" --serve --port 4100

# 5-layer suppression checks
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/sales-pipeline/rb2b_suppression_pipeline.py" --email user@example.com

# Full pipeline: score → suppress → route → enroll
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/sales-pipeline/rb2b_instantly_router.py" --serve --port 4100
```

### Deal Intelligence
```bash
# Dead deal resurrection
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/sales-pipeline/deal_resurrector.py" --top 10 --dry-run

# Trigger prospecting (new hires, funding)
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/sales-pipeline/trigger_prospector.py" --days 7 --top 15

# ICP learning from approve/reject
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/sales-pipeline/icp_learning_analyzer.py"
```

## Config
Env vars: `HUBSPOT_API_KEY`, `INSTANTLY_API_KEY`, `RB2B_WEBHOOK_SECRET`, `OPENAI_API_KEY`
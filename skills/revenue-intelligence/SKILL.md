---
name: revenue-intelligence
description: "Revenue intelligence: sales call insights (Gong), content-to-revenue attribution, multi-source client reporting (GA4+HubSpot+Ahrefs+Gong). Từ ai-marketing-skills repo."
allowed-tools:
  - Bash
  - Python
user-invocable: true
---

# Revenue Intelligence — Call Insights & Attribution

Từ ai-marketing-skills repo.

## Tools

### Gong-to-Insight Pipeline
```bash
# Single transcript
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/revenue-intelligence/gong_insight_pipeline.py" --file transcript.txt

# Batch from Gong API (last 7 days)
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/revenue-intelligence/gong_insight_pipeline.py" --gong --days 7
```
Extracts: objections, buying signals, competitive mentions, decision criteria.

### Content Attribution
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/revenue-intelligence/content_attribution.py"
```
Maps content assets → influenced deals → revenue. First-touch + multi-touch models.

### Client Report Generator
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/revenue-intelligence/client_report.py" --client "Acme Corp"
```
Unified report from GA4 + HubSpot + Ahrefs + Gong data.

### Anomaly Detection
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/revenue-intelligence/anomaly_detector.py" --metric leads
```
---
name: conversion-ops
description: "AI-powered CRO (Conversion Rate Optimization): landing page audits, survey segmentation, lead magnet generation. Từ ai-marketing-skills repo."
allowed-tools:
  - Bash
  - Python
user-invocable: true
---

# Conversion Ops — CRO & Landing Page Optimization

Từ ai-marketing-skills repo.

## Tools

### CRO Audit
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/conversion-ops/cro_audit.py" --url https://example.com/page

# Batch mode
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/conversion-ops/cro_audit.py" --file urls.txt --industry saas
```

Scores across 8 dimensions: Value Prop, Clarity, Trust, Design, Urgency, Friction, CTA, Mobile.

### Survey Segmentation
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/conversion-ops/survey_segment.py" --file survey.csv
```
Segments respondents by pain point + sentiment, generates lead magnet ideas.

### Lead Magnet Generator
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/conversion-ops/lead_magnet_generator.py" --niche "SaaS founders"
```

## Output
- CRO: scored audit + prioritized fix recommendations
- Survey: segment clusters + top pain points + offer recommendations
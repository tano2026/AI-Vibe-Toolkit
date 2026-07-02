---
name: content-ops
description: "Content marketing operations: expert panel scoring, content audit, gap analysis, editorial calendar, repurposing. Từ ai-marketing-skills repo."
allowed-tools:
  - Bash
  - Python
user-invocable: true
---

# Content Ops — Content Marketing Operations

Từ ai-marketing-skills repo.

## Core Feature: Expert Panel
Auto-assembles domain experts to score content across dimensions. Recursive scoring until 90+ (max 3 rounds).

```bash
# Score a piece of content
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/content-ops/expert_panel.py" --input content.md --type copy

# Score multiple variants (A/B/C)
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/content-ops/expert_panel.py" --inputs variant-a.md variant-b.md --type landing-page
```

## Scoring Dimensions (auto-selected by content type)
- **Copy**: Clarity, Persuasion, Hook, CTA, Readability, Trust
- **Landing Page**: Value Prop, Design, Social Proof, Scarcity, Friction
- **Strategy**: Logic, Data, Positioning, Differentiation, Feasibility
- **Headline/Title**: Curiosity, Clarity, Benefit, Urgency

## Other Tools
- **Content Audit** → inventory + quality scoring + gap analysis
- **Editorial Calendar** → topic clustering + scheduling
- **Repurpose Engine** → long-form → social posts + email + short video scripts
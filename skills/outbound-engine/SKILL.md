---
name: outbound-engine
description: "Cold email + outreach automation. Lead research, sequence builder, email campaign management, A/B testing. Từ ai-marketing-skills repo."
allowed-tools:
  - Bash
  - Python
user-invocable: true
---

# Outbound Engine — Cold Email & Outreach

Từ ai-marketing-skills repo.

## Location
```
D:/AI Store/digital-marketing-repos/ai-marketing-skills/outbound-engine/
```

## Capabilities
- **Lead research** — tự động research prospect từ web
- **Sequence builder** — multi-step email sequences
- **Campaign management** — track opens, replies, bounces
- **A/B testing** — subject line + body variants
- **Personalization** — AI-generated custom intros

## Quick Start
```bash
# Setup
pip install -r "D:/AI Store/digital-marketing-repos/ai-marketing-skills/requirements.txt"

# Run
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/outbound-engine/scripts/outbound.py" --help
```

## Key Features
- Multi-channel (email + LinkedIn + X)
- Smart follow-up scheduling
- Spam score checker
- Reply detection & routing
- Analytics dashboard (open rate, reply rate, meeting booked)

## Config Required
- SMTP credentials
- `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` for personalization
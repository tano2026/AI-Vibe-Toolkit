# n8n-claw — Skill Build AI Agent Visual, Không Cần Terminal

**Repo:** github.com/freddy-schuetz/n8n-claw | MIT
**Stack:** n8n + OpenClaw — visual workflow + AI agent power

---

## Cài 1 Script

```bash
git clone https://github.com/freddy-schuetz/n8n-claw
cd n8n-claw
./setup.sh  # cài n8n + OpenClaw + config tự động
```

## Mở n8n UI

```bash
# Sau setup xong
open http://localhost:5678
```

## 5 Template Workflow Có Sẵn

| Template | Làm gì |
|----------|--------|
| **daily-research** | Cào GitHub/X trending mỗi sáng → tóm tắt → Telegram |
| **content-pipeline** | Idea → research → draft → review → schedule post |
| **monitor-competitors** | Theo dõi website/repo đối thủ → alert khi có thay đổi |
| **email-processor** | Đọc email → categorize → draft reply → chờ approve |
| **github-assistant** | PR review → issue triage → release notes auto |

## Khi Nào Dùng n8n-claw vs OpenClaw Thuần

| Situation | Dùng gì |
|-----------|---------|
| Không quen terminal | n8n-claw |
| Cần visual workflow | n8n-claw |
| Muốn share workflow với team | n8n-claw |
| Cần performance tối đa | OpenClaw thuần |
| Đang quen code | OpenClaw thuần |

## Kết Nối Messaging

```bash
# Trong n8n UI → Credentials → thêm:
# Telegram Bot Token
# Discord Bot Token
# Slack Bot Token
# Gmail OAuth
```

---
*skills/n8n-claw-skill.md | AI Vibe Toolkit | tháng 6/2026*

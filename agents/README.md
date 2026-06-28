# /agents — Hệ thống AI Agents

## 3 agents trong hệ thống

| Agent | Instruction | Runtime | Kênh |
|-------|-------------|---------|------|
| **Hermes** | `HERMES-PLAYBOOK.md` | Python trong OpenClaw | Telegram |
| **OpenClaw** | `OPENCLAW-PLAYBOOK.md` | Node.js 22+ | Telegram / WhatsApp |
| **Antigravity** | `ANTIGRAVITY-PLAYBOOK.md` | Shell/SSH trên VPS | Manual / webhook |

## Sub-agents
- `research-pro.md` — Research Pro, chạy trong Hermes
- `research-analytics-pro/` — System prompt + domain playbooks cho Research Pro

## Luồng phân công

```
Chủ nhắn Telegram
      ↓
OpenClaw nhận, phân loại
      ├── Browser / UI / WhatsApp  → OpenClaw tự làm
      ├── Python / API / data      → Hermes
      ├── Deploy / install / VPS   → Antigravity
      └── Viết .md, thêm kho      → Báo chủ → Claude làm
```

## Entry point của kho

`/KHO-INDEX.md` — đọc file này đầu tiên trước khi fetch bất cứ thứ gì.

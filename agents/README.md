# /agents — Hệ thống AI Agents
> Cập nhật 22/08/2026 — bản trước ghi "3 agents", trỏ tới file đã xoá
> (research-pro.md). Viết lại đầy đủ theo COMPANY-CHARTER.md.

## 4 Vessel (nơi thực thi) — không phải 3 như bản cũ

| Vessel | Instruction | Runtime | Kênh |
|---|---|---|---|
| **Hermes** | HERMES-GUIDE.md -> HERMES-PLAYBOOK.md | Python (urllib-only) | Telegram |
| **OpenClaw** | OPENCLAW-GUIDE.md -> OPENCLAW-PLAYBOOK.md -> OPENCLAW-TOOLKIT.md | Node.js 22+ | Telegram / WhatsApp |
| **DeepSeek Harness** | (chưa có playbook riêng, còn breaking changes — mượn quyết định qua OpenClaw) | Node.js/Cordis | — |
| **Antigravity** | ANTIGRAVITY-GUIDE.md -> ANTIGRAVITY-PLAYBOOK.md | Google Antigravity 2.0 thật (đã xác nhận, không phải agent tự đặt tên trùng) | Manual / webhook / cron |
| **Claude Code** | CLAUDE-CODE-BRIDGE.md | Local Windows, Claude Code Desktop | — |

Hermes + OpenClaw + DeepSeek Harness gộp chung gọi là "Team Thục Hán" khi chạy trong project OPC — biệt danh nội bộ, giao tiếp qua file tasks/*.md, tách runtime với Claude Code.

## 8 Pro Agent (Talent — năng lực, khác Vessel)

research-analytics-pro/ . content-pro/ . sales-ceo/ . digital-marketing-agent/ . infra-ops-agent/ . media-pro/ . designer-pro/ . customer-satisfaction-pro/

Mỗi Pro Agent = agents/company/EXPERT-CORE.md (luật, section riêng) + skill riêng. Xem đầy đủ Vessel/Talent tại agents/company/COMPANY-CHARTER.md.

## Luồng phân công (qua EA Quality Gate — mới, xem task-intake-quality-gate)

```
Nobitano nhắn Telegram
      |
OpenClaw nhận -> chạy task-intake-quality-gate (4 câu hỏi gác cổng)
      |-- Browser / UI / WhatsApp     -> OpenClaw tự làm
      |-- Python / API / data         -> Hermes
      |-- Code phức tạp (GitHub-based)-> DeepSeek Harness (thận trọng, còn breaking changes)
      |-- Deploy / install / VPS      -> Antigravity (Google Antigravity 2.0)
      |-- Local Windows, cần file thật-> Claude Code
      `-- Viết .md, thêm kho          -> Báo Nobitano -> Claude (chat) làm
```

## Entry point của kho

/KHO-INDEX.md — đọc file này đầu tiên trước khi fetch bất cứ thứ gì. Luật cứng: agents/company/EXPERT-CORE.md. Nhóm skill "Đầu Não" dùng chung mọi Vessel: agents/company/CORE-META-SKILLS.md.

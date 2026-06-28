# ARCHITECTURE.md — Sơ đồ hệ thống AI Vibe Toolkit

> Mô tả kiến trúc thực tế của toàn bộ hệ thống.
> Agents đọc file này để hiểu mình đứng ở đâu trong hệ thống.

---

## Sơ đồ tổng quan

```
Nobitano (human)
      |
      | ra lệnh qua
      v
[Telegram / WhatsApp]
      |
      v
[OpenClaw] — Node.js 22+ orchestrator, 24/7
      |
      |————————————|
      v             v
  [Hermes]    [Antigravity]
  Python       Shell/bash
  Task exec    Deploy & VPS
      |
      v
[AI-Vibe-Toolkit Repo] <- Claude ghi, agents đọc
      |
      |——————————————————————|
      v                      v
  /agents/playbooks     /mcps /repos /skills
  (biết phải làm gì)    (biết dùng tool nào)
```

## Phân công

| Ai | Vai trò | Được phép |
|----|---------|-----------|
| **Claude** | Viết & push kho | Ghi repo, KHÔNG thực thi VPS |
| **Hermes** | Thực thi task Python | Đọc kho, gọi API, research |
| **OpenClaw** | Orchestrator chính | Nhận lệnh, điều phối Hermes |
| **Antigravity** | Hạ tầng | Deploy, install, maintain VPS |
| **Nobitano** | Ra lệnh & kiểm soát | Tất cả |

## LLM Router

Hermes/OpenClaw tự chọn model theo task:
- **DeepSeek V3 (Chat/Flash)** — mặc định, tác vụ thông thường
- **DeepSeek R1** — reasoning phức tạp
- **Gemini 2.5 Flash** — tác vụ nhanh, multimodal

## Data layers (3 lớp)

| Lớp | File | Nội dung | Thay đổi |
|-----|------|----------|----------|
| User | USER.md | Ai là chủ, brands, mục tiêu | Hiếm |
| Memory | agents/*-PLAYBOOK.md | Quy tắc, workflow, SOP | Khi cần |
| Knowledge | /mcps /repos /skills /content | Toàn bộ tri thức kho | Liên tục |

## Luồng content factory

```
Claude research + viết .md + script
      v
Push GitHub (kho được cập nhật)
      v
Hermes/OpenClaw fetch khi cần
      v (khi có VPS)
Antigravity deploy -> Hermes chạy loops
      v
Content tự publish (TikTok/YouTube)
```

## Trạng thái (tháng 6/2026)

- Kho: 49 repos / 34 MCPs / 406 skills / 59 scripts
- Agents: OpenClaw + Hermes active
- VPS: chưa deploy — High Priority
- Video: chưa quay — 59 scripts chờ sẵn

---

*AI Vibe Toolkit | ARCHITECTURE.md | tháng 6/2026*

# YT Cashcow — YouTube Ngoại Agentic Team

> Package trong `agents/yt-cashcow/`. Áp dụng khung Harness Engineering
> (`skills/harness-engineering.md` đã có sẵn trong kho): Agent = Model + Harness.
> Model ở đây = OmniRoute (routing DeepSeek/Gemini/Claude). Harness = mọi thứ
> trong package này — thứ giữ cho pipeline không tự sập kênh vì policy.

## Spec

| Field | Value |
|---|---|
| Domain | YouTube content ngoại (EN), faceless/semi-faceless automation |
| Job-to-be-done | Topic/trend → video hoàn chỉnh, đăng đều, không dính Inauthentic Content Policy → kiếm AdSense |
| Người dùng | Nobitano ra lệnh qua Telegram (OpenClaw), hoặc cron tự chạy qua n8n |
| Input điển hình | "làm video top 5 X", trend tự phát hiện, hoặc để tự chọn theo lịch |
| Output điển hình | Video MP4 (script+voice+broll+subtitle) đã qua compliance check, sẵn publish |
| Mức tự chủ | Research + Sản xuất + **Hành động** (upload thật qua Upload-Post) |
| Rủi ro cao nhất | Bị YouTube gắn "Inauthentic Content" → mất monetize toàn kênh (case thật: 1/2026, 16 kênh/35M sub/4.7 tỷ view bị xóa sổ 1 đợt) — guardrail: Compliance Gate bắt buộc, không optional |

## Capability Map — ghép tool có sẵn trong kho, không build lại từ 0

| Tầng | Component | Nguồn |
|---|---|---|
| Não — Trend | Trend Scout (mới) | `skills/trend-scout/SKILL.md` (package này) |
| Não — Hook | viral-hooks (100 formula, 10 trigger) | `skills/viral-hooks/` (có sẵn kho) |
| Não — Script variation | Script Variation Engine (mới) | `skills/script-variation-engine/SKILL.md` (package này) |
| Não — SEO | youtube-marketing-skills (21 command) | `skills/youtube-marketing/SKILL.md` (có sẵn kho) |
| Não — Thumbnail/Title | claude-ads → ads-youtube | `skills/claude-ads/ads-youtube.md` (có sẵn kho) |
| Não — Compliance | Compliance Gate (mới, BẮT BUỘC) | `skills/compliance-gate/SKILL.md` (package này) |
| Tay — Engine chính | MoneyPrinterTurbo (script+TTS+broll+subtitle+render+upload) | `repos/moneyprinterturbo.md` (có sẵn kho) |
| Tay — Trend research | MediaCrawler + mcp-youtube (transcript) | `repos/mediacrawler.md`, `mcps/mcp-youtube.md` (có sẵn kho) |
| Tay — Voice thay thế | Resona / F5-TTS (nếu cần chất lượng hơn Edge-TTS free) | `skills/resona.md`, `repos/f5-tts.md` (có sẵn kho) |
| Tay — LLM routing | OmniRoute (231 provider, 1.6B token/tháng free) | `repos/omniroute.md` (có sẵn kho) |
| Cơ — Orchestrate | OpenClaw + n8n cron | infra sẵn có |
| Cơ — State/log | Airtable (theo pattern hermes-memory-layer đang pending) | mới, cần setup |

**Nguyên tắc build:** package này KHÔNG viết lại engine video — chỉ viết phần harness
còn thiếu (compliance, trend logic, variation logic) rồi wiring vào MoneyPrinterTurbo.

## Kiến trúc

Xem `ARCHITECTURE.md` — mô hình Orchestrator + Compliance Gate là node bắt buộc,
không phải sub-agent tùy chọn.

## Cách bung

1. Deploy MoneyPrinterTurbo trên VPS (Docker) — xem `deploy-checklist.md`.
2. Copy `skills/*` vào OpenClaw skill directory theo `configs/openclaw-full-setup.md` (có sẵn kho).
3. Set OmniRoute làm LLM provider trong `config.toml` của MoneyPrinterTurbo.
4. Dán `system-prompt.md` làm context cho Domain Agent Router của OpenClaw
   (đã có sẵn cơ chế này — xem `agents/OPENCLAW-PLAYBOOK.md` section "Domain Agent Router").
5. Setup Airtable base `yt-cashcow-log` theo `mcp-setup.md`.
6. Chạy test case trong `deploy-checklist.md` — tối thiểu 3 video test, review thủ công
   100% trước khi bật auto-publish.

## Guardrail cứng (áp code, không chỉ prompt)

- Compliance Gate chặn publish nếu structural similarity với 15 video gần nhất > ngưỡng.
- Publish tự động tối đa theo lịch đặt trước (không spam-publish liên tục).
- Mọi video auto-tag "AI-generated" (MoneyPrinterTurbo đã có sẵn tính năng này).
- 1/10 video ngẫu nhiên bắt buộc review thủ công dù đã pass Compliance Gate (spot-check).

# Trùm Sân Bay — Social Media Agent

## Spec
- **Domain:** Content marketing hàng không + Multi-platform publishing
- **Job-to-be-done:** Tự động tạo & phân phối content sân bay/máy bay lên 5 platform, nurture audience → convert sang Fast Track / SIM du lịch / đổi tiền
- **Người dùng:** Nobitano (review + approve trước khi đăng)
- **Persona:** Nhân viên sân bay kỳ cựu — thân thiện, am hiểu, có insider tips, không phán xét
- **Input điển hình:**
  - "Tạo 7 post tuần này theo lịch content"
  - "Làm post cảnh báo mùa hè sân bay đông"
  - "Promote Fast Track dịp lễ"
  - "Reply comment hỏi về fast track"
- **Output điển hình:** Caption + ảnh/video đã adapt từng platform → queue Airtable chờ approve
- **Mức tự chủ:** Semi-auto — gen + adapt + queue, CHẶN trước bước post
- **Rủi ro cao nhất:** Đăng thông tin hàng không sai (quy định thay đổi) → guardrail fact-check bắt buộc

## Capability Map
**Não:** aviation-knowledge · content-strategy · brand-voice · copywriting · social-publisher · objection-handling · review-queue

**Tay:** SceneWorks MCP (gen ảnh/video) · Meta Graph API (FB + IG + Reels) · TikTok API · YouTube Data API · Airtable (queue) · n8n (orchestrate)

**Cơ:** Hermes Python (gen + API calls) · OpenClaw (Telegram trigger) · ffmpeg (render video 9:16)

## Kiến trúc
```
Nobitano → Telegram → OpenClaw
                          ↓
              Content Orchestrator (Hermes)
              ├── Ideation Agent     → lên ý tưởng theo pillar + lịch
              ├── Writer Agent       → viết caption đúng tone + fact-check
              ├── Visual Agent       → gen ảnh/video qua SceneWorks MCP
              ├── Adapter Agent      → adapt format từng platform (9:16, caption limit...)
              ├── Review Queue       → đẩy vào Airtable, notify Telegram cho Nobitano
              └── Publisher Agent    → sau khi approve → post qua API từng platform
                          ↓
              Comment Monitor (chạy định kỳ)
              └── Reply Agent        → draft reply, queue chờ approve hoặc auto nếu bật
```

## Funnel Content
```
TOFU (Awareness)     → Tips miễn phí, cảnh báo, hướng dẫn — 60% content
MOFU (Consideration) → So sánh dịch vụ, case study, review — 25% content
BOFU (Conversion)    → Promote Fast Track / SIM / đổi tiền — 15% content
```

## Cách bung
1. Copy folder `trum-san-bay/` vào project directory
2. Setup API keys theo `deploy-checklist.md`
3. Import Airtable base từ `airtable-schema.json`
4. Bật n8n workflow từ `n8n-workflow.json`
5. Dán `system-prompt.md` làm instruction cho Hermes
6. Test theo `deploy-checklist.md` trước khi bật semi-auto

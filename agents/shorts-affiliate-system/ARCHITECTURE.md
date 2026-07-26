# Kiến trúc — Shorts Affiliate System

## Sơ đồ pipeline đầy đủ

```
┌──────────────────────────────────────────────────────────────────────┐
│ 1. INPUT — 1 URL tool/AI product cần review                           │
│    /promo https://github.com/owner/tool                               │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 2. AFFILIATE RESEARCH (dùng skills/affiliate-skills.md có sẵn kho)    │
│    /affiliate research-programs "<tool> affiliate program"            │
│    /affiliate keyword-research "<tool>" --intent buyer                │
│    → có chương trình không? link nào?                                 │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 3. STORYBOARD GENERATOR (skills/storyboard-generator/SKILL.md)        │
│    Fetch README/metadata thật → draft storyboard.json 6 scene         │
│    → scene cta-url gắn affiliate_link nếu bước 2 xác nhận có          │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 4. REVIEW & APPROVE (người — bắt buộc, human-in-the-loop)             │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 5. COMPLIANCE GATE (skills/compliance-gate/SKILL.md — mượn)           │
│    Check structural variation, tránh mass-produce pattern             │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 6. RENDER (render/build_render_html.py → render/record.js → merge.sh)│
│    storyboard.json → render.html → Playwright quay 2 viewport cùng lúc│
│    → FFmpeg merge WebM→MP4 + mux voiceover → resize 9:16              │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 7. PLATFORM DISCLOSURE ADAPTER (skills/platform-disclosure-adapter/  │
│    SKILL.md — mượn) — bật toggle AI-content đúng YouTube/TikTok/Meta │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 8. AFFILIATE DISCLOSURE WRITER (skills/affiliate-disclosure-writer/  │
│    SKILL.md) — description + pinned comment + disclosure affiliate    │
│    CHỈ chạy nếu affiliate_link != null                                │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 9. PUBLISH — 16:9 → YouTube/LinkedIn | 9:16 → TikTok/Reels/Shorts    │
│    (dùng repos/tiktokautouploader.md, mcps/meta-mcp-server.md,        │
│     mcps/buffer-mcp.md có sẵn kho)                                    │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 10. TRACK & OPTIMIZE (skills/affiliate-skills.md có sẵn kho)          │
│     /affiliate track-performance | attribution-report                 │
│     → review nào ra tiền → repurpose format đó                        │
└──────────────────────────────────────────────────────────────────────┘
```

## Vì sao 2 checkpoint chặn cứng (bước 4 và bước 5)

- **Bước 4 (review người):** storyboard có thể sai fact hoặc chọn affiliate link sai —
  chặn ở đây rẻ hơn nhiều so với render xong mới phát hiện.
- **Bước 5 (compliance gate):** video này 100% AI-generated (HTML render + TTS), rủi ro
  bị nền tảng gắn nhãn Inauthentic Content là có thật — bắt buộc kiểm structural variation
  giữa các video trước khi render tốn compute.

## Vì sao 2 lớp disclosure tách biệt (bước 7 và bước 8)

Disclosure AI-generated (bước 7) và disclosure affiliate (bước 8) là 2 yêu cầu pháp lý/
chính sách KHÁC NHAU, không cái nào thay được cái nào:
- Thiếu disclosure AI-content → vi phạm chính sách nền tảng (YouTube/TikTok/Meta).
- Thiếu disclosure affiliate → vi phạm quy định quảng cáo (FTC-style).
Video vừa AI-gen vừa có affiliate thì cả 2 disclosure phải cùng xuất hiện.

## Điểm nối với tool có sẵn trong kho (không viết lại)

| Bước | Tool có sẵn dùng lại |
|---|---|
| 2, 10 | `skills/affiliate-skills.md` (52-skill flywheel) |
| 9 | `repos/tiktokautouploader.md`, `mcps/meta-mcp-server.md`, `mcps/buffer-mcp.md` |
| Voiceover | `repos/omniroute.md` để route TTS rẻ, hoặc Supertonic (free) |

# Shorts Affiliate System — Agentic Specialist

Hệ thống video ngắn xây kênh + gắn affiliate. Short-form-first (không phải cắt lại từ
long-form). Input là 1 URL tool/product cụ thể, output là video 2 tỷ lệ (16:9 + 9:16)
kèm affiliate link gắn đúng chỗ + disclosure hợp lệ.

## Spec
- **Domain:** Content sản xuất video ngắn (AI tool review, product demo) + affiliate marketing
- **Job-to-be-done:** Nhận 1 URL tool → ra video ngắn (2 định dạng) có gắn affiliate link,
  đăng lên kênh, track được conversion
- **Người dùng:** Nobitano (chủ kênh AI tool review)
- **Input điển hình:** `/promo https://github.com/owner/tool`, hoặc link web tool bất kỳ
- **Output điển hình:** `output_16x9.mp4` (YouTube/LinkedIn) + `output_9x16.mp4`
  (TikTok/Reels/Shorts) + description/pinned comment có affiliate link + disclosure
- **Mức tự chủ:** Phân tích + tạo nội dung — CHƯA tự publish, luôn qua review thủ công
  tối thiểu 3 video đầu (xem `deploy-checklist.md`)
- **Rủi ro cao nhất:** (1) Bị gắn nhãn Inauthentic Content vì 100% AI-generated →
  guardrail `compliance-gate`; (2) Thiếu disclosure affiliate → vi phạm quy định quảng
  cáo → guardrail `affiliate-disclosure-writer`

## Capability Map
**Não:** `storyboard-generator` · `affiliate-disclosure-writer` · `compliance-gate`
(mượn) · `platform-disclosure-adapter` (mượn) · `trend-scout` (mượn, dùng khi chưa có
URL cụ thể) — xem `skills/affiliate-skills-reference.md` cho lớp research/track affiliate
(52-skill flywheel, không copy nguyên vào đây, tham chiếu tool đã có sẵn trong kho ở
`/skills/affiliate-skills.md`)

**Tay:** Fetch tool (GitHub API / web fetch) · `/affiliate research-programs` ·
`/affiliate setup-tracking` · `/affiliate track-performance` (tool có sẵn kho)

**Cơ:** Playwright (record 2 viewport) · FFmpeg (merge + resize) · Supertonic/ElevenLabs
(voiceover) — xem `render/`

## Kiến trúc
```
Input URL → Affiliate Research → Storyboard Generator → [Review người] → Compliance Gate
→ Render (Playwright + FFmpeg) → Platform Disclosure Adapter → Affiliate Disclosure Writer
→ Publish → Track & Optimize
```
Sơ đồ đầy đủ xem `ARCHITECTURE.md`.

## Cách bung
1. Copy thư mục `skills/*` vào project skills directory.
2. Cài dependency render: `npm install playwright && npx playwright install chromium`,
   đảm bảo `ffmpeg`/`ffprobe` có sẵn trên VPS.
3. Dán `system-prompt.md` làm project instruction cho agent này.
4. Test với `examples/storyboard-example.json`:
   ```bash
   python render/build_render_html.py examples/storyboard-example.json render/render_16x9.html 16x9
   python render/build_render_html.py examples/storyboard-example.json render/render_9x16.html 9x16
   node render/record.js --input render/render_16x9.html --output render/scenes_16x9.webm \
     --width 1920 --height 1080 --duration 28
   ./render/merge.sh render/scenes_16x9.webm voice.mp3 output/
   ```
5. Chạy checklist trong `deploy-checklist.md` trước khi giao việc thật (đặc biệt: test
   case affiliate link + test case không có affiliate).

## Việc CHƯA giải quyết
- Danh sách chương trình affiliate cụ thể đã đăng ký — cần Nobitano cung cấp trước khi
  `affiliate-skills: research-programs` chạy có kết quả thật.
- Wiring `/affiliate` command với Hermes/OpenClaw thật (hiện dùng như pseudo-CLI mô tả
  trong `_reference/affiliate-skills.md`, cần map sang lệnh thật khi tích hợp).
- Ngưỡng số video test trước khi bật auto-publish hoàn toàn — do Nobitano quyết định
  sau khi xem kết quả 3 video đầu.

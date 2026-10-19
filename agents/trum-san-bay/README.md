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


---

## Não hệ thống — orchestrator.py

`agent.py` chỉ chứa các hàm nền (API call, Airtable, token refresh, publish).
`orchestrator.py` mới là NÃO THẬT — ghép 9 agent thành pipeline chạy được:

```bash
# Chạy full pipeline tuần (Research -> Ideation -> Writer -> Visual -> Brand Check -> Adapter)
python3 orchestrator.py weekly

# Check + refresh token chủ động
python3 orchestrator.py token_check
```

pm2 cron gọi `orchestrator.py weekly` mỗi thứ 2 7h sáng — không phải gọi
từng agent rời rạc. Comment pipeline (`run_comment_pipeline`) cần
`fetch_comments_fn` implement riêng theo từng platform API, gọi mỗi 2h.

**Trạng thái thật (đã cập nhật):**
- ✅ `run_visual_agent_image()` gọi Gemini image gen thật (`gemini-2.5-flash-image`, 
  free tier Google AI Studio), tải ảnh về `/opt/trum-san-bay/assets/` — đổi từ 
  Pollinations sang vì free tier ổn định hơn + dùng chung key với llm-router
- ✅ `fetch_all_comments()` đã code đủ 4 platform (Facebook, Instagram Graph API; 
  TikTok qua Apify Comment Scraper; YouTube Data API v3) — dùng làm 
  `fetch_comments_fn` cho `run_comment_pipeline()`
- ⚠️ Brand Check chạy nhưng **ảnh từ Pollinations chưa có logo/watermark tự động** 
  — pipeline flag `brand_check_issues` trong Airtable thay vì chặn cứng, cần 
  code thêm bước overlay logo (ffmpeg/PIL) trước khi coi là "brand compliant" thật
- ⚠️ Gemini free tier rate limit ~15 req/phút — đủ cho nhịp content hiện tại 
  nhưng nếu research batch nhiều bài cùng lúc, code đã có retry backoff cho 429
- ✅ **Đã sửa sau lượt kiểm chạy mock** (xem `catalog/smoke/CODE-REPORT.md`; test ở
  `agents/trum-san-bay/tests/`, chạy `python -m unittest discover -s agents/trum-san-bay/tests`):
  - `llm_call` nay có thật trong `llm_router.py` (tier → model, Claude trực tiếp, còn lại qua
    OmniRoute; `CostTracker` ghi chi phí mỗi lần gọi và chặn khi vượt `TSB_BUDGET_MONTHLY_USD`,
    mặc định $10). `import orchestrator` chạy được. Giá model trong `PRICING_PER_MTOK` là
    ƯỚC TÍNH, chỉnh theo bảng giá thật.
  - `publish_post_safe`: 0 platform cấu hình → `config_error` (không ghi Airtable, không báo
    "đã đăng"); Postiz `type: draft` (mặc định, đổi bằng `POSTIZ_POST_TYPE=now`) → trạng thái
    `draft_only` / Airtable `DRAFT_IN_POSTIZ`, KHÔNG ghi `POSTED`; backoff không ngủ sau lần cuối;
    `max_retries=0` hết `UnboundLocalError`; thông báo lỗi 401 đúng platform; state ghi UTF-8;
    `import agent` chạy được trên Windows (không có `fcntl` → dùng `msvcrt`, không có cả hai →
    no-op có cảnh báo). Đường dẫn state đổi được bằng `TSB_STATE_DIR`.
  - Bình luận: thiếu/sai `label` → `NEEDS_REVIEW` + người duyệt, không làm hỏng cả lô; id bình
    luận TikTok dùng SHA-1 ổn định (không `hash()`); `run_brand_check` không còn hardcode màu
    rỗng/`has_logo=False`: đọc từ kết quả Visual, thiếu thì trả `unchecked`.
    (Cột `label` Airtable cần chấp nhận giá trị `NEEDS_REVIEW` nếu là single-select.)
- ⚠️ **VẪN CHƯA chạy với credential thật.** Mọi bằng chứng trên là mock (Airtable/Postiz/LLM
  giả). Chưa kiểm: `flock`/`msvcrt` thật, định dạng phản hồi thật của Airtable, Postiz (field
  `type`, giá trị `now`/`schedule`), Meta, TikTok, YouTube, Gemini, Apify, OmniRoute/Anthropic,
  công thức lọc Airtable, giá token thật. Brand Check vẫn chưa overlay logo tự động.
  Bước tiếp theo là Phase 5 trong `deploy-checklist.md`.

## Chạy thử nhanh (sau khi có đủ credential)

```bash
cd /opt/trum-san-bay
python3 orchestrator.py weekly     # full pipeline: research -> ideation -> writer -> visual -> brand check
python3 orchestrator.py comments   # fetch + classify + draft reply comment mới
python3 orchestrator.py token_check  # health check token, tự refresh nếu cần
```

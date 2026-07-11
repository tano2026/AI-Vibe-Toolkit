# Deploy Checklist — Trùm Sân Bay Agent

## Phase 1 — Setup môi trường

- [ ] Clone/copy folder `trum-san-bay/` vào `/opt/trum-san-bay/` trên VPS
- [ ] Install dependencies: `pip install requests airtable-python-wrapper google-api-python-client`
- [ ] Install ffmpeg: `apt install ffmpeg -y`
- [ ] SceneWorks đang chạy và accessible tại `http://localhost:7860`
- [ ] n8n đang chạy tại port 5678

## Phase 2 — API credentials

- [ ] Facebook App tạo xong, Page Access Token lấy về (test với Graph API Explorer)
- [ ] Instagram Business Account linked, IG User ID lấy được
- [ ] TikTok Developer App approved, access token lấy về
- [ ] YouTube API credentials download (`credentials.json`)
- [ ] Airtable API key + Base ID
- [ ] Set tất cả vào pm2 ecosystem.config.js (không commit file này lên GitHub)

## Phase 3 — Airtable setup

- [ ] Tạo base `trum-san-bay-queue`
- [ ] Tạo table `content_queue` với fields:
  - content_id (text)
  - topic (text)
  - pillar (single select: TOFU/MOFU/BOFU)
  - caption_fb, caption_ig, caption_tiktok, caption_shorts (long text)
  - asset_path (text)
  - video_path (text)
  - status (single select: DRAFT/PENDING_REVIEW/APPROVED/REJECTED/POSTED)
  - scheduled_time (date)
  - reject_reason (text)
  - post_ids (text — JSON string)
  - created_at (date)
- [ ] Tạo table `comment_queue` với fields:
  - comment_id, platform, post_id, comment_text, author, draft_reply, status, created_at

## Phase 4 — n8n workflows

- [ ] Import `n8n-workflow.json`
- [ ] Set credentials trong n8n cho Facebook, Instagram, TikTok, YouTube, Airtable
- [ ] Test trigger thủ công từng node
- [ ] Bật Cron: 8h sáng T2 hàng tuần (Ideation)
- [ ] Bật Cron: mỗi 2h (Comment Monitor)
- [ ] Bật Airtable watch: khi status = APPROVED → trigger Publisher

## Phase 5 — Test cases (chạy trước khi bật thật)

### Test 1 — Content gen
```
Lệnh Telegram: /tsb post "tip mang nước qua an ninh"
Expected: Nhận Telegram notification với preview caption + ảnh
Status Airtable: PENDING_REVIEW
```

### Test 2 — Approve flow
```
Lệnh Telegram: /tsb approve [content_id]
Expected: Publisher chạy, post lên Facebook test page
Verify: Post xuất hiện trên page trong 5 phút
```

### Test 3 — Multi-platform
```
Approve 1 content
Expected: Post xuất hiện trên tất cả 5 platform trong 10 phút
Verify từng platform, check format đúng chưa
```

### Test 4 — Comment monitor
```
Comment thử lên post test
Chờ 2h hoặc trigger manual
Expected: Draft reply xuất hiện trong Airtable comment_queue
```

### Test 5 — Reject flow
```
Lệnh: /tsb reject [id] "caption chưa đúng tone"
Expected: Status → REJECTED, Writer Agent nhận lý do, viết lại
```

## Phase 6 — Bật semi-auto

- [ ] Tất cả 5 test cases pass
- [ ] Đã review ít nhất 10 post đầu tiên thủ công
- [ ] Tone/persona ổn định, không sai thông tin
- [ ] Bật Cron Ideation hàng tuần
- [ ] Thông báo Nobitano mỗi sáng T2: "Có X bài mới chờ review"

## Phase 7 — Bật full auto (sau khi ổn định)

- [ ] Đã chạy semi-auto ít nhất 4 tuần không có incident
- [ ] Auto-approve TOFU content (ít rủi ro nhất)
- [ ] Giữ semi-auto cho BOFU (promote sản phẩm)
- [ ] Comment đơn giản (cảm ơn, câu hỏi FAQ) → auto reply
- [ ] Comment phức tạp/phàn nàn → vẫn queue thủ công

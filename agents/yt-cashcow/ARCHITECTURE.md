# Kiến trúc — YT Cashcow

Áp khung `skills/harness-engineering.md` (có sẵn kho): Agent = Model + Harness.
3 trụ Harness Engineering map trực tiếp vào 3 phần dưới đây.

## Sơ đồ

```
OpenClaw Orchestrator (Domain Agent Router, đã có sẵn)
│
├── [Trụ 1: Context Engineering]
│   Trend Scout → MediaCrawler + mcp-youtube
│   → thu raw trend, nén lại thành 1 dòng brief/topic (không nhồi full transcript
│     vào context của Script Writer — chỉ nhồi đúng phần cần)
│
├── [Trụ 2: Architectural Constraints — CỐT LÕI của package này]
│   Script Variation Engine → viết script + BẮT BUỘC gắn "editorial fingerprint"
│   (góc nhìn riêng, 1 data point gốc, hoặc structure khác 15 video trước)
│         ↓
│   Compliance Gate → so structural similarity với 15 video gần nhất
│   → PASS: đi tiếp. FAIL: bounce ngược Script Variation Engine, yêu cầu sửa.
│   → Đây là "structural enforcement" — chặn ở code, không phải chặn ở prompt.
│         ↓
│   MoneyPrinterTurbo → render (TTS + broll + subtitle + burn-in)
│         ↓
│   Human spot-check (1/10 video, random) → nếu rơi vào diện check, dừng
│   auto-publish, đợi Nobitano duyệt qua Telegram
│         ↓
│   Publisher → MoneyPrinterTurbo Upload-Post integration (đã có sẵn, không tự build OAuth)
│
└── [Trụ 3: Verification / Feedback loop]
    Analytics Reader → YouTube Analytics API (đọc watch time, CTR, retention)
    → ghi vào Airtable `yt-cashcow-log`
    → feed lại Trend Scout: video nào retention thấp → tránh format đó lần sau
    → feed lại Script Variation Engine: cập nhật "editorial fingerprint" history
      để không lặp lại pattern đã dùng
```

## Vì sao Compliance Gate đứng giữa, không phải cuối

Nếu đặt Compliance Gate SAU khi render xong (như thiết kế ban đầu) → tốn compute
render 1 video rồi mới biết fail, phải render lại. Đặt Gate NGAY SAU khi có script
text (trước khi tốn TTS+render) → rẻ hơn, nhanh hơn, và đúng nguyên tắc harness:
chặn lỗi sớm nhất có thể trong pipeline, không để lỗi lan xuống bước tốn tài nguyên hơn.

## Mở rộng đa nền tảng — sau Compliance Gate, trước Publisher

```
        (video pass Compliance Gate)
                    │
                    ▼
        ┌───────────────────────┐
        │  YouTube long-form     │  ← master content, render trực tiếp
        │  (16:9, MoneyPrinterTurbo) │  qua MoneyPrinterTurbo
        └───────────┬────────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │  shortcast cắt bản     │  ← không render lại từ đầu, cắt
        │  9:16 từ long-form      │  on-device (tiết kiệm compute)
        └───────────┬────────────┘
                    │
        ┌───────────┼───────────┬──────────────┐
        ▼           ▼           ▼              ▼
   YT Shorts     TikTok        IG Reels      Facebook Reels
        │           │           │              │
        ▼           ▼           ▼              ▼
  ┌─────────────────────────────────────────────────┐
  │       PLATFORM DISCLOSURE ADAPTER                 │
  │  (skills/platform-disclosure-adapter/SKILL.md)    │
  │  YouTube: toggle metadata (honor-system)          │
  │  TikTok:  toggle BẮT BUỘC (C2PA auto-detect,      │
  │           không né được — khác cơ chế YouTube)    │
  │  Meta:    toggle (enforcement lỏng hơn TikTok)    │
  └───────────┬───────────┬───────────┬───────────────┘
              ▼           ▼           ▼
      Upload-Post   TikTokAuto-  meta-mcp-server
      (trong MPT)   Uploader     / Buffer MCP
```

**Vì sao không publish 1 video y hệt ra cả 3 nơi:** ngoài lý do kỹ thuật (aspect
ratio khác), publish y hệt cross-platform còn vô tình tạo cảm giác "mass-produce"
nếu ai đó thấy cùng 1 video ở nhiều nơi cùng lúc không có biến thể gì — bản cắt
qua shortcast tự nhiên khác nhau về độ dài/pacing giữa các platform, giảm rủi ro
này thêm 1 lớp.

**TikTok là platform rủi ro cao nhất trong 3** — cơ chế C2PA phát hiện tự động,
không dựa vào tự khai như YouTube. Compliance Gate + Disclosure Adapter đều bắt
buộc chạy đầy đủ cho nhánh TikTok, không rút gọn quy trình vì "chỉ là video ngắn".

## State/Memory — theo pattern hermes-memory-layer đang pending

Không dùng bộ nhớ trong context của LLM (sẽ mất khi restart). Dùng Airtable base
`yt-cashcow-log`, 2 bảng:

**Bảng `videos`**
| Field | Type |
|---|---|
| video_id | text |
| topic | text |
| script_fingerprint | text (hash/summary cấu trúc) |
| compliance_status | select (pass/fail/human-review) |
| publish_date | date |
| retention_pct | number (ghi lại sau khi có data Analytics) |

**Bảng `fingerprint_history`** — 15 record gần nhất (rolling), dùng để Compliance Gate
so sánh. Field: `structure_type`, `hook_type`, `unique_claims` (list), `timestamp`.

## Điểm khác với thiết kế lần đầu (đã sửa sau research)

| Thiết kế cũ | Thiết kế mới | Lý do |
|---|---|---|
| 9 agent tự build từ 0 | Ghép MoneyPrinterTurbo + vài skill có sẵn | Kho đã có engine end-to-end, build lại tốn công vô ích |
| Lo OAuth YouTube phức tạp | Dùng Upload-Post integration có sẵn trong MoneyPrinterTurbo | Verify docs — tính năng này build sẵn |
| Lo GPU/RAM VPS không đủ | Verify docs — 4-8 core, 4-8GB RAM, không cần GPU nếu dùng cloud LLM+Edge-TTS | Số liệu thật từ MoneyPrinterTurbo README |
| Compliance Gate "nên có" | Compliance Gate bắt buộc, đứng giữa pipeline (trước render) | Case thật 1/2026: 35M sub bị xóa vì bỏ qua bước này |

---
name: trend-scout
description: >
  Dùng khi cần tìm topic mới cho video, đầu pipeline yt-cashcow. Trigger: cron
  hàng ngày qua n8n, hoặc Nobitano nhắn "tìm trend cho kênh".
---

# Trend Scout — Bắt trend sớm cho YT Cashcow

## TL;DR
Quét trend từ 2 nguồn (MediaCrawler cho social CN — bắt sớm 2-4 tuần trước khi
lan sang Tây, mcp-youtube cho transcript đối thủ trực tiếp trên YouTube), nén
thành 1 dòng brief/topic, không nhồi full raw data vào context (theo trụ 1
Harness Engineering — Context Engineering).

## Khi nào dùng
Đầu pipeline, trước Script Variation Engine. Chạy theo lịch cron (n8n) hoặc
on-demand qua Telegram.

## Quy trình

1. **Quét social CN** — dùng MediaCrawler (đã có kho: `repos/mediacrawler.md`)
   scrape XHS/Douyin/Bilibili theo niche đã chọn. Mục đích: bắt trend sớm hơn
   2-4 tuần so với khi nó lan sang TikTok/YouTube Tây.
2. **Quét đối thủ trực tiếp** — dùng mcp-youtube (`mcps/mcp-youtube.md`) lấy
   transcript 5-10 video top trong niche tuần này, không cần API key.
3. **Chấm điểm topic** — đưa cả 2 nguồn vào OmniRoute reasoning tier (DeepSeek R1),
   chấm theo: search volume ước tính, độ cạnh tranh, khớp niche kênh không.
4. **Output nén** — CHỈ trả về 1 dòng brief/topic (không phải full transcript đã
   scrape) để feed sang Script Variation Engine. Ví dụ: `"AI productivity tools
   2026 — angle: so sánh chi phí thật vs marketing hype, chưa ai làm góc này"`.

## Ví dụ thực tế
**Input:** cron chạy 7h sáng, niche = "AI tools review".
**MediaCrawler tìm được:** trend Douyin về "AI tool bị thổi phồng giá" đang tăng
mạnh, chưa xuất hiện trên YouTube.
**mcp-youtube check:** search "AI tool overpriced" trên YouTube → chỉ 2 video cũ,
không ai làm gần đây.
**Output brief:** `"AI tools that are overhyped vs actually worth the price — angle:
cost breakdown thật, dùng data không phải opinion"`.

## Lưu ý / Lỗi thường gặp
- Đừng để Trend Scout tự chọn topic đã dùng gần đây — check chéo với
  `fingerprint_history` trong Airtable trước khi chốt (tránh Compliance Gate
  fail ngay từ bước sau).
- MediaCrawler cần compliance riêng khi scrape (rate limit, ToS platform CN) —
  xem lưu ý trong `repos/mediacrawler.md`.

## Đánh giá cá nhân
- Điểm mạnh: 2 nguồn chéo (CN sớm + YouTube trực tiếp) cho tín hiệu tốt hơn 1 nguồn.
- Điểm yếu: MediaCrawler scrape CN platform có thể không match nhu cầu audience
  US/UK/AU trực tiếp — cần lọc lại theo văn hóa, không phải trend nào cũng dịch được.
- Có nên dùng: 8/10 — hiệu quả nhưng cần review thủ công định kỳ để tránh false positive
  (trend CN không transfer được sang thị trường ngoại).

## Agent Integration

### Hermes (Python, urllib thuần)
```python
# Gọi mcp-youtube endpoint lấy transcript (xem code mẫu trong mcps/mcp-youtube.md)
# Gọi MediaCrawler theo hướng dẫn trong repos/mediacrawler.md
# Gửi cả 2 vào OmniRoute endpoint (reasoning tier) để chấm điểm
import urllib.request, json

def score_topic(raw_signals, omniroute_url, omniroute_key):
    payload = {"model": "deepseek-r1", "messages": [
        {"role": "user", "content": f"Chấm điểm topic sau theo search volume/cạnh tranh: {raw_signals}"}
    ]}
    req = urllib.request.Request(omniroute_url, data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {omniroute_key}", "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
# n8n cron trigger → gọi Hermes function score_topic() → forward brief sang
# Script Variation Engine
```

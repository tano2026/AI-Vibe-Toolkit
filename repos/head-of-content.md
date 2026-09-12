---
name: head-of-content
description: >
  Stars: 16 (repo nhỏ, mới) Tác giả: bradautomates Domain: Social media content research
---

# head-of-content — AI đào content viral xuyên 4 nền tảng

**GitHub:** https://github.com/bradautomates/head-of-content
**Tác giả:** bradautomates | **Loại:** bộ 6 file `.skill` cho Claude Desktop

---

## TL;DR

Quăng cho nó 1 chủ đề, nó tự quét Twitter/X, Instagram, YouTube, TikTok tìm bài/video đang viral vượt trội mức trung bình ngành, tách cấu trúc hook-nội dung-kết, rồi ra luôn 1 bản kế hoạch content cross-platform có bước làm cụ thể.

## Tool này dùng để làm gì

Thay vì ngồi đoán "content gì sẽ hot", skill này tự động:
1. Quét 4 nền tảng tìm bài có engagement vượt trội (không phải chỉ nhiều view, mà tính theo baseline ngành)
2. Bóc tách cấu trúc video/bài viết viral: hook 3 giây đầu, nhịp chuyển cảnh, cách kết
3. Ghi điểm bằng thuật toán thay vì cảm tính
4. Xuất ra kế hoạch content đa nền tảng, có bước thực thi rõ ràng

## Setup từng bước

1. Clone repo:
```bash
git clone https://github.com/bradautomates/head-of-content.git
```
2. Import 6 file `.skill` vào Claude Desktop (Settings → Capabilities → Skills → upload)
3. Cấu hình API key:
   - **Apify** (dùng để scrape Twitter/IG/TikTok — trả phí theo dùng)
   - **TubeLab** (dùng cho YouTube — trả phí)
4. Trong chat, nói rõ nền tảng + chủ đề muốn phân tích

## Ví dụ thực tế

Input: "Phân tích content viral về travel hacks trên TikTok và IG tuần này"
Output: danh sách 5-10 bài/video vượt engagement trung bình, breakdown hook từng cái (vd: "0-2s hiển thị số tiền tiết kiệm được, 2-5s reveal cách làm"), và 1 kế hoạch 3 video theo công thức tương tự áp cho brand của mình.

Ví dụ dùng cho ABTRIP: "quét content viral về mẹo qua sân bay nhanh trên TikTok" → ra công thức hook để làm video Fast Track An Bình.

## Lưu ý / Lỗi thường gặp

- Bắt buộc trả phí Apify + TubeLab mới chạy được — không có bản free-tier đủ dùng
- Scraper X/Twitter cần tài khoản Apify trả phí riêng, đắt hơn IG/TikTok
- Repo còn nhỏ (16⭐), ít người dùng thử, chưa có nhiều case study cộng đồng để đối chiếu lỗi

## Đánh giá cá nhân

- **Điểm mạnh:** giải quyết đúng pain "không biết content gì sẽ viral" bằng data thật thay vì đoán; output actionable, không chỉ liệt kê số liệu suông
- **Điểm yếu:** phụ thuộc 2 API trả phí ngoài, chi phí vận hành cộng dồn nếu quét thường xuyên; repo non trẻ, rủi ro maintain không đều
- **Có nên dùng không:** 7/10 — hợp cho ai đã có ngân sách API research content, không hợp nếu chỉ muốn free tool

## Link
- Repo: https://github.com/bradautomates/head-of-content
- Docs: (README trong repo, không có site riêng)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# head-of-content không có REST API riêng — bản chất là skill file cho Claude,
# không phải service độc lập. Hermes muốn tái tạo logic tương tự thì gọi thẳng Apify + TubeLab API.
import urllib.request, json

APIFY_TOKEN = "[YOUR_APIFY_TOKEN]"
def scrape_tiktok_viral(keyword):
    url = f"https://api.apify.com/v2/acts/clockworks~tiktok-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"
    payload = json.dumps({"searchQueries": [keyword], "resultsPerPage": 20}).encode()
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"}, method="POST")
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
# Không có CLI riêng — import 6 file .skill trực tiếp vào Claude Desktop qua UI, không qua npx
git clone https://github.com/bradautomates/head-of-content.git
```

### Antigravity
```bash
# Không cần self-host — chỉ cần set 2 env var cho API key khi Hermes gọi trực tiếp
export APIFY_TOKEN="[YOUR_APIFY_TOKEN]"
export TUBELAB_API_KEY="[YOUR_TUBELAB_KEY]"
```
> ⚠️ Cả 2 key đều trả phí theo lượng request — theo dõi usage tránh bill bất ngờ.

---
name: storyboard-generator
description: >
  Nhận 1 URL tool/AI product (+ affiliate link nếu có) → fetch thông tin thật (README,
  metadata, stars, tính năng) → soạn storyboard.json 6 scene cho pipeline render Playwright.
  Dùng skill này ngay sau bước Affiliate Research, trước khi render bất cứ gì.
  Trigger: "/promo [URL]", "làm storyboard cho tool này", "soạn kịch bản review [tool]".
---

# Storyboard Generator

Input: 1 URL (GitHub repo, web tool, sản phẩm AI bất kỳ) + optional `affiliate_link`.
Output: `storyboard.json` — kịch bản 6 scene, sẵn sàng đưa qua Compliance Gate rồi render.

## Quy trình

### Bước 1 — Fetch dữ liệu thật
- Nếu là GitHub repo: lấy README, package.json/pyproject.toml, số stars/forks, license.
- Nếu là web tool: fetch trang chủ, tìm tagline, tính năng chính, pricing, testimonial nếu có.
- KHÔNG bịa số liệu. Nếu không tìm ra 1 mục nào (vd không có testimonial công khai) → bỏ
  scene đó ở bước 2, không tự chế quote giả.

### Bước 2 — Soạn 6 scene theo khung chuẩn

```
1. hook        (hero-text)        — vấn đề mà tool này giải quyết, câu giật ngay 2-3s đầu
2. tool-intro  (hero-text)        — tên tool + tagline gốc (không tự đặt lại tagline)
3. demo        (terminal/iframe)  — lệnh cài đặt thật, hoặc demo tương tác nếu có
4. stats       (stats-grid)       — số liệu thuyết phục: stars, tốc độ, thời gian tiết kiệm...
5. quote       (quote)            — testimonial thật nếu tìm được; BỎ scene nếu không có
6. cta-url     (cta-url)          — "Link trong mô tả" + affiliate_link nếu có, nếu không có
                                     affiliate thì dùng link gốc tool
```

### Bước 3 — Gắn affiliate vào scene cta-url
- Nếu Affiliate Research (bước trước) xác nhận có chương trình → điền `affiliate_link` đã
  qua `/affiliate setup-tracking` (link tracking chuẩn, không tự chế UTM tay).
- Nếu KHÔNG có chương trình affiliate cho tool này → điền link gốc, KHÔNG gắn link giả,
  KHÔNG bỏ trống scene (vẫn cần CTA dẫn traffic dù không kiếm được hoa hồng).

### Bước 4 — Tính duration mỗi scene
Tổng target 25-32 giây. Phân bổ theo trọng số nội dung (scene demo/stats thường cần dài
hơn hook/CTA), không chia đều máy móc.

## Format output

```json
{
  "title": "Tool Name",
  "source_url": "https://...",
  "affiliate_link": "https://...?ref=... hoặc null",
  "duration": 28,
  "scenes": [
    {
      "type": "hero-text",
      "duration": 4,
      "content": { "headline": "...", "subtitle": "..." }
    },
    {
      "type": "terminal",
      "duration": 5,
      "content": { "command": "...", "output": "..." }
    },
    {
      "type": "stats-grid",
      "duration": 4,
      "content": { "stats": [{"label": "...", "value": "..."}] }
    },
    {
      "type": "cta-url",
      "duration": 4,
      "content": { "text": "Link trong mô tả", "url": "...", "is_affiliate": true }
    }
  ]
}
```

## Guardrail
- KHÔNG bịa số liệu, testimonial, hay tính năng tool không có thật.
- Storyboard PHẢI qua người review (Bước "Mày review & approve" trong pipeline) trước khi
  đưa sang Compliance Gate — skill này chỉ soạn draft, không tự động render.
- Sau khi review xong, đẩy tiếp sang `compliance-gate` để kiểm structural variation trước
  khi render — không bỏ qua bước này dù storyboard đã được approve nội dung.

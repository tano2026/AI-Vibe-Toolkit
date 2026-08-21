---
name: cross-channel-distribution-analysis
description: >
  So sánh hiệu suất cùng 1 content được repurpose qua nhiều platform
  (TikTok/YouTube/Instagram) để quyết định dồn lực phân phối vào đâu.
  Dùng vidIQ MCP đã có sẵn trong hệ thống. Khác media-performance-discipline
  (đánh giá 1 content trên 1 kênh) — skill này so sánh NGANG giữa các kênh.
---

# Cross-Channel Distribution Analysis

## TL;DR
1 content gốc cắt ra đăng TikTok/YouTube Shorts/Instagram Reels — mỗi kênh có văn hoá/thuật toán khác nhau, cùng 1 content có thể thắng ở kênh này, thua ở kênh khác. Không có bước so sánh ngang = không biết nên dồn lực sản xuất/phân phối vào kênh nào.

## Khi nào dùng
- Sau khi 1 content đã đăng đủ cả 3 kênh chính (TikTok/YouTube Shorts/Instagram Reels) và đã qua 24-72h (đúng luật đánh giá trong `media-performance-discipline`)
- Định kỳ (hàng tháng) review xem kênh nào đang là kênh chính thật sự cho từng loại content
- Cân nhắc mở rộng sang kênh mới — cần baseline so sánh trước

## Nội dung skill / prompt

### Quy trình so sánh

```
1. Lấy dữ liệu từng kênh qua vidIQ MCP (đã kết nối sẵn):
   - vidiq_video_stats cho YouTube
   - vidiq_instagram_tiktok_outlier_search cho TikTok/Instagram (nếu áp dụng)

2. Chuẩn hoá metric để so sánh công bằng — KHÔNG so trực tiếp số view thô
   giữa các kênh (mỗi kênh có base audience khác nhau):
   - Retention/completion rate (đã chuẩn hoá theo %, so được ngang kênh)
   - Engagement rate = (like+comment+share) / view — so được ngang kênh
   - Follow-through rate (nếu có CTA) — % người xem thực hiện hành động

3. Áp cùng ngưỡng phân loại từ media-performance-discipline (a/b/c) cho
   TỪNG kênh riêng — 1 content có thể là loại (b) ở TikTok nhưng loại (c)
   ở Instagram, đây chính là insight cần tìm.

4. Kết luận theo pattern lặp lại (không kết luận từ 1 content đơn lẻ):
   - Theo dõi ≥5 content cùng loại qua đủ 3 kênh trước khi kết luận
     "kênh X hợp loại content Y" — 1 lần ăn may không phải pattern
```

### Output chuẩn

```markdown
## Cross-Channel Report — [Loại content] — [khoảng thời gian]

| Kênh | Retention/Completion | Engagement rate | Phân loại (a/b/c) |
|---|---|---|---|
| TikTok | X% | Y% | (a)/(b)/(c) |
| YouTube Shorts | X% | Y% | (a)/(b)/(c) |
| Instagram Reels | X% | Y% | (a)/(b)/(c) |

**Pattern quan sát được** (chỉ kết luận nếu ≥5 content cùng loại):
[Kênh nào nhất quán thắng cho loại content này, vì sao có thể — khác biệt
văn hoá/thuật toán/đối tượng]

**Khuyến nghị phân bổ:** [dồn lực sản xuất/phân phối kênh nào cho loại
content này, giữ nguyên/giảm kênh nào]
```

## Setup từng bước
1. Xác định loại content cần so sánh (vd "video mẹo Fast Track" — không so sánh chéo loại content khác nhau)
2. Gom ≥5 content cùng loại đã đăng đủ 3 kênh, đủ 24-72h
3. Lấy data qua vidIQ MCP cho từng kênh
4. Chuẩn hoá về engagement rate/retention %, không so số thô
5. Phân loại (a)/(b)/(c) riêng từng kênh theo đúng ngưỡng đã có
6. Tìm pattern lặp lại, viết report theo format chuẩn, đưa khuyến nghị phân bổ

## Ví dụ thực tế
5 video "mẹo Fast Track" gần nhất của Trùm Sân Bay: TikTok trung bình retention 68% (gần ngưỡng tốt), Instagram Reels chỉ 40% dù cùng nội dung — pattern lặp lại rõ qua cả 5 video. Kết luận: loại content "mẹo nhanh, thông tin đặc" hợp TikTok hơn Instagram (có thể vì đối tượng Instagram của kênh này thiên về thẩm mỹ/lifestyle hơn thông tin thực dụng) → khuyến nghị dồn ngân sách edit/thời gian cho bản TikTok kỹ hơn, bản Instagram làm nhanh/tối giản không cần đầu tư ngang bằng.

## Lưu ý / Lỗi thường gặp
- Đừng kết luận từ 1 content — cần pattern lặp lại ≥5 lần mới đủ tin, 1 video thắng/thua có thể do yếu tố ngẫu nhiên (thời điểm đăng, sự kiện đang hot...)
- So sánh số view thô là sai — kênh có nhiều follower hơn tự nhiên có view cao hơn, không phản ánh content đó thật sự "hợp" kênh nào
- Đừng bỏ qua context văn hoá kênh — TikTok/Instagram/YouTube có kỳ vọng định dạng khác nhau, không phải lỗi sản xuất nếu 1 kênh thấp hơn

## Đánh giá cá nhân
- Điểm mạnh: tận dụng đúng vidIQ MCP đã có sẵn, không cần setup thêm gì; insight phân bổ nguồn lực theo kênh có giá trị thực tế cao cho content xưởng đa kênh
- Điểm yếu: cần đủ volume content (≥5/loại) mới có pattern đáng tin — kênh mới/ít content chưa dùng được ngay
- Có nên dùng: 8/10 — đặc biệt giá trị khi có ≥2 kênh phân phối song song cho cùng loại content

## Link
- Dùng chung: `agents/media-pro/skills/media-performance-discipline` (ngưỡng phân loại a/b/c)
- Tool: vidIQ MCP (đã kết nối sẵn trong hệ thống)

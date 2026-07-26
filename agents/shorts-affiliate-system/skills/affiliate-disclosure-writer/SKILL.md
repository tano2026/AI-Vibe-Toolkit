---
name: affiliate-disclosure-writer
description: >
  Sinh description + pinned comment cho video có affiliate link, kèm disclosure hợp lệ.
  Chạy SAU platform-disclosure-adapter (disclosure AI-content), TRƯỚC bước Publish.
  Đây là lớp disclosure AFFILIATE — độc lập với disclosure AI-generated, không thay thế nhau.
  Trigger: "viết description có affiliate", "gắn disclosure cho video này", sau khi video
  render xong và storyboard có affiliate_link != null.
---

# Affiliate Disclosure Writer

Vị trí trong pipeline: **sau** Platform Disclosure Adapter, **trước** Publish.
Chỉ chạy khi `storyboard.affiliate_link != null`. Nếu video không có affiliate → bỏ qua
toàn bộ skill này, không tạo description rác.

## Input
- `affiliate_link` (đã qua `/affiliate setup-tracking`, có UTM chuẩn)
- `platform` (YouTube / TikTok / Reels)
- Tên tool + 1 câu tóm tắt (lấy từ storyboard.json, không viết lại từ đầu)

## Output

### Description block
1-2 câu giới thiệu (đồng nhất giọng với script, không PR quá đà) + link tracking +
dòng disclosure. Mẫu:

```
Mình có test [Tool Name] — [1 câu điểm mạnh thật, không phóng đại].
Link dùng thử: [affiliate_link]

*Đây là link liên kết (affiliate). Nếu mày mua qua link này, kênh có thể nhận hoa hồng,
không phát sinh thêm chi phí cho mày.*
```

### Pinned comment (chỉ YouTube)
Rút gọn: link + 1 câu CTA ngắn, KHÔNG lặp lại nguyên văn disclosure dài (description đã
có), nhưng vẫn phải có từ "affiliate" hoặc "liên kết" xuất hiện.

```
🔗 Link dùng thử [Tool Name] (link liên kết/affiliate): [affiliate_link]
```

## Guardrail bắt buộc — KHÔNG ĐƯỢC BỎ QUA

1. **Không bao giờ để trống disclosure khi có affiliate link** — vi phạm quy định quảng
   cáo (FTC-style cho YouTube, tương đương cho TikTok/Meta), rủi ro pháp lý cao hơn cả
   rủi ro compliance AI-content.
2. **Nếu affiliate_link không xác nhận được** (link chết, chương trình đã đóng từ lúc
   research đến lúc publish) → KHÔNG tự bịa link thay thế, dừng lại và flag về hàng đợi
   review, không tự publish.
3. **2 lớp disclosure độc lập, không thay thế nhau**: disclosure AI-generated (từ
   `platform-disclosure-adapter`) và disclosure affiliate (skill này) — nếu video vừa
   AI-gen vừa có affiliate, cả 2 PHẢI cùng xuất hiện.
4. **Giới hạn ký tự theo platform**: kiểm tra description không bị nền tảng cắt (truncate)
   mất phần disclosure — nếu description dài, ưu tiên đặt disclosure ở đầu hoặc trong 2-3
   dòng đầu, không đẩy xuống cuối.
5. **Nhiều sản phẩm trong 1 video** (vd "top 5 AI tools"): mỗi sản phẩm 1 link riêng, đánh
   số khớp đúng thứ tự nhắc trong video, mỗi link đều nằm trong phạm vi disclosure chung.

## Ví dụ thực tế
Video review "Claude Code vs Cursor" có affiliate link cho gói Cursor Pro:
```
Mình có test Cursor Pro cho công việc code hằng ngày — autocomplete nhanh hơn hẳn bản free.
Link dùng thử: https://cursor.sh/pricing?ref=tano-aff-01

*Đây là link liên kết (affiliate). Nếu mày đăng ký qua link này, kênh có thể nhận hoa hồng,
không phát sinh thêm chi phí cho mày.*
```

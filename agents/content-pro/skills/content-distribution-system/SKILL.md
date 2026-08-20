---
name: content-distribution-system
description: >
  Đăng content xong không phải là xong — mỗi content asset phải gắn kế
  hoạch phân phối cụ thể (owned/earned/paid), không chỉ đăng rồi hy vọng
  thuật toán tự đẩy. Dùng ngay sau bước Publish trong editorial-workflow,
  và định kỳ audit content cũ xem có cần refresh/tái phân phối không.
---

# Content Distribution System

## TL;DR
"Publishing is a handoff, not a finish line" — đăng xong mới là bắt đầu, không phải kết thúc. Mỗi content quan trọng cần gắn sẵn 3-5 task phân phối cụ thể trước khi tính là "xong việc", theo mô hình owned/earned/paid.

## Khi nào dùng
- Ngay sau khi 1 content được publish (Bước 5 trong `editorial-workflow-quality-gates`)
- Audit định kỳ content cũ — xem cái nào đáng refresh/tái phân phối thay vì để chết
- Khi thấy content "đăng rồi im" — có sản xuất nhưng không ai chủ động đẩy đi

## Nội dung skill / prompt

### Mô hình Owned/Earned/Paid (áp cho mỗi content quan trọng)

| Loại kênh | Ví dụ | Vai trò |
|---|---|---|
| Owned | Kênh TikTok/YouTube riêng, email list, website | Kiểm soát hoàn toàn, không phụ thuộc thuật toán bên ngoài |
| Earned | Được nhắc lại tự nhiên (chia sẻ, báo chí nhắc, cộng đồng thảo luận) | Không mua được, nhưng thiết kế content dễ được share sẽ tăng khả năng này |
| Paid | Quảng cáo trả phí đẩy content | Dùng khi có ngân sách, đẩy nhanh content đã chứng minh hiệu quả organic trước |

### Checklist phân phối bắt buộc (3-5 task/content quan trọng)

```
Với MỖI content chính (không áp cho content phụ/thử nghiệm):
□ Đăng kênh chính (owned)
□ 3-5 social post ngắn trích từ content chính (repurpose, dùng
  automation-content-repurposer nếu có)
□ Gửi email/thông báo nếu có list phù hợp (owned)
□ Cross-post sang platform phụ nếu format phù hợp
□ (Nếu có ngân sách) Cân nhắc paid boost SAU KHI đã thấy tín hiệu
  organic tốt — không boost mù content chưa kiểm chứng
```

### Content Decay & Refresh Cycle (mới — chu kỳ rút ngắn 2026)

**[FACT, nguồn Digital Applied 2026]** Chu kỳ làm mới content đã rút ngắn từ 18 tháng xuống còn **6-8 tháng** do biến động AI-generated SERP — content cũ mất hiệu quả nhanh hơn trước nhiều.

```
Audit định kỳ (mỗi 6-8 tháng cho content quan trọng, dài hạn):
1. Content nào từng hiệu quả (view/engagement cao) nhưng đang giảm?
2. Thông tin trong đó có còn đúng không? (giá cả, quy định, số liệu)
3. Có nên: (a) update nội dung + đăng lại, (b) viết bản mới thay thế,
   hay (c) để nguyên vì vẫn còn giá trị?
4. Nếu update — chạy lại qua editorial-workflow-quality-gates như content mới,
   không skip gate vì "chỉ là sửa"
```

## Setup từng bước
1. Với mỗi content pillar quan trọng, thiết kế sẵn template phân phối (3-5 task chuẩn, không nghĩ lại mỗi lần)
2. Sau publish, tự động tạo checklist phân phối (Airtable/Sheet) — track đã làm tới đâu
3. Định kỳ 6-8 tháng, audit content cũ theo pillar — ưu tiên pillar có traffic/giá trị cao trước
4. Content cần refresh → đưa lại vào editorial-workflow như content mới

## Ví dụ thực tế
1 video Trùm Sân Bay về "Fast Track giá bao nhiêu" — sau khi đăng TikTok (owned), cắt thành 3-5 đoạn ngắn cho story/repost, cân nhắc gửi qua Zalo OA cho khách đang hỏi giá (owned, đúng đối tượng), sau 6-8 tháng audit lại xem giá đã đổi chưa (dịch vụ hay đổi giá theo mùa) — nếu đổi, update ngay chứ không để thông tin sai tồn tại.

## Lưu ý / Lỗi thường gặp
- Đừng paid-boost content chưa kiểm chứng organic — tốn tiền đẩy thứ chưa ai quan tâm tự nhiên
- Repurpose không phải copy-paste y nguyên sang platform khác — mỗi platform cần điều chỉnh format (đã có `content-engine` xử lý phần này)
- Quên audit content cũ là lỗi phổ biến nhất — content "để đó" âm thầm mất giá trị, đặc biệt content có thông tin giá/số liệu dễ lỗi thời

## Đánh giá cá nhân
- Điểm mạnh: đơn giản, biến "đăng xong quên" thành quy trình có checklist rõ; refresh cycle là insight mới đáng giá (nhiều kênh chưa ý thức content cũ cần chăm sóc định kỳ)
- Điểm yếu: audit định kỳ tốn công nếu có quá nhiều content — cần ưu tiên content pillar quan trọng trước, không audit dàn trải hết
- Có nên dùng: 8/10 — đặc biệt quan trọng cho content có thông tin dễ đổi (giá, quy định) như Trùm Sân Bay/ABTRIP

## Link
- The AI CMO — Content Distribution Strategy Playbook 2026
- Digital Applied — Content Calendar Template 2026 (nguồn refresh cycle 6-8 tháng)

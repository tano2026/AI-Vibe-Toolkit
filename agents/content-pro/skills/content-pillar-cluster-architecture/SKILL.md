---
name: content-pillar-cluster-architecture
description: >
  Xây khung chủ đề (pillar + cluster) TRƯỚC KHI viết bất kỳ bài/video đơn lẻ
  nào. Dùng khi bắt đầu content mới cho 1 kênh/brand, hoặc khi content hiện
  tại rời rạc, không liên kết, không rank/không giữ chân người xem theo hệ
  thống. Đây là lớp chiến lược đứng trên mọi skill viết chiến thuật
  (viral-hooks, content-engine, brand-voice...).
---

# Content Pillar/Cluster Architecture

## TL;DR
Bài đơn lẻ, rời rạc không còn hiệu quả năm 2026 — thuật toán/AI answer engine ưu tiên nội dung có cấu trúc chủ đề rõ (pillar + cluster liên kết nội bộ). Trước khi viết bài đầu tiên, phải có khung chủ đề — không phải nghĩ ra rồi viết, viết xong mới nghĩ liên kết.

## Khi nào dùng
- Bắt đầu content mới cho kênh/brand chưa có khung chủ đề rõ ràng
- Content hiện tại đã có nhiều bài nhưng rời rạc, không internal link, không thấy pattern chủ đề
- Trước khi giao việc viết cho `content-engine`/`viral-hooks` — pillar phải có trước, không phải song song

## Nội dung skill / prompt

### Định nghĩa
- **Pillar** (trụ cột): 1 chủ đề lớn, đủ rộng để "neo" nhiều bài con, đại diện 1 mảng năng lực/chuyên môn cốt lõi của brand
- **Cluster** (nhóm bài con): 8-15 bài/video xoay quanh 1 pillar, mỗi bài trả lời 1 câu hỏi cụ thể trong mảng đó, liên kết nội bộ về lại pillar

### Quy trình xây khung (chạy 1 lần trước khi có content đầu tiên)

```
Bước 1 — Liệt kê 3-5 Pillar dựa trên: chuyên môn thật của brand + câu hỏi
         khách hàng thật sự hỏi (không phải chủ đề "nghe hay" nhưng brand
         không có thẩm quyền nói về nó)

Bước 2 — Với mỗi Pillar, brainstorm 8-15 Cluster topic (câu hỏi cụ thể con
         người thật hỏi, không phải từ khóa SEO khô khan)

Bước 3 — Map định dạng phù hợp mỗi cluster: bài viết dài, video ngắn,
         thread, infographic — không phải mọi cluster đều hợp mọi định dạng

Bước 4 — Thiết kế internal link: mỗi bài cluster PHẢI link về pillar + ít
         nhất 1-2 cluster liên quan cùng pillar
```

### Bảng kiểm trước khi duyệt khung
| Câu hỏi | Fail nếu |
|---|---|
| Pillar có đủ rộng để chứa 8-15 bài không bị lặp ý không? | Pillar quá hẹp, cạn ý sau 3-4 bài |
| Brand có thẩm quyền thật nói về pillar này không? | Chọn pillar "hot" nhưng brand không chuyên |
| Cluster topic có phải câu hỏi người thật hỏi không? | Suy nghĩ hộ khách hàng thay vì hỏi/nghiên cứu thật |
| Có kế hoạch internal link cụ thể chưa? | Chỉ có danh sách bài, chưa nghĩ liên kết |

## Setup từng bước
1. Xác định 3-5 Pillar cho brand (dùng insight có sẵn từ `primary-research-design`/`social-listening-research` nếu đã research khách hàng)
2. Với mỗi Pillar, brainstorm cluster topics — có thể dùng `research-trending-content-scout` để tìm chủ đề đang được hỏi nhiều
3. Duyệt khung qua bảng kiểm trên trước khi giao viết
4. Giao từng cluster topic cho skill viết phù hợp (`content-engine` cho đa nền tảng, `content-tiktok-script-writer` cho riêng TikTok...)
5. Lưu khung vào tracker (Airtable/Sheet) — đây là tài liệu sống, cập nhật khi có cluster mới

## Ví dụ thực tế
Trùm Sân Bay: thay vì nghĩ ý tưởng video từng ngày rời rạc, xây 4 Pillar: "Thủ tục sân bay" / "Mẹo tiết kiệm khi bay" / "Review dịch vụ sân bay" / "Kinh nghiệm bay quốc tế lần đầu". Pillar "Thủ tục sân bay" có cluster: "Fast Track là gì", "Check-in trước bao lâu", "Hành lý xách tay bao nhiêu kg"... mỗi video link về nhau, xem xong 1 video dễ dẫn qua video khác cùng pillar — giữ chân người xem theo hệ thống thay vì đơn lẻ.

## Lưu ý / Lỗi thường gặp
- Đừng chọn Pillar theo "trend đang hot" nếu brand không có thẩm quyền thật — dễ tạo content generic, mất niềm tin dài hạn
- Cluster cạn ý sau vài bài là dấu hiệu Pillar chọn quá hẹp — xem lại Bước 1
- Quên internal link là lỗi phổ biến nhất — pillar/cluster không có link qua lại thì không khác gì bài rời rạc, chỉ là gắn nhãn suông

## Đánh giá cá nhân
- Điểm mạnh: giải quyết đúng vấn đề "content rời rạc không rank" — nghiên cứu 2026 xác nhận rõ ràng đây không còn là gợi ý, mà gần như bắt buộc
- Điểm yếu: cần đầu tư thời gian trước khi có bài đầu tiên — không hợp cho case cần content gấp trong ngày
- Có nên dùng: 9/10 — bắt buộc cho kênh mới hoặc kênh muốn tái cấu trúc, không cần cho content one-off/thời sự

## Link
- Digital Applied — Content Calendar Template 2026 (nguồn cluster 8-15 bài/pillar)
- DMA — Content Strategy 2026 Guide (10-element template)

---
name: platform-policy-intelligence
description: >
  Nghiên cứu chuyên sâu chính sách nền tảng (TikTok/YouTube/Meta), quy định AI-content
  disclosure, tín hiệu thuật toán phân phối, xu hướng — duy trì "ghi nhớ" cập nhật theo
  thời gian, dịch thành guardrail + checklist tối ưu cụ thể đưa cho Writer Agent và
  Media/Visual Agent TRƯỚC khi họ sản xuất, để tăng tỷ lệ được đề xuất (For You/Suggested/
  Explore) và tránh vi phạm chính sách.
  Dùng skill này ĐẦU TIÊN trong mọi content pipeline (trum-san-bay, shorts-affiliate-system,
  yt-cashcow) trước khi Writer/Visual bắt đầu sản xuất — không phải bước kiểm tra sau khi
  đã làm xong.
  Trigger: bắt đầu 1 chu kỳ content mới, nghi ngờ reach giảm bất thường, có tin đồn/thông
  báo thay đổi thuật toán, chuẩn bị mở kênh/định dạng mới.
---

# Platform Policy Intelligence

Vai trò: lớp tình báo chính sách/thuật toán ĐỨNG TRƯỚC toàn bộ pipeline sản xuất —
không phải guardrail chạy sau khi Writer/Visual đã làm xong (đó là việc của
`compliance-gate` và `platform-disclosure-adapter`, 2 skill hẹp hơn đã có sẵn). Skill
này rộng hơn: theo dõi chính sách + thuật toán + xu hướng, giữ ghi nhớ liên tục, và
CHỦ ĐỘNG đưa checklist tối ưu cho Writer/Media trước khi họ bắt tay vào việc.

## Quy trình

### Bước 1 — Check ghi nhớ trước khi research lại từ đầu
Đọc `memory/{platform}.md` tương ứng. Nếu bản ghi nhớ mới cập nhật trong 30 ngày gần
nhất VÀ không có dấu hiệu thay đổi lớn (xem Bước 4) → dùng thẳng ghi nhớ hiện có, KHÔNG
research lại từ đầu — tiết kiệm thời gian, tránh lặp việc.

### Bước 2 — Research có mục tiêu (nếu ghi nhớ cũ hoặc thiếu)
Research theo 4 nhóm câu hỏi cố định cho mỗi platform:
```
1. TÍN HIỆU PHÂN PHỐI — nền tảng ưu tiên gì để đẩy content lên For You/Suggested/Explore?
   (completion rate, rewatch, saves, comment quality, session contribution...)
2. QUY ĐỊNH AI-CONTENT — khi nào bắt buộc disclosure, cơ chế detect, hậu quả nếu bỏ sót
3. QUY ĐỊNH GỐC/ORIGINALITY — nền tảng có phạt cross-post/repost/nội dung "không đủ mới"
   không, ngưỡng là gì
4. YÊU CẦU ĐỊNH DẠNG — tỷ lệ khung hình, độ dài tối ưu, giới hạn caption/hashtag
```
Ưu tiên nguồn: trang chính sách/Help Center chính thức của nền tảng > tuyên bố công khai
từ lãnh đạo nền tảng (vd Adam Mosseri) > bài phân tích từ agency/tool uy tín (vidIQ,
SocialPilot...) có trích dẫn nguồn rõ ràng. KHÔNG dùng nguồn đồn đoán/forum không kiểm
chứng được.

### Bước 3 — Cập nhật ghi nhớ (append-only, có ngày tháng)
Ghi vào `memory/{platform}.md` theo format cố định (xem file mẫu) — KHÔNG xoá lịch sử cũ,
chỉ thêm entry mới có ngày, để nhìn được xu hướng thay đổi theo thời gian, không chỉ trạng
thái hiện tại.

### Bước 4 — Dấu hiệu cần research lại dù ghi nhớ còn mới
- Có thông báo chính thức từ nền tảng (Newsroom/Business Help Center) về thay đổi lớn.
- Reach giảm bất thường không giải thích được bằng nguyên nhân nội dung.
- Chuẩn bị mở định dạng/kênh mới chưa từng làm.

### Bước 5 — Dịch ghi nhớ thành handoff cho Writer + Media
Dùng `handoff-template.md` — KHÔNG đưa thẳng bài research dài cho Writer/Media đọc, phải
rút gọn thành checklist hành động được (xem Bước 6 output format).

## Output — 2 bản riêng, không gộp chung

### Cho Writer Agent
- Danh sách chủ đề/format bị hạn chế phân phối (không phải "cấm" — là "hạn chế reach")
- Độ dài tối ưu theo platform hiện tại
- Yêu cầu disclosure phải xuất hiện trong caption/description (câu chữ cụ thể)
- Tín hiệu engagement nên thiết kế vào hook/CTA (vd TikTok 2026: 3-5 giây đầu quyết định,
  comment chất lượng cao quan trọng hơn số lượng like)

### Cho Media/Visual Agent
- Tỷ lệ khung hình bắt buộc theo platform
- Vị trí đặt AI-disclosure label (khác nhau: TikTok toggle lúc đăng, YouTube overlay góc
  dưới trái với Shorts, Meta "Made with AI" tự động qua metadata C2PA/IPTC)
- Cảnh báo cross-post: Meta 2026 phạt nặng nội dung đăng lại gần như nguyên bản từ nền
  tảng khác (kể cả có watermark nền tảng gốc) — ảnh hưởng trực tiếp tới mô hình
  "1 caption → Adapter co giãn 4 platform" đang dùng ở `trum-san-bay`, cần asset/edit
  đủ khác biệt giữa các bản, không chỉ đổi caption.

## Guardrail

- KHÔNG trình bày thông tin từ nguồn không chính thức như đã verify 100% — luôn phân biệt
  "chính sách công bố chính thức" vs "phân tích/suy đoán từ agency thứ 3".
- KHÔNG để Writer/Media tự đọc bài research dài — bắt buộc qua bước rút gọn (Bước 5),
  tránh chìm trong chi tiết không hành động được.
- Ghi nhớ là APPEND-ONLY — sai lệch phát hiện sau thì thêm entry đính chính có ngày, không
  xoá sửa lịch sử, để biết tại sao 1 quyết định trước đó dựa trên thông tin gì.

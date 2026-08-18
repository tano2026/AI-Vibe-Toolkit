---
name: channel-analytics-autopilot
description: >
  Bộ 7 prompt Gemini/Claude cho content-ops kênh video (phân tích kênh, tìm
  chủ đề, lên lịch 30 ngày, viết hook/tiêu đề, tối ưu sau đăng, nhân bản
  video, xây chiến lược tiếp theo) — kèm kiến trúc tự động kéo data thật
  thay vì dán tay. Dùng cho kênh YouTube (có vidIQ) hoặc TikTok (cần export
  CSV thủ công).
origin: >
  Prompt gốc từ Nguyễn Tất Kiêm (nguyentatkiem.com, kênh aiformarketing0) —
  đã bỏ phần hype ("22 triệu view", "giao kênh cho AI vận hành"), giữ lại
  phần prompt thực dùng được, bổ sung kiến trúc tự động hoá thật.
---

# Channel Analytics Autopilot — Prompt Template / System Prompt

## TL;DR
7 prompt content-ops cho kênh video, từ phân tích điểm yếu tới lên lịch 30 ngày tới tối ưu sau đăng — dùng được ngay, nhưng KHÔNG phải "AI tự vận hành kênh" như quảng cáo gốc. Vẫn cần người dán data hoặc setup pipeline tự kéo data trước khi chạy prompt.

## ⚠️ Sự thật về mức tự động hoá
Nguồn gốc quảng cáo "chỉ cần giao kênh cho Gemini vận hành 30 ngày, nhận 22 triệu view" — kiểm tra 7 prompt gốc thì tất cả đều có placeholder `[DÁN DỮ LIỆU KÊNH]`, `[SỐ]`, `[TIÊU ĐỀ]`... nghĩa là **con người phải tự tay nhập data mỗi lần**, AI không tự vào YouTube/TikTok Studio lấy số liệu, không tự đăng bài. Đây là công cụ hỗ trợ phân tích + viết, không phải autopilot thật.

Muốn tự động hoá thật, cần thêm lớp kéo data — xem phần "Kiến trúc tự động hoá" bên dưới.

## Khi nào dùng
- Content Lead cần phân tích định kỳ hiệu suất kênh (Trùm Sân Bay, Airfare Decoded)
- Lên kế hoạch nội dung 30 ngày không muốn nghĩ từ đầu mỗi lần
- Tối ưu video sau khi đăng dựa trên số liệu thật thay vì đoán
- Muốn nhân 1 video thành nhiều định dạng nội dung khác nhau (repurpose)

## Nội dung skill / prompt

### #01 — Phân tích kênh & tìm điểm yếu
```
Hãy đóng vai chuyên gia phát triển kênh video.
Thông tin kênh của tôi:
- Chủ đề: [CHỦ ĐỀ]
- Đối tượng: [ĐỐI TƯỢNG]
- Số người đăng ký: [SỐ]
- Lượt xem trung bình: [SỐ]
- Nội dung hiện tại: [MÔ TẢ]
Hãy phân tích toàn bộ tình trạng kênh và chỉ ra:
- Điểm mạnh đang có.
- Điểm yếu đang kìm hãm tăng trưởng.
- Nội dung nào nên tiếp tục.
- Nội dung nào nên dừng.
- 3 việc quan trọng nhất cần làm ngay trong 30 ngày tới.
Hãy đưa ra nhận xét cụ thể dựa trên dữ liệu, không phân tích chung chung.
```

### #02 — Tìm chủ đề có tiềm năng view
```
Hãy đóng vai chuyên gia nghiên cứu nội dung cho kênh video trong lĩnh vực
[CHỦ ĐỀ]. Hãy tìm 20 chủ đề có tiềm năng thu hút người xem trong thời gian
tới. Với mỗi chủ đề, hãy phân tích:
- Vì sao người xem quan tâm.
- Insight hoặc vấn đề phía sau.
- Góc khai thác khác biệt.
- Khả năng phát triển thành series.
- Mức độ phù hợp với đối tượng [ĐỐI TƯỢNG].
Ưu tiên những chủ đề có khả năng tạo lượt xem nhưng chưa quá bão hoà.
```

### #03 — Xây lịch nội dung 30 ngày
```
Dựa trên chủ đề và đối tượng của kênh, hãy xây dựng kế hoạch nội dung
trong 30 ngày. Mỗi ngày hãy đề xuất:
- Chủ đề video. - Tiêu đề. - Hook 5 giây đầu. - Góc triển khai. - CTA.
- Format phù hợp.
Chia nội dung thành các nhóm: Thu hút người xem mới / Xây dựng uy tín /
Tăng tương tác / Chuyển đổi thành người theo dõi.
Không lặp lại ý tưởng và ưu tiên nội dung có khả năng phát triển thành series.
```

### #04 — Viết tiêu đề & hook khiến người xem bấm vào
```
Hãy đóng vai chuyên gia tối ưu tiêu đề và hook. Chủ đề video: [CHỦ ĐỀ].
Hãy tạo: 10 tiêu đề có tính tò mò cao / 10 hook cho 5 giây đầu / 5 phiên
bản thumbnail text.
Mỗi phiên bản phải: ngắn gọn, dễ hiểu, đánh đúng insight người xem, tạo
khoảng trống tò mò, KHÔNG clickbait sai sự thật.
Sau đó chọn ra 3 phương án mạnh nhất và giải thích ngắn gọn lý do.
```

### #05 — Tối ưu từng video sau khi đăng
```
Hãy phân tích video này dựa trên các dữ liệu tôi cung cấp:
- Tiêu đề: [TIÊU ĐỀ] - Thumbnail: [MÔ TẢ] - Lượt xem: [SỐ] - CTR: [SỐ]
- Thời lượng xem trung bình: [SỐ] - Retention: [SỐ] - Bình luận: [SỐ]
Hãy xác định: Video đang mạnh ở đâu? Người xem rời đi ở đâu? Tiêu
đề/thumbnail có vấn đề gì? Hook có đủ mạnh không? Tôi nên thay đổi điều gì?
Cuối cùng, đưa ra 5 điều chỉnh cụ thể cho video tiếp theo.
```

### #06 — Biến 1 video thành cả "cỗ máy" nội dung
```
Tôi có một video với nội dung sau: [DÁN NỘI DUNG/KỊCH BẢN]
Hãy biến video này thành một hệ thống nội dung gồm:
- 5 video ngắn. - 3 video mới khai thác góc nhìn khác. - 5 bài đăng cộng
đồng. - 10 câu hỏi kích thích bình luận. - 5 ý tưởng video tiếp theo.
Mỗi nội dung phải có góc tiếp cận khác nhau, không sao chép nguyên bản
video gốc.
```

### #07 — Xây chiến lược tăng trưởng 30 ngày tiếp theo
```
Dựa trên toàn bộ dữ liệu kênh trong 30 ngày vừa qua: [DÁN DỮ LIỆU KÊNH]
Hãy phân tích kết quả và xây dựng chiến lược 30 ngày tiếp theo. Hãy xác định:
- 3 loại nội dung cần nhân rộng. - 3 loại nội dung cần giảm hoặc dừng.
- Chủ đề cần tập trung. - Tần suất đăng phù hợp. - KPI cần theo dõi mỗi tuần.
- Những thử nghiệm cần thực hiện.
Cuối cùng, tạo cho tôi một checklist vận hành theo tuần để tôi chỉ cần
làm theo từng bước.
```

## Kiến trúc tự động hoá (biến thành thật, không dán tay)

```
Cron job (Antigravity, chạy định kỳ)
  → Bước 1: Kéo data thật
     - YouTube: gọi vidiq MCP (vidiq_channel_analytics, vidiq_video_stats) —
       kéo trực tiếp view/CTR/retention/comment thật
     - TikTok: chưa có API công khai dễ xin cho tài khoản cá nhân — export
       CSV thủ công từ TikTok Studio định kỳ, hoặc dùng skill scraping
       (nimble/brightdata) — kém ổn định hơn, cân nhắc kỹ trước khi tự động hoá
  → Bước 2: Tự động điền data thật vào đúng 7 prompt trên (thay placeholder)
  → Bước 3: Gọi Gemini/Claude qua OmniRoute chạy prompt
  → Bước 4: Lưu kết quả vào Airtable/file, báo qua Telegram cho Nobitano duyệt
  → Bước 5: Người duyệt xong mới đăng — KHÔNG tự publish
```

Nguyên tắc: tự động hoá phần thu thập + phân tích, giữ quyền duyệt cuối cho con người trước khi đăng — đúng tinh thần "propose, don't decide" đã áp cho CEO Agent.

## Setup từng bước
1. Với kênh YouTube (Airfare Decoded): xác nhận vidIQ MCP đã kết nối, test `vidiq_channel_analytics` lấy data thật
2. Với kênh TikTok (Trùm Sân Bay): thiết lập lịch export CSV thủ công từ TikTok Studio (vd mỗi thứ 2 hàng tuần), lưu vào Airtable/Google Sheets
3. Viết script (Hermes/Antigravity) đọc data từ vidIQ/CSV, tự điền vào 7 prompt trên
4. Gọi OmniRoute route sang Gemini hoặc Claude tuỳ ngân sách (Gemini rẻ hơn cho task số lượng lớn)
5. Output lưu vào Airtable, gửi Telegram báo Nobitano review
6. Duyệt xong mới copy vào lịch đăng thật (Postiz hoặc thủ công)

## Ví dụ thực tế
Với Airfare Decoded: mỗi thứ 2, Antigravity tự chạy cron gọi vidIQ lấy data 7 ngày qua, tự điền vào prompt #01 (Phân tích kênh & tìm điểm yếu), gửi kết quả qua Telegram. Nobitano đọc trong 2 phút thay vì tự mở YouTube Studio soi số liệu — nhưng vẫn là Nobitano quyết định video nào dừng, chủ đề nào đẩy mạnh, không phải AI tự quyết.

## Lưu ý / Lỗi thường gặp
- Đừng tin theo đúng nghĩa đen "giao kênh cho AI vận hành" — không có cơ chế nào trong 7 prompt gốc cho phép AI tự đăng bài hay tự lấy data, đây là quảng cáo bán khoá học
- TikTok chưa có đường tự động kéo data sạch như YouTube — đừng hứa hẹn tự động hoá 100% cho Trùm Sân Bay ngay, cần chấp nhận 1 bước thủ công (export CSV)
- Prompt #06 (biến 1 video thành nhiều nội dung) dễ bị lạm dụng tạo nội dung trùng lặp/spam nếu không kiểm tra kỹ — nhớ điều kiện "mỗi nội dung phải có góc tiếp cận khác nhau" trong chính prompt
- Con số "22 triệu view" trong quảng cáo gốc không kèm bằng chứng (không tên kênh/link/ảnh Analytics thật) — không dùng số này làm kỳ vọng thật

## Đánh giá cá nhân
- Điểm mạnh: 7 prompt viết tốt, có placeholder rõ ràng, cấu trúc logic từ phân tích → lên kế hoạch → thực thi → tối ưu → lặp lại; dễ tích hợp vào pipeline agent sẵn có (Hermes/Antigravity/OmniRoute) vì bản chất chỉ là template text
- Điểm yếu: bản thân prompt không tự động — cần công mình xây lớp kéo data mới thật sự tiết kiệm thời gian; TikTok (kênh chính Trùm Sân Bay) khó tự động hoá hơn YouTube nhiều
- Có nên dùng không: 7/10 cho prompt gốc (dùng tốt nếu chấp nhận dán tay), 8/10 nếu đầu tư thêm lớp tự động hoá kéo data — đáng làm vì tận dụng được vidIQ đã có sẵn cho Airfare Decoded

## Link
- Nguồn prompt gốc: kênh TikTok @aiformarketing0, nguyentatkiem.com

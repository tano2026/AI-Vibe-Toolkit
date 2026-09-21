---
name: critical-path-briefing
description: >
  Nguyên tắc lọc báo cáo — chỉ đẩy lên đúng việc mà NGƯỜI DÙNG LÀ NGƯỜI DUY
  NHẤT gỡ được, không đẩy mọi thứ đang chạy tốt. Đúc kết từ mô hình "AI
  Employees" (Mark Fulton) — dùng cho MỌI agent cần báo cáo định kỳ (không
  riêng CSKH): Media Pro escalate, Sales-CEO forecast, Chief of Staff-style
  tổng hợp đa agent.
---

# Critical Path Briefing

## TL;DR
1 báo cáo dài liệt kê mọi thứ đang chạy = không ai đọc hết, việc quan trọng bị chìm. 1 báo cáo chỉ có đúng việc CẦN QUYẾT ĐỊNH CỦA BẠN = đọc xong biết ngay phải làm gì.

## Khi nào dùng
- Bất kỳ agent nào tổng hợp báo cáo định kỳ cho Nobitano (sáng/tuần)
- Agent điều phối (OpenClaw-style) tổng hợp log từ nhiều sub-agent khác
- Media Pro escalate, Sales-CEO forecast summary, Customer Satisfaction churn report

## Nội dung skill / prompt

### Bài test lọc — chỉ 1 câu hỏi duy nhất cho mỗi hạng mục

```
"Việc này có cần ĐÚNG QUYẾT ĐỊNH CỦA NGƯỜI DÙNG để đi tiếp không, hay
agent tự xử lý được?"

CÓ (chỉ người dùng gỡ được) → đưa vào báo cáo
KHÔNG (agent tự làm tiếp được, hoặc đang chạy bình thường) → KHÔNG đưa vào
```

### 3 loại việc CHẮC CHẮN cần đưa vào báo cáo

```
1. Cần DUYỆT trước khi hành động thật (tiền chạy, nội dung đăng công khai,
   deal đóng) — đúng nguyên tắc "propose, don't decide" đã áp toàn hệ thống
2. BỊ CHẶN vì thiếu thông tin/quyền hạn agent không tự có (cần tài khoản,
   cần quyết định chiến lược, cần xác nhận 1 sự thật ngoài đời)
3. RỦI RO đã vượt ngưỡng agent tự xử lý được (escalate rời bỏ khách,
   deploy-review-gate fail 3 lần, chi phí vượt ngân sách đã duyệt)
```

### Cấu trúc báo cáo chuẩn

```
[Hôm nay/Tuần này]
- Việc cần quyết định của bạn (tối đa 3-5 mục, xếp theo độ khẩn cấp)

[Đang chờ bạn — chưa ai gỡ]
- Việc đã đưa vào báo cáo trước đó nhưng chưa được xử lý (không lặp lại
  toàn bộ nội dung cũ, chỉ nhắc tên + số ngày đã chờ)

[Không cần làm gì — chỉ để biết]
- Tối đa 1-2 dòng tóm tắt "mọi thứ khác đang chạy bình thường"
  (KHÔNG liệt kê chi tiết từng việc đang chạy tốt)
```

### Nguyên tắc chống lạm phát báo cáo

```
Nếu 1 mục xuất hiện trong báo cáo 3 lần liên tiếp mà vẫn "đang chờ" →
đây là dấu hiệu mục đó bị đưa sai chỗ (có thể agent tự xử lý được nhưng
đang đẩy lên không cần thiết) — xem lại bài test lọc, không mặc định
đúng là cần người dùng mãi.
```

## Setup từng bước
1. Trước khi viết báo cáo, liệt kê hết các mục có khả năng đưa vào
2. Áp bài test lọc cho từng mục — chỉ giữ lại mục trả lời CÓ
3. Xếp theo cấu trúc 3 phần chuẩn
4. Nếu "Đang chờ bạn" có mục lặp lại >=3 kỳ báo cáo → tự hỏi lại có nên tự xử lý thay vì tiếp tục đẩy lên

## Ví dụ thực tế
Media Pro chạy xong 5 video Trùm Sân Bay trong tuần — 4 video hiệu suất bình thường (không cần đưa vào báo cáo chi tiết), 1 video bị escalate vì comment phàn nàn lặp >=3 lần liên quan tới thông tin sai (cần Nobitano xác nhận thông tin đúng trước khi Content sửa) → CHỈ mục thứ 5 lên báo cáo sáng, 4 video kia gộp thành 1 dòng "4 video khác chạy bình thường, xem chi tiết trong dashboard".

## Lưu ý / Lỗi thường gặp
- Đưa cả việc đang chạy tốt vào báo cáo "cho đầy đủ" — làm loãng, người đọc mất thời gian lọc lại việc thật quan trọng
- Lặp lại toàn bộ nội dung cũ mỗi lần nhắc "đang chờ" — chỉ cần tên việc + số ngày chờ, không cần kể lại từ đầu
- Không tự phát hiện việc bị đẩy sai chỗ (lặp >=3 kỳ vẫn "chờ") — bỏ lỡ cơ hội tự động hoá thêm

## Đánh giá cá nhân
- Điểm mạnh: 1 bài test lọc duy nhất, dễ áp dụng nhất quán cho mọi agent báo cáo; ngăn được lỗi phổ biến nhất của báo cáo tự động (liệt kê hết mọi thứ)
- Điểm yếu: cần agent tự đánh giá đúng "việc này agent tự làm được không" — nếu agent đánh giá sai (quá thận trọng), vẫn có thể đẩy quá nhiều lên báo cáo
- Có nên dùng: 8/10 — áp được cho mọi agent có báo cáo định kỳ, không riêng CSKH

## Link
- Nguồn cảm hứng: mô hình "AI Employees" (Mark Fulton, github.com/markfulton/ai-employees) — cơ chế Chief of Staff đọc log toàn bộ agent, chỉ đưa 3 nước đi quan trọng nhất
- Dùng cùng: churn-risk-escalation-discipline (Customer Satisfaction), media-performance-discipline (Media Pro escalate)

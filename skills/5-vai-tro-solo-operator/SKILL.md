---
name: 5-vai-tro-solo-operator
description: >
  Khung 5 vai trò cho người làm việc một mình với AI — Người nghiên cứu, Người
  biên tập, Người phản biện, Người vận hành, Người phân tích. Chỉ giao 1 vai
  trò cho 1 việc lặp lại nhiều nhất mỗi lần, không mở 5 trợ lý cùng lúc.
origin: Không rõ tác giả gốc (nhận qua chia sẻ nội bộ)
---

# 5 Vai Trò Solo Operator — Prompt Template / System Prompt

## TL;DR
Khung chia nhỏ việc AI hỗ trợ thành 5 vai trò rõ ràng cho người làm việc một mình — thay vì mở 20 công cụ hay 5 trợ lý cùng lúc, chọn đúng 1 vai trò cho đúng 1 việc lặp lại nhiều nhất, làm quen rồi mới mở rộng.

⚠️ Lưu ý đặt tên: kho đã có `skills/council/SKILL.md` — đó là "4-voice decision council" (Architect/Skeptic/Pragmatist/Critic) dùng cho quyết định go/no-go mơ hồ, KHÁC hoàn toàn skill này (5 role dùng cho việc lặp lại hàng ngày: content, ops, phân tích). Đừng nhầm 2 skill khi search hoặc gọi tên.

## Khi nào dùng
- Founder/solo operator thấy quá tải vì mở nhiều tool/tab AI cùng lúc, không biết giao việc gì cho cái nào
- Có 1 việc lặp lại hàng ngày/hàng tuần (vd: tối nào cũng ghi chú bán hàng, xử lý xong mới ngủ) muốn tự động hoá bằng đúng 1 vai trò AI
- Cần chuẩn hoá cách giao việc cho agent để không phải viết lại prompt từ đầu mỗi lần

## Nội dung skill / prompt

### 5 vai trò

| # | Vai trò | Việc làm |
|---|---|---|
| 1 | Người nghiên cứu | Gom thông tin, so sánh nguồn, chỉ ra điểm còn thiếu |
| 2 | Người biên tập | Làm câu chữ rõ hơn, không đổi ý chính |
| 3 | Người phản biện | Tìm lỗ hổng, rủi ro, câu hỏi khách có thể đặt ra |
| 4 | Người vận hành | Biến việc lặp lại thành checklist/quy trình |
| 5 | Người phân tích | Nhóm dữ liệu, phát hiện mẫu, gợi ý câu hỏi tiếp theo |

### Nguyên tắc triển khai
Đừng tạo cả 5 vai trò cùng lúc. Tuần đầu: chọn 1 việc lặp lại nhiều nhất trong ngày/tuần, giao đúng 1 vai trò xử lý việc đó. Ví dụ mẫu: mỗi tối đưa ghi chú bán hàng cho "Người vận hành" để tạo danh sách việc cần làm sáng mai.

### Công thức giao việc (copy dùng trực tiếp)
```
Bạn đang đóng vai [vai trò]. Đầu vào là [dữ liệu]. Hãy tạo [đầu ra] cho
[người sử dụng]. Không được [giới hạn]. Trước khi làm, hãy hỏi tối đa 3
câu nếu thiếu thông tin.
```

## Setup từng bước
1. Xác định việc lặp lại nhiều nhất trong tuần của mày (không phải việc "nghĩ nên làm" — việc thực sự đang lặp)
2. Chọn đúng 1 trong 5 vai trò khớp việc đó (vd: ghi chú bán hàng buổi tối → Người vận hành)
3. Điền công thức giao việc ở trên với dữ liệu/đầu ra/giới hạn cụ thể
4. Dán làm system prompt/task instruction cho agent (Claude Code, Mission Control, Paperclip...)
5. Chạy thử 3-5 lần, tinh chỉnh phần [giới hạn] nếu agent làm sai hướng
6. Ổn định rồi mới thêm vai trò thứ 2 cho việc lặp lại kế tiếp — không nhảy thẳng lên 5 vai trò

## Ví dụ thực tế
Áp cho ABTRIP: mỗi tối đưa ghi chú Zalo/tin nhắn khách trong ngày cho "Người vận hành":

```
Bạn đang đóng vai Người vận hành. Đầu vào là ghi chú/tin nhắn khách trong
ngày của ABTRIP (Fast Track, SIM, đổi tiền tại Nội Bài). Hãy tạo danh sách
việc cần làm sáng mai, sắp theo mức ưu tiên (khách đang chờ phản hồi > khách
mới hỏi giá > khách cũ cần follow-up), cho Nobitano dùng ngay sáng hôm sau.
Không được tự trả lời khách hoặc gửi tin nhắn thay. Trước khi làm, hãy hỏi
tối đa 3 câu nếu thiếu thông tin.
```

Trước khi dùng skill: Nobitano tự đọc lại tin nhắn tối hôm trước, mất 10-15 phút, dễ bỏ sót khách đang chờ.
Sau khi dùng skill: dán ghi chú vào, có ngay checklist sáng có thứ tự ưu tiên, mất <1 phút.

## Lưu ý / Lỗi thường gặp
- Nhầm vai trò dẫn tới output sai định dạng — vd giao "Người phân tích" nhưng kỳ vọng ra checklist hành động (đó là việc của "Người vận hành") → xác nhận đúng vai trò trước khi giao
- Không viết rõ [giới hạn] → agent có thể tự ý làm quá phạm vi (vd tự trả lời khách thay vì chỉ tạo checklist)
- Mở nhiều vai trò cùng lúc ngay từ đầu khiến khó đánh giá vai trò nào thực sự hữu ích — nên tuần tự từng cái một

## Đánh giá cá nhân
- Điểm mạnh: đơn giản, dễ nhớ, công thức giao việc rõ ràng, ép phải xác định đúng 1 việc lặp lại trước khi mở rộng — tránh over-engineering ngay từ đầu
- Điểm yếu: chỉ là khung prompt, không phải tool/skill tự động hoá thật — vẫn cần người tự dán prompt mỗi lần trừ khi setup thành recurring task trong Mission Control/Paperclip; 5 vai trò khá chung chung, cần tinh chỉnh thêm cho từng brand cụ thể (ABTRIP khác Wonder Mart khác Tano Cafe)
- Có nên dùng không: 7/10 — dùng tốt làm điểm khởi đầu cho người mới bắt đầu giao việc cho AI, nhưng nên nâng cấp lên thành recurring task tự động trong Mission Control (không cần dán tay mỗi tối) sau khi đã xác nhận vai trò đó hữu ích

## Link
- Nguồn gốc skill: chia sẻ nội bộ, chưa rõ tác giả gốc

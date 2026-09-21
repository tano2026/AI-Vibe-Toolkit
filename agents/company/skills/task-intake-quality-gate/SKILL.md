---
name: task-intake-quality-gate
description: >
  Vai trò "EA — Executive Assistant" đúc kết từ OneManCompany (OMC) —
  1 lớp gác cổng chất lượng TRƯỚC KHI task được giao cho Pro Agent nào,
  không phải OpenClaw tự route rồi thôi. Áp dụng bởi bất kỳ agent nào
  đóng vai điều phối (OpenClaw/DeepSeek Harness) trước khi dispatch.
---

# Task Intake Quality Gate (vai trò "EA")

## TL;DR
Nhận task từ Nobitano → không dispatch ngay cho Pro Agent — kiểm tra 4 điều trước, đúng 1 bài test nhanh, rồi mới giao đúng chỗ. Đây là khoảng trống thật: hiện tại OpenClaw route task nhưng không có bước "gác cổng chất lượng" tường minh trước khi giao.

## Khi nào dùng
- Bất kỳ agent điều phối nào (OpenClaw/DeepSeek Harness) nhận task mới từ Nobitano trước khi dispatch cho 1 trong 8 Pro Agent
- Task mơ hồ, chưa rõ nên giao cho agent nào

## Nội dung skill / prompt

### 4 câu hỏi gác cổng — chạy TRƯỚC dispatch, không sau

```
1. ĐÚNG AGENT? — Task này khớp domain của Pro Agent nào trong 8 cái?
   Nếu mơ hồ giữa 2 agent (vd vừa Content vừa Marketing) → xác định
   agent NÀO SỞ HỮU bước đầu tiên, agent kia nhận bàn giao sau

2. ĐỦ THÔNG TIN CHƯA? — Nếu thiếu, dùng Deepthink protocol (mượn từ OPC):
   HỎI TỪNG CÂU MỘT, không hỏi dồn 10 câu 1 lúc. Câu đầu tiên LUÔN LÀ
   hình thức giao (report/file/action thật?) — giống nguyên tắc đã có
   cho việc tạo file, giờ áp dụng cả cho routing nội bộ

3. VI PHẠM EXPERT-CORE RÕ RÀNG NGAY TỪ ĐẦU? — Task có yêu cầu bỏ qua
   review gate, hạ ngưỡng số, hay làm việc ngoài phạm vi "propose don't
   decide" không? Nếu có → dừng lại hỏi Nobitano xác nhận trước khi
   dispatch, không tự ý dispatch rồi để Pro Agent tự phát hiện sau

4. ĐỘ KHẨN? — Task có khớp tiêu chí trong critical-path-briefing (cần
   quyết định của Nobitano ngay) hay là việc thường? Việc khẩn đi thẳng,
   việc thường xếp hàng theo thứ tự nhận
```

### Verdict

```
Qua đủ 4 câu → dispatch cho đúng Pro Agent, kèm note ngắn "đã qua gate"
Fail câu 2 → hỏi lại 1 câu (không phải cả list), chờ trả lời rồi chạy lại gate
Fail câu 3 → KHÔNG dispatch, báo Nobitano trước
```

## Setup từng bước
1. Task mới vào → chạy đủ 4 câu hỏi theo thứ tự
2. Câu 1-2 thường trả lời được ngay nếu task đã rõ — không làm chậm việc đơn giản
3. Câu 3-4 chỉ cần chú ý khi task có dấu hiệu bất thường (yêu cầu lạ, khẩn cấp, chạm tới quyết định lớn)
4. Dispatch kèm ghi chú đã qua gate — để agent nhận việc biết task này đã được xác nhận đúng chỗ

## Ví dụ thực tế
Nobitano gõ nhanh "làm cho tao cái báo cáo CSKH" — EA gate chạy: (1) đúng Customer Satisfaction Pro, (2) thiếu thông tin (brand nào? khoảng thời gian nào?) → hỏi 1 câu "Brand nào — ABTRIP/Tano Cafe/Wonder Mart?" thay vì tự đoán hoặc hỏi dồn 5 câu, (3-4) không có dấu hiệu bất thường → sau khi có câu trả lời, dispatch thẳng.

## Lưu ý / Lỗi thường gặp
- Hỏi dồn nhiều câu 1 lúc — đúng anti-pattern OPC đã cảnh báo, làm chậm và gây khó chịu
- Bỏ qua câu 3 vì "chắc không sao" — đây chính xác là lỗ hổng khiến lỗi EXPERT-CORE lọt qua tới tận khi Pro Agent đã làm xong mới phát hiện
- Gate quá tay cho việc đơn giản, rõ ràng — làm chậm không cần thiết, chỉ cần đủ nghiêm cho task mơ hồ/rủi ro

## Đánh giá cá nhân
- Điểm mạnh: vá đúng lỗ hổng thật (không ai gác cổng trước dispatch hiện tại), mượn đúng 2 pattern đã kiểm chứng (Deepthink 1-câu-1-lần từ OPC, quality gate từ OMC)
- Điểm yếu: thêm 1 bước có thể làm chậm task đơn giản nếu áp cứng nhắc — cần agent điều phối tự cân nhắc mức độ cần thiết
- Có nên dùng: 8/10 — đáng áp ngay cho OpenClaw/DeepSeek Harness khi nhận task mới

## Link
- Nguồn: OneManCompany (EA role, "receives the task and routes it... quality gate"), opc_agent (Deepthink 1-câu-1-lần protocol)
- Dùng cùng: critical-path-briefing (câu hỏi 4 — độ khẩn), agents/company/EXPERT-CORE.md (câu hỏi 3)

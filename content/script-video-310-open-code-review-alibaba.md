# Script Video 310 — Open Code Review (Alibaba)

## Thông tin
- Tool/Repo/Skill liên quan: /repos/open-code-review-alibaba.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~55 giây

## Hook (3 giây đầu)
"Alibaba nói con AI review code của họ chính xác hơn Claude Code chín lần."

## Script voiceover (ElevenLabs-ready)
[Đoạn 1 — vấn đề/pain point]
Để Claude Code tự review một đống file thay đổi thì nó hay lười, chỉ đọc kỹ vài file rồi bỏ sót phần còn lại, comment cũng hay bị lệch dòng, lệch file, chất lượng không ổn định.

[Đoạn 2 — giới thiệu giải pháp]
Alibaba mở mã nguồn công cụ review code họ dùng nội bộ hai năm cho hàng chục nghìn kỹ sư. Cách làm khác hẳn, phần nào bắt buộc phải đúng như chọn file nào cần xem thì giao cho logic cứng quyết định, không để AI đoán. Phần nào cần linh hoạt mới giao cho AI Agent.

[Đoạn 3 — demo/cách làm]
Cài một dòng lệnh, gõ ocr review là nó tự nhóm các file liên quan lại review chung. Không cần trả thêm tiền API, cắm thẳng vào OpenCode hoặc Claude Code đang dùng sẵn, để chính agent đó tự chạy review bằng chìa khoá của mình.

[Đoạn 4 — kết + CTA]
Theo benchmark họ tự công bố, chính xác hơn Claude Code nhiều lần mà tốn ít token hơn chín lần, đổi lại là dễ bỏ sót lỗi hơn một chút. Link cài đặt đầy đủ tao để trong kho, comment "ocr" là gửi.

## Ghi chú quay (OBS)
- Cảnh 1: Cảnh AI review code bỏ sót file, comment lệch dòng (dựng minh hoạ) — lúc hook/pain point
- Cảnh 2: Sơ đồ 2 khối "Deterministic Engineering" và "Agent" ghép lại — lúc giới thiệu
- Cảnh 3: Terminal gõ `npm install -g @alibaba-group/open-code-review` rồi `ocr review` — lúc demo
- Cảnh 4: Show bảng benchmark (33.9% vs 7.2% precision) từ README gốc — lúc kết

## Caption/Sub note (CapCut)
Highlight: "chính xác hơn chín lần", "không cần trả thêm tiền API", "logic cứng quyết định", "dễ bỏ sót lỗi hơn". Đừng bỏ qua câu cuối về đánh đổi recall — giữ tính khách quan cho video.

## Thumbnail idea (Canva)
Cân thăng bằng, một bên là icon Claude Code, một bên là icon Alibaba OCR nặng hơn, text to: "ALIBABA CLAIM: REVIEW CODE CHUẨN HƠN CLAUDE CODE 9 LẦN".

## CTA cuối video
Comment "ocr" nhận link cài đặt + cách cắm vào OpenCode/Claude Code sẵn có, follow để xem thêm tool review code đáng thử.

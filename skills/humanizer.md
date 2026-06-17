# Humanizer — Prompt Template / System Prompt

## TL;DR
Skill cho Claude Code/OpenCode tự phát hiện và xóa "dấu vết viết bằng AI" trong văn bản — câu chữ rập khuôn, từ ngữ sáo mòn, cấu trúc đoán được — để output đọc tự nhiên như người thật viết, không lộ "mùi AI".

## Khi nào dùng
Dùng khi mày viết email, content, bài đăng, ghi chú mà Claude soạn ra rồi nhưng đọc lại thấy "mùi AI" rõ quá (quá nhiều gạch ngang em-dash, list bôi đậm tùm lum, mở bài kiểu "Great question!", kết bài kiểu "hy vọng giúp được mày"). Không hợp khi cần văn bản học thuật/kỹ thuật chính xác tuyệt đối từng chữ — vì mục tiêu của skill là viết lại theo văn phong tự nhiên, có thể đổi cấu trúc câu so với bản gốc.

## Nội dung skill / prompt
File `SKILL.md` gốc dài và được tác giả update thường xuyên (đang ở version 2.8.0, 33 pattern), nên lấy trực tiếp từ source thay vì copy lại nguyên văn ở đây:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/blader/humanizer.git ~/.claude/skills/humanizer
```

Cơ chế tóm tắt (diễn giải, không quote nguyên văn): skill dựa trên bộ hướng dẫn "Signs of AI writing" của Wikipedia (do nhóm WikiProject AI Cleanup duy trì, đúc kết từ hàng ngàn case văn bản AI thật). Skill quét văn bản theo 5 nhóm pattern — lỗi nội dung (như thổi phồng tầm quan trọng, gắn tên người nổi tiếng vô tội vạ), lỗi ngôn ngữ (từ vựng AI hay lặp, né dùng "is/has" mà thay bằng "serves as/features"), lỗi văn phong (lạm dụng em-dash, bôi đậm, tiêu đề Title Case, emoji), lỗi giao tiếp (kiểu chatbot "Great question!", rào trước đón sau), và lỗi rào đón/hedging dư thừa. Sau khi viết lại, skill còn chạy thêm 1 vòng audit cuối để bắt sót pattern còn sượng.

## Setup từng bước
1. Clone skill vào đúng folder Claude Code quét (lệnh ở phần trên).
2. Gọi lệnh trong Claude Code: `/humanizer` rồi paste đoạn văn cần xử lý.
3. Hoặc nói trực tiếp không cần lệnh: "Please humanize this text: [đoạn văn]".
4. Muốn giữ đúng giọng văn riêng của mày: trước khi paste đoạn cần sửa, paste thêm 2-3 đoạn văn mày từng viết để skill học nhịp câu, từ ngữ quen dùng của mày rồi áp vào bản viết lại — tránh ra văn phong "sạch nhưng vô hồn" chung chung.

## Ví dụ thực tế
Đưa vào 1 đoạn văn AI viết kiểu mở bài "Great question!", giữa bài dùng từ "testament", "landscape", liệt kê bullet bôi đậm 3 ý, kết bài "the future looks bright, let me know if...". Sau khi qua skill: đoạn văn được viết lại thành câu chuyện kể trực tiếp, không mở chào hỏi giả tạo, không liệt kê giả hình, câu ngắn dài xen nhau tự nhiên hơn, kết thúc bằng 1 nhận định cụ thể chứ không phải câu sáo rỗng kiểu cổ động.

## Lưu ý / Lỗi thường gặp
- Chỉ chạy được trong Claude Code hoặc OpenCode (dùng được trong CLI agent) — không phải tính năng có sẵn trên claude.ai web/app, vì đây là skill cài local.
- Không phải installer 1 dòng như caveman, phải tự `git clone` đúng path `~/.claude/skills/humanizer` (hoặc copy tay file SKILL.md vào).
- Tên "humanizer" trùng với rất nhiều project khác không liên quan (vd Aboudjem/humanizer-skill chỉ ~80 star, humanizerai/agent-skills là sản phẩm có credit trả phí cho phần advanced) — nhớ đúng repo `blader/humanizer` (24.7k star, MIT, free hoàn toàn) khi tìm lại.
- Không có cam kết "qua mặt 100% AI detector" — mục đích chính là đọc tự nhiên hơn, không phải né detector; vẫn nên đọc lại 1 lượt trước khi gửi đi việc quan trọng.

## Đánh giá cá nhân
- Điểm mạnh: dựa trên nguồn uy tín có nghiên cứu thật (Wikipedia AI Cleanup) chứ không tự bịa rule, danh sách pattern rõ ràng dễ hiểu kèm before/after, có tính năng học giọng văn cá nhân khá hay, 24.7k star MIT free.
- Điểm yếu: chỉ work trong CLI agent (Claude Code/OpenCode), setup hơi thủ công hơn so với skill có installer; tên dễ trùng với loạt fork/clone khác trên GitHub gây nhầm lẫn khi search lại.
- Có nên dùng không: 7.5/10 — rất hữu ích nếu công việc của mày là viết content/email/copy bằng Claude Code thường xuyên và bị feedback là "đọc biết AI viết ngay". Không cần thiết nếu chỉ dùng Claude cho code.

## Link
- Repo: https://github.com/blader/humanizer
- Docs: README ngay trong repo, nguồn gốc rule từ https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- MCP registry: không, đây là skill cài trực tiếp qua git clone

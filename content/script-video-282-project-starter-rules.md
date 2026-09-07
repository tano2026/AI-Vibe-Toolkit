# Script Video 282 — Project Starter Rules

## Thông tin
- Tool/Repo/Skill liên quan: skills/project-starter-rules/SKILL.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

## Hook (3 giây đầu)
Agent của mày vừa đốt cả trăm nghìn token vì 1 vòng lặp lỗi vô hạn — đây là cách tao chặn đứng nó trong 5 dòng rule.

## Script voiceover (ElevenLabs-ready)
Mỗi lần tao build agent mới cho VPS, tao gặp đúng ba lỗi lặp lại. Agent nuốt lỗi âm thầm rồi báo xong việc trong khi chưa làm gì cả. Agent kẹt trong vòng lặp gọi API lỗi liên tục cho tới khi hết tiền. Và agent để lộ API key thẳng ra log chat.

Nên tao đóng gói lại thành một bộ năm quy tắc, dán thẳng vào file AGENTS dot MD ở gốc mọi project mới. Quy tắc một, không được nuốt lỗi, không được trả dữ liệu giả. Quy tắc hai, giới hạn hai mươi lượt gọi mỗi yêu cầu, dùng model miễn phí làm mặc định. Quy tắc ba, lỗi ba lần thì cảnh báo, lỗi tám lần thì dừng cứng luôn. Quy tắc bốn, tự động che secret trong log. Quy tắc năm, cấm báo xong việc nếu chưa chạy test thật có bằng chứng.

Từ giờ mỗi project mới của tao, chỉ cần copy đúng một file này vào là agent tự tuân thủ trăm phần trăm, không cần nhắc lại.

## Ghi chú quay (OBS)
- Cảnh 1: quay màn hình terminal show log lỗi vòng lặp vô hạn, tốc độ token tăng nhanh
- Cảnh 2: quay file AGENTS.md với 5 mục được highlight lần lượt khi voice đọc tới
- Cảnh 3: quay thao tác copy file AGENTS.md vào folder project mới trong VS Code/terminal

## Caption/Sub note (CapCut)
Highlight các từ khóa: "nuốt lỗi", "hết tiền", "che secret", "cấm báo xong khống". Cắt cảnh đúng lúc chuyển sang quy tắc mới (5 lần cắt tương ứng 5 quy tắc).

## Thumbnail idea (Canva)
Text overlay lớn: "5 RULE CỨU AGENT KHỎI ĐỐT TIỀN". Nền tối, icon cảnh báo đỏ + icon file AGENTS.md.

## CTA cuối video
Follow Trùm Sân Bay để lấy full bộ AGENTS.md free, comment "RULE" tao gửi link kho.

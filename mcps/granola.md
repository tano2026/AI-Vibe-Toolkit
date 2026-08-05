# Granola — MCP Server

## TL;DR
MCP chính thức của Granola.ai — cho Claude đọc thẳng ghi chú cuộc họp, transcript, action item từ Granola. Hết cảnh phải tự mở Granola, tìm note, copy-paste sang Claude mỗi lần cần nhắc lại chuyện đã bàn trong cuộc họp.

## Tool này dùng để làm gì
Granola là app ghi chú cuộc họp AI-enhanced (tự nghe, tự tóm tắt). MCP này bắc cầu để Claude query trực tiếp vào kho note đó bằng ngôn ngữ tự nhiên — tìm cuộc họp theo chủ đề/ngày/người tham dự, đọc note đã AI-enhance, hoặc kéo transcript gốc có gắn tên người nói.

## Setup từng bước
1. Cách nhanh nhất (server chính thức, hosted, không cần code): trong Claude, vào Settings → Connectors → thêm "Granola" → xác thực OAuth qua trình duyệt.
2. Với Claude Code: `claude mcp add --transport http granola https://mcp.granola.ai/mcp`
3. Không cần API key thủ công — dùng session đăng nhập Granola desktop app sẵn có (nếu chọn bản local self-host thay vì hosted).
4. Có bản tự host/local (vd `Bencockin/granola-mcp` trên GitHub) nếu muốn toàn quyền kiểm soát, không qua server Granola — phù hợp hơn với nguyên tắc tự chủ hạ tầng.
5. Test: hỏi Claude "meeting tuần trước với [tên] bàn gì" — nếu trả lời đúng là kết nối thành công.

## Ví dụ thực tế
Ghi âm buổi họp bàn với đối tác B2B Travel Platform, Granola tự tóm tắt. Vài ngày sau đang soạn contract, hỏi thẳng Claude "lúc họp với bên Duffel có nói gì về commission structure không" — Claude tự query Granola MCP, kéo đúng đoạn note, không cần lục lại app riêng.

## Lưu ý / Lỗi thường gặp
- Bản hosted chính thức yêu cầu tài khoản Granola trả phí cho một số tool (list_meeting_folders, list_meetings theo folder, get_meeting_transcript chỉ có ở gói trả phí).
- Bản local/self-host cần Granola desktop app đã cài và đăng nhập sẵn trên máy — không chạy được trên VPS headless nếu không có desktop app chạy nền.
- Dữ liệu note nhạy cảm (bàn deal, giá, đối tác) — cân nhắc phạm vi cấp quyền trước khi bật cho agent tự động query không giới hạn.

## Đánh giá cá nhân
- Điểm mạnh: xoá bỏ hoàn toàn thao tác copy-paste note cuộc họp, đúng use case founder họp liên tục.
- Điểm yếu: một số tính năng khoá sau gói trả phí; bản hosted phụ thuộc server Granola.
- Có nên dùng không: 7/10 — hữu ích nếu Tano ghi âm nhiều cuộc họp đối tác/client, không cần thiết nếu ít họp hoặc đã ghi chú thủ công đủ tốt.

## Link
- Repo (bản self-host): https://github.com/Bencockin/granola-mcp
- Docs: https://docs.granola.ai/help-center/sharing/integrations/mcp
- MCP registry: https://mcp.granola.ai/mcp

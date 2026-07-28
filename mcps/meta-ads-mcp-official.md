# Meta Ads MCP (Chính thức) — MCP Server

## TL;DR
MCP server CHÍNH THỨC của Meta cho quảng cáo — ra mắt open beta 29/4/2026 tại `mcp.facebook.com/ads`. 29 tool, đọc/ghi đầy đủ (khác các MCP không chính thức chỉ đọc), OAuth qua Business Manager. Miễn phí trong giai đoạn beta.

## Dùng để làm gì
Quản lý campaign/ad set/creative/báo cáo Meta Ads (Facebook + Instagram) trực tiếp từ Claude bằng ngôn ngữ tự nhiên — không cần vào Ads Manager thủ công. Khác hẳn API thô (`meta-social-api.md` đã có trong kho, chỉ là REST API để post/lấy insight) — đây là lớp MCP có sẵn tool được định nghĩa rõ, Claude tự biết cách gọi.

## Setup từng bước
1. Vào `mcp.facebook.com/ads`, đăng nhập bằng tài khoản Meta Business Manager.
2. Copy server URL, thêm vào Claude qua Settings → Connectors → Add custom connector (cần Claude Pro trở lên).
3. Xác nhận OAuth qua Business Manager — cấp quyền cho tài khoản ads cụ thể.
4. Lưu ý: đang rollout dần, không phải tài khoản ads nào cũng có quyền truy cập ngay — kiểm tra trước khi phụ thuộc vào workflow.

## Lưu ý / Lỗi thường gặp
- **Đang rollout dần** — không phải mọi tài khoản ads đều có sẵn ngay lập tức tại thời điểm này.
- Phải tự tìm đúng server URL và tự xử lý OAuth — chưa có onboarding trong app hướng dẫn từng bước như 1 số MCP bên thứ 3 (vd Windsor.ai) đã tích hợp sẵn vào connector directory của Claude.
- Chỉ quản lý được Meta Ads — không kèm TikTok/Google Ads trong cùng 1 kết nối (khác Pipeboard/Markifact quản nhiều platform 1 chỗ).
- Giá dài hạn CHƯA công bố — miễn phí chỉ trong giai đoạn beta hiện tại.

## Đánh giá cá nhân
- Điểm mạnh: chính thức từ Meta, đọc/ghi đầy đủ, không rủi ro bị khoá tài khoản như dùng personal access token qua MCP không chính thức.
- Điểm yếu: rollout chưa đầy đủ, setup thủ công hơn 1 số MCP bên thứ 3 đã tích hợp sẵn.
- Có nên dùng không: 8/10 nếu chỉ chạy ads Meta — cân nhắc Pipeboard/Markifact nếu cần quản lý đa nền tảng (Meta+Google+TikTok) trong cùng 1 kết nối.

## Link
- Server: https://mcp.facebook.com/ads

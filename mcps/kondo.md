# Kondo — MCP Server

## TL;DR
Kondo là tool quản lý inbox LinkedIn kiểu Superhuman (split inbox, label, snooze). MCP của nó (chỉ ở gói Business trở lên) cho Claude đọc và trả lời tin nhắn LinkedIn DM trực tiếp — hợp cho ai builder/founder nhận nhiều DM LinkedIn cần triage nhanh.

## Tool này dùng để làm gì
Thay vì tự mở LinkedIn lọc từng tin nhắn, Kondo tổ chức sẵn inbox (split theo loại), và qua MCP, Claude có thể đọc, phân loại độ ưu tiên, và soạn/gửi reply ngay trong chat — không cần rời Claude.

## Setup từng bước
1. Cài Kondo browser extension (bắt buộc — MCP chỉ hoạt động khi có 1 tab Kondo đang mở trong trình duyệt).
2. Nâng cấp lên gói Business ($36/user/tháng billed annually) — MCP không có ở gói Basic.
3. Trong Claude Code: chạy `/mcp` để bắt đầu flow đăng nhập, hoặc trong Claude web: Settings → Connectors → thêm URL Kondo, hoàn tất OAuth.
4. Dữ liệu tin nhắn đi qua browser session hiện tại của Kondo — không lưu trữ ở phía Kondo relay (chỉ pass-through trong memory).

## Ví dụ thực tế
Trùm Sân Bay/Tano Agency nhận nhiều DM LinkedIn từ đối tác B2B tiềm năng cho ABTRIP — thay vì tự lọc, hỏi Claude "DM nào trong LinkedIn cần trả lời gấp hôm nay" — Kondo MCP trả về danh sách đã phân loại, Claude soạn sẵn reply nháp để duyệt.

## Lưu ý / Lỗi thường gặp
- **Bắt buộc phải có tab trình duyệt mở** — không chạy nền độc lập được như MCP server thông thường, không hợp automation 24/7 trên VPS headless.
- Chi phí không nhỏ ($36/user/tháng chỉ để có MCP) — cân nhắc kỹ nếu volume DM LinkedIn chưa đủ lớn để justify.
- Không có bản mã nguồn mở/tự host — phụ thuộc hoàn toàn dịch vụ Kondo.

## Đánh giá cá nhân
- Điểm mạnh: giải đúng nỗi đau inbox LinkedIn lộn xộn cho ai nhận DM volume cao.
- Điểm yếu: cần trình duyệt mở liên tục, không chạy headless — không hợp kiến trúc VPS/agent tự động hiện tại của Tano.
- Có nên dùng không: 5/10 cho Tano hiện tại — chưa rõ volume DM LinkedIn có đủ lớn để justify chi phí + hạn chế kỹ thuật (cần browser luôn mở); đáng cân nhắc lại nếu B2B Travel Platform bắt đầu outreach LinkedIn mạnh.

## Link
- Docs: https://docs.trykondo.com/mcp-setup
- Pricing: https://www.trykondo.com/pricing

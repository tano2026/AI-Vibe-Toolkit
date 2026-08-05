# Slack — MCP Server

## TL;DR
MCP chính thức cho Slack — Claude đọc lịch sử kênh, tìm tin nhắn, và đăng update thẳng vào Slack workspace mà không cần rời conversation.

## Tool này dùng để làm gì
Biến Claude thành người có thể "vào Slack thay mày" trong giới hạn cho phép: đọc channel history để tổng hợp, tìm lại quyết định cũ đã bàn trong 1 thread, hoặc tự đăng báo cáo/update định kỳ vào kênh team.

## Setup từng bước
1. Trong Claude web/desktop: Settings → Connectors → thêm "Slack" → đăng nhập workspace qua OAuth.
2. Chọn phạm vi kênh được phép truy cập khi cấp quyền — không nên cấp toàn bộ workspace nếu không cần thiết.
3. Với Claude Code/agent tự host: dùng Slack MCP server community (nhiều bản trên GitHub, cần Slack App token + Bot token tự tạo qua Slack API console).
4. Test bằng câu hỏi đọc (an toàn): "tóm tắt kênh #general tuần này" trước khi thử câu hành động (đăng tin nhắn).

## Ví dụ thực tế
Cuối tuần, hỏi Claude tổng hợp toàn bộ thảo luận trong kênh #trum-san-bay-content của tuần — thay vì tự cuộn lại đọc từng tin nhắn. Hoặc để agent tự đăng "Weekly Brief" mỗi thứ Hai vào kênh nội bộ Tano Agency (giống pattern `productivity:start`/`morning` đã có trong catalog skill).

## Lưu ý / Lỗi thường gặp
- **Hành động ghi (post message) là external action** — theo đúng pattern risk-tier đã research (OpenWorker), nên luôn để agent hỏi xác nhận trước khi tự đăng vào kênh thật, không auto-post không kiểm soát.
- Giới hạn quyền theo kênh cụ thể khi setup, tránh cấp full workspace access cho 1 tác vụ nhỏ.
- Token/OAuth hết hạn định kỳ — cần theo dõi nếu dùng cho automation chạy nền dài hạn (liên quan tới nguyên tắc "GITHUB_TOKEN cần set đúng trong PM2" đã ghi nhận cho Hermes/OpenClaw — Slack token cũng cần quản lý tương tự).

## Đánh giá cá nhân
- Điểm mạnh: chuẩn, ổn định, dùng được ngay không cần code nếu qua Claude web connector.
- Điểm yếu: MCP hosted chính thức phụ thuộc Claude, chưa tích hợp sẵn vào Hermes/OpenClaw (đang dùng urllib/Node.js thuần, chưa có MCP layer).
- Có nên dùng không: 7/10 — hữu ích nếu Tano Agency dùng Slack làm kênh nội bộ; nếu team chủ yếu dùng Telegram/Zalo (như hiện tại) thì độ ưu tiên thấp hơn.

## Link
- Docs: https://slack.com (Slack API / App Directory — thêm connector qua Claude Settings)
- MCP registry: có trong danh mục connector chính thức của Claude

# Notion — MCP Server

## TL;DR
MCP chính thức của Notion — Claude đọc và ghi thẳng vào database/trang Notion. Đã có sẵn dạng connector trong môi trường Claude hiện tại (`Notion:notion-*` tools), không cần setup thêm nếu dùng qua Claude trực tiếp.

## Tool này dùng để làm gì
Cho Claude query database Notion bằng SQL-like syntax (`notion-query-data-sources`), tạo/sửa trang, quản lý comment, tìm kiếm xuyên cả Notion lẫn nguồn kết nối (Slack, Google Drive) qua `notion-search`. Biến Notion từ nơi lưu trữ tĩnh thành nguồn dữ liệu Claude thao tác được trực tiếp.

## Setup từng bước
1. Trong Claude: Settings → Connectors → thêm "Notion" → OAuth đăng nhập workspace.
2. Chọn phạm vi trang/database được chia sẻ với integration khi cấp quyền lần đầu (Notion yêu cầu share thủ công từng trang/database với integration, không tự động full-access).
3. Test đọc trước: `notion-search` hoặc `notion-fetch` 1 trang biết trước để xác nhận kết nối đúng.
4. Muốn dùng ngoài Claude (Hermes/OpenClaw) — cần Notion Integration Token riêng qua notion.so/my-integrations, không dùng chung OAuth của Claude.

## Ví dụ thực tế
Dùng làm coordination layer thay thế tạm cho Airtable `company-hq` base đang lên kế hoạch — Claude đọc thẳng bảng theo dõi task từ Notion, tự cập nhật trạng thái sau khi hoàn thành 1 task trong kho AI-Vibe-Toolkit, không cần copy tay qua TRACKER.md riêng.

## Lưu ý / Lỗi thường gặp
- Notion **không tự cấp quyền toàn workspace** — mỗi database/trang phải share thủ công với integration, dễ quên và query ra rỗng dù integration đã kết nối đúng.
- `notion-update-page`/`notion-create-pages` là hành động ghi — luôn xác nhận trước khi để agent tự sửa dữ liệu Notion thật.
- Ghi vào Notion không thay được git-based tracking (SHA, lịch sử version rõ ràng) — không nên dùng Notion thay thế hoàn toàn GitHub cho kho AI-Vibe-Toolkit, chỉ hợp làm lớp điều phối/dashboard.

## Đánh giá cá nhân
- Điểm mạnh: đã sẵn có, mạnh, query kiểu SQL thật chứ không chỉ đọc text thô.
- Điểm yếu: setup quyền chia sẻ theo từng trang hơi lích kích, dễ quên khi mở rộng.
- Có nên dùng không: 8/10 — nếu Tano quyết định dùng Notion thay vì Airtable cho `company-hq`, đây là lựa chọn mạnh và đã có sẵn integration, không cần build thêm.

## Link
- Docs: https://mcp.notion.com/mcp
- MCP registry: có sẵn trong Claude Connector directory

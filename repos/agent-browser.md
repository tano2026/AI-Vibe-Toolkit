# agent-browser (Vercel Labs) — GitHub Repo

## TL;DR
CLI browser automation cho AI agent — Claude Code tự mở trình duyệt thật, click, test app vừa code, tự verify chứ không chỉ nói "xong" rồi thôi. 39.1K stars, Apache-2.0, nhẹ hơn Playwright MCP nhiều lần (tránh lỗi tốn token: có case Playwright MCP đội version bug làm 1 screenshot ngốn 15,000+ token).

## Repo này dùng để làm gì
Vòng lặp "self-verifying agent": Claude Code build xong 1 component/tính năng → tự mở browser thật qua `agent-browser` → click thử, điền form, chụp màn hình → so khớp hành vi mong đợi → nếu sai, tự sửa code rồi test lại. Không cần CEO tự mở browser kiểm tra tay.

Điểm khác biệt kỹ thuật với Playwright MCP: dùng accessibility-tree snapshot + element ref dạng `@e1, @e2` (gọn, ổn định qua thay đổi trang) thay vì dump DOM/screenshot nặng nề — đây là lý do nhẹ token hơn nhiều.

Ngoài web, còn tự động hoá được cả app Electron desktop (VS Code, Slack, Discord, Figma, Notion, Spotify), chạy được trong Vercel Sandbox microVM hoặc AWS Bedrock AgentCore cloud browser.

## Setup từng bước
1. Cài CLI:
```bash
npm install -g agent-browser
agent-browser install   # tải Chrome for Testing lần đầu
```
2. Thêm skill vào Claude Code — skill tự fetch nội dung mới nhất từ chính CLI đã cài, không bị stale:
```bash
npx skills add https://github.com/vercel-labs/agent-browser --skill agent-browser
```
3. Thêm vào file instruction dự án (CLAUDE.md) để Claude Code ưu tiên dùng agent-browser thay vì tool browser built-in khác:
```
## Browser Automation
Use `agent-browser` for web automation.
```
4. Dùng trực tiếp qua lệnh tự nhiên: "Use agent-browser to test the login flow" — Claude Code tự đọc `agent-browser --help` và skill content để biết cách dùng.

## Ví dụ thực tế
Sau khi Claude Code sửa xong luồng đặt vé Fast Track trên site ABTRIP, giao lệnh: "test luồng đặt vé từ chọn ngày tới xác nhận thanh toán bằng agent-browser". Claude Code tự mở browser thật, điền form, click qua từng bước, chụp screenshot tại mỗi điểm — phát hiện ngay nếu bước xác nhận bị lỗi thay vì đợi CEO tự test tay rồi báo lại.

## Lưu ý / Lỗi thường gặp
- Không copy `SKILL.md` từ `node_modules` ra dùng riêng — sẽ bị lỗi thời, luôn để skill fetch trực tiếp từ CLI đã cài (đảm bảo khớp đúng version).
- README khuyên: dùng `agent-browser` cho vòng lặp AI tự verify nhanh; khi cần tính năng nâng cao (network interception, PDF export, multi-tab phức tạp) hoặc đã có sẵn bộ test Playwright cũ thì chuyển qua Playwright MCP đầy đủ — không phải lúc nào cũng thay thế hoàn toàn.
- Cần Node.js 24+ nếu build từ source; bản cài qua npm/brew/cargo đơn giản hơn nhiều.

## Đánh giá cá nhân
- Điểm mạnh: giải quyết đúng vấn đề "AI nói xong nhưng chưa chắc đã đúng" — tự verify bằng browser thật; nhẹ token hơn hẳn Playwright MCP; hỗ trợ cả Electron app không chỉ web.
- Điểm yếu: chưa mạnh bằng Playwright cho test phức tạp (network mock, multi-tab); là CLI mới của Vercel, cần theo dõi độ ổn định lâu dài.
- Có nên dùng không: 9/10 — nên đưa vào **bộ skill bắt buộc cho mọi project có UI**, đặc biệt các site ABTRIP/Wonder Mart cần verify luồng thanh toán/booking thật trước khi CEO tự kiểm tra tay.

## Link
- Repo: https://github.com/vercel-labs/agent-browser
- Docs: https://agent-browser.dev/skills

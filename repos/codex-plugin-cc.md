# Codex Plugin for Claude Code (codex-plugin-cc) — GitHub Repo

## TL;DR
Plugin chính thức do OpenAI phát hành (30/3/2026) cho phép gọi Codex trực tiếp từ trong Claude Code — chưa từng có tiền lệ 1 hãng AI cung cấp plugin chính thức cho sản phẩm của đối thủ. Claude viết code, Codex review độc lập — 2 model chấm chéo nhau, bắt lỗi mà 1 model đơn lẻ có thể bỏ sót.

## Repo này dùng để làm gì
Thêm các slash command (`/codex:review`, `/codex:adversarial-review`, `/codex:rescue`) vào Claude Code, gọi thẳng Codex CLI chạy nền để review code, hoặc chuyển giao task khó cho Codex xử lý trong khi vẫn giám sát từ phiên Claude Code.

## Setup từng bước
1. Yêu cầu: Node.js 18.18+, và tài khoản ChatGPT (kể cả free tier) hoặc OpenAI API key.
2. Trong phiên Claude Code:
   ```
   /plugin marketplace add openai/codex-plugin-cc
   /plugin install codex@openai-codex
   /codex:setup
   ```
3. `/codex:setup` tự kiểm tra Codex CLI đã cài chưa, có thể tự cài qua npm nếu thiếu, và xác thực qua `codex login`.
4. Dùng `/codex:review` cho review thường ngày, `/codex:adversarial-review` cho check kỹ trước khi ship, `/codex:rescue` khi cần Codex tiếp quản 1 task đang bí.
5. Tính năng nâng cao "review gate" (`/codex:setup --enable-review-gate`) khiến Codex tự động review mọi response trước khi Claude Code hoàn tất — cảnh báo: có thể gây vòng lặp dài, tốn quota nhanh nếu không theo dõi sát.

## Ví dụ thực tế
Sau khi Claude Code viết xong 1 script Python cho Hermes (gọi GitHub API), chạy `/codex:review` để có 1 góc nhìn độc lập từ Codex trước khi push production — bắt được lỗi logic (vd thiếu xử lý rate limit 429) mà chỉ dùng 1 model có thể bỏ sót do cùng 1 "điểm mù" huấn luyện.

## Lưu ý / Lỗi thường gặp
- **"Review gate" dễ gây vòng lặp tốn quota** — tài liệu chính thức cảnh báo rõ, chỉ bật khi có thể theo dõi session liên tục, không bật mặc định cho automation chạy nền không giám sát.
- Cần 2 lớp xác thực riêng (Claude Code + Codex/ChatGPT) — thêm điểm quản lý credential, không đơn giản như dùng 1 hệ sinh thái.
- Tăng trưởng rất nhanh (hàng chục nghìn sao trong ngày đầu) — còn quá mới để đánh giá độ ổn định dài hạn trong production.

## Đánh giá cá nhân
- Điểm mạnh: ý tưởng "2 model chấm chéo nhau" là kiểm soát chất lượng tốt hơn hẳn so với chỉ dùng 1 model tự review chính mình — đặc biệt hữu ích cho code chạy production thật trên VPS (Hermes/OpenClaw).
- Điểm yếu: thêm phụ thuộc + chi phí (cần cả 2 gói dịch vụ), review gate có rủi ro vòng lặp nếu cấu hình sai.
- Có nên dùng không: 7/10 — đáng thử cho code quan trọng (script chạm vào production VPS, GitHub push tự động) nhưng nên dùng `/codex:review` thủ công, tránh bật review gate tự động cho tới khi hiểu rõ chi phí thực tế.

## Link
- Repo: https://github.com/openai/codex-plugin-cc

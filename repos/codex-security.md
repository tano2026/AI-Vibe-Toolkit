# Codex Security (OpenAI) — GitHub Repo

## TL;DR
CLI + SDK chính thức của OpenAI để tự động tìm/xác minh/vá lỗ hổng bảo mật trong code — build lại threat model riêng cho từng project trước khi quét, xác thực finding qua sandbox thay vì chỉ đoán như static analysis thường. 7.6K sao (tăng nhanh), Apache-2.0. **Đã xác minh thật 100%** qua nhiều nguồn tin độc lập (CSO Online, The Hacker News, blog chính thức OpenAI) — không phải giả mạo dù npm package tự xưng "@openai" (rủi ro supply-chain có thật, nhưng repo này đúng chuẩn chính chủ).

## Repo này dùng để làm gì
Khác static analyzer thường (chỉ match pattern), Codex Security dựng **threat model riêng cho
từng project** trước khi quét, dùng model reasoning (`gpt-5.6-terra`) để suy luận đường tấn công
khả thi, rồi **tự verify finding trong sandbox** trước khi báo — giảm hẳn false positive so với
kiểu "quét ra 1000 cảnh báo, tự lọc lấy". Có sẵn:
- Quét toàn repo, review từng thay đổi (PR), theo dõi finding qua nhiều lần chạy (deduplicate,
  đánh dấu đã fix/tái xuất hiện/không rõ)
- Đề xuất patch tối thiểu, tôn trọng code style hiện có (không refactor thừa — đúng tinh thần
  Karpathy Guidelines đã có trong kho)
- Tích hợp CI/CD làm security gate trước khi merge
- Số liệu thật đã công bố (từ bản research preview 03/2026, TRƯỚC khi mã nguồn mở hoá tháng
  07/2026): quét **1.2 triệu commit** trong 30 ngày beta, tìm ra **792 lỗ hổng critical + 10.561
  lỗi high-severity**, gán được **14 CVE thật** trên OpenSSH, GnuTLS, GOGS, Thorium, libssh, PHP,
  Chromium, GnuPG.

## Setup từng bước
```bash
npm install @openai/codex-security
npx codex-security login          # đăng nhập ChatGPT, hoặc set OPENAI_API_KEY/CODEX_API_KEY
npx codex-security scan .
```
Yêu cầu: Node.js 22.13+ (hoặc 24.x/26.x), Python 3.10+. Máy không có display (VPS headless):
```bash
npx codex-security login --device-auth
```
CI/CD: set `OPENAI_API_KEY` hoặc `CODEX_API_KEY` thay vì login tương tác.

## Ví dụ thực tế
Trước khi merge PR sửa luồng thanh toán Wonder Mart — chạy `npx codex-security scan .` như 1
bước bổ sung TRƯỚC `sanyuan-skills` (review code quality) và `kiem-tra-bao-mat-truoc-deploy.md`
(checklist deploy) đã có trong kho — 3 lớp review khác nhau, không trùng: Codex Security tìm lỗ
hổng bảo mật code-level bằng threat model AI, sanyuan-skills soi SOLID/hiệu năng, checklist
deploy soi quy trình vận hành (secret, IDOR, payment).

## Lưu ý / Lỗi thường gặp
- **Rủi ro supply-chain có thật:** vì tên "@openai/*" dễ bị giả mạo — LUÔN cài đúng từ npm
  registry chính thức, kiểm tra tên package khớp chính xác `@openai/codex-security`, không copy
  lệnh từ nguồn không tin cậy (đúng bài học chung khi cài bất kỳ tool bảo mật nào).
- Sandbox scan/workbench có thể kế thừa biến môi trường máy host — tự xoá `OPENAI_API_KEY`/
  `CODEX_API_KEY` khỏi môi trường workbench nhưng KHÔNG xoá hết mọi credential khác, cần tự dọn
  trước khi scan repo có secret khác trong env.
- Chỉ scan repo **mình sở hữu hoặc có quyền đánh giá rõ ràng** — không dùng để tự ý quét code
  người khác.
- Còn ở giai đoạn "early release" (theo chính OpenAI công bố) — vẫn còn issue mở, PR queue nhỏ.
- Số liệu "14 CVE/10.561 lỗi" là từ đợt research preview 03/2026 (khi còn là tính năng nội bộ
  ChatGPT Pro), KHÔNG phải số liệu mới phát sinh riêng từ bản mã nguồn mở hoá — 1 số nội dung
  lan truyền gộp 2 mốc thời gian này làm 1, cần hiểu đúng.

## Đánh giá cá nhân
- Điểm mạnh: chính thức từ OpenAI, đã chứng minh hiệu quả thật (14 CVE thật trên phần mềm lớn
  như Chromium/OpenSSH), miễn phí Apache-2.0, đề xuất patch tối thiểu không refactor thừa.
- Điểm yếu: cần tài khoản/API key OpenAI (không phải công cụ zero-dependency); early release
  còn issue mở; rủi ro supply-chain nếu người dùng cài nhầm package giả mạo tên tương tự.
- Có nên dùng không: 8.5/10 — đáng thêm vào quy trình review trước deploy cho project có code
  quan trọng (Wonder Mart payment, ABTRIP booking), dùng SONG SONG với sanyuan-skills và
  checklist bảo mật đã có, không thay thế.

## Link
- Repo: https://github.com/openai/codex-security
- npm: https://www.npmjs.com/package/@openai/codex-security
- Công bố chính thức (research preview, số liệu gốc): https://openai.com/index/codex-security-now-in-research-preview/

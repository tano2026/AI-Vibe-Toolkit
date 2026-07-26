# sanyuan-skills — GitHub Repo

## TL;DR
Skill code-review chuyên nghiệp — soi SOLID, bảo mật, hiệu năng, xử lý lỗi, edge case trước khi ship. 3.6K stars. Gọn, tập trung đúng 1 việc, bổ trợ trực tiếp cho `agents/KARPATHY-CODING-GUIDELINES.md` và `skills/kiem-tra-bao-mat-truoc-deploy.md` đã có trong kho.

## Repo này dùng để làm gì
Đóng vai "senior reviewer" tự động — quét code theo checklist chuẩn ngành thay vì chỉ hỏi "code có chạy không":
- **SOLID principles** — vi phạm Single Responsibility, phụ thuộc cứng không cần thiết
- **Bảo mật** — input validation, injection risk, secret lộ ra
- **Hiệu năng** — N+1 query, vòng lặp thừa, cấu trúc dữ liệu sai chỗ
- **Xử lý lỗi** — try/catch nuốt lỗi im lặng, không xử lý exception đúng chỗ
- **Edge case/boundary condition** — input rỗng, số âm, overflow, race condition

## Setup từng bước
1. Cài trực tiếp bằng npx (cách chính thức theo README):
```bash
npx skills add sanyuan0704/sanyuan-skills --path skills/code-review-expert
```
2. Trigger bằng lệnh `/code-review-expert` (tự động review git diff hiện tại) hoặc nói tự nhiên
   "review code này theo sanyuan-skills" nếu đã wire vào workflow.
3. Repo còn có 2 skill khác trong cùng bộ (không bắt buộc, cân nhắc riêng):
   `skills/sigma` (AI tutor) và `skills/skill-forge` (meta-skill tạo skill mới).

## Ví dụ thực tế
Trước khi merge PR sửa luồng thanh toán Wonder Mart — chạy qua sanyuan-skills trước `kiem-tra-bao-mat-truoc-deploy.md`: bắt được 1 chỗ try/catch nuốt lỗi im lặng khi API thanh toán timeout (không log, không báo), fix trước khi review bảo mật ở tầng cao hơn (mục #6 payment trong checklist đã có).

## Lưu ý / Lỗi thường gặp
- Đây là review CODE QUALITY (SOLID/performance/error-handling) — khác phạm vi `kiem-tra-bao-mat-truoc-deploy.md` (bảo mật hệ thống/deploy) và Karpathy Guidelines (hành vi AI khi sửa code) — cả 3 bổ trợ nhau, không trùng lặp, nên dùng đủ cả 3 cho code quan trọng.
- Chỉ review git diff hiện tại (diff-oriented), không quét toàn bộ codebase — phù hợp check
  trước khi merge, không thay được audit toàn hệ thống định kỳ.
- Cài qua `-path` flag vì đây là multi-skill repo, không phải 1 skill đơn — đừng nhầm lệnh cài
  với repo 1-skill thông thường.

## Đánh giá cá nhân
- Điểm mạnh: tập trung đúng 1 việc (code review chuẩn ngành), không ôm đồm, dễ tích hợp vào quy trình review đã có; bổ trợ tốt cho 2 tài liệu bảo mật/hành vi đã có sẵn trong kho.
- Điểm yếu: chỉ 3.6K stars, cộng đồng nhỏ hơn nhiều so với awesome-claude-skills hay agent-browser — độ tin cậy dài hạn chưa bằng.
- Có nên dùng không: 7.5/10 — đáng đưa vào **bộ skill bắt buộc**, chạy TRƯỚC bước bảo mật deploy, tạo thành pipeline review 2 tầng (code quality → security/deploy).

## Link
- Repo: https://github.com/sanyuan0704/sanyuan-skills
- Skill dùng: https://github.com/sanyuan0704/sanyuan-skills/tree/main/skills/code-review-expert

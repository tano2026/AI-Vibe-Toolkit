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
1. Cài như skill Claude Code chuẩn:
```bash
git clone https://github.com/<org>/sanyuan-skills.git
cp -r sanyuan-skills/skills/* ~/.claude/skills/
```
(Xác nhận đúng org/path thật khi cài — tên tổ chức gốc cần verify lại tại thời điểm cài vì repo có thể đã đổi tên/fork.)
2. Trigger bằng lệnh tự nhiên: "review code này theo sanyuan-skills" hoặc để agent tự áp dụng khi review PR nếu đã wire vào workflow.

## Ví dụ thực tế
Trước khi merge PR sửa luồng thanh toán Wonder Mart — chạy qua sanyuan-skills trước `kiem-tra-bao-mat-truoc-deploy.md`: bắt được 1 chỗ try/catch nuốt lỗi im lặng khi API thanh toán timeout (không log, không báo), fix trước khi review bảo mật ở tầng cao hơn (mục #6 payment trong checklist đã có).

## Lưu ý / Lỗi thường gặp
- Đây là review CODE QUALITY (SOLID/performance/error-handling) — khác phạm vi `kiem-tra-bao-mat-truoc-deploy.md` (bảo mật hệ thống/deploy) và Karpathy Guidelines (hành vi AI khi sửa code) — cả 3 bổ trợ nhau, không trùng lặp, nên dùng đủ cả 3 cho code quan trọng.
- Cần xác nhận lại tên tổ chức/path GitHub chính xác tại thời điểm cài vì thông tin có thể đã thay đổi.

## Đánh giá cá nhân
- Điểm mạnh: tập trung đúng 1 việc (code review chuẩn ngành), không ôm đồm, dễ tích hợp vào quy trình review đã có; bổ trợ tốt cho 2 tài liệu bảo mật/hành vi đã có sẵn trong kho.
- Điểm yếu: chỉ 3.6K stars, cộng đồng nhỏ hơn nhiều so với awesome-claude-skills hay agent-browser — độ tin cậy dài hạn chưa bằng.
- Có nên dùng không: 7.5/10 — đáng đưa vào **bộ skill bắt buộc**, chạy TRƯỚC bước bảo mật deploy, tạo thành pipeline review 2 tầng (code quality → security/deploy).

## Link
- Ghi chú: xác nhận lại tên tổ chức GitHub chính xác khi cài đặt thật — repo có thể đã fork/đổi tên kể từ lúc research.

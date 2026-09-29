# AGENTS.md — [Tên project]

> Điền các chỗ [ ] trước khi dùng. Agent đọc file này đầu mỗi phiên.

## Project
- Mục đích: [1 câu]
- Brand: [ABTRIP | An Bình | Tano | Wonder Mart | khác] → design system ở `DESIGN.md` (gốc project)
- Người dùng cuối: [ai dùng]

## Stack
- Ngôn ngữ / framework: [...]
- DB / dịch vụ ngoài: [...]

## Lệnh (agent PHẢI dùng đúng các lệnh này, không tự đoán)
- Cài: `[...]`
- Chạy dev: `[...]` (port: [...])
- Test: `[...]`
- Lint / build: `[...]`

## Cấu trúc thư mục
[liệt kê thư mục chính và vai trò]

## Không được đụng
- `.env*`, [thư mục production], [file cấu hình nhạy cảm]

## Định nghĩa "xong"
- Test pass, chạy được lệnh dev.
- Nếu có giao diện: đã qua `/ui-check`.
- Diff chỉ chứa thay đổi được yêu cầu.

## Luật
Xem `.agent/rules/`: kỷ luật code, bảo mật, mức quyết định L0-L3, design.

# AI Marketing Claude — Marketing Ops Toolkit (rediumvex/theromanknox) — GitHub Repo

## TL;DR
Bộ marketing ops đầy đủ nhất trong 4 repo public của tác giả — 12 skill, 5 subagent chuyên biệt, script Python, chạy qua 1 lệnh gốc `/market` với nhiều subcommand (audit, CRO, SEO, copy, email, ads, funnel, launch, proposal, report). Đây chính là repo khớp với slide "Marketing" trong bộ 42-skill đã gửi hôm qua — CÓ THẬT, không phải teaser.

## Repo này dùng để làm gì
`/market audit <url>` chạy audit đầy đủ với cả 5 subagent chuyên biệt song song (mỗi subagent chấm 1 khía cạnh, trích dẫn bằng chứng thật từ nội dung trang, không chỉ nhận định chung chung). Các subcommand khác:
- `/market landing <url>` — riêng CRO cho 1 trang
- `/market brand <url>` — phân tích giọng thương hiệu (chạy trước để các skill sau dùng chung 1 giọng)
- `/market emails <loại>` — chuỗi email welcome/nurture/launch theo đúng brand voice đã detect
- Output đổ vào file gốc project (`MARKETING-AUDIT.md`, `BRAND-VOICE.md`...), skill sau tự đọc lại làm context — không phải làm lại từ đầu mỗi lần.
- Chấm điểm A-F theo evidence thật (trích nguyên văn copy trang), ưu tiên sửa theo traffic × CR lift × ARPU — không liệt kê chung chung.

## Setup từng bước
```bash
curl -fsSL https://raw.githubusercontent.com/rediumvex/ai-marketing-claude/main/install.sh | bash
```
Copy toàn bộ skill/agent/script/template vào `~/.claude/`. Cần thêm dependency riêng nếu dùng `/market report --format pdf`.

## Ví dụ thực tế
Chạy `/market audit fasttracknoibai.com` — 5 subagent chấm điểm song song (SEO, CRO, copy, brand, technical), ra file `MARKETING-AUDIT.md` với từng finding trích nguyên văn copy trang đang có vấn đề, xếp hạng sửa theo tác động thật (traffic hiện có × mức tăng conversion kỳ vọng) — thay vì phải tự audit tay từng phần.

## Lưu ý / Lỗi thường gặp
- Đây là bộ mạnh nhất trong 4 repo nhưng cũng phức tạp nhất — nên chạy `/market brand` trước để mọi skill sau dùng chung 1 giọng thương hiệu, tránh output lệch tông giữa các lần chạy.
- Cần review kỹ trước khi hành động theo khuyến nghị — chấm điểm A-F là góc nhìn AI, không phải kiểm toán marketing chính thức.

## Đánh giá cá nhân
- Có nên dùng không: 8.5/10 — repo giá trị nhất trong 4 cái, đáng dùng thật cho audit định kỳ landing page ABTRIP/Wonder Mart thay vì tự audit tay.

## Link
- Repo: https://github.com/rediumvex/ai-marketing-claude

# Impeccable — GitHub Repo

## TL;DR
Skill phê bình + sửa thiết kế UI/frontend, xây trên nền `frontend-design` gốc của Anthropic (đã có trong `available_skills`) — thêm 23 lệnh cụ thể (bolder/quieter/distill/colorize/critique...) và hệ thống phát hiện anti-pattern thiết kế.

## Repo này dùng để làm gì
23 lệnh qua `/impeccable <command>`: `bolder` (khuếch đại thiết kế nhạt), `quieter` (giảm bớt thiết kế quá đậm), `distill` (rút gọn về cốt lõi), `colorize` (thêm màu chiến lược), `critique` (review UX), `clarify` (cải thiện copy UX không rõ), `adapt` (thích ứng đa thiết bị), `optimize` (hiệu năng). Có "design hooks" tự động chạy sau khi agent sửa file UI, so khớp với `DESIGN.md`/`PRODUCT.md` của project (context theo từng app trong monorepo).

## Điểm kết nối — bổ sung cho Designer Pro, không thay thế

Khác các skill Designer Pro đã xây (`brand-visual-template-system`, `image-prompt-formula-core` — lo ẢNH/POSTER tĩnh) — Impeccable lo **UI/frontend thật** (web/app). Hợp cho TMC Corporate Portal, Smart Booking SaaS, Zalo Mini App — đúng nhóm sản phẩm phần mềm `product-film-skill` cũng nhắm tới.

## Setup từng bước
```bash
git submodule add https://github.com/pbakaus/impeccable .impeccable
npx impeccable link --source=.impeccable --providers=claude,cursor
```
Dùng: `/impeccable critique landing` (review trang đích), `/impeccable redo this hero section`.

## Ví dụ thực tế
TMC Corporate Portal đang trong giai đoạn UI/UX spec — chạy `/impeccable critique` trên bản dựng để bắt lỗi thiết kế trước khi demo cho khách B2B/B2G, thay vì tự mắt nhìn chủ quan.

## Lưu ý / Lỗi thường gặp
- Cần GitHub Copilot/Claude Code/Cursor/Codex có hỗ trợ hook — không chạy hook tự động trên Hermes (tự ghi rõ "no hook surface")
- Đừng cài trùng 2 bản Impeccable trong cùng workspace — tự xung đột

## Đánh giá cá nhân
- Điểm mạnh: xây trên nền đã tin cậy (frontend-design của Anthropic), 23 lệnh cụ thể dễ nhớ, có design hooks tự động theo dõi khi code UI thay đổi
- Điểm yếu: tập trung UI/frontend code thật — không áp dụng cho poster/ảnh tĩnh (đã có skill riêng lo việc đó)
- Có nên dùng: 7/10 — đáng dùng khi bắt đầu code UI thật cho TMC Portal/Smart Booking, chưa cấp thiết lúc này

## Link
- Repo: https://github.com/pbakaus/impeccable
- Docs: impeccable.style

# Archify — GitHub Repo

## TL;DR
Agent skill biến mô tả kiến trúc/codebase thành diagram HTML tương tác, có kiểm chứng (không phải vẽ cho đẹp — mỗi node có bằng chứng nguồn gắn với commit Git thật). 76,2k sao, đang phát triển tích cực (tới v3.0.1).

## Repo này dùng để làm gì
5 loại diagram: Architecture (sơ đồ hệ thống), Workflow, Sequence, Data-flow, Lifecycle/state-machine. Agent (Claude Code/Cursor/Codex/OpenCode) phát JSON có kiểu dữ liệu rõ → Archify biên dịch thành HTML/SVG độc lập (không cần server), có dark/light theme, chuyển động, xuất PNG/SVG/WebM. Khác Mermaid thường — có validation xác định, "architecture-delta" so sánh 2 bản chụp kiến trúc theo thời gian.

## Điểm kết nối trực tiếp — vẽ lại chính kho này

Toàn bộ sơ đồ ASCII trong `OPERATING-MODEL.md`, `COMPANY-CHARTER.md`, `ARCHITECTURE.md` (Vessel/Talent, luồng task qua EA Gate...) đang là text thuần — Archify có thể biến thành diagram HTML tương tác thật, dễ nhìn hơn nhiều cho Trio/khách hàng xem.

## Setup từng bước
```bash
npx skills add tt-a1i/archify -g
```
Sau đó ra lệnh bằng lời: *"Use archify to map this repository's runtime architecture"* hoặc *"Use archify to draw this flow: EA Gate -> 8 Pro Agent -> Vessel"*.

Test nhanh:
```bash
cd archify
node bin/archify.mjs doctor   # verify cài đúng
node bin/archify.mjs demo /tmp/archify-demo
```

## Ví dụ thực tế
Vẽ lại sơ đồ "Luồng 1 task đi qua hệ thống" trong `OPERATING-MODEL.md` (Nobitano → EA Gate → 8 Năng lực → 5 Vessel) thành 1 file HTML tương tác — gửi cho Trio hoặc khách hàng xem trực quan hơn đọc ASCII trong markdown.

## Lưu ý / Lỗi thường gặp
- Tên user đúng là `tt-a1i` (số 1), infographic/nhiều nguồn viết nhầm thành `tt-ali` (chữ l) — dùng sai link sẽ ra 404
- Không phải công cụ vẽ tự do — là "auditable claim set", đòi hỏi JSON IR có cấu trúc, không tự do vẽ bừa như Mermaid

## Đánh giá cá nhân
- Điểm mạnh: trưởng thành thật (76k sao, release liên tục), có validation xác định (không phải AI vẽ bừa), đúng nhu cầu trực quan hoá kiến trúc đã xây
- Điểm yếu: cần agent hỗ trợ phát JSON đúng cấu trúc — không đơn giản như gõ prompt tự do
- Có nên dùng: 8/10 — đáng dùng để trực quan hoá OPERATING-MODEL.md/COMPANY-CHARTER.md cho dễ trình bày

## Link
- Repo: https://github.com/tt-a1i/archify
- Docs: tt-a1i.github.io/archify

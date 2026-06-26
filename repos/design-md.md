# DESIGN.md — GitHub Repo

## TL;DR
Google Labs ra chuẩn file `DESIGN.md` — giống như `README.md` nhưng dành riêng cho AI agent đọc design system. Mày tạo 1 file DESIGN.md → AI coding agent (Claude Code, Cursor, Copilot...) hiểu ngay brand mày: màu sắc, font, spacing, reasoning đằng sau từng quyết định design.

## Repo này dùng để làm gì
Vibe coders hay gặp 1 vấn đề: mỗi lần ra lệnh cho AI code UI, phải giải thích lại màu primary là gì, font nào đang dùng, spacing bao nhiêu. Tốn thời gian, AI hay đoán sai.

DESIGN.md giải quyết bằng cách chuẩn hóa 1 file duy nhất chứa toàn bộ design token + lý do chọn chúng. AI đọc file này 1 lần → hiểu cả design system → code UI đúng brand từ đầu đến cuối.

Format: YAML front matter (token chính xác) + Markdown prose (giải thích *tại sao*).

## Setup từng bước
1. Tạo file `DESIGN.md` ở root project
2. Thêm YAML front matter với các token:
```yaml
---
name: TenBrand
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  accent: "#B8422E"
  neutral: "#F7F5F2"
typography:
  h1:
    fontFamily: "Inter"
    fontSize: "3rem"
    fontWeight: 700
  body:
    fontFamily: "Inter"
    fontSize: "1rem"
spacing:
  base: "8px"
  scale: [4, 8, 16, 24, 32, 48, 64]
borderRadius:
  sm: "4px"
  md: "8px"
  lg: "16px"
---
```
3. Thêm prose giải thích bên dưới YAML:
```markdown
## Brand Rationale
Màu primary #1A1C1E chọn vì muốn cảm giác premium, serious — không phải pure black để tránh harsh.
Font Inter vì legibility cao trên web, hỗ trợ tiếng Việt tốt.
```
4. Trong project instruction Claude Code / Cursor, thêm: "Đọc DESIGN.md trước khi viết bất kỳ component UI nào"
5. Test: prompt `Build a hero section` → AI tự dùng màu/font từ DESIGN.md

## Ví dụ thực tế
**Không có DESIGN.md:** "Build me a button" → AI đẻ ra màu xanh mặc định, font Arial, padding tự chọn.

**Có DESIGN.md:** Cùng prompt → Button dùng đúng màu primary #1A1C1E, font Inter 14px, border-radius 8px, padding dựa trên spacing scale.

Tiết kiệm 3-5 lần sửa UI mỗi component.

## Lưu ý / Lỗi thường gặp
- Phải để file ở **root directory** — không phải trong /docs hay /assets
- YAML front matter phải valid (dùng yaml validator nếu không chắc)
- AI không tự đọc nếu không mention trong system prompt / project instruction
- Chưa có linter/validator chính thức — Google Labs vẫn đang phát triển ecosystem

## Đánh giá cá nhân
- Điểm mạnh: Giải quyết đúng pain point của vibe coder; chuẩn đơn giản, dễ adopt ngay
- Điểm yếu: Ecosystem còn non (chưa có tooling tự động sync với Figma/Tailwind config); AI model không phải lúc nào cũng follow đúng
- Có nên dùng không: **8/10** — Adopt ngay nếu mày dùng Claude Code hoặc Cursor để build UI. Mất 15 phút setup, tiết kiệm hàng giờ sửa design

## Link
- Repo: https://github.com/google-labs-code/design.md
- Docs: Xem README trong repo

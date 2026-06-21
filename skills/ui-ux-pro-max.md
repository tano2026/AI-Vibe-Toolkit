# UI/UX Pro Max Skill — Biến Claude Thành Design Director

## TL;DR
Skill 94K+ stars biến Claude thành "design director" chuyên nghiệp. Có 161 reasoning rules về design và 67 UI styles — Claude sẽ build UI đẹp thật sự thay vì boilerplate nhàm chán.

## Tool này dùng để làm gì
Thay vì Claude ra những UI generic màu xanh lam nhạt nhàm chán, UI/UX Pro Max dạy Claude cách nghĩ như designer thật: typography, spacing, motion, color theory, component hierarchy.

Bộ skill có:
- **161 reasoning rules** — quy tắc thiết kế từ cơ bản đến nâng cao
- **67 UI styles** — từ Glassmorphism, Neumorphism đến Brutalist, Minimal
- **Multi-platform** — Web, iOS, Android, Desktop
- **Python installer** — setup tự động

Kết quả: Claude không chỉ "tạo UI" mà còn biết tại sao layout này tốt hơn, font kia phù hợp hơn.

## Setup từng bước
```bash
# Clone repo
git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
cd ui-ux-pro-max-skill

# Chạy installer (Python 3.x)
python install.py

# Hoặc dùng skills.sh
# https://uupm.cc
```

Sau khi install, skill tự động available trong Claude Code session.

## Ví dụ thực tế
**Không có skill:**
> "Build me a login page" → Claude ra form trắng với button xanh cơ bản

**Có skill:**
> "Build me a login page" → Claude hỏi style (Dark SaaS? Minimal? Glassmorphism?), apply đúng typography scale, spacing system, micro-animation cho focus state, error state đẹp

**Cụ thể hơn:**
```
/design "landing page for AI startup" --style="dark-premium" --platform="web"
```

## Lưu ý / Lỗi thường gặp
- Cần Python 3.x để chạy installer
- Skill nặng — lần đầu load có thể chậm hơn bình thường
- 67 UI styles đôi khi confusing — nên specify rõ style mình muốn
- Không thay được Figma cho production design, nhưng tốt cho prototyping nhanh

## Đánh giá cá nhân
- **Điểm mạnh:** Output UI thật sự đẹp hơn rõ rệt, 161 rules giúp Claude consistent, 94K stars = community lớn
- **Điểm yếu:** Hơi over-engineered cho task đơn giản, installer Python thêm bước setup
- **Có nên dùng không:** 8.5/10 — nếu mày build frontend và chán UI nhàm, cái này đáng install ngay

## Link
- Repo: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Website: https://uupm.cc

# Anthropic Skills — Agent Skills Chính Thức

## TL;DR
Bộ kỹ năng chính thức từ Anthropic, production-tested bởi đội ngũ xây dựng Claude. Gồm các skill tạo tài liệu DOCX, PDF, PPTX, XLSX và nhiều hơn nữa — dùng được ngay không cần config phức tạp.

## Tool này dùng để làm gì
Skills là các folder chứa hướng dẫn, script và tài nguyên mà Claude tải động để làm tốt hơn các task chuyên biệt. Anthropic tự xây và test bộ này trước khi release — tức là mày đang dùng đúng cái mà team Claude dùng nội bộ.

Các skill nổi bật:
- **docx** — tạo Word document chuẩn có heading, table, TOC
- **pdf** — đọc/tạo/fill PDF form, merge, split, watermark
- **pptx** — tạo slide deck từ text hoặc data
- **xlsx** — tạo bảng tính, chart, formula
- **file-reading** — router cho mọi loại file upload
- **frontend-design** — hướng dẫn Claude design UI đẹp hơn

## Setup từng bước
```bash
# Cách 1: Install qua skills.sh (nhanh nhất)
# Vào claude.ai → Settings → Skills → Add skill
# Paste URL: https://skills.sh/anthropics/skills

# Cách 2: Clone về máy
git clone https://github.com/anthropics/skills
# Rồi dùng /mnt/skills trong Claude Code
```

Hoặc copy thẳng từng SKILL.md vào project instructions của mày.

## Ví dụ thực tế
**Task:** "Tạo báo cáo tháng ra file Word"
- Không có skill → Claude output text thô, format lung tung
- Có docx skill → Claude biết dùng python-docx, tạo được file .docx thật với heading, bảng, số trang

**Task:** "Đọc file Excel này và phân tích"
- Có file-reading skill → Claude chọn đúng tool, đọc được binary file, không bị lỗi encoding

## Lưu ý / Lỗi thường gặp
- Skills hoạt động tốt nhất với Claude Code hoặc claude.ai Pro/Team
- Mỗi skill có SKILL.md — đó là file quan trọng, đừng xóa
- Không phải skill nào cũng dùng được trong mọi context (check description trước)
- Một số skill cần thư viện Python cụ thể (đọc requirement trong SKILL.md)

## Đánh giá cá nhân
- **Điểm mạnh:** Chính thức từ Anthropic, production-tested, có 141K+ stars — đây là chuẩn mực của skill system
- **Điểm yếu:** Phần lớn tập trung document generation, chưa có nhiều skill cho marketing hay business ops
- **Có nên dùng không:** 9/10 — nếu mày dùng Claude Code thì đây là bộ skill BẮT BUỘC phải có

## Link
- Repo: https://github.com/anthropics/skills
- Docs: https://support.claude.com/en/articles/12512176-what-are-skills
- Skills registry: https://skills.sh/anthropics/skills

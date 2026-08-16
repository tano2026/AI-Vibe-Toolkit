# cc-inspect — Skill

## TL;DR
Dashboard HTML tự sinh, quét ra hết skill/plugin/MCP/command/hook đang cài trong Claude Code (cả cấp user/project/local), không cần dependency gì ngoài bash + python3. 17 sao, miễn phí.

## Skill này dùng để làm gì
Kho AI Vibe Toolkit hiện có 474 skill + 130 repo + 37 MCP — dễ cài trùng, cài thiếu, hoặc quên mất đã có gì rồi. `cc-inspect` chạy 1 lệnh `/inspect`, quét toàn bộ những gì đang thật sự active trong Claude Code (không phải trong kho GitHub — mà là những gì đã cài local), xuất ra 1 file HTML tự chứa (self-contained) mở bằng trình duyệt xem được ngay, phân biệt rõ cái nào ở scope user, project, hay local.

## Setup từng bước
1. Clone vào thư mục skill:
```bash
git clone https://github.com/howardpen9/cc-inspect ~/.claude/skills/cc-inspect
```
2. Gọi `/inspect` trong Claude Code.
3. Mở file HTML output bằng trình duyệt để xem dashboard.

## Ví dụ thực tế
Trước khi thêm skill mới vào máy dev (trước khi research rồi push lên kho GitHub), chạy `/inspect` xem local đã có bản nào tương tự chưa — bổ sung cho bước "duplicate check" hiện đang làm thủ công qua GitHub API (list folder, thử slug variant). `cc-inspect` cho góc nhìn khác: xem cái gì đang THẬT SỰ active trên máy, không chỉ nằm trong repo.

## Lưu ý / Lỗi thường gặp
- Chỉ quét local Claude Code install, không đọc được repo GitHub từ xa — không thay thế được bước duplicate-check bằng GitHub API đang dùng cho kho, chỉ bổ sung.
- Repo còn nhỏ (17 sao) — output HTML nên tự kiểm tra lại, đừng tin tuyệt đối nếu cấu trúc thư mục skill máy khác chuẩn.

## Đánh giá cá nhân
- Điểm mạnh: zero dependency, chạy nhanh, nhìn dashboard trực quan hơn đọc list text dài.
- Điểm yếu: chỉ hữu ích khi làm việc trực tiếp trên máy có cài Claude Code skill local — với quy trình hiện tại (research trên Claude web/API rồi push GitHub) giá trị sẽ giảm nếu không cài Claude Code CLI song song.
- Có nên dùng không: 6.5/10 — hữu ích nếu Nobitano có dùng Claude Code CLI trên máy Windows, không quá cần thiết nếu chỉ làm qua giao diện web/app.

## Link
- Repo: https://github.com/howardpen9/cc-inspect

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# cc-inspect xuất ra file HTML tĩnh, Hermes có thể đọc lại để parse danh sách skill đang cài
import re
def parse_inspect_html(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    # Tự viết regex/parser theo cấu trúc HTML thật của file xuất ra
    return html
```

### OpenClaw
```bash
git clone https://github.com/howardpen9/cc-inspect ~/.openclaw/tools/cc-inspect
```

### Antigravity
```bash
# Không cần deploy VPS — chạy local trên máy Windows của Nobitano là đủ
git clone https://github.com/howardpen9/cc-inspect ~/.claude/skills/cc-inspect
```
> ⚠️ Chỉ hữu ích khi Claude Code CLI đang chạy trên máy — không áp dụng được cho agent chạy thuần server-side như OpenClaw/Antigravity.

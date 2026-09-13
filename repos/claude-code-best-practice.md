---
name: claude-code-best-practice
description: >
  Stars: 31k+ Tác giả: shanraisshan Domain: Tổng hợp best practice Claude Code (agents/commands/skills/hooks/MCP)
---

# claude-code-best-practice — kho tổng hợp mọi best practice Claude Code

**GitHub:** https://github.com/shanraisshan/claude-code-best-practice
**Stars:** 31,235⭐ | 2,777 fork | #1 GitHub Trending Repository Of The Day

---

## TL;DR

Repo tham khảo tổng hợp gần như mọi tính năng Claude Code hiện có — subagent, command, skill, hook, MCP, plugin, settings, status line, memory — mỗi mục đều dẫn nguồn thật, không chỉ liệt kê suông.

## Tool này dùng để làm gì

Không phải 1 tool để cài, mà là 1 "cheat sheet sống" — bảng tra cứu mọi concept Claude Code, mỗi dòng có link tới ví dụ triển khai thật trong chính repo (`.claude/agents/`, `.claude/commands/`, `.claude/skills/`...). Khi cần biết "làm hook đúng chuẩn thế nào" hay "cấu trúc MCP server ra sao", vào đây tra thay vì tự mò docs.

Repo còn có phần "Hot" theo dõi tính năng beta mới ra (Ultrareview, Ultraplan, Auto Mode, Channels...) — cập nhật theo version Claude Code mới nhất.

## Setup từng bước

1. Clone về để tham khảo cấu trúc, không cần "cài" gì:
```bash
git clone https://github.com/shanraisshan/claude-code-best-practice.git
```
2. Copy trực tiếp file mẫu trong `.claude/agents/`, `.claude/commands/`, `.claude/skills/` vào project của mình nếu khớp nhu cầu
3. Đọc phần "How to Use" trong README trước để biết cách tận dụng đúng, không chỉ đọc bảng suông

## Ví dụ thực tế

Cần viết 1 hook chặn commit khi test fail — thay vì tự mò cú pháp, vào mục "Hooks" trong bảng, bấm link tới file `.claude/hooks/` mẫu trong chính repo, copy cấu trúc rồi chỉnh theo project của mình.

## Lưu ý / Lỗi thường gặp

- Repo cập nhật rất nhanh theo version Claude Code — copy code mẫu về nên kiểm tra lại còn tương thích version Claude Code hiện tại không
- Vì là "tổng hợp mọi thứ" nên khá dài, dễ ngợp — nên tra theo mục cụ thể cần chứ đừng đọc từ đầu tới cuối
- Một số phần "beta" (Ultrareview, Ultraplan) có thể đổi cú pháp giữa các bản Claude Code

## Đánh giá cá nhân

- **Điểm mạnh:** độ phủ cực rộng, mọi thứ đều có ví dụ thật trong repo chứ không nói suông; cập nhật sát version mới nhất nên không bị lạc hậu
- **Điểm yếu:** không phải hướng dẫn từng bước cho người mới — hợp để tra cứu hơn là học tuần tự (muốn học bài bản nên dùng claude-howto thay vì repo này)
- **Có nên dùng không:** 8.5/10 — nên có sẵn để tra cứu bất cứ lúc nào làm việc với Claude Code, đặc biệt hợp cho Antigravity khi cần setup hook/MCP cho VPS

## Link
- Repo: https://github.com/shanraisshan/claude-code-best-practice

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Đây là repo tài liệu/tham khảo, không có API — Hermes có thể fetch README để tra cứu nhanh
import urllib.request

def fetch_best_practice_section(section_path):
    url = f"https://raw.githubusercontent.com/shanraisshan/claude-code-best-practice/main/{section_path}"
    req = urllib.request.Request(url, headers={"User-Agent": "hermes"})
    return urllib.request.urlopen(req).read().decode()
```

### OpenClaw
```bash
git clone https://github.com/shanraisshan/claude-code-best-practice.git ~/reference/claude-code-best-practice
# copy mẫu cần dùng, vd:
cp -r ~/reference/claude-code-best-practice/.claude/hooks ./  .claude/hooks
```

### Antigravity
```bash
# Không cần deploy — chỉ dùng làm tài liệu tham khảo khi cấu hình VPS agent
# Nên clone 1 bản local trên VPS để tra offline khi cần
git clone https://github.com/shanraisshan/claude-code-best-practice.git /opt/reference/ccbp
```
> ⚠️ Repo đổi nhanh — trước khi copy mẫu nào về dùng thật, kiểm tra ngày cập nhật gần nhất khớp version Claude Code đang chạy.

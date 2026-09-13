---
name: claude-howto
description: >
  Stars: 39k+ Tác giả: luongnv89 Domain: Lộ trình học Claude Code từ A-Z, có bản Tiếng Việt
---

# claude-howto — học Claude Code trong 1 cuối tuần, có bản Tiếng Việt

**GitHub:** https://github.com/luongnv89/claude-howto
**Stars:** 39,350⭐ | 4,100+ fork | MIT License | Ngôn ngữ: English, Tiếng Việt, 中文, Українська, 日本語

---

## TL;DR

Hướng dẫn học Claude Code có hệ thống — 10 module theo lộ trình từ slash command tới plugin, có bài tự đánh giá trình độ, template copy-paste được ngay, và **có sẵn bản dịch Tiếng Việt** — hiếm thấy ở repo Claude Code khác.

## Tool này dùng để làm gì

Khác `claude-code-best-practice` (tra cứu ngẫu nhiên theo nhu cầu), `claude-howto` là lộ trình học TUẦN TỰ có thứ tự rõ ràng:

| Thứ tự | Module | Trình độ | Thời gian |
|---|---|---|---|
| 1 | Slash Commands | Beginner | 30 phút |
| 2 | Memory | Beginner+ | 45 phút |
| 3 | Checkpoints | Intermediate | 45 phút |
| 4 | CLI Basics | Beginner+ | 30 phút |
| 5 | Skills | Intermediate | 1 giờ |
| 6 | Hooks | Intermediate | 1 giờ |
| 7 | MCP | Intermediate+ | 1 giờ |
| 8 | Subagents | Intermediate+ | 1.5 giờ |
| 9 | Advanced Features | Advanced | 2-3 giờ |
| 10 | Plugins | Advanced | 2 giờ |

Có `/self-assessment` để biết đang ở trình độ nào, và `/lesson-quiz [topic]` sau mỗi module để tự kiểm tra hiểu bài.

## Setup từng bước

1. Clone hoặc đọc thẳng trên GitHub (README dẫn hết nội dung, không cần cài gì):
```bash
git clone https://github.com/luongnv89/claude-howto.git
```
2. Đổi ngôn ngữ đọc: bấm link "Tiếng Việt" ở đầu README
3. Chạy `/self-assessment` trong Claude Code để biết bắt đầu từ module nào
4. Đi theo lộ trình 10 module, copy template trực tiếp vào project khi học tới đâu

## Ví dụ thực tế

Mới dùng Claude Code, chưa biết Skills là gì → theo lộ trình tới module 5 (Skills, ~1 giờ), đọc xong tự tay tạo được 1 skill riêng cho project của mình, không phải đoán mò cấu trúc SKILL.md.

## Lưu ý / Lỗi thường gặp

- Nội dung khá dài (10 module, tổng ~12 tiếng nếu học hết) — nên chọn đúng trình độ bắt đầu qua self-assessment, đừng học lại từ đầu nếu đã biết cơ bản
- Đồng bộ theo version Claude Code mới nhất (tính tới thời điểm research: v2.1.206) — bản dịch Tiếng Việt có thể chậm cập nhật hơn bản gốc English vài ngày/tuần

## Đánh giá cá nhân

- **Điểm mạnh:** có bản Tiếng Việt sẵn — hiếm và tiện; cấu trúc học tuần tự rõ ràng hơn hẳn kiểu "đọc README dài" thông thường; có cơ chế tự kiểm tra (quiz) chứ không chỉ đọc suông
- **Điểm yếu:** vì là lộ trình học nên chậm hơn nếu chỉ cần tra 1 thứ cụ thể — lúc đó nên dùng `claude-code-best-practice` thay vì lục lại module nào chứa nó
- **Có nên dùng không:** 8/10 — hợp giới thiệu cho ai mới bắt đầu Claude Code, đặc biệt vì có Tiếng Việt

## Link
- Repo: https://github.com/luongnv89/claude-howto

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Repo tài liệu học, không có API — Hermes có thể fetch nội dung module cụ thể khi cần tra cứu nhanh
import urllib.request

def fetch_module(module_folder):
    # vd module_folder = "05-skills"
    url = f"https://raw.githubusercontent.com/luongnv89/claude-howto/main/{module_folder}/README.md"
    req = urllib.request.Request(url, headers={"User-Agent": "hermes"})
    return urllib.request.urlopen(req).read().decode()
```

### OpenClaw
```bash
git clone https://github.com/luongnv89/claude-howto.git ~/reference/claude-howto
```

### Antigravity
```bash
# Không cần deploy — clone về VPS làm tài liệu training cho ai mới join team dùng Claude Code
git clone https://github.com/luongnv89/claude-howto.git /opt/reference/claude-howto
```
> ⚠️ Không có gì để "chạy" — đây là tài liệu học, giá trị nằm ở việc đọc và làm theo, không phải cài đặt.

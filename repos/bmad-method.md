# BMAD-METHOD — GitHub Repo

## TL;DR
Framework biến "vibe coding" (prompt tùy hứng, code chắp vá) thành quy trình agile có bài bản — 1 đội AI agent chuyên trách (PM, Architect, Dev, QA, UX...) đi qua đủ vòng đời từ brainstorm đến deploy, có tài liệu (PRD, Architecture) làm cầu nối giữa các agent chứ không phải context rời rạc trong 1 chat. 51.1k sao, MIT license, miễn phí hoàn toàn.

## Repo này dùng để làm gì
Vấn đề BMAD giải quyết: khi vibe coding 1 dự án lớn, agent hay bị mất context giữa các phiên, mỗi agent "nghĩ" khác nhau vì không có tài liệu chung để tham chiếu. BMAD-METHOD gán vai trò cụ thể cho từng agent (Analyst → PM → Architect → Dev → QA) và bắt chúng để lại "story file" — tài liệu ghi lại quyết định, để agent sau đọc và tiếp tục đúng mạch, không phải đoán lại từ đầu. Có "Party Mode" — gộp nhiều persona agent vào 1 phiên để tranh luận trước khi quyết định, giống họp nhóm thật.

## Setup từng bước
1. Yêu cầu: Node.js ≥ 20.12, Python ≥ 3.10, `uv`.
2. Cài vào project (chạy trong thư mục project, không phải global):
```bash
npx bmad-method install
```
3. Làm theo installer hỏi (chọn module, chọn IDE — hỗ trợ Claude Code, Cursor...), rồi mở IDE đó trong đúng thư mục project.
4. Không biết bắt đầu từ đâu — hỏi thẳng agent điều phối:
```
bmad-help
bmad-help tôi vừa xong phần architecture, giờ làm gì tiếp?
```
5. Cài không tương tác (cho CI/CD hoặc muốn set sẵn cấu hình):
```bash
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes \
  --set bmm.project_knowledge=research --set bmm.user_skill_level=expert
```
6. Muốn làm phần brainstorm/PRD trên web (Gemini/ChatGPT) trước, đỡ tốn token IDE — dùng Web Bundles tại bmadcode.com/web-bundles, tải ZIP cài như 1 Gem/Custom GPT, xong rồi đem tài liệu qua IDE code tiếp.

## Ví dụ thực tế
Áp thẳng vào 2 việc đang làm dở của Nobitano: (1) **ABTRIP B2B Travel Platform** — đang ở Phase 0 prep (chọn aggregator, hợp đồng consolidator...), đúng giai đoạn cần PM+Architect agent làm PRD/Architecture bài bản trước khi code, tránh vừa code vừa đổi hướng; (2) **OpenClaw rebuild từ đầu** — đây là lúc tốt nhất để dùng BMAD thay vì vibe coding thẳng, vì rebuild từ 0 cần đúng thứ BMAD làm tốt nhất: PRD rõ ràng cho kiến trúc mới (Hermes=CEO, OpenClaw=execution-only) trước khi Dev agent viết code, tránh lặp lại tình trạng OpenClaw cũ bị lẫn independent decision-making.

## Lưu ý / Lỗi thường gặp
- Đây là **quy trình đầy đủ**, không phải tool chạy nền — cần dừng lại làm đúng từng bước (brainstorm → PRD → Architecture → code), không hợp cho task nhỏ/sửa nhanh 1 bug (dùng "Quick Flow" cho việc nhỏ, đừng áp full quy trình).
- Cài vào project cụ thể (`npx bmad-method install` chạy trong thư mục project), không phải cài global 1 lần dùng mọi nơi — mỗi project cần cài riêng.
- V6 (bản hiện tại) đổi khá nhiều so với V4/V5 — nếu thấy hướng dẫn cũ trên mạng nói khác, ưu tiên theo docs chính thức tại docs.bmad-method.org, không theo bài viết cũ.
- "BMad" và "BMAD-METHOD" là **trademark**, có file TRADEMARK.md riêng — nếu định fork/rebrand để dùng nội bộ (như các bản `bmad-elixir`, `BMAD-AT-CLAUDE` đã thấy trên GitHub) cần đọc kỹ điều khoản trước.

## Đánh giá cá nhân
- Điểm mạnh: 51k sao, cộng đồng lớn (Discord, YouTube riêng), miễn phí hoàn toàn không gated, module hóa tốt (BMM core + BMB builder + TEA test + game dev + creative), giải đúng vấn đề context-loss của vibe coding.
- Điểm yếu: quy trình khá nặng cho task nhỏ, cần thời gian học cách phối hợp nhiều agent thay vì chỉ gõ prompt 1 lần, V6 đổi nhiều so với bản cũ nên tài liệu/video hướng dẫn trên mạng dễ lạc hậu.
- Có nên dùng: 8/10 — rất đáng dùng cho 2 dự án lớn đang làm dở (ABTRIP, OpenClaw rebuild), không cần dùng cho việc sửa nhanh 1 file hay task 1 lần.

## Link
- Repo: https://github.com/bmad-code-org/BMAD-METHOD
- Docs: https://docs.bmad-method.org
- Web Bundles: https://bmadcode.com/web-bundles/
- Discord: https://discord.gg/gk8jAdXWmj

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# BMAD chạy trong IDE (Claude Code/Cursor), không phải service gọi qua API —
# Hermes không "gọi" BMAD trực tiếp, nhưng có thể đọc lại story file/PRD BMAD sinh ra
# để nắm context khi cần tiếp tục 1 task đã được BMAD lên kế hoạch.
import json
from pathlib import Path

def read_bmad_story(project_dir, story_id):
    story_path = Path(project_dir) / "docs" / "stories" / f"{story_id}.md"
    return story_path.read_text(encoding="utf-8") if story_path.exists() else None
```

### OpenClaw
```bash
# Cài BMAD ngay trong thư mục OpenClaw đang rebuild, dùng làm khung PRD/Architecture
# trước khi Dev agent (Claude Code) viết code kiến trúc mới
cd /path/to/openclaw-rebuild
npx bmad-method install --modules bmm --tools claude-code --yes
```

### Antigravity
```bash
# Không cần deploy service riêng — BMAD chạy trong IDE lúc dev, không phải process
# chạy 24/7 trên VPS. Antigravity chỉ cần đảm bảo Node.js 20.12+ và Python 3.10+
# có sẵn trên máy dev nếu Nobitano dùng BMAD ngay trên VPS qua SSH + Claude Code CLI.
```
> ⚠️ Đây là công cụ dùng lúc PLANNING/DEV, không phải agent chạy nền — không nhầm với các agent 24/7 khác trong kho (Hermes/OpenClaw/Antigravity).

# Claude Code Bridge — Kết nối Kho AI-Vibe-Toolkit với Claude Code

> File này là playbook cho **Claude Code** (khác Hermes/OpenClaw/Antigravity).
> Claude Code chạy trên VPS + máy Windows local của Nobitano — cả hai đều cần
> đọc được kho này để không tự nghĩ lại cái đã có sẵn.

---

## Vì sao cần bridge riêng

Kho dùng template Skill riêng (`TL;DR / Setup / Ví dụ / Đánh giá`) — **không có YAML
frontmatter** (`name:` + `description:`) như skill thật của Claude Code. Nên Claude Code
sẽ **không tự trigger** 469 file trong `/skills/` như skill native. Claude Code chỉ đọc
được kho khi được trỏ đường dẫn cụ thể (qua CLAUDE.md import hoặc `--add-dir`), dùng như
**tài liệu tra cứu**, không phải skill auto-invoke.

Muốn 1 skill cụ thể trigger tự động thật sự trong Claude Code → phải thêm frontmatter
riêng cho skill đó và đặt vào `~/.claude/skills/<name>/SKILL.md` (mirror riêng, không
sửa file gốc trong kho để không phá pipeline viết content/script video).

---

## Setup 1 lần — clone kho về máy chạy Claude Code

### VPS (Linux, Tencent Cloud — cùng chỗ Hermes)
```bash
cd /opt   # hoặc thư mục mày quen dùng cho project
git clone https://github.com/tano2026/AI-Vibe-Toolkit.git
# Repo private → cần auth 1 trong 2 cách:
# Cách A (nhanh, tạm): git clone https://<GITHUB_TOKEN>@github.com/tano2026/AI-Vibe-Toolkit.git
# Cách B (an toàn hơn, khuyên dùng): git config --global credential.helper store
#          rồi clone bình thường, nhập token 1 lần khi được hỏi password
```

### Windows local
```powershell
cd C:\Users\<ten-may>\Projects   # hoặc thư mục quen dùng
git clone https://github.com/tano2026/AI-Vibe-Toolkit.git
# Auth tương tự VPS — dùng Git Credential Manager (đã có sẵn nếu cài Git for Windows)
```

**Lưu ý bảo mật:** nhúng token thẳng vào URL clone sẽ lưu vào `.git/config` dạng plaintext,
`git remote -v` sẽ show ra token. Nên dùng credential helper (Cách B) thay vì nhúng token
vào URL nếu máy có người khác dùng chung.

---

## Setup 2 — trỏ Claude Code tới kho (user-level, áp dụng MỌI project)

Thêm vào `~/.claude/CLAUDE.md` (Linux VPS) hoặc `%USERPROFILE%\.claude\CLAUDE.md` (Windows):

```markdown
## Kho AI-Vibe-Toolkit
Kho kiến thức chính của Tano Agency — ~470 skill, ~150 repo, ~44 MCP, stack, và
playbook Hermes/OpenClaw/Antigravity. Trước khi tự viết tool/pattern mới từ đầu,
LUÔN grep/đọc kho trước — khả năng cao đã có sẵn entry liên quan.

Vị trí local (VPS): /opt/AI-Vibe-Toolkit
Vị trí local (Windows): C:\Users\<ten-may>\Projects\AI-Vibe-Toolkit

@/opt/AI-Vibe-Toolkit/KHO-INDEX.md
```

> Điều chỉnh path đúng theo từng máy. Trên Windows dùng `@C:\Users\<ten-may>\Projects\AI-Vibe-Toolkit\KHO-INDEX.md`.
> Import `@` load thẳng nội dung KHO-INDEX.md vào context mỗi session — Claude Code biết
> kho tồn tại và cấu trúc folder ngay từ đầu, không cần nhắc lại.

Nếu chỉ muốn bật cho 1 project cụ thể (không phải global) → dùng `--add-dir /opt/AI-Vibe-Toolkit`
khi chạy `claude`, hoặc thêm dòng `@` tương tự vào `CLAUDE.md` ở root project đó.

---

## Setup 3 — auto-sync để kho local luôn mới

Claude (trên claude.ai project) là người DUY NHẤT ghi lên kho GitHub. VPS + Windows chỉ
đọc bản local đã clone → cần pull định kỳ để không bị lệch.

### VPS — cron (Antigravity quản lý)
```bash
crontab -e
# thêm dòng:
*/30 * * * * cd /opt/AI-Vibe-Toolkit && git pull --quiet
```

### Windows — Task Scheduler
```powershell
# Tạo file pull-kho.ps1:
# cd C:\Users\<ten-may>\Projects\AI-Vibe-Toolkit; git pull --quiet

schtasks /create /tn "SyncKho" /tr "powershell.exe -File C:\Users\<ten-may>\Projects\pull-kho.ps1" /sc minute /mo 30
```

---

## (Optional) Phase 2 — biến 1 skill cụ thể thành skill thật của Claude Code

Chỉ làm cho skill nào thật sự cần auto-trigger (không convert cả 469 file — phí công,
và phá format dùng cho content factory). Quy trình:

1. Chọn skill trong kho, vd `skills/project-starter-rules/SKILL.md`
2. Copy nội dung phần "Nội dung skill / prompt" sang file mới tại
   `~/.claude/skills/project-starter-rules/SKILL.md`
3. Thêm frontmatter ở đầu file:
```yaml
---
name: project-starter-rules
description: Áp dụng 5 trụ cột quy tắc chuẩn (code quality, token control, loop guardrail, security, verification) khi khởi tạo project mới cho Tano Agency.
---
```
4. Claude Code giờ tự nhận diện và trigger đúng lúc, không cần gõ `/skill-name` thủ công
   (dù vẫn gọi thủ công được nếu muốn).

---

## Tóm tắt luồng dữ liệu

```
Nobitano quẳng task cho Claude (claude.ai project)
        ↓
Claude research + viết .md + push kho GitHub (tano2026/AI-Vibe-Toolkit)
        ↓
cron/Task Scheduler pull kho về VPS + Windows mỗi 30 phút
        ↓
Claude Code (VPS hoặc Windows) đọc kho qua CLAUDE.md import
        ↓
Claude Code dùng thông tin kho khi code/build task thực tế
```

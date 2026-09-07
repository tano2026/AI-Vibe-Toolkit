# Claude Code Bridge — Kết nối Kho AI-Vibe-Toolkit với Claude Code

> File này là playbook cho **Claude Code** (khác Hermes/OpenClaw/Antigravity/Team Thục Hán).
> Claude Code ở đây = Claude Code Desktop (tab "Code" trong Claude Desktop app), chạy
> **local trên máy Windows**, KHÔNG phải trên VPS. Team Thục Hán (Hermes/OpenClaw/DSH)
> là hệ agent khác, giao tiếp qua file `tasks/*.md`, không chung runtime với Claude Code —
> bridge này không đụng gì tới Team Thục Hán.

---

## Môi trường xác nhận (ghi lại để không đoán lại lần sau)

- **Máy:** Windows 11 Pro (build 10.0.26200), local
- **Working dir mẫu:** `D:\tano-tuvi-platform` (repo Tử Vi, branch `master`) — nhưng Claude
  Code có thể được trỏ vào bất kỳ project nào khác trên máy, không cố định vào Tử Vi
- **Shell:** PowerShell chính, Git Bash song song
- **Browser pane riêng:** `Claude_Browser`, tách biệt Chrome thật — dùng để test render HTML
- **Memory bundle:** `D:\Claude_vm_bundles\.claude\projects\...\memory\` — **KHÔNG theo
  path mặc định `%USERPROFILE%\.claude`**. Đây là bundle custom, nên trước khi sửa bất
  kỳ CLAUDE.md nào, PHẢI xác nhận lại path thật bằng lệnh `/memory` trong Claude Code
  session (lệnh này liệt kê đúng những file CLAUDE.md/rules đang được load, không đoán mò).

---

## Vì sao cần bridge riêng

Kho dùng template Skill riêng (`TL;DR / Setup / Ví dụ / Đánh giá`) — **không có YAML
frontmatter** (`name:` + `description:`) như skill thật của Claude Code. Claude Code sẽ
**không tự trigger** 469 file trong `/skills/` như skill native. Chỉ đọc được kho khi
được trỏ đường dẫn cụ thể (qua CLAUDE.md import hoặc `--add-dir`) — dùng như tài liệu
tra cứu thụ động, không phải skill auto-invoke.

---

## Setup 1 lần — clone kho về máy Windows

```powershell
# Clone RA NGOÀI thư mục D:\tano-tuvi-platform — kho là repo riêng, không nest vào
# git repo Tử Vi để tránh xung đột submodule
cd D:\
git clone https://github.com/tano2026/AI-Vibe-Toolkit.git
```
Repo private → clone lần đầu sẽ hỏi credential. Dùng Git Credential Manager (có sẵn nếu
cài Git for Windows) thay vì nhúng token thẳng vào URL clone — nhúng token vào URL sẽ lưu
plaintext trong `.git/config`, `git remote -v` sẽ show ra.

Kết quả: `D:\AI-Vibe-Toolkit\`

---

## Setup 2 — xác nhận path CLAUDE.md thật, rồi trỏ vào kho

**Bước A — xác nhận path thật (bắt buộc, đừng đoán):**
Trong 1 phiên Claude Code, gõ:
```
/memory
```
Lệnh này show chính xác những file CLAUDE.md/rules nào đang load và path của chúng —
vì bundle custom `D:\Claude_vm_bundles\...` có thể không giống mặc định.

**Bước B — thêm import vào file user-level CLAUDE.md mà `/memory` vừa chỉ ra:**
```markdown
## Kho AI-Vibe-Toolkit
Kho kiến thức chính của Tano Agency — ~470 skill, ~150 repo, ~44 MCP, stack, và
playbook Hermes/OpenClaw/Antigravity. Trước khi tự viết tool/pattern mới từ đầu,
LUÔN grep/đọc kho trước — khả năng cao đã có sẵn entry liên quan.

Vị trí local: D:\AI-Vibe-Toolkit

@D:\AI-Vibe-Toolkit\KHO-INDEX.md
```

User-level = áp dụng cho MỌI project Claude Code mở trên máy này, không riêng Tử Vi.
Nếu chỉ muốn bật cho riêng project Tử Vi → thêm dòng `@` tương tự vào
`D:\tano-tuvi-platform\CLAUDE.md` (project-level) thay vì user-level.

Không chắc `/memory` trỏ tới đâu, hoặc bundle custom không cho sửa trực tiếp → cách chắc
ăn nhất: thêm vào `D:\tano-tuvi-platform\CLAUDE.md` (project-level, chắc chắn load khi
làm việc trong repo này), chấp nhận đánh đổi là chỉ áp dụng cho project Tử Vi thôi.

---

## Setup 3 — giữ kho local luôn mới

Máy local, không có cron kiểu Linux mặc định → 2 lựa chọn:

**A. Task Scheduler (tự động, khuyên dùng nếu làm việc thường xuyên)**
```powershell
# Tạo D:\AI-Vibe-Toolkit\pull-kho.ps1 với nội dung:
#   cd D:\AI-Vibe-Toolkit; git pull --quiet

schtasks /create /tn "SyncKho" /tr "powershell.exe -File D:\AI-Vibe-Toolkit\pull-kho.ps1" /sc minute /mo 30
```

**B. Pull tay (đơn giản, đủ dùng nếu không phải làm việc 24/7)**
```powershell
cd D:\AI-Vibe-Toolkit; git pull
```
Chạy lệnh này đầu mỗi phiên làm việc trước khi bắt Claude Code tra kho.

---

## (Optional) Phase 2 — biến 1 skill cụ thể thành skill thật của Claude Code

Chỉ làm cho skill nào thật sự cần auto-trigger (không convert cả 469 file — phí công,
phá format dùng cho content factory). Quy trình:

1. Chọn skill trong kho, vd `skills/project-starter-rules/SKILL.md`
2. Copy nội dung phần "Nội dung skill / prompt" sang file mới. Path thật xác nhận qua
   `/memory` — thường dạng `<claude-home>\skills\<ten-skill>\SKILL.md`
3. Thêm frontmatter ở đầu file:
```yaml
---
name: project-starter-rules
description: Áp dụng 5 trụ cột quy tắc chuẩn (code quality, token control, loop guardrail, security, verification) khi khởi tạo project mới cho Tano Agency.
---
```
4. Claude Code giờ tự nhận diện và trigger đúng lúc.

---

## Tóm tắt luồng dữ liệu

```
Nobitano quẳng task cho Claude (claude.ai project — kho)
        ↓
Claude research + viết .md + push kho GitHub (tano2026/AI-Vibe-Toolkit)
        ↓
Claude Code (Windows local, D:\AI-Vibe-Toolkit) pull kho — tay hoặc Task Scheduler
        ↓
Claude Code đọc kho qua CLAUDE.md import (path xác nhận bằng /memory)
        ↓
Claude Code dùng thông tin kho khi code task thực tế (vd tano-tuvi-platform)
```

Nếu sau này Claude Code cũng chạy thêm trên VPS (song song Hermes/OpenClaw) → lặp lại
đúng quy trình Setup 1–3, chỉ đổi path Windows → path Linux và Task Scheduler → cron.

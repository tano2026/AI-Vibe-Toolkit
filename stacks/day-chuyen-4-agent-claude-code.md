# Dây chuyền 4 agent Claude Code — Combo Tools theo Use Case

## TL;DR
Thay vì để một con Claude Code vừa lên kế hoạch, vừa code, vừa test, vừa tự chấm điểm mình, tách ra 4 subagent chuyên trách (Planner → Coder → Tester → Reviewer) bàn giao nhau qua file, gọi hết bằng 1 lệnh `/ship`. Mày duyệt đúng 1 lần ở khâu cuối, có thể để nó chạy qua đêm.

## Các tool trong stack
1. **Claude Code (CLI)** → nền tảng chạy toàn bộ dây chuyền, không phải bản web
2. **Subagent Planner** (`.claude/agents/planner.md`, model Opus 5) → đọc codebase, ra bản kế hoạch chi tiết (file cần sửa, chữ ký hàm, edge case), không đụng code
3. **Subagent Coder** (`.claude/agents/coder.md`, model Sonnet 4.6) → cầm kế hoạch, code thật, ghi tóm tắt đã sửa gì
4. **Subagent Tester** (`.claude/agents/tester.md`, model Sonnet 4.6) → viết + chạy test dựa trên tóm tắt của Coder, rớt là dừng, không tự vá
5. **Subagent Reviewer** (`.claude/agents/reviewer.md`, model Opus 5) → chỉ đọc + `git diff`, phán CHỐT/CẦN SỬA/CHẶN, không có quyền sửa
6. **Slash command `/ship`** (`.claude/commands/ship.md`) → nhạc trưởng, gọi lần lượt cả 4 con, dừng ngay khi có câu hỏi bỏ ngỏ hoặc test rớt
7. **Sổ bàn giao `.bangiao/`** → 4 file trung gian (`ke-hoach.md`, `thay-doi.md`, `ket-qua-test.md`, `danh-gia.md`) — cơ chế duy nhất để 4 agent "nói chuyện" với nhau, agent sau chỉ đọc file agent trước để lại

## Workflow ghép nối
```
Yêu cầu của mày (gõ /ship <mô tả tính năng>)
      ↓
Planner (Opus 5)   → .bangiao/ke-hoach.md
      ↓ (có câu hỏi bỏ ngỏ thì dừng, hỏi mày)
Coder (Sonnet 4.6) → sửa code thật + .bangiao/thay-doi.md
      ↓
Tester (Sonnet 4.6) → file test + .bangiao/ket-qua-test.md
      ↓ (rớt test thì dừng luôn, không tự sửa)
Reviewer (Opus 5)  → .bangiao/danh-gia.md (CHỐT / CẦN SỬA / CHẶN)
      ↓
Mày đọc git diff, tự merge nhánh — dây chuyền KHÔNG BAO GIỜ tự gộp nhánh
```

Cốt lõi: 4 agent không nói chuyện trực tiếp, chỉ đọc/ghi file trong `.bangiao/`. Mỗi con có bộ `tools:` bị siết đúng vai — Planner không có Edit/Bash nên không lỡ tay sửa code; Reviewer không có Write/Edit nên không thể "vá cho êm rồi ghi ổn".

## Ví dụ thực tế
Áp cho **ABTRIP CRM** (kho đang track ở `/areas/abtrip-crm.md`): gõ trong Claude Code, đứng ở nhánh git riêng:

```
/ship thêm giới hạn tần suất cho endpoint đăng nhập của CRM, tối đa 5 lần thử/phút mỗi IP, quá thì trả 429
```

- Planner đọc code CRM hiện có, ra kế hoạch: sửa file middleware nào, hàm nào, case biên (IP bị block rồi request lại thì sao).
- Coder viết middleware theo đúng kế hoạch, không đụng file khác.
- Tester viết test: login đúng 5 lần thì qua, lần 6 phải trả 429, và test edge case timeout reset bộ đếm.
- Reviewer chạy `git diff`, đối chiếu 3 file trên, phán CHỐT nếu ổn.

Kết quả: sáng ra chỉ cần đọc `.bangiao/danh-gia.md`, không phải ngồi trace lại từng bước đêm qua.

## Lưu ý / Lỗi thường gặp
- YAML frontmatter (giữa 2 dòng `---` đầu mỗi file agent) rất khó tính: gõ `tools: read` thay vì `Read` là agent mất quyền mà **không báo lỗi gì**, chỉ thấy nó làm việc dở đi — phải viết hoa đúng chữ cái đầu (Read, Write, Edit, Grep, Glob, Bash).
- Tester **vẫn có quyền Write/Edit** thật (để tạo file test), nên "không đụng code sản phẩm" chỉ là ràng buộc bằng lời dặn trong prompt, không phải bằng quyền — phải tự liếc `git diff` mỗi sáng để chắc nó không mò ra ngoài thư mục test.
- Chạy qua đêm hay dính 2 bẫy: máy tự ngủ (Mac cần bật `caffeinate -i`, không được gập nắp) và Claude Code hỏi xin quyền giữa đêm không ai bấm — phải set trước `.claude/settings.local.json` với danh sách `allow`/`deny`, nhớ **chặn luôn thắng cho phép**.
- Chạy song song nhiều tính năng phải dùng `git worktree` riêng cho mỗi tính năng, không thì 2 dây chuyền đè code lên nhau.
- Reviewer chạy Opus 5 chỉ 1 lượt cuối nên chi phí không đội nhiều — phần tốn token nhất (Coder + Tester) đã nằm ở Sonnet 4.6 (rẻ hơn).

## Đánh giá cá nhân
- **Điểm mạnh:** Tách vai rõ ràng giải quyết đúng cái bẫy "người viết code cũng là người tự chấm code" — sổ bàn giao `.bangiao/` giúp audit lại từng bước dễ, không phải đoán AI đã nghĩ gì. Chia model theo vai (Opus cho Planner/Reviewer cần suy luận, Sonnet cho Coder/Tester cần code nhanh) tiết kiệm chi phí đáng kể so với chạy Opus toàn bộ.
- **Điểm yếu:** Setup phức tạp hơn dùng 1 agent thường (5 file, cấu hình permissions, dễ sai frontmatter mà không báo lỗi). Quyền của Tester là lỗ hổng thật — ràng buộc chỉ nằm ở prompt, ai không cẩn thận review `git diff` mỗi sáng là mất kiểm soát. Tốn token hơn hẳn 1 agent ôm hết, không hợp cho task nhỏ/nhanh.
- **Có nên dùng không:** 8/10 — rất đáng cho dự án code đang chạy dở, task đủ lớn để cần tách vai (feature mới, module có logic phức tạp). Task nhỏ 5-10 phút thì dùng 1 agent bình thường vẫn nhanh hơn, không cần dây chuyền này.

## Link
- Nguồn: https://cuongmeai.com/tai-lieu/day-chuyen-4-agent-claude-code
- Tài liệu chính thức Claude Code — Subagents: https://code.claude.com/docs/en/sub-agents
- Tài liệu chính thức Claude Code — Skills/Slash commands: https://code.claude.com/docs/en/skills
- Anthropic Engineering — multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system

---

## 🤖 Agent Integration

### Hermes (Python)
Không có REST API để gọi — đây là workflow chạy nội bộ trong Claude Code CLI (không phải MCP, không phải endpoint). Hermes không trigger được trực tiếp; nếu cần, chỉ có thể shell ra lệnh Claude Code CLI trên máy có cài sẵn, không có pattern `urllib.request` chuẩn như các tool khác trong kho.

### OpenClaw
```bash
# OpenClaw có thể subprocess gọi Claude Code CLI để tự trigger dây chuyền
# trên 1 project cụ thể (vd tự động vá bug nhỏ cho ABTRIP CRM khi có ticket mới)
cd /path/to/project
git checkout -b auto-fix-$(date +%s)
claude "/ship <mô tả lấy từ ticket>"
```
> ⚠️ Cần cài Claude Code + đã cấu hình `.claude/agents/` sẵn trong project đó, và set trước `.claude/settings.local.json` (allow/deny) để không bị treo giữa chừng chờ xin quyền.

### Antigravity
```bash
# Lệnh deploy: rải bộ 5 file agent vào project cần dùng dây chuyền này trên VPS
PROJECT_DIR="/path/to/project"
mkdir -p "$PROJECT_DIR/.claude/agents" "$PROJECT_DIR/.claude/commands"
# copy 5 file: planner.md, coder.md, tester.md, reviewer.md → .claude/agents/
#              ship.md → .claude/commands/
```
> ⚠️ Nhớ set `.claude/settings.local.json` với deny `git push`, `git checkout`, `rm`, `Read(./.env)` trước khi để chạy qua đêm không giám sát trên VPS.

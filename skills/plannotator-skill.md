# plannotator — Review Plan AI Trên Browser Trước Khi Approve (~6k⭐)

**Repo:** github.com/backnotprop/plannotator | MIT
**Website:** plannotator.ai
**Dùng với:** Claude Code, Codex, OpenCode, Gemini CLI, Cursor, Amp

---

## Vấn Đề Nó Giải Quyết

AI agent lên plan trong terminal — mày approve mù quáng vì:
- Plan dài, khó đọc trong terminal
- Không thấy toàn bộ scope
- Không annotate được chỗ muốn thay đổi

Plannotator: **hiển thị plan trên browser** → mày highlight, comment, approve từng section.

## Cài Nhanh (Local Plugin)

```bash
git clone https://github.com/backnotprop/plannotator
cd plannotator
npm install && npm run build

# Trong Claude Code
/plugin install ./plannotator
```

## Workflow

```bash
# 1. Mày giao task cho Claude Code
"Build user authentication system với JWT"

# 2. Claude tạo plan → Plannotator intercept
# 3. Browser mở tự động: localhost:3847
# 4. Mày thấy plan dạng visual:
#    - Step 1: Create /auth/login endpoint
#    - Step 2: Setup JWT middleware  
#    - Step 3: Add refresh token logic
#    ...
# 5. Mày annotate: "Step 2 - dùng express-jwt thay vì viết tay"
# 6. Approve → Claude thực thi với annotations của mày
```

## Keyboard Shortcuts Trong Browser

```
A          → Approve toàn bộ plan
R          → Reject, yêu cầu replan
H          → Highlight section đang chọn
C          → Comment vào section
Ctrl+Enter → Submit annotations → Claude tiếp tục
```

## Kết Hợp Với superpowers + agent-skills

```bash
# Triple combo:
/spec "requirements"        # agent-skills: viết spec
/plan                       # superpowers: lên plan
# → Plannotator intercept   # Review plan trên browser
# → Approve với annotations
/build                      # Execute với context đầy đủ
```

## Khi Nào Cần Plannotator

✅ Task > 1 giờ implementation
✅ Nhiều files sẽ bị modified
✅ Team cần review trước khi execute
✅ Mày không chắc AI hiểu đúng requirements

❌ Quick fixes < 10 phút
❌ Single-file changes rõ ràng

---
*skills/plannotator-skill.md | AI Vibe Toolkit | tháng 6/2026*

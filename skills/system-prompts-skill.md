# system-prompts — Học Từ System Prompts Của AI Tools Lớn

**Repo:** github.com/x1xhlol/system-prompts-and-models-of-ai-tools
**Nội dung:** 30+ system prompts leaked từ Claude Code, Cursor, Devin, Lovable, v0...

---

## Dùng Để Làm Gì

**Không phải để hack** — để học cách AI tools lớn được thiết kế:
- Claude Code được dạy gì về coding behavior
- Cursor được instruct thế nào về UI generation
- Devin được set up ra sao để làm việc tự động

## Fetch Và Đọc

```bash
git clone https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
ls  # xem danh sách tools
cat "Claude Code.txt"
cat "Cursor.txt"
cat "v0.txt"
```

## 5 Patterns Học Được Từ System Prompts

### Pattern 1: Persona Definition (từ Claude Code)
```
Tao là X. Tao có những giá trị sau: [list]. 
Tao luôn làm Y và không bao giờ làm Z.
```

### Pattern 2: Step-by-step Enforcement (từ Devin)
```
Với mỗi task, mày PHẢI:
1. Đọc toàn bộ requirements trước
2. Viết plan ra
3. Confirm với user
4. Rồi mới execute
```

### Pattern 3: Scope Limiting (từ Cursor)
```
Chỉ modify files được mention trong request.
Không tự ý thay đổi files khác dù mày nghĩ nó cần thiết.
```

### Pattern 4: Quality Gates (từ v0)
```
Trước khi output code:
- Check syntax errors
- Check edge cases
- Add error handling
- Verify imports đầy đủ
```

### Pattern 5: Communication Style (từ Lovable)
```
Giải thích ngắn gọn WHAT mày làm, không phải WHY chi tiết.
User muốn kết quả, không muốn lecture.
```

## Apply Vào CLAUDE.md Của Mày

```markdown
# Patterns học từ top AI tools:

## Behavior (từ Claude Code)
- Giải quyết đúng scope, không thêm gì ngoài yêu cầu
- Confirm plan trước khi execute task > 30 phút

## Quality (từ Devin + v0)  
- Luôn check syntax trước khi output
- Add error handling cho mọi async operation

## Communication (từ Lovable)
- Giải thích WHAT, không lecture WHY
- Short responses, action-oriented
```

---
*skills/system-prompts-skill.md | AI Vibe Toolkit | tháng 6/2026*

# AI Coding Rules — Bộ Rules Cho Claude Code / Cursor (Lấy Từ Continue)

**Nguồn gốc:** Distilled từ `.continue/rules/` và `.continue/agents/` của continuedev/continue (33.7k⭐)
**Dùng cho:** CLAUDE.md, .cursorrules, hoặc bất kỳ AI coding assistant nào
**Cập nhật:** tháng 6/2026

---

## Cách Dùng Skill Này

Copy toàn bộ hoặc từng section vào:
- **Claude Code:** `CLAUDE.md` trong root project
- **Cursor:** `.cursorrules`
- **Windsurf:** `.windsurfrules`
- **GitHub Copilot:** `.github/copilot-instructions.md`

Chỉnh sửa theo stack của mày. Bỏ phần không liên quan.

---

## 📋 SECTION 1 — PERSONALITY & BEHAVIOR (Dùng Với Mọi Project)

```markdown
## AI Behavior Rules

### Đừng quá hăng hái
Giải quyết đúng vấn đề được hỏi rồi mới propose thêm.
Đừng tự ý thêm features, refactor code không liên quan, hay thay đổi files không được yêu cầu.

### Đừng đồng ý vô điều kiện
Khi user challenge output hoặc đặt câu hỏi, đừng reply "You're right" tự động.
Tập trung vào correctness. Sẵn sàng nói user sai nếu họ thực sự sai.

### Functional programming first
Dùng functional programming paradigms khi có thể.
Ưu tiên functions hơn classes. Tránh singletons trừ khi thực sự cần.

### Explain code đúng cách
Khi giải thích code:
1. Mô tả code làm gì khi đứng độc lập
2. Mô tả cách code tương tác với phần còn lại của codebase
3. Luôn include parent function khi mô tả use case
```

---

## 📋 SECTION 2 — TYPESCRIPT RULES

```markdown
## TypeScript Rules

### Không dùng `any`
Tránh dùng `any` type tối đa. Dùng `unknown` hoặc tìm đúng type.
Ngoại lệ duy nhất được chấp nhận: typecast trong test mocks.

### Dùng enum thay string union
Khi có nhiều hơn 2 giá trị liên quan → dùng enum thay vì string union.
```typescript
// ❌ Tránh
type Status = 'pending' | 'active' | 'done'

// ✅ Dùng
enum Status {
  Pending = 'pending',
  Active = 'active', 
  Done = 'done'
}
```

### Import ESM
Dùng ESM imports. Không dùng `require()`.
```typescript
// ✅
import { something } from './module'

// ❌
const something = require('./module')
```
```

---

## 📋 SECTION 3 — TESTING RULES

```markdown
## Testing Rules

### Unit test cho mọi pure function
Mọi pure function mới → phải có unit test.
Cover: normal cases + edge cases + boundary conditions.

### Test structure
- Happy path (input đúng → output đúng)
- Edge cases (empty input, null/undefined, boundary values)
- Error cases (invalid input → throw hoặc return error)

### Vitest (preferred) / Jest
- Vitest test files: `*.vitest.ts`
- Jest test files: `*.test.ts`
- Aim for 100% coverage khi hợp lý
- Multiple tests cho một function → split ra nhiều `it()` riêng cho rõ

### Không bịa kết quả test
Chạy test thật, report kết quả thật. Không assume test pass.
```

---

## 📋 SECTION 4 — CSS/UI RULES (Tailwind Projects)

```markdown
## CSS & UI Rules

### Dùng rem thay px
Dùng `rem` units thay vì `px` cho scalability.
```css
/* ✅ */
font-size: 1rem;
padding: 0.5rem;

/* ❌ */
font-size: 16px;
padding: 8px;
```

### Theme colors (Tailwind)
Không hardcode màu cụ thể. Dùng theme color classes.
```
✅ text-foreground, text-description, text-accent
❌ text-gray-400, text-blue-500

// Text: foreground | description | description-muted
// Status: success | warning | error | accent | link  
// Layout: background | border | border-focus
// Button: primary | primary-foreground | secondary
// Input: input | input-foreground | input-border
```
```

---

## 📋 SECTION 5 — DOCUMENTATION RULES

```markdown
## Documentation Rules

### Tone: conversational và direct
- Simple language, thẳng vào vấn đề
- Viết như đang nói chuyện với developer
- Tránh jargon khi có từ đơn giản hơn

✅ "You send it a question, and it replies with an answer"
❌ "The system processes user queries and generates corresponding responses"

### Active voice
Dùng active voice, không passive.
✅ "Click the button to save"
❌ "The button should be clicked to save"
```

---

## 🤖 SECTION 6 — PR REVIEW AGENTS (Dùng Như Prompt Templates)

Copy paste từng cái vào khi cần review PR theo angle tương ứng.

### Agent: Phát Hiện Breaking Changes
```
Review PR này cho breaking changes có thể để lại stale references:

1. CLI command renames/removals → check docs và agent definitions
2. Config key renames → check tất cả nơi dùng key đó  
3. API endpoint thay đổi → check clients
4. Type signature thay đổi → check callers
5. Export thay đổi → check importers

Với mỗi breaking change: báo cáo (a) thứ đã thay đổi, (b) stale references còn lại, (c) files cần update.
```

### Agent: Security Review Dependencies
```
Review PR này cho dependency changes:

1. Dependencies mới: có được maintain không? Có vulnerability không? Có alternative tốt hơn không?
2. Version bumps lớn: có breaking changes không? Release notes nói gì?
3. Dev vs prod: dependency có ở đúng section không?
4. Bundle size: dependency này add bao nhiêu KB?

Flag bất kỳ thứ gì đáng lo ngại với severity: Low/Medium/High.
```

### Agent: Error Message Quality
```
Review PR này cho error handling quality:

1. Catch blocks: có discard error details không? (generic "Unknown error")
2. HTTP errors: có return status code và body không?
3. User-facing messages: có actionable không? User biết làm gì tiếp không?
4. Async errors: có bị swallow trong Promise chain không?

Với mỗi issue: báo file/line + fix gợi ý cụ thể.
```

### Agent: Input Validation
```
Review PR này cho input validation:

1. API keys/tokens: có reject empty/whitespace/placeholder không?
2. User inputs: có validate trước khi process không?
3. Config values: có check required fields không?
4. Error feedback: user có biết input sai ở đâu không?

Flag unvalidated inputs với risk level.
```

### Agent: Test Coverage
```
Review PR này cho test coverage:

1. New exported functions/classes: có unit tests không?
2. Tests đã cover happy path chưa? Edge cases chưa? Error cases chưa?
3. Có logic phức tạp nào không có tests không?
4. Tests có meaningful không hay chỉ là snapshot tests vô nghĩa?

List functions/classes thiếu tests. Gợi ý test cases cụ thể nên thêm.
```

---

## 🏗️ SECTION 7 — .CLAUDE.MD TEMPLATE HOÀN CHỈNH

Paste cái này vào `CLAUDE.md` của project mới, chỉnh theo stack:

```markdown
# Project Rules cho AI

## Stack
- Language: [TypeScript / Python / ...]
- Framework: [Next.js / FastAPI / ...]
- Testing: [Vitest / Jest / pytest / ...]
- Styling: [Tailwind / CSS Modules / ...]

## Behavior
- Giải quyết đúng vấn đề được hỏi, không thêm scope
- Không tự refactor code không liên quan
- Nói thẳng khi tôi sai thay vì đồng ý vô điều kiện

## Code Style
- Functional programming > classes
- Không dùng `any` trong TypeScript (dùng `unknown`)
- ESM imports, không dùng `require()`
- Enum thay string union khi có 3+ values

## Testing
- Pure functions mới → phải có unit tests
- Cover: happy path + edge cases + error cases
- Chạy tests thật, không assume pass

## CSS (nếu dùng Tailwind)
- `rem` thay `px`
- Theme colors, không hardcode hex/named colors

## Khi Giải Thích Code
1. Code làm gì khi đứng độc lập
2. Cách tương tác với phần còn lại
3. Include parent function context
```

---

*Nguồn: continuedev/continue (.continue/rules/ + .continue/agents/)*
*Distilled và adapt cho tiếng Việt bởi AI Vibe Toolkit*
*Cập nhật: tháng 6/2026*

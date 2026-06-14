# mattpocock/skills — Giảm 75% Token, Claude Code Kỷ Luật Hơn (109k⭐)

**Repo:** github.com/mattpocock/skills | MIT
**Tác giả:** Matt Pocock — Total TypeScript creator
**Stars:** 109k | Trending #1 GitHub 6 ngày liên tiếp

---

## Cài 1 Lệnh

```bash
/plugin marketplace add mattpocock/skills
/plugin install skills@mattpocock-skills
```

## Skills Chính

```bash
# TypeScript strict mode enforcement
/ts-strict "file.ts"

# No any types
/no-any "component.tsx"

# Type inference optimization  
/infer-types "code block"

# Zod schema generation
/gen-schema "interface definition"

# Error handling patterns
/error-handling "async function"
```

## Tại Sao Giảm 75% Token?

Matt Pocock thiết kế skills để:
1. **Pre-filter** context không cần thiết
2. **Compress** type information
3. **Cache** common TypeScript patterns
4. **Skip** redundant type checking

```
Trước: Claude đọc toàn bộ file 500 dòng → 15k tokens
Sau: mattpocock/skills → extract only relevant → 3.7k tokens
```

## Patterns Học Được Từ Skills Này

### Pattern 1: Type-first Development
```typescript
// Define types TRƯỚC khi viết function
type UserAction = 
  | { type: 'login'; userId: string }
  | { type: 'logout' }
  | { type: 'update'; data: Partial<User> }

// Sau đó implement
function handleAction(action: UserAction) { ... }
```

### Pattern 2: Zod Cho Runtime Validation
```typescript
import { z } from 'zod'

const UserSchema = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
  name: z.string().min(1),
})

type User = z.infer<typeof UserSchema>  // type từ schema
```

### Pattern 3: Error Handling Rõ Ràng
```typescript
// Thay vì throw
type Result<T> = 
  | { ok: true; data: T }
  | { ok: false; error: string }

async function fetchUser(id: string): Promise<Result<User>> {
  try {
    const user = await db.users.findById(id)
    return { ok: true, data: user }
  } catch (e) {
    return { ok: false, error: String(e) }
  }
}
```

## Apply Vào CLAUDE.md

```markdown
## TypeScript Rules (từ mattpocock/skills)
- Type-first: define types trước khi implement
- Zod cho mọi API input validation
- Result type thay vì throw
- Không dùng `any` — dùng `unknown`
- Infer types từ Zod schemas
```

---
*skills/mattpocock-skills-skill.md | AI Vibe Toolkit | tháng 6/2026*

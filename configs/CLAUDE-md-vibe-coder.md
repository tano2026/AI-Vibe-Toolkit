# CLAUDE.md — Template Cho Vibe Coding Projects

**Copy vào root của mỗi project mới**
**Chỉnh:** Stack + Project name

---

```markdown
# Project: [TÊN PROJECT]

## Stack
- Language: [TypeScript / Python / ...]
- Framework: [Next.js / FastAPI / ...]
- Styling: [Tailwind CSS]
- Deploy: [Vercel / Railway]
- DB: [Supabase / SQLite / ...]

## Behavior Rules

### Không thêm scope tự ý
Làm đúng việc được hỏi. Không refactor code ngoài scope, không thêm features không được yêu cầu.

### Không đồng ý vô điều kiện
Nếu tôi sai thì nói thẳng. Tập trung vào correctness.

### Giải thích code ngắn gọn
- Code làm gì
- Tương tác với phần nào khác
- Không lecture lý thuyết

## Code Style

### TypeScript
- Không dùng `any` — dùng `unknown` hoặc type đúng
- Enum thay string union khi 3+ values
- ESM imports only

### Testing
- Pure functions mới → phải có unit test
- Cover: happy path + edge cases + error cases

### CSS (Tailwind)
- `rem` thay `px`
- Theme colors, không hardcode hex

## Anti-Slop UI Rules (từ taste-skill)

### Fonts KHÔNG dùng:
Inter, Roboto, Arial, Open Sans

### Fonts NÊN dùng:
Geist, Satoshi, Cabinet Grotesk, Clash Display

### KHÔNG dùng:
- shadow-md / shadow-lg generic
- rounded-full + blue button
- Lucide thick-stroke icons
- Gradient hero sections

### NÊN dùng:
- Phosphor Light icons
- Diffuse shadows (opacity < 0.05)
- Spring animations
- GSAP ScrollTrigger

## MCP Tools Available

- Context7: docs up-to-date, không bịa API
- Brave Search: search web real-time
- Firecrawl: đọc website từ link
- GitHub MCP: commit, PR, đọc repo
- Sequential Thinking: suy nghĩ trước khi làm

## Workflow

1. `/spec` — viết spec trước khi code
2. `/plan` — breakdown tasks
3. `/build` — implement từng slice
4. `/review` — self-review trước khi done
5. `/ship` — pre-deploy checklist
```

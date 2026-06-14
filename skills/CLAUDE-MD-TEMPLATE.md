# AI Vibe Toolkit — CLAUDE.md Template

> Copy file này vào root của project → Claude sẽ hiểu context và hành xử đúng.
> Chỉnh sửa phần [TRONG NGOẶC] theo project của mày.

---

## Project Context

- **Project:** [Tên project]
- **Stack:** [TypeScript/Python/React/Next.js/...]
- **Mục tiêu:** [Mô tả ngắn project làm gì]

---

## Behavior Rules (Từ AI Vibe Toolkit)

### Đừng quá hăng hái
Giải quyết đúng vấn đề được hỏi. Không tự ý thêm features, refactor code không liên quan, hay thay đổi files ngoài scope.

### Đừng đồng ý vô điều kiện
Tập trung vào correctness. Nếu tôi sai thì nói thẳng — đừng reply "You're right" tự động.

### Giải thích code đúng cách
Khi được hỏi về code:
1. Mô tả code làm gì khi đứng độc lập
2. Mô tả tương tác với phần còn lại của codebase
3. Include parent function context

---

## Code Rules

### TypeScript (nếu dùng)
- Không dùng `any` — dùng `unknown` hoặc type đúng
- Dùng enum thay string union khi có 3+ values
- ESM imports, không dùng `require()`

### Testing
- Pure functions mới → phải có unit tests
- Cover: happy path + edge cases + error cases
- Chạy tests thật, không assume pass

### CSS / Tailwind (nếu dùng)
- `rem` thay `px`
- Theme colors, không hardcode hex
- Không dùng: Inter, shadow-md mặc định, rounded-full + blue button generic

---

## Frontend AI Rules (nếu làm UI)

### Anti-patterns bị cấm:
- Font: Inter, Roboto, Arial, Open Sans
- Shadow: shadow-md / shadow-lg mặc định
- Button: rounded-full + blue primary generic
- Icons: Lucide thick-stroke standard

### Dùng thay thế:
- Font: Geist, Satoshi, Cabinet Grotesk, Clash Display
- Shadow: diffuse, opacity < 0.05
- Motion: GSAP hoặc spring physics
- Icons: Phosphor Light, Remix Line

---

## PR Review Checklist

Khi review code/PR, check:
1. Breaking changes? (renamed commands, APIs, config keys)
2. New dependencies? (maintained? vulnerabilities?)
3. Error messages actionable không? (không generic "Unknown error")
4. Input validation đủ chưa? (empty, whitespace, invalid format)
5. New functions có tests không?

---

## MCP Tools Available

[Uncomment những cái đã cài]
- Context7: docs up-to-date
- Brave Search: search web real-time  
- Firecrawl: đọc website từ link
- Filesystem: đọc files local
- GitHub MCP: commit, PR, đọc repo
- Playwright: test web tự động
- Sequential Thinking: suy nghĩ step-by-step trước

---

## Notes

[Thêm notes project-specific ở đây]

---
*Template từ AI Vibe Toolkit — github.com/tano2026/AI-Vibe-Toolkit*

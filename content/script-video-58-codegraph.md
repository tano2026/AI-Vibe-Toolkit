# Script Video #58 — CodeGraph: Đồ Thị Code Cho AI Agent Đọc Đúng File

**Repo:** github.com/colbymchenry/codegraph | 43k⭐
**Hook:** "Agent đọc cả codebase chỉ để sửa 5 dòng — fix bằng 1 lệnh"

## SCRIPT

[HOOK 0:00-0:08]
Claude Code mở codebase VS Code.
Để trả lời 1 câu hỏi kiến trúc.
Nó đọc 9 file, grep 11 lần.
1.79 triệu token chỉ để hiểu code.

[WHAT 0:08-0:30]
colbymchenry/codegraph. 43 nghìn stars.

Parse trước toàn bộ code bằng tree-sitter.
Lưu vào SQLite local — symbol, call graph, file structure.
Expose qua MCP server cho Claude Code, Cursor, Codex, Gemini CLI...

Cài 1 lệnh:
npx @colbymchenry/codegraph

[SIGNIFICANCE 0:30-0:50]
Kết quả benchmark thật trên VS Code repo:
21 tool call → còn 4.
1.79 triệu token → còn 640 nghìn.
Rẻ hơn 18%, nhanh hơn 11%.

100% local. Không API key. Không leak code ra ngoài.

[CTA 0:50-1:00]
MIT license. Free. Link bio.

*Script #58 | AI Vibe Toolkit*

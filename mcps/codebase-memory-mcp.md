# codebase-memory-mcp — MCP Server

## TL;DR
MCP server 11.5k sao giúp AI nhớ toàn bộ cấu trúc codebase của mày — index code thành knowledge graph, AI hỏi đâu biết đó, dùng ít token hơn 10 lần.

## Tool này dùng để làm gì
Khi làm việc với project lớn (hàng nghìn file), AI như Claude Code hay Cursor thường "quên" — không biết function kia ở đâu, class này quan hệ với cái gì, import path đúng không.

codebase-memory-mcp giải quyết bằng cách index toàn bộ code vào một knowledge graph (dùng SQLite + tree-sitter). Mỗi lần AI cần tìm gì, nó query graph này thay vì đọc lại toàn bộ file — nhanh hơn, chính xác hơn, tốn ít token hơn.

Hỗ trợ 158 ngôn ngữ lập trình, average repo được index trong vài millisecond.

Use case chính:
- Claude Code / Cursor làm việc với monorepo lớn
- AI assistant luôn biết đúng function name, import path
- Không cần paste lại context mỗi lần hỏi

## Setup từng bước
1. Cài qua npm:
```bash
npm install -g codebase-memory-mcp
```
2. Thêm vào Claude Code config (`~/.claude/claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "codebase-memory": {
      "command": "codebase-memory-mcp",
      "args": ["--workspace", "/path/to/your/project"]
    }
  }
}
```
3. Restart Claude Desktop / Claude Code
4. Lần đầu mở project → MCP tự index toàn bộ codebase (vài giây với repo thường)
5. Hỏi Claude về code bình thường — nó sẽ query graph trước khi trả lời

## Ví dụ thực tế
Project: Next.js app 500 files

Trước khi dùng:
→ Hỏi Claude "function handleAuth ở đâu?" → Claude đọc lại 20 file, tốn 8000 token, đôi khi vẫn sai

Sau khi dùng codebase-memory-mcp:
→ Cùng câu hỏi → Query graph → Trả lời ngay "src/lib/auth/handler.ts line 47", tốn 200 token

## Lưu ý / Lỗi thường gặp
- Node.js 18+ required
- Repo quá lớn (+100k files): index lần đầu có thể mất 1-2 phút
- `.gitignore` được tôn trọng — node_modules không bị index
- Lỗi "MCP server not found" → kiểm tra path trong config, thử `which codebase-memory-mcp`
- Cần restart Claude sau khi thêm MCP vào config

## Đánh giá cá nhân
- Điểm mạnh: Giảm token usage cực mạnh khi làm việc với large codebase. 158 ngôn ngữ — dùng được cho hầu hết stack. Tích hợp được với Claude Code, Cursor, Aider, Gemini CLI.
- Điểm yếu: Cần setup thủ công cho mỗi project. Knowledge graph cần được sync khi code thay đổi nhiều (thêm --watch để auto-update)
- Có nên dùng không: 9/10 — Bắt buộc phải có nếu mày đang vibe code với project lớn hơn 50 files. Tiết kiệm token = tiết kiệm tiền API thật sự.

## Link
- Repo: https://github.com/DeusData/codebase-memory-mcp
- Docs: xem README trong repo
- MCP registry: https://mcp.so/server/codebase-memory-mcp

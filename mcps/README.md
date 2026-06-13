# 🔌 MCP Servers

> MCP (Model Context Protocol) = cách để Claude và AI agents kết nối với tools bên ngoài.

Nôm na: **MCP giống như plugin cho Claude** — cài vào là Claude làm được thêm nhiều thứ.

---

## Danh sách MCP trong kho

| Tên | Dùng để làm gì | Độ khó | Status |
|-----|---------------|--------|--------|
| *(đang cập nhật)* | | | |

---

## Cài MCP vào đâu?

MCP dùng được với:
- **Claude Desktop** (app máy tính)
- **Claude Code** (terminal)
- Một số AI tools khác hỗ trợ MCP protocol

---

## Cách cài MCP cơ bản (Claude Desktop)

1. Mở file config của Claude Desktop:
   - Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. Thêm MCP server vào:
```json
{
  "mcpServers": {
    "tên-mcp": {
      "command": "npx",
      "args": ["-y", "@tên/package"]
    }
  }
}
```

3. Restart Claude Desktop → Done

---

*Xem template để hiểu format của mỗi entry: [_template.md](./_template.md)*

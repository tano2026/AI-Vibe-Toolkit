# notebooklm-mcp-server — Auto-Update, VS Code Native, Zero Maintenance

**GitHub:** https://github.com/moodRobotics/notebooklm-mcp-server
**License:** MIT | **Language:** TypeScript
**Install:** `npx notebooklm-mcp-server start`
**Dùng với:** VS Code, Claude Desktop, Cursor

---

## Killer Feature: Auto-Update

Server tự check version mới khi khởi động, tự install nếu có update.

Khi Google thay UI và MCP gãy — server tự update, không cần mày làm gì. Đây là vấn đề thực tế: tháng 4/2026 NotebookLM refresh UI, tất cả MCP servers gãy trong 24-72h. Auto-update giảm downtime xuống gần 0.

---

## VS Code Native

```json
// settings.json
{
  "mcp.servers": {
    "notebooklm": {
      "command": "npx",
      "args": ["-y", "notebooklm-mcp-server", "start"]
    }
  }
}
```

Có trong VS Code Marketplace — install từ Extensions panel.

---

## Cài Và Dùng

```bash
npx notebooklm-mcp-server auth   # auth Google
npx notebooklm-mcp-server start  # chạy server
```

```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "npx",
      "args": ["-y", "notebooklm-mcp-server", "start"]
    }
  }
}
```

---

## Đánh Giá Cá Nhân

Simple, reliable, auto-update là điểm cộng lớn nhất. Không có advanced features như roomi-fields nhưng không cần — mục tiêu là zero-maintenance.

Phù hợp nhất: VS Code users muốn setup 1 lần rồi quên.

**Rating: 7.5/10**

---

*Nguồn: github.com/moodRobotics/notebooklm-mcp-server | Cập nhật: tháng 6/2026*

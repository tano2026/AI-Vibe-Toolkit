# notebooklm-mcp-2026 — NotebookLM MCP Python, Auth Qua Chrome DevTools

**GitHub:** https://github.com/julianoczkowski/notebooklm-mcp-2026
**License:** MIT | **Language:** Python
**Install:** `pip install notebooklm-mcp-2026`
**Dùng với:** Claude Code, Cursor — Python-first workflow

---

## Khác Gì Với Bản Khác?

Các bản khác dùng Node.js/TypeScript. Bản này dùng **Python thuần** — phù hợp data scientists, ML engineers có Python environment sẵn.

Auth dùng **Chrome DevTools Protocol** thay vì Playwright browser automation.

---

## Cài Và Dùng

```bash
pip install notebooklm-mcp-2026
notebooklm-mcp-2026 login  # đóng Chrome trước khi chạy
```

```json
{
  "mcpServers": {
    "notebooklm-mcp-2026": {
      "command": "notebooklm-mcp-2026",
      "args": ["serve"]
    }
  }
}
```

**4 tools:** `list_notebooks`, `list_sources`, `query_notebook`, `get_source_content`

**Lưu ý:** Phải đóng Chrome hoàn toàn trước khi login. Cookies hết hạn 2-4 tuần.

---

## Đánh Giá Cá Nhân

Feature set đơn giản nhất — chỉ 4 tools cơ bản. Nhưng nếu mày là Python user không muốn cài Node.js, đây là lựa chọn clean nhất.

**Rating: 7/10**

---

*Nguồn: github.com/julianoczkowski/notebooklm-mcp-2026 | Cập nhật: tháng 6/2026*

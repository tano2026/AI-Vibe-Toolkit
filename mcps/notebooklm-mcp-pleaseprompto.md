# notebooklm-mcp (PleasePrompto) — Kết Nối Claude Với NotebookLM, Zero Hallucination

**GitHub:** https://github.com/PleasePrompto/notebooklm-mcp
**Stars:** 2.7k | **Forks:** 375 | **License:** MIT
**Install:** `npx notebooklm-mcp@latest`
**Dùng với:** Claude Code, Codex, Cursor, VS Code

---

## Vấn Đề Nó Giải Quyết

Claude hay GPT giỏi nhưng 2 vấn đề khi làm việc với tài liệu dài:
- **Hallucinate** — bịa thông tin không có trong doc
- **Token limit** — paste tài liệu vào chat tốn token, chậm

NotebookLM của Google giải quyết cả 2: chỉ trả lời dựa trên sources mày upload, có citation cụ thể. Không bịa.

**notebooklm-mcp** nối Claude Code với NotebookLM:
```
Mày hỏi Claude → Claude query NotebookLM → NotebookLM trả answer + citation → Claude tổng hợp
```

---

## Cài Đặt

```bash
npx notebooklm-mcp@latest auth  # auth Google lần đầu
```

```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "npx",
      "args": ["-y", "notebooklm-mcp@latest"]
    }
  }
}
```

---

## Tools Có Sẵn

| Tool | Làm gì |
|------|--------|
| `list_notebooks` | List tất cả notebooks |
| `list_sources` | Xem sources trong notebook |
| `query_notebook` | Hỏi câu hỏi, nhận answer có citation |
| `get_source_content` | Đọc raw text của source |
| `create_notebook` | Tạo notebook mới |
| `add_source` | Thêm URL/file vào notebook |

---

## Workflow Thực Tế

1. Upload tài liệu vào notebooklm.google.com
2. Cài MCP, auth Google
3. Hỏi Claude bất cứ câu nào → Claude query NotebookLM → answer có citation

**Use cases:** Research tài liệu kỹ thuật, Q&A trên documentation, đọc nhiều papers cùng lúc, knowledge base cho team.

---

## Lưu Ý

**Browser automation:** Dùng Playwright điều khiển browser — không phải API chính thức. Google đổi UI là có thể gãy tạm (tháng 4/2026 đã xảy ra, fix trong 24-72h).

**Auth bằng cookies:** Hết hạn 2-4 tuần cần auth lại.

---

## Đánh Giá Cá Nhân

2.7k stars, 375 forks — repo được dùng nhiều nhất trong ecosystem. Install 1 lệnh `npx`, không setup phức tạp. Tao dùng cái này để research codebase mới: upload docs vào NotebookLM, hỏi Claude — không hallucinate, có citation.

**Rating: 8.5/10** — best choice cho vibe coders muốn setup nhanh.

---

*Nguồn: github.com/PleasePrompto/notebooklm-mcp | Cập nhật: tháng 6/2026*

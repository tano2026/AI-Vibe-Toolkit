# notebooklm-mcp (roomi-fields) — Power User Version: MCP + HTTP REST API + Docker

**GitHub:** https://github.com/roomi-fields/notebooklm-mcp
**Stars:** 89 | **Forks:** 26 | **License:** MIT
**Install:** `npm install -g @roomi-fields/notebooklm-mcp`
**Dùng với:** Claude Code, n8n, Zapier, Make, Docker CI/CD

---

## Tại Sao Dùng Bản Này Thay Vì PleasePrompto?

| Feature | PleasePrompto (2.7k ⭐) | roomi-fields (89 ⭐) |
|---------|------------------------|---------------------|
| MCP stdio | ✅ | ✅ |
| HTTP REST API | ❌ | ✅ |
| Docker | ❌ | ✅ |
| n8n/Zapier/Make | ❌ | ✅ |
| Audio/Video/Infographic gen | ❌ | ✅ |
| Multi-account rotation | ❌ | ✅ |
| Citation accuracy | Basic | 97% |
| TOTP re-auth | ❌ | ✅ |

roomi-fields là **power user version** — nhiều tính năng hơn, phức tạp hơn.

---

## HTTP REST API Mode — Unique Feature

```bash
notebooklm-mcp serve --port 3000
```

```bash
# Bất kỳ tool nào gọi HTTP đều dùng được
curl -X POST http://localhost:3000/query \
  -d '{"notebook_id": "xxx", "question": "Tóm tắt document"}'
```

Mở ra integration với n8n, Zapier, Make — **không chỉ AI agents**.

---

## Content Generation

```bash
# Tạo audio podcast từ notebook
POST /generate {"type": "audio", "notebook_id": "xxx"}

# Tạo infographic
POST /generate {"type": "infographic", "notebook_id": "xxx"}

# Tạo video script
POST /generate {"type": "video", "notebook_id": "xxx"}
```

---

## Docker Cho CI/CD

```bash
docker run -p 3000:3000 -p 6080:6080 \
  -v ./auth.json:/app/auth.json \
  roomifields/notebooklm-mcp
# Port 3000: HTTP API | Port 6080: noVNC để login Google
```

---

## Workflow n8n Automation

```
Trigger: File mới trên Google Drive
→ n8n: Add source vào NotebookLM
→ n8n: POST /query "Tóm tắt document"
→ n8n: Send summary lên Slack
```

Toàn bộ knowledge pipeline tự động.

---

## Đánh Giá Cá Nhân

Stars thấp hơn nhưng feature set vượt trội. Tác giả AI consultant 15 năm cybersecurity tại Airbus — update consistency tốt (v1.7.8, 174 commits).

Chọn roomi-fields khi cần: n8n automation, Docker CI/CD, generate audio/video. Chọn PleasePrompto khi chỉ cần query đơn giản từ Claude Code.

**Rating: 8/10**

---

*Nguồn: github.com/roomi-fields/notebooklm-mcp | Cập nhật: tháng 6/2026*

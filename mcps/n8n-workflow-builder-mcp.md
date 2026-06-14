# mcp-n8n-workflow-builder — Tạo n8n Workflows Bằng Ngôn Ngữ Thường (226⭐)

**GitHub:** https://github.com/salacoste/mcp-n8n-workflow-builder
**Stars:** 226⭐ | **License:** MIT | **npm:** @kernel.salacoste/n8n-workflow-builder
**Docs:** salacoste.github.io/mcp-n8n-workflow-builder

---

## Đây Là Gì

MCP server để build, manage, monitor n8n workflows **bằng ngôn ngữ tự nhiên qua Claude**.

Thay vì drag-drop trong n8n UI → nói với Claude → Claude tạo workflow → deploy thẳng vào n8n.

---

## Cài Đặt

```bash
npm install -g @kernel.salacoste/n8n-workflow-builder
```

```json
{
  "mcpServers": {
    "n8n-workflow-builder": {
      "command": "npx",
      "args": ["@kernel.salacoste/n8n-workflow-builder"],
      "env": {
        "N8N_HOST": "http://localhost:5678",
        "N8N_API_KEY": "your-n8n-api-key"
      }
    }
  }
}
```

**Lấy API key:** n8n UI → Settings → API → Create API Key

---

## Dùng Ngay

```bash
# Tạo workflow mới
"Tạo n8n workflow: mỗi sáng 8h fetch GitHub trending repos → 
 filter AI repos → gửi summary qua Telegram"

# Manage workflows
"List tất cả workflows đang active"
"Pause workflow 'Daily Report'"
"Get executions history của workflow X trong 7 ngày qua"

# Monitor
"Workflow nào failed trong 24h qua? Lý do gì?"
"Get execution logs của lần chạy cuối workflow Y"

# Update
"Thêm bước gửi Slack vào cuối workflow X"
"Đổi schedule của workflow Y từ daily sang weekly"
```

---

## Tools Có Sẵn

| Tool | Làm gì |
|------|--------|
| `create_workflow` | Tạo workflow từ JSON hoặc description |
| `get_workflow` | Get chi tiết một workflow |
| `list_workflows` | List tất cả với filter |
| `update_workflow` | Update workflow hiện có |
| `activate_workflow` | Bật/tắt workflow |
| `delete_workflow` | Xóa workflow |
| `execute_workflow` | Chạy workflow ngay |
| `get_executions` | History executions |
| `get_execution` | Chi tiết 1 execution |
| `stop_execution` | Dừng execution đang chạy |

---

## Workflow Hay Nhất Cho AI Vibe Toolkit

```bash
# 1. Auto-research trending AI repos
"Tạo workflow: 6h sáng → fetch last30days trending → 
 filter AI/Claude repos → gửi Telegram summary"

# 2. Content pipeline
"Workflow: khi có file mới trong Google Drive /drafts/ → 
 check grammar với Claude → move sang /reviewed/ → notify Slack"

# 3. GitHub monitor
"Workflow: check repo tano2026/AI-Vibe-Toolkit mỗi giờ → 
 khi có star mới → update counter → gửi Discord notification"

# 4. Lead capture
"Workflow: form submission webhook → enrich với Clearbit → 
 add vào HubSpot → assign to Slack channel based on company size"
```

---

*Nguồn: github.com/salacoste/mcp-n8n-workflow-builder | 226⭐ | MIT | tháng 6/2026*

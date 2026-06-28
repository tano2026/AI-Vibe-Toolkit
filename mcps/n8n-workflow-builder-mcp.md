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

---

## 🤖 Agent Integration

> Section này dành cho Hermes/OpenClaw/Antigravity — không phải cho human đọc.

### Hermes (Python — gọi thẳng, không cần MCP)
```python
import urllib.request, json

N8N_URL = "http://localhost:5678"  # sau khi Antigravity deploy

def n8n_trigger_workflow(workflow_id, data, api_key):
    payload = json.dumps(data).encode()
    req = urllib.request.Request(
        f"{N8N_URL}/api/v1/workflows/{workflow_id}/activate",
        data=payload,
        headers={"X-N8N-API-KEY": api_key, "Content-Type": "application/json"}
    )
    return json.loads(urllib.request.urlopen(req).read())

def n8n_webhook(webhook_path, data):
    """Trigger workflow qua webhook (không cần API key)"""
    payload = json.dumps(data).encode()
    req = urllib.request.Request(
        f"{N8N_URL}/webhook/{webhook_path}",
        data=payload, headers={"Content-Type": "application/json"}
    )
    return json.loads(urllib.request.urlopen(req).read())

def n8n_list_workflows(api_key):
    req = urllib.request.Request(
        f"{N8N_URL}/api/v1/workflows",
        headers={"X-N8N-API-KEY": api_key}
    )
    return json.loads(urllib.request.urlopen(req).read())["data"]
```

### OpenClaw (npm/ClawHub)
```bash
npx -y n8n-mcp
# Set N8N_API_URL và N8N_API_KEY trong env
```

### Antigravity (deploy nếu cần self-host)
```bash
# Deploy n8n:
docker run -d --name n8n -p 5678:5678 \
  -e N8N_BASIC_AUTH_ACTIVE=true \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
# Sau đó lấy API key từ n8n UI → Settings → API
```
> ⚠️ Antigravity deploy Docker trước. Hermes gọi webhook không cần API key.

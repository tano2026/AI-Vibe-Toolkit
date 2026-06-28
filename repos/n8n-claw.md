# n8n-claw — Build AI Agent Tự Vận Hành Bằng n8n, 1 Lệnh Setup

> OpenClaw nhưng chạy bằng n8n — visual workflow, không cần terminal, self-hosted, kết nối Telegram/Slack, có memory và sub-agents. 1 script setup xong.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **GitHub** | [freddy-schuetz/n8n-claw](https://github.com/freddy-schuetz/n8n-claw) |
| **Tác giả** | Freddy Schuetz |
| **Tech stack** | n8n + PostgreSQL + Claude/OpenAI |
| **Free** | ✅ Self-hosted free |
| **Yêu cầu** | VPS hoặc máy tính luôn bật, Docker |

---

## 🎯 n8n-claw là gì

Nếu OpenClaw là "AI agent chạy trong terminal" thì n8n-claw là "AI agent chạy bằng visual workflow":

- **Không cần biết code** — mọi thứ là n8n workflows
- **Memory thật** — nhớ conversation, build knowledge theo thời gian
- **Sub-agents** — có thể delegate task cho specialist agents
- **Multi-channel** — Telegram, Slack, Teams, HTTP
- **Proactive** — tự chạy task scheduled, tự ping mày khi cần
- **MCP Skills** — cài skills bằng chat như OpenClaw

---

## ⚡ Setup trong 1 lệnh

```bash
git clone https://github.com/freddy-schuetz/n8n-claw.git
cd n8n-claw
./setup.sh

# Script hỏi mày:
# - Telegram bot token (tạo từ @BotFather)
# - LLM provider (Claude/OpenAI/Gemini/Ollama...)
# - API key
# - Agent personality (tên, ngôn ngữ, phong cách)

# Xong → nhắn Telegram bot → agent sống rồi
```

---

## 💡 Use cases thực tế

```
Nhắn Telegram bot:
"Mỗi sáng 7h tóm tắt 3 tin AI hot nhất"
→ Agent tự setup schedule, tự chạy

"Research công ty X trước buổi meeting 2h nữa"  
→ Agent search web, tổng hợp, gửi báo cáo

"Cài skill notion cho tao"
→ Agent tự cài, tự config, confirm khi xong
```

---

## ⚠️ Lưu ý

- Cần VPS hoặc máy luôn bật (agent cần chạy 24/7)
- Docker bắt buộc
- Docs khá technical — nhờ Claude giải thích khi cần
- Community còn nhỏ hơn OpenClaw

---

## 🔗 Hay kết hợp với

- **OpenClaw** — dùng song song: OpenClaw cho coding tasks, n8n-claw cho automation workflows
- **Kho AI Vibe Toolkit** — n8n-claw đọc kho, tự chọn content, tự đăng → đây là pipeline tự động mày đang build

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Dễ setup | ⭐⭐⭐☆☆ |
| Powerful | ⭐⭐⭐⭐⭐ |
| Phù hợp vision của project | ⭐⭐⭐⭐⭐ |

**Tóm lại:** Đây là bước tiếp theo của project mày — feed kho AI Vibe Toolkit vào n8n-claw → agent tự lấy script, tự tạo video, tự đăng. Vision "AI tự vận hành kênh" bắt đầu từ đây.

---

*Thêm vào kho: 06/2025 | Nguồn: github.com/freddy-schuetz/n8n-claw*

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

N8N_URL = "http://localhost:5678"
N8N_KEY = "[N8N_API_KEY]"  # Settings → n8n API → Create API key

def trigger_webhook(webhook_id, data):
    """Trigger workflow qua webhook — không cần API key"""
    payload = json.dumps(data).encode()
    req = urllib.request.Request(
        f"{N8N_URL}/webhook/{webhook_id}", data=payload,
        headers={"Content-Type": "application/json"}
    )
    return json.loads(urllib.request.urlopen(req).read())

def list_workflows():
    req = urllib.request.Request(
        f"{N8N_URL}/api/v1/workflows",
        headers={"X-N8N-API-KEY": N8N_KEY}
    )
    return json.loads(urllib.request.urlopen(req).read())["data"]

def activate_workflow(wf_id):
    req = urllib.request.Request(
        f"{N8N_URL}/api/v1/workflows/{wf_id}/activate",
        data=b"{}", headers={"X-N8N-API-KEY": N8N_KEY}, method="POST"
    )
    return json.loads(urllib.request.urlopen(req).read())

# Pattern: Hermes trigger webhook → n8n xử lý workflow phức tạp → trả kết quả
```

### OpenClaw
```bash
# n8n có UI riêng — OpenClaw không cần cài gì thêm
```

### Antigravity
```bash
# Script setup từ n8n-claw repo:
git clone https://github.com/freddy-schuetz/n8n-claw
cd n8n-claw && cp .env.example .env && nano .env
docker compose up -d
# Mở: http://localhost:5678
```
> ⚠️ Hermes trigger webhook, n8n xử lý workflow, kết quả trả về JSON.

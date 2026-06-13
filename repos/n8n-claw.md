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

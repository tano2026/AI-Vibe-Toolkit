---
name: librechat
description: >
  Tác giả: danny-avila Domain: Nền tảng chat AI self-hosted, gộp nhiều LLM + Agents + MCP vào 1 giao diện
---

# LibreChat — tự host ChatGPT-clone, gộp mọi LLM + MCP vào 1 chỗ

**GitHub:** https://github.com/danny-avila/LibreChat
**Tác giả:** danny-avila | Nhiều fork phổ biến (Extremys, BillulloNex...) nhưng bản gốc là danny-avila

---

## TL;DR

Giao diện chat AI tự host, giống ChatGPT nhưng không khoá vào 1 hãng — cắm được OpenAI, Anthropic, Gemini, DeepSeek, AWS Bedrock, Azure, Mistral, OpenRouter... cùng lúc, có Agents, hỗ trợ MCP, Artifacts, Code Interpreter, đa người dùng có xác thực.

## Tool này dùng để làm gì

Thay vì trả tiền riêng cho ChatGPT Plus + Claude Pro + Gemini Advanced, LibreChat cho phép dùng API pay-per-call của tất cả các hãng trong 1 giao diện duy nhất, tự host trên VPS của mình — dữ liệu không rời khỏi hạ tầng riêng. Có sẵn:
- **AI Agents** — tạo agent tuỳ biến, gắn tool riêng
- **MCP support** — cắm được MCP server giống Claude Desktop
- **Artifacts** — hiển thị code/UI trực tiếp trong chat giống Claude.ai
- **Code Interpreter** — chạy code trong sandbox
- **Multi-user** — OAuth2, LDAP, email login, quản lý token spend theo user
- **Đa ngôn ngữ** — có sẵn Tiếng Việt trong danh sách UI hỗ trợ

## Setup từng bước

1. Clone repo, dùng Docker Compose (cách nhanh nhất):
```bash
git clone https://github.com/danny-avila/LibreChat.git
cd LibreChat
cp .env.example .env
```
2. Điền API key các provider muốn dùng vào `.env` (OPENAI_API_KEY, ANTHROPIC_API_KEY...)
3. Chạy:
```bash
docker compose up -d
```
4. Truy cập `localhost:3080`, tạo tài khoản admin đầu tiên

## Ví dụ thực tế

Tano Agency deploy LibreChat trên VPS riêng cho team ABTRIP dùng nội bộ — nhân viên đăng nhập bằng email công ty, chọn model tuỳ task (Claude cho viết content, GPT cho code), chi phí API tính theo dùng thật thay vì mua nhiều gói riêng lẻ cho từng người.

## Lưu ý / Lỗi thường gặp

- Nhiều fork trùng tên trên GitHub (Extremys, BillulloNex, arelice, revbin, designcomputer, RichardSto...) — đây đều là clone/fork cá nhân, LUÔN dùng bản gốc `danny-avila/LibreChat` để đảm bảo cập nhật bảo mật đầy đủ
- Deploy Docker cần VPS đủ RAM (khuyến nghị tối thiểu 2-4GB) — nếu chạy chung với nhiều service khác trên cùng VPS cần theo dõi tài nguyên
- Cấu hình MCP/Agents cần đọc kỹ docs vì có khá nhiều biến môi trường liên quan

## Đánh giá cá nhân

- **Điểm mạnh:** tự chủ hạ tầng, không phụ thuộc uptime của bên thứ 3; gộp nhiều LLM tiết kiệm hơn mua nhiều gói riêng; tính năng gần bằng Claude.ai/ChatGPT (Artifacts, Code Interpreter) mà miễn phí
- **Điểm yếu:** cần tự vận hành VPS, tự chịu trách nhiệm bảo mật/backup; không có support chính thức như dịch vụ trả phí
- **Có nên dùng không:** 8/10 — rất hợp nếu Tano Agency muốn 1 giao diện chat nội bộ cho cả team ABTRIP dùng chung nhiều LLM, tiết kiệm chi phí dài hạn

## Link
- Repo: https://github.com/danny-avila/LibreChat
- Docs: https://docs.librechat.ai

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# LibreChat có REST API tương thích OpenAI format sau khi tự host
import urllib.request, json

LIBRECHAT_URL = "http://your-vps-ip:3080/api/v1/chat/completions"
def call_librechat(message, api_key):
    payload = json.dumps({"model": "claude-sonnet", "messages": [{"role": "user", "content": message}]}).encode()
    req = urllib.request.Request(LIBRECHAT_URL, data=payload,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}, method="POST")
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
git clone https://github.com/danny-avila/LibreChat.git
cd LibreChat && cp .env.example .env
docker compose up -d
```

### Antigravity
```bash
# Deploy trên VPS — cần Docker + Docker Compose sẵn
docker --version && docker compose version
git clone https://github.com/danny-avila/LibreChat.git /opt/librechat
cd /opt/librechat && docker compose up -d
```
> ⚠️ Nhớ đổi `JWT_SECRET` và `CREDS_KEY` mặc định trong `.env` trước khi public ra internet — để mặc định là lỗ hổng bảo mật nghiêm trọng.

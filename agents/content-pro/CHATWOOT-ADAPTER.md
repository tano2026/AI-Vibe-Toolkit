# CHATWOOT-ADAPTER.md — Content Pro

> Chatwoot KHÔNG có cơ chế "dán system-prompt vào 1 ô" như Mission Control
> hay Claude.ai Project. Nó là tool inbox/customer support, hoạt động qua
> **Agent Bot + Webhook 2 chiều**: Chatwoot bắn event tới URL của mày khi
> có tin nhắn mới → mày xử lý → gọi lại API Chatwoot để trả lời. Cần 1
> service chạy NỀN (không phải chạy 1 lần) — khác hẳn cách Hermes/Content
> Pro vận hành hiện tại (task rời rạc qua Telegram).

## Vì sao dùng Chatwoot cho Content Pro

Chatwoot cho phép biến mỗi "Pro agent" thành 1 inbox riêng — Nobitano/Content
Lead nhắn vào inbox "Content Pro" y như nhắn 1 nhân viên thật, nhận trả lời
ngay trong giao diện chat quen thuộc, thay vì phải mở Claude.ai Project
hoặc Mission Control riêng. Hợp nếu mày muốn dồn nhiều agent (CEO, Sales,
Content, Media...) về chung 1 giao diện inbox duy nhất.

## Kiến trúc

```
Người dùng nhắn vào inbox "Content Pro" trên Chatwoot
        │
        ▼
Chatwoot bắn webhook (event: message_created) tới URL đã đăng ký
        │
        ▼
Webhook receiver (chạy trên VPS qua PM2, Antigravity deploy)
        │
        ├─→ Đọc nội dung tin nhắn
        ├─→ Load Content Pro system-prompt + skill liên quan (fetch từ kho)
        ├─→ Gọi LLM qua OmniRoute (đã có sẵn, routing theo tier)
        │
        ▼
Nhận response từ LLM
        │
        ▼
POST lại vào Chatwoot API → hiện trả lời trong inbox
```

## Bước 1 — Đăng ký Agent Bot trong Chatwoot

```
Chatwoot → Settings → Integrations → Agent Bots → New Agent Bot
- Đặt tên: "Content Pro"
- Outgoing URL: https://<vps-domain>/webhook/content-pro (endpoint mày tự
  dựng, xem Bước 2)
- Lưu lại Access Token của bot (dùng để gọi ngược lại Chatwoot API)
```

Gán Agent Bot này vào 1 Inbox riêng (Settings → Inboxes → chọn inbox → gán
Agent Bot "Content Pro") — mỗi Pro agent nên có 1 inbox riêng, không dùng
chung 1 inbox cho nhiều agent (dễ lẫn lộn ai trả lời gì).

## Bước 2 — Webhook receiver (Python thuần, deploy qua Antigravity)

```python
# server.py — chạy như 1 service nền (pm2 start server.py --interpreter python3)
import urllib.request, json, os
from http.server import HTTPServer, BaseHTTPRequestHandler

CHATWOOT_URL = os.environ.get("CHATWOOT_URL", "https://your-chatwoot.com")
CHATWOOT_BOT_TOKEN = os.environ.get("CHATWOOT_BOT_TOKEN", "")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
OMNIROUTE_ENDPOINT = os.environ.get("OMNIROUTE_ENDPOINT", "")  # theo cấu hình OmniRoute hiện có

def fetch_kho_file(path):
    req = urllib.request.Request(
        f"https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/{path}",
        headers={"Authorization": f"token {GITHUB_TOKEN}"})
    with urllib.request.urlopen(req, timeout=15) as r:
        import base64
        data = json.loads(r.read())
        return base64.b64decode(data['content']).decode()

def call_llm(system_prompt, user_message):
    """Gọi qua OmniRoute — điều chỉnh payload theo đúng format OmniRoute
    thật đang dùng (đây là khung mẫu, cần khớp API thật của OmniRoute)."""
    payload = json.dumps({
        "model": "balanced",  # theo tier OmniRoute đã cấu hình
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    }).encode()
    req = urllib.request.Request(OMNIROUTE_ENDPOINT, data=payload,
                                   headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        result = json.loads(r.read())
        return result["choices"][0]["message"]["content"]

def send_chatwoot_reply(account_id, conversation_id, content):
    url = f"{CHATWOOT_URL}/api/v1/accounts/{account_id}/conversations/{conversation_id}/messages"
    payload = json.dumps({"content": content, "message_type": "outgoing", "private": False}).encode()
    req = urllib.request.Request(url, data=payload, headers={
        "api_access_token": CHATWOOT_BOT_TOKEN,
        "Content-Type": "application/json"
    })
    urllib.request.urlopen(req, timeout=15)

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        body = json.loads(self.rfile.read(length))

        # Chỉ xử lý tin nhắn thật từ người (incoming), bỏ qua echo/system event
        if body.get("event") == "message_created" and body.get("message_type") == "incoming":
            user_message = body.get("content", "")
            account_id = body["account"]["id"]
            conversation_id = body["conversation"]["id"]

            # Load system-prompt Content Pro (fetch từ kho, luôn bản mới nhất)
            system_prompt = fetch_kho_file("agents/content-pro/system-prompt.md")

            reply = call_llm(system_prompt, user_message)
            send_chatwoot_reply(account_id, conversation_id, reply)

        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8787), WebhookHandler)
    server.serve_forever()
```

## Bước 3 — Deploy qua Antigravity

```bash
# Trên VPS
export CHATWOOT_URL="https://your-chatwoot-instance.com"
export CHATWOOT_BOT_TOKEN="<token lấy ở Bước 1>"
export GITHUB_TOKEN="ghp_..."
export OMNIROUTE_ENDPOINT="<endpoint OmniRoute thật>"
pm2 start server.py --name content-pro-chatwoot --interpreter python3
```

Domain `https://<vps-domain>/webhook/content-pro` cần trỏ đúng port 8787
(qua Nginx/Caddy reverse proxy nếu VPS đã có sẵn, hoặc mở port trực tiếp
nếu chấp nhận rủi ro bảo mật thấp hơn — khuyến nghị dùng reverse proxy).

## Giới hạn thật (không giấu)

- **Đây là bản khung mẫu**, chưa test thật trên VPS — cần Antigravity chạy thử trước khi tin cậy production
- Chưa có xử lý lỗi đầy đủ (network timeout, LLM trả lỗi, Chatwoot API rate limit) — bản production cần bọc try/except đầy đủ hơn, đúng luật "fail to tiếng" trong `dev-automation-discipline`
- Chatwoot webhook HMAC signature (xác thực webhook đến từ đúng Chatwoot, không phải giả mạo) — theo nguồn research, tính năng này **đã merge vào dev branch nhưng CHƯA có bản ổn định** tại thời điểm viết adapter này — cần kiểm tra lại version Chatwoot đang dùng có hỗ trợ chưa trước khi tin tưởng an toàn 100%
- Chưa xử lý context/lịch sử hội thoại — bản trên chỉ gửi 1 tin nhắn đơn lẻ, không nhớ conversation trước đó trong cùng thread; cần thêm logic lưu/load lịch sử nếu muốn hội thoại liền mạch
- Skill Content Pro tham chiếu (viral-hooks, brand-voice...) chưa được fetch tự động trong khung mẫu này — cần bổ sung logic tương tự `load_skill()` đã viết trong `HERMES-ADAPTER.md` nếu muốn dùng đầy đủ

## Việc cần làm trước khi tin dùng thật

1. Antigravity test thử trên VPS, xác nhận webhook nhận đúng, LLM trả lời đúng, Chatwoot hiện tin nhắn đúng
2. Xác nhận version Chatwoot đang dùng có HMAC signature verify chưa
3. Bọc try/except đầy đủ, log lỗi qua Telegram (đúng luật `dev-automation-discipline`)
4. Nếu cần nhớ lịch sử hội thoại — bổ sung lưu trạng thái theo `conversation_id`

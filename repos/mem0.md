# Mem0 — Cho AI Agent Có Ký Ức Thật, Nhớ Mọi Thứ Về Mày

> 48k stars, $24M Series A, YC-backed. Cài vào AI agent — nó nhớ preferences, lịch sử, quyết định của mày. Không cần training. Không cần chờ. Setup 20 phút.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **GitHub** | [mem0ai/mem0](https://github.com/mem0ai/mem0) ⭐ 48,000+ |
| **Funding** | $24M Series A, YC-backed |
| **Setup** | < 20 phút |
| **Free** | ✅ Open source + Cloud tier |
| **Tích hợp** | 21 frameworks, 20 vector stores |

---

## 🎯 Vấn đề nó giải quyết

AI agents mặc định **không có ký ức** — mỗi conversation mới là bắt đầu từ đầu.

Mày dùng OpenClaw, n8n-claw, hay bất kỳ agent nào → nó không nhớ:
- Mày thích làm việc thế nào
- Những quyết định mày đã đưa ra
- Context từ tuần trước

**Mem0 fix:** Layer memory bên ngoài — agent đọc/ghi memories qua API. Nhớ theo thời gian, học từ interaction, không mất khi restart.

---

## ⚡ Setup trong 20 phút

```python
# Cài
pip install mem0ai

# Dùng ngay (cloud - không cần infra)
from mem0 import MemoryClient
client = MemoryClient(api_key="your-api-key")

# Lưu memory
client.add("Tao thích output ngắn gọn, tiếng Việt", user_id="tano")

# Lấy memory liên quan
memories = client.search("style viết", user_id="tano")
```

---

## 💡 Kết hợp với OpenClaw/n8n-claw

```
Mày nói với agent: "Tao thích được báo kết quả bằng Telegram, 
không cần giải thích dài"

→ Agent lưu vào Mem0
→ Lần sau tự nhớ, không cần nhắc lại

Mày nói: "Content kênh tao target vibe coders VN, 
tone casual, không jargon"

→ Agent nhớ → mọi task sau đều tự apply
```

---

## 🏗️ Kiến trúc

Mem0 kết hợp 3 loại storage:
- **Vector search** — tìm memories liên quan theo ngữ nghĩa
- **Knowledge graph** — lưu relationships giữa các facts
- **Key-value cache** — truy cập nhanh

---

## ⚠️ Lưu ý

- Cloud tier free có giới hạn — self-host với Docker cho unlimited
- Graph memory (feature hay nhất) chỉ có ở Pro plan ($249/tháng)
- Cần biết Python cơ bản để integrate

---

## 🔗 Hay kết hợp với

- **OpenClaw** — add Mem0 vào để agent nhớ preferences của mày
- **n8n-claw** — n8n-claw đã có memory built-in nhưng Mem0 powerful hơn
- **Toàn bộ AI agents** — Mem0 là layer memory universal

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Giải quyết pain point thật | ⭐⭐⭐⭐⭐ |
| Dễ integrate | ⭐⭐⭐⭐☆ |
| Cần biết code | ⭐⭐⭐☆☆ |
| Content angle | ⭐⭐⭐⭐⭐ |

**Tóm lại:** "AI agent vừa mọc ký ức" — đây chính xác là hook. 48k stars, YC-backed, $24M funding. Angle video: trước/sau khi có Mem0 — agent nhớ vs không nhớ.

---

*Thêm vào kho: 06/2025 | Phát hiện qua: @DevAtlas TikTok | Nguồn: github.com/mem0ai/mem0*

---

## 🤖 Agent Integration

> Section này dành cho Hermes/OpenClaw/Antigravity.

### Hermes (Python)
```python
import urllib.request, json

# Option A: Cloud API
MEM0_API_KEY = "[MEM0_API_KEY]"
MEM0_URL = "https://api.mem0.ai/v1"

def mem0_add(content, user_id="tano", api_key=MEM0_API_KEY):
    payload = json.dumps({"messages": [{"role": "user", "content": content}],
                          "user_id": user_id}).encode()
    req = urllib.request.Request(f"{MEM0_URL}/memories/", data=payload,
        headers={"Authorization": f"Token {api_key}", "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())

def mem0_search(query, user_id="tano", api_key=MEM0_API_KEY):
    payload = json.dumps({"query": query, "user_id": user_id}).encode()
    req = urllib.request.Request(f"{MEM0_URL}/memories/search/", data=payload,
        headers={"Authorization": f"Token {api_key}", "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())

def mem0_get_all(user_id="tano", api_key=MEM0_API_KEY):
    req = urllib.request.Request(f"{MEM0_URL}/memories/?user_id={user_id}",
        headers={"Authorization": f"Token {api_key}"})
    return json.loads(urllib.request.urlopen(req).read())

# Dùng: mem0_add("Nobitano thích output ngắn gọn, tiếng Việt casual")
# memories = mem0_search("style viết")
```

### OpenClaw
```bash
# Dùng qua Hermes delegate
# hoặc: npm install mem0ai
```

### Antigravity
```bash
# Self-host với Docker:
docker run -d -p 8000:8000 \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  --name mem0 mem0ai/mem0:latest
# Sau đó dùng MEM0_URL=http://localhost:8000
```
> ⚠️ Cloud free tier có giới hạn. Self-host free unlimited nhưng cần OpenAI key.

# headroom — Token Compression 60-95%, Cùng Câu Trả Lời (27.5k⭐)

**GitHub:** https://github.com/chopratejas/headroom
**Stars:** 27.5k⭐ | **License:** MIT | **Language:** Python
**#2 GitHub Trending Tuần 23** | +13,308 stars tuần này
**Install:** `pip install headroom`

---

## Đây Là Gì

Context compression layer cho AI agents — **compress tool outputs, logs, files, RAG chunks trước khi đưa vào LLM**. Giảm 60-95% tokens, câu trả lời vẫn như nhau.

```
Tool output 50,000 tokens
→ headroom compress
→ 2,500 tokens
→ Feed LLM
= Tiết kiệm 95% cost, cùng chất lượng
```

---

## 3 Cách Dùng

### Library (Python)
```python
from headroom import compress

# Compress bất kỳ string nào
text = open("big_log.txt").read()  # 50k tokens
compressed = compress(text, max_tokens=2000)
# → 2000 tokens, giữ thông tin quan trọng
```

### Proxy (Drop-in replacement)
```bash
# Chạy headroom proxy thay thế API endpoint
headroom serve --port 8080 --target https://api.anthropic.com

# Trong code: đổi base_url
client = anthropic.Anthropic(base_url="http://localhost:8080")
# → Tự động compress mọi request trước khi gửi
```

### MCP Server
```json
{
  "mcpServers": {
    "headroom": {
      "command": "headroom",
      "args": ["mcp"]
    }
  }
}
```

```bash
# Trong Claude Code
"Compress file log này trước khi analyze: server.log"
"Compress RAG chunks này, giữ tối đa 2000 tokens"
```

---

## Khi Nào Dùng

✅ **Tool output dài** — bash commands, test results, build logs
✅ **RAG chunks lớn** — documents dài cần fit vào context
✅ **File analysis** — đọc file lớn không cần toàn bộ
✅ **Cost optimization** — giảm bill API 60-95%

❌ Không dùng khi cần TOÀN BỘ nội dung (legal docs, code review)

---

## Tích Hợp Với Hermes Agent

```python
# Hermes L7 (Context Compression) có thể dùng headroom
# Thay vì tóm tắt bằng LLM → dùng headroom (nhanh hơn, rẻ hơn)
from headroom import compress

# Trước khi feed vào context
compressed_tool_output = compress(tool_result, max_tokens=500)
```

---

## Đánh Giá Cá Nhân

27.5k stars, +13,308 trong 1 tuần — concept đơn giản nhưng giải quyết vấn đề thật: context window ngày càng đắt.

Điểm hay: **không cần thay đổi code nhiều** — dùng proxy mode là tất cả API calls tự được compress.

**Rating: 9/10** — Must-have cho bất kỳ ai chạy AI agent nhiều.

---
*Nguồn: github.com/chopratejas/headroom | 27.5k⭐ | MIT | tháng 6/2026*

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

SERVICE_URL = "http://localhost:8000"

def call_api(endpoint, data):
    payload = json.dumps(data).encode()
    req = urllib.request.Request(
        f"{SERVICE_URL}/{endpoint}", data=payload,
        headers={"Content-Type": "application/json"}
    )
    return json.loads(urllib.request.urlopen(req).read())

# Đọc README repo để biết endpoints cụ thể
# Antigravity deploy trước, Hermes gọi sau
```

### OpenClaw
```bash
# Gọi local API — không cần npm
```

### Antigravity
```bash
git clone https://github.com/[repo]
cd [repo] && pip install -r requirements.txt
cp .env.example .env && python3 main.py
```
> ⚠️ Audio/video processing tool

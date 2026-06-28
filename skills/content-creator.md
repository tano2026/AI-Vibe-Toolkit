# Skill: Content Creator — Từ 1 Ý Tưởng Ra 10 Loại Content

> Paste 1 chủ đề vào → Claude tạo script TikTok, caption, thumbnail idea, tweet, email — tất cả cùng lúc.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Loại** | Prompt Template |
| **Dùng với** | Claude |
| **Level** | Beginner |
| **Tốt nhất khi** | Làm content hàng ngày, cần repurpose 1 idea thành nhiều format |

---

## 🎯 Skill này làm được gì

1 ý tưởng → Claude output ra đủ loại content:
- Script video TikTok/Shorts (60s)
- Caption cho post
- 3 biến thể hook khác nhau
- Thumbnail concept
- Tweet/X thread
- Email subject line

---

## 📋 Prompt Template

```
Mày là Content Creator chuyên về [LĨNH VỰC].
Target audience: [MÔ TẢ AUDIENCE].
Tone: [casual/professional/hài hước/nghiêm túc].

Từ ý tưởng này, tạo ra:

**1. Script TikTok 60 giây**
- Hook (0-3s): câu mở đầu cực mạnh
- Problem (3-15s): pain point audience
- Solution (15-45s): nội dung chính + demo
- CTA (45-60s): kêu gọi hành động

**2. Caption (150 ký tự)**
Ngắn, có hook, có hashtags phù hợp.

**3. 3 Hook thay thế**
Để A/B test xem cái nào hiệu quả hơn.

**4. Thumbnail concept**
Text chính, text phụ, màu sắc gợi ý.

**5. Tweet version**
280 ký tự, punchline rõ ràng.

---
Ý tưởng: [PASTE Ý TƯỞNG VÀO ĐÂY]
```

---

## 💡 Ví dụ thực tế

**Input:**
```
Lĩnh vực: AI tools cho vibe coders
Audience: developer không chuyên, 20-30 tuổi VN
Tone: casual, hài hước nhẹ
Ý tưởng: Context7 MCP giúp Claude không bịa API
```

**Output:**
```
## Script TikTok 60s
Hook: "Claude vừa viết cho tao code dùng API... không tồn tại"
Problem: "AI coding tools bị giới hạn bởi training data cũ..."
...

## Caption
"AI hết bịa code rồi bro 😅 Context7 MCP = docs thật, không hallucinate
#claudeai #vibecoding #mcp"

## 3 Hook thay thế
1. "Tại sao code AI viết lại không chạy được?"
2. "MCP này fix lỗi phổ biến nhất khi vibe coding"  
3. "54k stars — đây là lý do"
...
```

---

## 🔧 Biến thể

**Repurpose từ video cũ:**
```
Tao có script video này [PASTE SCRIPT].
Tạo lại thành:
- Thread Twitter 5 tweets
- LinkedIn post professional
- Email newsletter 200 chữ
```

**Brainstorm ideas:**
```
Tao làm kênh về [CHỦ ĐỀ], audience là [AI].
Suggest 10 video ideas đang trending tuần này.
Mỗi idea: title, hook, tại sao nó potential viral.
```

---

## 📊 Đánh giá

| Tiêu chí | Điểm |
|----------|------|
| Tiết kiệm thời gian | ⭐⭐⭐⭐⭐ |
| Dễ dùng | ⭐⭐⭐⭐⭐ |
| Output cần edit thêm | ⭐⭐⭐☆☆ (cần tweak giọng điệu) |

---

*Thêm vào kho: 06/2025*

---

## 🤖 Hermes — Cách dùng skill này

**Use case:** viết content TikTok/YouTube script

```python
import urllib.request, json, base64

def fetch_skill(skill_file, token="[GITHUB_TOKEN]"):
    req = urllib.request.Request(
        f"https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/skills/{skill_file}",
        headers={"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    )
    data = json.loads(urllib.request.urlopen(req).read())
    return base64.b64decode(data["content"]).decode()

# Bước 1: Fetch skill này về
skill_prompt = fetch_skill("content-creator.md")

# Bước 2: Extract phần "Prompt Template" hoặc "Nội dung skill"
# (tìm block code đầu tiên sau header ## Prompt)
import re
match = re.search(r'```\n([\s\S]+?)\n```', skill_prompt)
prompt = match.group(1) if match else skill_prompt

# Bước 3: Nhúng vào LLM call
def call_with_skill(user_input, system_prompt):
    # Gọi Claude/DeepSeek với skill làm system prompt
    payload = json.dumps({
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 2000,
        "system": system_prompt,
        "messages": [{"role": "user", "content": user_input}]
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=payload,
        headers={"x-api-key": "[ANTHROPIC_KEY]",
                 "anthropic-version": "2023-06-01",
                 "Content-Type": "application/json"}
    )
    r = json.loads(urllib.request.urlopen(req).read())
    return r["content"][0]["text"]

# Dùng:
# result = call_with_skill("Phân tích thị trường AI tools VN 2026", prompt)
```

> Skills không cần cài gì — fetch về, nhúng làm system prompt, gọi LLM.

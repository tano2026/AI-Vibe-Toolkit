# Skill: Auto Research Trending — Tự Động Tìm Tools Hay Mỗi Tuần

> Skill này tao (Claude) dùng để tự research GitHub Trending, Reddit, Product Hunt — tìm ra top tools đáng làm content cho kênh.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Loại** | Research Skill — Claude tự chạy |
| **Tần suất** | Hàng tuần hoặc khi mày gọi |
| **Output** | Top 5 tools đáng làm content + lý do |
| **Trigger** | Mày nhắn: "tìm trending tuần này" hoặc "research mới đi" |

---

## 🔍 Nguồn tao check

| Nguồn | Tìm gì |
|-------|--------|
| GitHub Trending (weekly) | Repos nhiều stars nhất tuần |
| Reddit r/ClaudeAI | MCP, skills được cộng đồng khen |
| Reddit r/vibecoding | Tools vibe coders đang dùng |
| Reddit r/cursor | Cursor + AI tools trending |
| Product Hunt | AI tools mới ra |
| TikTok/YouTube trends | Content dạng nào đang viral |

---

## 📋 Prompt Tao Tự Dùng Khi Research

```
Search GitHub Trending tuần này (since=weekly) — 
lọc repos liên quan đến: AI tools, MCP servers, 
Claude skills, coding agents, data visualization, 
automation tools.

Với mỗi repo/tool tìm được, đánh giá theo:
1. Stars và growth rate
2. Phù hợp với vibe coders không chuyên không
3. Có thể setup trong < 30 phút không
4. Wow factor — nhìn vào có muốn xem thêm không
5. Chưa có trong kho AI Vibe Toolkit chưa

Output: Top 5 theo format bên dưới
```

---

## 📊 Format Output Chuẩn

```
## Top 5 Trending Tuần [XX/XX]

### 1. [Tên repo/tool]
- GitHub: [link]
- Stars: ⭐ [số]
- Tóm tắt: [1 câu]
- Tại sao hay cho kênh: [1-2 câu]
- Độ khó làm content: Dễ / Trung bình / Khó

### 2. ...
```

---

## ⚡ Cách Kích Hoạt

Mày chỉ cần nhắn 1 trong các câu này:

```
"tìm trending tuần này"
"research mới đi"  
"có gì hay không"
"update kho đi"
"GitHub trending tuần này có gì"
```

→ Tao tự search, tự filter, tự output top 5
→ Mày chọn cái nào → tao viết .md + script + push GitHub

---

## 🎯 Tiêu Chí Filter — Chỉ Lấy Vào Kho Khi

✅ Liên quan đến AI tools, MCP, coding agents, automation
✅ Phù hợp với vibe coders — không cần background kỹ thuật sâu
✅ Có thể demo được trong video ngắn
✅ Free hoặc có free tier đáng dùng
✅ Chưa có trong kho

❌ Loại bỏ nếu:
- Quá academic, không có ứng dụng thực tế ngay
- Setup phức tạp hơn 1 tiếng
- Chỉ dành cho senior engineers
- Đã có tool tương tự tốt hơn trong kho

---

*Thêm vào kho: 06/2025*

---

## 🤖 Hermes — Cách dùng skill này

**Use case:** tự động research trending AI tools

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
skill_prompt = fetch_skill("auto-research-trending.md")

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

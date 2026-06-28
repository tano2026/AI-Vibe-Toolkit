# viral-hooks — 100 Hook Formulas Cho TikTok/Reels/YouTube Shorts (54⭐)

**GitHub:** https://github.com/rediumvex/viral-hooks-skill
**Stars:** 54⭐ | **License:** MIT | **Dùng với:** Claude Code

---

## Cài Nhanh

```bash
# User-level (mọi session)
mkdir -p ~/.claude/skills
git clone https://github.com/rediumvex/viral-hooks-skill.git ~/.claude/skills/viral-hooks

# Project-level
mkdir -p .claude/skills
git clone https://github.com/rediumvex/viral-hooks-skill.git .claude/skills/viral-hooks
```

---

## Dùng Ngay

```bash
# Paste script hoặc topic
"Dùng viral-hooks skill, tạo 3 hook variants cho video về hermes agent"

# Theo trigger cụ thể
"Tạo hook kiểu CURIOSITY GAP cho video về taste-skill"
"Tạo hook kiểu CONTRARIAN cho video về AI agents"
"Tạo hook kiểu STORY cho video về vibe coding journey"
```

---

## 10 Psychology Triggers — 100 Formulas

### 1. CURIOSITY GAP
```
"[X] người đang dùng AI sai cách — đây là lý do"
"Tool này có [X]k stars nhưng 99% chưa biết tên"
"Tôi mất [X] tháng mới biết trick này tồn tại"
```

### 2. CONTRARIAN
```
"Đừng cài ChatGPT — đây là thứ tôi dùng thay"
"Claude Code không phải tool tốt nhất cho [X]"
"Mọi người đều sai về AI agents"
```

### 3. SOCIAL PROOF
```
"[X]k developer đang dùng cái này hàng ngày"
"Google engineer public tool cá nhân — [X]k star trong 1 tuần"
"Tool được [famous person] recommend"
```

### 4. BEFORE/AFTER
```
"[X] giờ làm việc → [Y] phút với tool này"
"Trước: viết từng dòng. Sau: AI viết hết"
"Từ 0 → [X]k stars trong [Y] tháng"
```

### 5. FEAR/URGENCY  
```
"Tool này sắp bị paywall — lấy free ngay"
"Nếu mày không biết cái này, đối thủ biết rồi"
"[X] ngày nữa close beta — đăng ký ngay"
```

### 6. STORY
```
"Tôi vừa mất 3 tiếng vì không biết trick này"
"Cách tôi build [X] trong [Y] giờ với AI"
"Story: từ khi tôi cài tool này, mọi thứ thay đổi"
```

### 7. LIST/NUMBER
```
"5 MCPs mày phải cài ngay cho Claude Code"
"3 skill biến AI thành senior developer"
"24 tools senior Google engineer dùng hàng ngày"
```

### 8. QUESTION
```
"AI của mày đang làm UI nhàm chán? Fix trong 2 phút"
"Mày đang dùng AI cho mọi thứ? Đây là sai lầm"
"Tại sao agent của mày không nhớ được gì?"
```

### 9. EXCLUSIVE
```
"Tool chưa ai làm video về ở Việt Nam"
"Repo 8 stars nhưng concept thay đổi ngành"
"Beta feature chưa public — preview ngay"
```

### 10. TRANSFORMATION
```
"Tool này biến 1 người thành cả team marketing"
"Từ vibe coder → ship product trong 1 tuần"
"AI agent của mày sẽ khác hoàn toàn sau video này"
```

---

## Workflow AI Vibe Toolkit

```bash
# Sau khi research xong 1 tool mới
"Dùng viral-hooks, tạo 5 hook variants cho [TOOL NAME]:
 - Angle: [concept độc đáo nhất của tool]
 - Audience: vibe coders, dev không chuyên
 - Platform: TikTok + YouTube Shorts
 - Mix: curiosity gap + before/after + social proof"

# Chọn hook tốt nhất → feed vào content-creator.md skill
```

---
*Nguồn: github.com/rediumvex/viral-hooks-skill | 54⭐ | MIT | tháng 6/2026*

---

## 🤖 Hermes — Cách dùng skill này

**Use case:** viết hook cho video khi content factory cần

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
skill_prompt = fetch_skill("viral-hooks-skill.md")

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

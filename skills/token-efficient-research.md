# Token-Efficient Research — Cheat Sheet Dùng Ngay

**Tổng hợp từ:** web-research MCP + deep-research ladder + agent-research-skills + Firecrawl + Brave Search + Exa
**Cập nhật:** tháng 6/2026

---

## 🎯 Nguyên Tắc Tối Ưu Token Khi Research

### Rule 1: Chọn Đúng Depth
```
Task đơn giản → Quick search (L0) → ~500 tokens
Task trung bình → Research (L1-L2) → 2-8k tokens
Task phức tạp → Deep/Expert (L3-L4) → 20-40k tokens

Đừng bao giờ dùng deep research cho task cần quick fact-check
```

### Rule 2: Pre-process Trước Khi Feed Claude
```
❌ Feed raw HTML → 50,000 tokens bị waste
❌ Feed full webpage → 90% là noise
✅ Summarize trước → Feed clean ~500 tokens
✅ Extract only relevant section → 10x efficient
```

### Rule 3: Parallel Search > Sequential
```
❌ Search A → wait → Search B → wait → Search C
✅ Search A + B + C song song → cùng latency, 3x throughput
```

### Rule 4: Cache Aggressively
```
Same query trong 7 ngày → dùng lại cache
Đừng re-search thứ đã biết
```

---

## 🛠️ TOOL STACK THEO USE CASE

### Use Case 1: Quick Fact-Check (< 1 phút, ~500 tokens)
```bash
# Option A: Brave Search MCP (đã có trong kho)
# → Search → lấy snippet → done

# Option B: web-research CLI
wr search "query ngắn gọn"

# Option C: Exa quick
# /research quick "fact cần check"
```

### Use Case 2: Research 1 Topic (5-10 phút, ~5k tokens)
```bash
# Recommended: web-research full pipeline
wr research "hermes agent 8 loops architecture"
# → auto decompose → parallel search → summarize → clean output

# Alternative: deep-research L1
/research "topic"

# Alternative: Brave Search + Firecrawl
# Search → get URLs → Firecrawl fetch → summarize
```

### Use Case 3: Deep Research / Report (20-40 phút, ~20k tokens)
```bash
# deep-research L3
/research expert "comprehensive topic"

# Alternative: Research Agent skill (trong kho)
# → Paste research-agent.md → run

# Stack tốt nhất:
# Tavily (structured) + Firecrawl (scrape) + Exa (neural)
```

### Use Case 4: Academic Literature Review
```bash
# agent-research-skills (lingzhi227)
/literature-search "topic"
/literature-review
/novelty-assessment
```

### Use Case 5: Real-time Trends / Social Signals
```bash
# X/Twitter: x-research-skill
# → mount vào Claude Code → search X

# Brave News search
# → MCP brave-search với news filter
```

---

## 📊 SO SÁNH TOKEN COST

| Method | Token/search | Latency | Quality |
|--------|-------------|---------|---------|
| Raw WebFetch | ~50,000 | Medium | Noisy |
| WebSearch snippets | ~5,000 | Fast | Partial |
| **web-research (wr)** | **~500** | Medium | Clean |
| Brave Search MCP | ~2,000 | Fast | Good |
| Firecrawl MCP | ~3,000 | Medium | Good |
| Exa neural | ~1,500 | Fast | Excellent |
| Tavily research | ~2,000 | Medium | Excellent |

---

## 🔌 MCP STACK TỐI THIỂU CHO RESEARCH

```json
// claude_desktop_config.json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": { "BRAVE_API_KEY": "..." }
    },
    "firecrawl": {
      "command": "npx", 
      "args": ["-y", "firecrawl-mcp"],
      "env": { "FIRECRAWL_API_KEY": "..." }
    },
    "web-research": {
      "command": "wr-mcp",
      "env": {
        "TINYFISH_API_KEY": "...",
        "GROQ_API_KEY": "..."
      }
    }
  }
}
```

**Priority order:**
1. `web-research` → token-optimized, pre-summarized
2. `brave-search` → fast, real-time
3. `firecrawl` → khi cần full content từ URL cụ thể

---

## 📋 RESEARCH PROMPT TEMPLATES

### Template 1: Quick Research (copy paste)
```
Research nhanh: [TOPIC]
- Tìm 3-5 sources đáng tin
- Summarize trong 200 words
- List key facts với sources
- Flag any conflicting info
```

### Template 2: Deep Research Report
```
Deep research: [TOPIC]

Yêu cầu:
1. Search ít nhất 10 sources
2. Cross-validate key claims
3. Structure: Overview → Details → Examples → Conclusion
4. Include: publication dates, credibility signals
5. Flag: gaps in knowledge, conflicting sources
6. Output: markdown report với citations

Token budget: ~10,000 tokens max
```

### Template 3: Competitive Research
```
Research đối thủ: [COMPANY/PRODUCT]

Cần tìm:
- Stars/downloads/usage metrics
- Key features vs [MY PRODUCT]
- Recent updates (last 30 days)
- Community sentiment
- Pricing model

Sources: GitHub, Product Hunt, HackerNews, Twitter/X
Output: Bảng so sánh + SWOT ngắn
```

### Template 4: Token-Efficient GitHub Research
```
Research GitHub repo: [REPO_URL]

Đọc theo thứ tự này (dừng khi đủ info):
1. README.md (summary + install)
2. package.json / pyproject.toml (dependencies)
3. /examples folder nếu có
4. Recent commits (last 10)
5. Issues với label "bug" hoặc "help wanted"

KHÔNG đọc toàn bộ source code.
Output: 300 words summary + install command + rating.
```

---

## 🔄 WORKFLOW RESEARCH CHO AI VIBE TOOLKIT

```
Mày quẳng link/ảnh
         ↓
Quick check: repo có trong kho chưa?
         ↓ (chưa có)
L0 Quick: fetch repo metadata (stars, desc, license)
         ↓
L1 Research: README → install → features
         ↓
Đánh giá: có đáng lưu vào kho không?
         ↓ (có)
Viết .md → viết script → push GitHub → update TRACKER
```

Token budget per entry: ~3,000-5,000 tokens (metadata + README relevant parts)

---

## 🧠 SKILL FILES ĐÃ CÓ TRONG KHO

| Skill | File | Dùng cho |
|-------|------|---------|
| Research Agent | `skills/research-agent.md` | General research với Brave+Firecrawl |
| Auto Research Trending | `skills/auto-research-trending.md` | GitHub trending auto-research |
| deep-research L0-L5 | (repo: deep-research-skills.md) | Research ladder |
| academic research | (repo: agent-research-skills-academic.md) | Literature review |

---

*AI Vibe Toolkit | Token-Efficient Research Guide | tháng 6/2026*

---

## 🤖 Hermes — Cách dùng skill này

**Use case:** optimize token khi research nhiều source

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
skill_prompt = fetch_skill("token-efficient-research.md")

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

# web-research — Token-Efficient Research MCP (99% Ít Token Hơn)

**GitHub:** https://github.com/mrvarmazyar/web-research
**Stars:** 8⭐ (mới, concept cực kỳ hay) | **License:** Go | **MIT**
**Tác giả:** mrvarmazyar | **Tạo:** 2026
**Tagline:** "99% fewer tokens than raw HTML"

---

## Vấn Đề Nó Giải Quyết

Khi Claude search web theo cách thông thường:
- `WebSearch` native → dump raw snippets vào context (đắt)
- `WebFetch` native → gửi toàn bộ HTML cho Claude (rất đắt)
- Kết quả: 90% token bị waste vào navbars, ads, cookie banners, scripts vô nghĩa

**web-research fix cái đó:**

```
AI Agent / MCP Client
        ↓
wr-mcp (MCP server)
        ↓
decompose → parallel search → parallel fetch (+Jina fallback) → summarize → cache
        ↓
Clean context với sources — 99% ít token hơn raw HTML
```

---

## Cách Hoạt Động

**Bước 1 — Decompose:** Auto expand query thành 2-3 sub-queries
**Bước 2 — Parallel search:** Tìm kiếm song song qua TinyFish API
**Bước 3 — Parallel fetch:** Lấy nội dung các URLs cùng lúc, Jina làm fallback
**Bước 4 — Summarize:** Groq (Llama 3.1 8B) hoặc Copilot CLI tóm tắt
**Bước 5 — Cache:** Lưu 7 ngày mặc định, tránh re-fetch

---

## Cài Đặt

```bash
# macOS Apple Silicon
curl -L https://github.com/mrvarmazyar/web-research/releases/latest/download/wr-darwin-arm64 -o ~/.local/bin/wr && chmod +x ~/.local/bin/wr
curl -L https://github.com/mrvarmazyar/web-research/releases/latest/download/wr-mcp-darwin-arm64 -o ~/.local/bin/wr-mcp && chmod +x ~/.local/bin/wr-mcp

# Linux amd64
curl -L https://github.com/mrvarmazyar/web-research/releases/latest/download/wr-linux-amd64 -o ~/.local/bin/wr && chmod +x ~/.local/bin/wr
curl -L https://github.com/mrvarmazyar/web-research/releases/latest/download/wr-mcp-linux-amd64 -o ~/.local/bin/wr-mcp && chmod +x ~/.local/bin/wr-mcp

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
```

## Config

```bash
export TINYFISH_API_KEY="..."   # https://agent.tinyfish.ai → Settings → API Keys
export GROQ_API_KEY="..."       # https://console.groq.com (free tier)
export WR_CACHE_DAYS=7          # cache TTL
```

## Dùng Như MCP Server

```json
// claude_desktop_config.json hoặc .cursor/mcp.json
{
  "mcpServers": {
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

## Commands

```bash
wr research "stripe webhook idempotency next.js"  # Full pipeline — recommended
wr search "query"                                  # Raw search results
wr fetch "https://url.com"                         # Clean content từ 1 URL
wr setup                                           # Verify setup
```

---

## Token Savings Thực Tế

| Method | Token dùng |
|--------|-----------|
| WebFetch raw HTML | ~50,000 tokens |
| WebSearch snippets | ~5,000 tokens |
| **web-research (wr)** | **~500 tokens** |

Giảm **99%** token — cùng một lượng thông tin hữu ích.

---

## Đánh Giá Cá Nhân

8 stars nhưng concept này là **game-changer cho token budget**. Nếu mày research nhiều trong 1 phiên Claude → chi phí token từ web research là vấn đề thật. Tool này giải quyết đúng vấn đề đó.

Stack: TinyFish (search) + Groq Llama 3.1 8B (summarize) = cheap + fast + clean.

**Rating: 8.5/10** — Concept xuất sắc, stars chưa reflect đúng giá trị.

---
*Nguồn: github.com/mrvarmazyar/web-research | tháng 6/2026*

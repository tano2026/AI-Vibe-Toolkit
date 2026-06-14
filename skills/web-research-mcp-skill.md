# web-research MCP — 99% Ít Token Hơn Raw HTML

**Repo:** github.com/mrvarmazyar/web-research | Go | MIT
**Stack:** TinyFish + Groq Llama 3.1 8B

---

## Setup

```bash
# Download binary
curl -L https://github.com/mrvarmazyar/web-research/releases/latest/download/wr-darwin-arm64 -o ~/.local/bin/wr
curl -L https://github.com/mrvarmazyar/web-research/releases/latest/download/wr-mcp-darwin-arm64 -o ~/.local/bin/wr-mcp
chmod +x ~/.local/bin/wr ~/.local/bin/wr-mcp

# Config
export TINYFISH_API_KEY="..."  # agent.tinyfish.ai
export GROQ_API_KEY="..."      # console.groq.com (free)
```

## MCP Config

```json
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
wr research "query"     # Full pipeline — decompose+search+fetch+summarize
wr search "query"       # Raw search results
wr fetch "https://url"  # Single URL → clean text
wr setup                # Verify config
```

## Token Comparison

```
Raw WebFetch:      ~50,000 tokens (HTML + CSS + JS + ads)
Brave Search MCP:  ~2,000 tokens (snippets)
wr research:       ~500 tokens (summarized, relevant only)
```

## Khi Nào Dùng wr vs Brave Search

```
Quick fact → Brave Search (nhanh hơn, 1 step)
Research topic → wr research (token hiệu quả hơn nhiều)
Read specific URL → wr fetch (cleaner than Firecrawl cho simple pages)
Deep crawl site → Firecrawl (mạnh hơn cho complex sites)
```

---
*skills/web-research-mcp-skill.md | AI Vibe Toolkit | tháng 6/2026*

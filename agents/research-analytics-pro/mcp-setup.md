# MCP Setup — Research Analytics Pro

Danh sách MCP cần bật, theo thứ tự ưu tiên. Tất cả đều có trong kho AI Vibe Toolkit.

---

## Tier 1 — Bắt buộc (agent không chạy được nếu thiếu)

### 1. Brave Search MCP
**Lý do:** Web search sạch, không bị tracking, kết quả tốt hơn DuckDuckGo cho agent tasks.
**File kho:** `mcps/brave-search.md`
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "YOUR_BRAVE_API_KEY"
      }
    }
  }
}
```
**Get API key:** https://api.search.brave.com → Free tier: 2000 queries/tháng

---

### 2. Firecrawl MCP
**Lý do:** Scrape web có cấu trúc, handle JavaScript-heavy pages, crawl cả site.
Không có cái này agent chỉ đọc được snippet Google, không đọc được nội dung thật.
**File kho:** `mcps/firecrawl.md`
```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_FIRECRAWL_API_KEY"
      }
    }
  }
}
```
**Get API key:** https://firecrawl.dev → Free tier: 500 scrapes/tháng

---

### 3. MarkItDown MCP
**Lý do:** Convert PDF/Excel/PPT/Word → Markdown để feed vào agent.
Cần thiết khi user upload báo cáo ngành, tài liệu nghiên cứu.
**File kho:** `mcps/markitdown-mcp.md`
```bash
pip install markitdown-mcp
```
```json
{
  "mcpServers": {
    "markitdown": {
      "command": "python",
      "args": ["-m", "markitdown_mcp"]
    }
  }
}
```

---

## Tier 2 — Strongly recommended (nâng cấp đáng kể)

### 4. x-research-skill (X/Twitter Research)
**Lý do:** Research pulse thị trường real-time, tìm practitioner opinions, track trending topics.
DeerFlow và TradingAgents đều dùng social media signal layer.
**File kho:** `skills/x-research-skill-skill.md`
```bash
mkdir -p .claude/skills
cd .claude/skills
git clone https://github.com/rohunvora/x-research-skill.git x-research
```
```bash
export X_BEARER_TOKEN="YOUR_X_BEARER_TOKEN"
```
**Get token:** https://developer.x.com → Free tier đủ dùng

---

### 5. Google Sheets MCP (hoặc filesystem MCP)
**Lý do:** Lưu data table, build tracker, chia sẻ kết quả research.
**File kho:** `mcps/filesystem.md` (local) hoặc bật Google Workspace integration
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/research-outputs"]
    }
  }
}
```

---

## Tier 3 — Power-ups (dùng khi cần deep analysis)

### 6. Mem0 (Long-term memory)
**Lý do:** Agent nhớ context research trước → không research lại từ đầu, build knowledge base dần.
**File kho:** `repos/mem0.md`
```bash
pip install mem0ai
export MEM0_API_KEY="YOUR_MEM0_KEY"  # hoặc self-host
```
Sau đó enable trong system-prompt (đã có sẵn).

---

### 7. Sequential Thinking MCP
**Lý do:** Bắt agent suy nghĩ từng bước trước khi research — tránh nhảy vào search lung tung.
Đặc biệt hiệu quả với L3-L4 research tasks.
**File kho:** `mcps/sequential-thinking.md`
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

---

## Config tổng hợp (copy vào claude_desktop_config.json hoặc .mcp.json)

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": { "BRAVE_API_KEY": "YOUR_KEY" }
    },
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": { "FIRECRAWL_API_KEY": "YOUR_KEY" }
    },
    "markitdown": {
      "command": "python",
      "args": ["-m", "markitdown_mcp"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "./research-outputs"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

# OPENCLAW-PLAYBOOK — Cách dùng kho AI Vibe Toolkit

> Mày là OpenClaw. Runtime: Node.js 22+. Gateway chính nhận lệnh từ chủ.
> Hermes chạy bên trong mày như một sub-agent Python.

---

## Năng lực của mày

✅ CÓ: Node.js, npm, npx, browser automation, filesystem, ClawHub 13k+ skills  
✅ CÓ: Kết nối Telegram/WhatsApp/Slack/Discord  
❌ KHÔNG PHẢI VIỆC CỦA MÀY: Python data processing, deploy lên VPS, pip install

---

## Phân luồng khi nhận task từ chủ

```
Nhận lệnh
    ↓
Phân loại task
    ├── Cần browser/UI → mày tự xử (Playwright skill)
    ├── Cần Python/data/API phức tạp → route sang Hermes
    ├── Cần deploy/install package → escalate Antigravity
    └── Cần research chuyên sâu → Hermes → Research Pro
```

---

## Cách cài tool từ kho vào mày

### Bước 1: Check ClawHub trước
```
/skill search firecrawl
/skill search brave-search
/skill search github
/skill search playwright
/skill search filesystem
```
Có trên ClawHub → `/skill install [tên]` là xong.

### Bước 2: Không có ClawHub → dùng npm MCP

Tất cả MCPs trong `/mcps/` kho đều chạy được qua npm:

```bash
# Scraping
npx -y firecrawl-mcp
npx -y @unclecode/crawl4ai-mcp

# Browser
npx -y @playwright/mcp

# Dev tools
npx -y @modelcontextprotocol/server-github
npx -y @modelcontextprotocol/server-filesystem

# AI/Media
npx -y @context7/mcp-server
npx -y sequential-thinking
```

Add vào OpenClaw MCP config section.

### Bước 3: Task cần Python → delegate Hermes

```
[TO HERMES]
Task: {mô tả rõ ràng}
Input: {data/URL/params cụ thể}
Expected output: {format kết quả cần trả về}
Deadline: {nếu có}
```

---

## Cách fetch kho (Node.js)

```javascript
const https = require("https");

async function fetchKho(path) {
  const token = process.env.GITHUB_TOKEN;
  return new Promise((resolve, reject) => {
    https.get({
      hostname: "api.github.com",
      path: `/repos/tano2026/AI-Vibe-Toolkit/contents/${path}`,
      headers: {
        "Authorization": `token ${token}`,
        "User-Agent": "openclaw-agent",
        "Accept": "application/vnd.github.v3+json"
      }
    }, res => {
      let data = "";
      res.on("data", chunk => data += chunk);
      res.on("end", () => {
        const parsed = JSON.parse(data);
        resolve(Buffer.from(parsed.content, "base64").toString("utf-8"));
      });
    }).on("error", reject);
  });
}

// Dùng
const tracker = await fetchKho("TRACKER.md");
const hermesPlaybook = await fetchKho("agents/HERMES-PLAYBOOK.md");
const skill = await fetchKho("skills/research-agent.md");
```

---

## Bảng phân công: OpenClaw vs Hermes vs Antigravity

| Task | OpenClaw | Hermes | Antigravity |
|------|----------|--------|-------------|
| Nhận/gửi Telegram | ✅ chính | - | - |
| Browse web, click | ✅ | ❌ | ❌ |
| Cài npm package | ✅ | ❌ | ✅ |
| Gọi REST API | ✅ | ✅ | - |
| Python xử lý data | ❌ | ✅ | - |
| Research + báo cáo | route → | ✅ | - |
| pip install | ❌ | ❌ | ✅ |
| Deploy VPS | ❌ | ❌ | ✅ |
| Docker | ❌ | ❌ | ✅ |
| Thêm entry vào kho | route → Claude | - | - |

---

## MCPs trong kho đã test — cài ngay được

| File kho | npm command |
|----------|-------------|
| mcps/firecrawl.md | npx -y firecrawl-mcp |
| mcps/playwright.md | npx -y @playwright/mcp |
| mcps/github-mcp.md | npx -y @modelcontextprotocol/server-github |
| mcps/filesystem.md | npx -y @modelcontextprotocol/server-filesystem |
| mcps/brave-search.md | npx -y @modelcontextprotocol/server-brave-search |
| mcps/context7.md | npx -y @context7/mcp-server |
| mcps/sequential-thinking.md | npx -y @modelcontextprotocol/server-sequential-thinking |
| mcps/crawl4ai.md | npx -y @unclecode/crawl4ai-mcp |
| mcps/markitdown-mcp.md | npx -y markitdown-mcp |

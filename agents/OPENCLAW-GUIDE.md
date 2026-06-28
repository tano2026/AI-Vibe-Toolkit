# OpenClaw — Hướng dẫn dùng kho AI Vibe Toolkit

> File này dành riêng cho OpenClaw runtime.

---

## Mày là ai trong hệ thống

- **Runtime:** Node.js 22.19+ / 24
- **Skills:** ClawHub marketplace (13,700+ skills)
- **Có:** filesystem, browser automation, npm ecosystem, subprocess
- **Kênh:** Telegram / WhatsApp / Slack / Discord
- **Hermes chạy bên trong mày** như agent chuyên Python

---

## Nguyên tắc đọc kho

| Loại file | Mày làm gì |
|-----------|-----------|
| /mcps/*.md | Xem phần "Setup" — nếu có `npx` command → mày cài được |
| /repos/*.md | Đọc TL;DR — nếu repo có ClawHub skill → install qua /skill install |
| /skills/*.md | Copy prompt → dùng trực tiếp |
| /stacks/*.md | Blueprint workflow để orchestrate |
| /agents/*.md | Pass cho Hermes nếu cần Python xử lý |

---

## Cài tool từ kho vào OpenClaw

### Bước 1 — Check ClawHub trước
```
/skill search firecrawl
/skill search brave-search
/skill search github
/skill search playwright
```
Nếu có → /skill install [tên] là xong.

### Bước 2 — Không có ClawHub skill → dùng npm MCP

Các MCP trong kho /mcps/ đều chạy được:
```bash
npx -y firecrawl-mcp
npx -y @playwright/mcp
npx -y @modelcontextprotocol/server-github
npx -y @modelcontextprotocol/server-filesystem
```

### Bước 3 — Task cần Python → route sang Hermes

```
[Internal message to Hermes]:
Task: [mô tả task]
Input: [data/URL/params]
Output cần: [format kết quả]
```

---

## Phân chia công việc

| Task | Ai làm |
|------|--------|
| Browse web, click UI | OpenClaw |
| Nhận/gửi Telegram | OpenClaw |
| Python data processing | Hermes |
| Gọi REST API | Cả hai |
| Deploy/install mới | Antigravity |
| Long-running background | Hermes (kanban queue) |
| Research + báo cáo | Hermes → Research Pro |

---

## Fetch kho (Node.js)

```javascript
const https = require("https");

function fetchKho(path, token) {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: "api.github.com",
      path: `/repos/tano2026/AI-Vibe-Toolkit/contents/${path}`,
      headers: { "Authorization": `token ${token}`, "User-Agent": "openclaw", "Accept": "application/vnd.github.v3+json" }
    };
    https.get(options, res => {
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
const tracker = await fetchKho("TRACKER.md", process.env.GITHUB_TOKEN);
const hermesGuide = await fetchKho("agents/HERMES-GUIDE.md", process.env.GITHUB_TOKEN);
```

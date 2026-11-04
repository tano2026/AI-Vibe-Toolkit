---
name: context7
description: >
  Cấp docs mới nhất của mọi thư viện cho AI khi code
---

# Context7 — Docs Thật, Không Hallucinate

> Claude/Cursor hay bịa API không tồn tại? Cài cái này vào — AI sẽ lấy docs thật từ internet thay vì "nhớ" lung tung.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Dùng để làm gì** | Cấp docs mới nhất của mọi thư viện cho AI khi code |
| **Độ khó setup** | ⭐⭐☆☆☆ Dễ |
| **Cần biết code không** | Không — chỉ cần chạy 1 lệnh |
| **Free hay trả phí** | Free (có API key free tốc độ cao hơn) |
| **GitHub** | [upstash/context7](https://github.com/upstash/context7) ⭐ 54,000+ |

---

## 🎯 Vấn đề nó giải quyết

Mày hỏi Claude *"làm thế nào dùng Next.js 15 server actions?"* — Claude trả lời dựa trên kiến thức cũ từ lúc được train, API có thể đã đổi rồi.

**Context7 fix cái này:** Thay vì dùng "ký ức", AI lấy docs thật từ nguồn gốc → code đúng version → không bị lỗi vớ vẩn.

---

## ⚡ Setup trong 3 bước

```bash
# Bước 1: Cài Node.js nếu chưa có (nodejs.org)

# Bước 2: Thêm vào Claude Desktop config
# Mở file: ~/Library/Application Support/Claude/claude_desktop_config.json (Mac)
# Hoặc: %APPDATA%\Claude\claude_desktop_config.json (Windows)

{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}

# Bước 3: Restart Claude Desktop → Done
```

---

## 🖥️ Cài cho Claude Code (cập nhật 04/11/2026)

Phần "Setup trong 3 bước" ở trên chỉ dành cho Claude Desktop. Với Claude Code (theo README gốc `upstash/context7`, đã đối chiếu một phần):

```bash
# Cách README khuyên: đăng nhập OAuth, tạo khoá API, cài skill (cần Node 22.13+)
npx ctx7 setup --claude

# Hoặc nối MCP từ xa (URL và header lấy từ README, cú pháp lệnh đã kiểm bằng `claude mcp add --help`)
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "Authorization: Bearer YOUR_API_KEY"

# Hoặc chạy cục bộ qua npx
claude mcp add context7 -- npx -y @upstash/context7-mcp
```

- Đã kiểm: gói `@upstash/context7-mcp` (4.5.0, MIT) và `ctx7` (0.9.0, MIT) có trên npm, `ctx7 --help` liệt kê lệnh `login`, `setup`, `library`, `docs`, `search`.
- Chưa chạy: `ctx7 setup` (cần đăng nhập), các lệnh `claude mcp add` với Context7 thật.
- Khoá API khuyến nghị, không bắt buộc. Khoá miễn phí có giới hạn tần suất cao hơn bản không khoá, README không ghi con số.
- Công cụ MCP: `resolve-library-id` và `query-docs`. Gọi bằng "use context7" hoặc chỉ thẳng thư viện kiểu `/org/project`. Muốn tự kích hoạt thì thêm một quy tắc vào `CLAUDE.md`.
- Repo chỉ chứa mã MCP server (khoảng 64 nghìn sao, MIT). Phần backend, bộ phân tích và bộ cào docs là mã đóng.
- Docs trong Context7 do cộng đồng đóng góp, hãng nói không đảm bảo chính xác hay an toàn. Gặp nội dung đáng ngờ thì báo bằng nút Report.
- Gỡ: `npx ctx7 remove`.

---

## 💡 Dùng thế nào

Chỉ cần thêm **"use context7"** vào cuối prompt:

```
❌ Trước: "Viết middleware Next.js check JWT"
✅ Sau:   "Viết middleware Next.js check JWT. use context7"
```

Claude sẽ tự động lấy docs Next.js version mới nhất trước khi trả lời.

---

## ⚠️ Lưu ý

- Cần Node.js 18 trở lên
- Lần đầu chạy hơi chậm (đang download)
- Nên lấy API key free tại context7.com/dashboard để không bị rate limit

---

## 🔗 Hay kết hợp với

- **Sequential Thinking** — Context7 lo docs, Sequential Thinking lo logic
- **GitHub MCP** — docs + code version control = combo hoàn hảo

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Dễ setup | ⭐⭐⭐⭐☆ |
| Thực sự hữu ích | ⭐⭐⭐⭐⭐ |
| Tiết kiệm thời gian | ⭐⭐⭐⭐⭐ |

**Tóm lại:** MCP #1 phải cài nếu mày dùng AI để code. 54k stars không phải ngẫu nhiên.

---

*Thêm vào kho: 06/2025 | Nguồn: github.com/upstash/context7*


---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

def context7_get_docs(library_id, topic=""):
    url = f"https://context7.com/api/v1/{library_id}"
    if topic:
        url += f"?topic={topic}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    return urllib.request.urlopen(req).read().decode()
```

### OpenClaw
```bash
npx -y @upstash/context7-mcp
```

### Antigravity
```bash
# Free tier khong can key, rate limit thap hon ban co key
echo 'CONTEXT7_API_KEY=your_key_here' >> /home/ubuntu/.hermes/.env  # optional, tang rate limit
```
> ⚠️ Chủ yếu để lấy docs thư viện code mới nhất — hữu ích khi Hermes viết code dùng library có version mới sau training cutoff.

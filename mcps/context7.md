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

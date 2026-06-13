# Brave Search MCP — Cho Claude Tự Search Google

> Thay vì mày search Google rồi copy paste vào Claude — cài cái này là Claude tự search và trả lời luôn.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Dùng để làm gì** | Claude tự search web real-time để trả lời câu hỏi mới nhất |
| **Độ khó setup** | ⭐⭐☆☆☆ Dễ |
| **Cần biết code không** | Không |
| **Free hay trả phí** | Free 2,000 searches/tháng |
| **GitHub** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — official |

---

## 🎯 Vấn đề nó giải quyết

Claude bị giới hạn knowledge cutoff — không biết chuyện xảy ra gần đây.

**Brave Search fix cái này:** Claude tự search Brave (search engine riêng, không phải Google) → lấy thông tin mới nhất → trả lời chính xác hơn.

**Use cases thực tế:**
- Hỏi về tin tức, giá cả, sự kiện mới nhất
- Research thị trường real-time
- Tìm tool/repo mới ra gần đây
- Fact-check thông tin

---

## ⚡ Setup trong 3 bước

```bash
# Bước 1: Lấy API key free
# Vào: api.search.brave.com → Sign up → Free plan → Copy API key

# Bước 2: Thêm vào claude_desktop_config.json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "PASTE_API_KEY_VÀO_ĐÂY"
      }
    }
  }
}

# Bước 3: Restart Claude Desktop → Done
```

---

## 💡 Dùng thế nào

```
Prompt ví dụ:

"Search xem MCP server nào đang trending nhất tuần này"

"Tìm giá iPhone 15 Pro Max ở Việt Nam hiện tại"

"Search top 5 AI tools mới ra tháng này"

→ Claude tự search → tổng hợp → trả kết quả
```

---

## ⚠️ Lưu ý

- Free tier: 2,000 searches/tháng — đủ dùng cho cá nhân
- Kết quả từ Brave index, không phải Google — đôi khi thiếu kết quả local VN
- Nên kết hợp với Firecrawl để đọc nội dung trang sau khi search

---

## 🔗 Hay kết hợp với

- **Firecrawl** — Search tìm ra link → Firecrawl cào nội dung chi tiết
- **Sequential Thinking** — Search → thu thập data → phân tích có hệ thống

**Combo killer cho research:**
```
Brave Search tìm links → Firecrawl cào nội dung → Claude tổng hợp báo cáo
```

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Dễ setup | ⭐⭐⭐⭐☆ |
| Thực sự hữu ích | ⭐⭐⭐⭐☆ |
| Free tier đủ dùng | ⭐⭐⭐⭐⭐ |

**Tóm lại:** MCP đơn giản nhất để cho Claude "nhìn thấy" internet. Phải có trong bộ toolkit của mọi vibe coder.

---

*Thêm vào kho: 06/2025 | Nguồn: modelcontextprotocol/servers (official Anthropic)*

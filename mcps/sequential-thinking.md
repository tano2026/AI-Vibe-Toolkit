# Sequential Thinking — Bắt AI Suy Nghĩ Trước Khi Làm

> AI hay nhảy vào code luôn rồi sai? MCP này bắt nó lên kế hoạch từng bước trước — như senior dev ngồi nghĩ trước khi gõ.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Dùng để làm gì** | Bắt AI chia nhỏ bài toán, suy nghĩ có cấu trúc trước khi làm |
| **Độ khó setup** | ⭐⭐☆☆☆ Dễ |
| **Cần biết code không** | Không |
| **Free hay trả phí** | Free hoàn toàn |
| **GitHub** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — official |

---

## 🎯 Vấn đề nó giải quyết

Mày bảo Claude *"refactor toàn bộ auth flow"* — nó nhảy vào làm luôn, xong sai đủ chỗ, mày debug cả buổi.

**Sequential Thinking fix cái này:** AI sẽ tự chia task thành các bước nhỏ, suy nghĩ từng bước, phát hiện edge cases TRƯỚC khi code → ít bug hơn, ít phải làm lại hơn.

---

## ⚡ Setup trong 3 bước

```bash
# Thêm vào claude_desktop_config.json:

{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequentialthinking"]
    }
  }
}

# Restart Claude Desktop → Done
```

---

## 💡 Dùng thế nào

Thêm **"use sequential thinking"** vào prompt phức tạp:

```
❌ Trước: "Thêm feature login với Google OAuth vào app"

✅ Sau: "Thêm feature login với Google OAuth vào app. 
         Dùng sequential thinking để lên kế hoạch trước."
```

Claude sẽ output ra:
- Bước 1: Phân tích hiện trạng
- Bước 2: Xác định những gì cần thay đổi
- Bước 3: Thứ tự implement
- Bước 4: Các edge cases cần handle
- → Sau đó mới code

---

## ⚠️ Lưu ý

- **Không cần dùng cho task đơn giản** — nó sẽ chậm hơn không có lý do
- Best dùng cho: refactor lớn, feature phức tạp, debug khó tìm nguyên nhân
- Tốn nhiều token hơn bình thường

---

## 🔗 Hay kết hợp với

- **Context7** — Sequential Thinking lên kế hoạch + Context7 lấy docs đúng → combo killer
- **GitHub MCP** — plan xong → commit từng bước rõ ràng

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Dễ setup | ⭐⭐⭐⭐⭐ |
| Thực sự hữu ích | ⭐⭐⭐⭐☆ |
| Dùng hàng ngày | ⭐⭐⭐☆☆ (chỉ khi task phức tạp) |

**Tóm lại:** Không cần cài ngay, nhưng khi gặp bug khó hoặc task lớn — bật lên ngay.

---

*Thêm vào kho: 06/2025 | Nguồn: modelcontextprotocol/servers (official Anthropic)*

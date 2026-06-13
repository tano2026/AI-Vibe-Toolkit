# Filesystem MCP — Claude Đọc Và Ghi File Trên Máy Mày

> Cho Claude quyền đọc/ghi file trên máy tính — nó có thể xử lý docs, CSV, code files mà không cần mày copy paste.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Dùng để làm gì** | Claude đọc, viết, tìm kiếm files trên máy tính của mày |
| **Độ khó setup** | ⭐⭐☆☆☆ Dễ |
| **Cần biết code không** | Không |
| **Free hay trả phí** | Free hoàn toàn |
| **GitHub** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — official Anthropic |

---

## 🎯 Vấn đề nó giải quyết

Mày có file CSV 500 dòng, muốn Claude phân tích → phải copy hết vào chat. File code dài → cũng vậy. Bất tiện.

**Filesystem MCP fix cái này:** Claude tự đọc file từ máy mày, xử lý, viết kết quả ra file mới — mày chỉ nói "đọc file này và làm X".

---

## ⚡ Setup trong 3 bước

```bash
# Thêm vào claude_desktop_config.json:
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:/Users/TÊN_MÀY/Documents"
      ]
    }
  }
}

# Thay đường dẫn thành folder mày muốn Claude được phép vào
# Restart Claude Desktop → Done
```

---

## 💡 Dùng thế nào

```
"Đọc file data.csv trong Documents
 Phân tích doanh thu theo tháng
 Vẽ nhận xét xu hướng"

"Đọc tất cả file .js trong folder src
 Tìm chỗ nào có thể gây memory leak"

"Tạo file report.md trong Desktop
 Tóm tắt cuộc họp hôm nay [mày paste nội dung]"
```

---

## ⚠️ Lưu ý

- **Chỉ cho Claude vào folder cụ thể** — không nên cho vào toàn bộ ổ C
- Claude có thể GHI file — cẩn thận với file quan trọng
- Nên tạo 1 folder riêng cho AI làm việc

---

## 🔗 Hay kết hợp với

- **GitHub MCP** — đọc code từ máy → commit lên GitHub
- **Firecrawl** — cào web → lưu kết quả ra file local

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Dễ setup | ⭐⭐⭐⭐☆ |
| Thực sự hữu ích | ⭐⭐⭐⭐⭐ |
| Dùng hàng ngày | ⭐⭐⭐⭐⭐ |

**Tóm lại:** MCP "bread and butter" — developers gọi nó là must-have số 1. Xử lý file không cần copy paste nữa.

---

*Thêm vào kho: 06/2025 | Nguồn: modelcontextprotocol/servers (official)*

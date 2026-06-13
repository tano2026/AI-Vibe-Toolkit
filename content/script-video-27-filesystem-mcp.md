# Script Video #27 — Filesystem MCP: Claude Đọc File Máy Tính Không Cần Copy Paste

**Format:** TikTok / YouTube Shorts (~65s)
**Hook type:** Pain point đơn giản nhất — "copy paste mệt mỏi"
**Style:** Không lộ mặt, demo đơn giản, dễ hiểu nhất trong series

---

## 🎬 SCRIPT

**[0s - 6s] HOOK**
> "File CSV 500 dòng muốn Claude phân tích — mày phải copy hết vào chat. File code dài 1000 dòng — cũng vậy. Có cách cho Claude tự đọc file trực tiếp."

**[6s - 18s] FILESYSTEM MCP**
> "Filesystem MCP — official từ Anthropic, free. Cho Claude quyền đọc và ghi file trực tiếp trên máy mày trong thư mục mày cho phép."

> "Mày kiểm soát hoàn toàn — chỉ định đúng folder nào Claude được phép access."

**[18s - 45s] DEMO 3 VIỆC THỰC TẾ**
> "Việc 1 — Phân tích data:"
> "'Đọc file sales_q2.csv trong Desktop, tìm top 10 sản phẩm bán chạy nhất'"
> "Claude đọc thẳng, phân tích, trả kết quả — không copy paste gì hết."

> "Việc 2 — Xử lý nhiều file cùng lúc:"
> "'Đọc tất cả file .md trong thư mục notes, tóm tắt thành 1 file summary'"
> "10 files → 1 summary → Claude tự ghi ra file mới."

> "Việc 3 — Code review nhanh:"
> "'Đọc toàn bộ thư mục src, tìm chỗ nào có thể gây memory leak'"
> "Không cần paste từng file."

**[45s - 57s] CÀI**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y", "@modelcontextprotocol/server-filesystem",
        "/Users/mày/Desktop",
        "/Users/mày/Documents/projects"
      ]
    }
  }
}
```
> "Chỉ định folder mày muốn cho phép — Claude chỉ access đúng chỗ đó."

**[57s - 65s] CTA**
> "MCP đơn giản nhất trong list nhưng tiết kiệm thời gian nhiều nhất cho task hàng ngày. Cài 2 phút."

---

## 📝 CAPTION
```
Copy paste file vào Claude mãi rồi à? Cho nó tự đọc luôn đi 📁

Filesystem MCP — Claude đọc/ghi file trực tiếp trên máy, mày kiểm soát folder nào được phép

Free · Official Anthropic · Cài 2 phút

#claudeai #mcp #vibecoding #productivity #ai #filesystem #nocopypaste
```

## 🎯 B-ROLL
1. Copy paste file dài vào Claude → mệt mỏi
2. Contrast: gõ 1 câu lệnh → Claude tự đọc file
3. Multiple files → summary file mới xuất hiện
4. Config JSON — highlight phần folder path

---
*Script v1 — tháng 6/2026*

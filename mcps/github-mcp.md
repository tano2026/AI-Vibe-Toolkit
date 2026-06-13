# GitHub MCP — Claude Quản Lý Code Repo Cho Mày

> Tạo branch, commit, tạo PR, đọc issues — Claude làm hết, mày không cần mở GitHub.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Dùng để làm gì** | Claude thao tác GitHub: commit, PR, issues, branches |
| **Độ khó setup** | ⭐⭐☆☆☆ Dễ |
| **Cần biết code không** | Biết tí (hiểu Git cơ bản) |
| **Free hay trả phí** | Free hoàn toàn |
| **GitHub** | [github/github-mcp-server](https://github.com/github/github-mcp-server) — official by GitHub |

---

## 🎯 Vấn đề nó giải quyết

Vibe coding xong → phải tự tạo commit message, tạo PR, viết description... Tốn thời gian và nhàm.

**GitHub MCP fix cái này:** Claude tự tạo commit message có nghĩa, tạo PR với description đầy đủ, đọc issues và suggest fix — tất cả không cần mày rời khỏi chat.

---

## ⚡ Setup trong 3 bước

```bash
# Bước 1: Lấy GitHub Personal Access Token
# GitHub → Settings → Developer Settings → Personal Access Tokens
# → Generate new token → tick: repo, issues, pull_requests

# Bước 2: Thêm vào claude_desktop_config.json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "PASTE_TOKEN_VÀO_ĐÂY"
      }
    }
  }
}

# Bước 3: Restart Claude Desktop → Done
```

---

## 💡 Dùng thế nào

```
"Tạo PR cho branch feature/login-page
 Description tự động dựa trên các commits"

"Đọc tất cả issues đang open của repo này
 Cái nào urgent nhất?"

"Tạo issue mới: bug login không hoạt động trên Safari"

"Commit tất cả file đã thay đổi
 Message phù hợp với conventional commits"
```

---

## ⚠️ Lưu ý

- Token cần được bảo mật — đừng share cho ai
- Chỉ access được repo mà token có quyền

---

## 🔗 Hay kết hợp với

- **Context7** — code đúng docs + commit sạch = workflow hoàn hảo
- **Sequential Thinking** — plan feature → implement → commit từng bước

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Dễ setup | ⭐⭐⭐⭐☆ |
| Thực sự hữu ích | ⭐⭐⭐⭐⭐ |
| Tiết kiệm thời gian | ⭐⭐⭐⭐⭐ |

**Tóm lại:** Nếu mày code bằng AI thì cái này là must-have. Claude viết code + tự commit + tự tạo PR = mày chỉ ngồi review.

---

*Thêm vào kho: 06/2025 | Nguồn: github.com/github/github-mcp-server*

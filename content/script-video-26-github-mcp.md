# Script Video #26 — GitHub MCP: Claude Tự Commit, Tạo PR, Đọc Issues

**Format:** TikTok / YouTube Shorts (~70s)
**Hook type:** "Việc nhàm nhất trong vibe coding"
**Style:** Không lộ mặt, screen record Claude Code + GitHub

---

## 🎬 SCRIPT

**[0s - 7s] HOOK**
> "Vibe coding xong một feature — giờ phải tự viết commit message, tạo PR, điền description... Phần nhàm nhất của workflow. GitHub MCP xử lý hết."

*[Show: GitHub PR creation page — nhàm chán]*

**[7s - 20s] GITHUB MCP LÀ GÌ**
> "GitHub MCP — official từ GitHub, free. Cho Claude quyền thao tác thẳng vào repo của mày: đọc code, tạo commit, tạo PR, đọc và comment issues."

> "Không cần mở GitHub. Không cần nhớ Git commands. Không cần copy paste."

**[20s - 48s] DEMO WORKFLOW THỰC TẾ**
> "Mày vừa code xong, nói với Claude:"

*[Show chat với Claude Code]*

> "'Tạo commit cho những thay đổi vừa rồi với message phù hợp, push lên branch mới, tạo PR vào main'"

*[Show: git commit → push → PR tạo tự động trên GitHub]*

> "Claude tự đặt tên branch theo convention, tự viết commit message mô tả đúng những gì mày làm, tự tạo PR description có checklist."

> "Đọc issues cũng được:"
> "'Đọc issues đang open, cái nào mày có thể fix dựa trên codebase hiện tại?'"

**[48s - 62s] CÀI**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "token_của_mày"
      }
    }
  }
}
```

**[62s - 70s] CTA**
> "Tạo GitHub token trong Settings → Developer Settings → 5 phút setup. Tiết kiệm được thời gian nhàm nhất của mỗi coding session."

---

## 📝 CAPTION
```
Phần nhàm nhất của vibe coding — Claude tự làm hết rồi 🤖

GitHub MCP: tự commit, tạo PR, đọc issues, comment — không cần mở GitHub

Free · Official GitHub · Cần GitHub token

#github #vibecoding #claudeai #mcp #git #developer #coding
```

## 🎯 B-ROLL
1. GitHub UI → contrast với Claude chat đơn giản
2. PR tự tạo trên GitHub — show kết quả
3. Commit message được generate — đọc lên nghe
4. Config JSON với token

---
*Script v1 — tháng 6/2026*

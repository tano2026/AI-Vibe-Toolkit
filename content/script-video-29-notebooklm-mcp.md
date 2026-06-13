# Script Video #29 — NotebookLM MCP: Claude Hỏi NotebookLM Thay Vì Bịa

**Format:** TikTok / YouTube Shorts (~80s)
**Hook type:** Pain point — "AI bịa thông tin từ tài liệu của mày"
**Style:** Không lộ mặt, demo Claude query NotebookLM real-time
**Cover:** Giới thiệu ecosystem + focus PleasePrompto (dễ nhất)

---

## 🎬 SCRIPT

**[0s - 8s] HOOK**
> "Mày upload tài liệu vào Claude, hỏi câu hỏi — nó trả lời tự tin nhưng không có trong doc. Hallucinate. Có cách để Claude không bao giờ bịa từ tài liệu của mày nữa."

*[Show: Claude trả lời → highlight câu không có trong doc → user frustrated]*

**[8s - 22s] GIẢI PHÁP**
> "NotebookLM của Google — upload tài liệu vào đây, nó chỉ trả lời dựa trên sources đó. Có citation đến đúng đoạn văn. Không bịa được."

> "NotebookLM MCP nối Claude Code với NotebookLM. Mày hỏi Claude — Claude hỏi NotebookLM — NotebookLM trả lời có citation."

*[Show: flow diagram đơn giản]*

**[22s - 50s] DEMO**
> "Setup:"

```bash
npx notebooklm-mcp@latest auth
```

```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "npx",
      "args": ["-y", "notebooklm-mcp@latest"]
    }
  }
}
```

*[Show: Claude Code với MCP hoạt động]*

> "Tao upload toàn bộ docs của React 19 vào NotebookLM. Hỏi Claude:"
> "'Trong React 19, useOptimistic hoạt động thế nào với concurrent features?'"

*[Show: Claude gọi query_notebook → NotebookLM trả về answer + citation cụ thể]*

> "Answer có citation chỉ đến đúng đoạn trong doc. Không bịa được vì nó không có quyền thêm thông tin ngoài source."

**[50s - 65s] 5 REPOS TRONG ECOSYSTEM**
> "Có 5 repos NotebookLM MCP khác nhau:"

*[Show: bảng so sánh nhanh]*

> "Đơn giản nhất: PleasePrompto — 2.7k stars, 1 lệnh npx"
> "Cần automation n8n/Make: roomi-fields — có HTTP REST API, Docker"
> "VS Code và lười maintain: moodRobotics — auto-update"
> "Python user: julianoczkowski — pip install"
> "Enterprise security: Pantheon Security — 17 hardening layers"

**[65s - 80s] CTA**
> "Lưu ý: tất cả đều dùng browser automation — Google chưa mở API chính thức. Có thể gãy khi Google update UI nhưng maintainers fix nhanh trong 24-72h."

> "Link 5 repos trong bio. Bắt đầu với PleasePrompto — đơn giản nhất."

---

## 📝 CAPTION
```
Claude bịa thông tin từ tài liệu của mày? Fix bằng NotebookLM MCP 🔗

Claude hỏi NotebookLM → answer có citation → không hallucinate được

5 repos khác nhau cho 5 use case:
↳ PleasePrompto (2.7k⭐) — đơn giản nhất
↳ roomi-fields — n8n/Docker/REST API  
↳ moodRobotics — auto-update VS Code
↳ julianoczkowski — Python
↳ Pantheon Security — enterprise

#notebooklm #mcp #claudeai #vibecoding #ai #googleai #rag
```

## 🎯 B-ROLL
1. Claude hallucinate → so sánh với Claude + NotebookLM có citation
2. Flow diagram: Claude → NotebookLM → citation answer
3. Terminal: `npx notebooklm-mcp@latest auth`
4. Demo real-time: query → citation response xuất hiện
5. Bảng 5 repos nhanh cuối video

---
*Script v1 — tháng 6/2026*

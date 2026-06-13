# Script Video #24 — Sequential Thinking MCP: Bắt AI Nghĩ Trước Khi Làm

**Format:** TikTok / YouTube Shorts (~70s)
**Hook type:** Pain point — "AI nhảy vào làm luôn rồi sai"
**Style:** Không lộ mặt, screen record Claude Code

---

## 🎬 SCRIPT

**[0s - 7s] HOOK**
> "Mày bảo Claude refactor toàn bộ auth flow — nó nhảy vào làm luôn, xong sai đủ chỗ, mày debug cả buổi. Có MCP fix đúng vấn đề này."

*[Show: Claude đang code ào ào → error đỏ xuất hiện]*

**[7s - 22s] VẤN ĐỀ**
> "AI không suy nghĩ — nó predict. Hỏi câu phức tạp là nó generate thẳng, không kiểm tra logic trước. Như junior dev nhảy vào code mà không hiểu requirement."

**[22s - 48s] SEQUENTIAL THINKING — DEMO**
> "Sequential Thinking MCP — official từ Anthropic, free hoàn toàn. Cài vào, Claude Code sẽ tự chia bài toán thành từng bước nhỏ trước khi làm."

*[Show: Claude Code với MCP bật]*

> "Cùng câu hỏi — refactor auth flow. Lần này Claude tự nói:"
> "'Bước 1: Map toàn bộ auth flow hiện tại'"
> "'Bước 2: Identify dependencies'"  
> "'Bước 3: Tìm edge cases'"
> "'Bước 4: Viết migration plan'"
> "'Bước 5: Bắt đầu code từng phần'"

*[Show từng thought step xuất hiện trên màn hình]*

> "Phát hiện edge case trước khi code — không phải sau khi debug 3 tiếng."

**[48s - 62s] CÀI**
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```
> "Paste vào claude_desktop_config.json. Restart. Xong."

**[62s - 70s] CTA**
> "Free, official từ Anthropic, cài 30 giây. Đây là MCP đầu tiên tao cài khi setup Claude Code mới."

---

## 📝 CAPTION
```
AI nhảy vào code ngay rồi sai? MCP này bắt nó nghĩ trước 🧠

Sequential Thinking — Claude tự chia bài toán thành steps, tìm edge cases TRƯỚC khi code

Free · Official Anthropic · Cài 30 giây

#claudeai #mcp #vibecoding #claudecode #ai #coding #developer
```

## 🎯 B-ROLL
1. Claude code không có MCP → error ngay
2. Claude code CÓ MCP → thought steps xuất hiện từng cái một (satisfying)
3. Config JSON paste vào file — đơn giản
4. Before/after: debug time

---
*Script v1 — tháng 6/2026*

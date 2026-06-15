# Script Video #48 — headroom: Giảm 95% Token, Câu Trả Lời Như Nhau

**Repo:** https://github.com/chopratejas/headroom | 27.5k⭐
**Hook:** "AI agent của mày đang đốt tiền vào 95% rác — fix trong 1 lệnh"

## 🎬 SCRIPT

**[HOOK 0:00-0:08]**
Tool output 50,000 tokens.
AI của mày đọc hết → tốn tiền.
Nhưng 95% là rác: timestamps, whitespace, repeated info.
Fix trong 1 lệnh.

**[SOLUTION 0:08-0:25]**
headroom. 27.5k stars. #2 trending tuần này.
"Context compression layer cho AI agents."

```python
from headroom import compress
compressed = compress(big_output, max_tokens=2000)
# 50,000 → 2,000 tokens. Câu trả lời như nhau.
```

**[3 MODES 0:25-0:50]**
Library: compress trong code.
Proxy: drop-in thay API endpoint, tự động compress mọi request.
MCP Server: dùng trong Claude Code.

**[CTA 0:50-1:00]**
MIT free. pip install headroom.
Link bio.

*Script #48 | AI Vibe Toolkit*

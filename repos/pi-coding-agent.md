---
name: pi-coding-agent
description: >
  Stars: 71k+ Tác giả: Mario Zechner (badlogic) Domain: Terminal coding agent tối giản, thay thế Claude Code
---

# pi-coding-agent — coding agent tối giản, tự mở rộng bằng chính nó

**GitHub:** https://github.com/earendil-works/pi (monorepo: https://github.com/badlogic/pi-mono)
**Tác giả:** Mario Zechner (tác giả libGDX, 25k⭐, 17 năm kinh nghiệm open source)
**Cài:** `npm install -g @mariozechner/pi-coding-agent`

---

## TL;DR

Coding agent chạy terminal, chỉ có 4 tool lõi (Read, Write, Edit, Bash) và system prompt dưới 1000 token — ngược hẳn xu hướng nhồi nhét tính năng. Bù lại tự mở rộng bằng TypeScript extension, skill, prompt template do chính agent viết ra khi cần.

## Tool này dùng để làm gì

Mario Zechner làm ra Pi vì chán Claude Code (giật lag terminal), chán OpenCode (phá cache prompt), chán agent 200 tính năng mà chỉ dùng 5. Pi cố tình KHÔNG có: MCP tích hợp sẵn, sub-agent, plan mode, to-do list, popup xin quyền, bash chạy nền. Triết lý: "There are many coding agents, but this one is yours" — build lõi tối giản rồi để user tự mở rộng đúng nhu cầu, không áp workflow có sẵn.

Hỗ trợ 15+ nhà cung cấp LLM (Anthropic, OpenAI, Google, Groq, xAI, Mistral, Ollama...), đăng nhập được bằng Claude Pro/Max hoặc ChatGPT Plus/Pro qua `/login` thay vì bắt buộc API key.

## Setup từng bước

1. Cài global:
```bash
npm install -g @mariozechner/pi-coding-agent
```
2. Set API key hoặc đăng nhập bằng subscription có sẵn:
```bash
export ANTHROPIC_API_KEY="sk-..."
# hoặc
pi /login   # dùng Claude Pro/Max, ChatGPT Plus/Pro, GitHub Copilot subscription
```
3. Chạy `pi` trong thư mục project, agent tự đọc code và làm việc như Claude Code

## Ví dụ thực tế

Chạy `pi` trong repo Node.js, gõ "sửa lỗi TypeError ở dòng 42 file server.js" — agent đọc file, sửa trực tiếp, chạy test kiểm tra bằng Bash tool, không hỏi xin quyền từng bước (mặc định YOLO mode).

## Lưu ý / Lỗi thường gặp

- Không có MCP built-in — nếu quen dùng MCP server trong Claude Code, phải tự viết extension để tích hợp tương đương
- Mặc định "YOLO" (tự chạy lệnh không hỏi xin phép) — cẩn thận khi chạy trên repo/máy quan trọng, không có permission popup như Claude Code
- Cộng đồng còn nhỏ hơn Claude Code/Cursor dù tăng trưởng rất nhanh (71k⭐ trong ~10 tháng) — ít tài liệu tiếng Việt, ít case study production dài hạn

## Đánh giá cá nhân

- **Điểm mạnh:** nhẹ, nhanh, không giật lag terminal như phàn nàn về Claude Code; triết lý tối giản dễ tuỳ biến đúng ý; hỗ trợ nhiều LLM provider hơn hẳn Claude Code (dùng được Claude Pro/Max sẵn có, không cần trả thêm API riêng)
- **Điểm yếu:** thiếu MCP/sub-agent sẵn có nghĩa là phải tự code nhiều hơn để đạt độ tiện dụng tương đương; mặc định YOLO rủi ro nếu không cẩn thận
- **Có nên dùng không:** 7.5/10 — hợp cho dev muốn agent nhẹ, tự chủ cấu hình; không hợp nếu muốn plug-and-play với MCP ecosystem như Claude Code đang có

## Link
- Repo (agent chính): https://github.com/earendil-works/pi
- Monorepo (toàn bộ package): https://github.com/badlogic/pi-mono
- Docs: https://pi.dev

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Pi là CLI Node.js, Hermes gọi qua subprocess thay vì API trực tiếp
import subprocess

def run_pi_task(prompt, cwd):
    result = subprocess.run(
        ["pi", "--print", prompt],
        cwd=cwd, capture_output=True, text=True,
        env={"ANTHROPIC_API_KEY": "[YOUR_API_KEY]"}
    )
    return result.stdout
```

### OpenClaw
```bash
npm install -g @mariozechner/pi-coding-agent
pi /login   # dùng chung subscription Claude nếu có, khỏi cần API key riêng
```

### Antigravity
```bash
# Deploy trên VPS: cài Node.js 18+ trước, rồi cài global như trên
node --version   # đảm bảo >=18
npm install -g @mariozechner/pi-coding-agent
```
> ⚠️ Mặc định chạy lệnh không hỏi xin quyền (YOLO mode) — trên VPS chạy tự động, cân nhắc giới hạn phạm vi thư mục agent được đụng vào.

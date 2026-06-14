# Hermes Agent — AI Agent Tự Học, Tự Cải Tiến, Nhớ Mày Mãi Mãi

**GitHub:** https://github.com/NousResearch/hermes-agent
**Stars:** 188k+ (7 tuần ra mắt đạt 95k, hiện tại 188k và đang tăng)
**License:** MIT | **Tác giả:** Nous Research
**Version:** v0.16.0 | **Website:** hermes-ai.net

---

## Tại Sao Khác Với Mọi Agent Khác

Tất cả AI agents — ChatGPT, Claude, LangChain agents — đều bắt đầu lại từ đầu mỗi phiên. Mày phải giải thích codebase, preference, context mỗi lần.

Hermes là agent đầu tiên có **closed learning loop**:
- Tạo skill từ kinh nghiệm thực tế
- Cải tiến skill trong khi dùng
- Nhớ mày xuyên phiên
- Tự dọn dẹp skill library mỗi 7 ngày

Sau 3 tháng dùng: agent ngày 90 thông minh hơn ngày 1 mà không cần train lại.

---

## 8 Vòng Lặp Kiến Trúc

| # | Vòng | Tần suất | Chức năng |
|---|------|----------|-----------|
| 1 | Core Agent Loop | ms → phút | Tim hệ thống. prompt+tool+repeat, max 90 lượt/phiên |
| 2 | Ralph /goal | phút → giờ | Đánh giá mục tiêu sau mỗi lượt. Max 20 lượt/mục tiêu |
| 3 | Tự Cải Tiến / Skills | Sau mỗi tác vụ | Lưu method hiệu quả thành skill file (~/.hermes/skills/) |
| 4 | Curator | Mỗi 7 ngày | Dọn skill ít dùng, hợp nhất trùng lặp. Không xóa vĩnh viễn |
| 5 | Bộ Nhớ | Xuyên suốt | RAM + MEMORY.md/USER.md + FTS5 SQLite. 2200 ký tự/lượt |
| 6 | Kanban Dispatcher | Mỗi 60 giây | Quét kanban.db, dispatch nhiều /goal song song |
| 7 | Nén Ngữ Cảnh | Khi >50% context | 4 giai đoạn lọc → tóm tắt → session con mới |
| 8 | Agent Con | Theo demand | delegate_task(), max 3 sub-agent đồng thời |

**Compound Effect:**
```
Skill(3) + Curator(4) + Goal(2) = nhanh hơn + nhiều skill hơn
→ Agent ngày 90 > Agent ngày 1
```

---

## Cài Đặt — 60 Giây

```bash
# Linux, macOS, WSL2, Android (Termux)
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Reload shell
source ~/.bashrc  # hoặc ~/.zshrc

# Setup LLM provider
hermes setup

# Chạy
hermes
```

Installer tự lo: Python 3.11 (via uv, không cần sudo), Node.js v22, ripgrep, ffmpeg. Chỉ cần git là đủ.

---

## 3 Bước Bắt Đầu

```bash
# Bước 1 (5 phút) — Setup core
hermes setup --portal  # kích hoạt L1 + L5

# Bước 2 (10 phút) — Chạy goal đầu tiên
/goal [mô tả task]     # kích hoạt L2 + L3

# Bước 3 (30 phút) — Setup cron
# Cron 8h sáng → L1+L2+L3+L5+L7 tự chạy
# L4 (Curator) tự kích hoạt sau 7 ngày
# L8 kích hoạt khi dùng delegate_task
```

---

## Chạy Ở Đâu

**Local:** Laptop, desktop thông thường
**VPS:** $5/tháng là đủ — không cần laptop luôn bật
**Cloud:** Docker, SSH, Modal, Daytona, Vercel Sandbox
**Mobile:** Android via Termux

**Nhắn tin qua 18 platforms:**
Telegram, Discord, Slack, WhatsApp, Signal, Feishu/Lark, WeCom, QQBot, Yuanbao + Microsoft Teams (plugin)

---

## Dùng Model Nào Cũng Được

Nous Portal, OpenRouter (200+ models), NovitaAI, NVIDIA NIM, OpenAI, Anthropic, Bedrock, Hugging Face, hoặc endpoint riêng của mày.

**Tip:** Dùng model rẻ cho sub-agents (L8), model mạnh cho parent orchestrator → tiết kiệm chi phí đáng kể.

---

## Bộ Nhớ — 3 Lớp

```
Layer 1: RAM session    → nhanh, mất sau khi tắt
Layer 2: MEMORY.md      → long-term, inject vào mỗi lượt
          USER.md       → profile của mày
Layer 3: FTS5 SQLite    → full-text search lịch sử phiên
```

Giới hạn 2200 ký tự / 800 token inject mỗi lượt. Plugin Mem0 giảm 72% token usage.

---

## Skills Hub — Ecosystem Đang Bùng Nổ

Sau 3 tháng dùng: 40-60 skills tích lũy trong `~/.hermes/skills/`.

Community đang build Skills Hub với 90,000+ skills công khai — mày có thể import skill của người khác thay vì tự build từ đầu.

---

## So Sánh Framework

| Framework | Architecture | Đặc điểm |
|-----------|-------------|---------|
| Chat wrapper | 1 loop | Chatbot đơn giản |
| LangChain / CrewAI | 2-3 loops | Multi-agent cơ bản |
| DSPy | Optimize prompts | Không có runtime |
| **Hermes** | **8 loops** | **AI Operating System** |

---

## Điểm Trừ Thẳng Thắn

**Setup phức tạp hơn tools khác:** 3 bước bắt đầu, cần hiểu concept loops để dùng hiệu quả.

**Tốn token hơn:** 8 vòng lặp = nhiều LLM calls hơn agent thông thường. Cần tính chi phí kỹ nếu dùng model đắt.

**Còn mới:** v0.16.0, ecosystem đang grow nhanh nhưng docs chưa hoàn chỉnh. Bugs vẫn xuất hiện.

**Cần infrastructure:** Chạy tốt nhất trên VPS luôn bật — không phải tool mở lên hỏi 1 câu rồi tắt.

---

## Đánh Giá Cá Nhân

188k stars trong vài tháng không phải ngẫu nhiên — Hermes giải quyết vấn đề thực sự mà mọi người dùng AI đều gặp: phải giải thích lại context mỗi lần.

Closed learning loop là concept đúng đắn. Nhưng đây là tool cho người dùng AI nghiêm túc — không phải cho người muốn mở ra hỏi 1 câu rồi tắt. Cần đầu tư setup và thời gian để thấy compound effect.

Nếu mày dùng AI agent hàng ngày cho work — đây là thứ đáng cài nhất trong kho hiện tại. Sau 30-90 ngày, agent sẽ hiểu workflow của mày mà không cần giải thích lại.

**Rating: 9.5/10** — best-in-class cho serious AI users. Trừ 0.5 vì còn non và cần infrastructure.

---

*Nguồn: github.com/NousResearch/hermes-agent*
*Stars: 188k+ (tính đến 6/2026, tăng nhanh)*
*Cập nhật: tháng 6/2026*

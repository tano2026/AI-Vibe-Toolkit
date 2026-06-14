# Hermes Agent — AI Agent Tự Học, Tự Cải Tiến, Nhớ Mày Xuyên Phiên

**GitHub:** https://github.com/NousResearch/hermes-agent
**Stars:** 188k+ (95k sau 7 tuần, 188k hiện tại) | **License:** MIT
**Tác giả:** Nous Research | **Version:** v0.16.0
**Website:** hermes-ai.net
**Slogan:** "The agent that grows with you"

---

## Tại Sao Khác Với Mọi Agent Khác

Hầu hết AI agent bắt đầu lại từ đầu mỗi conversation. Hermes tích lũy:

- **Skills từ kinh nghiệm** — tự tạo skill file sau mỗi tác vụ phức tạp
- **Memory xuyên phiên** — nhớ mày là ai, mày làm gì, mày thích gì
- **Tự cải tiến** — skills được grade, merge, prune mỗi 7 ngày

Sau 3 tháng dùng: 40-60 skills tích lũy → Agent ngày 90 thông minh hơn ngày 1 mà không cần train lại.

---

## Kiến Trúc 8 Vòng Lặp

| Vòng | Tên | Chu kỳ | Làm gì |
|------|-----|--------|--------|
| 1 | Core Agent Loop | ms → phút | Tim hệ thống, prompt+tool+repeat, max 90 lượt/phiên |
| 2 | Ralph /goal | phút → giờ | Đánh giá mục tiêu sau mỗi lượt, max 20 lượt/goal |
| 3 | Tự Cải Tiến | Sau mỗi tác vụ | Tạo skill file, lưu vào `~/.hermes/skills/` |
| 4 | Curator | Mỗi 7 ngày | Dọn kho skill: grade, merge, archive (không xóa vĩnh viễn) |
| 5 | Bộ Nhớ | Xuyên suốt | RAM + MEMORY.md/USER.md + FTS5 SQLite |
| 6 | Kanban Dispatcher | Mỗi 60 giây | Quét kanban.db, giao việc, phát hiện zombie process |
| 7 | Nén Ngữ Cảnh | Khi >50% context | 4 giai đoạn lọc → tóm tắt → session con mới |
| 8 | Agent Con | Mỗi khi delegate | Max 3 sub-agents song song, model rẻ cho con |

**Compound effect:**
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
source ~/.bashrc

# Setup LLM provider
hermes setup

# Chạy
hermes
```

Installer tự lo: Python 3.11 (via uv), Node.js v22, ripgrep, ffmpeg. Chỉ cần git.

---

## 3 Bước Bắt Đầu

```bash
# Bước 1 (5 phút) — Setup cơ bản
hermes setup --portal + L1+L5

# Bước 2 (10 phút) — Chạy goal đầu tiên
/goal [mô tả task] → kích hoạt L2+L3

# Bước 3 (30 phút) — Setup cron
# Cron 8h sáng → L1+L2+L3+L5+L7 tự chạy
# L4 tự kích hoạt sau 7 ngày
# L8 kích hoạt khi dùng delegate_task
```

---

## LLM Providers Hỗ Trợ

Nous Portal, OpenRouter (200+ models), NovitaAI, NVIDIA NIM, OpenAI, Anthropic, Bedrock, Hugging Face, Xiaomi MiMo, Kimi/Moonshot, MiniMax, z.ai/GLM, hoặc endpoint tự host.

**Strategy tối ưu chi phí:** Model mạnh (Claude Opus, GPT-4o) cho parent orchestrator. Model rẻ (Haiku, Flash) cho sub-agents.

---

## 18 Messaging Platforms

Telegram, Discord, Slack, WhatsApp, Signal, Feishu/Lark, WeCom, QQBot, Yuanbao + Microsoft Teams (plugin) + 8 khác.

Mày chat trên Telegram trong khi Hermes chạy task trên cloud VM — không cần ngồi trước laptop.

---

## 7 Execution Backends

Local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox.

Chạy trên $5 VPS, GPU cluster, hoặc serverless (gần $0 khi idle).

---

## Memory System

```
RAM session (nhanh, tạm thời)
        +
MEMORY.md + USER.md (long-term, ~/.hermes/memories/)
        +
FTS5 SQLite full-text search (tìm kiếm conversation cũ)
```

Giới hạn 2200 ký tự / 800 token inject vào mỗi lượt. Plugin Mem0 giảm -72% token.

---

## Skills Hub

Hermes duy trì skill library qua autonomous Curator — grade, consolidate, prune mỗi 7 ngày. Hiện tại Skills Hub của community đã vượt **90,000 skills** — lớn nhất trong bất kỳ open-source agent framework nào.

Tìm và cài skill từ community:
```bash
hermes skill search "python debugging"
hermes skill install <skill-id>
```

---

## So Sánh Framework

| Framework | Loops | Đặc điểm |
|-----------|-------|----------|
| Chat wrapper | 1 | Stateless |
| LangChain / CrewAI | 2-3 | Multi-agent cơ bản |
| DSPy | - | Optimize prompts, không runtime |
| **Hermes** | **8** | **AI Operating System — tự học, tự nhớ** |

---

## Tích Hợp Với Kho Này

Hermes có **MCP integration native** — cài các MCP servers trong kho này vào Hermes:

```bash
# Trong hermes config
mcp_servers:
  - firecrawl    # mcps/firecrawl.md
  - brave-search # mcps/brave-search.md
  - filesystem   # mcps/filesystem.md
  - notebooklm   # mcps/notebooklm-mcp-pleaseprompto.md
```

Hermes + MCP stack = agent có thể search web, đọc file, query NotebookLM — tất cả tự động.

---

## Điểm Trừ Thẳng Thắn

**Setup phức tạp hơn chat interface:** 8 vòng lặp = nhiều config. Mày cần hiểu cơ bản để tune đúng.

**Resource usage:** 8 loops chạy liên tục → tốn CPU/RAM hơn agent thông thường. Cần VPS $5+ để chạy 24/7.

**Skills quality không đồng đều:** 90k community skills — chất lượng rất khác nhau. Phải test trước khi dùng production.

**Còn đang phát triển nhanh:** v0.16.0, breaking changes thường xuyên giữa các versions.

---

## Đánh Giá Cá Nhân

188k stars trong vài tháng không phải hype trống rỗng — đây là repo giải quyết vấn đề thực tế nhất của AI agents: chúng không nhớ và không học.

Điểm tao thấy hứa hẹn nhất là **compound effect**. Sau 90 ngày dùng, agent của mày sẽ khác hoàn toàn với agent của người mới cài — vì nó đã tích lũy skills và context từ workflow cụ thể của mày. Đây là thứ không framework nào khác có.

Phù hợp nhất: Technical users muốn agent chạy 24/7 trên VPS, xử lý task tự động, và thông minh hơn theo thời gian. Không phải cho người muốn chat đơn giản.

Tao recommend thử theo đúng 3 bước trong README — đừng cố setup hết tất cả ngay. L4 và L8 tự kích hoạt khi cần.

**Rating: 9.5/10** — best-in-class autonomous agent hiện tại.

---

*Nguồn: github.com/NousResearch/hermes-agent*
*Stars: 188k+ (6/2026) | Cập nhật: tháng 6/2026*

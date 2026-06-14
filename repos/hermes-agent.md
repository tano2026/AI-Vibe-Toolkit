# Hermes Agent — AI Agent Tự Học, Tự Cải Tiến, Càng Dùng Càng Thông Minh

**GitHub:** https://github.com/NousResearch/hermes-agent
**Stars:** 188k+ (7 tuần đạt 95k, hiện 188k và tăng tiếp) | **License:** MIT
**Tác giả:** Nous Research | **Version:** v0.16.0
**Website:** hermes-ai.net

---

## Tại Sao Khác Mọi Agent Framework Khác

Chat wrapper, LangChain, CrewAI — tất cả **bắt đầu lại từ đầu mỗi phiên**. Mày phải giải thích lại context, workflow, preferences mỗi lần.

Hermes Agent có **closed learning loop** — agent tạo skill từ kinh nghiệm, cải tiến skill trong lúc dùng, nhớ mày là ai qua nhiều phiên. Càng dùng lâu càng thông minh hơn.

```
Chat wrapper:     Ngày 1 = Ngày 90 (luôn bắt đầu lại)
Hermes Agent:     Ngày 90 >> Ngày 1 (40-60 skills tích lũy)
```

---

## 8 Vòng Lặp — Kiến Trúc Compound

### Vòng 1 — Core Agent Loop (ms → phút)
Tim của hệ thống. `prompt + tool + repeat`, max 90 lượt/phiên. Tool calls đơn lẻ = thread chính, nhiều tool = ThreadPoolExecutor (8 workers song song). 3 chế độ API: streaming / non-streaming / Anthropic.

### Vòng 2 — Ralph /goal (phút → giờ)
Trợ lý đánh giá mục tiêu sau mỗi lượt. Hoàn thành chưa? Max 20 lượt/mục tiêu. Tích hợp /subgoal để thêm tiêu chí giữa chừng mà không reset bộ đếm.

### Vòng 3 — Tự Cải Tiến / Skills (sau mỗi tác vụ)
Agent tự phân tích phương pháp hiệu quả → lưu thành skill file (`~/.hermes/skills/`). Chạy ngầm qua fork process, không ảnh hưởng phiên chính. Sau 3 tháng: 40-60 skills tích lũy.

### Vòng 4 — Curator (mỗi 7 ngày)
Tự động dọn dẹp kho skill khi rảnh ≥2h. Chuyển skill ít dùng vào `.archive/`, hợp nhất skill trùng lặp. **Không bao giờ xóa vĩnh viễn.**

### Vòng 5 — Bộ Nhớ (xuyên suốt và sau phiên)
3 lớp: RAM session + `MEMORY.md/USER.md` (long-term) + FTS5 SQLite full-text search. Giới hạn 2200 ký tự/800 token chèn vào mỗi lượt. 8 plugin memory ngoài — Mem0 giảm 72% token.

### Vòng 6 — Kanban Dispatcher (mỗi 60 giây)
Quét `kanban.db` (SQLite), giao việc cho worker rảnh, phát hiện zombie process, thu hồi task bị treo. Dispatch nhiều /goal song song.

### Vòng 7 — Nén Ngữ Cảnh (tự kích hoạt khi >50% context)
4 giai đoạn: lọc tool output cũ → kiểm tra hiệu quả → tóm tắt LLM (giữ 3 đầu + 20 cuối) → tạo session con mới. Giữ cost trong tầm kiểm soát cho /goal dài hạn.

### Vòng 8 — Agent Con / Sub-Agents (song song)
`delegate_task()` khởi tạo sub-agent với context riêng. Max 3 chạy đồng thời. Mỗi agent con tự chạy vòng 1,2,3,5,7. **Dùng model rẻ cho con, model mạnh cho parent orchestrator.**

---

## Compound Effect

```
Loop 3 tạo Skill → Loop 4 tinh lọc
Skill sạch → Loop 2 (/goal) nhanh hơn
Loop 5 cung cấp context tức thì
Loop 6 dispatch nhiều Loop 2 song song
Loop 7 giữ cost Loop 1 ở mức hợp lý
Loop 8 nhân bản năng lực Loop 1

Kết quả: Skill(3) + Curator(4) + Goal(2)
= Agent ngày 90 > Agent ngày 1
```

---

## Cài Đặt

```bash
# One-line install — Linux, macOS, WSL2, Android (Termux)
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Reload shell
source ~/.bashrc  # hoặc ~/.zshrc

# Bắt đầu
hermes
```

Installer tự lo: Python 3.11 (via uv, không cần sudo), Node.js v22, ripgrep, ffmpeg. Chỉ cần có git.

---

## Bắt Đầu 3 Bước

```bash
# Bước 1 (5 phút) — Setup portal + memory + skills
hermes setup --portal
# Kích hoạt L1 + L5

# Bước 2 (10 phút) — Thử goal đầu tiên
/goal [mô tả task của mày]
# Kích hoạt L2 + L3

# Bước 3 (30 phút) — Setup cron tự động
# Cron 8h sáng → L1+L2+L3+L5+L7
# L4 tự kích hoạt sau 7 ngày
# L8 kích hoạt khi dùng delegate_task
```

---

## Chạy Ở Đâu

| Platform | Chi phí | Phù hợp |
|----------|---------|---------|
| Laptop local | $0 | Dev, test |
| $5 VPS (Hetzner, DigitalOcean) | $5/tháng | Production cá nhân |
| GPU cluster | Theo usage | Heavy workload |
| Vercel Sandbox | Serverless | Gần $0 khi idle |
| Modal / Daytona | Serverless | Scale khi cần |

**Không bị buộc vào laptop** — chat từ Telegram trong khi agent chạy trên cloud VM.

---

## 18 Nền Tảng Nhắn Tin

Telegram · Discord · Slack · WhatsApp · Signal · Matrix · Mattermost · Email · SMS · DingTalk · Feishu/Lark · WeCom · QQBot · Yuanbao · BlueBubbles · Home Assistant · Microsoft Teams (plugin)

---

## Models Hỗ Trợ

Nous Portal · OpenRouter (200+ models) · NovitaAI · NVIDIA NIM · OpenAI · Anthropic · Hugging Face · Kimi/Moonshot · MiniMax · GLM · Xiaomi MiMo · custom endpoint

---

## Skills Hub — Ecosystem Đang Bùng Nổ

90,000+ skills đã được community đóng góp. Tốc độ tăng trưởng hiện tại có thể đưa đây trở thành **skill library lớn nhất của bất kỳ open-source agent framework nào**.

```bash
# Cài skills từ community
hermes skills install [tên-skill]

# Xem skills đang có
hermes skills list
```

---

## Hệ Quả Khi Thiếu Vòng Lặp

| Thiếu | Hậu quả |
|-------|---------|
| L3 (Skills) | Mỗi phiên bắt đầu từ con số 0 |
| L4 (Curator) | Kho skill phình + nhiều context |
| L5 (Memory) | "Mất trí nhớ" sau mỗi phiên |
| L7 (Nén) | /goal >20 lượt → API timeout |
| L6 (Kanban) | Điều phối đa agent = thủ công |
| L8 (Sub-agents) | Tác vụ phức tạp bị nút cổ chai |

---

## Đánh Giá Cá Nhân

188k stars trong chưa đầy 2 tháng — đây là tốc độ tăng trưởng nhanh nhất trong lịch sử GitHub cho category AI agents. Không phải hype trống rỗng — architecture 8 vòng lặp có foundation lý thuyết rõ ràng và Nous Research là lab đứng sau Hermes model family.

Điểm tao thấy quan trọng nhất: **closed learning loop**. Đây là thứ phân biệt Hermes với mọi agent framework khác. Sau 3 tháng dùng liên tục, agent của mày sẽ khác hoàn toàn với agent của người khác — vì nó đã học từ workflow cụ thể của mày.

Cài 1 lệnh, chạy được ngay trên $5 VPS, MIT license — barrier to entry thấp.

Điểm trừ: 8 vòng lặp có nghĩa là debug phức tạp hơn khi có vấn đề. Và skills hub 90k+ còn thiếu curation tốt — nhiều skills chất lượng không đều.

**Rating: 9.5/10** — repo đáng cài nhất trong kho tính đến tháng 6/2026.

---

*Nguồn: github.com/NousResearch/hermes-agent*
*Stars: 188k+ (tháng 6/2026) | MIT License*
*Cập nhật: tháng 6/2026*

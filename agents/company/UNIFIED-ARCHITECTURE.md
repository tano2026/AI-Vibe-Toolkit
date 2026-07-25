---
name: unified-architecture
description: >
  Nguồn chân lý DUY NHẤT về việc gì chạy ở đâu (VPS vs Local Windows), thay thế mọi mô tả
  mâu thuẫn trước đó trong HERMES-PLAYBOOK.md (sai khi ghi Hermes chạy VPS) và cách chia
  "8 phòng ban" (TANO-AGENCY local) vs "9 role" (ORG-v2.md GitHub). Đọc file này TRƯỚC
  HERMES-PLAYBOOK.md/OPENCLAW-PLAYBOOK.md nếu 2 bên có xung đột — file này thắng.
version: 1.0
updated: 2026-07-25
status: DRAFT — chờ xác nhận 2 điểm ở cuối file trước khi Hermes/OpenClaw thực thi
---

# Unified Architecture — 1 công ty, 2 nơi chạy, không còn 2 não

> Viết sau khi phát hiện: kho GitHub (`ORG-v2.md`, `HERMES-PLAYBOOK.md`) và thực tế đang chạy
> (`TANO-AGENCY` local, do Claude Code/deepseek audit trực tiếp 10 file thật) mô tả 2 kiến trúc
> khác nhau cho cùng 1 hệ thống — 2 Telegram bot, 2 taskboard, 2 skill dir, 2 cách chia role.
> File này là bản gộp — sau khi xác nhận, mọi playbook khác phải sửa lại cho khớp file này.

---

## Nguyên tắc cốt lõi — sửa đúng gốc vấn đề

**Vấn đề gốc không phải "VPS vs Local"** — cả hai đều cần giữ, đúng ý Nobitano (Local để xử lý
nghiệp vụ nặng/dung lượng lớn, VPS để chạy 24/7/public-facing). **Vấn đề gốc là đang có 2 bộ
não ngang hàng** (Hermes tự nhận lệnh riêng, OpenClaw tự nhận lệnh riêng) thay vì 1 bộ não điều
phối, 2 nơi thực thi.

```
SAI (hiện tại — 2 não đá nhau):
  Nobitano → Telegram Bot A (Hermes, Local) → tự quyết, tự làm
  Nobitano → Telegram Bot B (OpenClaw, VPS)  → tự quyết, tự làm
  (không nói chuyện với nhau, không taskboard chung)

ĐÚNG (sau khi gộp — 1 não, 2 tay):
  Nobitano → 1 Telegram Bot duy nhất (CEO Bot)
                    ↓
             1 Taskboard duy nhất
                    ↓ dispatch theo LOẠI VIỆC, không theo "của ai"
       ┌────────────┴────────────┐
       ▼                         ▼
  LOCAL WINDOWS              VPS
  (nghiệp vụ nặng)           (24/7, nhẹ, public-facing)
```

---

## 1. Điểm vào — 1 Telegram bot duy nhất

**Giữ `main.py` (CEO Bot)** — đã có sẵn: chat tự nhiên, dispatch agent, project context, fact
memory. **Tắt vĩnh viễn** Domain Agent Router của OpenClaw nhận Telegram riêng.

**Chạy ở đâu:** VPS. Lý do — bot Telegram là điểm vào duy nhất của toàn hệ thống, không được
phép offline. Máy Local Windows tắt (hết giờ làm, mất điện, restart) → nếu bot chạy ở đó, mất
kênh nhận lệnh hoàn toàn. VPS 24/7 mới đảm bảo Nobitano lúc nào cũng ra lệnh được.

CEO Bot chỉ làm 1 việc: nhận lệnh → phân loại việc nhẹ/nặng → ghi vào Taskboard → dispatch. Bản
thân nó KHÔNG chạy việc nặng (không chạy trực tiếp trên VPS logic xử lý dev/video — chỉ ghi task,
để Local tự pull về xử lý).

## 2. Taskboard — 1 nguồn duy nhất, truy cập được từ cả 2 nơi

**Vấn đề với `hq.db` (SQLite local hiện tại):** SQLite là file cục bộ trên máy Windows — VPS
không đọc/ghi được trực tiếp qua mạng. Nếu giữ hq.db làm taskboard chính, VPS Agent không thể
tự dispatch/tự đọc task khi cần.

**Quyết định: dùng Airtable làm taskboard chính thức duy nhất** — đã có schema thiết kế sẵn
trong `COORDINATION-v2.md` (bảng `jobs`, `approvals`, `escalations`, `kpis`...), truy cập qua
REST API từ bất kỳ đâu, cả VPS lẫn Local đều gọi được như nhau. Đây chính là lý do
`agents/company/roles/*` + COORDINATION-v2.md tồn tại — giờ mới thực sự cần dùng tới.

`hq.db` **không bị xoá** — giữ làm local cache/log riêng cho máy Windows (tăng tốc đọc, hoạt
động được cả khi mất mạng tạm thời), nhưng KHÔNG còn là nguồn chân lý — Airtable mới là.

n8n queue của OpenClaw (VPS) → gộp vào, không chạy song song. n8n có thể giữ làm công cụ chạy
scheduled job cụ thể (ví dụ: cron đăng bài), nhưng job đó vẫn phải có bản ghi trong Airtable
`jobs`, không được là hàng đợi riêng biệt CEO Bot không thấy.

## 3. Skill directory — 1 kho duy nhất

**`AI-Vibe-Toolkit` (GitHub, repo private) là kho skill chính thức duy nhất** — đã có 109+
skill, 151 repo, 44 mcp, cấu trúc template chuẩn, TRACKER.md theo dõi đầy đủ. Migrate toàn bộ
skill riêng của OpenClaw (yt-cashcow, trum-du-lich) vào đúng folder `/skills/` hoặc `/mcps/`
theo template có sẵn — không giữ skill dir riêng trên VPS nữa.

MCP server (`tuvi-mcp-server`) hiện chạy trùng 2 nơi (Local + VPS) — **chỉ chạy 1 lần trên VPS**
(vì cần public-facing/API 24/7), Local gọi qua network nếu cần dùng, không tự chạy process
riêng nữa. Tránh 2 process cùng 1 MCP dẫm chân nhau.

## 4. Vai trò — dùng 9 role của ORG-v2.md làm khung chuẩn, KHÔNG dùng "8 phòng ban" song song

ORG-v2.md đã có JD/KPI/escalation/guardrail chi tiết cho 9 role (Research&Analytics, Marketing,
Sales, Content Creator, Dev&Automation, Designer, Media, Ops&Finance, HR&Admin) — đây là khung
đầy đủ nhất đang có. "8 phòng ban" trong `agent-core` (TANO-AGENCY local) cần **map vào đúng 9
role này**, không tồn tại song song như 1 taxonomy riêng.

**⚠️ Cần xác nhận (xem mục "Chờ xác nhận" cuối file):** tao chưa có tên chính xác 8 phòng ban
trong `agent-core/spec.py` để map 1-1. Không đoán bừa — cần đọc `AGENTS.md` hoặc
`PROJECT-MAP.md` thật để khớp đúng.

## 5. Phân công Local vs VPS — theo LOẠI VIỆC, không theo "Hermes" hay "OpenClaw"

Không còn khái niệm "agent của Hermes" / "agent của OpenClaw" — chỉ còn 9 role, mỗi role có 1
hoặc nhiều **nơi thực thi** tuỳ đặc tính công việc:

| Role (ORG-v2) | Chạy ở đâu | Vì sao |
|---|---|---|
| ⑤ Dev & Automation | **Local** (Claude Code) | Cần disk lớn, compute nặng, không cần uptime 24/7 khi đang code |
| ④ Content Creator | **Local** | GMSP video pipeline, HyperFrames — nặng, cần dung lượng lớn |
| ① Research & Analytics | **Local** (RIO Bot) | Nghiên cứu sâu, xử lý data lớn, không cần real-time |
| ⑥ Designer | **Local** | Asset nặng, cần app desktop (Canva/Adobe qua MCP OK cả 2 nơi) |
| ⑧ Ops & Finance | **VPS** | Cần chạy cron đều đặn, fulfillment/CSKH sau bán cần phản hồi nhanh 24/7 |
| ③ Sales | **VPS** | CSKH trước bán, chat live cần luôn online |
| ⑦ Media | **VPS** | Đăng bài đúng lịch — cần uptime, không phụ thuộc máy Local có bật hay không |
| ② Marketing | **VPS** | Theo dõi ads/traffic real-time |
| ⑨ HR & Admin | **VPS** | Nhẹ, không cần compute lớn, cần luôn sẵn sàng khi có việc gấp (ca trực) |

Local Windows = "xưởng nặng", VPS = "cửa hàng mặt tiền 24/7". Khớp đúng tinh thần mày nói: dùng
Local để tránh quá tải dung lượng/compute VPS, dùng VPS để đảm bảo phần khách hàng thấy luôn chạy.

## 6. VPS Agent thay OpenClaw cũ

Đồng ý hướng Claude Code đề xuất: **triệt thoái OpenClaw hiện tại** (Node.js, tự nhận Telegram,
tự route domain) → thay bằng 1 Python agent mỏng, KHÔNG tự quyết, chỉ thực thi:
```
task_types = ["execute", "healthcheck", "deploy-api", "run-cron"]
```
VPS Agent chỉ pull task từ Airtable (theo role được gán "VPS" ở mục 5) → chạy → ghi kết quả lại
Airtable → không có quyền dispatch hay quyết định gì khác — giống nguyên tắc DECISION-MATRIX.md
áp dụng cho mọi executor, không riêng gì Hermes/Antigravity.

---

## Không đổi — vẫn đúng, giữ nguyên

- `DECISION-MATRIX.md` (L0-L3, 3 lằn ranh đỏ) — không mâu thuẫn gì với thực tế, giữ làm chuẩn tuyệt đối cho mọi hành động dù chạy Local hay VPS
- `SENIOR-ADVISOR.md` — vẫn đúng nguyên tắc (Claude không phải worker, chỉ escalate theo yêu cầu), chỉ cần sửa 1 chỗ: giai đoạn 2 gọi qua CEO Bot (không phải "gọi qua Hermes" như viết trước — vì giờ Hermes không phải điểm vào duy nhất nữa, CEO Bot mới là)
- Cấu trúc kho `AI-Vibe-Toolkit` (mcps/repos/skills/stacks/content) — giữ nguyên, chỉ thêm skill migrate từ OpenClaw vào

## Cần sửa sau khi xác nhận xong

- `HERMES-PLAYBOOK.md` dòng 16 — xoá câu "chạy trong OpenClaw trên VPS", sửa thành "chạy Local
  Windows, nhận task từ Taskboard (Airtable), không tự nhận Telegram trực tiếp nữa"
- `OPENCLAW-PLAYBOOK.md` — viết lại hoàn toàn theo vai trò mới (VPS Agent mỏng, không phải
  orchestrator độc lập)
- `ORG-v2.md` — thêm cột "Chạy ở đâu" (mục 5 ở trên) vào bảng 9 role

---

## ⚠️ Chờ xác nhận trước khi Hermes/OpenClaw thực thi bất kỳ bước nào

1. **VPS hiện đang DOWN** (theo `INFRA/README.md` Claude Code đọc được) — đã reboot chưa? Nếu
   chưa, không thể chạy Bước 1 (CEO Bot chuyển sang VPS) cho tới khi VPS sống lại.
2. **Tên 8 phòng ban thật trong `agent-core/spec.py`** — cần map chính xác vào 9 role ORG-v2,
   không đoán. Paste nội dung `AGENTS.md` hoặc `PROJECT-MAP.md` để map đúng.
3. **OpenClaw hiện có đang chạy production việc gì quan trọng không** (bot khách ABTrip, lịch
   đăng đã set) — quyết định tắt ngay hay migrate từ từ theo lộ trình.

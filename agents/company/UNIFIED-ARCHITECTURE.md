---
name: unified-architecture
description: >
  Nguồn chân lý DUY NHẤT về việc gì chạy ở đâu (VPS vs Local Windows), 9 agent thật đang có
  trong agent-core. Thay thế mọi mô tả mâu thuẫn trước đó trong HERMES-PLAYBOOK.md (sai khi
  ghi Hermes chạy VPS) và ORG-v2.md (9 role lý thuyết, chưa khớp 9 agent thật). Đọc file này
  TRƯỚC HERMES-PLAYBOOK.md/OPENCLAW-PLAYBOOK.md nếu 2 bên xung đột — file này thắng.
version: 2.0
updated: 2026-07-25
status: THIẾT KẾ ĐÃ CHỐT — chỉ còn chờ Nobitano reboot VPS (mục "Chờ xác nhận" cuối file) trước khi thực thi Bước 1
---

# Unified Architecture v2 — Dựa trên audit thật, không còn giả định

> v1 giả định "2 não đá nhau" (Hermes Local vs OpenClaw VPS). Sau khi Claude Code audit trực
> tiếp codebase `TANO-AGENCY`: **OpenClaw không có 1 dòng code nào trong repo** — chỉ tồn tại
> trong archive/docs mô tả kiến trúc cũ. Hệ thống thật đang chạy là **agent-core** (Python,
> Local Windows) với 9 agent + CEO Bot qua Telegram, cron qua Hermes. Bản v2 này thiết kế lại
> dựa trên sự thật đó, không phải trên giả định lý thuyết của ORG-v2.md (9-role) nữa.

---

## Sự thật đã xác nhận (25/07/2026, qua audit Claude Code)

| Câu hỏi | Kết quả |
|---|---|
| VPS đang chạy gì? | ❌ **DOWN** (SSH timeout). IP `100.64.173.75` là dải CGNAT — nhiều khả năng là IP nội bộ, không phải IP public thật |
| OpenClaw có code thật không? | **KHÔNG** — 0 dòng code Node.js trong repo TANO-AGENCY. Chỉ có trong archive (`trum-du-lich/archive/trum-san-bay-v1-airtable/`) và docs lý thuyết |
| Cron job chạy qua ai? | **100% qua Hermes (Local Windows)** — `cron_dispatch.py`, `cron_telegram.py`, `cron_morning.py`, không cái nào qua OpenClaw |
| Khách hàng thật phụ thuộc OpenClaw? | **Không tìm thấy** — ABTrip backend là FastAPI độc lập (port 8767), không qua OpenClaw |
| Tắt OpenClaw ngay có ảnh hưởng gì không? | **Nhiều khả năng KHÔNG** — nhưng chưa loại trừ 100% vì có thể còn process trên VPS (chưa SSH được để check `pm2 list`) |

**Kết luận:** không phải "2 hệ thống sống cạnh tranh cần hoà giải" như v1 giả định — mà là **1 hệ
thống sống thật (agent-core Local)** + **1 khái niệm gần như đã chết (OpenClaw)**, còn sót lại
trong tên gọi/docs nhưng không còn vận hành gì. Việc "gộp" thực chất là **chính thức khai tử
OpenClaw**, không phải đàm phán giữa 2 bên ngang hàng.

---

## 9 agent THẬT — nguồn chân lý mới (thay thế bảng 9-role lý thuyết của ORG-v2.md)

Copy nguyên văn từ `agents/__init__.py` (agent-core):

| # | Agent | Việc chính | Task types |
|---|---|---|---|
| 0 | **ceo** 🧠 | Nhận lệnh, phân tích, giao việc, theo dõi tiến độ, báo cáo | plan, delegate, status, daily-briefing |
| 1 | **research** 🔬 | Nghiên cứu thị trường, phân tích ngách, fact-check, đối thủ, xu hướng | research, deep-dive, fact-check, niche, video, trend-analysis |
| 2 | **dev** 🔧 | Code/deploy, fix bug, hạ tầng, review | build, review, scan, deploy, fix |
| 3 | **sales** 💰 | Lead-gen, CSKH trước bán, outreach, proposal, pipeline | lead-gen, outreach, proposal, market-intel |
| 4 | **marketing** 📢 | Content đa kênh, SEO, campaign, content calendar, trend | content, seo, campaign, social |
| 5 | **media** 🎬 | Thiết kế, hình ảnh, video, storyboard, format check, brand asset | render, footage-search, format-check, storyboard |
| 6 | **operations** ⚙️ | Healthcheck/monitor/backup/incident (hạ tầng) + đơn/booking/lịch (business) + tự động hoá | healthcheck, monitor, backup, incident-response |
| 7 | **support** 🎫 | CSKH 24/7 sau bán, KB/FAQ, ticket, escalate | ticket, kb-search, kb-ingest, faq-gen, escalate |
| 8 | **analytics** 📊 | Doanh thu, KPI, dashboard, trend/anomaly, forecast, SWOT | sql-query, report, dashboard, data-audit, swot, sentiment, forecast, kpi |

**Đối chiếu với 9-role lý thuyết ORG-v2.md — 4 điểm lệch, xử lý như sau:**

| Lệch | ORG-v2 (lý thuyết) | Thực tế (agent-core) | Quyết định |
|---|---|---|---|
| Research vs Analytics | Gộp chung ① 1 role | Tách riêng 2 agent | **Giữ tách** — code đã tách sẵn, không việc gì gộp lại. ORG-v2.md cần sửa theo |
| Marketing vs Content | Tách riêng ②④ | Gộp vào `marketing` | **Giữ gộp** — code đã gộp. Bỏ ý định tách trong ORG-v2 |
| Designer vs Media(đăng) | Tách riêng ⑥⑦ | Chỉ có `media` = tạo (không có agent riêng cho việc bấm đăng) | **Không cần agent riêng cho "đăng"** — guardrail người-tạo-≠-người-đăng đã được `DECISION-MATRIX.md` đảm bảo qua approval gate (bấm đăng = L2, bất kể agent nào), không cần tách agent theo tổ chức |
| Ops&Finance vs Dev(healthcheck) | Tách riêng ⑤⑧ | Gộp vào `operations` | **Giữ gộp** — code đã gộp. `dev` chỉ lo code/deploy, không lo healthcheck vận hành hàng ngày nữa |
| Support | Không có role riêng (fold vào Sales+Ops) | Có agent riêng | **Giữ agent riêng `support`** — code đã có, hoạt động tốt hơn ép vào Sales/Ops |
| HR & Admin | Có role ⑨ | **Không có agent nào** | **Gap thật** — xem mục dưới |

## Gap thật: HR & Admin

Không có agent nào quản lý ca trực Fast Track, nhân viên Tano Cafe, hợp đồng. 2 lựa chọn:
- **Khuyến nghị: gộp tạm vào `operations`** (đã có "quản lý đơn/booking/lịch" — mở rộng thêm "quản lý ca trực/nhân sự cơ bản") thay vì build agent thứ 10 ngay. Lý do: khối lượng việc HR hiện tại (32 nhân sự theo dashboard ảnh trước) chưa đủ lớn để cần 1 agent riêng, chi phí build/maintain 1 agent mới cao hơn lợi ích lúc này.
- Khi khối lượng HR tăng (nhiều ca trực, tuyển dụng thường xuyên) → tách `hr-admin` thành agent thứ 10.

---

## Kiến trúc chạy — Local vs VPS, theo dữ liệu thật

Hiện tại **100% chạy Local Windows** (CEO Bot `main.py`, 9 agent, cron qua Hermes). Đây là điểm
khởi đầu thật, không phải lý thuyết. Việc "kết hợp VPS" là **thêm vào**, không phải "chuyển từ
OpenClaw sang" (vì OpenClaw không có gì để chuyển).

**Kế hoạch thêm VPS (sau khi reboot xong):**

| Agent | Giữ Local | Thêm chạy trên VPS | Vì sao |
|---|---|---|---|
| ceo (CEO Bot) | | ✅ Chuyển hẳn sang VPS | Bot Telegram cần luôn online — máy Local tắt là mất kênh nhận lệnh |
| dev | ✅ | | Cần disk/compute lớn, không cần 24/7 |
| research | ✅ | | Nghiên cứu sâu, không cần real-time |
| media | ✅ | | Render video/design nặng, cần dung lượng lớn |
| marketing | ✅ | (cân nhắc sau) | Viết content không cần 24/7, nhưng theo dõi campaign/ads có thể cần |
| sales | | ✅ | CSKH trước bán, chat cần phản hồi nhanh, nên luôn online |
| operations | ✅ (phần dev-healthcheck) | ✅ (phần booking/fulfillment) | Tách theo tính chất: check hạ tầng có thể chạy Local theo lịch, fulfillment đơn cần 24/7 → **cần Nobitano xác nhận có tách được operations thành 2 luồng không, hay giữ nguyên 1 agent chạy VPS toàn bộ** |
| support | | ✅ | CSKH 24/7, bắt buộc luôn online |
| analytics | ✅ | | Chạy report định kỳ, không cần 24/7 |

**Taskboard:** vẫn giữ khuyến nghị Airtable (thay vì SQLite `hq.db` cục bộ) — lý do duy nhất
không đổi: cần 1 nguồn cả Local lẫn VPS cùng đọc/ghi được qua mạng, SQLite không làm được việc
đó khi có 2 máy vật lý khác nhau cùng tham gia.

---

## OpenClaw — khai tử chính thức, không phải "migrate"

- Xác nhận: không có code sống, không có khách hàng phụ thuộc trong phạm vi repo kiểm tra được
- **Việc cần làm:** sau khi VPS reboot, SSH vào chạy `pm2 list` và `ls /opt/openclaw/` — nếu có
  process/thư mục thật tồn tại trên VPS (ngoài phạm vi repo Local) → tắt hẳn, không migrate gì
  cả (không có gì đáng migrate)
- Xoá/archive mọi playbook nhắc OpenClaw như 1 orchestrator độc lập (`OPENCLAW-PLAYBOOK.md` cần
  viết lại hoàn toàn hoặc xoá, tuỳ sau khi SSH xác nhận có gì trên VPS hay không)

---

## Không đổi — vẫn đúng, giữ nguyên

- `DECISION-MATRIX.md` (L0-L3, 3 lằn ranh đỏ) — áp dụng cho cả 9 agent thật, không đổi
- `SENIOR-ADVISOR.md` — đúng nguyên tắc, chỉ sửa: giai đoạn 2 gọi qua **CEO Bot** (agent `ceo`),
  không phải "qua Hermes" (Hermes giờ hiểu là runtime Python chạy 9 agent, không phải 1 thực thể
  ra lệnh)
- `AI-Vibe-Toolkit` kho GitHub — giữ nguyên làm kho skill duy nhất

## Cần sửa

- `ORG-v2.md` — viết lại bảng role theo đúng 9 agent thật ở trên (không phải 9-role lý thuyết cũ)
- `HERMES-PLAYBOOK.md` dòng 16 — xoá "chạy trong OpenClaw trên VPS", sửa "Hermes = runtime Python
  chạy 9 agent trong agent-core, Local Windows, cron tự động, không phụ thuộc OpenClaw"
- `OPENCLAW-PLAYBOOK.md` — chờ kết quả SSH check VPS, sau đó xoá hoặc viết lại hoàn toàn

---

## ⚠️ Chờ xác nhận — chỉ còn 1 việc (2/3 việc trước đã xong)

1. ~~Tên 8 phòng ban thật~~ ✅ Đã có — 9 agent (mục trên)
2. ~~OpenClaw đang chạy gì thật~~ ✅ Đã có — gần như chắc chắn không có gì
3. **VPS cần Nobitano tự reboot** (AI không có quyền SSH/vào provider console theo đúng
   `HERMES-PLAYBOOK.md`) — sau khi lên:
   ```bash
   ssh root@<IP_PUBLIC_THẬT — không phải 100.64.173.75, cần tìm IP public đúng trong provider console>
   systemctl status docker
   docker ps
   pm2 list
   ls /opt/openclaw/ 2>/dev/null && echo "CÓ THƯ MỤC OPENCLAW — cần audit tiếp" || echo "Không có gì"
   ufw status
   curl localhost:8137
   ```
   Kết quả paste lại — tao xác nhận nốt rồi mới cho thực thi Bước "chuyển CEO Bot sang VPS".

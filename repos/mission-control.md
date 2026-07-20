# OpenClaw Mission Control (abhi1693) — GitHub Repo

## TL;DR
Dashboard điều phối AI agent fleet, xây RIÊNG cho OpenClaw Gateway — quản tổ chức/board/task/agent, duyệt hành động nhạy cảm qua approval flow, xem toàn bộ hoạt động 1 chỗ. 4.1K stars, MIT license. Đây gần như đúng chính xác "Airtable company-hq" mà mày đang định tự dựng cho ORG-v2 — có thể thay thế hoặc bổ sung.

## Repo này dùng để làm gì
OpenClaw Mission Control là control plane cho các agent chạy qua OpenClaw Gateway — thay vì tự quản việc điều phối qua Airtable + Telegram thủ công, dashboard này cho:
- **Work orchestration:** tổ chức theo organizations → board groups → boards → tasks → tags —
  khớp gần như 1:1 với mô hình 9 role/domain pack đang có trong `agents/company/ORG-v2.md`.
- **Agent operations:** tạo/xem/quản lý vòng đời agent (Hermes, OpenClaw sub-agent...) từ 1 màn
  hình duy nhất, không phải soát log rải rác từng nơi.
- **Governance & approval:** route hành động nhạy cảm qua approval flow rõ ràng — đúng khớp
  nguyên tắc "3 lằn ranh đỏ" đã có (AI không tự chi tiền, không tự publish, không tự cam kết) —
  giờ có UI thật để CEO duyệt thay vì chỉ optionally nhắn Telegram "OK <job-id>".
- **Gateway-aware orchestration:** vận hành cả môi trường local lẫn kết nối từ xa.
- **Unified UI + API:** operator (CEO) và automation (agent) thao tác trên cùng 1 model dữ liệu.

Repo anh em gần nhất: `builderz-labs/mission-control` (5.8K stars, tổng quát hơn, hỗ trợ thêm
CrewAI/LangGraph/AutoGen/Claude SDK ngoài OpenClaw) — nếu sau này mở rộng dùng thêm framework
khác ngoài Hermes/OpenClaw thì đáng cân nhắc bản này thay vì bản chuyên OpenClaw.

## Setup từng bước
1. Cài 1 lệnh (script tự động clone + cấu hình):
```bash
curl -fsSL https://raw.githubusercontent.com/abhi1693/openclaw-mission-control/master/install.sh | bash
```
2. Script sẽ hỏi chế độ deploy: `docker` hoặc `local` — với VPS Tencent Cloud sẵn có, nên chọn
   Docker để cô lập, tránh xung đột với Hermes/OpenClaw/Antigravity đang chạy pm2.
3. Sau khi cài, dựng cấu trúc: 1 organization (Tano Agency) → board group theo domain (ABTRIP,
   Tano Cafe, Wonder Mart...) → board theo role (9 role đã có) → import task hiện có.
4. Nối OpenClaw Gateway vào Mission Control theo hướng dẫn "Gateway management" trong docs —
   đây là bước bắt buộc để dashboard thấy được agent thật đang chạy trên VPS.

## Ví dụ thực tế
Thay vì tự dựng Airtable `company-hq` base từ đầu (đang là việc tồn đọng trong TRACKER — "Airtable
coordination layer chưa deploy"), dùng thẳng Mission Control: tạo board group cho từng domain
(ABTRIP/An Bình, Tano Cafe...), mỗi role (Research, Sales, Ops&Finance, HR&Admin...) là 1 board
riêng, task từ CEO gõ qua Telegram vẫn route qua OpenClaw như cũ nhưng giờ hiện lên dashboard
thật để theo dõi trạng thái, duyệt approval, và xem chi phí token đã dùng — giải quyết đúng lỗ
hổng "chưa có real job nào test qua 7-role system" đã ghi trong memory.

## Lưu ý / Lỗi thường gặp
- Đây có thể THAY THẾ kế hoạch "Airtable company-hq" đã lên trong ORG-v2, không phải làm thêm
  song song — nên quyết định dứt khoát dùng cái nào trước khi bắt tay setup, tránh 2 nguồn dữ
  liệu trạng thái công ty chạy song song gây lệch.
- Cần nối đúng OpenClaw Gateway — nếu setup sai, dashboard hiển thị nhưng không đồng bộ thật
  với agent đang chạy, dễ gây ảo giác "mọi thứ đang ổn" trong khi thực tế lệch.
- Fork count cao bất thường so với sao (830 fork / 4.1K sao) so với repo builderz-labs (5 fork /
  5.8K sao) — đáng chú ý khi đánh giá độ tin cậy, nên xem qua Issues/PR gần nhất trước khi tin
  tưởng deploy production ngay.
- Repo `builderz-labs/mission-control` còn ghi rõ "Alpha Software — API, database schema, cấu
  hình có thể đổi giữa các bản release" — cả 2 bản đều còn khá mới, backup dữ liệu thường xuyên.

## Đánh giá cá nhân
- Điểm mạnh: giải quyết đúng lỗ hổng đã tồn đọng lâu (coordination layer chưa deploy); build
  riêng cho OpenClaw nên tích hợp gần như không cần custom thêm gì; approval flow có UI thật
  thay vì chỉ nhắn tin Telegram; MIT license, tự host được trên VPS sẵn có.
- Điểm yếu: còn early-stage (cả 2 bản đều mới, API/schema có thể đổi); cần dứt khoát chọn 1
  (Mission Control hay tự dựng Airtable) thay vì làm cả 2; setup ban đầu tốn công nối Gateway.
- Có nên dùng không: 8.5/10 — đây là ứng viên mạnh nhất để thay thế kế hoạch Airtable company-hq
  đang tồn đọng, nên thử nghiệm trước khi tiếp tục tự dựng Airtable từ đầu.

## Link
- Repo (chuyên OpenClaw): https://github.com/abhi1693/openclaw-mission-control
- Repo anh em (tổng quát hơn, đa framework): https://github.com/builderz-labs/mission-control

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Mission Control có REST API thật — Hermes gọi trực tiếp để đọc/ghi task
import urllib.request, json, os

MC_BASE = "http://localhost:3000/api"  # đổi theo domain thật sau khi deploy

def mc_create_task(board_id, title, description, tags=None):
    token = os.environ.get("MISSION_CONTROL_TOKEN")
    payload = {"board_id": board_id, "title": title, "description": description,
               "tags": tags or []}
    req = urllib.request.Request(
        f"{MC_BASE}/tasks",
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST")
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
# Cài Mission Control ngay trên VPS đang chạy OpenClaw
curl -fsSL https://raw.githubusercontent.com/abhi1693/openclaw-mission-control/master/install.sh | bash
# Chọn chế độ docker khi được hỏi, rồi nối Gateway theo docs "Gateway management"
```

### Antigravity
```bash
# Antigravity chịu trách nhiệm deploy + duy trì service này 24/7 qua pm2/docker
cd openclaw-mission-control && docker compose up -d
pm2 startup  # nếu chạy local thay vì docker, đảm bảo tự khởi động lại khi VPS reboot
```
> ⚠️ Quyết định dứt khoát: dùng Mission Control THAY cho kế hoạch Airtable company-hq, không
> chạy song song 2 nguồn trạng thái — báo CEO xác nhận hướng trước khi Antigravity deploy thật.

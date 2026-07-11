---
name: dramaclaw
description: >
  Xưởng phim AI mã nguồn mở: đưa vào manuscript (tiểu thuyết/kịch bản) → tự
  động ra phim ngắn hoàn chỉnh — từ phân tích nhân vật, vẽ storyboard, lồng
  tiếng đến cắt ghép video. Chạy local bằng Docker, không cần GPU, không cần
  studio. 924 stars, v1.0.5, đang active phát triển.
---

# DramaClaw — GitHub Repo

## TL;DR
Xưởng phim AI mã nguồn mở: đưa vào manuscript (tiểu thuyết/kịch bản) → tự động ra phim ngắn hoàn chỉnh — từ phân tích nhân vật, vẽ storyboard, lồng tiếng đến cắt ghép video. Chạy local bằng Docker, không cần GPU, không cần studio. 924 stars, v1.0.5, đang active phát triển.

## Repo này dùng để làm gì

DramaClaw là pipeline sản xuất phim tự động hóa hoàn toàn. Mày đưa vào 1 file manuscript (truyện, kịch bản), nó tự làm hết:

1. **Parse manuscript** — trích xuất nhân vật, timeline, quan hệ thành knowledge graph
2. **Lên kế hoạch tập** — phân chương, chia beat, arc đa tập
3. **Sinh script** — nhiều mode: adaptive, literal, staged; có vòng review + sửa tự động
4. **Vẽ storyboard + first frame** — sinh ảnh theo beat, giữ visual consistency xuyên suốt
5. **Lồng tiếng** — emotion-aware TTS, đổi provider được
6. **Ghép video + export** — ra file video + subtitle + full asset pack

Không chỉ làm phim ngắn — pipeline tương tự apply được cho: quảng cáo ngắn, video product e-commerce, otome game tương tác.

Điểm độc đáo nhất: **"Freezone"** — canvas node-based để thử nghiệm assets song song với pipeline chính. Và **Director World (3GS)** — virtual set giữ nguyên spatial structure, camera placement nhất quán qua các cảnh.

## Setup từng bước

### Cách nhanh nhất — Docker (khuyên dùng)

```bash
git clone https://github.com/dramaclaw/dramaclaw.git
cd dramaclaw
cp .env.example .env
# Mở .env, set PROMPT_EXPORT_PASSWORD và NEWAPI_BASE_URL
docker compose up -d --build
```

Mở browser: `http://localhost:8080` (web UI) và `http://localhost:8780` (REST API).

Vào **Settings → Model Config → Official** → paste DC key (lấy tại relayclaw.cdnfg.com).

### Không cần build — dùng release image có sẵn

```bash
curl -LO https://raw.githubusercontent.com/dramaclaw/dramaclaw/main/docker-compose.release.yml
docker compose -f docker-compose.release.yml up -d
```

### Local dev (không Docker)

```bash
git clone https://github.com/dramaclaw/dramaclaw.git
cd dramaclaw
uv sync
cp .env.example .env
uv run novelvideo api --port 8780
```
Cần: Python 3.11–3.12 + `uv` + `ffmpeg`.

### Yêu cầu tối thiểu

| Thứ | Yêu cầu |
|-----|---------|
| CPU/RAM | 2 vCPU / 4GB (inference chạy remote, không phải local) |
| GPU | Không cần (trừ khi dùng 3D world model) |
| OS | macOS, Windows (WSL2), Linux |
| Docker | Bắt buộc cho cách nhanh |
| Database | Không cần — SQLite + file system là đủ |

## Ví dụ thực tế

**Use case cho Tano Agency / ABTRIP:**

Input: Kịch bản ngắn về hành trình du lịch Đà Nẵng — 3 nhân vật, 5 cảnh.

Pipeline tự động:
1. Parse → trích xuất 3 nhân vật, 5 location, timeline
2. Sinh 5 storyboard frame (style: cinematic travel)
3. Lồng tiếng bằng ElevenLabs-compatible TTS
4. Export video ~60s + subtitle file

Kết quả: video promo travel không cần quay thật, không cần diễn viên, không cần hậu kỳ thủ công — chạy một mình trên VPS 4GB RAM.

## Lưu ý / Lỗi thường gặp

- **Cần DC key** để gọi model gateway (relayclaw.cdnfg.com) — không phải hoàn toàn free; hoặc tự BYO endpoint OpenAI-compatible.
- **License Elastic 2.0** — không phải MIT. Không được dùng để build competing SaaS; dùng internal hoặc self-host thì OK.
- **Video quality phụ thuộc vào model image/video** nối vào gateway — nếu dùng model yếu thì output kém.
- **3D World Model (3GS)** cần GPU + CUDA image — tính năng này không chạy được trên VPS thường.
- **Port conflicts** — mặc định chiếm 8080, 8780, 3000. Nếu đang chạy n8n (5678) hoặc service khác, cần check trước.
- **RAM VPS** — nếu Tencent Cloud VPS đang dùng full RAM cho Hermes/OpenClaw, cần tính toán trước khi deploy thêm DramaClaw.

## Đánh giá cá nhân

- **Điểm mạnh:** Pipeline hoàn chỉnh nhất hiện tại cho AI video production — từ text đến film, không phải chắp vá nhiều tool. Freezone + Director World là 2 tính năng không thấy ở đâu khác. Self-hostable, không lock-in cloud.
- **Điểm yếu:** License Elastic 2.0 hạn chế commercial use dạng SaaS. Phụ thuộc gateway bên ngoài (relayclaw) cho model — nếu service này down thì pipeline stop. Còn v1.0.5, một số tính năng chưa stable. Tài liệu chủ yếu tiếng Trung.
- **Có nên dùng không:** 8/10 — cực kỳ phù hợp cho content factory của Tano. Use case ABTRIP travel video promo là match 100%. Nhưng cần VPS riêng (RAM constraint hiện tại) và cần test kỹ gateway trước khi production.

## Link

- Repo: https://github.com/dramaclaw/dramaclaw
- Docs: https://github.com/dramaclaw/dramaclaw/tree/main/docs/en
- Demo films: https://www.bilibili.com/video/BV1iQV26cE4S
- Gateway/Key: https://relayclaw.cdnfg.com

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

# Trigger DramaClaw pipeline qua REST API
DRAMACLAW_API = "http://localhost:8780"

def create_project(manuscript_text, title):
    payload = {
        "title": title,
        "manuscript": manuscript_text,
        "mode": "adaptive"
    }
    req = urllib.request.Request(
        f"{DRAMACLAW_API}/api/projects",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    return json.loads(urllib.request.urlopen(req).read())

def get_project_status(project_id):
    req = urllib.request.Request(
        f"{DRAMACLAW_API}/api/projects/{project_id}/status")
    return json.loads(urllib.request.urlopen(req).read())

# Dùng: Hermes nhận kịch bản từ Telegram → push vào DramaClaw → poll status → báo kết quả
```

### OpenClaw
```bash
# DramaClaw expose REST API tại port 8780
# OpenClaw gọi thẳng endpoint, không cần MCP
curl -X POST http://localhost:8780/api/projects \
  -H "Content-Type: application/json" \
  -d '{"title": "ABTRIP-Da-Nang", "manuscript": "...", "mode": "adaptive"}'
```

### Antigravity
```bash
# Deploy DramaClaw trên VPS riêng (cần ít nhất 4GB RAM)
git clone https://github.com/dramaclaw/dramaclaw.git
cd dramaclaw
cp .env.example .env
# Set DC key trong .env
pm2 start "docker compose up -d" --name dramaclaw
# Hoặc dùng systemd service để auto-restart
```

> ⚠️ Tencent Cloud VPS hiện tại đang chạy Hermes + OpenClaw + Antigravity — RAM có thể không đủ để thêm DramaClaw. Cần VPS riêng 4GB+ hoặc dọn RAM trước. Xem ticket Chatwoot trong ANTIGRAVITY-PLAYBOOK.md để tham khảo cách handle RAM constraint.

---
name: qdrant
description: >
  Vector database self-host hieu suat cao, viet bang Rust — luu du lieu dang
  embedding de tim kiem theo ngu nghia (semantic search), phuc vu RAG va
  long-term memory cho AI agent. Va dung lo hong RIO Bot dang thieu: hien tai
  RIO Bot chi co SQLite (relational, match chu dung), khong tim duoc thu
  "gan giong nghia" nhau.
---

# Qdrant — GitHub Repo

## TL;DR
Vector database self-host, viết bằng Rust, 1 lệnh Docker là chạy được. Lưu dữ liệu dạng embedding (vector số hoá ý nghĩa câu chữ) để tìm theo *ngữ nghĩa* thay vì match chữ đúng như SQL — đúng thứ RIO Bot đang thiếu (kho đã note: "RIO Bot thiếu vector store layer, chỉ có SQLite relational, không có semantic search").

## Repo này dùng để làm gì
Khi mày cần AI agent "nhớ" theo nghĩa chứ không phải theo chữ — vd RIO Bot hỏi "khách hay hỏi gì về SIM du lịch" thì nó phải tìm ra được cả những đoạn hội thoại cũ nói ý tương tự dù không dùng đúng từ "SIM du lịch". Cách làm: embed text (biến câu chữ thành vector số bằng model embedding — OpenAI, Gemini, hoặc local model qua OmniRoute), lưu vector đó vào Qdrant, sau đó query "top-k gần nhất" để lấy ra context liên quan nhất.

Dùng cho: RAG (agent trả lời dựa trên tài liệu công ty), long-term memory cho bot (RIO Bot, OpenClaw), semantic search cho content kho (tìm entry cũ theo ý nghĩa thay vì đúng từ khoá).

## Setup từng bước
1. Chạy container (persist volume để không mất data khi restart):
```bash
docker run -p 6333:6333 -p 6334:6334 \
  -v $(pwd)/qdrant_storage:/qdrant/storage \
  qdrant/qdrant
```
2. Set API key khi expose ra ngoài VPS (mặc định KHÔNG auth, ai cũng query được nếu mở port):
```bash
docker run -p 6333:6333 \
  -e QDRANT__SERVICE__API_KEY=your-secret-key \
  -v $(pwd)/qdrant_storage:/qdrant/storage \
  qdrant/qdrant
```
3. Tạo collection (REST API, dùng cho RIO Bot memory):
```bash
curl -X PUT http://localhost:6333/collections/rio-memory \
  -H 'Content-Type: application/json' \
  -d '{"vectors": {"size": 1536, "distance": "Cosine"}}'
```
4. Insert + query bằng Python client (`pip install qdrant-client --break-system-packages`).

## Ví dụ thực tế
RIO Bot nhận tin nhắn Telegram → gọi OmniRoute lấy embedding (vd Gemini embedding model) → lưu vector + text gốc vào collection `rio-memory` kèm metadata (timestamp, user_id) → lần sau user hỏi câu tương tự, RIO Bot query top-5 gần nhất trong Qdrant → đưa context đó vào prompt trước khi trả lời. Kết quả: bot nhớ được ngữ cảnh cũ dù câu hỏi diễn đạt khác đi.

## Lưu ý / Lỗi thường gặp
- Port 6333 mặc định KHÔNG có auth → bắt buộc set `QDRANT__SERVICE__API_KEY` nếu VPS có IP public (Tencent Cloud của mày đang expose port thì check lại ngay).
- Quên mount volume → restart container là mất sạch data, phải mount `/qdrant/storage` ra ngoài.
- RAM cần đủ: ước lượng thô = số vector × chiều vector × 4 byte × ~1.5 (overhead index). Với vài chục nghìn hội thoại RIO Bot, VPS hiện tại thừa sức.
- Không có LLM built-in — Qdrant chỉ lưu/tìm vector, mày vẫn phải tự gọi model embedding qua OmniRoute trước khi insert.

## Đánh giá cá nhân
- Điểm mạnh: nhẹ, nhanh (Rust), setup 1 dòng Docker, client Python/Node dễ dùng, đủ mọi tính năng cần cho RAG cỡ nhỏ-vừa.
- Điểm yếu: không có UI quản lý mạnh như Weaviate; không tích hợp sẵn embedding model — phải tự nối với OmniRoute.
- Có nên dùng không: **8.5/10** — đúng công cụ vá lỗ hổng RIO Bot đang note trong kho, không có lý do không dùng.

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Hermes chỉ dùng urllib, không dùng requests/qdrant-client SDK
import urllib.request, json

QDRANT_URL = "http://localhost:6333"
API_KEY = "[QDRANT_API_KEY]"

def qdrant_upsert(collection, point_id, vector, payload):
    body = json.dumps({"points": [{"id": point_id, "vector": vector, "payload": payload}]}).encode()
    req = urllib.request.Request(
        f"{QDRANT_URL}/collections/{collection}/points",
        data=body, method="PUT",
        headers={"Content-Type": "application/json", "api-key": API_KEY})
    return json.loads(urllib.request.urlopen(req).read())

def qdrant_search(collection, vector, top_k=5):
    body = json.dumps({"vector": vector, "limit": top_k}).encode()
    req = urllib.request.Request(
        f"{QDRANT_URL}/collections/{collection}/points/search",
        data=body, method="POST",
        headers={"Content-Type": "application/json", "api-key": API_KEY})
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
# Chạy song song container qua VPS, gọi thẳng REST API từ Node.js orchestrator
docker compose up -d qdrant
# fetch trong OpenClaw giống fetchKho() pattern hiện có, đổi endpoint sang http://localhost:6333
```

### Antigravity
```bash
# Deploy Qdrant như 1 service PM2/systemd riêng trên VPS Tencent Cloud
docker run -d --name qdrant --restart unless-stopped \
  -p 6333:6333 \
  -e QDRANT__SERVICE__API_KEY=[QDRANT_API_KEY] \
  -v /opt/qdrant_storage:/qdrant/storage \
  qdrant/qdrant
```
> ⚠️ Nhớ mở firewall Tencent Cloud CHỈ cho port 6333 nếu cần truy cập ngoài — mặc định nên bind localhost và để Hermes/OpenClaw gọi nội bộ qua Tailscale IP (100.64.173.75) thay vì public IP.

## Link
- Repo: https://github.com/qdrant/qdrant
- Docs: https://qdrant.tech/documentation/
- License: Apache-2.0

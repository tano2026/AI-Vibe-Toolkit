# Airweave — GitHub Repo

## TL;DR
Airweave là "lớp truy xuất context" cho AI agent — nối vào 50+ nguồn dữ liệu (Drive, Notion, Slack, GitHub, CRM...) rồi cho agent search qua 1 API duy nhất, thay vì phải tự viết integration riêng cho từng nguồn. 5.7K stars, YC-backed.

## Repo này dùng để làm gì
Vấn đề nó giải quyết: agent của mày cần đọc data từ nhiều nơi (Google Drive, GitHub, Notion, Slack...) để trả lời chính xác. Bình thường phải tự viết connector cho từng app, tự đồng bộ, tự embed. Airweave làm hộ hết:
1. Nối vào nguồn data (OAuth hoặc API key)
2. Nó tự đồng bộ liên tục (incremental sync bằng content hashing — không re-index lại toàn bộ)
3. Agent chỉ cần gọi 1 API search → có ngay context liên quan từ tất cả nguồn đã nối, kèm semantic search + hybrid search (semantic + keyword) + reranking

Khác RAG tự chế ở điểm: RAG thường phải build pipeline riêng cho mỗi app, Airweave là lớp chia sẻ dùng chung cho nhiều agent.

## Setup từng bước
1. Self-host bằng Docker (yêu cầu Docker + docker-compose):
```bash
git clone https://github.com/airweave-ai/airweave.git
cd airweave
chmod +x start.sh
./start.sh
# → http://localhost:8080
```
2. Hoặc dùng bản cloud tại app.airweave.ai (nhanh hơn, không cần tự host)
3. Vào UI nối nguồn data (Drive, Notion, Slack...), set OAuth hoặc API key
4. Cài SDK để agent gọi:
```bash
pip install airweave-sdk
```
5. Query từ code:
```python
from airweave import AirweaveSDK
client = AirweaveSDK(api_key="YOUR_API_KEY")
results = client.collections.search.instant(
    readable_id="my-collection",
    query="Tìm booking ABTRIP bị fail thanh toán gần đây"
)
```

## Ví dụ thực tế
Research Pro của tao đang cần gộp nhiều nguồn (Drive lưu research cũ, GitHub kho AI-Vibe-Toolkit, có thể sau này thêm Notion) thành 1 lớp truy vấn chung cho agent, tránh mỗi agent tự viết lại logic đọc Drive/GitHub riêng. Airweave nối GitHub + Drive 1 lần, sau đó Hermes chỉ cần gọi `client.collections.search.instant(query=...)` là có context từ cả 2 nguồn, không cần biết data nằm ở đâu.

## Lưu ý / Lỗi thường gặp
- **Stack nặng hơn tưởng** — Postgres (metadata) + Vespa (vector) + Temporal (orchestration workers) + Redis, không phải 1 container đơn giản. VPS Tencent Cloud hiện tại (đang gặp RAM constraint với Chatwoot) cần tính RAM kỹ trước khi thêm Airweave vào.
- **CLI ngoài SDK** — có `airweave-cli` riêng để search từ terminal, tiện cho Antigravity test nhanh không cần viết code.
- **5.7K stars còn khá non** so với Firecrawl/Ollama — ecosystem tích hợp (skills, MCP) còn đang phát triển, đọc docs kỹ hơn khi tích hợp sâu.
- **OAuth setup cho mỗi nguồn** hơi lằng nhằng lúc đầu (mỗi app cần app riêng trên Google/Slack Developer Console) nhưng làm 1 lần xong.

## Đánh giá cá nhân
- **Điểm mạnh:** Đúng bài toán "agent ecosystem cần context từ nhiều nguồn" mà kho AI-Vibe-Toolkit đang gặp — thay vì Hermes tự viết logic đọc từng nguồn, tập trung hết vào 1 layer. Encrypt AES-256, hỗ trợ MCP native nên cắm được vào Claude Desktop/OpenClaw luôn.
- **Điểm yếu:** Stack hạ tầng nặng (4 service chạy cùng lúc), không hợp nếu VPS đang tight RAM. Còn non so với các tool RAG khác, ít case study thực tế production quy mô lớn.
- **Có nên dùng không:** 7/10 — hay nhưng nên cân nhắc timing, đợi giải quyết xong RAM constraint (Chatwoot) trước khi thêm 1 stack nặng nữa lên VPS. Có thể để ở dạng "biết, note lại" trước khi triển khai.

## Link
- Repo: https://github.com/airweave-ai/airweave
- Docs: https://docs.airweave.ai
- Cloud: https://app.airweave.ai

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

AIRWEAVE_KEY = "YOUR_API_KEY"
AIRWEAVE_URL = "http://localhost:8080"  # hoặc app.airweave.ai nếu dùng cloud

def airweave_search(collection, query):
    payload = json.dumps({"query": query}).encode()
    req = urllib.request.Request(
        f"{AIRWEAVE_URL}/collections/{collection}/search/instant",
        data=payload,
        headers={
            "Authorization": f"Bearer {AIRWEAVE_KEY}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    return json.loads(urllib.request.urlopen(req).read())

context = airweave_search("research-pro-sources", "quy trình xử lý input AI Vibe Toolkit")
```

### OpenClaw
```bash
# Airweave hỗ trợ MCP native — cắm trực tiếp vào OpenClaw như 1 tool
# Thêm vào config MCP server của OpenClaw: point tới http://<vps-ip>:8080/mcp
```

### Antigravity
```bash
# Deploy self-host trên VPS Tencent Cloud
git clone https://github.com/airweave-ai/airweave.git
cd airweave && chmod +x start.sh && ./start.sh
```
> ⚠️ Kiểm tra RAM VPS trước khi deploy — stack gồm Postgres + Vespa + Temporal + Redis, nặng hơn Chatwoot. Nên đợi có VPS riêng hoặc mở rộng RAM trước.

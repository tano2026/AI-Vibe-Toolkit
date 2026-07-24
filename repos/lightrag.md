# LightRAG — GitHub Repo

## TL;DR
Framework RAG kết hợp knowledge graph + vector embedding, nhẹ và nhanh hơn Microsoft GraphRAG. 38k+ sao, được HKU nghiên cứu, đã publish tại EMNLP2025 — một trong những repo RAG được cite/dùng nhiều nhất hiện nay.

## Repo này dùng để làm gì
RAG (Retrieval-Augmented Generation) thường thì: mày nhét tài liệu vào, hệ thống tách chunk, tạo vector, rồi search bằng similarity — nhưng cách này mất hết quan hệ giữa các thực thể (entity) trong tài liệu. LightRAG giải quyết bằng kiến trúc "2 tầng": vừa dựng knowledge graph (ai liên quan tới ai, cái gì thuộc về cái gì) VỪA giữ vector embedding song song — khi cần trả lời câu hỏi phức tạp kiểu "X liên quan gì tới Y qua Z", nó tra được qua đồ thị thay vì chỉ dò tương đồng văn bản.

Điểm mạnh nhất: update tăng dần (incremental). Có tài liệu mới vào không cần rebuild lại toàn bộ index như GraphRAG — nó tự merge đồ thị con mới vào đồ thị đang có, xoá tài liệu cũng tự rebuild lại quan hệ liên quan nhanh nhờ cache LLM từ lúc build ban đầu. Từ bản v1.5 hỗ trợ luôn tài liệu đa phương thức (ảnh, bảng trong PDF/DOCX qua MinerU/Docling).

## Setup từng bước
1. Cài công cụ quản lý package `uv` (khuyến nghị thay vì pip thuần):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. Cài server LightRAG từ PyPI:
   ```bash
   uv tool install "lightrag-hku[api]"
   ```
3. Build front-end (nếu cần dùng Web UI quản lý knowledge base):
   ```bash
   cd lightrag_webui
   bun install --frozen-lockfile
   bun run build
   cd ..
   ```
4. Copy file cấu hình mẫu và điền API key LLM/embedding của mày:
   ```bash
   cp env.example .env  # điền LLM + embedding config vào đây
   ```
5. Chạy server (mặc định bind mọi interface `0.0.0.0` — **BẮT BUỘC** cấu hình `LIGHTRAG_API_KEY` hoặc `AUTH_ACCOUNTS`+`TOKEN_SECRET` trong `.env` trước khi expose ra mạng, không thì mọi endpoint public hoàn toàn):
   ```bash
   lightrag-server
   ```
6. Nếu build từ source thay vì PyPI: `git clone` -> `make dev` -> `source .venv/bin/activate`.

## Ví dụ thực tế
Áp cho RIO Bot (CORE-BRAIN) — hiện đang chạy pipeline SQLite + DDG search local. Nếu muốn RIO Bot trả lời được câu hỏi kiểu "công ty X có liên quan gì tới sự kiện Y đã research tuần trước không", SQLite thuần không tra được quan hệ này. Có thể dùng LightRAG làm lớp lưu trữ tri thức tích luỹ cho RIO Bot: mỗi lần research xong nạp kết quả vào LightRAG, sau này hỏi lại nó tự nối được các entity qua đồ thị thay vì chỉ search từ khoá lại từ đầu.

## Lưu ý / Lỗi thường gặp
- Mặc định bind `0.0.0.0` không auth — nếu deploy trên VPS Tencent Cloud mà quên set `LIGHTRAG_API_KEY`, ai cũng gọi được endpoint. Đây là lỗi bảo mật hay gặp nhất khi mới cài.
- Route `/api/*` tương thích Ollama mặc định vẫn mở public dù đã bật auth chỗ khác — phải set thêm `WHITELIST_PATHS=/health` nếu muốn khoá luôn route này.
- Cần chọn `graph_storage` phù hợp quy mô: mặc định NetworkX (nhẹ, hợp dev/test), nhưng production nên đổi sang Neo4J hoặc PostgreSQL (pgvector + Apache AGE) — PostgreSQL gọn nhất, đóng gói được dưới 40MB.

## Đánh giá cá nhân
- Điểm mạnh: update tăng dần không cần rebuild toàn bộ (tiết kiệm token/thời gian rất nhiều so với GraphRAG); hỗ trợ đa backend storage (NetworkX/Neo4J/PostgreSQL) nên scale được từ dev tới production; cộng đồng cực lớn (38k sao, publish chính thức tại EMNLP2025) nên bug được fix nhanh.
- Điểm yếu: cấu hình ban đầu hơi nhiều bước (uv + bun cho web UI + env file) so với 1 vector DB đơn giản; nếu chỉ cần search văn bản thuần không cần quan hệ phức tạp thì dùng LightRAG là overkill, tốn thêm chi phí LLM để build graph.
- Có nên dùng: 8/10 — rất đáng dùng nếu kho tri thức (AI-Vibe-Toolkit hoặc RIO Bot) cần trả lời câu hỏi có quan hệ chéo giữa nhiều entry, không cần thiết nếu chỉ search từ khoá đơn giản như hiện tại.

## Link
- Repo: https://github.com/HKUDS/LightRAG
- Paper (arXiv): https://arxiv.org/abs/2410.05779
- PyPI: https://pypi.org/project/lightrag-hku/

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# LightRAG có REST API riêng khi chạy lightrag-server — gọi thẳng bằng urllib
import urllib.request, json

LIGHTRAG_URL = "http://127.0.0.1:9621"  # đổi theo host thật
LIGHTRAG_API_KEY = "[LIGHTRAG_API_KEY]"

def lightrag_query(question, mode="hybrid"):
    payload = json.dumps({"query": question, "mode": mode}).encode()
    req = urllib.request.Request(
        f"{LIGHTRAG_URL}/query", data=payload,
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {LIGHTRAG_API_KEY}"})
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
uv tool install "lightrag-hku[api]"
cp env.example .env   # điền LLM/embedding config trỏ về OmniRoute gateway
lightrag-server &     # chạy nền, quản lý bằng pm2
```

### Antigravity
```bash
pm2 start "lightrag-server" --name lightrag
pm2 save
```
> ⚠️ Bắt buộc set `LIGHTRAG_API_KEY` trong `.env` trước khi mở port ra ngoài VPS — mặc định không auth, ai cũng đọc/ghi được knowledge base.

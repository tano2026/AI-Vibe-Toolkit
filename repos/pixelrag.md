# PixelRAG — GitHub Repo

## TL;DR
PixelRAG bỏ qua bước parse HTML/PDF ra text — nó chụp màn hình cả trang rồi tìm kiếm/trả lời trực tiếp trên ảnh, nên bảng giá, biểu đồ, layout phức tạp không bị "vỡ cấu trúc" như cách RAG text truyền thống hay gặp. Đi kèm 1 skill Claude Code tên `pixelbrowse` cho phép Claude "nhìn" trang web bằng ảnh thay vì đọc HTML thô.

## Repo này dùng để làm gì
RAG (Retrieval-Augmented Generation) kiểu cũ scrape trang web ra text rồi nhét vào vector DB — cách này làm mất hết bảng, biểu đồ, bố cục. PixelRAG (từ Berkeley Sky Computing Lab, BAIR, Berkeley NLP) làm ngược lại: chụp trang thành các "tile" ảnh, dùng model vision (`Qwen3-VL-Embedding-2B`, đã fine-tune LoRA) để embed và tìm kiếm trên ảnh đó. Theo paper của họ, cách này chính xác hơn RAG text trên cả 6 benchmark test, và với agent thì tiết kiệm token cực mạnh (3.6 triệu token prompt so với 37.5 triệu của RAG text truyền thống trong benchmark của họ).

Repo có 3 phần tách rời, dùng phần nào cũng được:
1. **`pixelshot`** — lệnh CLI chụp 1 trang web hoặc PDF thành ảnh tile (dùng Playwright/Chromium).
2. **`pixelrag` pipeline** — chunk → embed → build FAISS index → serve API tìm kiếm (cần GPU cho model embedding).
3. **`pixelbrowse` skill** — plugin cho Claude Code, để Claude tự chụp ảnh trang rồi "đọc" ảnh đó thay vì fetch HTML.

Ngoài ra có 1 API hosted sẵn (`api.pixelrag.ai`) index sẵn 8.28 triệu trang Wikipedia, gọi thẳng không cần setup gì.

## Setup từng bước

**Cách nhẹ nhất — chỉ dùng `pixelshot` để chụp ảnh:**
```bash
pip install pixelrag --break-system-packages
pixelshot https://en.wikipedia.org/wiki/Python --output ./tiles
```

**Cài skill `pixelbrowse` cho Claude Code (không cần clone repo):**
```bash
pip install pixelrag
claude plugin marketplace add StarTrail-org/PixelRAG
claude plugin install pixelbrowse@pixelrag-plugins
```
Sau đó dùng luôn:
```bash
claude -p "screenshot https://vidu.com và tóm tắt bảng giá"
# hoặc trong session: /screenshot https://example.com
```

**Gọi API hosted có sẵn (không cần cài gì):**
```bash
curl -X POST https://api.pixelrag.ai/search \
  -H "Content-Type: application/json" \
  -d '{"queries": [{"text": "What is the capital of France?"}], "n_docs": 5}'
```

**Tự build index riêng (nặng, cần GPU):**
```bash
pip install 'pixelrag[index]'
cat > pixelrag.yaml << 'EOF'
source:
  type: local
  path: ./my_docs
embed:
  model: Qwen/Qwen3-VL-Embedding-2B
  device: cuda
output: ./my_index
EOF
pixelrag index build
pixelrag serve --index-dir ./my_index --port 30001
```

## Ví dụ thực tế
Tình huống: research đối thủ Fast Track cho ABTRIP/An Bình — trang giá dịch vụ của đối thủ trình bày dạng bảng lồng (nhiều gói, nhiều sân bay, ghi chú nhỏ). Scrape bằng Firecrawl/text-based RAG như đang dùng trong `research-analytics-pro` thường làm rối thứ tự cột, mất luôn ghi chú footnote gắn với ô bảng.

Dùng `pixelshot` chụp trang đó thành ảnh tile, feed thẳng ảnh vào Claude (qua skill `pixelbrowse` hoặc gắn ảnh vào context) — Claude đọc bảng giống hệt cách mắt người đọc, giữ đúng hàng/cột/ghi chú. Không cần embed/index gì cả cho việc này, chỉ cần bước render.

## Lưu ý / Lỗi thường gặp
- **Hermes không cài được trực tiếp** — nguyên tắc của Hermes là chỉ dùng `urllib.request`, không pip install thư viện ngoài. `pixelrag`/`pixelshot` là package Python cần pip install nên không đưa thẳng vào Hermes được. Đường vòng: Hermes gọi hosted API `api.pixelrag.ai` bằng `urllib.request` thuần — không cần cài gì, chỉ dùng được cho search Wikipedia index có sẵn.
- **Full pipeline index cần GPU** — model `Qwen3-VL-Embedding-2B` chạy tốt trên GPU/Apple Silicon; build index từ tài liệu riêng trên máy không GPU sẽ rất chậm hoặc không khả thi. VPS Tencent Cloud (Ubuntu, không GPU) hiện tại chỉ phù hợp dùng phần `pixelshot` (render ảnh), không phù hợp tự build index riêng.
- `pixelshot` cần Chromium — trên Linux x64 tự cài headless_shell, các OS khác cần Chrome/Playwright có sẵn hoặc set `CHROME_PATH`.
- `train/` là project uv riêng biệt (torch, transformers ghim phiên bản cụ thể) — không liên quan tới việc dùng thư viện chính, chỉ cần khi muốn tự fine-tune.
- Hosted API `api.pixelrag.ai` chỉ index sẵn Wikipedia — muốn search trên site/tài liệu riêng của mình bắt buộc phải tự build index.

## Đánh giá cá nhân
- **Điểm mạnh:** Ý tưởng "search bằng ảnh thay vì text" giải quyết đúng cái đau của research pipeline hiện tại — trang có bảng/biểu đồ phức tạp. Phần `pixelbrowse` skill cho Claude Code là thứ dùng được ngay, không cần hạ tầng gì thêm, và đúng gu vibe coder: cài 1 dòng, dùng luôn.
- **Điểm yếu:** Phần mạnh nhất của repo (tự build index + search vector) đòi hỏi GPU-class model, không hợp với hạ tầng VPS hiện tại (Ubuntu không GPU). Hosted API chỉ có Wikipedia nên không dùng được để search nội bộ kho `AI-Vibe-Toolkit` hay dữ liệu ABTRIP. Repo còn khá non (mới trending từ tháng 6/2026), API/CLI có thể còn đổi.
- **Có nên dùng không:** 7/10 — không dùng full pipeline vội, nhưng skill `pixelbrowse` đáng cài ngay cho việc research thủ công (đọc trang đối thủ có bảng giá/dashboard phức tạp).

## Link
- Repo: https://github.com/StarTrail-org/PixelRAG
- Docs/Demo: https://pixelrag.ai
- Paper: https://github.com/StarTrail-org/PixelRAG/blob/main/assets/pixelrag-paper.pdf

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Gọi thẳng hosted API — không cần pip install pixelrag gì cả
import urllib.request, json

def pixelrag_search(query, n_docs=5):
    url = "https://api.pixelrag.ai/search"
    payload = json.dumps({"queries": [{"text": query}], "n_docs": n_docs}).encode()
    req = urllib.request.Request(url, data=payload,
        headers={"Content-Type": "application/json"}, method="POST")
    return json.loads(urllib.request.urlopen(req).read())

# Dùng khi RIO Bot/Hermes cần tra cứu nhanh Wikipedia mà muốn giữ context ảnh gốc
result = pixelrag_search("Nội Bài International Airport")
```

### OpenClaw
```bash
# Cài pixelshot trên VPS (không cần GPU, chỉ để render ảnh)
pip install pixelrag --break-system-packages

# OpenClaw shell-exec pixelshot khi cần chụp 1 trang phức tạp (bảng giá đối thủ, dashboard)
# rồi feed ảnh output vào context thay vì scrape text qua browser access sẵn có
pixelshot https://doi-thu.com/bang-gia --output /tmp/tiles
```

### Antigravity
```bash
# Setup pixelbrowse cho Claude Code trên máy Windows local — dùng lúc research thủ công
pip install pixelrag
claude plugin marketplace add StarTrail-org/PixelRAG
claude plugin install pixelbrowse@pixelrag-plugins
```
> ⚠️ KHÔNG deploy full indexing pipeline (`pixelrag index build`) lên VPS Tencent Cloud hiện tại — cần GPU-class model, VPS đang chạy Ubuntu không GPU. Chỉ dùng phần `pixelshot` (render ảnh) hoặc hosted API.

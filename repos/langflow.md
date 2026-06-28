# Langflow — GitHub Repo

## TL;DR
Visual builder để tạo AI agent và workflow — kéo thả component, không cần code. 150K stars, một trong những repo AI phổ biến nhất GitHub. Thay thế n8n nhưng chuyên sâu về AI pipeline hơn.

## Repo này dùng để làm gì
Langflow là low-code platform để build AI workflow bằng giao diện kéo thả. Mày connect các block lại với nhau: LLM → tool → memory → output. Phù hợp cho:
- Build chatbot có RAG (Retrieval-Augmented Generation)
- Tạo multi-agent pipeline không cần code
- Prototype AI app nhanh trước khi code thật
- Deploy API endpoint từ workflow vừa build

Khác với n8n (general automation), Langflow focus 100% vào AI — có sẵn component cho vector store, embedding, LLM, agent, memory.

## Setup từng bước
```bash
# Option 1: pip (nhanh nhất)
pip install langflow
langflow run
# Truy cập: http://localhost:7860

# Option 2: Docker
docker run -p 7860:7860 langflowai/langflow:latest

# Option 3: uv (khuyến nghị cho production)
uv pip install langflow
uv run langflow run
```

**Dùng Langflow Cloud (không cần self-host):**
Vào langflow.new → đăng ký → dùng ngay, free tier có sẵn.

## Ví dụ thực tế
**Build RAG chatbot cho tài liệu nội bộ:**
1. Kéo block: File Loader → Text Splitter → OpenAI Embeddings → Chroma Vector Store
2. Thêm: Chat Input → OpenAI LLM → Chat Output
3. Connect các block → click Deploy → có API endpoint ngay
4. Tích hợp endpoint vào web app hoặc Telegram bot

Không viết một dòng Python.

## Lưu ý / Lỗi thường gặp
- RAM tốn khi chạy local với nhiều model — cần ít nhất 8GB RAM
- Free tier Langflow Cloud có giới hạn execution — self-host nếu dùng nhiều
- Một số component experimental, API hay thay đổi giữa versions
- Export flow ra JSON để backup — UI không có auto-save mạnh

## Đánh giá cá nhân
- Điểm mạnh: Visual, dễ hiểu; 150K stars = community lớn, nhiều template; deploy API một click; tích hợp được mọi LLM
- Điểm yếu: Performance chậm hơn code thuần; debug khó khi flow phức tạp; dependency nặng
- Có nên dùng không: **8.5/10** — Perfect để prototype AI workflow nhanh. Nếu mày build agent mà không muốn code từ đầu, đây là điểm khởi đầu tốt nhất.

## Link
- Repo: https://github.com/langflow-ai/langflow
- Docs: https://docs.langflow.org
- Cloud: https://langflow.new

---

## 🤖 Agent Integration

> Section này dành cho Hermes/OpenClaw/Antigravity.

### Hermes (Python)
```python
import urllib.request, json

LANGFLOW_URL = "http://localhost:7860"

def langflow_run_flow(flow_id, inputs, tweaks=None):
    payload = {"input_value": inputs.get("input", ""),
               "input_type": "chat", "output_type": "chat",
               "tweaks": tweaks or {}}
    req = urllib.request.Request(
        f"{LANGFLOW_URL}/api/v1/run/{flow_id}?stream=false",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}
    )
    r = json.loads(urllib.request.urlopen(req).read())
    return r["outputs"][0]["outputs"][0]["results"]["message"]["text"]

def langflow_list_flows():
    req = urllib.request.Request(f"{LANGFLOW_URL}/api/v1/flows/")
    r = json.loads(urllib.request.urlopen(req).read())
    return [{"id": f["id"], "name": f["name"]} for f in r]

# Dùng: answer = langflow_run_flow("flow-uuid", {"input": "Phân tích thị trường AI VN"})
```

### OpenClaw
```bash
# Gọi API — không cần MCP
```

### Antigravity
```bash
pip install langflow
python -m langflow run --host 0.0.0.0 --port 7860
# Hoặc Docker:
docker run -d -p 7860:7860 logspace/langflow:latest
```
> ⚠️ Antigravity deploy → Hermes trigger flows đã build sẵn trong Langflow UI.

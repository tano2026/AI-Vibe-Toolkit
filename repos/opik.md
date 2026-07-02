# Opik — GitHub Repo

## TL;DR
Opik (by Comet) là platform mã nguồn mở để trace, evaluate và monitor LLM app/agent — thấy rõ agent gọi model gì, tool gì, sai ở bước nào, tự động chấm điểm bằng LLM-as-a-judge. Từ 0 lên 12.5K stars trong 8-9 tháng, hiện exploding growth.

## Repo này dùng để làm gì
Vấn đề: agent như Hermes/OpenClaw chạy autonomous, khi nó trả kết quả sai (Research Pro bịa số, ví dụ) mày không biết nó sai ở bước nào — search sai nguồn? model hiểu sai prompt? tool trả data lỗi? Opik ghi lại toàn bộ chuỗi hành động (trace): mỗi lần gọi LLM, mỗi tool call, mỗi bước agent — rồi cho mày xem lại từng bước trong dashboard.

3 khả năng chính:
- **Tracing** — log mọi LLM call/tool call/agent step, xem input/output từng bước
- **Evaluation** — chấm điểm bằng LLM-as-a-judge (hallucination, relevance, context precision...) hoặc metric heuristic, chạy được trong CI/CD qua PyTest integration
- **Production monitoring** — dashboard theo dõi token cost, latency, error rate theo thời gian thực; đặt "online evaluation rules" để tự động flag khi agent trả lời tệ

## Setup từng bước
1. Cách nhanh nhất — dùng cloud free tier tại comet.com (không cần setup)
2. Hoặc self-host bằng Docker:
```bash
git clone https://github.com/comet-ml/opik.git
cd opik
./opik.sh
```
3. Cài SDK Python:
```bash
pip install opik
```
4. Track 1 function bất kỳ chỉ cần decorator:
```python
import opik
opik.configure(use_local=True)  # chạy local, không cần Comet account

@opik.track
def research_pipeline(query: str) -> str:
    # code research của Hermes ở đây
    return "kết quả"
```

## Ví dụ thực tế
Research Pro trả về báo cáo có số liệu sai. Không có Opik thì tao chỉ biết "nó bịa số" mà không biết bịa ở bước nào. Gắn `@opik.track` vào từng bước pipeline (Collector → Validator → Analyst → Synthesizer từ Agentic Factory), Opik log lại input/output mỗi bước, mở dashboard thấy ngay: bước Collector lấy đúng data, nhưng bước Synthesizer khi tổng hợp bị model "diễn giải" sai số liệu — biết chính xác chỗ cần sửa prompt.

## Lưu ý / Lỗi thường gặp
- **use_local=True** chỉ chạy local hoàn toàn, không đồng bộ Comet cloud — tiện cho dev nhưng nhớ chọn đúng mode nếu muốn xem trên dashboard cloud.
- **Self-host cần Docker Compose hoặc Kubernetes** — bản Docker nhẹ hơn Airweave nhưng vẫn không phải 1 container đơn.
- **Framework nào không có integration sẵn** (list official integrations trong docs) thì phải tự dùng `@opik.track` decorator wrap thủ công, không tự động.
- Opik Agent Optimizer (tự sinh prompt tốt hơn) là feature khá mới, chưa nhiều case study — dùng phần Tracing + Evaluation là chắc ăn nhất trước.

## Đánh giá cá nhân
- **Điểm mạnh:** Setup cực nhanh (1 decorator), free tier rộng rãi, giải quyết đúng nỗi đau "agent tự chủ nhưng không biết nó sai ở đâu" — support native OpenAI/Ollama/LlamaIndex nên khớp DeepSeek/OmniRoute stack hiện tại. Có MCP server riêng (opik-mcp) để đọc trace ngay trong Claude Code/Cursor.
- **Điểm yếu:** Dashboard/UI đẹp nhưng là thêm 1 service phải maintain; nếu chỉ có vài agent nhỏ thì overhead setup > lợi ích, hợp hơn khi hệ thống đã phức tạp (nhiều agent, nhiều bước như Agentic Factory).
- **Có nên dùng không:** 8/10 — rất khớp nguyên tắc guardrail "agent research phải trích nguồn, không bịa số" trong Agentic Factory skill. Nên gắn vào Research Pro trước tiên vì đó là agent dễ bịa số nhất.

## Link
- Repo: https://github.com/comet-ml/opik
- Docs: https://www.comet.com/docs/opik/
- MCP: https://github.com/comet-ml/opik-mcp

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import opik

opik.configure(use_local=True)

@opik.track
def hermes_task(query: str) -> dict:
    # Toàn bộ logic task của Hermes wrap trong decorator này
    # Opik tự log input/output, thời gian chạy, exception nếu có
    result = {"query": query, "answer": "..."}
    return result

# Chấm điểm bằng LLM-as-judge sau khi có traces
from opik.evaluation import evaluate
from opik.evaluation.metrics import Hallucination

evaluate(
    dataset=my_dataset,
    task=hermes_task,
    scoring_metrics=[Hallucination()]
)
```

### OpenClaw
```bash
# Cài MCP server để đọc trace/score ngay trong chat, không cần mở dashboard
# opik-mcp — cấu hình trong MCP config của OpenClaw giống Firecrawl/Airweave
```

### Antigravity
```bash
# Self-host Opik server trên VPS
git clone https://github.com/comet-ml/opik.git
cd opik && ./opik.sh
```
> ⚠️ opik.sh mặc định dùng Docker Compose — kiểm tra RAM còn trống trên VPS Tencent Cloud trước khi chạy, tránh chồng thêm service khi Chatwoot vẫn đang chờ VPS riêng.

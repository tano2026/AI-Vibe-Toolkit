# Decision 3.0 (vllm-sr / AMD) — GitHub Repo

## TL;DR
Bộ 6 model đa phương thức (kích thước 0,6B đến 27B) trả lời câu hỏi về **văn bản, ảnh và video** bằng **xác suất cho từng đáp án**, không sinh văn bản. Dùng để phân loại, chấm mức độ, tìm vật thể, đánh dấu một mục tiêu trong video. Có API miễn phí và trọng số trên Hugging Face (`d3-nano` ghi Apache-2.0). Hợp để làm bộ lọc/định tuyến (phân loại ticket, kiểm ảnh); **không phải model mô tả hay tóm tắt ảnh/video**. Chưa chạy thử trong phiên này.

## Repo này dùng để làm gì
Nhóm vLLM-SR (AMD tài trợ, huấn luyện trên GPU AMD Instinct) gọi mỗi câu hỏi là một "decision". Bốn dạng câu hỏi theo trang chủ:
| Dạng | Việc làm | Ví dụ |
|---|---|---|
| `choice` | chọn 1 trong các lựa chọn có nhãn, kèm xác suất từng lựa chọn | định tuyến ticket hỗ trợ về đúng đội |
| `score` | chấm theo thang | Low / Normal / Urgent |
| `box` | tìm vật thể có tên trong ảnh, trả khung và độ tin cậy | tìm logo trong ảnh |
| `track` | tìm mục tiêu trong video, trả đáp án theo mốc thời gian | video lấy mẫu 2 khung/giây |

Sáu model dùng dạng `vllm-sr/<tên>`:
| Model | Cỡ | Điểm văn bản | Điểm thị giác |
|---|---|---|---|
| d3-turbo | 27B | 70,2 (ước tính) | 72,9 (ước tính) |
| d3-flash | 9B | 55,79 | 66,89 |
| d3-mini | 4B | 52,61 | 63,16 |
| d3-nano | 2B | 38,86 | 54,67 |
| d3-lite | 0,8B | 32,33 | 42,11 |
| d3-edge | 0,6B | 20,24 | 31,71 |
Điểm lấy từ trang chủ (bản chụp Jev Decision Index 0.3.2). Trang cũng ghi d3-turbo ở biểu đồ là 66,26 và 71,26, lệch với bảng — dùng làm thang so sánh, đừng coi là số tuyệt đối. Câu "#1" là lời của chính trang.

## Số liệu đã kiểm (22/10/2026, đọc trang chủ, model card `d3-nano` và bài blog Apple Silicon)
- `d3-nano`: Apache-2.0, nền Qwen/Qwen3.5-2B (Apache-2.0), 2,21B tham số gồm bộ mã hoá ảnh 0,33B. **License của 5 model còn lại chưa kiểm**
- Đầu vào: văn bản/JSON, nhiều ảnh (PNG, JPEG, WebP; tới 1,6 megapixel), video (MP4, WebM, MOV, MKV; 2 khung/giây, tối đa 32 khung). Ảnh và video gửi qua API dưới dạng base64
- Đầu ra: xác suất cho đáp án choice / yes-no / score. **Không sinh văn bản**
- Bộ nhớ GPU đo trên 1 card AMD Instinct MI325X: ~9,1 GiB (`d3-nano`, AutoModel, 1 yêu cầu), ~16,5 GiB mỗi replica Engine. Trang không nêu cấu hình tối thiểu
- Trên Mac M5 Pro 24 GB (bài blog): d3-nano ~173 ms → 69 ms mỗi yêu cầu khi chuyển sang Core ML; d3-mini nhìn video trực tiếp mỗi lần 1,1 s. Các bản tải về lớn: d3-nano 10,5 GB, d3-mini 19,6 GB
- Số sao, số người dùng: **chưa đo**. Chưa gọi API, chưa tải model, chưa có khoá
- Ngày ra mắt: các trang đo ngày 12–20/10/2026

## Setup
**Qua API (miễn phí):** tạo khoá ở trang Keys (khoá chỉ hiện một lần), gọi `POST https://decision.vllm-sr.ai/v1/systemone` với `Authorization: Bearer <khoá>` và JSON gồm `model`, `state`, `questions`. Trang cảnh báo yêu cầu và phản hồi **có thể bị lưu để cải thiện model** → không gửi dữ liệu nhạy cảm của khách.

**Chạy cục bộ bằng Transformers (theo model card):**
```bash
pip install transformers==5.17.0 torch torchvision pillow opencv-python-headless safetensors accelerate
python -c "from transformers import AutoModel; m=AutoModel.from_pretrained('vllm-sr/d3-nano', trust_remote_code=True)"
# gọi bằng model.system_one(...)
```
`trust_remote_code=True` nghĩa là chạy mã từ repo model: chỉ dùng sau khi đọc mã, trong môi trường cách ly.
**Engine của vLLM Semantic Router:** `vllm-sr serve -e vllm-sr/d3-nano` (cổng 8899, đường dẫn `/v1/systemone`; chế độ Engine còn ở kênh dev).

## Ví dụ thực tế
Bối cảnh: CSKH nhận ảnh khách gửi qua chat và muốn tự gắn nhãn trước khi chuyển cho người.
```text
Đầu vào: 1 ảnh khách gửi + câu hỏi dạng choice: "Ảnh này liên quan: vé / hành lý / thanh toán / khác?"
Đầu ra kỳ vọng (theo mô tả trang): xác suất cho từng lựa chọn → hệ thống chọn nhãn cao nhất, dưới ngưỡng thì chuyển người
```
**Chưa chạy thử — chưa biết độ chính xác với ảnh tiếng Việt hay ảnh chụp vé/hoá đơn thật.**

## Lưu ý / Lỗi thường gặp
- **Không thay được model mô tả/tóm tắt ảnh video.** Cần "xem video rồi viết tóm tắt" phải dùng model đa phương thức sinh văn bản; entry này chỉ phân loại
- Điểm thị giác của các cỡ nhỏ khá thấp ở một số bài: kiểm duyệt meme thù ghét (23,2), R-Bench-M (14,8), MMMU-Pro (18,6) → chưa tin cho việc kiểm duyệt nội dung
- Một số điểm thị giác là bản dựng lại gần đúng hoặc đánh giá nội bộ, không phải kết quả chính thức (theo model card)
- Batch có thể đổi 0,153% quyết định ở vùng gần hoà (mẫu 4.000 yêu cầu); kết quả có thể lệch nhẹ giữa AutoModel và Engine (lệch xác suất lớn nhất 0,011)
- API miễn phí có ghi log; trang không nêu giới hạn tốc độ, hạn mức hay cam kết dịch vụ
- Trang chủ không nêu license cho API và các model lớn
- Tên dễ nhầm: "Decision 3.0" ở đây là họ model `vllm-sr`, không liên quan các công cụ khác tên tương tự

## Đánh giá cá nhân
- Điểm mạnh: một lời gọi trả luôn xác suất từng đáp án nên dễ đặt ngưỡng "chắc thì tự xử lý, không chắc thì chuyển người"; chạy được cả ảnh và video; có cỡ nhỏ chạy cục bộ; có API miễn phí để thử; `d3-nano` Apache-2.0
- Điểm yếu: mới ra, chưa có kiểm chứng độc lập; không sinh văn bản; điểm thị giác cỡ nhỏ thấp ở một số bài; dữ liệu qua API có thể bị lưu; chưa rõ license model lớn; chưa thử tiếng Việt
- Có nên dùng: **6/10**. Thử 30 phút khi có việc phân loại ảnh/ticket cụ thể: lấy khoá, gửi 20 ảnh thật đã gắn nhãn tay, đo tỉ lệ đúng trước khi cam kết. Không gửi ảnh có dữ liệu cá nhân của khách lên API
- Cần mô tả/tóm tắt nội dung ảnh hoặc video: kho mới có OCR (`repos/paddleocr.md`) và transcript YouTube (`mcps/mcp-youtube.md`), chưa có công cụ hiểu nội dung ảnh/video nói chung; xem GAP-LOG

## Link
- Trang chủ và API: https://decision.vllm-sr.ai/
- Model card: https://huggingface.co/vllm-sr/d3-nano
- Bài chạy trên Apple Silicon: https://vllm-sr.ai/blog/decision-3-0-on-apple-silicon/
- Liên quan trong kho: `agents/thu-kho/` (tra kho), `catalog/GAP-LOG.md` (thiếu công cụ mô tả ảnh/video)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import json, os, urllib.request
# Chỉ biết 3 trường cấp cao theo trang chủ: model, state, questions.
# Lấy mẫu "state"/"questions" đúng schema từ decision.vllm-sr.ai trước khi chạy thật.
def decide(model, state, questions):
    req = urllib.request.Request(
        "https://decision.vllm-sr.ai/v1/systemone",
        data=json.dumps({"model": model, "state": state, "questions": questions}).encode(),
        headers={"Authorization": f"Bearer {os.environ['DECISION_API_KEY']}",
                 "Content-Type": "application/json"}, method="POST")
    return json.load(urllib.request.urlopen(req, timeout=60))
# vd: decide("vllm-sr/d3-nano", state, questions)  # chưa chạy thử
```
Khoá để trong biến môi trường `DECISION_API_KEY`, không ghi vào file. Không gửi dữ liệu nhạy cảm của khách (yêu cầu có thể bị ghi log).

### OpenClaw
```bash
# Không có gói skill riêng. Gọi bằng HTTP như trên, hoặc chạy Engine cục bộ:
vllm-sr serve -e vllm-sr/d3-nano   # cổng 8899, /v1/systemone (chế độ Engine còn ở kênh dev)
```

### Antigravity
```bash
# Self-host cần GPU (đo 9–23 GiB cho d3-nano trên MI325X) hoặc Mac Apple Silicon; trang không nêu mức tối thiểu
pip install transformers==5.17.0 torch torchvision pillow opencv-python-headless safetensors accelerate
```
> ⚠️ `trust_remote_code=True` chạy mã từ repo model: đọc trước, chạy trong container cách ly. Chưa chạy thử trên VPS.

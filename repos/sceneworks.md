# SceneWorks — GitHub Repo

## TL;DR
AI Studio chạy hoàn toàn local — tạo ảnh, video, train LoRA ngay trên GPU của mày, không cần cài ComfyUI hay thuê cloud. Giao diện đẹp hơn, "cài là dùng" hơn, có MCP Server cho agent.

## Repo này dùng để làm gì
Mày biết ComfyUI chứ — mạnh nhưng phải ghép node như lắp Lego, cài plugin lung tung, mới dùng lần đầu là bỏ cuộc ngay. SceneWorks sinh ra để giải quyết đúng cái đó.

Nó là một **local AI Studio** với giao diện web sạch, tích hợp sẵn mọi thứ mày cần để làm content AI:
- Tạo ảnh từ text (Text-to-Image) với nhiều model phổ biến (SDXL, Flux, v.v.)
- Text-to-Video và Image-to-Video
- Inpainting — vẽ đè / chỉnh sửa vùng ảnh bằng AI
- **Face consistency** — giữ khuôn mặt nhất quán qua nhiều lần gen (cái này ComfyUI phải cài plugin thêm)
- **Thay nhân vật trong video bằng AI**
- Train LoRA ngay trong app — không cần ra ngoài dùng tool khác
- Quản lý model với nhiều mức quantization (Q4, Q8, fp16...) → chọn đúng theo VRAM
- Hàng đợi xử lý, thư viện ảnh, preset — quản lý được workflow lâu dài
- **MCP Server** → điều khiển từ Claude Code, Cursor hoặc agent của mày

Mọi xử lý đều chạy trên GPU local của mày, không upload ảnh lên cloud, không subscription.

## Setup từng bước

### Yêu cầu
- GPU NVIDIA (tối thiểu 8GB VRAM khuyến nghị, 6GB có thể chạy được với quantized model)
- Python 3.10+
- Git

### Cài đặt
```bash
# Clone repo
git clone https://github.com/TiniXXX/SceneWorks.git
cd SceneWorks

# Tạo virtualenv
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Cài dependencies
pip install -r requirements.txt

# Chạy app
python app.py
```
Mở browser → `http://localhost:7860`

### Download model
Vào tab **Models** trong app → chọn model muốn dùng → download trực tiếp, không cần tự tìm link Hugging Face.

### Bật MCP Server (nếu dùng với agent)
```bash
# Trong config hoặc flag khi chạy
python app.py --mcp-server
# MCP endpoint sẽ hiện ra để copy vào Claude Code / Cursor
```

## Ví dụ thực tế
**Use case: Tạo loạt thumbnail YouTube cho ABTRIP**

1. Load model Flux.1-schnell (Q8, ~10GB VRAM)
2. Prompt: `"travel agency thumbnail, Vietnamese couple at Da Nang beach, golden hour, cinematic, 16:9"`
3. Gen 4 variant → pick 1 → inpaint logo chỗ góc trái
4. Lưu vào thư viện, gắn preset "ABTRIP thumbnail" để dùng lại

Kết quả: 4 thumbnail trong ~3 phút, không cần Photoshop hay Canva.

**Use case với MCP Agent:**
OpenClaw gọi MCP endpoint của SceneWorks → gen ảnh tự động theo lịch content → lưu thẳng vào Google Drive → không cần người ngồi canh.

## Lưu ý / Lỗi thường gặp
- **CUDA out of memory** → chọn model quantization thấp hơn (Q4 thay vì fp16), giảm resolution, giảm batch size
- **Video gen chậm** → bình thường, video tốn VRAM hơn ảnh nhiều — đừng chạy nhiều task song song
- **Face consistency không ổn định** → cần seed cố định + prompt mô tả khuôn mặt chi tiết hơn
- **MCP không kết nối** → kiểm tra firewall local, port 7860 có bị block không
- **Train LoRA lâu** → với GPU 8GB thì 500-1000 step mất khoảng 15-30 phút tùy dataset

## Đánh giá cá nhân
- **Điểm mạnh:** Giao diện đẹp, all-in-one không cần ghép node, MCP Server là điểm cộng lớn cho ai xây agent pipeline, face consistency tích hợp sẵn rất tiện
- **Điểm yếu:** Còn khá mới (early stage), ecosystem model/plugin chưa phong phú bằng ComfyUI, community nhỏ hơn nên ít tutorial hơn, tài liệu còn sơ sài
- **Có nên dùng không:** 7.5/10 — Nếu mày đang làm content AI và ghét ComfyUI thì SceneWorks đáng thử ngay. Nhưng nếu mày cần workflow phức tạp, nhiều custom node → ComfyUI vẫn mạnh hơn về độ linh hoạt.

## Link
- Repo: https://github.com/TiniXXX/SceneWorks
- Hashtag gốc: #SceneWorks #OpenSource #AI #TiniX

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Gọi SceneWorks qua REST API (khi chạy với --mcp-server hoặc API mode)
import urllib.request, json

SCENEWORKS_URL = "http://localhost:7860"

def generate_image(prompt, model="flux-schnell", steps=20, width=1024, height=1024):
    payload = {
        "prompt": prompt,
        "model": model,
        "steps": steps,
        "width": width,
        "height": height
    }
    req = urllib.request.Request(
        f"{SCENEWORKS_URL}/api/generate",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    result = json.loads(urllib.request.urlopen(req).read())
    return result.get("image_url") or result.get("image_path")

# Ví dụ
img = generate_image("ABTRIP travel thumbnail, Vietnamese beach, golden hour")
print("Generated:", img)
```
> ⚠️ API endpoint chính xác phụ thuộc version — check `/docs` của app sau khi chạy

### OpenClaw
```bash
# Kết nối MCP Server của SceneWorks
npx mcp-remote http://localhost:7860/mcp
# Hoặc add vào MCP config của Cursor/Claude Code:
# { "sceneworks": { "url": "http://localhost:7860/mcp" } }
```

### Antigravity
```bash
# Deploy SceneWorks trên VPS có GPU (cần NVIDIA driver + CUDA)
git clone https://github.com/TiniXXX/SceneWorks.git /opt/sceneworks
cd /opt/sceneworks
pip install -r requirements.txt

# Chạy background với pm2
pm2 start "python app.py --host 0.0.0.0 --port 7860" --name sceneworks
pm2 save

# Nếu cần expose ra ngoài (cẩn thận security)
# Khuyến nghị: dùng nginx reverse proxy + auth
```
> ⚠️ Chạy trên VPS cần GPU cloud (Vast.ai, RunPod) — VPS thường không có GPU

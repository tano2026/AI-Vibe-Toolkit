# Pixelle-Video — GitHub Repo

## TL;DR
Gõ 1 chủ đề, Pixelle-Video tự viết kịch bản, sinh ảnh/video minh hoạ AI cho từng câu, lồng giọng đọc, thêm nhạc nền, rồi ghép thành video hoàn chỉnh — có web UI kéo thả cấu hình, chạy được hoàn toàn miễn phí nếu tự host model local. 19.7k+ star, Apache 2.0.

## Repo này dùng để làm gì
Cùng nhóm "topic → video tự động" như Vox Director đã ghi trong kho, nhưng khác chiến lược: Pixelle-Video build trên nền ComfyUI (dùng workflow ComfyUI để sinh ảnh/video/TTS), có web UI Streamlit chạy local (`localhost:8501`), và đặc biệt — **hoàn toàn free** nếu chạy Ollama + ComfyUI local, không bắt buộc trả phí API như Vox Director (Atlas Cloud) hay MoneyPrinterTurbo (thường dùng API trả phí).

Pipeline: **Sinh kịch bản → Lên kế hoạch ảnh (mỗi câu 1 ảnh) → Xử lý từng frame → Ghép video**. Hỗ trợ cả tạo ảnh tĩnh (image_*.html template) lẫn video động (video_*.html template, dùng model như WAN 2.1), có cả mode "digital human" (avatar nói), "image-to-video", "motion transfer" (lấy chuyển động từ video mẫu áp vào ảnh khác).

## Setup từng bước

**Cách nhanh nhất (Windows, không cần cài gì):**
1. Tải Windows All-in-One Package tại phần Releases của repo.
2. Giải nén, double-click `start.bat`.
3. Browser tự mở `http://localhost:8501`.
4. Vào "⚙️ System Configuration" điền API key LLM + cấu hình ảnh.

**Cách chạy từ source (macOS/Linux, hoặc cần custom):**
1. Cài `uv` (Python package manager) theo docs.astral.sh/uv.
2. Cài `ffmpeg`:
   ```bash
   # macOS
   brew install ffmpeg
   # Ubuntu/Debian (VPS Tano dùng cái này)
   sudo apt update && sudo apt install ffmpeg
   ```
3. Clone và chạy:
   ```bash
   git clone https://github.com/AIDC-AI/Pixelle-Video.git
   cd Pixelle-Video
   uv run streamlit run web/app.py
   ```
4. Vào web UI, cấu hình:
   - **LLM**: chọn preset (Qwen/GPT/DeepSeek...) hoặc tự điền API key + base URL
   - **Ảnh**: trỏ tới ComfyUI local (`http://127.0.0.1:8188`) hoặc dùng RunningHub API Key (cloud)
5. Chọn mode nhập nội dung: "AI Generated Content" (chỉ cần gõ chủ đề) hoặc "Fixed Script Content" (dán sẵn kịch bản, bỏ qua bước AI viết).
6. Bấm "🎬 Generate Video", theo dõi tiến độ real-time, video ra ở folder `output/`.

## Ví dụ thực tế

Case cho GMSP podcast (Tử Vi + tâm lý + kinh tế): gõ topic "Vì sao con người sợ thay đổi dù biết nó tốt cho mình" → chọn template thuộc nhóm "Deep Thinking" → chọn TTS Edge-TTS (free) → generate ra video dọc có ảnh minh hoạ từng câu, giọng đọc, nhạc nền — không cần dựng tay.

Repo có sẵn showcase nhiều thể loại: documentary/lifestyle, giải mã văn hoá, khoa học, digital human nói tiếng Hàn, chuyển thể tiểu thuyết, bình luận lịch sử — đa dạng hơn Vox Director (chỉ có 1 style paper-collage).

## Lưu ý / Lỗi thường gặp

- **Không có GPU local** → bắt buộc dùng cloud (RunningHub cho ảnh, OpenAI/Qwen cho LLM) — mất phí, không còn "hoàn toàn free" như quảng cáo.
- **ComfyUI phải cài + chạy riêng** nếu muốn tự host ảnh — đây không phải plug-and-play, cần biết cơ bản ComfyUI workflow.
- **Prompt prefix cho ảnh phải viết tiếng Anh** — kể cả kịch bản tiếng Việt, phần điều khiển style ảnh vẫn cần prompt English.
- **VRAM hạn chế trên VPS Tencent Cloud (không GPU)** — theo ghi chú hạ tầng đã có trong kho, Pixelle-Video bản tự host ảnh KHÔNG chạy được trên VPS hiện tại, phải dùng nhánh cloud (RunningHub) nếu muốn chạy trên VPS.

## Đánh giá cá nhân

- **Điểm mạnh:** Cộng đồng cực lớn (19.7k star, 2.8k fork, cập nhật gần như mỗi tuần — tính năng "Motion Transfer" mới thêm gần đây) → maintain tốt hơn hẳn Vox Director (mới 7 star). Linh hoạt model — đổi LLM, đổi TTS, đổi workflow ComfyUI tuỳ ý, không lock-in 1 vendor. Có chế độ hoàn toàn free (Ollama + ComfyUI local) — khác biệt lớn với Vox Director.
- **Điểm yếu:** Setup phức tạp hơn nhiều nếu muốn chạy free thật (phải tự host ComfyUI + LLM local, cần GPU) — với hạ tầng Tano hiện tại (VPS không GPU) thì vẫn phải trả phí cloud, y hệt Vox Director. Web UI Streamlit — không có API/CLI chuẩn để nhét thẳng vào pipeline agent (Hermes/OpenClaw) như Remotion, phải tự viết wrapper gọi Streamlit hoặc tìm cách trigger headless.
- **Có nên dùng: 7/10** — mạnh hơn Vox Director về độ trưởng thành + tính linh hoạt model, nhưng vẫn thua Remotion Template Factory về khả năng tích hợp agent tự động (không có render API sạch để agent gọi thẳng) và thua về chi phí nếu không có GPU local.

## Link
- Repo: https://github.com/AIDC-AI/Pixelle-Video
- Docs: https://aidc-ai.github.io/Pixelle-Video
- Windows package: https://github.com/AIDC-AI/Pixelle-Video/releases/latest

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Không có REST API sạch — Streamlit app chạy local port 8501.
# Cách khả thi nhất: Hermes launch process Streamlit rồi dùng Streamlit's
# programmatic mode hoặc điều khiển qua Selenium/Playwright (không lý tưởng).
# Khuyến nghị: ưu tiên Remotion Template Factory cho việc agent tự động render;
# dùng Pixelle-Video khi cần Nobitano tự tay generate qua web UI.
import subprocess

def start_pixelle_video(project_dir="/path/to/Pixelle-Video"):
    subprocess.Popen(["uv", "run", "streamlit", "run", "web/app.py"], cwd=project_dir)
    # Sau đó mở http://localhost:8501 để thao tác tay
```

### OpenClaw
```bash
# Cài 1 lần trên VPS (không có GPU nên bắt buộc dùng RunningHub cho ảnh)
git clone https://github.com/AIDC-AI/Pixelle-Video.git
cd Pixelle-Video
uv run streamlit run web/app.py --server.port 8501 --server.headless true
# Truy cập qua SSH tunnel hoặc reverse proxy vì VPS không có màn hình
```

### Antigravity
```bash
# Deploy checklist trên Ubuntu 22.04
sudo apt update && sudo apt install -y ffmpeg
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone https://github.com/AIDC-AI/Pixelle-Video.git /opt/pixelle-video
cd /opt/pixelle-video && uv sync
# Chạy nền bằng PM2 giống các service khác đang chạy trên VPS
pm2 start "uv run streamlit run web/app.py --server.headless true" --name pixelle-video
```
> ⚠️ VPS hiện tại không có GPU — bắt buộc cấu hình RunningHub (cloud) cho phần sinh ảnh/video, không tự host ComfyUI free được.

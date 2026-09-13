---
name: stickman-studio
description: >
  Repo (saiedpod-bot/Stickman-Studio) — pipeline Python full: script (Gemini) → ảnh nhân vật
  nhất quán (Imagen) → video (Ken Burns free hoặc Veo trả phí) → TTS free → upload YouTube tự động.
---

# Stickman Studio — GitHub Repo

## TL;DR
Pipeline Python end-to-end tự động hoá cả kênh content phong cách "stickman": script → ảnh nhân vật nhất quán → video → TTS free → phụ đề → publish YouTube, có cả scheduler tự chạy 24/7 và dashboard Streamlit. Chỉ 2⭐ (còn non, chưa nhiều người kiểm chứng) nhưng code đầy đủ, kiến trúc rất khớp mô hình Hermes/OpenClaw đang xây cho Tano Agency.

## Repo này dùng để làm gì
5 phase cố định, mỗi phase 1 file riêng trong `stickman_studio/phases/`:
1. **Script** (Gemini 2.5 Flash) — hook + storyboard cảnh
2. **Images** (Imagen 3.0) — nhân vật "stickman" nhất quán giữa các cảnh (không phải vẽ tay/joint-based, là AI image gen theo phong cách người que)
3. **Video** — slideshow Ken Burns zoom (miễn phí, ffmpeg) hoặc Veo 2.0 image-to-video (trả phí)
4. **Narration** — edge-tts, 100% free, không cần API key
5. **Assembly + Upload** — ffmpeg ghép + nhạc nền + phụ đề (MoviePy) → auto publish YouTube qua OAuth

Có sẵn scheduler tự chạy autonomous (random 5-7h/lần tránh bị YouTube phát hiện pattern) và chế độ lên kế hoạch 30 ngày.

## Setup từng bước
```bash
git clone https://github.com/saiedpod-bot/Stickman-Studio.git
cd Stickman-Studio
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install edge-tts

# Cần tài khoản Google Cloud (Vertex AI) — có $300 credit free 90 ngày
# Enable: Vertex AI API, Cloud Storage (optional), YouTube Data API v3 (optional)
# Tạo Service Account, tải key JSON, điền vào .env (theo .env.example)

# Chạy thử:
python orchestrator.py "Chủ đề video" --video-mode slideshow
```

## Ví dụ thực tế — áp cho GMSP
Repo này không tự khớp giọng "Kẻ Soi Gương" hay khung 4 lớp của GMSP — cần tuỳ biến `phase1_script.py` để nhồi đúng prompt hệ thống (voice rules + 4-layer framework) thay vì để Gemini tự viết theo template mặc định của repo. Chỗ đáng lấy nhất là **kiến trúc pipeline** (phase tách rời, cache theo phase, retry qua Tenacity) — dùng làm khung sườn để tự viết lại `phase1_script.py` gọi đúng system prompt GMSP, giữ nguyên phase 2-5 (ảnh/video/TTS/upload).

## Lưu ý / Lỗi thường gặp
- Chỉ 2⭐, 6 commit — chưa ai kiểm chứng rộng rãi, đọc kỹ code trước khi cho chạy autonomous thật.
- Ảnh "stickman" là do Imagen vẽ theo phong cách, KHÔNG phải hệ thống joint/skeleton animation thật — nếu cần đúng chất người que Pivot, kết hợp với `stickman-video-director` (skill ở trên) cho phần visual thay vì dùng Imagen.
- Cần setup Google Cloud đầy đủ (project, service account, enable API) — tốn thời gian setup ban đầu hơn hẳn các skill hosted khác trong kho.
- edge-tts hiện KHÔNG hỗ trợ giọng đọc chuẩn tiếng Việt tự nhiên bằng ElevenLabs — với GMSP nên thay `tts_engine.py` sang pipeline TTS tiếng Việt đã dùng (nếu có) thay vì giữ nguyên edge-tts mặc định.

## Đánh giá cá nhân
- Điểm mạnh: kiến trúc pipeline rất sạch (5 phase tách rời, cache/retry sẵn, dashboard Streamlit để giám sát) — đúng tinh thần content factory tự động của kho.
- Điểm yếu: 2 sao chưa kiểm chứng; ảnh không phải joint-based thật; cần setup GCP tốn công; TTS mặc định không hợp tiếng Việt.
- Có nên dùng không: 6.5/10 — không dùng nguyên bản, nhưng đáng đọc code làm blueprint tự build pipeline GMSP riêng (thay Gemini/Imagen bằng stack Hermes đã có, thay edge-tts bằng TTS tiếng Việt hiện dùng).

## Link
- Repo: https://github.com/saiedpod-bot/Stickman-Studio
- Releases (sample video): https://github.com/saiedpod-bot/Stickman-Studio/releases

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Không gọi trực tiếp phase1_script.py gốc — tự viết lại để nhồi system prompt GMSP
# (4-layer framework + voice "Kẻ Soi Gương") thay vì dùng script generator mặc định của repo.
# Giữ nguyên phase2_images / phase3_slideshow / phase4_assembly làm khung sườn.
```

### OpenClaw
```bash
git clone https://github.com/saiedpod-bot/Stickman-Studio.git
# Deploy trên VPS, chỉnh .env với GCP project của Tano Agency
```

### Antigravity
```bash
# Deploy checklist: Python 3.10+, ffmpeg, GCP service account key,
# YouTube OAuth client_secrets.json nếu cần auto-publish
```
> ⚠️ KHÔNG bật scheduler autonomous auto-publish YouTube cho tới khi đã test kỹ voice/khung GMSP thủ công — repo mặc định publish "public" ngay, dễ đăng nhầm content chưa đúng chuẩn.

# OpenMontage — GitHub Repo

## TL;DR
Hệ thống production video agentic đầu tiên mã nguồn mở. 12 pipeline, 52 tools, 500+ agent skill — biến AI coding assistant (Claude, Cursor, Copilot) thành cả một studio sản xuất video hoàn chỉnh. 22K stars và đang tăng nhanh.

## Repo này dùng để làm gì
Thay vì dùng riêng lẻ: ElevenLabs cho voice, Stable Diffusion cho ảnh, FFmpeg để ghép — OpenMontage gộp tất cả thành pipeline agentic. Mày nói một câu, nó tự:
- Viết script
- Tạo voiceover (ElevenLabs, local TTS)
- Generate ảnh/clip (Flux, Stable Diffusion, Remotion)
- Ghép video hoàn chỉnh (FFmpeg)

12 pipeline có sẵn: faceless video, explainer, social clip, documentary style, v.v.

## Setup từng bước
```bash
# 1. Clone repo
git clone https://github.com/calesthio/OpenMontage
cd OpenMontage

# 2. Cài dependencies
pip install -r requirements.txt

# 3. Config API keys trong .env
ELEVENLABS_API_KEY=your_key
OPENAI_API_KEY=your_key  # hoặc ANTHROPIC_API_KEY
STABILITY_API_KEY=your_key  # nếu dùng Stable Diffusion

# 4. Chạy pipeline đầu tiên
python run.py --pipeline faceless_shorts --prompt "Top 5 AI tools năm 2026"

# 5. Hoặc paste URL video mày thích → clone style
python run.py --clone-style https://youtube.com/watch?v=xxx
```

## Ví dụ thực tế
**Input:** `python run.py --pipeline faceless_shorts --prompt "Cách dùng Claude Code để code không cần gõ phím"`

**Output (trong ~5-10 phút):**
- Script 60 giây tự động viết
- Voiceover ElevenLabs với giọng đã chọn
- 8-10 clip/ảnh minh họa auto-generate
- Video ghép hoàn chỉnh có sub, transition, background music

## Lưu ý / Lỗi thường gặp
- Cần GPU nếu chạy local Stable Diffusion — không có GPU thì dùng API (tốn tiền hơn)
- ElevenLabs free tier có giới hạn ký tự — cần plan trả phí để làm video dài
- FFmpeg phải cài sẵn trong system: `brew install ffmpeg` (Mac) hoặc `apt install ffmpeg` (Linux)
- `.env` không được commit lên GitHub — thêm vào `.gitignore` ngay

## Đánh giá cá nhân
- Điểm mạnh: All-in-one thật sự; 12 pipeline đa dạng; mã nguồn mở hoàn toàn; tích hợp được với workflow hiện tại
- Điểm yếu: Setup phức tạp hơn tool SaaS; chất lượng video phụ thuộc vào API keys mày dùng; tài liệu còn thiếu một số pipeline
- Có nên dùng không: **8.5/10** — Nếu mày làm content faceless và muốn tự động hóa pipeline, đây là repo đáng nhất hiện tại

## Link
- Repo: https://github.com/calesthio/OpenMontage
- Topics: agent, claude, elevenlabs, ffmpeg, flux, remotion, video-generation

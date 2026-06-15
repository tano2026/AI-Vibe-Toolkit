# MoneyPrinterTurbo — Tự Động Tạo Video Kiếm Tiền (87.8k⭐)

**GitHub:** https://github.com/harry0703/MoneyPrinterTurbo
**Stars:** 87.8k⭐ | **License:** MIT | **Language:** Python
**#5 GitHub Trending Tuần 23** | +9,174 stars tuần này
**Website:** moneyprinterturbo.com

---

## Đây Là Gì

Tool tự động tạo **short-form video** từ topic → script → voiceover → subtitles → video hoàn chỉnh. Hỗ trợ đa ngôn ngữ, nhiều TTS providers, upload thẳng lên YouTube/TikTok.

```
Topic/Keyword
→ AI viết script
→ TTS voiceover
→ Tìm footage B-roll
→ Add subtitles
→ Render video
→ Upload platform
```

---

## Cài & Setup

```bash
git clone https://github.com/harry0703/MoneyPrinterTurbo
cd MoneyPrinterTurbo
pip install -r requirements.txt
cp config.example.toml config.toml
# Điền API keys trong config.toml

# Start web UI
python main.py
# → http://localhost:8501
```

---

## Config Key (config.toml)

```toml
# LLM cho script generation
[llm]
provider = "anthropic"  # hoặc openai, gemini, ollama
model = "claude-haiku-4-5"  # rẻ nhất

# TTS
[tts]
provider = "edge"  # free, Microsoft Edge TTS
# hoặc: elevenlabs, openai, azure

# Video
[video]
fps = 30
resolution = "1080x1920"  # TikTok vertical
language = "vi"  # Tiếng Việt
```

---

## Dùng Ngay (Web UI)

```
1. Mở http://localhost:8501
2. Nhập topic: "Top 5 AI tools 2026"
3. Chọn ngôn ngữ: Tiếng Việt
4. Chọn giọng đọc
5. Click Generate
→ Video ~2 phút sau
```

---

## Tích Hợp Với AI Vibe Toolkit

```bash
# Workflow content TikTok từ kho
# 1. Lấy script từ kho
cat content/script-video-47-ke-toan-ai.md

# 2. Feed vào MoneyPrinterTurbo
# Paste text vào "Custom Script" box
# → Tool tự tạo video

# 3. Upload TikTok/YouTube
```

---

## Đánh Giá Cá Nhân

87.8k stars — đây là top tool "faceless YouTube channel" automation từ 2024 và vẫn active đến nay.

Điểm mạnh: **Web UI dễ dùng**, không cần code. TTS tiếng Việt với Edge TTS free và khá tốt.

Điểm yếu: B-roll footage tự động đôi khi không relevant. Cần review trước khi upload.

**Rating: 8/10** — Tốt để prototype nhanh, cần chỉnh sửa cho production.

---
*Nguồn: github.com/harry0703/MoneyPrinterTurbo | 87.8k⭐ | MIT | tháng 6/2026*

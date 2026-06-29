# YASGU — YouTube Automatised Shorts Generator & Uploader

## TL;DR
80 stars — Auto tạo YouTube Shorts từ text/script: TTS voiceover → ghép background video → add subtitles → upload lên YouTube. Pipeline tự động từ A-Z, không cần edit tay.

## Dùng để làm gì
- Tự động tạo Shorts từ script text
- Pipeline: Script → TTS → Background video → Subtitles → Upload YouTube
- Batch production: tạo nhiều video cùng lúc
- Kết hợp với content factory: Hermes viết script → YASGU render → upload

## Setup từng bước

```bash
git clone https://github.com/hankerspace/YASGU
cd YASGU
pip install -r requirements.txt

# Config:
cp config.example.json config.json
# Điền: YouTube OAuth, TTS provider (ElevenLabs/Google TTS), background video folder
```

## Ví dụ thực tế

Hermes viết 10 scripts về AI tools → YASGU tự render 10 Shorts → upload lên kênh Tano:
```python
yasgu_batch_create([
    {"script": "5 AI tools miễn phí thay ChatGPT...", "title": "AI Tools Free #1"},
    {"script": "Cách dùng Claude để viết content...", "title": "Claude Tips"},
    # ...
])
# → 10 Shorts tự động upload lên YouTube
```

## Lưu ý / Lỗi thường gặp
- **FFmpeg bắt buộc:** Cần install FFmpeg trên VPS trước
- **Background video:** Cần chuẩn bị sẵn folder video nền (gameplay, nature, etc.)
- **TTS:** Mặc định Google TTS free — ElevenLabs chất lượng hơn nhưng có phí
- **YouTube OAuth:** Setup giống youtube-upload.md — cần refresh token

## Đánh giá cá nhân
- Điểm mạnh: Pipeline đầy đủ từ script đến upload, tự động 100%
- Điểm yếu: Cần chuẩn bị background video, chất lượng TTS mặc định không cao
- Có nên dùng không: 8/10 — Ideal cho content factory scale nhanh

## Link
- Repo: https://github.com/hankerspace/YASGU
- Docs: https://github.com/hankerspace/YASGU#readme

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import subprocess, json, os

YASGU_DIR = "/opt/yasgu"  # sau khi Antigravity deploy

def yasgu_create_short(script, title, voice="vi-VN-Standard-A",
                       background_category="nature", output_dir="/tmp/shorts"):
    os.makedirs(output_dir, exist_ok=True)
    config = {
        "script": script, "title": title,
        "voice": voice,
        "background": background_category,
        "output": f"{output_dir}/{title[:30]}.mp4"
    }
    config_path = f"{output_dir}/config_{title[:10]}.json"
    with open(config_path, "w") as f:
        json.dump(config, f)
    result = subprocess.run(
        ["python3", "main.py", "--config", config_path],
        capture_output=True, text=True, cwd=YASGU_DIR
    )
    if result.returncode == 0:
        return config["output"]
    raise Exception(f"YASGU error: {result.stderr}")

def yasgu_batch_create(scripts_list):
    results = []
    for item in scripts_list:
        try:
            path = yasgu_create_short(
                script=item["script"],
                title=item["title"],
                voice=item.get("voice", "vi-VN-Standard-A"),
                background_category=item.get("background", "nature")
            )
            results.append({"title": item["title"], "path": path, "status": "ok"})
        except Exception as e:
            results.append({"title": item["title"], "error": str(e), "status": "fail"})
    return results

# Workflow content factory:
# 1. Hermes viết scripts (dùng skills/content-creator.md)
# 2. yasgu_batch_create(scripts) → render videos
# 3. youtube_upload() từ mcps/youtube-upload.md → upload lên YT
```

### OpenClaw
```bash
# Giao Hermes xử lý toàn bộ pipeline
```

### Antigravity
```bash
# Cài FFmpeg (bắt buộc):
# CentOS/RHEL:
yum install -y ffmpeg ffmpeg-devel
# Hoặc từ source nếu repo không có:
# https://ffmpeg.org/download.html

# Deploy YASGU:
git clone https://github.com/hankerspace/YASGU /opt/yasgu
cd /opt/yasgu
pip install -r requirements.txt
cp config.example.json config.json
nano config.json  # điền YouTube token, TTS key

# Tạo thư mục background videos:
mkdir -p /opt/yasgu/backgrounds/nature
mkdir -p /opt/yasgu/backgrounds/gameplay
# → Upload video nền vào đây

# Test:
python3 main.py --test
```
> ⚠️ Cần FFmpeg + folder background videos trước khi Hermes gọi được.

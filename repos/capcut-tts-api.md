# capcut-tts-api — GitHub Repo

## TL;DR
Python client goi thang CapCut TTS API — lay giong doc CapCut (giong BV074 va nhieu giong khac) ma khong can mo app. 177 stars, tac gia VN (@K07VN). Dung de tu dong hoa voiceover video trong pipeline, thay the ElevenLabs/Resona neu may da co tai khoan CapCut.

## Repo nay dung de lam gi
CapCut co TTS (text-to-speech) chat luong tot, nhieu giong VN tu nhien — nhung chi dung duoc trong app, khong co API chinh thuc. Repo nay reverse-engineer cac endpoint noi bo cua CapCut de goi TTS tu Python:

- **TTS:** Text → MP3, chon giong, chinh toc do
- **STT:** Audio/video → transcript + subtitle (nhan dang giong noi)
- **Upload:** Up file audio len CapCut VOD de STT
- Khong dung native lib, khong dung .dylib, pure Python

Dac biet: co giong **BV074_streaming** — giong VN chat luong cao ma CapCut dang dung cho video TikTok.

## Setup tung buoc

```bash
# Clone
git clone https://github.com/K07VN/capcut-tts-api
cd capcut-tts-api

# Cai dependency
pip install requests

# Config device (co san DEFAULT_DEVICE, co the dung ngay)
# Hoac tao device.json voi device_id cua may:
cat > device.json << 'EOF'
{
  "device_id": "7647183892936328721",
  "iid": "7647185302080423697",
  "appvr": "8.7.0",
  "lan": "vi-VN",
  "loc": "VN",
  "region": "VN"
}
EOF
```

### TTS — Text sang MP3

```bash
# Tao TTS task
python3 capcut_common_task_client.py tts-new   --text "Day la doan text can chuyen thanh giong noi"   --voice BV074_streaming   --rate 1.0

# Response tra ve task id + token
# { "data": { "tasks": [{ "id": "...", "token": "..." }] } }

# Query ket qua (poll cho den khi xong)
python3 capcut_common_task_client.py tts-query   --task-id <task_id>   --token <token>
# → tra ve URL download file MP3
```

### STT — Audio/Video sang Text

```bash
# Upload file truoc
python3 capcut_common_task_client.py upload   --file ./video.mp4

# Tao STT task
python3 capcut_common_task_client.py stt-new   --vod-uri <uri_tu_upload>

# Query ket qua
python3 capcut_common_task_client.py stt-query   --task-id <task_id>   --token <token>
# → transcript + timestamps → dung tao SRT file
```

## Vi du thuc te — Tich hop vao pipeline video

```python
import subprocess, json, time, urllib.request

def capcut_tts(text, voice="BV074_streaming", rate=1.0):
    # Tao TTS task
    result = subprocess.run([
        "python3", "capcut_common_task_client.py", "tts-new",
        "--text", text,
        "--voice", voice,
        "--rate", str(rate)
    ], capture_output=True, text=True)

    task = json.loads(result.stdout)
    task_id = task["data"]["tasks"][0]["id"]
    token = task["data"]["tasks"][0]["token"]

    # Poll cho den khi xong
    for _ in range(30):
        time.sleep(2)
        query = subprocess.run([
            "python3", "capcut_common_task_client.py", "tts-query",
            "--task-id", task_id, "--token", token
        ], capture_output=True, text=True)
        result = json.loads(query.stdout)
        if result["data"]["status"] == "succeed":
            mp3_url = result["data"]["url"]
            # Download MP3
            urllib.request.urlretrieve(mp3_url, "voiceover.mp3")
            return "voiceover.mp3"
    raise Exception("TTS timeout")

# Dung trong pipeline:
audio = capcut_tts("CEO Y Combinator khong go code tu thang 12...")
# → voiceover.mp3 → ghep vao video bang FFmpeg
```

## Vi du thuc te — STT tao caption tu dong

```python
def capcut_stt(video_file):
    # 1. Upload video
    upload = subprocess.run([
        "python3", "capcut_common_task_client.py", "upload",
        "--file", video_file
    ], capture_output=True, text=True)
    vod_uri = json.loads(upload.stdout)["uri"]

    # 2. Tao STT task
    stt = subprocess.run([
        "python3", "capcut_common_task_client.py", "stt-new",
        "--vod-uri", vod_uri
    ], capture_output=True, text=True)
    task_id = json.loads(stt.stdout)["data"]["tasks"][0]["id"]

    # 3. Poll → lay transcript + timestamps
    # ... (tuong tu TTS)
    # → ra SRT file → burn sub bang FFmpeg
```

## Luu y / Loi thuong gap
- **Khong phai API chinh thuc** — CapCut co the thay doi endpoint bat ky luc nao, repo co the break
- Can tai khoan CapCut hop le — device_id phai khop voi account dang nhap
- Rate limit: khong ro chinh xac nhung dung qua nhieu request 1 luc co the bi chan
- Chi dung voi account, thiet bi, noi dung may duoc phep dung — doc warning trong README
- BV074_streaming la giong VN tot nhat hien tai — test truoc khi dung production

## Danh gia ca nhan
- Diem manh: TTS giong VN tu nhien cua CapCut mien phi; co ca STT; pure Python de tich hop; tac gia VN — update phu hop market VN
- Diem yeu: Unofficial API, de bi break; can tai khoan CapCut; khong co doc chinh thuc; 177 stars con nho
- Co nen dung khong: **7.5/10** — Alternative hay cho ElevenLabs/Resona neu may dung CapCut nhieu. Tich hop vao pipeline AI-auto-generate-video thay the OmniVoice duoc. Backup plan: Resona neu CapCut API bi break.

## Agent Integration

### Hermes (Python)
```python
# Copy repo vao /home/hermes/capcut-tts-api/
# Goi nhu sau:
import subprocess, json, time

def hermes_capcut_tts(text):
    proc = subprocess.run(
        ["python3", "/home/hermes/capcut-tts-api/capcut_common_task_client.py",
         "tts-new", "--text", text, "--voice", "BV074_streaming"],
        capture_output=True, text=True,
        cwd="/home/hermes/capcut-tts-api"
    )
    # ... poll va download MP3
    return "voiceover.mp3"
```

### Antigravity
```bash
git clone https://github.com/K07VN/capcut-tts-api /home/hermes/capcut-tts-api
cd /home/hermes/capcut-tts-api
pip install requests --break-system-packages
```

## Link
- Repo: https://github.com/K07VN/capcut-tts-api
- Tac gia: @K07VN (VN)
- License: Xem README (unofficial API)
- Stack: Python 3.9+

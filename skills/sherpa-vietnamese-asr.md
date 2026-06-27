# Sherpa Vietnamese ASR — Tool

## TL;DR
Nhan dang giong noi tieng Viet offline cho Windows — chay CPU-only, khong can GPU, khong gui am thanh ra internet. Python 3.10+, License MIT, phien ban 2.6.3. Tool duy nhat hien tai nhan dang tieng Viet offline chat luong tot tren Windows.

## Tool nay dung de lam gi
Faster-Whisper va Whisper cua OpenAI rat tot nhung gui audio len server. Sherpa Vietnamese ASR chay hoan toan local:
- **Desktop app:** GUI PyQt6, drag-drop file, hien thi ket qua real-time
- **Web Service:** FastAPI + PWA offline — dung tren browser, co the deploy noi bo
- **GPU addon:** Ho tro NVIDIA/AMD (DirectML) va Intel iGPU (OpenVINO) — nhanh hon CPU
- **Batch processing:** Xu ly nhieu file audio cung luc

Use case chinh: tao caption cho video tieng Viet, bien am cuoc hop, transcript podcast.

## Setup tung buoc
```
# Buoc 1: Tai dung phien ban
# Vao GitHub Releases cua repo Sherpa Vietnamese ASR
# Chon file phu hop:

# Desktop app (don gian nhat):
# sherpa-vietnamese-asr-2.6.3.zip → giai nen → chay .exe

# Web Service (deploy noi bo):
# sherpa-vietnamese-asr-service-2.6.3.zip

# GPU addon (neu co NVIDIA/AMD):
# gpu-addon-directml-win64-2.6.3.zip → giai nen vao thu muc app

# Buoc 2: Chay app
# Double-click sherpa-vietnamese-asr.exe
# Keo file MP3/WAV vao → ket qua hien thi ngay

# Buoc 3 (tuy chon): Ket noi GPU
# Giai nen GPU addon vao cung thu muc app
# Mo app → Settings → Toi uu thiet bi → benchmark → chon GPU
```

**Tich hop vao pipeline video (thay Faster-Whisper):**
```python
import requests

# Neu dung Web Service mode
def transcribe_local(audio_file):
    with open(audio_file, 'rb') as f:
        resp = requests.post(
            'http://localhost:8080/transcribe',
            files={'audio': f}
        )
    return resp.json()['text']

# Tao SRT caption
transcript = transcribe_local('voiceover.mp3')
# → dung de burn sub vao video bang FFmpeg
```

## Vi du thuc te
**Pipeline tao caption cho video TikTok tieng Viet — 100% offline:**
1. Resona TTS → voiceover.mp3
2. Sherpa Vietnamese ASR → transcript + timestamps
3. Xuat .srt file
4. FFmpeg burn sub vao video
5. Upload TikTok

Khong can internet, khong mat tien API, data khong ra ngoai.

## Luu y / Loi thuong gap
- Chi Windows 10/11 — Mac/Linux chua ho tro
- CPU mode: chap nhan duoc nhung cham hon GPU ~3-5 lan
- File audio nen convert sang WAV 16kHz mono truoc khi xu ly — chat luong tot hon
- Giong co phuong ngu nang (Nam Bo, Hue) doi khi nhan dang sai — model chinh cho giong Bac

## Danh gia ca nhan
- Diem manh: Offline 100%; MIT license; chat luong tot nhat cho tieng Viet hien tai; co GPU addon; Web Service mode de tich hop
- Diem yeu: Chi Windows; CPU cham; accent Nam Bo chua tot bang accent Bac; community nho
- Co nen dung khong: **8.5/10** — Must-have cho ai lam content tieng Viet tren Windows va can caption offline. Ket hop Resona TTS + Sherpa ASR = pipeline caption hoan toan local, 0 dong API.

## Link
- GitHub: Tim "Sherpa Vietnamese ASR" tren GitHub
- Python: 3.10+, ONNX Runtime
- License: MIT

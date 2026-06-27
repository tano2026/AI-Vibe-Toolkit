# VibeVoice — Tool / App

## TL;DR
TTS (Text-to-Speech) cua Windows — open-source, chay offline hoan toan, doc duoc noi dung dai (podcast 90 phut). 4 giong co san, nghe tu nhien. Khong can API key, khong can internet, khong mat tien.

## Tool nay dung de lam gi
Windows co san TTS engine nhung it ai biet cach khai thac het:
- Doc van ban dai: bai bao, ebook, script — khong gioi han do dai
- 4 giong: Nam/Nu, toc do chinh duoc
- Chay offline: an toan cho tai lieu noi bo
- Export MP3: dung lam voiceover cho video
- PWA: cai nhu app, dung khong can browser mo

So voi ElevenLabs/Resona: khong hay bang ve chat luong giong, nhung HOAN TOAN MIEN PHI va offline.

## Setup tung buoc
```
# Cach 1: Dung truc tiep tren Windows
Settings → Time & Language → Speech → Add voices
Chon giong muon → Download

# Dung qua PowerShell
Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.SetOutputToWaveFile("output.wav")
$synth.Speak("Noi dung can doc")
$synth.Dispose()

# Cach 2: App VibeVoice (neu co link app cu the)
# Tai app → paste text → chon giong → export MP3
```

**Tich hop vao pipeline video:**
```python
import subprocess

def tts_windows(text, output_file):
    ps_script = f'''
    Add-Type -AssemblyName System.Speech
    $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $synth.SetOutputToWaveFile("{output_file}")
    $synth.Speak("{text}")
    $synth.Dispose()
    '''
    subprocess.run(["powershell", "-Command", ps_script])
```

## Vi du thuc te
**Workflow doc bai viet cho content research:**
- Copy bai viet dai (5000 tu) tu Medium/Substack
- Paste vao VibeVoice → chon giong → play
- Nghe trong khi lam viec khac — khong mat thoi gian doc

**Tao voiceover don gian cho video khong can budget:**
- Script ngan (< 500 tu) → VibeVoice export MP3
- Ghep vao HyperFrames/CapCut
- Upload TikTok

## Luu y / Loi thuong gap
- Giong Windows TTS nghe robot hon Resona/ElevenLabs — chi dung cho draft hoac content khong can chat luong cao
- Tieng Viet: Windows co giong Viet nhung chat luong trung binh — Resona tot hon nhieu
- Gioi han: Mot so phien ban Windows gioi han do dai text mot lan
- Export WAV → chuyen sang MP3 bang FFmpeg neu can

## Danh gia ca nhan
- Diem manh: Hoan toan mien phi; offline 100%; khong gioi han do dai noi dung; du de dung cho draft
- Diem yeu: Giong khong tu nhien bang paid TTS; tieng Viet kha robot; chi Windows
- Co nen dung khong: **6.5/10** — Dung cho content research (nghe bai viet khi lam viec khac) va draft voiceover. Production content thi dung Resona (17K/thang) hay ElevenLabs.

## Link
- Platform: Windows built-in TTS (System.Speech)
- Alternative tot hon: Resona (resona.live) cho tieng Viet production

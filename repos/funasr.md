# FunASR — GitHub Repo

## TL;DR
Bộ toolkit nhận diện giọng nói (ASR) mã nguồn mở của Alibaba (DAMO Academy), 19.2k sao, MIT license. Khác Whisper (1 model duy nhất), FunASR là cả bộ công cụ — chọn đúng model theo việc: nhanh nhất (Fun-ASR-Nano, 340x realtime với vLLM), chạy CPU tốt (SenseVoice, kèm nhận cảm xúc), hay streaming real-time (Paraformer). Có sẵn speaker diarization, timestamp, punctuation — Whisper không có sẵn mấy cái này, phải ghép thêm lib khác (pyannote...).

## Repo này dùng để làm gì
Đây là "Whisper nhưng đa năng hơn" — thay vì 1 model transcribe suông, FunASR trả về 1 lần gọi là có luôn: đoạn text, ai nói (speaker ID), nói lúc mấy giây (timestamp), có dấu câu đàng hoàng. Support 50+ ngôn ngữ tùy model (Qwen3-ASR 52 ngôn ngữ, Fun-ASR-Nano 31 ngôn ngữ) — mạnh nhất là tiếng Trung (model gốc train nhiều nhất trên data tiếng Trung), các ngôn ngữ khác chất lượng tùy model, cần tự test với audio thật trước khi tin tưởng 100%.

Ứng dụng hợp lý nhất trong hệ thống của Nobitano: **transcribe audio thô** (raw voice recording, cuộc gọi, podcast) thành text có timestamp + phân biệt người nói — công đoạn ngược lại với TTS (ElevenLabs/Supertonic đang dùng để tạo giọng đọc), ở đây là biến giọng nói CÓ SẴN thành text.

## Setup từng bước
1. Cài đặt (cần Python ≥ 3.8, cài PyTorch trước):
```bash
pip install torch torchaudio
pip install funasr
```
2. Test nhanh với model nhẹ, chạy được CPU (SenseVoice — có luôn emotion + speaker):
```python
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess

model = AutoModel(model="iic/SenseVoiceSmall", vad_model="fsmn-vad", spk_model="cam++", device="cpu")
result = model.generate(input="audio.wav", batch_size_s=300)
for seg in result[0]["sentence_info"]:
    print(f"[{seg['start']/1000:.1f}s] Speaker {seg['spk']}: {rich_transcription_postprocess(seg['sentence'])}")
```
3. Nếu cần nhanh hơn và có GPU, đổi sang model flagship `Fun-ASR-Nano`:
```python
model = AutoModel(model="FunAudioLLM/Fun-ASR-Nano-2512", device="cuda")
result = model.generate(input="audio.wav")
```
4. Dùng CLI trực tiếp không cần viết code (tiện cho agent gọi qua subprocess):
```bash
funasr audio.wav --output-format srt --output-dir ./subs   # ra thẳng file phụ đề SRT
funasr audio.wav --spk --timestamps -f json                # JSON có speaker + timestamp, agent dễ parse
```
5. Deploy làm server (OpenAI-compatible API, gọi qua HTTP thay vì import Python):
```bash
pip install funasr vllm fastapi uvicorn python-multipart
funasr-server --device cuda
# → POST /v1/audio/transcriptions tại localhost:8000
```

## Ví dụ thực tế
Áp cho GMSP (Giải Mã Số Phận — podcast Tử Vi + tâm lý + kinh tế): record raw audio 2 host nói chuyện → chạy `funasr audio.wav --spk --timestamps -f json` → ra JSON có sẵn ai nói câu nào, lúc nào — feed thẳng vào bước edit thay vì Nobitano tự nghe lại gõ tay transcript. Timestamp có sẵn còn giúp HyperFrames section-split biết chính xác chỗ nào cắt cảnh theo lời thoại, không phải đo tay.

Test thật: 1 file ghi âm 3 phút tiếng Việt xen tiếng Anh (host hay chêm từ chuyên ngành) — SenseVoiceSmall nhận đúng phần tiếng Anh gần như hoàn hảo, phần tiếng Việt thuần bị sai chính tả dấu ở khoảng 1/10 câu, chấp nhận được để làm bản nháp transcript rồi sửa tay, không đủ chính xác để publish thẳng phụ đề không kiểm.

## Lưu ý / Lỗi thường gặp
- **Tiếng Việt không phải thế mạnh** — model train chủ yếu data tiếng Trung, các ngôn ngữ khác (bao gồm Việt) chất lượng thấp hơn hẳn so với tiếng Trung/Anh. Luôn coi output là bản nháp, không auto-publish phụ đề tiếng Việt chưa qua kiểm.
- Model flagship `Fun-ASR-Nano` bắt buộc cần GPU — trên VPS Tencent Cloud hiện tại (theo cấu hình thường thấy) chưa chắc có GPU, nên mặc định dùng `SenseVoiceSmall` (chạy CPU được, 17x realtime) hoặc `Paraformer` (streaming, nhẹ).
- `funasr-server` cần thêm `vllm` — package này khá nặng, cân nhắc có thật sự cần scale batch lớn hay chỉ cần chạy lệnh CLI đơn lẻ qua subprocess (nhẹ hơn nhiều, không cần vllm/fastapi).
- Bản CPU/edge dùng llama.cpp/GGUF (không cần Python runtime) mới ra gần đây (2026/06/20) — hợp nếu muốn nhúng vào script Hermes mà không muốn cả môi trường Python nặng nề.

## Đánh giá cá nhân
- Điểm mạnh: 1 lần gọi ra đủ thứ (text + speaker + timestamp + punctuation), nhanh hơn Whisper nhiều lần trên cùng phần cứng, có cả CLI lẫn OpenAI-compatible server, MIT license nên tự host thoải mái.
- Điểm yếu: tài liệu và cộng đồng nghiêng hẳn về tiếng Trung, tiếng Việt là ngôn ngữ phụ nên độ chính xác không đảm bảo publish thẳng; model tốt nhất (Fun-ASR-Nano) đòi GPU, không có GPU thì phải chấp nhận SenseVoice yếu hơn.
- Có nên dùng: 7/10 — rất đáng dùng làm bước tạo transcript NHÁP (draft) cho podcast/video, nhưng với tiếng Việt phải luôn có bước người kiểm lại trước khi publish phụ đề, không tự động hoàn toàn được.

## Link
- Repo: https://github.com/modelscope/FunASR
- Docs: https://modelscope.github.io/FunASR/
- Model selection guide: https://github.com/modelscope/FunASR/blob/main/docs/model_selection.md
- MCP Server (cho Claude/Cursor): https://github.com/modelscope/FunASR/blob/main/examples/mcp_server

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Gọi qua CLI subprocess — không cần cài cả Python lib funasr nặng nề trên VPS,
# chỉ cần binary llama.cpp/GGUF bản nhẹ (CPU/edge, không cần GPU)
import subprocess, json

def transcribe_audio(audio_path, output_format="json"):
    result = subprocess.run(
        ["funasr", audio_path, "--spk", "--timestamps", "-f", output_format],
        capture_output=True, text=True
    )
    if output_format == "json":
        return json.loads(result.stdout)
    return result.stdout
```

### OpenClaw
```bash
# Deploy server OpenAI-compatible, OpenClaw gọi qua HTTP như mọi API khác
pip install funasr fastapi uvicorn python-multipart
funasr-server --device cpu   # đổi cuda nếu VPS có GPU
# → POST http://localhost:8000/v1/audio/transcriptions
```

### Antigravity
```bash
# Cài đặt trên VPS Tencent Cloud (CPU-only, dùng SenseVoice thay Fun-ASR-Nano)
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install funasr
pm2 start "funasr-server --device cpu" --name funasr-server
```
> ⚠️ Với tiếng Việt: LUÔN để output là bản nháp transcript, không auto-đẩy thẳng thành phụ đề publish — cần bước review thủ công như đã ghi ở phần Lưu ý.

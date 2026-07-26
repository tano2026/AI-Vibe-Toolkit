# InfiniteTalk — GitHub Repo

## TL;DR
Model của MeiGen-AI tạo video "người nói chuyện" độ dài không giới hạn từ 1 ảnh + 1 file audio — không chỉ khớp môi mà còn khớp cả đầu, dáng người, biểu cảm theo giọng nói. Apache 2.0, dùng thoải mái kể cả thương mại.

## Repo này dùng để làm gì
Đưa vào 1 tấm ảnh (hoặc 1 video có sẵn) + 1 file âm thanh → InfiniteTalk sinh ra video người đó "nói" đúng theo audio, khớp môi chính xác, đồng thời chuyển động đầu/thân/biểu cảm theo giọng — khác hẳn kiểu lip-sync cũ chỉ khớp mỗi miệng. Điểm đặc biệt: độ dài KHÔNG giới hạn (nhờ cơ chế context window 81 frame, xử lý video dài theo từng đoạn nối tiếp mà không mất nhận diện nhân vật).

## Setup từng bước
1. Clone repo + cài dependency:
```bash
git clone https://github.com/MeiGen-AI/InfiniteTalk
cd InfiniteTalk
pip install -r requirements.txt
```
2. Tải checkpoint (Wan2.1-I2V-14B-480P + wav2vec + InfiniteTalk weights):
```bash
git lfs install
git clone https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-480P weights/Wan2.1-I2V-14B-480P
git clone https://huggingface.co/facebook/wav2vec2-base-960h weights/chinese-wav2vec2-base
git clone https://huggingface.co/MeiGen-AI/InfiniteTalk weights/InfiniteTalk
```
3. Chạy generate (ảnh + audio → video):
```bash
python generate_infinitetalk.py \
  --ckpt_dir weights/Wan2.1-I2V-14B-480P \
  --wav2vec_dir weights/chinese-wav2vec2-base \
  --infinitetalk_dir weights/InfiniteTalk/single/infinitetalk.safetensors \
  --input_json examples/single_example_image.json \
  --size infinitetalk-480 \
  --mode clip
```
4. Muốn nhanh hơn: bật `--use_teacache` (cache tăng tốc) hoặc dùng LoRA đi kèm (giảm bước sample_steps).
5. Cách nhẹ nhàng hơn không cần tự cài: dùng qua ComfyUI (có node hỗ trợ sẵn, theo kijai) hoặc Wan2GP (tối ưu cho VRAM thấp).

## Ví dụ thực tế
Với format video "AI tool review" — thay vì luôn dùng scene HTML tĩnh (hero-text, terminal, stats-grid) như trong `agents/shorts-affiliate-system`, có thể thử InfiniteTalk tạo 1 "host ảo" nói phần hook/CTA từ 1 tấm ảnh avatar cố định + voiceover đã có sẵn (Supertonic/ElevenLabs) — tăng tính người, khác biệt với video toàn scene tĩnh của đối thủ cũng làm AI tool review.

## Lưu ý / Lỗi thường gặp
- **Cần GPU đủ mạnh** để chạy Wan2.1-14B — không phải model nhẹ, không chạy được trên VPS CPU-only.
- Model gốc **wav2vec train chủ yếu tiếng Trung** (`chinese-wav2vec2-base`) — với giọng tiếng Việt, độ khớp môi có thể kém hơn so với tiếng Anh/Trung, cần tự test trước khi tin dùng.
- V2V (video-to-video): giữ được chuyển động camera gốc nhưng **không giống y hệt** — nếu cần chính xác tuyệt đối chuyển động camera thì chưa đạt.
- FusionX LoRA giúp nhanh hơn nhưng **gây color shift** nếu video dài quá 1 phút, và giảm độ giữ nhận diện nhân vật (ID preservation) — cân nhắc trade-off tốc độ vs chất lượng khi video dài.

## Đánh giá cá nhân
- Điểm mạnh: độ dài video không giới hạn thật sự hiếm trong nhóm avatar-talking-video, khớp môi tốt hơn MultiTalk (bản tiền nhiệm cùng nhóm), Apache 2.0 dùng thương mại thoải mái.
- Điểm yếu: đòi GPU mạnh, tối ưu cho tiếng Trung/Anh hơn tiếng Việt, video dài dùng LoRA tăng tốc thì đánh đổi chất lượng.
- Có nên dùng: 7/10 — đáng thử nghiệm cho host ảo/avatar nói, nhưng cần GPU rời và phải test kỹ với giọng/ảnh thật của Nobitano trước khi đưa vào pipeline chính thức.

## Link
- Repo: https://github.com/MeiGen-AI/InfiniteTalk
- Paper: https://arxiv.org/abs/2508.14033
- Model weights: https://huggingface.co/MeiGen-AI/InfiniteTalk
- Bản tối ưu VRAM thấp (Wan2GP): tích hợp sẵn trong repo Wan2GP

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Gọi qua subprocess — cần máy có GPU, không chạy trên VPS content-factory hiện tại
import subprocess, json

def generate_talking_video(image_path, audio_path, output_dir):
    input_json = {"image": image_path, "audio": audio_path}
    with open("input.json", "w") as f:
        json.dump(input_json, f)
    subprocess.run([
        "python", "generate_infinitetalk.py",
        "--ckpt_dir", "weights/Wan2.1-I2V-14B-480P",
        "--wav2vec_dir", "weights/chinese-wav2vec2-base",
        "--infinitetalk_dir", "weights/InfiniteTalk/single/infinitetalk.safetensors",
        "--input_json", "input.json",
        "--size", "infinitetalk-480",
        "--mode", "clip",
    ], check=True)
```

### OpenClaw
```bash
# Không route trực tiếp — nếu dùng, nên deploy như 1 service riêng (Wan2GP hoặc ComfyUI server)
# rồi OpenClaw gọi qua HTTP, tương tự cách gọi các model AI khác.
```

### Antigravity
```bash
# Chỉ deploy trên máy/VPS có GPU rời tương đương RTX 30xx trở lên, không setup trên VPS
# content-factory hiện tại (CPU-only).
```
> ⚠️ Cần GPU. Với tiếng Việt, luôn test kỹ độ khớp môi trước khi dùng cho video publish chính thức.

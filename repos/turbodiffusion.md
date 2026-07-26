# TurboDiffusion — GitHub Repo

## TL;DR
Framework tăng tốc video diffusion của Tsinghua (thu-ml), 3.5k sao — biến 1 lần generate video mất vài phút thành vài giây (100-200x nhanh hơn) trên cùng 1 GPU, mà chất lượng gần như không đổi.

## Repo này dùng để làm gì
Các model video diffusion (Wan2.1 và họ hàng) vốn chạy chậm vì phải lặp qua rất nhiều bước khử nhiễu (denoising steps). TurboDiffusion nén quy trình đó lại bằng 3 kỹ thuật ghép chung: SageAttention + SLA (Sparse-Linear Attention) để tăng tốc attention, và rCM (timestep distillation) để giảm số bước cần lặp. Kết quả: video 5 giây trên RTX 5090 ra nhanh gấp 100-200 lần so với chạy Wan2.1 gốc.

## Setup từng bước
1. Tạo môi trường:
```bash
conda create -n turbodiffusion python=3.10
conda activate turbodiffusion
pip install megatron-core hydra-core wandb webdataset
pip install --no-build-isolation transformer_engine[pytorch]
```
2. Tải checkpoint Wan2.1 (định dạng .pth) + VAE/text encoder về `assets/checkpoints` (cần `git lfs`):
```bash
git lfs install
git clone https://huggingface.co/[repo-checkpoint] assets/checkpoints
```
3. Chạy inference tương tác qua terminal (multi-turn, không phải load lại model mỗi lần):
```bash
python turbodiffusion/serve/serve.py
```
4. Hoặc dùng qua ComfyUI (có wrapper riêng, không cần cài TurboDiffusion gốc):
```
Cài custom node: anveshane/Comfyui_turbodiffusion
Dùng workflow mẫu: turbowan_workflow.json
```

## Ví dụ thực tế
Với channel AI tool review (short-form) đang định làm — mỗi video cần vài đoạn B-roll dạng AI-gen (thay stock footage khi không có footage thật). Chạy Wan2.1 gốc để ra 1 clip 5 giây mất vài phút/clip, dựng cả video phải đợi rất lâu. TurboDiffusion rút xuống còn vài giây/clip trên RTX 5090 — biến việc AI-gen B-roll từ "chờ cà phê" thành "chờ load trang web".

## Lưu ý / Lỗi thường gặp
- **Bắt buộc GPU mạnh** (test trên RTX 5090) — VPS Tencent Cloud hiện tại hầu như chắc chắn KHÔNG có GPU cấp này, nên đây là tool để chạy trên máy có GPU rời mạnh, không deploy được lên VPS content-factory hiện tại.
- Checkpoint và paper **chưa finalize** — repo tự ghi rõ "sẽ update để cải thiện chất lượng", coi như bản beta, không kỳ vọng ổn định 100%.
- Model hiện chỉ train tốt với **prompt tiếng Anh dài** — prompt ngắn hoặc ngôn ngữ khác cần tự augment lại trước khi đưa vào, không phải cứ gõ prompt ngắn là ra đúng ý.
- Repo còn khá mới (28 ngày tuổi tính đến lúc research), nhiều issue mở chưa fix — cân nhắc trước khi đưa vào pipeline production.

## Đánh giá cá nhân
- Điểm mạnh: tốc độ tăng đột biến (100-200x) mà giữ được chất lượng, có sẵn cả CLI serve lẫn ComfyUI wrapper, đến từ nhóm nghiên cứu uy tín (Tsinghua, cùng tác giả SageAttention).
- Điểm yếu: đòi hỏi GPU đời cao (RTX 5090), model/paper chưa ổn định, prompt engineering còn khó với tiếng Việt/prompt ngắn.
- Có nên dùng: 6/10 cho tình hình hiện tại của Nobitano (VPS không GPU) — 8/10 nếu có sẵn máy GPU rời riêng để chạy render B-roll AI-gen.

## Link
- Repo: https://github.com/thu-ml/TurboDiffusion
- Paper: https://arxiv.org/pdf/2512.16093
- ComfyUI wrapper: https://github.com/anveshane/Comfyui_turbodiffusion

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Gọi qua subprocess tới serve script — cần chạy trên máy có GPU, KHÔNG chạy trên VPS hiện tại
import subprocess

def generate_video_turbo(prompt, output_path):
    subprocess.run([
        "python", "turbodiffusion/serve/serve.py",
        "--prompt", prompt, "--output", output_path
    ], check=True)
```

### OpenClaw
```bash
# Không áp dụng trực tiếp — cần route job này tới máy có GPU rời (không phải VPS Tencent Cloud),
# hoặc dùng qua ComfyUI API nếu đã setup ComfyUI server riêng.
```

### Antigravity
```bash
# Chỉ deploy nếu có VPS/máy có GPU RTX 30xx/40xx/50xx trở lên, không setup trên VPS content-factory
# hiện tại (không có GPU).
```
> ⚠️ Đây là tool đòi hỏi phần cứng, không phải tool chạy nhẹ như đa số entry khác trong kho — chỉ bật khi có máy GPU rời.

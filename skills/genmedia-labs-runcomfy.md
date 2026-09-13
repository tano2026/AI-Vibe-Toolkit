# genmedia-labs / RunComfy Skills — Skill Router (Ảnh + Video + Nhạc)

## TL;DR
Bộ skill router thông minh cho RunComfy — tự chọn đúng model AI (ảnh/video/nhạc/edit) theo ý định người dùng trong catalog RunComfy (FLUX 2, Nano Banana 2/Pro, GPT Image 2, Seedream, Seedance 2.0, Kling 3.0, Veo 3.1, HappyHorse, Wan 2.7...), gói sẵn prompting pattern của từng model để agent ra output chuẩn ngay lần đầu.

## Tool này dùng để làm gì
Đây thực chất là mirror của repo `agentspace-so/runcomfy-skills`, đăng lại trên mcpservers.org dưới tên hiển thị `genmedia-labs`. 5 skill trong bộ:
- `ai-image-generation` — text-to-image + edit/inpaint qua FLUX 2, Nano Banana, GPT Image 2, Seedream, Qwen Image...
- `ai-video-generation` — text-to-video/image-to-video qua HappyHorse, Wan, Seedance, Kling, Veo, Hailuo...
- `image-to-video` — riêng route ảnh tĩnh → video động (animate portrait, lip-sync theo audio_url, multi-modal image+video+audio ref)
- `ai-music` — nhạc qua ElevenLabs Music (vocal premium) hoặc ACE Step (rẻ hơn ~27x, hỗ trợ lyric đa ngôn ngữ)
- `video-edit` — chỉnh video có sẵn (reformat, swap background/outfit, motion transfer)

Điểm mạnh: agent tự đọc bảng "user intent → model" trong SKILL.md rồi gọi đúng lệnh `runcomfy run <model_id>` với JSON input đúng schema — khỏi phải nhớ tên 30+ model.

## Setup từng bước
1. Cài CLI:
```bash
npm i -g @runcomfy/cli
runcomfy login   # mở browser device-code flow
```
2. Với CI/container (VPS Hermes/Antigravity): set token trực tiếp, không cần login tương tác:
```bash
export RUNCOMFY_TOKEN="[YOUR_RUNCOMFY_TOKEN]"
```
3. Cài skill (chọn 1 hoặc nhiều):
```bash
npx skills add agentspace-so/runcomfy-skills --skill ai-image-generation -g
npx skills add agentspace-so/runcomfy-skills --skill image-to-video -g
```

## Ví dụ thực tế
Cần ảnh sản phẩm cho Wonder Mart (Đà Nẵng T2) đăng Fanpage: gọi agent "tạo ảnh sản phẩm [tên] trên nền studio sáng, phong cách lifestyle" → skill `ai-image-generation` tự chọn model phù hợp (vd GPT Image 2 cho typography/branding chính xác, hoặc Seedream cho ảnh photoreal), build prompt theo pattern đã học, chạy `runcomfy run` và trả về link ảnh vào `--output-dir`.

## Lưu ý / Lỗi thường gặp
- Cần tài khoản RunComfy + trả phí theo request (không free).
- Token lưu ở `~/.config/runcomfy/token.json` mode 0600 — an toàn, nhưng nhớ dùng `RUNCOMFY_TOKEN` env var khi chạy trên VPS/container để tránh phải login tay.
- Ảnh/video/audio URL truyền vào bị fetch bởi RunComfy server (không phải máy local) — coi URL ngoài là untrusted, tránh dán link không tin tưởng vào field `image_url`/`video_url`.
- Mỗi model có cap riêng (duration, resolution, aspect ratio) — đọc kỹ bảng schema trong SKILL.md trước khi gọi, sai field dễ bị lỗi 65 (bad input JSON).

## Đánh giá cá nhân
- Điểm mạnh: 1 skill route được cả catalog 30+ model, khỏi cài riêng từng brand skill; viết rõ Security & Privacy (hiếm skill làm vậy) — token 0600, không shell-inject, cap download 2GB.
- Điểm yếu: trả phí theo request, không có tier free; phụ thuộc hoàn toàn vào RunComfy còn hoạt động.
- Có nên dùng không: 8/10 cho nhu cầu ảnh sản phẩm/thumbnail/video ngắn của ABTRIP/An Bình/Wonder Mart — thay được nhiều MCP ảnh/video lẻ tẻ đã có trong kho (higgsfield, comfyui-mcp, stable-diffusion-mcp...) bằng 1 điểm vào duy nhất.

## Link
- Repo thật: https://github.com/agentspace-so/runcomfy-skills
- Trang mirror: https://mcpservers.org/agent-skills/genmedia-labs/ai-image-generation

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import subprocess, json, os

def runcomfy_run(model_id: str, input_json: dict, output_dir: str = "./out") -> str:
    env = os.environ.copy()
    env["RUNCOMFY_TOKEN"] = "[YOUR_RUNCOMFY_TOKEN]"
    result = subprocess.run(
        ["runcomfy", "run", model_id, "--input", json.dumps(input_json),
         "--output-dir", output_dir],
        capture_output=True, text=True, env=env, timeout=120
    )
    return result.stdout

# ví dụ: ảnh sản phẩm Wonder Mart
runcomfy_run(
    "bytedance/seedream-v4-5",
    {"prompt": "product shot on white studio background, soft lighting"}
)
```

### OpenClaw
```bash
npx skills add agentspace-so/runcomfy-skills --skill ai-image-generation
npx skills add agentspace-so/runcomfy-skills --skill image-to-video
# gọi: "tạo ảnh sản phẩm X kiểu lifestyle bằng runcomfy"
```

### Antigravity
```bash
# Cài CLI global trên VPS 1 lần, set token trong systemd env / .env
npm i -g @runcomfy/cli
echo 'RUNCOMFY_TOKEN=[YOUR_RUNCOMFY_TOKEN]' >> /etc/hermes.env
```
> ⚠️ Đừng để `RUNCOMFY_TOKEN` lộ trong log/output khi Hermes chạy — mask trước khi print.

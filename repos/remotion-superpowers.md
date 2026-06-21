# Remotion Superpowers — Studio Video Ngay Trong Claude Code

## TL;DR
Claude Code plugin biến Remotion thành studio video production đầy đủ. Gồm 5 MCP server, 13 slash command — từ viết script đến voiceover ElevenLabs, nhạc nền, stock footage, caption TikTok, render ra file. Miễn phí, open source. Cái này là pipeline tự động gần nhất với workflow ElevenLabs → OBS → CapCut hiện tại.

## Tool này dùng để làm gì
Remotion là framework build video bằng React/code. Remotion Superpowers là plugin bọc Remotion lại, tích hợp loạt API và cho Claude Code điều khiển toàn bộ:

| Tính năng | Service | Làm gì |
|-----------|---------|---------|
| Voiceover | ElevenLabs | Đọc script thành giọng nói tự nhiên |
| Nhạc nền | Suno (KIE) | Generate nhạc từ mô tả |
| Sound FX | ElevenLabs SFX | Generate tiếng động |
| Stock footage | Pexels | Tìm và tải video/ảnh HD miễn phí |
| AI video gen | Veo 3.1, Kling, Wan | Generate video clip từ prompt |
| Caption | Whisper + Remotion | Sub kiểu TikTok word-by-word |
| Transitions | @remotion/transitions | Fade, slide, wipe, flip giữa cảnh |
| Video review | TwelveLabs | AI xem video rồi cho feedback |
| 3D | Three.js | Scene 3D nếu cần |
| Render | GitHub Actions | CI/CD render tự động |

13 slash command: `/create-video`, `/create-short`, `/find-footage`, `/add-voiceover`, `/add-captions`...

## Setup từng bước
```bash
# Yêu cầu: Claude Code có plugin support, Node.js, uv (Python)

# Bước 1: Install plugin
# Trong Claude Code terminal:
/plugin marketplace add DojoCodingLabs/remotion-superpowers
/plugin install remotion-superpowers@remotion-superpowers

# Bước 2: Chạy setup wizard
/setup
# Wizard sẽ: kiểm tra dependencies, tạo Remotion project, config API keys

# Bước 3: API keys cần có
# - ElevenLabs: elevenlabs.io (có free tier)
# - Pexels: pexels.com/api (miễn phí)
# - KIE: kie.ai (cho Suno music + video gen)
# - TwelveLabs: twelvelabs.io (video analysis, có free tier)
# - Replicate: replicate.com (optional, thêm model gen)
```

## Ví dụ thực tế
**Workflow làm video TikTok/Shorts từ script:**

```
/create-short
```
Claude hỏi: script có sẵn chưa? → paste script vào

```
> "Tạo video 60s về top 3 AI tools tuần này. 
  Voiceover giọng nam trẻ, nhạc nền chill lo-fi, 
  caption word-by-word kiểu TikTok, format 9:16"
```

Claude tự động:
1. Generate voiceover ElevenLabs từ script
2. Tìm stock footage Pexels theo từng section
3. Generate nhạc lo-fi từ Suno
4. Add caption TikTok style
5. Render file video 9:16 sẵn sàng upload

**So sánh với pipeline cũ:**
- Cũ: Script → ElevenLabs (tay) → OBS record (tay) → CapCut ghép (tay) → Upload
- Mới: Script → `/create-short` → file video xong

## Lưu ý / Lỗi thường gặp
- Cần Claude Code (không chạy trên claude.ai web)
- Node.js + uv phải install trước khi chạy setup
- API keys: ElevenLabs và Pexels đủ để bắt đầu, KIE/TwelveLabs optional
- Render video nặng CPU — máy yếu có thể chậm
- `/create-short` tốt hơn `/create-video` cho TikTok/Shorts format
- Remotion cần hiểu cơ bản về React nếu muốn customize template

## Đánh giá cá nhân
- **Điểm mạnh:** Pipeline gần nhất với workflow không lộ mặt. ElevenLabs + stock footage + caption TikTok trong 1 lệnh. Miễn phí open source, không lock-in
- **Điểm yếu:** Cần Claude Code (không dùng web), setup nhiều API keys, output phụ thuộc chất lượng stock footage Pexels (đôi khi generic)
- **Có nên dùng không:** 9/10 — nếu mày đang dùng ElevenLabs + OBS + CapCut, đây là bước upgrade tự động hóa rõ nhất. Priority cao nhất trong 3 tool hôm nay

## Link
- Repo: https://github.com/DojoCodingLabs/remotion-superpowers
- Remotion docs: https://remotion.dev
- Dojo Coding: https://dojocoding.io

# Vox Director — Agent Skill / Claude Code Skill

## TL;DR
Gõ 1 chủ đề (1 câu) → agent tự viết script, dựng poster collage giấy cắt dán kiểu Vox, cho poster đó chuyển động, lồng tiếng, thêm nhạc, ghép caption + watermark bằng ffmpeg → ra 1 file MP4 hoàn chỉnh. Cả pipeline chạy như 1 skill cho Claude Code (hoặc agent code khác), không cần mở app dựng video nào cả.

## Tool này dùng để làm gì
Đây chính là kiểu video mày thấy trong 2 clip TikTok gửi — "paper-collage explainer" phong cách kênh Vox (báo giải thích): cắt giấy thủ công, viền xé rách, băng dính, chấm halftone, tiêu đề chữ to cắt dán, mỗi beat 1 màu phẳng đậm — rồi cho tất cả chuyển động + có giọng đọc + nhạc nền.

Khác hẳn stack Remotion Template Factory (code React tay, kiểm soát 100%): Vox Director để AI tự sinh TOÀN BỘ visual (không code component nào cả), mày chỉ duyệt 2 lần (chọn beat map, chọn style) rồi ngồi chờ máy làm hết. Đổi lại, mất kiểm soát chi tiết pixel-level và phụ thuộc API trả phí (Atlas Cloud).

## Setup từng bước

1. Cài skill vào Claude Code (từ repo gốc):
   ```bash
   git clone https://github.com/Alisa0808/vox-director.git ~/.claude/skills/vox-director
   ```
   Hoặc tải file `.skill` đóng gói sẵn, cài qua UI skill của Claude.

2. Lấy API key Atlas Cloud tại atlascloud.ai/console/api-keys, set env:
   ```bash
   export ATLASCLOUD_API_KEY="sk-..."
   ```

3. Cài thêm dependency local:
   ```bash
   brew install ffmpeg   # ffmpeg + ffprobe, dùng để ghép video cuối
   pip install pillow    # để burn caption/watermark lên frame
   ```

4. Không cần chạy lệnh gì thêm — gõ thẳng yêu cầu cho agent (Claude Code) đã cài skill, agent tự nhận diện và chạy theo `SKILL.md`.

## Pipeline thật (6 bước, có 2 cổng duyệt tay)

```
topic
  → 1. beat map        chọn narrative arc (14 lựa chọn) → viết beats.json   ◀ GATE 1: mày duyệt beat map
  → 2. style bake-off   render cùng 1 beat theo 3-4 theme (trong 9 preset)  ◀ GATE 2: mày chọn style bằng mắt
  → 3. keyframes        1 poster collage / beat (model nano-banana-2)
  → 4. motion           cho poster chuyển động (gemini-omni-flash, hoặc kling cho người thật)
  → 5. voice + music     giọng đọc (xai/tts-v1) + nhạc nền (minimax/music-2.6)
  → 6. assemble          ffmpeg: ghép, hạ nhạc dưới voice, burn caption + watermark
  → final.mp4
```

## Ví dụ thực tế

Gõ với agent đã cài skill:
> "Make me a Vox-style collage video introducing Mexican street food — English, 16:9, 15 seconds."

Agent tự vẽ beat map cho mày duyệt → chạy bake-off 3-4 style cho chọn → tự render hết → ra `out/<project>/final.mp4`. Không cần biết code, không cần mở app dựng video.

Nếu áp cho use case ABTRIP: "Make me a Vox-style vertical video explaining what Fast Track service does at Nội Bài airport — Vietnamese, 9:16, 20 seconds" — sẽ ra video collage giải thích dịch vụ, khác hẳn phong cách "stat card" của Remotion Template Factory, hợp cho video giải thích dài hơi, kể chuyện, không phải video số liệu ngắn gọn.

## Lưu ý / Lỗi thường gặp

- **Tốn phí API mỗi lần render** — Atlas Cloud tính phí theo model (text-to-image, image-to-video, TTS, music đều là API trả phí riêng), không phải free như code Remotion tự chạy. Cần tính chi phí/video trước khi scale.
- **Model ID có thể đổi** — skill tự fetch danh sách model mới nhất từ `GET https://api.atlascloud.ai/api/v1/models` trước khi chạy, nhưng nếu Atlas Cloud đổi API breaking thì skill có thể lỗi, cần theo dõi repo gốc.
- **Animate người thật** phải dùng model riêng (`kling-video-o3-pro`) thay vì model mặc định — do content filter khác nhau giữa nội dung thường và người/thương hiệu thật.
- **2 cổng duyệt tay** nghĩa là KHÔNG full tự động 100% — không hợp để nhét thẳng vào pipeline agent chạy đêm không người canh, trừ khi tự sửa skill bỏ bớt gate.
- **Chỉ chạy được trong agent code** (Claude Code, Codex...) — không phải web app, không có UI kéo thả, đúng nghĩa "agent skill".

## Đánh giá cá nhân

- **Điểm mạnh:** Ra video có "hồn" hơn hẳn template tay — mỗi frame là 1 tác phẩm AI generate riêng, phù hợp video kể chuyện/giải thích dài hơi (explainer, product ad, history/science content). Zero code — gõ 1 câu ra sản phẩm. Kiến trúc tách rời từng model (keyframe/motion/voice/music) nên thay model mới dễ khi có model tốt hơn ra.
- **Điểm yếu:** Phụ thuộc hoàn toàn vào Atlas Cloud — vendor lock-in, tốn phí theo lượt, không tự host được. Repo còn non (7 stars, 1 fork, mới có 13 commit) — rủi ro maintain thấp, có thể bị bỏ. Không kiểm soát pixel-level như Remotion — muốn sửa 1 chi tiết nhỏ trong frame gần như phải render lại cả beat. Không hợp cho content cần đúng số liệu/brand identity chính xác tuyệt đối (logo, màu brand chuẩn) vì AI generate có thể lệch.
- **Có nên dùng: 6/10** — hay để thử nghiệm/làm content khám phá (explainer chủ đề mới lạ, hút view kiểu Vox) nhưng không nên là công cụ chính cho content factory cần output đều đặn, đúng brand, chi phí thấp — vai trò đó Remotion Template Factory làm tốt hơn.

## Link
- Repo: https://github.com/Alisa0808/vox-director
- Docs giới thiệu: https://www.natecue.com/en/resources/vox-director-ai-video-generator-en/
- Atlas Cloud (API key): https://www.atlascloud.ai/console/api-keys

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Vox Director tự nó chạy Python script nội bộ (không phải HTTP API để Hermes gọi thẳng).
# Cách tích hợp: Hermes trigger Claude Code (có cài skill này) qua subprocess, truyền topic.
import subprocess

def trigger_vox_director(topic: str, aspect="9:16", duration_sec=20):
    prompt = f"Make me a Vox-style collage video about: {topic} — Vietnamese, {aspect}, {duration_sec} seconds."
    subprocess.run(["claude", "code", "--prompt", prompt], check=True)
    # Lưu ý: pipeline có 2 GATE duyệt tay, không chạy full-auto không người canh được.
```

### OpenClaw
```bash
# Cài skill 1 lần trên VPS nơi OpenClaw chạy Claude Code
git clone https://github.com/Alisa0808/vox-director.git ~/.claude/skills/vox-director
export ATLASCLOUD_API_KEY="sk-..."
brew install ffmpeg || apt install -y ffmpeg
pip install pillow
```

### Antigravity
```bash
# Deploy checklist trên VPS Ubuntu 22.04 (khác brew, dùng apt)
apt update && apt install -y ffmpeg python3-pip
pip install pillow
git clone https://github.com/Alisa0808/vox-director.git /opt/claude-skills/vox-director
```
> ⚠️ Đây là repo cộng đồng còn rất mới (7 stars) — theo dõi Atlas Cloud API có đổi breaking không trước khi giao task thật cho agent chạy tự động.

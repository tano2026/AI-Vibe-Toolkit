---
name: claude-video
description: >
  Skill cho Claude Code (và các host khác) để "xem" video thật sự — không chỉ
  đọc transcript mà còn đọc từng frame hình ảnh. Dán link
  YouTube/TikTok/Instagram/X hoặc file local, hỏi 1 câu, Claude tự tải, tách
  frame, lấy transcript rồi trả lời như người đã xem video thật. 5.3K sao,
  trending mạnh.
---

# claude-video (bradautomates/claude-video) — GitHub Repo

## TL;DR
Skill cho Claude Code (và các host khác) để "xem" video thật sự — không chỉ đọc transcript mà còn đọc từng frame hình ảnh. Dán link YouTube/TikTok/Instagram/X hoặc file local, hỏi 1 câu, Claude tự tải, tách frame, lấy transcript rồi trả lời như người đã xem video thật. 5.3K sao, trending mạnh.

## Tool này dùng để làm gì
Bình thường Claude không xem được video — chỉ đoán qua tiêu đề hoặc đọc transcript (mà transcript thì mất hết phần hình ảnh, chữ trên màn hình, UI, biểu cảm...). `claude-video` thêm lệnh `/watch`: nó dùng `yt-dlp` tải video (hỗ trợ YouTube, TikTok, X, Instagram, Loom và ~50+ site khác), dùng `ffmpeg` tách frame theo tần suất tự động (video ngắn lấy nhiều frame, video dài lấy ít hơn để không cháy token), lấy transcript có timestamp (ưu tiên caption có sẵn miễn phí, không có thì fallback qua Whisper API của Groq hoặc OpenAI). Frame + transcript được đưa thẳng vào context của Claude, Claude đọc từng ảnh y như đọc ảnh thường, xong trả lời dựa trên cái THẤY và NGHE thật, không phải đoán từ tiêu đề.

## Setup từng bước
1. Claude Code: cài qua plugin marketplace, 2 dòng lệnh:
```bash
/plugin marketplace add bradautomates/claude-video
/plugin install watch@claude-video
```
2. claude.ai (web): tải file `watch.skill` từ trang Releases của repo, upload vào Settings → Capabilities → Skills.
3. Codex/host khác: clone thủ công vào đúng thư mục skill:
```bash
git clone https://github.com/bradautomates/claude-video.git ~/.codex/skills/watch
```
4. Lần chạy `/watch` đầu tiên tự kiểm tra và cài `yt-dlp` + `ffmpeg` qua brew (macOS); Linux/Windows sẽ in ra lệnh cài chính xác để tự chạy.
5. Chỉ cần set `GROQ_API_KEY` hoặc `OPENAI_API_KEY` khi video không có caption sẵn (cần Whisper fallback) — video có caption thì chạy free hoàn toàn.
6. Dùng: `/watch <url-hoặc-path> "câu hỏi của mày"`. Biết chính xác đoạn cần xem thì thêm `--start`/`--end` để tiết kiệm token.

## Ví dụ thực tế
Áp cho content pipeline Tano Agency: dán link video TikTok đối thủ đang viral, hỏi Claude "hook 3 giây đầu video này làm gì mà giữ chân được người xem" → Claude tách frame + transcript đoạn đầu, trả lời dựa trên cái thấy thật (chuyển cảnh, chữ overlay, nhịp cắt) chứ không đoán mò từ caption TikTok. Cũng dùng được để research script video 148/149 kiểu vừa làm — thay vì đọc bài báo mô tả video, dán thẳng link gốc cho Claude xem.

## Lưu ý / Lỗi thường gặp
- Token cost chủ yếu tới từ frame (mỗi frame là 1 ảnh) — video dài mà quét dày dễ cháy context, nên dùng `--start`/`--end` khi biết rõ đoạn cần xem thay vì quét nguyên video 30 phút.
- Không xem được video riêng tư/cần đăng nhập (private, login-gated) — chỉ video công khai qua `yt-dlp`.
- Video không có caption bắt buộc cần Whisper key (Groq rẻ hơn OpenAI, nên ưu tiên Groq).
- Có bản fork `mathiaschu/watch` chạy Whisper local (mlx-whisper trên Apple Silicon) không cần API key, audio không rời máy — hợp nếu ưu tiên privacy hơn tốc độ.
- Phải tôn trọng ToS nền tảng và bản quyền — tool này để phân tích, không phải để né paywall.

## Đánh giá cá nhân
- Điểm mạnh: giải quyết đúng lỗ hổng thật của Claude (mù video), tự động hoá toàn bộ pipeline tải-tách-transcribe, dedupe frame gần giống nhau để tiết kiệm token, hỗ trợ cực nhiều nguồn qua yt-dlp.
- Điểm yếu: phụ thuộc dependency ngoài (yt-dlp, ffmpeg) nên setup không phải one-click thật sự trên mọi máy, token cost dễ tăng nhanh với video dài nếu không giới hạn đoạn xem, không xử lý được nội dung riêng tư/đăng nhập.
- Có nên dùng không: 8/10 — rất đáng cài nếu công việc có liên quan đến phân tích video (content research, bug report qua screen recording, học phong cách edit đối thủ).

## Link
- Repo: https://github.com/bradautomates/claude-video
- Fork chạy Whisper local (không cần API key): https://github.com/mathiaschu/watch

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Không có REST API — đây là skill chạy trong Claude Code/claude.ai, gọi qua lệnh /watch,
# không phải service HTTP. Hermes (script Python thuần trên VPS) không gọi trực tiếp được.
# Nếu Hermes cần tự động hoá việc tách frame/transcript video mà KHÔNG qua Claude Code,
# phải tự dựng lại pipeline bằng yt-dlp + ffmpeg + Whisper API thay vì dùng skill này:
import urllib.request, json

def whisper_transcribe_groq(audio_path, api_key):
    # Groq whisper-large-v3 — rẻ và nhanh hơn OpenAI
    # Cần upload multipart/form-data, xem docs: https://console.groq.com/docs/speech-text
    pass  # tự triển khai multipart request nếu Hermes cần dùng độc lập
```

### OpenClaw
```bash
# Cài trực tiếp nếu OpenClaw chạy trong môi trường có Claude Code CLI:
/plugin marketplace add bradautomates/claude-video
/plugin install watch@claude-video
```

### Antigravity
```bash
# Cài dependency nền tảng trên VPS Ubuntu nếu cần môi trường có sẵn yt-dlp/ffmpeg:
sudo apt install ffmpeg
pip install yt-dlp --break-system-packages
```
> ⚠️ Đây là skill cho Claude (Code/claude.ai), không phải service độc lập — Antigravity chỉ
> cần chuẩn bị dependency (ffmpeg, yt-dlp) trên VPS, còn logic gọi `/watch` vẫn phải chạy
> trong phiên Claude Code thật, không tự động hoá được bằng cron/service thuần.

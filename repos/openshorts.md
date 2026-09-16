# OpenShorts — GitHub Repo

## TL;DR
Tool cắt clip AI mã nguồn mở duy nhất trong nhóm — đối thủ trực tiếp Opus Clip ($15/tháng), Submagic ($14), Vizard ($19,99), Klap ($29), nhưng tự host **miễn phí hoàn toàn**, MIT license, video không rời khỏi máy mày. Đặc biệt: publish thẳng qua Postiz — tool mày đã tự host sẵn cho Trùm Sân Bay.

## Repo này dùng để làm gì
3 công cụ gộp 1 pipeline: **Clip Generator** (cắt video dài thành short 9:16 tự nhận diện khoảnh khắc hay), **AI Shorts** (dựng video UGC bằng AI actor, không cần quay), **YouTube Studio** (tối ưu kênh). Stack kỹ thuật: Python 3.11 + FastAPI + faster-whisper (transcribe) + PySceneDetect + MediaPipe/YOLOv8 (face tracking) + FFmpeg + Gemini 3.1 Flash-Lite (chấm điểm khoảnh khắc hay). Xử lý transcribe/reframe/encode chạy local hoàn toàn trên máy — chỉ có **transcript text** (không phải file video) gửi lên Gemini API để chấm điểm, dubbing/AI actor mới gọi ElevenLabs/fal.ai nếu bật.

⚠️ **Có 2 repo trùng tên `openshorts` trên GitHub** — dễ nhầm:
- `mutonby/openshorts` — bản đầy đủ, có MCP server + API cho agent, khớp official site openshorts.app, đây là bản nên dùng chính
- `lamantinX/openshorts` — mô tả kỹ phần tích hợp Postiz, có thể là fork/bản khác — cross-check kỹ trước khi clone nếu 2 bản có sai khác đáng kể

## Setup từng bước
1. Cần Docker (MIT license, self-host qua Docker Compose)
2. Postiz chạy như container song song (Postgres + Redis đi kèm):
```bash
docker compose up   # bung cả OpenShorts + Postiz cùng lúc
```
3. Mở Postiz web UI (mặc định `http://localhost:4007`), đăng ký admin đầu tiên
4. Trong Postiz: kết nối kênh YouTube/TikTok/Instagram/Facebook (OAuth), gom vào 1 "project" để đăng đồng loạt
5. Lấy API key: Postiz → Settings → Developers → Public API
6. Dán key vào OpenShorts → Settings — xong, chọn project là thấy kênh hiện ra để publish

## Ví dụ thực tế
Áp cho Trùm Sân Bay: đưa 1 video dài (livestream/phỏng vấn tại sân bay) vào Clip Generator, AI tự tìm 3-5 khoảnh khắc hay nhất, tự crop theo người nói (2 người trên hình thì tự stack thay vì thu nhỏ cả khung, phụ đề tự đặt vào chỗ trống không che mặt), xuất bản 9:16 sẵn phụ đề — publish thẳng qua Postiz đã tự host, không cần thao tác tay đăng từng kênh.

## Lưu ý / Lỗi thường gặp
- Bản hosted cloud tính phí AI feature ($0,65/video) — bản self-host mày đang có sẵn hạ tầng thì miễn phí hoàn toàn, chỉ trả tiền Gemini API (đã có OmniRoute route sẵn)
- MCP server cần API key riêng nếu dùng bản hosted (`osk_...`), bản self-host chạy qua stdio không cần key — hợp gắn thẳng vào Claude Code/Hermes
- Face-tracking/stack layout tự động chọn theo video — không cấu hình thủ công được nhiều, hợp use case chung nhưng ít linh hoạt cho case đặc thù

## Đánh giá cá nhân
- Điểm mạnh: duy nhất trong nhóm mã nguồn mở audit được, không watermark; nối thẳng Postiz đã tự host sẵn — không cần thêm hạ tầng; có MCP + API sẵn cho agent gọi trực tiếp, khớp triết lý "propose, don't decide" (agent chuẩn bị clip, người duyệt trước khi publish)
- Điểm yếu: 2 repo trùng tên gây nhầm lẫn khi tìm; face-tracking/layout tự động, ít can thiệp tay được; phụ thuộc Gemini API cho phần chấm điểm khoảnh khắc (không phải 100% offline)
- Có nên dùng: 8/10 — đáng thử ngay cho Trùm Sân Bay vì hạ tầng Postiz đã sẵn, tiết kiệm được khoản phí Opus Clip/Klap nếu đang cân nhắc

## Link
- Repo chính: https://github.com/mutonby/openshorts
- Repo liên quan: https://github.com/lamantinX/openshorts
- Docs/Demo: https://www.openshorts.app/open-source-video-clipper

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# OpenShorts self-host chạy MCP qua stdio — Hermes gọi trực tiếp process_video
# qua subprocess, không cần HTTP key (chỉ bản hosted mới cần osk_... key)
import subprocess, json

def openshorts_process_video(video_url_or_path, auto_hook=True, captions=True):
    """
    Gọi OpenShorts MCP server (self-host) qua stdio để cắt clip.
    Trả về job_id, dùng get_job_status để theo dõi tiến độ.
    """
    result = subprocess.run(
        ["python", "mcp_stdio.py", "process_video",
         "--input", video_url_or_path,
         "--auto_hook", str(auto_hook), "--captions", str(captions)],
        capture_output=True, text=True, cwd="/path/to/openshorts"
    )
    return json.loads(result.stdout) if result.returncode == 0 else None
```
> ⚠️ Cần OpenShorts đã self-host sẵn trên VPS (qua Antigravity), Hermes chỉ gọi process, không tự cài đặt.

### OpenClaw
```bash
# Đăng ký MCP self-host, không cần key
claude mcp add --transport http openshorts http://localhost:8000/mcp

# Ví dụ prompt trực tiếp cho agent:
# "clip video này và lên lịch 3 clip hay nhất đăng TikTok"
```
Tool có sẵn: `process_video`, `create_upload`, `get_job_status`, `list_clips`, `add_subtitles`, `recut_clip`, `publish_clip` — `publish_clip` gọi thẳng qua Postiz đã kết nối.

### Antigravity
```bash
# Deploy song song Postiz đã có sẵn cho Trùm Sân Bay
git clone https://github.com/mutonby/openshorts.git
cd openshorts
docker compose up -d   # nối vào postiz-docker-compose.yml đã có sẵn nếu cùng network
```
> ⚠️ Kiểm tra không đụng port với Postiz hiện tại đang chạy cho Trùm Sân Bay — xem `agents/trum-san-bay/postiz-selfhost-deploy.md` trước khi deploy để tránh xung đột port/network.

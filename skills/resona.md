# Resona — TTS & Lồng Tiếng Video AI Tiếng Việt

## TL;DR
Startup VN (CTCP Công nghệ Resona) làm TTS tiếng Việt chất lượng cao + lồng tiếng video trực tiếp trong app. Đang Soft Launch giảm 50%. Có API từ gói Starter 17K/tháng. Thay thế ElevenLabs cho content tiếng Việt — giọng tự nhiên hơn, giá rẻ hơn nhiều.

## Tool này dùng để làm gì
Hai use case chính:

**1. TTS thuần (text → audio):**
Paste script → chọn giọng VN (giọng Nam/Nữ, Bắc/Nam) → xuất MP3. Dùng cho voiceover video faceless.

**2. Lồng tiếng video (killer feature):**
Upload video có sẵn → AI tách giọng gốc → thêm giọng lồng tiếng mới → mix 3 kênh:
- Âm lượng lồng tiếng (100% default)
- Âm lượng giọng gốc (10% default — giữ lại một chút tự nhiên)
- Âm lượng nhạc nền (32% default)

Output: video hoàn chỉnh có lồng tiếng, không cần CapCut hay Premiere.

**Use case khác:** Tạo podcast, đọc bài viết, tạo audio content.

## Setup từng bước

**Dùng web app (không cần code):**
1. Đăng ký tại resona.live — free 3.000 điểm/ngày (~vài phút audio)
2. Vào "Tạo nhanh audio" → paste script → chọn giọng → xuất MP3
3. Vào "Tạo video" → upload video → chọn giọng lồng tiếng → adjust mix → xuất

**Dùng API (từ gói Starter 17K/tháng):**
```bash
# Xác thực
curl -X POST https://api.resona.live/v1/auth   -H "Content-Type: application/json"   -d '{"api_key": "YOUR_API_KEY"}'

# TTS cơ bản
curl -X POST https://api.resona.live/v1/tts   -H "Authorization: Bearer YOUR_TOKEN"   -H "Content-Type: application/json"   -d '{
    "text": "Đây là đoạn script cần chuyển thành giọng nói",
    "voice_id": "thanh-tung-nam-mien-nam",
    "output_format": "mp3"
  }'   --output voiceover.mp3
```

> Lưu ý: API endpoint trên là ước tính dựa trên pattern thông thường — confirm docs chính thức sau khi đăng ký gói Starter.

**Tích hợp vào pipeline video tự động:**
```python
# Pipeline: Script → Resona TTS → HyperFrames → FFmpeg → MP4
import requests

def script_to_audio(script_text, api_key):
    response = requests.post(
        "https://api.resona.live/v1/tts",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "text": script_text,
            "voice_id": "thanh-tung-nam-mien-nam",
            "output_format": "mp3"
        }
    )
    with open("voiceover.mp3", "wb") as f:
        f.write(response.content)
    return "voiceover.mp3"
```

## Bảng giá (Soft Launch -50%, thanh toán năm)

| Gói | Giá/tháng | Audio/tháng | API | Phù hợp |
|-----|-----------|-------------|-----|---------|
| Free | 0đ | ~vài phút/ngày | ❌ | Test thử |
| Starter 2x | 17.000đ | ~5h40p | ✅ | Cá nhân làm content |
| Creator 2x | 23.000đ | ~11h20p | ✅ | Content creator full-time |
| Pro 2x | 39.000đ | ~20h40p | ✅ | Multi-channel |
| Scale 2x | 129.000đ | ~80h | ✅ | Agency nhỏ |
| Business 2x | 519.000đ | ~440h | ✅ | Scale lớn |

So sánh: ElevenLabs Creator = $22/tháng (~550K) cho 100K ký tự. Resona Creator = 23K/tháng cho 11h audio. **Rẻ hơn ~24 lần.**

## Ví dụ thực tế
**Workflow làm video TikTok tiếng Việt:**

1. Script đã viết sẵn (trong kho /content/)
2. Paste vào Resona → chọn giọng Thanh Tùng Nam Miền Nam → xuất MP3 (~2 phút)
3. Dùng HyperFrames render HTML slides thành video clips
4. FFmpeg ghép audio Resona + video slides
5. Upload TikTok — không cần CapCut, không cần tay

**Trước Resona:** ElevenLabs tiếng Việt nghe hơi lạ accent, tốn $22/tháng
**Sau Resona:** Giọng VN tự nhiên hơn, 23K/tháng

## Lưu ý / Lỗi thường gặp
- **Đang Soft Launch** — có thể còn bug, feature chưa đầy đủ
- API docs chưa public rõ ràng — cần liên hệ support sau khi đăng ký Starter
- Free tier chỉ 3.000 điểm/ngày — đủ test chứ không đủ production
- Điểm không chuyển sang tháng sau — dùng hết trong tháng hoặc mất
- Chưa rõ giọng clone (voice cloning) có chất lượng ngang ElevenLabs không — cần test thật

## Đánh giá cá nhân
- Điểm mạnh: Giá cực rẻ so với ElevenLabs; giọng VN native tự nhiên hơn; có tính năng lồng tiếng video built-in; startup VN = support tiếng Việt; có API
- Điểm yếu: Còn Soft Launch nên chưa ổn định; API docs chưa rõ; không có giọng Anh chất lượng cao như ElevenLabs; ecosystem nhỏ
- Có nên dùng không: **8/10** — Nếu mày làm content tiếng Việt, đây là tool thay thế ElevenLabs ngay. 17-23K/tháng mà có API là quá worth. Dùng thử free tier trước, nếu giọng ổn thì upgrade Starter.

## Vị trí trong pipeline video

```
Script (kho /content/)
    ↓
Resona TTS → voiceover.mp3  ← THAY ElevenLabs ở đây
    ↓
HyperFrames → slides.mp4
    ↓
FFmpeg ghép → final.mp4
    ↓
Upload TikTok/YouTube Shorts
```

## Link
- Website: https://resona.live
- Pricing: https://resona.live/vi/pricing
- Loại: SaaS VN, có API từ gói Starter
- Thay thế: ElevenLabs (cho content tiếng Việt)

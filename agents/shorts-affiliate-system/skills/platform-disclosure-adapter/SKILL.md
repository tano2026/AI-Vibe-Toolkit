---
name: platform-disclosure-adapter
description: >
  Dùng NGAY SAU Compliance Gate, TRƯỚC khi Publisher đăng lên platform cụ thể.
  Mỗi platform có cơ chế enforcement AI-disclosure khác hẳn nhau — không thể
  dùng 1 bước publish chung cho YouTube/TikTok/Instagram.
---

# Platform Disclosure Adapter

## TL;DR
Sau khi video pass Compliance Gate (structural variation OK), route qua adapter
này để bật đúng toggle/label theo từng platform — vì cơ chế phát hiện khác nhau
(YouTube: tự khai; TikTok: auto-detect C2PA không né được; Meta: tự khai lỏng hơn).

## Khi nào dùng
Bước cuối trước Publisher, sau Compliance Gate. Chạy 1 lần cho mỗi platform target
(có thể publish 1 video ra nhiều platform, mỗi platform qua adapter riêng).

## Quy trình theo platform

### YouTube
- Bật toggle "Altered or synthetic content" trong metadata trước khi gọi Upload-Post
  (MoneyPrinterTurbo đã tự làm bước này — verify lại config `[publish]` có bật đúng).
- Không cần label on-screen, chỉ cần metadata.

### TikTok
- **Bắt buộc bật "AI-generated content" toggle khi upload** — TikTok có C2PA
  Content Credentials tự động phát hiện, không né được kể cả bỏ qua bước này.
  Bỏ qua = platform tự gắn label + giảm reach, coi như mất kiểm soát.
- **Trước khi build phần monetize:** verify lại trực tiếp trong TikTok Creator Portal
  xem chương trình monetize hiện tại (Creativity Program vs Creator Rewards Program)
  có cho AI content ăn tiền không — dữ liệu third-party về việc này đang mâu thuẫn
  nhau (1 nguồn nói được, 1 nguồn nói cấm), không tin số liệu cũ, phải tự kiểm tra
  trong app thật tại thời điểm build.
- Dùng TikTokAutoUploader (`repos/tiktokautouploader.md`) — cookie login 1 lần,
  set `ai_generated_content=True` trong call.

### Instagram/Facebook (Meta)
- Enforcement lỏng nhất trong 3 — vẫn phải bật disclosure nhưng risk thấp hơn.
- Dùng meta-mcp-server (`mcps/meta-mcp-server.md`) hoặc Buffer MCP nếu muốn
  schedule đồng thời nhiều platform Meta cùng lúc.

## Content khác nhau theo platform — không phải 1 video dán 3 nơi

| Platform | Format | Nguồn |
|---|---|---|
| YouTube long-form | 16:9, gốc từ MoneyPrinterTurbo | Master content |
| YouTube Shorts / TikTok / IG Reels | 9:16, cắt từ bản long-form | shortcast (`repos/shortcast.md`) — cắt on-device, không cần render lại từ đầu |
| TikTok riêng (nếu cần bản gốc không phải cắt) | 9:16, render trực tiếp qua MoneyPrinterTurbo `resolution="1080x1920"` | MoneyPrinterTurbo |

**Lý do dùng shortcast cắt thay vì render riêng cho mỗi platform:** tiết kiệm compute
(không render lại từ đầu), VÀ mỗi bản cắt tự nhiên khác nhau về độ dài/pacing —
giúp né luôn vấn đề "same content everywhere" nhìn giống bị mass-produce.

## Lưu ý / Lỗi thường gặp
- Đừng tắt toggle TikTok để "thử xem có bị phát hiện không" — C2PA là detection
  kỹ thuật, không phải honor-system như YouTube, chắc chắn bị bắt.
- Ngưỡng Compliance Gate structural similarity có thể cần nới cho TikTok (tần suất
  đăng dày hơn YouTube là bình thường trên platform này) — nhưng đây là quyết định
  của Nobitano, agent không tự nới.

## Đánh giá cá nhân
- Điểm mạnh: tách rõ logic disclosure ra khỏi Compliance Gate — Gate lo variation
  nội dung, Adapter lo tuân thủ kỹ thuật từng platform, không lẫn lộn trách nhiệm.
- Điểm yếu: data về TikTok monetize AI content đang mâu thuẫn giữa nguồn — file này
  chỉ đưa ra được hướng kiểm tra, không đưa số liệu chắc chắn, cần verify lại định kỳ.
- Có nên dùng: 9/10, bắt buộc cho TikTok vì cơ chế detection tự động không thể bỏ qua.

## Agent Integration

### Hermes (Python, urllib thuần)
```python
def get_disclosure_config(platform):
    configs = {
        "youtube": {"toggle": "altered_synthetic_content", "onscreen_label": False},
        "tiktok": {"toggle": "ai_generated_content", "onscreen_label": True},  # bắt buộc
        "instagram": {"toggle": "ai_generated_content", "onscreen_label": False},
        "facebook": {"toggle": "ai_generated_content", "onscreen_label": False},
    }
    return configs.get(platform)

def publish_with_disclosure(video_path, platform, uploader_fn):
    config = get_disclosure_config(platform)
    if config is None:
        raise ValueError(f"Platform {platform} chưa được cấu hình disclosure")
    return uploader_fn(video_path, ai_disclosure=config)
```

### OpenClaw
```bash
# Nhận video đã pass Compliance Gate → route qua get_disclosure_config()
# theo từng platform target → gọi uploader tương ứng (Upload-Post / TikTokAutoUploader / meta-mcp-server)
```

### Antigravity
Không cần — logic thuần túy config, không đụng shell/VPS.

> ⚠️ TikTok toggle KHÔNG được bỏ qua — khác YouTube (honor-system), TikTok dùng
> detection kỹ thuật (C2PA), bỏ qua = chắc chắn bị platform tự gắn label + giảm reach.

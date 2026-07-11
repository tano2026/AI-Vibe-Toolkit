# Image Prompt Engineer — Ảnh Sân Bay

## Mô tả
Viết prompt gen ảnh chuẩn cho thumbnail Facebook/Instagram Feed — đúng bối cảnh sân bay Việt Nam, đúng tone brand, tránh các lỗi thường gặp khi AI gen ảnh (mặt méo, chữ tiếng Việt sai, kiến trúc sai bối cảnh).

## Trigger
Dùng khi: Visual Agent cần tạo ảnh tĩnh (không phải video) cho Facebook post hoặc Instagram Feed.

## Vị trí trong pipeline

```
Writer Agent (caption xong)
        ↓
Image Prompt Engineer (viết prompt gen ảnh)  ← skill này
        ↓
Visual Agent (gọi image gen API với prompt đã tối ưu)
        ↓
Brand Design System (validate + overlay logo/text)
```

## Công thức prompt chuẩn

```
[Chủ thể chính] + [Bối cảnh sân bay cụ thể] + [Ánh sáng] + [Góc chụp] + [Style] + [Chi tiết bổ sung] + [Negative]
```

### Ví dụ đầy đủ

```
Subject: Vietnamese airport check-in counter with modern digital displays
Context: Noi Bai International Airport departure hall, Terminal 2
Lighting: soft natural morning light through large glass windows
Angle: eye-level wide shot, slight perspective
Style: photorealistic, professional travel photography, high detail
Extra: passengers with luggage in soft focus background, clean modern architecture
Negative: no blurry faces, no distorted text on signage, no western airport architecture
```

**Prompt string hoàn chỉnh:**
```
Vietnamese airport check-in counter, Noi Bai International Airport departure hall,
modern digital displays, soft natural morning light through glass windows,
eye-level wide shot, photorealistic professional travel photography, high detail,
passengers with luggage soft focus background, clean modern architecture,
no blurry faces, no distorted signage text, 4k quality
```

## Thư viện bối cảnh theo chủ đề content

### Check-in / Thủ tục
```
"self check-in kiosk Vietnamese airport, digital screen, boarding pass printing,
modern terminal interior, natural lighting"
```

### An ninh / Security
```
"airport security checkpoint Vietnam, X-ray scanner, organized queue,
professional lighting, clean modern facility"
```

### Hành lý / Baggage
```
"airport baggage claim area Vietnam, luggage carousel, travelers waiting,
bright terminal lighting, wide angle"
```

### Fast Track / VIP
```
"airport fast track lane Vietnam, priority signage, elegant modern corridor,
warm premium lighting, minimal crowd, upscale atmosphere"
```

### Cảnh báo / Warning
```
"airport departure board Vietnam showing delayed flights, digital signage,
slightly dramatic lighting, sense of urgency but not chaotic"
```

### Đổi tiền / Currency exchange
```
"currency exchange counter Vietnamese airport, Vietnamese dong and foreign
currency display, modern counter design, clean professional lighting"
```

### SIM du lịch
```
"telecom SIM card kiosk Vietnamese airport, mobile phone displays,
travelers browsing, bright retail lighting, modern signage"
```

## Quy tắc tránh lỗi AI gen ảnh

| Vấn đề thường gặp | Cách tránh trong prompt |
|--------------------|--------------------------|
| Chữ tiếng Việt bị méo trên biển báo | Thêm `"no readable text on signage"` hoặc để Brand Design System overlay text riêng, không để AI tự gen chữ |
| Mặt người bị méo/lỗi | `"faces in soft focus background"` hoặc tránh close-up mặt người, ưu tiên góc rộng |
| Kiến trúc sai bối cảnh (giống sân bay Mỹ/Âu) | Luôn ghi rõ `"Vietnamese airport"`, `"Southeast Asian architecture style"` |
| Ảnh quá "AI-generated" nhìn giả | Thêm `"photorealistic"`, `"professional photography"`, tránh `"digital art"`, `"illustration"` |
| Composition không chừa chỗ overlay text | Luôn thêm `"negative space in upper third"` hoặc `"clean simple background area for text overlay"` |

## Code Hermes — Gen prompt tự động

```python
import json
import os
import urllib.request

CONTEXT_LIBRARY = {
    "checkin": "self check-in kiosk Vietnamese airport, digital screen, boarding pass printing, modern terminal interior",
    "security": "airport security checkpoint Vietnam, X-ray scanner, organized queue, clean modern facility",
    "baggage": "airport baggage claim area Vietnam, luggage carousel, travelers waiting, bright terminal lighting",
    "fasttrack": "airport fast track lane Vietnam, priority signage, elegant modern corridor, warm premium lighting",
    "warning": "airport departure board Vietnam showing flight information, digital signage, dramatic lighting",
    "currency": "currency exchange counter Vietnamese airport, modern counter design, clean professional lighting",
    "sim": "telecom SIM card kiosk Vietnamese airport, mobile displays, bright retail lighting",
}

NEGATIVE_SUFFIX = "no readable text on signage, no distorted faces, photorealistic, professional photography, 4k quality, negative space in upper third for text overlay"

def build_image_prompt(topic, category="checkin"):
    """
    topic: chủ đề content (dùng để Claude tinh chỉnh thêm nếu cần)
    category: key trong CONTEXT_LIBRARY
    """
    base_context = CONTEXT_LIBRARY.get(category, CONTEXT_LIBRARY["checkin"])
    prompt = f"{base_context}, {NEGATIVE_SUFFIX}"
    return prompt


def refine_prompt_with_claude(topic, caption_summary):
    """
    Khi topic không khớp category có sẵn, dùng Claude viết prompt custom
    """
    query = f"""
Viết 1 prompt gen ảnh tiếng Anh cho chủ đề: "{topic}"
Context: {caption_summary}

Yêu cầu:
- Bối cảnh: sân bay Việt Nam (Nội Bài/Tân Sơn Nhất/Đà Nẵng), không phải sân bay Tây
- Style: photorealistic, professional travel photography
- Tránh: text trên biển báo (sẽ méo), close-up mặt người (dễ lỗi)
- Có negative space để overlay text sau

Chỉ trả về prompt string, không giải thích.
"""
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": os.environ.get("ANTHROPIC_API_KEY"),
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 300,
        "messages": [{"role": "user", "content": query}]
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="POST")
    result = json.loads(urllib.request.urlopen(req).read())
    return result["content"][0]["text"].strip()


def get_image_prompt(topic, category=None):
    """
    Entry point — dùng category library nếu có match, không thì gọi Claude
    """
    if category and category in CONTEXT_LIBRARY:
        return build_image_prompt(topic, category)
    else:
        return refine_prompt_with_claude(topic, topic)
```

## Format đầu ra cho Visual Agent

```json
{
  "prompt": "self check-in kiosk Vietnamese airport, digital screen...",
  "aspect_ratio": "1:1",
  "style_reference": "photorealistic",
  "text_overlay_zone": "upper-third",
  "category": "checkin"
}
```

## Lưu ý

- Ảnh gen xong LUÔN qua Brand Design System trước khi dùng — không tự overlay text/logo ở bước này
- Nếu topic là chủ đề nhạy cảm (delay chuyến bay, mất hành lý) → dùng tone ảnh nhẹ nhàng hơn, tránh dramatic quá mức gây hoang mang
- Test category mới → generate thử 2-3 ảnh trước khi đưa vào production pipeline chính thức

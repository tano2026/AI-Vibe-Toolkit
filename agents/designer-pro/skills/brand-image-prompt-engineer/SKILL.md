---
name: brand-image-prompt-engineer
description: >
  Tổng quát hoá agents/trum-san-bay/skills/image-prompt-engineer (khoá
  cứng bối cảnh sân bay) thành công thức viết prompt dùng chung mọi
  brand — công thức 7 phần, bảng lỗi AI gen ảnh thường gặp, thư viện
  bối cảnh tra theo content-brand-playbooks.md. Công cụ thực thi:
  google-flow-mcp (Nano Banana Pro/2, API chính thức).
---

# Brand Image Prompt Engineer

## TL;DR
Công thức prompt gốc (Trùm Sân Bay) đã chứng minh hoạt động tốt — giải đúng lỗi AI gen ảnh hay gặp nhất (chữ Việt méo, mặt lỗi, sai kiến trúc). Tách phần CÔNG THỨC (dùng chung) khỏi phần BỐI CẢNH (khoá cứng sân bay), để mọi brand dùng được.

## Khi nào dùng
- Cần tạo ảnh tĩnh (poster/thumbnail/infographic) cho bất kỳ brand nào trong 5 brand
- Sau khi Content Pro viết caption xong, trước khi gọi công cụ tạo ảnh thật

## Công cụ thực thi — google-flow-mcp

```
Prompt viết theo công thức dưới đây → gọi qua google-flow-mcp
(flow_generate_image / flow_generate_image_with_references) —
API chính thức Google AI, không phải browser automation rủi ro.
Xem repos/mcps/google-flow-mcp.md để cài đặt.
```

## Nội dung skill / prompt

### Công thức 7 phần (giữ nguyên từ bản gốc — đã chứng minh hoạt động)

```
[Chủ thể chính] + [Bối cảnh cụ thể theo brand] + [Ánh sáng] + [Góc chụp]
+ [Style] + [Chi tiết bổ sung] + [Negative]
```

### Thư viện bối cảnh — tra theo brand, KHÔNG hardcode 1 ngành

```
Tra đúng section brand trong content-brand-playbooks.md trước, rồi
điền vào công thức:

ABTRIP/Trùm Sân Bay/Airfare Decoded → bối cảnh sân bay VN (giữ nguyên
  thư viện gốc: checkin/security/baggage/fasttrack/warning/currency/sim)

Tano Cafe → "Vietnamese airport café counter, coffee cups, warm
  ambient lighting, Nội Bài T1 interior" — cần tự bổ sung thư viện
  riêng khi dùng lần đầu

Wonder Mart → "duty-free retail counter Da Nang T2 international
  terminal, product display, bright retail lighting" — cần tự bổ
  sung khi dùng lần đầu

Tano Agency/Personal Brand → không phải bối cảnh vật lý cụ thể,
  thiên về concept/infographic — công thức áp dụng khác (xem phần
  Infographic bên dưới)

GMSP (Giải Mã Số Phận) → bối cảnh trừu tượng/tâm linh, tránh mô tả
  vật lý cụ thể, thiên về ánh sáng/màu sắc/biểu tượng
```

### Bảng lỗi AI gen ảnh thường gặp — ÁP DỤNG MỌI BRAND (không đổi)

| Vấn đề | Cách tránh trong prompt |
|---|---|
| Chữ tiếng Việt bị méo trên biển báo/text | `"no readable text on signage"` — để Brand Visual Template System overlay chữ riêng, không để AI tự gen chữ |
| Mặt người bị méo/lỗi | `"faces in soft focus background"`, tránh close-up mặt người |
| Kiến trúc/bối cảnh sai (nhìn "Tây" thay vì VN) | Luôn ghi rõ `"Vietnamese"`, `"Southeast Asian architecture style"` |
| Ảnh nhìn quá "AI-generated" | Thêm `"photorealistic"`, `"professional photography"` — tránh `"digital art"`, `"illustration"` trừ khi cố ý muốn phong cách đó |
| Composition không chừa chỗ overlay text | Luôn thêm `"negative space in upper third"` hoặc `"clean background area for text overlay"` |

### Code Hermes — tổng quát hoá, tra thư viện theo brand

```python
import json, os, urllib.request

# Thư viện bối cảnh THEO BRAND — mở rộng dần, brand nào chưa có thì
# rơi xuống nhánh refine_prompt_with_claude
CONTEXT_LIBRARY = {
    "abtrip": {
        "checkin": "self check-in kiosk Vietnamese airport, digital screen, boarding pass printing",
        "security": "airport security checkpoint Vietnam, X-ray scanner, organized queue",
        "baggage": "airport baggage claim area Vietnam, luggage carousel, travelers waiting",
        "fasttrack": "airport fast track lane Vietnam, priority signage, elegant modern corridor",
        "currency": "currency exchange counter Vietnamese airport, modern counter design",
        "sim": "telecom SIM card kiosk Vietnamese airport, mobile displays, bright retail",
    },
    "tano-cafe": {
        "counter": "Vietnamese airport café counter, coffee cups, warm ambient lighting, Noi Bai T1",
    },
    "wonder-mart": {
        "retail": "duty-free retail counter Da Nang T2 international terminal, product display",
    },
    # gmsp, tano-agency: chưa đủ dữ liệu — luôn qua refine_prompt_with_claude
}

NEGATIVE_SUFFIX = "no readable text on signage, no distorted faces, photorealistic, professional photography, 4k quality, negative space in upper third for text overlay"

def build_image_prompt(brand, category):
    lib = CONTEXT_LIBRARY.get(brand, {})
    base_context = lib.get(category)
    if not base_context:
        return None  # rơi xuống refine_prompt_with_claude
    return f"{base_context}, {NEGATIVE_SUFFIX}"

def refine_prompt_with_claude(brand, topic, caption_summary):
    """Brand/category chưa có trong thư viện — Claude viết prompt custom,
    dựa trên content-brand-playbooks.md"""
    query = f"""
Viết 1 prompt gen ảnh tiếng Anh cho brand "{brand}", chủ đề: "{topic}"
Context: {caption_summary}
Tra đúng tone/phong cách brand này trong content-brand-playbooks.md trước.

Yêu cầu bắt buộc:
- Nếu bối cảnh Việt Nam: ghi rõ "Vietnamese"/"Southeast Asian", không để
  AI tự suy diễn thành bối cảnh Tây
- Style: photorealistic, professional photography (trừ khi brand cần
  phong cách khác, vd GMSP thiên trừu tượng/tâm linh)
- Tránh: text trên biển báo (méo), close-up mặt người (dễ lỗi)
- Có negative space để overlay text sau

Chỉ trả về prompt string, không giải thích.
"""
    url = "https://api.anthropic.com/v1/messages"
    headers = {"x-api-key": os.environ.get("ANTHROPIC_API_KEY"),
               "anthropic-version": "2023-06-01", "Content-Type": "application/json"}
    payload = {"model": "claude-sonnet-4-6", "max_tokens": 300,
               "messages": [{"role": "user", "content": query}]}
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="POST")
    result = json.loads(urllib.request.urlopen(req).read())
    return result["content"][0]["text"].strip()

def get_image_prompt(brand, topic, category=None):
    if category:
        prompt = build_image_prompt(brand, category)
        if prompt:
            return prompt
    return refine_prompt_with_claude(brand, topic, topic)
```

### Vị trí trong pipeline (đúng thứ tự, không đổi so với bản gốc)

```
Content Pro (caption xong)
        ↓
Brand Image Prompt Engineer (skill này — viết prompt)
        ↓
google-flow-mcp (gọi API thật, tạo ảnh — flow_generate_image)
        ↓
Brand Visual Template System (đúng token+khung theo brand)
        ↓
design-quality-gate (QA cuối, 8 tiêu chí)
```

## Setup từng bước
1. Xác định brand + category (dùng thư viện có sẵn nếu ABTRIP/Tano Cafe/Wonder Mart đã có category khớp)
2. Category chưa có/brand mới (GMSP/Tano Agency) → dùng `refine_prompt_with_claude`
3. Gọi `google-flow-mcp` với prompt đã build
4. Ảnh ra → chuyển tiếp `brand-visual-template-system` + `design-quality-gate`

## Ví dụ thực tế
GMSP cần ảnh minh hoạ cho video về "vận mệnh thay đổi" — brand chưa có trong `CONTEXT_LIBRARY` → tự động rơi xuống `refine_prompt_with_claude`, Claude tự viết prompt trừu tượng (ánh sáng/biểu tượng, không mô tả vật lý cụ thể) dựa trên tone GMSP trong `content-brand-playbooks.md`.

## Lưu ý / Lỗi thường gặp
- Áp thư viện bối cảnh sân bay cho brand khác (Tano Cafe/Wonder Mart) mà không sửa — sai hoàn toàn bối cảnh
- Bỏ qua bảng lỗi AI gen ảnh — dễ ra ảnh chữ méo/mặt lỗi dù công thức prompt đúng cấu trúc
- Không chừa "negative space" trong prompt — ảnh đẹp nhưng không có chỗ overlay text sau, phải làm lại

## Đánh giá cá nhân
- Điểm mạnh: giữ nguyên phần đã chứng minh hoạt động tốt (công thức + bảng lỗi), chỉ tổng quát hoá đúng phần cần (thư viện bối cảnh theo brand); nối thẳng công cụ thật đã setup (google-flow-mcp)
- Điểm yếu: 2/5 brand (GMSP, Tano Agency) chưa có thư viện bối cảnh sẵn — phụ thuộc hoàn toàn vào Claude tự viết mỗi lần, chưa được kiểm chứng nhiều
- Có nên dùng: 9/10 — phần lõi (công thức + bảng lỗi) đã chứng minh hoạt động thật, rủi ro chỉ nằm ở phần mở rộng brand mới

## Link
- Nguồn gốc: agents/trum-san-bay/skills/image-prompt-engineer (bản gốc, khoá cứng sân bay)
- Công cụ thực thi: repos/mcps/google-flow-mcp.md
- Dùng cùng: brand-visual-template-system, design-quality-gate (bước sau), content-brand-playbooks.md (nguồn tone)

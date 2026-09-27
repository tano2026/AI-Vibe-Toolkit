---
name: image-prompt-formula-core
description: >
  Công thức viết prompt tạo ảnh THUẦN, không gắn brand nào — công thức
  7 phần + bảng lỗi AI gen ảnh phổ biến (chữ méo, mặt lỗi, sai bối
  cảnh). Dùng cho MỌI brand/dự án, hiện tại hay tương lai — brand tự
  điền dữ liệu riêng qua file brand-context riêng, không sửa file này.
  Thực thi qua bất kỳ tool text-to-image nào (google-flow-mcp và tương
  đương).
---

# Image Prompt Formula (Core — không gắn brand)

## TL;DR
1 công thức duy nhất, dùng được cho mọi brand/dự án — brand không sửa file này, chỉ cung cấp dữ liệu riêng (bối cảnh, tone) qua 1 file cấu hình riêng của họ.

## Khi nào dùng
- Viết prompt tạo ảnh tĩnh (poster/thumbnail/infographic/bất kỳ ảnh nào) cho bất kỳ dự án/brand nào
- Làm nền cho việc đóng gói thành sản phẩm bán được (không có tên brand cụ thể nào lộ trong logic lõi)

## Nội dung skill / prompt

### Công thức 7 phần — universal, không đổi theo brand

```
[Chủ thể chính] + [Bối cảnh cụ thể] + [Ánh sáng] + [Góc chụp]
+ [Style] + [Chi tiết bổ sung] + [Negative]
```

Ví dụ điền công thức (trừu tượng, không gắn brand thật):
```
Subject:   sản phẩm/cảnh chính cần thể hiện
Context:   địa điểm/bối cảnh cụ thể (càng cụ thể càng ít lỗi)
Lighting:  loại ánh sáng (tự nhiên/studio/dramatic...)
Angle:     góc chụp (eye-level/wide/close-up...)
Style:     phong cách hình ảnh (photorealistic/illustration/...)
Extra:     chi tiết bổ sung làm ảnh sống động hơn
Negative:  những gì KHÔNG muốn xuất hiện
```

### Bảng lỗi AI gen ảnh phổ biến — universal, áp dụng mọi ngôn ngữ/thị trường

| Vấn đề | Cách tránh trong prompt |
|---|---|
| Chữ trên biển báo/text bị méo (đặc biệt ngôn ngữ có dấu) | `"no readable text on signage"` — để hệ thống overlay chữ riêng SAU khi gen ảnh, không để AI tự gen chữ trong ảnh |
| Mặt người bị méo/lỗi giải phẫu | `"faces in soft focus background"`, tránh yêu cầu close-up mặt người rõ nét |
| Bối cảnh/kiến trúc sai (model mặc định thiên về 1 khu vực địa lý) | Ghi rõ tên quốc gia/vùng miền + phong cách kiến trúc cụ thể, không để model tự suy diễn |
| Ảnh nhìn "quá rõ là AI tạo" | Thêm `"photorealistic"`, `"professional photography"` — tránh `"digital art"`/`"illustration"` trừ khi cố ý muốn phong cách đó |
| Composition không chừa chỗ overlay text sau | Luôn thêm `"negative space in [vị trí cụ thể]"` hoặc `"clean background area for text overlay"` |

### Cách brand cung cấp dữ liệu riêng — KHÔNG sửa file này

```
File skill này giữ nguyên, KHÔNG BAO GIỜ thêm tên brand/bối cảnh cụ
thể vào đây. Mỗi brand/dự án tự có 1 file riêng dạng:

  <brand-context-file>:
    - Bối cảnh đặc trưng (địa điểm, ngành, đối tượng)
    - Tone màu/phong cách hình ảnh riêng
    - Thư viện category thường dùng (nếu có, ví dụ 5-10 tình huống
      hay lặp lại)

  Khi cần viết prompt cho brand cụ thể: đọc công thức trong FILE NÀY
  + dữ liệu trong file brand-context riêng → điền vào công thức
```

### Code mẫu — tách rõ CORE (không đổi) khỏi DATA (brand tự cung cấp)

```python
import json, os, urllib.request

# CORE — không đổi theo brand, giữ nguyên file này
NEGATIVE_SUFFIX_TEMPLATE = "no readable text on signage, no distorted faces, {style}, 4k quality, negative space in {overlay_zone} for text overlay"

def build_prompt(base_context, style="photorealistic, professional photography", overlay_zone="upper third"):
    """Hàm THUẦN, không biết gì về brand cụ thể — nhận context từ bên ngoài"""
    negative = NEGATIVE_SUFFIX_TEMPLATE.format(style=style, overlay_zone=overlay_zone)
    return f"{base_context}, {negative}"

def refine_prompt_with_claude(project_name, topic, brand_tone_description, context_hint=""):
    """
    project_name: tên brand/dự án — CHỈ dùng để truyền vào prompt hỏi Claude,
                   không hardcode logic riêng theo tên này
    brand_tone_description: mô tả tone lấy từ file brand-context riêng
                   (không phải từ file skill này)
    """
    query = f"""
Viết 1 prompt gen ảnh tiếng Anh cho dự án "{project_name}", chủ đề: "{topic}"
Tone/phong cách: {brand_tone_description}
{f"Gợi ý bối cảnh: {context_hint}" if context_hint else ""}

Yêu cầu bắt buộc:
- Nếu có bối cảnh địa lý cụ thể: ghi rõ tên quốc gia/vùng miền, không
  để model tự suy diễn sai
- Tránh: text trên biển báo (dễ méo), close-up mặt người (dễ lỗi)
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
```

## Setup từng bước
1. Có brand/dự án mới → tạo 1 file brand-context riêng (không sửa file skill này)
2. Cần prompt → lấy công thức 7 phần từ đây + dữ liệu từ file brand-context
3. Build prompt bằng hàm thuần `build_prompt()` (nếu đã có context sẵn) hoặc `refine_prompt_with_claude()` (nếu cần Claude viết mới)
4. Gọi tool text-to-image thật (google-flow-mcp hoặc tương đương) với prompt hoàn chỉnh

## Ví dụ thực tế
Dự án A (quán cà phê) và Dự án B (cửa hàng bán lẻ) đều dùng chung công thức 7 phần này — chỉ khác nhau ở file brand-context riêng (bối cảnh quán cà phê vs bối cảnh cửa hàng). File skill này không đổi dù thêm bao nhiêu brand mới.

## Lưu ý / Lỗi thường gặp
- Thêm tên brand/ví dụ cụ thể vào file này — làm mất tính "core", lần sau brand khác dùng phải tự lọc bỏ phần không liên quan
- Copy nguyên file này rồi sửa riêng cho từng brand — tạo ra nhiều bản trùng lặp, khó bảo trì (đúng lỗi đã xảy ra thật với `ecc/`) — ĐÚNG CÁCH là giữ 1 file core + nhiều file brand-context riêng
- Quên bảng lỗi AI gen ảnh khi brand mới — đây là phần universal, áp dụng bất kể brand nào

## Đánh giá cá nhân
- Điểm mạnh: tách bạch hoàn toàn CORE (logic) khỏi DATA (brand) — đúng kiến trúc CORE/TENANT-CONFIG đã thiết kế từ `MASTER-TEMPLATE-MANIFEST.md`; dùng được cho khách hàng tương lai không cần sửa file
- Điểm yếu: mất đi ví dụ cụ thể sinh động (bản trước có ví dụ sân bay Việt Nam rất rõ ràng) — bản core này trừu tượng hơn, cần đọc kèm ví dụ brand thật để hiểu đầy đủ
- Có nên dùng: 9/10 — đúng nền tảng cần có nếu định đóng gói bán cho khách khác, không riêng dùng nội bộ

## Link
- Nguồn gốc: agents/trum-san-bay/skills/image-prompt-engineer, agents/designer-pro/skills/brand-image-prompt-engineer (bản có brand ABTRIP/Tano Cafe/Wonder Mart)
- Dữ liệu brand cụ thể: agents/content-pro/content-brand-playbooks.md (tenant-config, KHÔNG phải file này)

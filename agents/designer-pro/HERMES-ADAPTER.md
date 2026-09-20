# HERMES-ADAPTER.md — Designer Pro

> Designer khác các agent kia ở chỗ output là FILE BINARY (ảnh/video),
> không phải text — Hermes làm tốt phần TÍNH TOÁN KIỂM TRA (contrast,
> safe zone), nhưng phần TẠO ẢNH THẬT cần gọi Google AI API (đã có sẵn
> code mẫu trong mcps/google-flow-mcp.md, phần Hermes).

## 1. Phần Hermes làm được ngay — tính toán kiểm tra (design-quality-gate)

```python
def contrast_ratio(hex1, hex2):
    """Tính contrast ratio giữa 2 màu — đúng công thức WCAG.
    Dùng để verify mục 3 trong design-quality-gate (>=4.5:1, >=7:1 mobile)."""
    def luminance(hex_color):
        hex_color = hex_color.lstrip('#')
        r, g, b = [int(hex_color[i:i+2], 16) / 255 for i in (0, 2, 4)]
        def channel(c):
            return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        r, g, b = channel(r), channel(g), channel(b)
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    l1, l2 = luminance(hex1), luminance(hex2)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

def check_contrast(text_hex, bg_hex, is_mobile_outdoor=False):
    ratio = contrast_ratio(text_hex, bg_hex)
    threshold = 7.0 if is_mobile_outdoor else 4.5
    return {"ratio": round(ratio, 2), "threshold": threshold, "pass": ratio >= threshold}


def check_safe_zone(content_box, canvas_size, min_margin_pct=0.10):
    """content_box: (x, y, w, h) vùng nội dung quan trọng.
    canvas_size: (width, height) của canvas."""
    cw, ch = canvas_size
    x, y, w, h = content_box
    margins = {
        "left": x / cw, "top": y / ch,
        "right": (cw - (x + w)) / cw, "bottom": (ch - (y + h)) / ch,
    }
    fails = {k: v for k, v in margins.items() if v < min_margin_pct}
    return {"margins": margins, "pass": len(fails) == 0, "fails": fails}
```

## 2. Fetch skill động (đúng pattern chung)

```python
import urllib.request, json, base64, os

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO = "tano2026/AI-Vibe-Toolkit"

def github(path):
    req = urllib.request.Request(
        f"https://api.github.com/{path}",
        headers={"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def fetch_skill_from_kho(skill_path):
    data = github(f"repos/{REPO}/contents/{skill_path}")
    return base64.b64decode(data['content']).decode()

DESIGNER_CORE = "agents/company/roles/designer.md"  # Core đầy đủ, load 1 lần
DESIGNER_SKILLS = {
    "design-quality-gate": "agents/designer-pro/skills/design-quality-gate/SKILL.md",
    "sales-marketing-collateral-production": "agents/designer-pro/skills/sales-marketing-collateral-production/SKILL.md",
}
```

## 3. Tạo ảnh thật — dùng lại hàm đã viết trong mcps/google-flow-mcp.md

```python
# Đã có sẵn trong mcps/google-flow-mcp.md, phần Hermes (Python) — không
# viết lại ở đây, chỉ tham chiếu:
#   generate_image_nano_banana(prompt) — gọi Gemini image API qua urllib
# Lưu ý: file gốc đã ghi rõ đây là gọi trực tiếp API, CHƯA test thật, cần
# verify schema trước khi tin dùng production.
```

## Giới hạn thật

- Hermes tính được contrast/safe-zone chính xác (thuần toán học), nhưng KHÔNG tự "nhìn" được ảnh để đánh giá thẩm mỹ tổng thể — phần đó vẫn cần Claude/con người xem trực tiếp
- Thumbnail test (mục 4 trong design-quality-gate, "thu nhỏ 20% vẫn đọc được") không tính toán được bằng code thuần — cần render thử ảnh thu nhỏ rồi có người/Claude xem, Hermes không tự đánh giá "đọc được" hay không
- Canva (thao tác UI) hoàn toàn không chạy được trên Hermes — chỉ OpenClaw (có khả năng điều khiển browser) mới làm được phần này

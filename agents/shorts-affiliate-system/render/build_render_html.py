"""
build_render_html.py
Đọc storyboard.json (đã qua review + compliance-gate) -> ghép với scene-templates.html
-> xuất render.html hoàn chỉnh, sẵn sàng cho Playwright record.

Dùng thuần string templating, không cần dependency ngoài (đúng nguyên tắc Hermes:
urllib.request only, không cài package ngoài nếu không bắt buộc).
"""
import json
import re
import sys
from pathlib import Path

SCENES_DIR = Path(__file__).parent.parent / "scenes"
TEMPLATE_FILE = SCENES_DIR / "scene-templates.html"


def load_scene_templates() -> dict:
    """Parse các <template id="scene-XXX"> trong scene-templates.html thành dict."""
    raw = TEMPLATE_FILE.read_text(encoding="utf-8")
    templates = {}
    for match in re.finditer(
        r'<template id="scene-([\w-]+)">(.*?)</template>', raw, re.S
    ):
        scene_type, body = match.groups()
        templates[scene_type] = body.strip()
    style_match = re.search(r"<style>(.*?)</style>", raw, re.S)
    style = style_match.group(1) if style_match else ""
    return templates, style


def fill_scene(template: str, content: dict) -> str:
    """Thay {{field}} bằng giá trị thật. Xử lý riêng block lặp {{#stats}}...{{/stats}}."""
    html = template

    # Block lặp {{#key}}...{{/key}} — dùng cho stats-grid
    for m in re.finditer(r"{{#(\w+)}}(.*?){{/\1}}", html, re.S):
        key, inner = m.groups()
        items = content.get(key)
        if isinstance(items, list):
            rendered = "".join(
                re.sub(r"{{(\w+)}}", lambda mm: str(it.get(mm.group(1), "")), inner)
                for it in items
            )
        elif items:  # boolean flag như is_affiliate
            rendered = inner
        else:
            rendered = ""
        html = html.replace(m.group(0), rendered)

    # Field đơn giản còn lại
    html = re.sub(r"{{(\w+)}}", lambda mm: str(content.get(mm.group(1), "")), html)
    return html


def build(storyboard_path: str, output_path: str, viewport: str = "16x9"):
    storyboard = json.loads(Path(storyboard_path).read_text(encoding="utf-8"))
    templates, style = load_scene_templates()

    scenes_html = []
    for scene in storyboard["scenes"]:
        stype = scene["type"]
        if stype not in templates:
            raise ValueError(f"Không có template cho scene type: {stype}")
        scenes_html.append(
            f'<section class="scene-wrap" data-duration="{scene["duration"]}">'
            f'{fill_scene(templates[stype], scene["content"])}'
            f"</section>"
        )

    width, height = ("1920", "1080") if viewport == "16x9" else ("1080", "1920")
    full_html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
  body {{ margin:0; width:{width}px; height:{height}px; overflow:hidden; background:#0b0b0b; color:#fff; }}
  .scene-wrap {{ width:100%; height:100%; }}
  {style}
</style></head>
<body>
{''.join(scenes_html)}
<script>
  // Script chuyển scene theo đúng duration từng cảnh — Playwright ghi lại toàn bộ quá trình
  const scenes = document.querySelectorAll('.scene-wrap');
  scenes.forEach((s, i) => {{ s.style.display = i === 0 ? 'block' : 'none'; }});
  let i = 0;
  function nextScene() {{
    if (i >= scenes.length) return;
    scenes.forEach(s => s.style.display = 'none');
    scenes[i].style.display = 'block';
    const dur = parseFloat(scenes[i].dataset.duration) * 1000;
    i++;
    setTimeout(nextScene, dur);
  }}
  nextScene();
</script>
</body></html>"""

    Path(output_path).write_text(full_html, encoding="utf-8")
    print(f"Đã tạo {output_path} ({viewport}, {len(storyboard['scenes'])} scenes)")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Dùng: python build_render_html.py storyboard.json output.html [16x9|9x16]")
        sys.exit(1)
    build(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "16x9")

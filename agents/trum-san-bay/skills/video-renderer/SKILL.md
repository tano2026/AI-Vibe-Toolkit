# Video Renderer — HyperFrames

## Mô tả
Nhận caption + topic → gen HTML template → HyperFrames render ra MP4 9:16 sẵn sàng đăng TikTok/Reels/Shorts. Không cần GPU, chạy trên VPS Node.js 22+.

## Trigger
Dùng khi: Visual Agent cần tạo video từ content Trùm Sân Bay.

## Setup trên VPS

```bash
# Yêu cầu: Node.js 22+, ffmpeg
apt install ffmpeg -y

# Cài HyperFrames
npx skills add heygen-com/hyperframes
npm install -g hyperframes

# Thư mục làm việc
mkdir -p /opt/trum-san-bay/video-workspace
cd /opt/trum-san-bay/video-workspace
npx hyperframes init tsb-template
```

## HTML Template chuẩn (9:16, 60s)

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1080px; height: 1920px;
    background: linear-gradient(135deg, #0a1628 0%, #1a3a5c 100%);
    font-family: 'Be Vietnam Pro', sans-serif;
    overflow: hidden;
    color: white;
  }
  .hook {
    position: absolute; top: 200px; left: 60px; right: 60px;
    font-size: 72px; font-weight: 900; line-height: 1.2;
    color: #FFD700;
    animation: slideIn 0.5s ease-out;
  }
  .body-text {
    position: absolute; top: 600px; left: 60px; right: 60px;
    font-size: 48px; line-height: 1.6;
    animation: fadeIn 0.5s ease-out 1s both;
  }
  .bullet {
    display: flex; align-items: flex-start;
    margin-bottom: 40px;
    animation: slideUp 0.4s ease-out both;
  }
  .bullet-icon { font-size: 52px; margin-right: 24px; flex-shrink: 0; }
  .cta {
    position: absolute; bottom: 200px; left: 60px; right: 60px;
    font-size: 52px; font-weight: 700; text-align: center;
    background: #FFD700; color: #0a1628;
    padding: 40px; border-radius: 24px;
    animation: popIn 0.5s ease-out 3s both;
  }
  .logo {
    position: absolute; bottom: 80px; right: 60px;
    font-size: 36px; opacity: 0.7;
  }
  .progress-bar {
    position: absolute; bottom: 0; left: 0;
    height: 8px; background: #FFD700;
    animation: progress linear var(--duration, 60s);
  }
  @keyframes slideIn { from { transform: translateX(-100px); opacity: 0; } to { transform: none; opacity: 1; } }
  @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
  @keyframes slideUp { from { transform: translateY(40px); opacity: 0; } to { transform: none; opacity: 1; } }
  @keyframes popIn { from { transform: scale(0.8); opacity: 0; } to { transform: scale(1); opacity: 1; } }
  @keyframes progress { from { width: 0; } to { width: 100%; } }
</style>
</head>
<body>
  <div class="hook">{{HOOK}}</div>
  <div class="body-text">
    {{#each BULLETS}}
    <div class="bullet" style="animation-delay: {{delay}}s">
      <span class="bullet-icon">{{icon}}</span>
      <span>{{text}}</span>
    </div>
    {{/each}}
  </div>
  <div class="cta">{{CTA}}</div>
  <div class="logo">✈️ Trùm Sân Bay</div>
  <div class="progress-bar"></div>
</body>
</html>
```

## Python helper — gen HTML + render

```python
import subprocess
import json
import os

WORKSPACE = "/opt/trum-san-bay/video-workspace"

def render_video(content_id, hook, bullets, cta, duration=55):
    """
    bullets = [{"icon": "✅", "text": "...", "delay": 1.5}, ...]
    Trả về path đến file MP4
    """
    # Gen HTML
    bullets_html = ""
    for b in bullets:
        bullets_html += f'''
        <div class="bullet" style="animation-delay: {b["delay"]}s">
          <span class="bullet-icon">{b["icon"]}</span>
          <span>{b["text"]}</span>
        </div>'''

    with open(f"{WORKSPACE}/tsb-template/template.html") as f:
        template = f.read()

    html = template \
        .replace("{{HOOK}}", hook) \
        .replace("{{#each BULLETS}}{{/each}}", bullets_html) \
        .replace("{{CTA}}", cta) \
        .replace("var(--duration, 60s)", f"{duration}s")

    html_path = f"{WORKSPACE}/tsb-template/{content_id}.html"
    mp4_path = f"/opt/trum-san-bay/assets/{content_id}_9x16.mp4"

    with open(html_path, "w") as f:
        f.write(html)

    # HyperFrames render
    result = subprocess.run([
        "npx", "hyperframes", "render",
        "--input", html_path,
        "--output", mp4_path,
        "--width", "1080",
        "--height", "1920",
        "--duration", str(duration)
    ], capture_output=True, text=True, cwd=WORKSPACE)

    if result.returncode != 0:
        return {"error": result.stderr}

    return {"video_path": mp4_path, "content_id": content_id}


def parse_caption_to_video_data(caption_tiktok):
    """
    Dùng Claude để parse caption → hook + bullets + cta cho video
    """
    # Gọi Claude API để extract structured data từ caption
    import urllib.request
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": os.environ.get("ANTHROPIC_API_KEY"),
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 500,
        "messages": [{
            "role": "user",
            "content": f"""Từ caption TikTok này, extract ra JSON:
{{
  "hook": "câu hook ngắn gọn max 10 từ",
  "bullets": [
    {{"icon": "emoji", "text": "điểm chính 1, max 8 từ", "delay": 1.5}},
    {{"icon": "emoji", "text": "điểm chính 2, max 8 từ", "delay": 2.5}},
    {{"icon": "emoji", "text": "điểm chính 3, max 8 từ", "delay": 3.5}}
  ],
  "cta": "CTA ngắn max 8 từ"
}}

Caption: {caption_tiktok}

Chỉ trả JSON."""
        }]
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="POST")
    result = json.loads(urllib.request.urlopen(req).read())
    return json.loads(result["content"][0]["text"])
```

## Render time ước tính (VPS 2 CPU)
- Video 45s đơn giản: ~2-3 phút
- Video 60s có animation: ~4-5 phút
- Chạy background, không block pipeline

## Output
- `{content_id}_9x16.mp4` — TikTok/Reels/Shorts ready
- Tự động crop 1:1 bằng ffmpeg nếu cần cho Instagram Feed

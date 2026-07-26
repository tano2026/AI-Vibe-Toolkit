# MCP/Tool Setup — Shorts Affiliate System

## Bắt buộc

| Tool | Vai trò | Có sẵn trong kho? |
|---|---|---|
| GitHub API / web fetch | Fetch README/metadata tool cần review | Có (pattern chuẩn trong Project Instructions) |
| Playwright | Record render.html thành video 2 viewport | Cần cài: `npm install playwright && npx playwright install chromium` |
| FFmpeg + FFprobe | Merge video + voiceover, resize 9:16 | Cần cài trên VPS: `apt-get install -y ffmpeg` |
| Supertonic hoặc ElevenLabs | Text-to-speech cho voiceover | Xem `repos/omniroute.md` để route rẻ |
| `skills/affiliate-skills.md` | Research affiliate program + tracking + track performance | Có sẵn kho |

## Tùy chọn (khi bật publish thật)

| Tool | Nền tảng |
|---|---|
| `repos/tiktokautouploader.md` | TikTok |
| `mcps/meta-mcp-server.md` | Facebook/Instagram Reels |
| `mcps/buffer-mcp.md` | Schedule đa nền tảng |
| `mcps/mcp-youtube.md` | Upload + quản lý YouTube |

## Env cần set

```
GITHUB_TOKEN=...           # fetch repo info (đã có sẵn trong Project Instructions)
AFFILIATE_TRACKING_BASE=... # domain rút gọn link tracking, nếu dùng riêng
TTS_PROVIDER=supertonic     # hoặc elevenlabs
```

## Kiểm tra trước khi chạy thật

```bash
node -e "require('playwright')" && echo "Playwright OK"
ffmpeg -version | head -1
ffprobe -version | head -1
```

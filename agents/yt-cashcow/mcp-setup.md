# MCP/Tool Setup — YT Cashcow

## Danh sách cần bật

| Tool | Loại | Đã có trong kho? | Cần làm gì |
|---|---|---|---|
| MoneyPrinterTurbo | Repo, self-host | ✅ `repos/moneyprinterturbo.md` | Deploy Docker trên VPS, xem `deploy-checklist.md` |
| MediaCrawler | Repo, self-host | ✅ `repos/mediacrawler.md` | Deploy theo hướng dẫn trong file, chú ý rate limit |
| mcp-youtube | MCP | ✅ `mcps/mcp-youtube.md` | Không cần API key, gắn JSON config 5 dòng |
| OmniRoute | Repo, self-host | ✅ `repos/omniroute.md` | Đã chạy sẵn trên VPS theo memory hiện tại — chỉ cần trỏ MoneyPrinterTurbo llm_provider vào endpoint OmniRoute |
| viral-hooks skill | Skill | ✅ `skills/viral-hooks/` | Copy vào OpenClaw skill dir |
| youtube-marketing-skills | Skill | ✅ `skills/youtube-marketing/SKILL.md` | Copy vào OpenClaw skill dir |
| claude-ads (ads-youtube) | Skill | ✅ `skills/claude-ads/ads-youtube.md` | Copy vào OpenClaw skill dir |
| Airtable | External | ❌ Chưa setup | Tạo base mới `yt-cashcow-log`, xem schema trong `ARCHITECTURE.md` |
| Upload-Post | External service (qua MoneyPrinterTurbo) | ❌ Chưa setup | Đăng ký tài khoản, lấy API key, điền vào `config.toml` của MoneyPrinterTurbo |

## Config MoneyPrinterTurbo (config.toml) — trỏ LLM qua OmniRoute

```toml
[llm]
provider = "openai_compatible"  # OmniRoute expose OpenAI-compatible endpoint
base_url = "http://<omniroute-vps-ip>:<port>/v1"
api_key = "[OMNIROUTE_KEY]"
model = "claude-sonnet-5"  # hoặc route qua creative tier

[tts]
provider = "edge"  # free, Microsoft Edge TTS — đủ dùng, không cần GPU

[video]
fps = 30
resolution = "1080x1920"  # Shorts/vertical, hoặc 1920x1080 cho long-form
language = "en"

[publish]
upload_post_api_key = "[UPLOAD_POST_KEY]"
platforms = ["youtube"]
```

## Airtable setup

1. Tạo base mới tên `yt-cashcow-log`.
2. Tạo 2 bảng theo schema trong `ARCHITECTURE.md` (`videos`, `fingerprint_history`).
3. Lấy API key + base ID, điền vào Hermes env (không hardcode trong file .md/skill).

## Token security
Mọi API key trong file này khi push lên kho GitHub phải là placeholder
(`[OMNIROUTE_KEY]`, `[UPLOAD_POST_KEY]`) — đúng nguyên tắc token security của kho.

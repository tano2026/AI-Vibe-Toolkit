# FreeLLMAPI — GitHub Repo

## TL;DR
OpenAI-compatible proxy gom 16+ LLM provider miễn phí thành 1 endpoint duy nhất — ~1.7B token/tháng, auto failover 20 lần, mã hóa AES-256. Cài Docker 1 lệnh. 14.1K stars. Đây là "OmniRoute phiên bản tập trung vào free tier" — cùng concept nhưng nhẹ hơn, dễ self-host hơn.

## Repo này dùng để làm gì
Vấn đề: Muốn dùng nhiều LLM miễn phí (Groq, Cerebras, Mistral, Gemini...) nhưng mỗi cái có SDK riêng, API key riêng, rate limit riêng. Hết quota cái này phải tay switch sang cái kia.

FreeLLMAPI giải quyết bằng cách đặt 1 proxy ở giữa:
- **1 endpoint OpenAI-compatible:** `http://localhost:3001/v1` — tất cả tool point vào đây
- **16+ provider miễn phí phía sau:** Google, Groq, Cerebras, Mistral, OpenRouter, GitHub Models...
- **~1.7B token miễn phí/tháng** từ tổng hợp free tier các provider
- **Auto failover:** Khi hit rate limit → tự switch provider khác, retry tối đa 20 lần
- **Smart routing:** Detect vision model, tool calling, embeddings → route đúng provider
- **Sticky sessions:** Multi-turn chat giữ cùng provider để tránh context loss
- **AES-256-GCM encryption:** API key lưu mã hóa, decrypt in-memory lúc gọi
- **Per-key rate tracking:** Theo dõi RPM, RPD, TPM, TPD — không để vượt quota
- **Desktop app:** Native menubar app cho macOS và Windows
- **Dashboard web:** Analytics: latency, token count, breakdown theo provider

## So sánh với OmniRoute

| | FreeLLMAPI | OmniRoute |
|---|---|---|
| Stars | 14.1K | 7.1K |
| Provider | 16+ (tập trung free) | 231 (cả paid) |
| Compression | Không | RTK+Caveman (15-95%) |
| Retry | 20 lần | 4-tier fallback |
| Token/tháng | ~1.7B | ~1.6B |
| Desktop App | Có (native) | Không |
| Dashboard | Có | Có |
| Antigravity | Không | Chính thức |
| License | MIT | MIT |

**Kết luận:** Nếu chỉ cần free tier → FreeLLMAPI đơn giản hơn, ít cấu hình hơn. Nếu cần full stack (compression, 231 provider, Antigravity) → OmniRoute.

## Setup từng bước

**Cách 1: Docker (nhanh nhất)**
```bash
curl -fsSL https://freellmapi.co/install.sh | bash
# Chạy trên http://localhost:3001
# Dashboard: http://localhost:3001/dashboard
```

**Cách 2: Docker Compose thủ công**
```bash
git clone https://github.com/tashfeenahmed/freellmapi
cd freellmapi
# Tạo encryption key
openssl rand -base64 32
# Paste vào .env → ENCRYPTION_KEY=...
docker compose up -d
```

**Cách 3: Local dev (Node.js 20+)**
```bash
git clone https://github.com/tashfeenahmed/freellmapi
cd freellmapi
npm install
npm run dev
```

**Config tool của mày sau khi chạy:**
```json
// Claude Code → .claude/settings.json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:3001/v1",
    "ANTHROPIC_API_KEY": "any-string-here"
  }
}
```

```python
# Hermes / Python agent
BASE_URL = "http://localhost:3001/v1"
# Thay anthropic.com bằng localhost:3001 — code khác giữ nguyên
```

```
# Cursor: Settings → AI → Base URL → http://localhost:3001/v1
# Windsurf: tương tự Cursor
# OpenRouter users: đổi endpoint sang đây để cache free tier
```

## Provider miễn phí được gom

| Provider | Highlights |
|----------|------------|
| Google AI Studio | Gemini 2.0 Flash, 1M context |
| Groq | Nhanh nhất hiện tại: Llama 3.3 70B, 117M token/tháng |
| Cerebras | WSC chip nhanh: 30M token/tháng |
| Mistral | La Plateforme: 1B token/tháng (research plan) |
| OpenRouter (free) | Nhiều model free nhưng giới hạn RPM |
| GitHub Models | Gpt-4o-mini, Phi-4, Llama free qua GitHub token |
| Cloudflare AI | 30M token/tháng |
| SambaNova | 30M token/tháng |
| + 8 provider khác | Xem dashboard để thêm |

## Wire format hỗ trợ

```
POST /v1/chat/completions       ← OpenAI format (default)
POST /v1/messages               ← Anthropic Messages API format
POST /v1/completions            ← Legacy OpenAI completion
POST /v1/embeddings             ← Embedding requests
```

Mày có thể đổi endpoint mà không cần đổi code — FreeLLMAPI tự map format.

## Ứng dụng trực tiếp cho hệ sinh thái agent

```
Hermes → FreeLLMAPI:3001 → [Groq / Gemini / Cerebras / Mistral...]
OpenClaw → FreeLLMAPI:3001 → auto fallback 20 lần trước khi báo lỗi
Claude Code → FreeLLMAPI:3001 → không bao giờ thấy "rate limit exceeded"
```

Khi kết hợp với OmniRoute:
```
Hermes → OmniRoute:20128 (compression + 231 provider)
         ↳ FreeLLMAPI:3001 (free tier aggregator, làm provider thứ 232)
```

## Lưu ý

- Port mặc định **3001**, không phải 8080 hay 3000
- Cần thêm API key từng provider vào dashboard (Settings → Providers) sau khi cài
- GitHub Models cần Personal Access Token (free, không cần payment)
- OpenRouter free tier có RPM thấp — nên để priority thấp trong fallback chain
- Desktop app ($19/năm hoặc $49 trọn đời) mới có live model catalog updates

## Đánh giá

- Điểm mạnh: Setup cực đơn giản (1 curl), OpenAI-compatible 100%, desktop app native, 14.1K stars, active community
- Điểm yếu: Ít provider hơn OmniRoute (16 vs 231), không có token compression, không có Antigravity integration
- Có nên dùng không: **8.5/10** — Tool lý tưởng cho người mới muốn gom free tier nhanh. Nếu đã có OmniRoute thì FreeLLMAPI bổ sung thêm 1.7B token/tháng như 1 provider trong chain.

## Link
- Repo: https://github.com/tashfeenahmed/freellmapi
- Website: https://freellmapi.co
- Docker: tashfeenahmed/freellmapi
- Node requirement: >=20.0.0
- License: MIT

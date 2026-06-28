# OmniRoute — GitHub Repo

## TL;DR
Free AI gateway mo nguon mo — gom 231 provider (50+ free tier) thanh 1 endpoint local OpenAI-compatible. ~1.6B token mien phi moi thang, RTK+Caveman compression tiet kiem them 15-95% token. Cai 2 phut, khong can credit card. Tich hop Antigravity chinh thuc. 7.1K stars, dang tang nhanh.

## Repo nay dung de lam gi
Van de: Muon dung nhieu LLM free (Mistral, Groq, Gemini, Cloudflare...) phai quan ly nhieu SDK, nhieu API key, nhieu rate limit khac nhau. Khi het han 1 provider phai manual switch.

OmniRoute giai quyet bang cach lam mot OpenAI-compatible proxy chay local:
- **1 endpoint duy nhat:** `http://localhost:20128/v1` — tat ca tool point vao day
- **231 providers phia sau:** tu dong fallback khi het rate limit
- **~1.6B token mien phi/thang** (pool-deduped, honest counting):
  - Mistral: 1B token/thang (research free plan)
  - LLM7: 150M token/thang
  - LongCat-2.0: 150M token/thang
  - Groq: 117M token/thang (inference nhanh nhat)
  - Gemini: 60M token/thang
  - Cerebras: 30M token/thang
  - Cloudflare: 30M token/thang
  - SambaNova: 30M token/thang
  - No-cap (khong gioi han): SiliconFlow, Z.AI GLM-Flash, Kilo, OpenCode Zen
- **RTK+Caveman compression:** 9 engine nep token truoc khi gui — tiet kiem 15-95%
- **14 routing strategy:** priority, weighted, cost-optimized, auto (9-factor scoring), reset-aware...
- **4-tier fallback:** Subscription → API Key → Cheap → Free
- **Tich hop Antigravity chinh thuc** — `omniroute login antigravity` helper rieng

## Setup tung buoc

**Cach 1: npx (nhanh nhat, khong can cai gi)**
```bash
npx omniroute
# → Chay tren http://localhost:20128
# → Mo dashboard: http://localhost:20128/dashboard
```

**Cach 2: npm global (khuyen nghi cho production)**
```bash
npm install -g omniroute
omniroute
```

**Cach 3: Docker (cho VPS)**
```bash
docker run -d   -p 20128:20128   -v omniroute-data:/app/data   --name omniroute   --restart always   diegosouzapw/omniroute:latest
```

**Sau khi chay — config tool cua may:**
```bash
# Claude Code
# .claude/settings.json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:20128/v1",
    "ANTHROPIC_API_KEY": "omniroute"
  }
}

# Hermes (Python)
import urllib.request
BASE_URL = "http://localhost:20128/v1"  # thay vi api.anthropic.com

# Cursor
# Settings → AI → Base URL: http://localhost:20128/v1

# OpenClaw / Antigravity
omniroute login antigravity  # helper rieng, tu dong OAuth
```

**Them free provider vao Dashboard:**
```
1. Mo http://localhost:20128/dashboard
2. Connections → Add Connection
3. Chon provider (Groq, Gemini, Mistral...) → Sign in / paste API key
4. Done — tu dong vao rotation
```

## Free token breakdown chi tiet

| Provider | Token/thang | Ghi chu |
|----------|-------------|---------|
| Mistral | 1,000M | Research free plan, can dang ky |
| LLM7 | 150M | |
| LongCat-2.0 | 150M | |
| Groq | 117M | Nhanh nhat hien tai |
| Gemini (Google) | 60M | AI Studio free |
| Cerebras | 30M | |
| Cloudflare | 30M | 10K Neurons/day |
| SambaNova | 30M | |
| SiliconFlow | No-cap | Khong gioi han |
| Z.AI GLM-Flash | No-cap | Khong gioi han |
| Kilo | No-cap | ~50 credits/thang/account |
| OpenCode Zen | No-cap | |
| **Tong** | **~1.6B** | **Thang dau len 2.1B voi signup credits** |

## RTK+Caveman Compression — tiet kiem token that su

9 compression engine chay trong pipeline:
- **RTK (Repetitive Token Kompressor):** Nen chuoi lap lai — 20-40% giam
- **Caveman:** Nen prose verbose → ngon ngu ngan — tiet kiem lon
- **LLMLingua-2 ONNX:** AI-powered compression
- **Output Styles:** terse-prose / less-code / terse-CJK
- **Context Budget:** Tu dong cut context khi qua dai

Ket qua thuc te:
- Tool-heavy session: giam 89% token
- Code review session: giam 40-60%
- Chat thong thuong: giam 15-30%

Code/URL/JSON luon duoc bao ve nguyen ven, khong bi nen.

## Vi du thuc te

**Hermes goi qua OmniRoute — khong can thay doi code:**
```python
import urllib.request, json

# Chi doi BASE_URL — code khac giu nguyen
BASE_URL = "http://localhost:20128/v1"  # OmniRoute local

def call_llm(prompt, model="auto/coding:fast"):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000
    }
    req = urllib.request.Request(
        f"{BASE_URL}/chat/completions",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": "Bearer omniroute",
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"]

# auto/coding:fast → OmniRoute tu chon model coding tot nhat dang free
# auto/reasoning:pro → chon model reasoning tot nhat
# Khi het rate limit → tu dong fallback sang provider khac
```

**Auto-combo routing thong minh:**
```
auto/coding:fast    → Kimi K2.6, DeepSeek Coder (NVIDIA NIM)
auto/reasoning:pro  → DeepSeek R1, Groq Llama
auto/chat:fast      → Gemini Flash, Groq Llama 3.3
auto/long-context   → Minimax M3 (1M context), Gemini Flash (1M)
```

## Luu y / Loi thuong gap
- **Port mac dinh 20128** khong phai 3000 — thong tin cu tren mang hay sai
- Mot so provider cam dung proxy (Kiro, iFlytek, Meta) — OmniRoute co flag canh bao
- **ToS warning:** Mot so provider explicitly cam dung voi "OpenClaw and similar tools" — doc flag truoc khi add provider nao
- Token compression co the thay doi nghia neu prompt qua ngan — nen dung voi prompt > 200 token
- Free tier co the thay doi — OmniRoute update bang tracking hang tuan

## So sanh voi 9router va freeLLM

| | OmniRoute | 9router | freeLLM |
|---|---|---|---|
| Endpoint | 1 local | 1 local | Directory (khong co endpoint) |
| Providers | 231 | 60+ | 224 (chi list) |
| Compression | RTK+Caveman (15-95%) | RTK (20-40%) | Khong |
| Fallback | 4-tier tu dong | 3-tier | Manual |
| MCP Server | 87 tools | 10+ | Khong |
| Antigravity | Chinh thuc | Khong | Khong |
| Dashboard | Co (dep) | CLI only | Web (chi compare) |
| Stars | 7.1K | 115K | 121 |

**Ket luan:** OmniRoute > 9router ve tinh nang; 9router nhieu star hon vi ra truoc. freeLLM chi de research model.

## Danh gia ca nhan
- Diem manh: Thiet ke tot nhat trong class; Antigravity integration chinh thuc; compression that su; honest token counting; MCP server built-in; dashboard dep; Docker ready
- Diem yeu: 7.1K stars con it, ecosystem moi; mot so provider ToS phuc tap; port 20128 hay nham voi port 3000 trong huong dan cu; Node >=22 required
- Co nen dung khong: **9.5/10** — Deploy len VPS ngay. Day la middleware quan trong nhat trong agent stack cua may: Hermes/OpenClaw goi OmniRoute → OmniRoute phan phoi sang 231 provider → auto fallback → compression → tiet kiem tien va khong bao gio bi rate limit.

## Ung dung truc tiep cho he sinh thai agent

```
Hermes → OmniRoute:20128 → [Groq / Gemini / Mistral / Cerebras...]
OpenClaw → OmniRoute:20128 → [auto-routing theo task type]
Antigravity → omniroute login antigravity → OAuth tu dong
```

Mot lan config OmniRoute → tat ca agent dung chung 1.6B token mien phi.

## Link
- Repo: https://github.com/diegosouzapw/OmniRoute
- Website: https://omniroute.online
- npm: https://www.npmjs.com/package/omniroute
- Docker: diegosouzapw/omniroute
- Discord/Telegram: link trong README
- Node requirement: >=22.0.0
- License: MIT

# freeLLM — Tool / Website

## TL;DR
Thu muc tong hop 224+ LLM API mien phi tu 25 nha cung cap (Google, Groq, NVIDIA NIM, Cloudflare, Mistral, SambaNova...) — so sanh rate limit, context window, one-click config cho Claude Code, Cursor, Hermes va moi OpenAI-compatible tool. Khong can credit card. freellm.net

## Tool nay dung de lam gi
Khi build AI agent hay vibe code, van de thuong gap la: model tot thi ton tien, model mien phi thi kho tim, kho so sanh. freeLLM giai quyet bang cach aggregate het vao mot cho:

- **224 models** duoc track tu 25 providers
- **127 models** dang free va online tai thoi diem kiem tra
- **So sanh truc tiep:** Score, context window, max output, rate limit, ngay release, usage activity, trang thai
- **One-click config:** Chon model → copy config JSON → paste vao Claude Code/Cursor/Hermes
- **Vault:** Luu API keys ma hoa, khong can hunt qua text files
- **Refresh hang ngay:** Data luon cap nhat, biet model nao dang online/offline

**Top models hom nay (theo score):**
| Model | Provider | Score | Context | Rate Limit |
|-------|----------|-------|---------|-----------|
| minimaxai/minimax-m3 | NVIDIA NIM | 95 | 1.0M | 40 RPM |
| moonshotai/kimi-k2.6 | NVIDIA NIM | 91 | 262K | 40 RPM |
| Gemini 3.5 Flash | Google Gemini | 89 | 1.0M | 15 RPM / 1500 RPD |

## Setup tung buoc

**Dung ngay (khong can cai gi):**
```
1. Vao freellm.net
2. Search model theo task: Coding / Chat / Vision / Audio / Reasoning / Embedding
3. Click provider muon dung → trang lau API key
4. Lay API key mien phi (khong can credit card)
5. Copy config → paste vao tool
```

**Tich hop vao Hermes (Python):**
```python
import urllib.request, json

# Vi du dung Gemini 3.5 Flash mien phi qua OpenAI-compatible endpoint
API_KEY = "YOUR_GOOGLE_FREE_API_KEY"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai"

def call_free_llm(prompt, model="gemini-2.5-flash"):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000
    }
    req = urllib.request.Request(
        f"{BASE_URL}/chat/completions",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"]
```

**Tich hop vao Claude Code / Cursor:**
```json
// .claude/settings.json hoac .cursor/mcp.json
{
  "llm": {
    "provider": "openai-compatible",
    "baseUrl": "https://api.groq.com/openai/v1",
    "apiKey": "YOUR_GROQ_FREE_KEY",
    "model": "llama-3.3-70b-versatile"
  }
}
```

**Providers hay dung nhat (free tier tot):**
| Provider | Model hay | Free limit | Lay key o dau |
|----------|-----------|------------|---------------|
| Google Gemini | Gemini 2.5 Flash | 15 RPM, 1500 RPD | aistudio.google.com |
| Groq | Llama 3.3 70B | 30 RPM, 14400 RPD | console.groq.com |
| NVIDIA NIM | Minimax M3, Kimi K2 | 40 RPM | build.nvidia.com |
| Cloudflare | Llama, Mistral | 10000 req/ngay | dash.cloudflare.com |
| SambaNova | Llama 3.1 405B | Generous free | cloud.sambanova.ai |

## Vi du thuc te
**Hermes research agent switch model theo task:**
```python
FREE_MODELS = {
    "reasoning": "groq/deepseek-r1-distill-llama-70b",
    "coding": "nvidia/kimi-k2.6",
    "fast_chat": "google/gemini-2.5-flash",
    "long_context": "nvidia/minimax-m3",  # 1M context
    "embedding": "cloudflare/bge-large-en-v1.5"
}

def get_model_for_task(task):
    return FREE_MODELS.get(task, FREE_MODELS["fast_chat"])

# Hermes tu chon model phu hop voi tung task
# Khong ton tien, khong can swap tay
```

## Luu y / Loi thuong gap
- Rate limit la van de chinh: 15-40 RPM du cho dev, khong du cho production traffic cao
- Model "Online" tren site co the offline dot ngot — nen co fallback
- NVIDIA NIM free tier doi khi can waitlist — check truoc khi plan
- Khong phai moi model ho tro function calling / tool use — kiem tra truoc khi dung cho agent
- freeLLM chi track, khong cung cap API — van phai lay key truc tiep tu provider

## Danh gia ca nhan
- Diem manh: Tong hop tot nhat hien tai cho free LLM; so sanh truc quan; config one-click; refresh hang ngay; Vault tien loi
- Diem yeu: 121 GitHub star = con rat moi, co the thay doi; khong co API rieng cua ho; rate limit free tier thap cho production
- Co nen dung khong: **9/10** — Bookmark bat buoc cho moi vibe coder va AI agent builder. Thay vi tra $20-100/thang cho LLM API khi dang dev/prototype, dung het free tier o day truoc.

## Ung dung cho he sinh thai agent cua tao
- **Hermes:** Switch giua Gemini Flash (fast, free), Groq Llama (reasoning), NVIDIA Kimi (coding) theo task
- **OpenClaw:** Dung Cloudflare free cho cac task nhe, giu DeepSeek cho task chinh
- **Content factory:** Gemini 2.5 Flash 1M context = doc ca file lon, free, nhanh

## Link
- Website: https://freellm.net
- GitHub: 121 stars (con moi)
- Loai: Directory / Comparison tool
- Update: Hang ngay

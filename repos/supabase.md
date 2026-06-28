# Supabase — GitHub Repo

## TL;DR
Firebase alternative mã nguồn mở — Postgres database + Auth + Storage + Realtime + Edge Functions trong một platform. 104K stars. Vibe coder dùng Supabase thay vì tự setup backend từ đầu.

## Repo này dùng để làm gì
Thay vì setup Node.js server + PostgreSQL + JWT auth + file storage riêng lẻ — Supabase gộp tất cả:
- **Database:** PostgreSQL thật (không phải NoSQL giả), có thể query SQL trực tiếp
- **Auth:** Email/password, OAuth (Google, GitHub, Apple...), magic link
- **Storage:** Upload file, image, video — có CDN
- **Realtime:** Subscribe data changes — build live chat, collaborative app
- **Edge Functions:** Serverless Deno functions gần giống Cloudflare Workers
- **Vector:** pgvector built-in → RAG app không cần Pinecone riêng

Vibe coder hay dùng: "Cursor viết code, Supabase làm backend" → ship app full-stack trong 1 ngày.

## Setup từng bước
```bash
# Option 1: Supabase Cloud (free tier, nhanh nhất)
# Vào supabase.com → tạo project → lấy URL + anon key

# Option 2: Self-host
npx supabase init
npx supabase start  # chạy local với Docker

# Cài SDK trong project
npm install @supabase/supabase-js

# Kết nối
import { createClient } from '@supabase/supabase-js'
const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY)

# Query database
const { data } = await supabase.from('posts').select('*')

# Auth
await supabase.auth.signInWithPassword({ email, password })

# Upload file
await supabase.storage.from('avatars').upload('user.jpg', file)
```

## Ví dụ thực tế
**Build AI Travel Planner (ABTRIP use case):**
```javascript
// Lưu itinerary user tạo
await supabase.from('itineraries').insert({
  user_id: user.id,
  destination: 'Ha Giang',
  days: 7,
  content: generatedPlan
})

// Realtime sync khi guide update
supabase.channel('itinerary-updates')
  .on('postgres_changes', { table: 'itineraries' }, handleUpdate)
  .subscribe()
```

Auth + database + realtime — 3 dòng config, không cần backend server riêng.

## Lưu ý / Lỗi thường gặp
- Free tier: 500MB database, 1GB storage, 50K monthly active users — đủ cho MVP
- RLS (Row Level Security) phải setup đúng — bỏ qua là security hole lớn
- Supabase pause project free tier sau 1 tuần inactive — dùng free plan cần ping định kỳ
- Self-host phức tạp hơn Firebase self-host — dùng cloud nếu không cần full control

## Đánh giá cá nhân
- Điểm mạnh: PostgreSQL thật (không lock-in NoSQL); dashboard đẹp; SDK tốt cho mọi framework; vector search built-in; community cực lớn
- Điểm yếu: Free tier bị pause; self-host phức tạp; edge functions còn hạn chế so với Cloudflare
- Có nên dùng không: **9/10** — Backend mặc định cho mọi vibe coder. Nếu mày build app với Cursor/Claude Code, dùng Supabase là lựa chọn số 1.

## Link
- Repo: https://github.com/supabase/supabase
- Docs: https://supabase.com/docs
- Dashboard: https://supabase.com

---

## 🤖 Agent Integration

> Section này dành cho Hermes/OpenClaw/Antigravity.

### Hermes (Python)
```python
import urllib.request, json

SUPABASE_URL = "[SUPABASE_URL]"  # https://xxx.supabase.co
SUPABASE_KEY = "[SUPABASE_ANON_KEY]"
HEADERS_SB = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}",
              "Content-Type": "application/json"}

def sb_select(table, filters="", limit=100):
    f = f"?{filters}&limit={limit}" if filters else f"?limit={limit}"
    req = urllib.request.Request(f"{SUPABASE_URL}/rest/v1/{table}{f}", headers=HEADERS_SB)
    return json.loads(urllib.request.urlopen(req).read())

def sb_insert(table, data):
    payload = json.dumps(data).encode()
    req = urllib.request.Request(f"{SUPABASE_URL}/rest/v1/{table}", data=payload,
        headers={**HEADERS_SB, "Prefer": "return=representation"}, method="POST")
    return json.loads(urllib.request.urlopen(req).read())

def sb_update(table, data, filter_col, filter_val):
    payload = json.dumps(data).encode()
    req = urllib.request.Request(
        f"{SUPABASE_URL}/rest/v1/{table}?{filter_col}=eq.{filter_val}",
        data=payload, headers=HEADERS_SB, method="PATCH")
    return json.loads(urllib.request.urlopen(req).read())

def sb_delete(table, filter_col, filter_val):
    req = urllib.request.Request(
        f"{SUPABASE_URL}/rest/v1/{table}?{filter_col}=eq.{filter_val}",
        headers=HEADERS_SB, method="DELETE")
    urllib.request.urlopen(req)

# Dùng: rows = sb_select("tools", "status=eq.active")
```

### OpenClaw
```bash
# Dùng Supabase JS SDK:
npm install @supabase/supabase-js
```

### Antigravity
```bash
# Self-host Supabase:
git clone https://github.com/supabase/supabase
cd supabase/docker && cp .env.example .env
docker compose up -d
# Mở: http://localhost:8000
```
> ⚠️ Dùng cloud miễn phí cho projects nhỏ. Self-host khi cần privacy.

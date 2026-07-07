# ANTIGRAVITY-PLAYBOOK
> Đọc file này trước khi thực thi bất kỳ deployment nào.

---

## Mày là Antigravity

Mày là layer infrastructure. Hermes/OpenClaw không tự deploy — chúng nhờ mày.
- **Runtime:** Shell/bash trên VPS CentOS/RHEL
- **Quyền:** sudo, docker, pm2, pip, npm
- **VPS:** 2-4 CPU / 4-8GB RAM, Hermes + OpenClaw chạy liên tục

---

## Fetch kho (bash)

```bash
GITHUB_TOKEN="[GITHUB_TOKEN]"
fetch_kho() {
  curl -sf     -H "Authorization: token $GITHUB_TOKEN"     -H "Accept: application/vnd.github.v3+json"     "https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/$1"     | python3 -c "import sys,json,base64; d=json.load(sys.stdin); print(base64.b64decode(d['content']).decode())"
}

# Ví dụ:
# fetch_kho "repos/mem0.md"       → đọc doc rồi deploy
# fetch_kho "KHO-INDEX.md"        → xem toàn bộ kho
# fetch_kho "TRACKER.md"          → xem danh sách entries
```

---

## Khi nào mày được gọi

Hermes/OpenClaw báo 1 trong các tình huống sau:
1. "Cần `pip install X` để chạy task Y"
2. "Cần deploy service X lên VPS"
3. "Service X bị crash, cần restart"
4. "Cần setup môi trường mới"

---

## Deploy pattern theo loại

### Python service
```bash
fetch_kho "repos/[tên].md" | head -60   # đọc TL;DR + setup
git clone https://github.com/[repo]
cd [repo] && python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env && nano .env        # điền keys
python3 main.py --test                   # verify
pm2 start "python3 main.py" --name [name] --cwd $(pwd)
pm2 save
```

### Docker service
```bash
fetch_kho "repos/[tên].md" | grep -A 20 "docker"
git clone https://github.com/[repo]
cd [repo] && cp .env.example .env && nano .env
docker compose up -d
docker compose ps && curl localhost:[port]/health
echo "Service [name] running on port [port]"
# → Báo Hermes: endpoint http://localhost:[port]
```

### Node.js / MCP server
```bash
git clone https://github.com/[repo]
cd [repo] && npm install
cp .env.example .env && nano .env
node index.js &   # test
pm2 start index.js --name [name] && pm2 save
```

---

## Packages cài sẵn cho Hermes — chạy 1 lần

```bash
pip install   markitdown   magika   tavily-python   mem0ai   posthog   sentry-sdk   requests   httpx   python-dotenv   playwright
playwright install chromium
```

---

## Services ưu tiên deploy (từ kho)

Đọc file tương ứng trong `/repos/` để lấy lệnh deploy chính xác:

| Service | File kho | Port | Hermes gọi vào |
|---------|----------|------|----------------|
| Mem0 | `repos/mem0.md` | 8000 | `/v1/memories/` |
| Supabase | `repos/supabase.md` | 5432/8000 | REST + Postgres |
| n8n-claw | `repos/n8n-claw.md` | 5678 | webhook/api |
| Open WebUI | `repos/open-webui.md` | 3000 | `/api/chat/completions` |
| Dify | `repos/dify.md` | 80 | `/v1/chat-messages` |
| Stirling PDF | `repos/stirling-pdf.md` | 8080 | `/api/v1/` |
| Coolify | `repos/coolify.md` | 8000 | `/api/v1/` |
| Crawl4AI | `repos/crawl4ai.md` | 11235 | `/crawl` |
| TurboVec | `repos/turbovec.md` | 6333 | Qdrant REST |

---

## Maintenance

```bash
pm2 status && df -h && free -h          # daily check
pm2 logs hermes --lines 50              # xem log Hermes
pm2 restart hermes                      # restart nếu cần
docker system prune -f                  # dọn disk hàng tháng
```

---

## Báo lại sau khi deploy

Luôn báo Hermes/chủ đủ 3 thứ:
1. **Endpoint:** `http://localhost:[port]/api/...`
2. **Auth:** API key ở đâu / cách lấy
3. **Health check:** `curl localhost:[port]/health` → kết quả gì


---

## 🎫 TICKET — Hermes thiếu tool HTTP fetch generic (03/07/2026)

**Vấn đề phát hiện:** `HERMES-PLAYBOOK.md` giả định Hermes có thể tự chạy
`urllib.request` tùy ý (Python runtime tự do). Thực tế: Hermes chỉ có bộ tool cố định
đăng ký sẵn trong `default_api` — KHÔNG có quyền chạy code Python tùy ý hoặc gọi HTTP
request generic. Hermes tự báo lỗi: "không có `fetch_file_from_repository` trong
default_api".

**Hệ quả:** Mọi code mẫu trong kho (GitHub API fetch, Tavily/Brave search, Firecrawl,
gửi email Resend...) mà Hermes "đọc" được nhưng KHÔNG "chạy" được — vì thiếu tool nền.

**Cần làm (mày quyết cách implement, đây chỉ là yêu cầu chức năng):**

Đăng ký 1 tool mới cho Hermes trong OpenClaw config, tối thiểu 2 việc:
1. Nhận `url` (string) + optional `method`/`headers`/`body`
2. Trả về response body (text) — để Hermes tự parse JSON/base64 tiếp theo logic
   trong HERMES-PLAYBOOK.md

Gợi ý implementation (Node.js, vì OpenClaw runtime là Node 22+):
```javascript
// vi du dang ky tool trong OpenClaw cho Hermes goi
async function httpFetch({ url, method = "GET", headers = {}, body = null }) {
  const res = await fetch(url, { method, headers, body });
  const text = await res.text();
  return { status: res.status, body: text };
}
// dang ky tool nay vao default_api cua Hermes voi ten "http_fetch" hoac "fetch_url"
```

**Verify sau khi thêm:** báo Nobitano nhắn Hermes qua Telegram — "fetch thử
`https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/TRACKER.md`" — nếu
trả về JSON thật (không còn báo lỗi thiếu tool) → xong.

**Status:** Chờ Antigravity xử lý. Claude không có quyền VPS để tự làm việc này.


---

## 🎫 TICKET UPDATE (05/07/2026) — Chi tiết kỹ thuật fetch_url + cảnh báo

**Khuyến nghị đã xác nhận:** KHÔNG route qua OpenClaw cho việc fetch URL đơn giản —
phức tạp hóa không cần thiết (2 process Node.js + Python gọi chéo cho 1 GET request).
Thêm trực tiếp 1 hàm `fetch_url(url, max_length)` vào registry `default_api` của
chính Hermes (cùng cơ chế đang dùng để đăng ký `search_flights`/`book_flight`).

```python
def fetch_url(url: str, max_length: int = 5000) -> str:
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "Hermes/1.0"})
    content = urllib.request.urlopen(req, timeout=10).read().decode("utf-8", errors="ignore")
    return content[:max_length]
```

Antigravity cần tự xác định framework Hermes dùng để định nghĩa `default_api`
(OpenAI tool-calling / LangChain / tự viết) — Claude không có quyền xem code gốc
Hermes nên không biết chính xác cơ chế, không đoán bừa.

**Alternative nếu muốn dùng MCP chuẩn:** `npx -y @modelcontextprotocol/server-fetch`
(official Anthropic) — nhưng vẫn cần wire vào default_api schema của Hermes, không
tự động expose chỉ vì cài package.

---

## ⚠️ CẢNH BÁO: Hermes tự bịa thông tin khi được hỏi về kho (05/07/2026)

Phát hiện qua Telegram: khi hỏi Hermes "kho có skill gì", nó tự liệt kê 12 skill —
**6/12 KHÔNG TỒN TẠI** trong kho GitHub thật (ecc-brand-voice, competitor-spy,
market-trends, antigravity-deploy, cron-manager, finance-forex, legal-doc-check —
đều là bịa, nghe hợp lý nhưng không có thật). Hermes cũng tự claim "OpenClaw có 163
skills" — chưa verify, cùng pattern nghi vấn.

**Nguyên nhân:** Hermes không có tool fetch thật (đúng ticket ở trên) nên không thể
tự kiểm tra kho — khi được hỏi, nó generate câu trả lời NGHE hợp lý dựa trên pattern
(không phải data thật).

**Hành động cần:** Sau khi fix `fetch_url`, TEST LẠI bằng câu hỏi có đáp án biết
trước (vd "liệt kê chính xác tên các file trong /skills/") để xác nhận nó đang đọc
thật, không phải tiếp tục bịa. Trước khi fix xong, KHÔNG tin bất kỳ câu trả lời nào
của Hermes về nội dung kho — luôn hỏi Claude (có GitHub API thật) để verify.


---

## 🎫 TICKET (07/07/2026) — State storage layer cho tầng "Trí nhớ" (Airtable)

**Bối cảnh:** Skill mới `skills/agent-self-improvement-loops/SKILL.md` chấm điểm Hermes
1/5 ở tầng Trí nhớ — mỗi lần chạy là tabula rasa, không nhớ lỗi/lesson từ lần trước.
Đây là gap lớn nhất trong 5 tầng, ưu tiên fix TRƯỚC các gap khác (Kế hoạch, Khám phá)
vì các tầng đó phụ thuộc vào có trí nhớ trước đã.

**Quyết định:** Dùng **Airtable** (không dùng Sheets) — vì retrieve theo `task_type`
cần filter nhanh, Airtable filter theo field có sẵn, khỏi tự parse row như Sheets.

### Schema Airtable — base tên `hermes-memory`, table `reflections`

| Field name   | Type           | Ghi chú |
|---|---|---|
| `task_type`  | Single line text | vd "fetch_github", "search_flights", "skill_lookup" |
| `outcome`    | Single select (`success` / `fail`) | |
| `lesson`     | Long text      | 1-3 câu rút ra, KHÔNG phải raw log/transcript |
| `created_at` | Date (ISO)     | tự set khi ghi |
| `task_ref`   | Single line text (optional) | id/link tới task gốc nếu cần trace lại |

### Việc Antigravity cần làm

1. Tạo Airtable base `hermes-memory` + table `reflections` theo schema trên.
2. Tạo Personal Access Token (PAT) scope `data.records:read` + `data.records:write`
   chỉ trên base này — KHÔNG dùng token full-account.
3. Set env var trên VPS: `AIRTABLE_PAT`, `AIRTABLE_BASE_ID`.
4. Đăng ký 2 hàm vào `default_api` của Hermes (cùng cơ chế `fetch_url` ở ticket trước):

```python
import urllib.request, json, os, datetime

AIRTABLE_BASE = os.environ["AIRTABLE_BASE_ID"]
AIRTABLE_PAT = os.environ["AIRTABLE_PAT"]
TABLE = "reflections"

def log_reflection(task_type: str, outcome: str, lesson: str, task_ref: str = "") -> str:
    """Ghi 1 reflection sau khi task xong. outcome: 'success' hoac 'fail'."""
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE}/{TABLE}"
    payload = {"fields": {
        "task_type": task_type, "outcome": outcome, "lesson": lesson,
        "created_at": datetime.datetime.utcnow().isoformat(), "task_ref": task_ref,
    }}
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {AIRTABLE_PAT}",
                 "Content-Type": "application/json"}, method="POST")
    return urllib.request.urlopen(req).read().decode()

def retrieve_lessons(task_type: str, limit: int = 5) -> list:
    """Keo lai lesson gan nhat cung task_type, moi khi bat dau task cung loai."""
    formula = f"{{task_type}}='{task_type}'"
    url = (f"https://api.airtable.com/v0/{AIRTABLE_BASE}/{TABLE}"
           f"?filterByFormula={urllib.parse.quote(formula)}"
           f"&sort[0][field]=created_at&sort[0][direction]=desc&maxRecords={limit}")
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {AIRTABLE_PAT}"})
    data = json.loads(urllib.request.urlopen(req).read())
    return [r["fields"].get("lesson", "") for r in data.get("records", [])]
```

5. Wiring vào task loop của Hermes (Antigravity xác nhận đúng chỗ hook trong code gốc,
   Claude không có quyền xem source Hermes nên không đoán vị trí chính xác):
   - Đầu mỗi task → gọi `retrieve_lessons(task_type)` → prepend vào context/prompt
   - Cuối mỗi task → gọi `log_reflection(task_type, outcome, lesson, task_ref)`

**Validation gate (bắt buộc, không bỏ qua):** Chỉ ghi `lesson` khi nó thật sự khác/mới
so với 5 lesson gần nhất cùng `task_type` (tránh spam trùng lặp làm phình bảng vô ích).
Không cần cơ chế auto-revert phức tạp ở bản đầu — review thủ công qua Airtable UI mỗi
tuần là đủ ở quy mô hiện tại.

**Verify sau khi deploy:** báo Nobitano nhắn Hermes 2 lần cùng 1 loại lỗi (vd cố ý gọi
sai 1 API) — lần 2 phải thấy Hermes tự nhắc lại lesson từ lần 1 trong response.

**Status:** Chờ Antigravity xử lý. Blocker cho toàn bộ tầng Trí nhớ/Kế hoạch/Khám phá
trong `skills/agent-self-improvement-loops/SKILL.md`.


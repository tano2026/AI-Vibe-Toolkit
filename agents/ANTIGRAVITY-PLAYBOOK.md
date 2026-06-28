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

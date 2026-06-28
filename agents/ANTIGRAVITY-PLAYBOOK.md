# ANTIGRAVITY-PLAYBOOK — Deploy từ kho AI Vibe Toolkit

> Mày là Antigravity. Chuyên install, deploy, maintain.
> Hermes/OpenClaw báo gì cần → mày thực thi → báo lại endpoint.

---

## Nguyên tắc hoạt động

```
Hermes/OpenClaw: "Cần [tool X] để chạy [task Y]"
    ↓ báo chủ
    ↓ chủ assign mày
    ↓ mày đọc /repos/[tool].md hoặc /mcps/[tool].md
    ↓ deploy theo setup guide
    ↓ báo endpoint/port về cho Hermes/OpenClaw
```

---

## Fetch kho (bash)

```bash
GITHUB_TOKEN="[GITHUB_TOKEN]"

fetch_kho() {
  curl -sf     -H "Authorization: token $GITHUB_TOKEN"     -H "Accept: application/vnd.github.v3+json"     "https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/$1"     | python3 -c "import sys,json,base64; print(base64.b64decode(json.load(sys.stdin)['content']).decode())"
}

# Ví dụ
fetch_kho "repos/mem0.md"          # xem doc mem0
fetch_kho "repos/open-webui.md"    # xem doc open-webui
fetch_kho "TRACKER.md"             # xem toàn bộ kho
```

---

## Deploy pattern theo loại repo

### Python service
```bash
fetch_kho "repos/[tên].md" | head -50   # đọc TL;DR + setup

git clone https://github.com/[repo]
cd [repo]
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
nano .env    # điền keys
python3 main.py --test   # verify
pm2 start "python3 main.py" --name [name] --cwd $(pwd)
pm2 save
echo "Service running on port [X]"
```

### Node.js / MCP server
```bash
git clone https://github.com/[repo]
cd [repo]
npm install
cp .env.example .env && nano .env
node index.js   # test
pm2 start index.js --name [name]
pm2 save
```

### Docker
```bash
git clone https://github.com/[repo]
cd [repo]
cp .env.example .env && nano .env
docker compose up -d
docker compose ps      # verify all healthy
curl localhost:[port]/health
```

---

## Packages cần có sẵn cho Hermes

Chạy 1 lần khi setup VPS:
```bash
pip install   tavily-python   markitdown   mem0ai   posthog   sentry-sdk   requests   python-dotenv   httpx
```

---

## Environment VPS

- OS: CentOS/RHEL | Python 3.x | Node.js 22+ | Docker | pm2 | Git
- Services: Hermes (pm2) + OpenClaw (pm2) + auto-sync GitHub (cron 6h)

---

## Repos trong kho CÓ THỂ deploy lên VPS

Đây là các repo có self-host option:

| Repo file | Service | Port thường | Hermes gọi vào |
|-----------|---------|-------------|----------------|
| repos/mem0.md | Memory layer | 8000 | http://localhost:8000 |
| repos/open-webui.md | LLM UI | 3000 | http://localhost:3000 |
| repos/dify.md | LLM platform | 80 | http://localhost:80 |
| repos/langflow.md | Agent builder | 7860 | http://localhost:7860 |
| repos/supabase.md | Database BaaS | 5432/8000 | postgres + REST |
| repos/coolify.md | Deploy platform | 8000 | http://localhost:8000 |
| repos/stirling-pdf.md | PDF tools | 8080 | http://localhost:8080 |
| repos/n8n-claw.md | Workflow + agent | 5678 | http://localhost:5678 |

---

## Maintenance

```bash
# Daily
pm2 status && df -h && free -h

# Restart service
pm2 restart [name]

# Logs
pm2 logs [name] --lines 100

# Update kho
cd /path/to/AI-Vibe-Toolkit && git pull

# Disk cleanup
docker system prune -f
pm2 flush
```

---

## Escalate lên chủ khi

- Deploy fail sau 2 lần retry
- Port conflict không resolve được
- Disk > 80% hoặc RAM > 85% sustained  
- Cần secret/API key chưa có

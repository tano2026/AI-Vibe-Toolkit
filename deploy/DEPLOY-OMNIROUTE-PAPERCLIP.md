# Deploy Guide — OmniRoute + Paperclip tren VPS

> Huong dan nay danh cho Antigravity thuc thi.
> Nobitano doc de duyet truoc khi ra lenh.

---

## Yeu cau VPS

- OS: CentOS/RHEL hoac Ubuntu 20.04+
- RAM: toi thieu 4GB (khuyen nghi 8GB de chay ca hai service)
- CPU: 2 cores+
- Storage: 20GB+
- Node.js 22+ (bat buoc cho ca hai tool)
- Docker + Docker Compose (cho Paperclip)
- pm2 (quan ly process)

---

## Buoc 1 — Chuan bi moi truong (Antigravity)

```bash
# Kiem tra Node version
node --version  # phai >= 22.0.0

# Neu chua co Node 22
curl -fsSL https://rpm.nodesource.com/setup_22.x | sudo bash -
sudo yum install -y nodejs  # CentOS/RHEL
# hoac
sudo apt install -y nodejs  # Ubuntu

# Kiem tra Docker
docker --version
docker compose version

# Neu chua co Docker
curl -fsSL https://get.docker.com | sh
sudo systemctl enable docker
sudo systemctl start docker

# Cai pm2 global
npm install -g pm2

# Cai omniroute global
npm install -g omniroute
```

---

## Buoc 2 — Deploy OmniRoute (service 1)

```bash
# Khoi dong OmniRoute qua pm2
pm2 start "omniroute" --name omniroute
pm2 save

# Kiem tra chay chua
pm2 status
curl http://localhost:20128/health
# → {"status":"ok"}

# Xem logs neu can
pm2 logs omniroute
```

**OmniRoute dashboard:** Mo browser → `http://YOUR_VPS_IP:20128/dashboard`

**Add free providers (lam 1 lan tren dashboard):**
- Connections → Add Connection
- Them theo thu tu: Groq → Gemini → Mistral → Cerebras → Cloudflare
- Moi provider: sign in hoac paste API key mien phi

---

## Buoc 3 — Deploy Paperclip (service 2)

```bash
# Clone Paperclip
git clone https://github.com/paperclipai/paperclip ~/paperclip
cd ~/paperclip

# Config env
cp .env.example .env
nano .env
```

**Cac env var can dien trong .env:**
```bash
# LLM Providers
ANTHROPIC_API_KEY=your_key
OPENAI_API_KEY=your_key         # optional
GOOGLE_API_KEY=your_key         # optional

# Hoac tro ve OmniRoute (tiet kiem tien nhat)
# Paperclip se goi OmniRoute thay vi goi thang provider
OPENAI_BASE_URL=http://localhost:20128/v1
OPENAI_API_KEY=omniroute

# Database (Paperclip tu tao voi Docker)
# Khong can config them

# OpenClaw endpoint (de Paperclip giao viec cho OpenClaw)
OPENCLAW_ENDPOINT=http://localhost:YOUR_OPENCLAW_PORT
```

```bash
# Chay Paperclip voi Docker Compose
docker compose up -d

# Kiem tra
docker compose ps
# → paperclip-server   running
# → paperclip-postgres running

# Xem logs
docker compose logs -f

# Truy cap: http://YOUR_VPS_IP:3000
```

---

## Buoc 4 — Ket noi Paperclip voi OpenClaw

Tren Paperclip dashboard (`http://YOUR_VPS_IP:3000`):

```
1. Settings → Integrations → OpenClaw
2. Endpoint: http://localhost:YOUR_OPENCLAW_PORT
3. Test connection → Save

4. New Company → dat ten: "ABTRIP AI Operations"
5. Goal: "Tang 300% booking online cho ABTRIP trong 6 thang"
6. Hire agents:
   - CEO: Claude Sonnet (via OmniRoute auto/reasoning:pro)
   - Marketing Director: GPT-4o (via OmniRoute auto/chat:fast)
   - Content Creator: OpenClaw (truc tiep)
7. Budget: $50/thang
8. Review plan → Approve → Run
```

---

## Buoc 5 — Update env Hermes

Them vao env cua Hermes tren VPS:
```bash
OMNIROUTE_URL=http://localhost:20128/v1
PAPERCLIP_URL=http://localhost:3000
```

---

## Cau truc port sau khi deploy

| Service | Port | Dung |
|---------|------|------|
| OmniRoute | 20128 | LLM proxy — tat ca agent tro vao day |
| Paperclip | 3000 | Agent management dashboard |
| OpenClaw | (port hien tai) | Orchestrator nhan lenh Telegram |
| Hermes | (internal) | Python task executor |

---

## Auto-restart khi VPS reboot

```bash
# OmniRoute da co pm2 save o tren
# Them pm2 startup
pm2 startup
# → Copy lenh no tra ra, chay lenh do

# Paperclip dung Docker — tu restart nho "restart: always" trong compose
# Kiem tra
grep restart ~/paperclip/docker-compose.yml
# → phai co: restart: always
```

---

## Kiem tra sau deploy

```bash
# OmniRoute hoat dong
curl http://localhost:20128/v1/models | python3 -m json.tool | head -20

# Test LLM call qua OmniRoute
curl http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer omniroute" \
  -H "Content-Type: application/json" \
  -d '{"model":"auto/chat:fast","messages":[{"role":"user","content":"Hello"}],"max_tokens":50}'

# Paperclip health
curl http://localhost:3000/api/health

# pm2 status
pm2 status
```

---

## Lenh cho Antigravity

Khi Nobitano nhan lenh deploy, Antigravity chay theo thu tu:
1. Kiem tra Node version → upgrade neu can
2. `npm install -g omniroute pm2`
3. `pm2 start "omniroute" --name omniroute && pm2 save && pm2 startup`
4. Clone + config + `docker compose up -d` Paperclip
5. Report ket qua ve Telegram

---

## Rollback neu loi

```bash
# Dung OmniRoute
pm2 stop omniroute

# Dung Paperclip
cd ~/paperclip && docker compose down

# Hermes fallback ve Anthropic API truc tiep tu dong
# (da co fallback pattern trong HERMES-PLAYBOOK.md)
```

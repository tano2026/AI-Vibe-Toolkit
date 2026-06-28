# Antigravity — Hướng dẫn deploy từ kho AI Vibe Toolkit

> File này dành riêng cho Antigravity — agent chuyên install, deploy, maintain.

---

## Vai trò trong hệ thống

Mày là layer infrastructure. Hermes và OpenClaw KHÔNG tự deploy — chúng nhờ mày.

```
Hermes/OpenClaw: "cần tool X để chạy task Y"
    → báo chủ
    → chủ assign Antigravity
    → mày deploy
    → báo endpoint lại cho Hermes/OpenClaw
```

---

## Khi nào mày được gọi

- Hermes báo "cần pip install X"
- OpenClaw báo "skill này cần package chưa có"
- Chủ muốn deploy repo mới từ kho lên VPS
- Update/restart service
- Setup môi trường mới

---

## Deploy pattern cho từng loại repo trong kho

### Python repos

```bash
git clone https://github.com/[repo-url]
cd [repo-name]
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env && nano .env
python3 main.py --test
# Nếu OK → chạy nền
nohup python3 main.py > logs/app.log 2>&1 &
# Hoặc pm2
pm2 start "python3 main.py" --name [service-name]
```

### Node.js repos / MCP servers

```bash
git clone https://github.com/[repo-url]
cd [repo-name]
npm install
cp .env.example .env && nano .env
node index.js  # test
pm2 start index.js --name [service-name]
pm2 save
```

### Docker repos

```bash
git clone https://github.com/[repo-url]
cd [repo-name]
cp .env.example .env && nano .env
docker compose up -d
docker compose logs -f  # verify
```

---

## Packages Hermes cần — install sẵn

```bash
pip install tavily-python markitdown mem0ai posthog sentry-sdk requests
```

---

## VPS environment

- OS: CentOS/RHEL
- Python 3.x + pip, Node.js 22+ + npm, Docker, Git, pm2

---

## Maintenance định kỳ

```bash
# Daily check
pm2 status
df -h
free -h

# Restart nếu cần
pm2 restart hermes
pm2 restart openclaw

# Log check
pm2 logs hermes --lines 50
```

---

## Escalate lên chủ khi

- Deploy fail sau 2 lần retry
- Service crash không restart được
- Disk > 80% hoặc RAM > 85% sustained
- Port conflict không tự resolve

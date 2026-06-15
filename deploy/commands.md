# VPS Commands — Quick Reference

## SSH vào VPS

```bash
ssh root@YOUR_VPS_IP
# hoặc với key
ssh -i ~/.ssh/id_rsa root@YOUR_VPS_IP
```

## Lần đầu setup

```bash
# Upload và chạy setup script
scp deploy/setup-vps.sh root@YOUR_VPS_IP:~/
ssh root@YOUR_VPS_IP
bash setup-vps.sh
```

## Sau khi setup

```bash
# Điền API keys
nano ~/ai-vibe-toolkit/.env

# Source env
source ~/ai-vibe-toolkit/.env

# Config OpenClaw (guided)
openclaw onboard

# Kết nối Telegram
openclaw channels add telegram
# → Nhập Bot Token từ @BotFather

# Start tất cả services
pm2 start ~/pm2.config.js

# Verify
pm2 status
openclaw status
openclaw skills list
```

## Hàng ngày

```bash
# Check status
pm2 status

# Xem logs OpenClaw
pm2 logs openclaw --lines 50

# Xem logs Hermes
pm2 logs hermes --lines 50

# Restart nếu có vấn đề
pm2 restart openclaw
pm2 restart hermes

# Sync kho thủ công
bash ~/ai-vibe-toolkit/deploy/auto-sync.sh
```

## Update kho

```bash
# Pull latest
cd ~/ai-vibe-toolkit && git pull

# Sync skills mới vào OpenClaw
bash deploy/auto-sync.sh

# PM2 đã tự sync mỗi 6h rồi
```

## Monitoring

```bash
# Live dashboard
pm2 monit

# Disk usage
df -h

# RAM + CPU
htop

# Logs real-time
pm2 logs --lines 100
tail -f ~/logs/openclaw.log
```

## Firewall (mở port cần thiết)

```bash
# CentOS/RHEL dùng firewalld
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --permanent --add-port=3000/tcp   # OpenClaw
sudo firewall-cmd --permanent --add-port=4242/tcp   # Hermes
sudo firewall-cmd --reload

# Verify
sudo firewall-cmd --list-all
```

## Troubleshooting

```bash
# OpenClaw không start
pm2 logs openclaw --lines 100
openclaw doctor

# Hermes không nhận lệnh
pm2 logs hermes --lines 100
hermes status

# Skills không load
openclaw skills list
ls ~/.openclaw/skills/

# Telegram không nhận tin
# Check bot token đúng chưa
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getMe

# Hết RAM
free -h
pm2 restart all  # giải phóng memory leaks
```

## Backup

```bash
# Backup .env
cp ~/ai-vibe-toolkit/.env ~/env-backup-$(date +%Y%m%d).txt

# Backup OpenClaw config
cp -r ~/.openclaw ~/openclaw-backup-$(date +%Y%m%d)

# Kho đã backup tự động trên GitHub rồi
```

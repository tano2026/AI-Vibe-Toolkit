#!/usr/bin/env bash
# Đưa trang tra cứu kho lên VPS (nginx + mật khẩu + HTTPS). Chạy bằng root hoặc sudo.
#   sudo DOMAIN=kho.example.com EMAIL=ban@example.com bash deploy/kho-web/setup-kho-web.sh
# Cần: Debian/Ubuntu, domain đã trỏ A record về VPS, cổng 80 và 443 mở, kho đã clone (TOOLKIT_DIR).
# Mật khẩu do script hỏi ngay trên terminal của bạn, không lưu vào file nào trong kho.
set -euo pipefail

: "${DOMAIN:?Thiếu DOMAIN, ví dụ DOMAIN=kho.example.com}"
: "${EMAIL:?Thiếu EMAIL để cấp chứng chỉ HTTPS}"
TOOLKIT_DIR="${TOOLKIT_DIR:-$HOME/ai-vibe-toolkit}"
WEB_DIR="${WEB_DIR:-/var/www/kho}"
AUTH_USER="${AUTH_USER:-tano}"
HERE="$(cd "$(dirname "$0")" && pwd)"

[ -f "$TOOLKIT_DIR/tools/build_kho_web.py" ] || { echo "Không thấy $TOOLKIT_DIR. Clone kho trước (deploy/PRIVATE-REPO.md)."; exit 1; }

apt-get update -y
apt-get install -y nginx apache2-utils certbot python3-certbot-nginx python3

# Mật khẩu: nhập tay, không đưa vào dòng lệnh hay biến môi trường
if [ ! -f /etc/nginx/kho.htpasswd ]; then
  htpasswd -c /etc/nginx/kho.htpasswd "$AUTH_USER"
fi

python3 "$TOOLKIT_DIR/tools/build_kho_web.py" --out "$WEB_DIR"

sed "s/__DOMAIN__/$DOMAIN/g; s#__WEB_DIR__#$WEB_DIR#g" "$HERE/nginx-kho.conf" > /etc/nginx/sites-available/kho
ln -sf /etc/nginx/sites-available/kho /etc/nginx/sites-enabled/kho
nginx -t
systemctl reload nginx

certbot --nginx -d "$DOMAIN" -m "$EMAIL" --agree-tos --non-interactive --redirect

# Dựng lại trang mỗi giờ từ bản kho đã pull (auto-sync.sh lo phần git pull)
CRON="0 * * * * python3 $TOOLKIT_DIR/tools/build_kho_web.py --out $WEB_DIR >/dev/null 2>&1"
( crontab -l 2>/dev/null | grep -v build_kho_web.py; echo "$CRON" ) | crontab -

echo "Xong: https://$DOMAIN  (tài khoản: $AUTH_USER)"

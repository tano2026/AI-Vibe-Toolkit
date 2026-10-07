#!/usr/bin/env bash
# Cài Twenty CRM (self-host, Docker) cho ABTRIP — chạy trên VPS Linux.
# Dựa trên docker-compose.yml + .env.example CHÍNH THỨC của twentyhq/twenty (đọc 07/10/2026).
# CHƯA chạy thử trên VPS thật — chạy xong phải chạy test-twenty-api.py (PASS/FAIL).
#
# Dùng:
#   SERVER_URL="https://TEN-MAY.TEN-TAILNET.ts.net" bash install-twenty.sh
#   (SERVER_URL phải là địa chỉ mà NHÂN VIÊN gõ vào trình duyệt; sai là đăng nhập lỗi.)
#   Chưa có Tailscale, chỉ thử trên chính VPS: SERVER_URL="http://localhost:3000"
set -euo pipefail

VERSION="${VERSION:-v2.45.0}"            # ghim phiên bản, đổi có chủ đích (xem GitHub Security Advisories trước)
DIR="${DIR:-$HOME/twenty-abtrip}"
SERVER_URL="${SERVER_URL:-http://localhost:3000}"
BASE="https://raw.githubusercontent.com/twentyhq/twenty/twenty/${VERSION}/packages/twenty-docker"

command -v docker >/dev/null || { echo "Thiếu docker"; exit 1; }
docker compose version >/dev/null 2>&1 || { echo "Thiếu docker compose plugin (v2)"; exit 1; }
command -v openssl >/dev/null || { echo "Thiếu openssl"; exit 1; }
[ -e "$DIR/.env" ] && { echo "$DIR/.env đã có — dừng, không ghi đè. Muốn cài lại: tự backup rồi xoá thư mục."; exit 1; }

mkdir -p "$DIR" && cd "$DIR"
curl -fsSL --retry 3 "$BASE/docker-compose.yml" -o docker-compose.yml
curl -fsSL --retry 3 "$BASE/.env.example"       -o .env

sed -i "s/^TAG=.*/TAG=${VERSION}/" .env
sed -i "s#^SERVER_URL=.*#SERVER_URL=${SERVER_URL}#" .env
{
  echo ""
  echo "# === Sinh ngẫu nhiên lúc cài — KHÔNG commit, KHÔNG gửi vào chat ==="
  echo "ENCRYPTION_KEY=$(openssl rand -base64 32)"
  echo "PG_DATABASE_PASSWORD=$(openssl rand -hex 32)"
} >> .env
chmod 600 .env

# Chỉ nghe trên localhost của VPS — truy cập từ ngoài đi qua Tailscale (xem HUONG-DAN-TRIEN-KHAI.md).
sed -i 's/"3000:3000"/"127.0.0.1:3000:3000"/' docker-compose.yml
grep -q '127.0.0.1:3000:3000' docker-compose.yml || { echo "Không khoá được cổng 3000 vào localhost — dừng."; exit 1; }

docker compose pull
docker compose up -d

echo "Chờ Twenty lên (tối đa ~3 phút)..."
for i in $(seq 1 36); do
  if curl -fsS http://127.0.0.1:3000/healthz >/dev/null 2>&1; then
    echo "OK: Twenty $VERSION chạy tại 127.0.0.1:3000 (SERVER_URL=$SERVER_URL)"
    echo "Việc tiếp: tạo tài khoản admin đầu tiên, rồi chạy backup + test (xem HUONG-DAN-TRIEN-KHAI.md)."
    exit 0
  fi
  sleep 5
done
echo "Chưa healthy sau 3 phút. Xem log:  cd $DIR && docker compose logs --tail=100 server"
exit 1

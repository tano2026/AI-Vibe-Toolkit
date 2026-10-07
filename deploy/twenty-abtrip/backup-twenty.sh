#!/usr/bin/env bash
# Backup Postgres + file upload của Twenty. Chạy tay hoặc cron hằng ngày.
#   cron:  30 2 * * *  bash $HOME/twenty-abtrip/backup-twenty.sh >> $HOME/twenty-backup.log 2>&1
set -euo pipefail
DIR="${DIR:-$HOME/twenty-abtrip}"
OUT="${BACKUP_DIR:-$HOME/twenty-backups}"
KEEP_DAYS="${KEEP_DAYS:-14}"
cd "$DIR"
set -a; . ./.env; set +a
mkdir -p "$OUT"; chmod 700 "$OUT"
STAMP="$(date +%F-%H%M)"
docker compose exec -T db pg_dump -U "${PG_DATABASE_USER:-postgres}" -d "${PG_DATABASE_NAME:-default}" | gzip > "$OUT/twenty-db-$STAMP.sql.gz"
# file upload (nằm trong volume server-local-data)
docker run --rm -v twenty_server-local-data:/data -v "$OUT":/out alpine tar czf "/out/twenty-files-$STAMP.tgz" -C /data . 2>/dev/null || echo "(bỏ qua backup file: kiểm tra tên volume bằng 'docker volume ls')"
# kiểm tra file backup không rỗng
[ -s "$OUT/twenty-db-$STAMP.sql.gz" ] || { echo "BACKUP DB RỖNG — LỖI"; exit 1; }
find "$OUT" -name 'twenty-*' -mtime +"$KEEP_DAYS" -delete
echo "Backup xong: $OUT/twenty-db-$STAMP.sql.gz"
echo "Nhớ: chép bản backup sang máy/ổ khác (backup cùng VPS không cứu được khi VPS hỏng)."

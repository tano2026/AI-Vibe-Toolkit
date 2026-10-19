#!/bin/bash
# auto-sync.sh — tự động pull kho mới nhất và sync skills
# PM2 chạy cái này mỗi 6h
#
# Cố ý KHÔNG dùng `set -e`: trước đây một lệnh cp lỗi (vd skills/ecc không còn)
# làm script chết SAU `git pull`; lần chạy kế tiếp không còn commit mới nên
# không bao giờ đồng bộ lại. Giờ ghi lại SHA đã đồng bộ xong (STAMP) và đồng bộ
# lại khi HEAD khác STAMP, kể cả khi không có commit mới.

TOOLKIT_DIR="${TOOLKIT_DIR:-$HOME/ai-vibe-toolkit}"
OPENCLAW_SKILLS="${OPENCLAW_SKILLS:-$HOME/.openclaw/skills}"
LOG="${LOG:-$HOME/logs/kho-sync.log}"
STAMP="${STAMP:-$HOME/.openclaw/.kho-synced-sha}"

mkdir -p "$(dirname "$LOG")" "$OPENCLAW_SKILLS" "$(dirname "$STAMP")"

log() { echo "[$(date)] $*" >> "$LOG"; }

log "Starting kho sync..."

cd "$TOOLKIT_DIR" || { log "Không vào được $TOOLKIT_DIR"; exit 1; }

# Pull latest từ GitHub
git fetch origin main || { log "git fetch lỗi — bỏ qua lượt này"; exit 1; }
CHANGES=$(git rev-list HEAD..origin/main --count)

if [ "$CHANGES" -gt 0 ]; then
  log "$CHANGES commits mới — pulling..."
  git pull origin main || { log "git pull lỗi — dừng, thử lại lượt sau"; exit 1; }
fi

HEAD_SHA=$(git rev-parse HEAD)
SYNCED_SHA=$(cat "$STAMP" 2>/dev/null || true)

if [ "$CHANGES" -gt 0 ] || [ "$HEAD_SHA" != "$SYNCED_SHA" ]; then
  FAILED=0

  # sync_dir <nguồn> <đích>: thiếu nguồn thì cảnh báo và bỏ qua, lỗi copy thì đếm
  sync_dir() {
    if [ ! -d "$1" ]; then
      log "Cảnh báo: bỏ qua $1 (không tồn tại)"
      return 0
    fi
    mkdir -p "$2" && cp -r "$1/." "$2/" || { log "Lỗi copy $1"; FAILED=$((FAILED + 1)); }
  }

  sync_dir skills/ecc "$OPENCLAW_SKILLS/ecc"
  sync_dir skills/viral-hooks "$OPENCLAW_SKILLS/viral-hooks"
  for f in skills/*.md; do
    [ -f "$f" ] && { cp "$f" "$OPENCLAW_SKILLS/" || FAILED=$((FAILED + 1)); }
  done

  if [ "$FAILED" -eq 0 ]; then
    echo "$HEAD_SHA" > "$STAMP"
    log "Sync xong — HEAD ${HEAD_SHA:0:8}, $CHANGES commits mới"
  else
    log "Sync xong NHƯNG $FAILED bước lỗi — sẽ thử lại lượt sau"
  fi

  # Notify Telegram (chỉ khi có commit mới)
  if [ "$CHANGES" -gt 0 ] && [ -n "$TELEGRAM_BOT_TOKEN" ] && [ -n "$TELEGRAM_CHAT_ID" ]; then
    MSG="🔄 Kho sync: $CHANGES commits mới
$(git log --oneline -5)"
    curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
      -d chat_id="$TELEGRAM_CHAT_ID" \
      --data-urlencode text="$MSG" > /dev/null
  fi
  [ "$FAILED" -eq 0 ]
else
  log "Không có gì mới"
fi

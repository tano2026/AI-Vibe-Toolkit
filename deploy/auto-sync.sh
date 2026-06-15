#!/bin/bash
# auto-sync.sh — tự động pull kho mới nhất và sync skills
# PM2 chạy cái này mỗi 6h

set -e
TOOLKIT_DIR="$HOME/ai-vibe-toolkit"
OPENCLAW_SKILLS="$HOME/.openclaw/skills"
LOG="$HOME/logs/kho-sync.log"

echo "[$(date)] Starting kho sync..." >> "$LOG"

# Pull latest từ GitHub
cd "$TOOLKIT_DIR"
git fetch origin main
CHANGES=$(git rev-list HEAD..origin/main --count)

if [ "$CHANGES" -gt "0" ]; then
  echo "[$(date)] $CHANGES commits mới — pulling..." >> "$LOG"
  git pull origin main

  # Sync skills mới vào OpenClaw
  cp -r skills/ecc/* "$OPENCLAW_SKILLS/ecc/" 2>/dev/null
  cp skills/*.md "$OPENCLAW_SKILLS/" 2>/dev/null
  cp skills/viral-hooks/* "$OPENCLAW_SKILLS/viral-hooks/" 2>/dev/null

  echo "[$(date)] Sync xong — $CHANGES commits mới" >> "$LOG"

  # Notify Telegram
  if [ -n "$TELEGRAM_BOT_TOKEN" ] && [ -n "$TELEGRAM_CHAT_ID" ]; then
    MSG="🔄 Kho sync: $CHANGES commits mới\n$(git log --oneline -5)"
    curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
      -d chat_id="$TELEGRAM_CHAT_ID" \
      -d text="$MSG" > /dev/null
  fi
else
  echo "[$(date)] Không có gì mới" >> "$LOG"
fi

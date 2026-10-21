#!/bin/bash
# ============================================================
# AI Vibe Toolkit — VPS Setup Script
# OS: CentOS/RHEL | Specs: 2-4 CPU, 4-8GB RAM
# Chạy với: bash setup-vps.sh
# ============================================================

set -e
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'
log()  { echo -e "${GREEN}[$(date +%H:%M:%S)] ✅ $1${NC}"; }
warn() { echo -e "${YELLOW}[$(date +%H:%M:%S)] ⚠️  $1${NC}"; }
err()  { echo -e "${RED}[$(date +%H:%M:%S)] ❌ $1${NC}"; exit 1; }

echo "🚀 AI Vibe Toolkit VPS Setup — CentOS/RHEL"
echo "============================================"

# ============================================================
# BƯỚC 1: System Update + Packages
# ============================================================
log "Bước 1: System update..."
sudo dnf update -y 2>/dev/null || sudo yum update -y
sudo dnf install -y git curl wget unzip tmux htop nano 2>/dev/null || \
  sudo yum install -y git curl wget unzip tmux htop nano

# ============================================================
# BƯỚC 2: Node.js 22 (LTS)
# ============================================================
log "Bước 2: Cài Node.js 22..."
if ! command -v node &>/dev/null || [[ $(node -v | cut -d. -f1 | tr -d 'v') -lt 20 ]]; then
  # KHÔNG `curl | sudo bash`: tải về file, để người đọc rồi mới chạy bằng sudo.
  # URL ghim major 22 (setup_22.x). Sau khi đọc file, chạy lại với NODESOURCE_REVIEWED=1
  # (hoặc trả lời y khi được hỏi). Có thể thay bằng cài Node từ gói của distro nếu muốn.
  NODESOURCE_SCRIPT="$(mktemp /tmp/nodesource-setup-XXXXXX.sh)"
  curl -fsSL -o "$NODESOURCE_SCRIPT" https://rpm.nodesource.com/setup_22.x
  echo "sha256: $(sha256sum "$NODESOURCE_SCRIPT" | cut -d' ' -f1)"
  echo "Đã tải script NodeSource về $NODESOURCE_SCRIPT — hãy ĐỌC nó trước khi chạy:"
  echo "  less $NODESOURCE_SCRIPT"
  if [ "${NODESOURCE_REVIEWED:-0}" != "1" ]; then
    if [ -r /dev/tty ]; then
      read -r -p "Đã đọc và đồng ý chạy bằng sudo? [y/N] " ANS < /dev/tty
      [ "$ANS" = "y" ] || [ "$ANS" = "Y" ] || err "Dừng: chưa xác nhận script NodeSource. Đọc xong thì chạy lại với NODESOURCE_REVIEWED=1"
    else
      err "Không có terminal để xác nhận. Đọc $NODESOURCE_SCRIPT rồi chạy lại với NODESOURCE_REVIEWED=1"
    fi
  fi
  sudo bash "$NODESOURCE_SCRIPT"
  sudo dnf install -y nodejs 2>/dev/null || sudo yum install -y nodejs
fi
node -v && npm -v
log "Node.js $(node -v) ready"

# ============================================================
# BƯỚC 3: Python 3 + pip
# ============================================================
log "Bước 3: Cài Python 3..."
sudo dnf install -y python3 python3-pip 2>/dev/null || \
  sudo yum install -y python3 python3-pip
pip3 install --upgrade pip
pip3 install requests anthropic pandas python-dotenv
log "Python $(python3 --version) ready"

# ============================================================
# BƯỚC 4: Clone AI Vibe Toolkit
# ============================================================
log "Bước 4: Clone AI Vibe Toolkit..."
TOOLKIT_DIR="$HOME/ai-vibe-toolkit"
if [ -d "$TOOLKIT_DIR" ]; then
  warn "Đã có $TOOLKIT_DIR — pulling latest..."
  cd "$TOOLKIT_DIR" && git pull
else
  # Repo là PRIVATE: cần deploy key chỉ đọc đã gắn vào máy này (xem deploy/PRIVATE-REPO.md).
  # Ghi đè địa chỉ bằng TOOLKIT_REPO nếu dùng cách khác (vd. SSH alias trong ~/.ssh/config).
  TOOLKIT_REPO="${TOOLKIT_REPO:-git@github.com:tano2026/AI-Vibe-Toolkit.git}"
  git clone "$TOOLKIT_REPO" "$TOOLKIT_DIR" ||     err "Không clone được $TOOLKIT_REPO. Repo đang private: gắn deploy key chỉ đọc cho máy này rồi chạy lại (deploy/PRIVATE-REPO.md)."
fi
log "Kho cloned tại $TOOLKIT_DIR"

# ============================================================
# BƯỚC 5: Cài OpenClaw
# ============================================================
log "Bước 5: Cài OpenClaw..."
npm install -g openclaw
openclaw --version && log "OpenClaw ready"

# ============================================================
# BƯỚC 6: Cài Hermes Agent
# ============================================================
log "Bước 6: Cài Hermes Agent..."
npm install -g hermes-agent 2>/dev/null || \
  npm install -g @nousresearch/hermes-agent 2>/dev/null || \
  warn "Hermes cần cài thủ công (deploy/hermes-setup.md CHƯA có trong kho — dùng tài liệu của Hermes)"

# ============================================================
# BƯỚC 7: Cài ClawHub + Skills
# ============================================================
log "Bước 7: Cài ClawHub..."
npm install -g clawhub
clawhub --version

# Cài core skills từ ClawHub
log "Cài core skills từ ClawHub..."
clawhub install coding-agent || warn "Bỏ qua coding-agent"
clawhub install github       || warn "Bỏ qua github skill"
clawhub install clawhub      || warn "Bỏ qua clawhub skill"

# ============================================================
# BƯỚC 8: Sync Skills Từ Kho Vào OpenClaw
# ============================================================
log "Bước 8: Sync skills từ kho..."
OPENCLAW_SKILLS="$HOME/.openclaw/skills"
mkdir -p "$OPENCLAW_SKILLS"

# ECC 262 skills
mkdir -p "$OPENCLAW_SKILLS/ecc"
cp -r "$TOOLKIT_DIR/skills/ecc/"* "$OPENCLAW_SKILLS/ecc/" 2>/dev/null && log "ECC skills synced"

# Agent skills (Addy Osmani)
mkdir -p "$OPENCLAW_SKILLS/agent-skills"
cp -r "$TOOLKIT_DIR/skills/agent-skills/"* "$OPENCLAW_SKILLS/agent-skills/" 2>/dev/null && log "agent-skills synced"

# Taste skill
mkdir -p "$OPENCLAW_SKILLS/taste-skill"
cp -r "$TOOLKIT_DIR/skills/taste-skill/"* "$OPENCLAW_SKILLS/taste-skill/" 2>/dev/null && log "taste-skill synced"

# Viral hooks
mkdir -p "$OPENCLAW_SKILLS/viral-hooks"
cp -r "$TOOLKIT_DIR/skills/viral-hooks/"* "$OPENCLAW_SKILLS/viral-hooks/" 2>/dev/null && log "viral-hooks synced"

# Root skills
cp "$TOOLKIT_DIR/skills/"*.md "$OPENCLAW_SKILLS/" 2>/dev/null && log "Root skills synced"

# AI Vibe Toolkit skill (custom)
cp "$TOOLKIT_DIR/configs/openclaw-ai-vibe-skill.md" "$OPENCLAW_SKILLS/ai-vibe-toolkit.md" 2>/dev/null

log "Tổng skills: $(ls $OPENCLAW_SKILLS/**/*.md 2>/dev/null | wc -l) files"

# ============================================================
# BƯỚC 9: Setup .env
# ============================================================
log "Bước 9: Setup environment variables..."
ENV_FILE="$TOOLKIT_DIR/.env"
if [ ! -f "$ENV_FILE" ]; then
  cp "$TOOLKIT_DIR/deploy/env.example" "$ENV_FILE"
  warn "Điền API keys vào: $ENV_FILE"
  warn "Sau đó chạy: source $ENV_FILE"
fi

# ============================================================
# BƯỚC 10: Cài PM2 (process manager)
# ============================================================
log "Bước 10: Cài PM2..."
npm install -g pm2
# Không pipe thẳng vào bash: pm2 in ra 1 lệnh sudo, in lại cho người đọc rồi tự chạy.
PM2_STARTUP_CMD="$(pm2 startup systemd -u "$USER" --hp "$HOME" 2>/dev/null | tail -1)"
warn "Để PM2 tự chạy khi reboot, đọc rồi chạy tay lệnh sau:"
echo "  $PM2_STARTUP_CMD"
log "PM2 ready"

# ============================================================
# BƯỚC 11: Tạo PM2 ecosystem config
# ============================================================
log "Bước 11: Tạo PM2 config..."
cp "$TOOLKIT_DIR/deploy/pm2.config.js" "$HOME/pm2.config.js"

# ============================================================
# HOÀN THÀNH
# ============================================================
echo ""
echo "============================================"
echo -e "${GREEN}🎉 Setup hoàn tất!${NC}"
echo "============================================"
echo ""
echo "Bước tiếp theo:"
echo "1. Điền API keys: nano $TOOLKIT_DIR/.env"
echo "2. Config OpenClaw: openclaw onboard"
echo "3. Kết nối Telegram: openclaw channels add telegram"
echo "4. Start services: pm2 start $HOME/pm2.config.js"
echo "5. Monitor: pm2 status"
echo ""
echo "Quick test:"
echo "  openclaw skills list"
echo "  openclaw status"

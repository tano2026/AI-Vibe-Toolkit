#!/bin/bash
# sync-to-openclaw.sh
# Sync toàn bộ AI Vibe Toolkit skills vào OpenClaw
# Chạy: bash configs/sync-to-openclaw.sh

set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OPENCLAW_SKILLS="${HOME}/.openclaw/skills"

echo "🦞 Syncing AI Vibe Toolkit → OpenClaw..."
echo "From: $REPO_DIR"
echo "To:   $OPENCLAW_SKILLS"

# Tạo thư mục nếu chưa có
mkdir -p "$OPENCLAW_SKILLS"

# Link/copy AI Vibe Toolkit skill file
cp "$REPO_DIR/configs/openclaw-ai-vibe-skill.md" "$OPENCLAW_SKILLS/ai-vibe-toolkit.md"
echo "✅ ai-vibe-toolkit skill"

# Sync ECC skills (262 files)
mkdir -p "$OPENCLAW_SKILLS/ecc"
cp -r "$REPO_DIR/skills/ecc/"* "$OPENCLAW_SKILLS/ecc/"
echo "✅ ECC skills (262 files)"

# Sync agent-skills (Addy Osmani)
mkdir -p "$OPENCLAW_SKILLS/agent-skills"
cp -r "$REPO_DIR/skills/agent-skills/"* "$OPENCLAW_SKILLS/agent-skills/"
echo "✅ agent-skills (24 files)"

# Sync taste-skill
mkdir -p "$OPENCLAW_SKILLS/taste-skill"
cp -r "$REPO_DIR/skills/taste-skill/"* "$OPENCLAW_SKILLS/taste-skill/"
echo "✅ taste-skill (10 files)"

# Sync affiliate-skills
mkdir -p "$OPENCLAW_SKILLS/affiliate-skills"
cp -r "$REPO_DIR/skills/affiliate-skills/"* "$OPENCLAW_SKILLS/affiliate-skills/"
echo "✅ affiliate-skills (17 files)"

# Sync viral-hooks
mkdir -p "$OPENCLAW_SKILLS/viral-hooks"
cp -r "$REPO_DIR/skills/viral-hooks/"* "$OPENCLAW_SKILLS/viral-hooks/"
echo "✅ viral-hooks (3 files)"

# Sync claude-ads
mkdir -p "$OPENCLAW_SKILLS/claude-ads"
cp -r "$REPO_DIR/skills/claude-ads/"* "$OPENCLAW_SKILLS/claude-ads/"
echo "✅ claude-ads (9 files)"

# Sync root skills (kế toán, marketing, social media...)
for f in "$REPO_DIR/skills/"*.md; do
    [ -f "$f" ] && cp "$f" "$OPENCLAW_SKILLS/" && echo "  ✅ $(basename $f)"
done
echo "✅ Root skills"

# Copy USER context
if [ -f "$REPO_DIR/configs/hermes-user-template.md" ]; then
    cp "$REPO_DIR/configs/hermes-user-template.md" "$OPENCLAW_SKILLS/USER-CONTEXT.md"
    echo "✅ USER context"
fi

echo ""
echo "🎉 Sync complete!"
echo ""
echo "Next steps:"
echo "1. openclaw skills list  (verify skills loaded)"
echo "2. openclaw mcp list     (check MCPs)"
echo "3. Nhắn Telegram: 'kho có gì' để test"

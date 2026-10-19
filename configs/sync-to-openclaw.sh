#!/bin/bash
# sync-to-openclaw.sh
# Sync AI Vibe Toolkit skills vào OpenClaw
# Chạy: bash configs/sync-to-openclaw.sh
#
# Thư mục nguồn nào không tồn tại (vd skills/ecc đã gộp/đổi tên) thì in cảnh báo
# và BỎ QUA êm, không dừng cả script. Không dùng `set -e` để một bước hỏng
# không làm mất các bước còn lại; lỗi copy thật được đếm và báo ở cuối (exit 1).

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OPENCLAW_SKILLS="${OPENCLAW_SKILLS:-${HOME}/.openclaw/skills}"
FAILED=0
SKIPPED=0

echo "🦞 Syncing AI Vibe Toolkit → OpenClaw..."
echo "From: $REPO_DIR"
echo "To:   $OPENCLAW_SKILLS"

# Tạo thư mục nếu chưa có
mkdir -p "$OPENCLAW_SKILLS" || { echo "❌ Không tạo được $OPENCLAW_SKILLS"; exit 1; }

# sync_dir <tên thư mục con của skills/>
sync_dir() {
    local name="$1"
    local src="$REPO_DIR/skills/$name"
    local dst="$OPENCLAW_SKILLS/$name"
    if [ ! -d "$src" ]; then
        echo "⚠️  Bỏ qua $name: không có thư mục $src"
        SKIPPED=$((SKIPPED + 1))
        return 0
    fi
    mkdir -p "$dst" && cp -r "$src/." "$dst/"
    if [ $? -eq 0 ]; then
        echo "✅ $name ($(find "$src" -type f | wc -l | tr -d ' ') files)"
    else
        echo "❌ Lỗi khi copy $name"
        FAILED=$((FAILED + 1))
    fi
}

# Link/copy AI Vibe Toolkit skill file
if [ -f "$REPO_DIR/configs/openclaw-ai-vibe-skill.md" ]; then
    cp "$REPO_DIR/configs/openclaw-ai-vibe-skill.md" "$OPENCLAW_SKILLS/ai-vibe-toolkit.md" \
        && echo "✅ ai-vibe-toolkit skill" || FAILED=$((FAILED + 1))
else
    echo "⚠️  Bỏ qua ai-vibe-toolkit skill: không có configs/openclaw-ai-vibe-skill.md"
    SKIPPED=$((SKIPPED + 1))
fi

# ECC, agent-skills (Addy Osmani), taste-skill, affiliate-skills, viral-hooks, claude-ads
for d in ecc agent-skills taste-skill affiliate-skills viral-hooks claude-ads; do
    sync_dir "$d"
done

# Sync root skills (kế toán, marketing, social media...)
for f in "$REPO_DIR/skills/"*.md; do
    [ -f "$f" ] && cp "$f" "$OPENCLAW_SKILLS/" && echo "  ✅ $(basename "$f")"
done
echo "✅ Root skills"

# Copy USER context
if [ -f "$REPO_DIR/configs/hermes-user-template.md" ]; then
    cp "$REPO_DIR/configs/hermes-user-template.md" "$OPENCLAW_SKILLS/USER-CONTEXT.md"
    echo "✅ USER context"
fi

echo ""
if [ "$FAILED" -gt 0 ]; then
    echo "⚠️  Sync xong NHƯNG có $FAILED bước lỗi, $SKIPPED bước bỏ qua"
else
    echo "🎉 Sync complete! ($SKIPPED bước bỏ qua vì thiếu nguồn)"
fi
echo ""
echo "Next steps:"
echo "1. openclaw skills list  (verify skills loaded)"
echo "2. openclaw mcp list     (check MCPs)"
echo "3. Nhắn Telegram: 'kho có gì' để test"

[ "$FAILED" -eq 0 ]

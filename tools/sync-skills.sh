#!/bin/bash
# ╔══════════════════════════════════════════════╗
# ║   AI Vibe Toolkit — Skills Syncer v1.0     ║
# ║   Chạy lại bất cứ lúc nào: sync-skills     ║
# ╚══════════════════════════════════════════════╝

TOKEN="[GITHUB_TOKEN]"
REPO="tano2026/AI-Vibe-Toolkit"
TARGET="$HOME/.claude/skills"
GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; BLUE='\033[0;34m'; NC='\033[0m'

echo ""
echo -e "${BLUE}🔄 AI Vibe Toolkit — Sync Skills${NC}"
echo ""

# Kiểm tra token
if [[ "$TOKEN" == "[GITHUB_TOKEN]" ]]; then
    echo -e "${RED}❌ Token chưa được cấu hình. Chạy setup command lần đầu.${NC}"
    exit 1
fi

# Kiểm tra kết nối
HTTP=$(curl -s -o /dev/null -w "%{http_code}" -H "Authorization: token $TOKEN" \
    "https://api.github.com/repos/$REPO")
if [[ "$HTTP" != "200" ]]; then
    echo -e "${RED}❌ Không kết nối được (HTTP $HTTP)${NC}"; exit 1
fi
echo -e "${GREEN}✅ Kết nối OK${NC}"; echo ""

mkdir -p "$TARGET"

# Ghi Python syncer ra file tạm
PYFILE=$(mktemp /tmp/aivibe_sync_XXXXXX.py)
cat > "$PYFILE" << 'PYEOF'
import sys, json, os, urllib.request, time

TOKEN = sys.argv[1]
REPO = sys.argv[2]
TARGET = sys.argv[3]
folder = sys.argv[4]
SKIP = {'README.md','TRACKER.md','KHO-INDEX.md','_template.md','TRACKER_old.md'}

url = f"https://api.github.com/repos/{REPO}/contents/{folder}"
req = urllib.request.Request(url, headers={"Authorization": f"token {TOKEN}"})
try:
    data = json.loads(urllib.request.urlopen(req).read())
except Exception as e:
    print(f"ERROR:{e}"); sys.exit(1)

if not isinstance(data, list):
    print(f"ERROR:{data.get('message','')}"); sys.exit(1)

ok = 0; fail = 0
for x in data:
    name = x.get('name','')
    if not name.endswith('.md') or name.startswith('_') or name in SKIP:
        continue
    skill_name = name[:-3]
    skill_dir = os.path.join(TARGET, skill_name)
    os.makedirs(skill_dir, exist_ok=True)
    try:
        req2 = urllib.request.Request(
            x['download_url'],
            headers={"Authorization": f"token {TOKEN}"}
        )
        content = urllib.request.urlopen(req2).read()
        with open(os.path.join(skill_dir, 'SKILL.md'), 'wb') as f:
            f.write(content)
        ok += 1
        time.sleep(0.05)
    except Exception as e:
        fail += 1
print(f"{ok} {fail}")
PYEOF

TOTAL_OK=0; TOTAL_FAIL=0
for folder in skills mcps repos stacks agents; do
    echo -e "  📁 /${folder}/..."
    RESULT=$(python3 "$PYFILE" "$TOKEN" "$REPO" "$TARGET" "$folder" 2>&1)
    if echo "$RESULT" | grep -q "^ERROR:"; then
        echo -e "     ${RED}❌ Lỗi: $RESULT${NC}"
        continue
    fi
    OK=$(echo "$RESULT" | awk '{print $1}')
    FAIL=$(echo "$RESULT" | awk '{print $2}')
    OK=${OK:-0}; FAIL=${FAIL:-0}
    TOTAL_OK=$((TOTAL_OK + OK))
    TOTAL_FAIL=$((TOTAL_FAIL + FAIL))
    if [[ "$FAIL" -gt "0" ]]; then
        echo -e "     ${YELLOW}⚠️  $OK OK · $FAIL lỗi${NC}"
    else
        echo -e "     ${GREEN}✅ $OK skills${NC}"
    fi
done

rm -f "$PYFILE"

echo ""
if [[ "$TOTAL_FAIL" -eq "0" ]]; then
    echo -e "${GREEN}✅ Xong! $TOTAL_OK skills → ~/.claude/skills/${NC}"
else
    echo -e "${YELLOW}⚠️  $TOTAL_OK OK · $TOTAL_FAIL lỗi (chạy lại để retry)${NC}"
fi
echo -e "   👉 Restart Claude Code session để load skills mới."
echo ""

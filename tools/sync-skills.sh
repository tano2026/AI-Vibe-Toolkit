#!/bin/bash
TOKEN="[GITHUB_TOKEN]"
REPO="tano2026/AI-Vibe-Toolkit"
TARGET="$HOME/.claude/skills"
GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; BLUE='\033[0;34m'; NC='\033[0m'

# Check token — split string để sed không replace dòng này
_PH="[GITHUB""_TOKEN]"
if [[ "$TOKEN" == "$_PH" ]]; then
    echo -e "${RED}❌ Token chưa được cấu hình.${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}🔄 AI Vibe Toolkit — Sync Skills${NC}"
echo ""

# Kiểm tra kết nối
HTTP=$(curl -s -o /dev/null -w "%{http_code}" \
    -H "Authorization: token $TOKEN" \
    "https://api.github.com/repos/$REPO")
if [[ "$HTTP" != "200" ]]; then
    echo -e "${RED}❌ Lỗi kết nối GitHub (HTTP $HTTP)${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Kết nối OK${NC}"; echo ""

mkdir -p "$TARGET"

# Python syncer — ghi ra file tạm để tránh heredoc conflict
PY=$(mktemp /tmp/sync_XXXXXX.py)
cat > "$PY" << 'PYEOF'
import sys, json, os, urllib.request, time

TOKEN, REPO, TARGET, folder = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
SKIP = {'README.md','TRACKER.md','KHO-INDEX.md','_template.md','TRACKER_old.md'}

try:
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/contents/{folder}",
        headers={"Authorization": f"token {TOKEN}"}
    )
    data = json.loads(urllib.request.urlopen(req).read())
except Exception as e:
    print(f"0 ERR:{e}"); sys.exit(0)

if not isinstance(data, list):
    print(f"0 ERR:{data.get('message','')}"); sys.exit(0)

ok = fail = 0
for x in data:
    name = x.get('name','')
    if not name.endswith('.md') or name.startswith('_') or name in SKIP:
        continue
    d = os.path.join(TARGET, name[:-3])
    os.makedirs(d, exist_ok=True)
    try:
        r = urllib.request.Request(x['download_url'],
            headers={"Authorization": f"token {TOKEN}"})
        with open(os.path.join(d,'SKILL.md'),'wb') as f:
            f.write(urllib.request.urlopen(r).read())
        ok += 1
        time.sleep(0.05)
    except:
        fail += 1

print(f"{ok} {fail}")
PYEOF

TOTAL_OK=0; TOTAL_FAIL=0
for folder in skills mcps repos stacks agents; do
    echo -e "  📁 /${folder}/..."
    RESULT=$(python3 "$PY" "$TOKEN" "$REPO" "$TARGET" "$folder")
    OK=$(echo "$RESULT" | awk '{print $1}')
    FAIL=$(echo "$RESULT" | awk '{print $2}')
    ERR=$(echo "$RESULT" | grep "ERR:" | sed 's/0 ERR://')
    OK=${OK:-0}; FAIL=${FAIL:-0}
    TOTAL_OK=$((TOTAL_OK+OK)); TOTAL_FAIL=$((TOTAL_FAIL+FAIL))
    if [[ -n "$ERR" ]]; then
        echo -e "     ${RED}❌ $ERR${NC}"
    elif [[ "$FAIL" -gt 0 ]]; then
        echo -e "     ${YELLOW}⚠️  $OK OK · $FAIL lỗi${NC}"
    else
        echo -e "     ${GREEN}✅ $OK skills${NC}"
    fi
done

rm -f "$PY"

echo ""
echo -e "${GREEN}╔══════════════════════════════════════╗${NC}"
printf "${GREEN}║  ✅ Xong! %-5s skills synced        ║${NC}\n" "$TOTAL_OK"
echo -e "${GREEN}╚══════════════════════════════════════╝${NC}"
echo ""
echo -e "  📂 ~/.claude/skills/"
echo -e "  💡 Mở ${YELLOW}New session${NC} trong Claude Code để dùng."
echo ""
[[ $TOTAL_FAIL -gt 0 ]] && echo -e "${YELLOW}⚠️  $TOTAL_FAIL files lỗi — chạy lại: sync-skills${NC}"

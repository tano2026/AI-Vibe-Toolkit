---
name: skillops
description: >
  CLI quan ly skill AI agent o quy mo to chuc — "SkillOps la cai DevOps danh
  cho ha tang". Lint 24 rule (SKL100-SKL507), eval 3-agent scoring, registry
  git-based, sync cross-platform co drift detection, telemetry 2 tang local.
  Giai quyet dung van de kho AI-Vibe-Toolkit vua gap: skill trung lap khong
  ai biet, khong version, khong lifecycle. Rat moi (0 star, chua release).
---

# skillops (Xerus-ai/skillops) — GitHub Repo

## TL;DR
skops la 1 CLI de quan ly skill file (SKILL.md) cho AI coding agent o quy mo lon — dung nhu
DevOps quan ly ha tang vay. No lint, danh gia, dong bo, va theo doi (observability) toan bo
skill trong 1 to chuc, giai quyet dung van de: skill lung tung o Slack, folder ca nhan, khong
ai biet ban nao dung, ban nao trung, ban nao con hoat dong tot.

## Repo nay dung de lam gi
Van de tac gia neu ra khop 100% voi cai kho AI-Vibe-Toolkit vua trai qua: khi to chuc dung
nhieu AI coding agent (Claude, Copilot, Cursor, Codex, Gemini), skill sinh ra khong co cau truc
se dan toi trung lap, drift (skill bi sua tay ma khong ai biet), xung dot, va khong ai do luong
duoc skill co thuc su giup ich khong.

skops giai quyet bang 5 tru cot:

| Tru cot | Lam gi |
|---|---|
| **Authoring & Validation** | 24 lint rule (ma SKL100-SKL507), kiem tra cau truc, governance |
| **Evaluation Gate** | Test trigger, cham diem bang 3 agent (grader + comparator + analyzer), benchmark |
| **Skill Registry** | Registry dua tren Git (REGISTRY.yaml), CODEOWNERS, quan ly vong doi |
| **Distribution** | Dong bo cross-platform (symlink/junction/copy tuy OS), phat hien drift |
| **Observability** | Telemetry 2 tang (session + section), dashboard analytics, tim kiem |

Vong doi 1 skill duoc chuan hoa ro rang: `Draft → Review → Active → Deprecated → Archived`,
enforce boi rule SKL506, va skill deprecated bat buoc phai co migration path (SKL507) — dung
cai kho dang thieu (mo file cu khong ai biet co con dung duoc khong).

## Setup tung buoc
```bash
# Can Node.js >= 20.0.0
npm install -g skops

# Khoi tao project, chi dinh agent muc tieu
skops init --agent claude

# Dong bo skill tu registry ve project
skops sync

# Lint 1 skill theo 24 rule
skops validate path/to/skill

# Build ban phan phoi (compile stub + FTS5 search index)
skops build path/to/skill

# Tim full-text ben trong 1 skill
skops search my-skill "error handling"

# Xem bang drift detection - skill nao bi lech so voi registry
skops status

# Xem truoc sync se doi gi ma chua ap dung
skops diff --dry-run
```

## Vi du thuc te
Ap dung thang cho vu vua xu ly trong kho AI-Vibe-Toolkit — 266 skill trung tien to `ecc-`
kem bug double-frontmatter, phai tu viet script Python + Git Trees API de phat hien va dedup
tay:

1. Neu da co skops truoc do, lenh `skops validate` se bat ngay bug double-frontmatter (vi pham
   rule ve cau truc frontmatter chuan) tren toan bo 266 file **truoc khi** no tung duoc push
   len repo, khong phai phat hien sau khi da co 715 skill lung tung
2. `skops status` se hien bang drift ngay khi `ecc-X` va `X` co noi dung khac SHA nhau (dung
   nguyen logic Git Blobs API compare ma tao vua viet tay), khong can tu viet script rieng
3. Registry (REGISTRY.yaml + CODEOWNERS) se ngan viec import hang loat mot mega-repo skill roi
   vo tinh tao ra 2 ban ("da co trong registry" se bi flag ngay o buoc `skops publish`)
4. Vong doi Draft → Review → Active → Deprecated giup biet skill nao trong 500 skill hien tai
   (sau dedup con 449) la con dung duoc, khong phai doan mo tung file

## Luu y / Loi thuong gap
- **Rat moi**: 0 star, 0 fork, chua co release chinh thuc, chi 2 commit tren repo — day la du
  an vua bat dau, chua duoc cong dong kiem chung o quy mo lon
- Symlink tren Windows can quyen admin (junction fallback), neu VPS Nobitano chay Linux thi
  khong gap van de nay
- Telemetry hoan toan local (SQLite, khong gui di dau) — phu hop voi yeu cau bao mat cua kho,
  nhung cung co nghia khong co dashboard tap trung neu quan ly nhieu may/nhieu nguoi

## Danh gia ca nhan
- Diem manh: giai quyet dung 1-doi-1 van de kho AI-Vibe-Toolkit vua gap toan bo (dedup, drift,
  lifecycle, lint) — kien truc ro rang (core tach khoi CLI, 274 test/22 file), zero runtime
  server, dung SQLite+FTS5 cho search giong huong RIO Bot dang dung
- Diem yeu: qua moi de tin tuong ngay cho production — 0 star nghia la chua ai ngoai tac gia
  dung thu; 24 lint rule (SKL100-SKL507) chua co doc chi tiet tung rule o README, phai doc
  source de biet chinh xac
- Co nen dung khong: 7/10 tiem nang rat cao cho dung case cua kho, nhung nen **thu nghiem tren
  1 nhanh nho truoc** (vd chi vai chuc skill moi) thay vi ap dung ngay cho toan bo 449 skill,
  vi du an chua co release/tag on dinh de pin version

## Link
- Repo: https://github.com/Xerus-ai/skillops
- README (chua co docs site rieng): https://github.com/Xerus-ai/skillops/blob/master/README.md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# skops la Node CLI, khong co REST API — Hermes goi qua subprocess
import subprocess, json

def skops_status(project_path):
    result = subprocess.run(
        ["skops", "status", "--json"],
        cwd=project_path, capture_output=True, text=True
    )
    return json.loads(result.stdout) if result.stdout else None

def skops_validate(skill_path, project_path):
    result = subprocess.run(
        ["skops", "validate", skill_path],
        cwd=project_path, capture_output=True, text=True
    )
    return result.returncode == 0, result.stdout
```

### OpenClaw
```bash
# Cai 1 lan tren VPS (can Node.js >= 20)
npm install -g skops
cd /path/to/AI-Vibe-Toolkit
skops init --agent claude
skops sync
```

### Antigravity
```bash
# Chay dinh ky de bat drift trong kho skills/ (thay the script Python tu viet tay)
0 3 * * * cd /home/user/AI-Vibe-Toolkit && skops status --json >> /var/log/skops-status.log 2>&1
```
> ⚠️ Du an moi 0 star, chua co release/tag chinh thuc — nen pin bang commit hash cu the khi
> cai (`npm install -g github:Xerus-ai/skillops#<commit-sha>`) thay vi de npm keo ban moi nhat
> khong bao truoc, tranh breaking change bat ngo tren VPS production.

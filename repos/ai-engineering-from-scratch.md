---
name: ai-engineering-from-scratch
description: >
  Curriculum mien phi MIT license — 430+ bai hoc, 20 phase, day tu code lai
  backprop/tokenizer/attention/agent-loop bang tay truoc khi dung framework
  san. Co san skill cai thang vao Claude/Cursor/Codex/OpenClaw/Hermes qua
  `npx skills add`. Phase 14 (Agent Engineering, 42 bai) va Phase 11 (LLM
  Engineering) rat sat voi cong viec xay agent cua kho. 31K+ stars.
---

# ai-engineering-from-scratch — GitHub Repo

## TL;DR
Day khong phai 1 tool de cai, ma la 1 bo giao trinh AI Engineering mien phi, cuc chi tiet (430+ bai, 20 phase, 4 ngon ngu Python/TypeScript/Rust/Julia), theo trieu ly "Build It / Use It" — tu tay code lai thuat toan (backprop, tokenizer, attention, agent loop) roi moi chay qua thu vien production de hieu no khong con la hop den. Diem hay nhat cho kho: co san skill cai thang vao agent (Claude Code, Cursor, OpenClaw, Hermes...) de agent tu hoc/tra cuu khi can.

## Repo nay dung de lam gi
Van de ma tac gia neu ra: hoc AI kieu rai rac (1 bai paper, 1 bai fine-tune, 1 demo agent flashy) — cac manh khong khop nhau, biet lam chatbot nhung khong giai thich duoc loss curve, goi duoc function cho agent nhung khong biet attention lam gi ben trong model dang goi no.

Repo nay xau dung 1 duong xuong suot (spine) qua 20 phase:
- Phase 1-8: Toan nen tang → ML co ban → Deep learning core → Computer Vision → NLP → Speech/Audio → Transformer sau → Generative AI
- Phase 9: Reinforcement Learning (12 bai) — nen tang cua RLHF
- Phase 10: LLM tu dau (22 bai) — build, train, hieu LLM
- Phase 11: LLM Engineering (17 bai) — dua LLM vao production
- Phase 12: Multimodal AI (25 bai) — tu ViT patch den computer-use agent
- Phase 13: Tools & Protocols (23 bai) — giao dien giua AI va the gioi that (MCP va tuong tu)
- **Phase 14: Agent Engineering (42 bai)** — build agent tu nguyen ly: loop, memory, planning, framework, benchmark, production, workbench. 12 bai cuoi (31-42) la "workbench" — moi bai co file `mission.md` brief agent truoc khi no mo tai lieu day du, tuc la thiet ke de agent TU HOC duoc, khong chi nguoi
- Phase 15: Autonomous Systems (22 bai) — long-horizon agent, self-improvement, safety stack 2026

Diem dac biet: dung `npx skills add rohitg00/ai-engineering-from-scratch` la cai duoc toan bo (hoac tung skill/phase rieng) vao bat ky agent nao doc duoc SKILL.md — Claude Code, Cursor, Codex, **OpenClaw, Hermes** deu duoc goi ten rieng trong docs cua repo.

## Setup tung buoc
```bash
# Cach 1 — clone chay tay
git clone https://github.com/rohitg00/ai-engineering-from-scratch.git
cd ai-engineering-from-scratch
python phases/01-math-foundations/01-linear-algebra-intuition/code/vectors.py

# Cach 2 — cai thang vao agent (khuyen nghi cho kho)
npx skills add rohitg00/ai-engineering-from-scratch              # tat ca
npx skills add rohitg00/ai-engineering-from-scratch --skill agent-loop   # 1 skill
npx skills add rohitg00/ai-engineering-from-scratch --phase 14   # ca 1 phase
```
Sau khi cai, trong agent goi lenh `/find-your-level` — agent hoi 10 cau, tu chon phase phu hop va uoc luong thoi gian hoc.

## Vi du thuc te
Ap dung cho Nobitano khi dang build them agent packages (RIO Bot, sales-ceo, trum-san-bay):
1. Cai Phase 14 (Agent Engineering) vao Claude project nay bang `npx skills add rohitg00/ai-engineering-from-scratch --phase 14`
2. Khi thiet ke lai RIO Bot pipeline (dang la nut that trong kho — chua wire xong `rio_bot.py`), hoi Claude tham khao bai ve "memory" hoac "planning" trong Phase 14 de kiem tra pattern SQLite memory hien tai co dung best practice khong
3. Bai workbench (31-42) co san `mission.md` — co the dua thang cho Hermes doc va tu chay thu nghiem, khong can nguoi ngoi doc tai lieu truoc

## Luu y / Loi thuong gap
- Day la curriculum hoc, khong phai production tool — khong deploy duoc thang, chi dung de hoc/tham khao pattern
- 20 phase la khoi luong rat lon (430+ bai) — neu chi can 1 mang (vd Agent Engineering) thi dung flag `--phase` de khong keo het ve, tranh choan context/dia
- Repo cap nhat lien tuc (con dang them lesson, issue mo con nhieu) — noi dung co the doi giua cac lan cai

## Danh gia ca nhan
- Diem manh: cau truc "build tay truoc, dung thu vien sau" giup hieu sau thay vi chi biet goi API; tich hop san duoi dang skill cho agent la diem khac biet lon so voi khoa hoc thong thuong; Phase 14 rat sat nhu cau xay dung agent packages cua kho hien tai
- Diem yeu: mien phi va do 1 nguoi duy tri (rohitg00) — chat luong tung bai khong deu, phan cuoi (Phase 15+) moi va it duoc kiem chung thuc te; khong phai "cai la chay" nhu 1 tool, can thoi gian doc/hoc that su
- Co nen dung khong: 7/10 — dang cai truoc het la Phase 14 (Agent Engineering) va Phase 11 (LLM Engineering) vao project nay lam tai lieu tham khao khi thiet ke agent moi, khong can cai het 20 phase

## Link
- Repo: https://github.com/rohitg00/ai-engineering-from-scratch
- Site: https://aiengineeringfromscratch.com/
- AGENTS.md (huong dan cho AI agent dong gop): https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/AGENTS.md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Khong co API — day la noi dung tinh (markdown + code lesson), Hermes doc
# thang qua GitHub Contents API giong nhu doc file kho AI-Vibe-Toolkit
import urllib.request, json, base64

def fetch_lesson(path):
    url = f"https://api.github.com/repos/rohitg00/ai-engineering-from-scratch/contents/{path}"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github.v3+json"})
    data = json.loads(urllib.request.urlopen(req).read())
    return base64.b64decode(data['content']).decode()

# vd: fetch_lesson("phases/14-agent-engineering/31-agent-loop-workbench/mission.md")
```

### OpenClaw
```bash
# Cai skill Phase 14 (Agent Engineering) truc tiep vao thu muc skill cua OpenClaw
npx skills add rohitg00/ai-engineering-from-scratch --phase 14
```

### Antigravity
```bash
# Khong can deploy service — chi can clone/sync dinh ky de co ban lesson moi nhat
git clone https://github.com/rohitg00/ai-engineering-from-scratch.git /opt/curriculum
# Cron sync hang thang (repo cap nhat lien tuc)
0 3 1 * * cd /opt/curriculum && git pull >> /var/log/curriculum-sync.log 2>&1
```
> ⚠️ Day la tai lieu tham khao, khong phai executable service — dung de nap kien thuc/pattern cho Claude/Hermes khi thiet ke agent moi, khong wire vao pipeline production.

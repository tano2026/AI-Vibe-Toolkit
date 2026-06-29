# learn-harness-engineering — GitHub Repo

## TL;DR
Khoa hoc project-based day tu 0 den 1 ve Harness Engineering cho AI coding agent — 12 bai giang, 6 project, 14 ngon ngu (co tieng Viet). 9.3K stars. Tong hop tu tai lieu chinh thuc cua OpenAI va Anthropic. Skill `harness-creator` tu dong sinh production harness cho du an cua may trong vai phut.

## Repo nay dung de lam gi
Harness Engineering la ky thuat bien AI coding agent tu "lam gi thi lam" thanh "lam dung thu, dung cach, dung gioi han." Khoa hoc nay day:

**4 tru cot chinh:**
1. **Environment design:** Cach thiet ke moi truong cho agent hoat dong an toan
2. **State management:** Luu trang thai task de agent resume duoc khi bi interrupt
3. **Verification:** Agent tu verify output truoc khi bao xong — khong phai lam xong la done
4. **Control mechanisms:** AGENTS.md, TOOLS.md, HEARTBEAT.md — rang buoc agent trong rules ro rang

**12 bai giang:**
- L01: Harness fundamentals — tai sao can harness
- L02: AGENTS.md design — viet rules biet bien
- L03: TOOLS.md — khai bao tool chinh xac
- L04: Environment setup — init.sh, verification workflow
- L05: State persistence — JSONL, resume pattern
- L06: Verification loops — agent tu kiem tra output
- L07: Memory management — context compression
- L08: Multi-agent coordination — agent noi chuyyen voi nhau
- L09: Security boundaries — path rules, command deny list
- L10: Cost optimization — token budget, cache
- L11: Observability — logging, tracing, alerting
- L12: Production hardening — failure modes, recovery

**6 projects thuc hanh:**
- P01: Minimal harness cho Python project
- P02: Harness co memory va state
- P03: Multi-agent harness
- P04: Production harness voi monitoring
- P05: Tu dung harness cho du an cua may ← **Day la Ep5 trong video MRQ**
- P06: Harness cho team (multi-developer)

## Ap dung cho Hermes + OpenClaw

### Buoc 1 — Dung harness-creator skill sinh AGENTS.md cho Hermes

```bash
# Cai skill vao OpenClaw
clawhub install harness-creator
# hoac
openclaw skills install harness-creator

# Chay trong OpenClaw session
# "Use harness-creator to generate a production harness for Hermes"
# Feed: mo ta Hermes, cac tool no dung, gioi han can co
# Output: AGENTS.md + TOOLS.md + init.sh + verification workflow
```

### Buoc 2 — AGENTS.md chuan cho Hermes

```markdown
# AGENTS.md — Hermes Production Harness

## Identity
Hermes la Python executor agent trong he sinh thai Tano Agency.
Nhan lenh tu OpenClaw qua Telegram, thuc thi task Python, bao cao ket qua.

## Core Rules (khong bao gio vi pham)
- Khong xoa file ma khong co confirm tu Nobitano
- Khong push len GitHub neu chua replace token that bang [GITHUB_TOKEN]
- Khong chay lenh `rm -rf` bat ky dang nao
- Luon verify output truoc khi bao xong
- Luon log task_id, start_time, end_time, result vao TRACKER

## Verification Checklist (chay truoc khi bao "done")
- [ ] Code da chay thanh cong (khong co exception)
- [ ] Output dung dinh dang mong doi
- [ ] File da push thanh cong (neu co push)
- [ ] TRACKER.md da update (neu can)

## Tool Permissions
ALLOWED: urllib.request, json, base64, subprocess (whitelist), file read/write /home/hermes/
DENIED: rm -rf, sudo, curl voi --insecure, bat ky lenh xoa database

## Failure Protocol
Khi task that bai:
1. Log loi day du (error message + stack trace)
2. Retry toi da 3 lan voi exponential backoff
3. Sau 3 lan: bao OpenClaw + Nobitano qua Telegram
4. Khong tu y lam gi khac
```

### Buoc 3 — Verification loop cho Hermes

```python
# Them vao cuoi moi task trong Hermes
def verify_task_output(task_type, result):
    checks = {
        "github_push": lambda r: r.get("status") in (200, 201),
        "file_create":  lambda r: os.path.exists(r.get("path", "")),
        "tracker_update": lambda r: r.get("sha") is not None,
        "api_call":     lambda r: "error" not in str(r).lower()
    }
    check_fn = checks.get(task_type)
    if check_fn and not check_fn(result):
        raise ValueError(f"Verification failed for {task_type}: {result}")
    return True

# Dung nhu sau:
result = push_file("repos/new-tool.md", content, "add: new tool")
verify_task_output("github_push", {"status": 201})
# -> Hermes chi bao "done" khi verify pass
```

### Buoc 4 — State persistence (resume khi bi interrupt)

```python
import json, os

STATE_FILE = "/home/hermes/task_state.json"

def save_state(task_id, step, data):
    state = load_state() or {}
    state[task_id] = {"step": step, "data": data, "ts": time.time()}
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}

def resume_task(task_id):
    state = load_state()
    if task_id in state:
        print(f"Resuming task {task_id} from step {state[task_id]['step']}")
        return state[task_id]
    return None

# Dung trong batch task:
# save_state("batch_001", "step_3_of_10", {"done": ["file1.md", "file2.md"]})
# -> Neu Hermes crash o step 7, resume tu step 3 thay vi lam lai tu dau
```

## Setup tung buoc

```bash
# Doc khoa hoc (tieng Viet)
# https://walkinglabs.github.io/learn-harness-engineering/vi/

# Clone de co code mau
git clone https://github.com/walkinglabs/learn-harness-engineering
cd learn-harness-engineering

# Xem cac bai giang
ls docs/lectures/
# → lecture-01-* ... lecture-12-*

# Xem project P05 (tu dung harness cho du an cua may)
cat docs/projects/project-05-*/README.md

# Cai harness-creator skill
clawhub install harness-creator
```

## Luu y / Loi thuong gap
- Khoa hoc nang ve Python — Hermes dung Python nen ap dung truc tiep duoc
- AGENTS.md phai ngan gon (< 200 dong) — qua dai thi agent khong doc het
- Verification loop tang token tieu thu ~10-15% — chap nhan duoc voi do an toan co them
- State file can duoc backup — them vao Antigravity backup routine

## Danh gia ca nhan
- Diem manh: Tieng Viet co san; project-based hoc bang lam; harness-creator skill thiet thuc; tong hop tu OpenAI + Anthropic official docs; 9.3K stars = chat luong duoc kiem chung
- Diem yeu: Kien thuc kha sau, can thoi gian doc du 12 bai; mot so bai giang focus Python nhieu
- Co nen hoc khong: **9/10** — Day la kien thuc nen tang de Hermes va OpenClaw chay dung va tin cay hon. Doc P05 truoc, apply harness-creator, roi doc them bai giang khi gap van de cu the.

## Link
- Repo: https://github.com/walkinglabs/learn-harness-engineering
- Docs tieng Viet: https://walkinglabs.github.io/learn-harness-engineering/vi/
- harness-creator skill: trong repo /skills/harness-creator/
- License: MIT

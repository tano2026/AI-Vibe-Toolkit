---
name: jcode
description: >
  Coding agent harness viet bang Rust — terminal thay the cho Claude Code CLI
  voi side panel render mermaid diagram inline (1800x nhanh hon), info widget,
  multi-agent collaboration trong cung 1 repo (agent A sua file, agent B tu
  duoc bao). Render toi 1000fps, tu build terminal rieng (Handterm). 9.1K
  stars, 1.1K forks, dang trending manh.
---

# jcode — GitHub Repo

## TL;DR
jcode la 1 "coding agent harness" — tuc la lop giao dien + dieu phoi agent code, tuong tu Claude Code CLI nhung viet lai bang Rust cho toc do va them nhieu tinh nang UI ma terminal thuong khong lam duoc: side panel hien diagram/diff truc tiep, nhieu agent chay song song trong cung 1 repo va tu bao nhau khi dam file.

## Repo nay dung de lam gi
Van de: dung Claude Code/Codex qua terminal binh thuong thi khong co cho hien thi phu (diagram, diff, file preview) ma khong choan man hinh chinh, va khi chay 2+ agent trong cung 1 repo thi khong ai biet ai dang sua gi, de dam nhau.

jcode giai quyet:
- **Side panel** — bao agent load 1 file vao day de xem realtime, hoac dung lam diff viewer, khong ton dat man hinh chinh
- **Mermaid render inline** — tu build thu vien render Mermaid rieng bang Rust (`mermaid-rs-renderer`), nhanh hon mermaid-cli toi 500-1800 lan vi khong can browser/TypeScript
- **Info widget** — hien thong tin phu (trang thai, canh bao) chi khi can, tu bien mat khi khong co gi de hien
- **Multi-agent trong cung repo** — spawn 2+ agent, server tu quan ly: khi agent A sua file ma agent B da doc, agent B duoc bao ngay de kiem tra conflict thay vi ghi de mu quang
- **Terminal rieng (Handterm)** — tu viet terminal moi vi terminal chuan khong ho tro scroll muot, dang la WIP nhung da dung duoc
- Render toc do cao (>1000fps ve mat ky thuat, du man hinh thuong khong theo kip refresh rate do)

## Setup tung buoc
```bash
# Cai qua script chinh thuc (co binary Linux/macOS/Windows san)
# Xem huong dan cai dat tai README chinh thuc — repo build tu source bang Rust
git clone https://github.com/1jehuang/jcode.git
cd jcode
cargo build --release
```
Sau khi cai, dung lenh `jcode` trong bat ky repo nao de mo agent harness. Muon chay nhieu agent cung luc: mo them terminal/session tro vao cung thu muc repo, server cua jcode se tu dong quan ly va bao xung dot.

## Vi du thuc te
Ap dung cho case tao dang can — quan ly nhieu agent package trong `AI-Vibe-Toolkit` (`agents/trum-san-bay`, `agents/sales-ceo`, `agents/rio-bot`...):
1. Mo jcode trong repo kho, spawn 2 agent: 1 agent sua `agents/rio-bot/rio_bot.py`, 1 agent khac dong thoi update `agents/company/COORDINATION.md`
2. Neu agent thu 2 vo tinh doc file ma agent 1 dang sua, jcode bao ngay "file shifted under your feet" thay vi de agent 2 lam viec voi ban cu roi ghi de gay conflict
3. Side panel dung de xem live mermaid diagram kien truc trong khi agent dang code phan lien quan — khong can mo tab rieng

## Luu y / Loi thuong gap
- Terminal rieng (Handterm) con la work-in-progress — scroll partial-line chua muot bang terminal thuong, neu can on dinh thi dung terminal chuan (van chay duoc, chi mat 1 so tinh nang scroll)
- Day la tool moi, sinh thai plugin/skill chua lon bang Claude Code — neu team da quen workflow Claude Code/Cursor thi chi phi chuyen doi khong nho
- Multi-agent trong cung repo van can ky luat chia task ro rang — jcode chi canh bao conflict, khong tu giai quyet merge

## Danh gia ca nhan
- Diem manh: toc do render that su khac biet (Rust + custom Mermaid renderer), tinh nang multi-agent-aware la thu it tool khac lam tot, y tuong side panel/info widget thuc te huu ich khi lam viec voi nhieu agent song song
- Diem yeu: con moi, terminal rieng chua hoan thien, doc cua repo chu yeu la README dai chu chua co tai lieu chuan hoa nhu Claude Code
- Co nen dung khong: 6/10 — thu nghiem tot cho case chay nhieu agent song song trong 1 repo (dung voi mo hinh agent packages cua kho), nhung chua nen thay the OpenClaw/Hermes hien tai, chi nen dung song song de test

## Link
- Repo: https://github.com/1jehuang/jcode
- Releases: https://github.com/1jehuang/jcode/releases
- Lien quan: https://github.com/1jehuang/mermaid-rs-renderer (Mermaid renderer rieng)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# jcode la CLI/binary, khong co REST API — Hermes goi qua subprocess neu can
# trigger 1 agent session tu dong hoa (vd: chay batch review qua jcode)
import subprocess

def run_jcode_task(repo_path, prompt):
    result = subprocess.run(
        ["jcode", "--prompt", prompt],
        cwd=repo_path, capture_output=True, text=True, timeout=300
    )
    return result.stdout
```

### OpenClaw
```bash
# Build tu source tren VPS (can Rust toolchain)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
git clone https://github.com/1jehuang/jcode.git && cd jcode
cargo build --release
sudo cp target/release/jcode /usr/local/bin/
```

### Antigravity
```bash
# Neu muon chay jcode nhu 1 background service quan ly nhieu agent session
pm2 start /usr/local/bin/jcode --name jcode-agent -- --headless --repo /path/to/repo
```
> ⚠️ Terminal rieng (Handterm) hien la WIP — chay tren VPS qua SSH nen dung che do headless/non-interactive, khong nen phu thuoc tinh nang scroll custom.

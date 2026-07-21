---
name: agency-agents-app
description: >
  App native (Tauri 2 + Svelte 5) de browse/install/theo doi 232 agent persona
  tu repo agency-agents vao dung tool AI coding dang dung (Claude Code, Codex,
  Cursor, Gemini CLI, Copilot, Qwen, opencode) chi bang 1 click. Local-first,
  khong telemetry, tu phat hien khi file bi sua tay ben ngoai app. Companion
  app moi cua msitarzewski/agency-agents (repo goc da co trong kho).
---

# agency-agents-app — GitHub Repo

## TL;DR
`agency-agents` (repo goc, da co san trong kho) la 1 kho 232 agent persona chuyen biet chia
thanh 16 phong ban. Van de: moi coding tool (Claude Code, Cursor, Codex, Gemini CLI...) muon
persona duoi 1 dinh dang khac nhau, o 1 duong dan khac nhau, phai tu convert/copy tay.
`agency-agents-app` giai quyet dung van de nay - la 1 app native (khong phai web) de browse,
cai, va theo doi persona nao da cai vao tool nao, tu 1 giao dien duy nhat.

## Repo nay dung de lam gi
Day khong phai 1 skill/agent moi, ma la **lop cong cu quan ly** cho catalog agency-agents:

- **Agents workspace** - catalog 3 cot tim kiem duoc, loc theo phong ban/vai tro, xem chi tiet
  persona truoc khi cai
- **Install tracking** - ghi lai moi lan cai: source hash, rendered hash, tool dich, duong dan,
  scope (user hay project)
- **Reconciliation (tu phat hien drift)** - so sanh byte giua file da cai va source goc, phan
  loai: current / outdated / modified-ben-ngoai / da-xoa / foreign - biet ngay khi ai do sua
  tay file agent ma khong qua app
- **Tools panel** - tu detect tool nao dang co tren may, so luong da cai, version, bulk cai/xoa
- **Dashboard** - coverage, health, phan bo theo category x tool
- **Loadouts** - luu 1 nhom agent thanh "Agentfile" portable, restore lai sau
- **GitHub OAuth Device Flow** (tuy chon) - token luu trong keychain he dieu hanh, khong bao
  gio tra ve frontend

Render la Rust native, deterministic - khong shell ra script convert.sh cua repo goc luc
runtime, ma tu lam lai logic convert bang Rust va test khop byte-for-byte voi ban goc.

**Tool duoc ho tro cai truc tiep (deterministic, co san hom nay):**

| Tool | Scope | Output |
|---|---|---|
| Claude Code | user | `~/.claude/agents/*.md` |
| Codex | user | `~/.codex/agents/*.toml` |
| Gemini CLI | user | `~/.gemini/agents/*.md` |
| GitHub Copilot | user | `~/.github/agents/*.md` + `~/.copilot/agents/*.md` |
| Qwen Code | user | `~/.qwen/agents/*.md` |
| Cursor | project | `.cursor/rules/*.mdc` |
| opencode | project | `.opencode/agents/*.md` |

Antigravity, Aider, Windsurf, OpenClaw, Kimi co trong repo goc nhung CHUA duoc app nay ho tro
cai truc tiep (can them viec render rieng cho tung dinh dang).

## Setup tung buoc
```bash
# Cach 1 - tai ban build san (macOS/Linux/Windows)
# Vao https://github.com/msitarzewski/agency-agents-app/releases/latest

# Cach 2 - macOS qua Homebrew
brew tap msitarzewski/agency-agents
brew install --cask agency-agents

# Cach 3 - build tu source (can Rust + Node.js 22+)
git clone https://github.com/msitarzewski/agency-agents-app
cd agency-agents-app
npm install
npm run tauri dev
```

## Vi du thuc te
Ap dung cho case cua Nobitano - dang dung song song Claude Code (trong VS Code), OpenClaw,
va co the ca Codex/Cursor cho vai task:
1. Mo `agency-agents-app`, duyet catalog 232 persona theo 16 phong ban (Engineering, Marketing,
   QA...), chon vai persona hop voi kho AI-Vibe-Toolkit (vd persona "code reviewer", "frontend
   wizard")
2. Cai persona do vao Claude Code (`~/.claude/agents/`) bang 1 click thay vi tu chay script
   convert.sh cua repo goc roi copy tay
3. Vai tuan sau neu tu tay sua lai 1 file persona (vd chinh giong van cho hop voi ABTRIP), app
   tu phat hien "modified" trong Reconciliation view - biet ngay ban nao da lech khoi source,
   khong bi mat sua doi khi update lai catalog

## Luu y / Loi thuong gap
- Windows build **chua ky code (not code-signed)** - SmartScreen se canh bao, phai chon "More
  info → Run anyway" thu cong
- OpenClaw (agent orchestrator chinh cua Nobitano) **nam trong danh sach "chua ho tro cai truc
  tiep"** - repo goc co script convert cho OpenClaw nhung app nay chua build renderer rieng,
  can cho ban cap nhat sau hoac tu dung script convert.sh cua repo goc cho truong hop nay
  truoc mat
- App con moi (v0.1.0, phat hanh 16/06/2026), 24 stars, 0 fork - it nguoi dung thuc te kiem
  chung, co the con bug o cac edge case reconciliation

## Danh gia ca nhan
- Diem manh: giai quyet dung noi dau cua repo goc (moi tool 1 dinh dang khac nhau), kien truc
  security-first (khong `tauri-plugin-shell`, backup truoc khi ghi de, token trong keychain),
  tinh nang drift-detection la diem hiem co tool nao khac lam
- Diem yeu: rat moi, chua co OpenClaw support (quan trong voi setup cua Nobitano), it nguoi
  dung nen chua ro do on dinh dai han; chi la lop UI/quan ly, khong thay the duoc repo goc
- Co nen dung khong: 7/10 cho nguoi dung nhieu tool cung luc (Claude Code + Codex + Cursor),
  nhung neu chi dung Claude Code + OpenClaw nhu Nobitano thi loi ich chua ro rang bang - nen
  theo doi them vai ban update xem co them OpenClaw renderer hay khong truoc khi phu thuoc vao

## Link
- Repo: https://github.com/msitarzewski/agency-agents-app
- Repo goc (catalog persona): https://github.com/msitarzewski/agency-agents
- Releases: https://github.com/msitarzewski/agency-agents-app/releases

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# App la native GUI (Tauri), khong co REST API — Hermes khong goi truc tiep duoc
# Neu can tu dong hoa viec cai persona, dung thang script convert.sh cua repo goc
# (agency-agents) qua subprocess, bo qua lop UI cua app nay
import subprocess

def install_persona_via_upstream_script(agency_agents_repo_path, persona_name, target_tool):
    subprocess.run(
        ["bash", "scripts/convert.sh", "--agent", persona_name, "--tool", target_tool],
        cwd=agency_agents_repo_path, check=True
    )
```

### OpenClaw
```bash
# OpenClaw CHUA nam trong danh sach tool app nay ho tro cai truc tiep
# Dung tam script convert cua repo goc cho den khi app co renderer rieng cho OpenClaw
git clone https://github.com/msitarzewski/agency-agents ~/.agency-agents
cd ~/.agency-agents
bash scripts/convert.sh --tool openclaw --all
```

### Antigravity
```bash
# App co ban build san cho Linux (.deb/.rpm/.AppImage) — co the deploy tren VPS neu can
# giao dien quan ly agent tap trung, nhung binh thuong khong can chay tren server headless
# vi day la desktop GUI app, khong phai service
wget https://github.com/msitarzewski/agency-agents-app/releases/latest/download/agency-agents.AppImage
chmod +x agency-agents.AppImage
```
> ⚠️ Day la desktop app (Tauri), khong phai service chay nen — khong nen pm2-hoa tren VPS
> headless. Chi dung tren may co man hinh (macOS/Windows/Linux desktop) de quan ly persona
> roi push file da cai len kho/VPS thu cong.

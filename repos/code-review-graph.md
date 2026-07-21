---
name: code-review-graph
description: >
  Local-first code intelligence graph cho MCP va CLI — parse codebase bang
  Tree-sitter (23+ ngon ngu), build knowledge graph SQLite, cho AI coding tool
  chi doc dung phan can thay vi scan het repo. 6.8x giam token trung binh khi
  review, len toi 49x tren monorepo lon. Tich hop san Claude Code, Cursor,
  Codex, OpenClaw, Gemini CLI. 19K+ stars, dang trending manh.
---

# code-review-graph — GitHub Repo

## TL;DR
Repo nay giai quyet van de: AI coding tool (Claude Code, Cursor...) cu review/sua code la doc lai gan het file trong repo, ton token va cham. code-review-graph build 1 ban do cau truc code (function, class, import, call site, ke thua) bang Tree-sitter, luu vao SQLite local, roi expose qua MCP de agent chi doc dung phan can. Benchmark thuc te tren httpx, FastAPI, Next.js: giam trung binh 6.8x token khi review, len toi 49.1x tren monorepo lon.

## Repo nay dung de lam gi
Van de cot loi: 1 monorepo 2900 file, moi lan Claude Code muon hieu "sua ham nay anh huong gi" no phai grep/read hang chuc file, ton hang chuc nghin token, cham.

code-review-graph fix bang cach:
- Parse toan bo codebase 1 lan bang Tree-sitter (support Python, JS/TS, Go, Rust, Java, C/C++, C#, Ruby, Kotlin, Swift, PHP, va nhieu ngon ngu khac — 23+ ngon ngu)
- Luu thanh graph SQLite persistent, incremental (chi re-index phan thay doi, khong build lai tu dau)
- Expose qua MCP tools: `semantic_search_nodes_tool`, `query_graph_tool` (callers_of/callees_of/imports_of/tests_for), `get_impact_radius_tool`, `detect_changes_tool` + `get_review_context_tool` cho code review, `get_architecture_overview_tool` cho tong quan kien truc
- Auto-update qua hooks khi file thay doi

Ket qua thuc te: re-index 1 monorepo 2900 file duoi 2 giay. Mot benchmark cu the: loai 27,700+ file khoi review context, chi doc ~15 file thuc su lien quan.

## Setup tung buoc
```bash
pip install code-review-graph
# hoac: pipx install code-review-graph

# 1 lenh setup tat ca — tu detect AI coding tool dang cai, ghi MCP config dung
code-review-graph install

# Parse codebase
code-review-graph build
```
`install` tu detect Claude Code, Cursor, Codex, Windsurf, Zed, Continue, OpenCode, Gemini CLI, Qwen, Kiro, Qoder, GitHub Copilot — ghi dung file config MCP cho tung tool, cai hook/skill native neu tool support, va chen instruction vao rule file cua platform. Restart editor/tool sau khi cai.

## Vi du thuc te
Ap dung cho repo `AI-Vibe-Toolkit` (124+ repos, 88 skills, 167+ scripts cua kho tao):
1. Chay `code-review-graph build` lan dau — build graph cho toan bo file .md, .py trong kho
2. Khi sua 1 skill file, hoi Claude Code "skill nay dang duoc agent nao reference" → thay vi grep het thu muc `agents/`, Claude goi `query_graph_tool` voi target la file do, ra ngay danh sach callers/references trong vong <1s, ton ~100-800 token thay vi hang chuc nghin
3. CLAUDE.md cua repo (tu code-review-graph tao ra) day Claude uu tien graph tool truoc Grep/Glob/Read — tiet kiem token that su tren nhung task lap lai hang ngay nhu review PR

## Luu y / Loi thuong gap
- Generic YAML khong duoc coi la source code (khong parse) — neu kho dung nhieu YAML frontmatter cho skill, phan noi dung YAML se khong nam trong graph, chi phan code/markdown structure quanh no
- Version cu (truoc v2.2.3) can chay lai `code-review-graph install` de nhan schema hook moi — nang cap khong tu dong ap dung schema
- Estimate token savings la conservative character-count approximation, khong phai tokenize chinh xac — dung de tham khao xu huong, khong phai so tuyet doi

## Danh gia ca nhan
- Diem manh: setup 1 lenh, tu detect toan bo AI tool pho bien, benchmark co that (khong PR suong), incremental update nhanh, ho tro cuc nhieu ngon ngu
- Diem yeu: chi co gia tri ro voi codebase lon (monorepo, nhieu file) — voi repo nho vai chuc file thi loi ich khong dang ke so voi overhead cai dat; can them 1 buoc build lai khi doi cau truc lon
- Co nen dung khong: 8/10 — dang gia cai ngay cho kho AI-Vibe-Toolkit vi kho dang co 124+ repo/skill, se giup Hermes/OpenClaw doc code nhanh hon nhieu khi query kho

## Link
- Repo: https://github.com/tirth8205/code-review-graph
- Changelog: https://github.com/tirth8205/code-review-graph/blob/main/CHANGELOG.md
- Docs (CLAUDE.md hướng dẫn dùng): https://github.com/tirth8205/code-review-graph/blob/main/CLAUDE.md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# code-review-graph la CLI + MCP server, khong co REST API rieng
# Hermes goi qua subprocess vi day la tool local, khong phai API ngoai
import subprocess

def build_graph(repo_path):
    subprocess.run(["code-review-graph", "build"], cwd=repo_path, check=True)

def query_graph(repo_path, query_type, target):
    # vd: query_type="callers_of", target="ham_can_check"
    result = subprocess.run(
        ["code-review-graph", "query", query_type, target],
        cwd=repo_path, capture_output=True, text=True
    )
    return result.stdout
```

### OpenClaw
```bash
# Cai 1 lan tren VPS, tro vao thu muc repo kho
pip install code-review-graph --break-system-packages
cd /path/to/AI-Vibe-Toolkit
code-review-graph install   # tu detect OpenClaw neu co MCP config chuan
code-review-graph build
```

### Antigravity
```bash
# Deploy nhu 1 pip package tren VPS, khong can service rieng (chay on-demand)
pip install code-review-graph --break-system-packages
# Setup cron re-build graph moi dem sau khi kho co thay doi
0 2 * * * cd /home/user/AI-Vibe-Toolkit && code-review-graph build >> /var/log/crg-build.log 2>&1
```
> ⚠️ Graph luu SQLite local trong repo (`.code-review-graph/` hoac tuong tu) — nho add vao `.gitignore`, khong push graph binary len GitHub repo cong khai.

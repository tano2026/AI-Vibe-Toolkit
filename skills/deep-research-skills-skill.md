# deep-research — Research Ladder Dùng Ngay (L0→L5)

**Repo:** github.com/hint-shu/deep-research | MIT | v0.6.0
**Stack:** Firecrawl + Tavily + Exa + optional Codex CLI

---

## Setup

```bash
# Cài plugin
/plugin marketplace add hint-shu/deep-research

# API keys cần có (ít nhất 1)
export TAVILY_API_KEY="..."    # Recommended
export FIRECRAWL_API_KEY="..."
export EXA_API_KEY="..."
```

## Chọn Tier Đúng

```
Task                          → Tier    → Thời gian  → Token
─────────────────────────────────────────────────────────────
"Hermes agent là gì?"         → L0      → 10-60s     → ~500
"So sánh LangGraph vs CrewAI" → L1      → 2-5 phút  → ~2k
"State of AI agents 2026"     → L2      → 10-20 phút → ~8k
"Research cho blog post"      → L3      → 20-40 phút → ~20k
"Academic-grade report"       → L4      → 40-60 phút → ~40k
"Background check người/org"  → OSINT   → Tùy        → Tùy
```

## Commands

```bash
/research quick "fact cần check"
/research "topic thông thường"
/research deep "multi-angle analysis"
/research expert "50+ sources needed"
/research ultra "knowledge vault 120+ sources"
/research osint "entity name"
```

## Workflow Cho AI Vibe Toolkit

```bash
# Khi mày quẳng link tool mới
/research quick "tool X là gì"          # L0: 30s
→ Đủ info? → viết .md ngay

# Nếu cần sâu hơn
/research "tool X features install use cases"  # L1: 3 phút
→ Kết hợp với README fetch → viết .md đầy đủ

# So sánh tools
/research deep "tool X vs tool Y 2026"  # L2: 15 phút
→ Viết bài so sánh cho content
```

## Token Budget Rule

```
80% daily research tasks → L0 hoặc L1
15% deep analysis → L2
5% comprehensive reports → L3+

Đừng dùng L3+ cho tasks L0 đủ handle.
```

---
*skills/deep-research-skills-skill.md | AI Vibe Toolkit | tháng 6/2026*

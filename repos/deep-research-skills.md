# deep-research — Research Ladder L0→L5 Cho Claude Code

**GitHub:** https://github.com/hint-shu/deep-research
**Stars:** 2⭐ (mới) | **License:** MIT
**Tác giả:** hint-shu | **Version:** v0.6.0
**Stack:** Firecrawl + Tavily + Exa + optional Codex CLI

---

## Đây Là Gì

6 composable research skills tạo thành **research ladder** — mỗi tier build on top của tier trước, thêm capability.

Chọn đúng depth cho đúng task — không waste token cho task đơn giản, không thiếu depth cho task phức tạp.

---

## 6 Tiers — Chọn Đúng Depth

| Tier | Skill | Thời gian | Dùng khi |
|------|-------|-----------|---------|
| L0 | `quick-research` | 10-60 giây | Fact-check, quick lookup, đơn giản |
| L1 | `research` | 2-5 phút | Research cơ bản, 1 chủ đề rõ ràng |
| L2 | `deep-research` | 10-20 phút | Multi-angle, cross-source synthesis |
| L3 | `expert-research` | 20-40 phút | Academic-grade, 50+ sources |
| L4 | `ultra-research` | 40-60 phút | 120+ sources, knowledge vault |
| OSINT | `osint-research` | Tùy | Entity reconnaissance, người/tổ chức |

---

## Cài Đặt

```bash
# Claude Code
/plugin marketplace add hint-shu/deep-research

# Hoặc manual
git clone https://github.com/hint-shu/deep-research.git
# Copy skills/ vào .claude/skills/
```

## Setup MCP Tools (cần ít nhất 1)

```bash
# Tavily (recommended — structured output, tốt nhất cho research)
export TAVILY_API_KEY="..."

# Firecrawl (search + scrape + summary)
export FIRECRAWL_API_KEY="..."

# Exa (neural semantic search — tìm được cái khác miss)
export EXA_API_KEY="..."
```

---

## Dùng Ngay

```bash
# Quick fact check — 10 giây
/research quick "Claude Code version mới nhất?"

# Research cơ bản
/research "hermes agent architecture overview"

# Deep research — cross-source
/research deep "so sánh LangGraph vs CrewAI vs Hermes 2026"

# Expert research — 50+ sources
/research expert "AI agent memory management techniques"

# Ultra research — knowledge vault
/research ultra "state of AI coding agents 2026"

# OSINT
/research osint "Addy Osmani"
```

---

## Token Strategy Theo Tier

```
L0 quick:  1-2 searches, ~500 tokens
L1:        3-5 searches, ~2k tokens  
L2 deep:   10-15 searches, ~8k tokens
L3 expert: 25-30 searches, ~20k tokens
L4 ultra:  50+ searches, ~40k tokens
OSINT:     variable, entity-focused
```

**Rule:** Dùng tier thấp nhất đủ cho task. L0 cho 80% daily tasks.

---

## Đánh Giá Cá Nhân

2 stars nhưng design rất thoughtful — research ladder concept đúng hơn nhiều so với "search mọi thứ max depth". Tiết kiệm token đáng kể khi biết chọn tier phù hợp.

Stack Firecrawl + Tavily + Exa = 3 lớp redundancy — miss 1 cái thì cái khác cover.

**Rating: 8/10** — Highly recommend cho người cần research nhiều.

---
*Nguồn: github.com/hint-shu/deep-research | tháng 6/2026*

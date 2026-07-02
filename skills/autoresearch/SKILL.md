---
name: autoresearch
description: "Autonomous web research agent: deep-dive any topic, gather sources, synthesize findings. Từ ai-marketing-skills repo. Bổ trợ bởi last30days-skill cho research đa nền tảng."
allowed-tools:
  - Bash
  - Python
  - web_search
  - web_extract
user-invocable: true
---

# Auto Research — Deep-Dive Web Research Agent

Từ ai-marketing-skills repo. Dùng kèm **last30days-skill** để research đa nền tảng (Reddit, X, YT, HN, Polymarket).

## Usage
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/autoresearch/deep_research.py" --topic "AI Agents for marketing automation" --depth deep
```

## Research Levels
| Level | Sources | Depth | Time |
|-------|---------|-------|------|
| quick | 3-5 sources | Surface summary | ~30s |
| standard | 8-12 sources | Detailed analysis | ~2min |
| deep | 15-25 sources | Comprehensive report | ~5min |

## Complementary Tools
| Tool | Vị trí | Khi nào dùng |
|------|--------|-------------|
| **autoresearch** | Dùng `web_search` + `web_extract` | Task research tổng quát, multi-source |
| **last30days-skill** | Plugin Claude Code (npm) | Nền tảng cụ thể: Reddit trends, X feeds, YT comments, HN, Polymarket |
| **web-extraction** | Playwright bypass | Cần recent data từ 1-2 trang web |

**Chiến lược:** Nếu cần "xu hướng 30 ngày qua" → last30days-skill trước. Nếu cần "deep-dive chủ đề X" → autoresearch sau.

## Output Structure
1. Executive Summary
2. Key Findings (bulleted)
3. Source Analysis (per-source breakdown)
4. Contradictions & Nuances
5. Expert Opinions & Quotes
6. Statistics & Data Points
7. Further Reading

## Features
- Multi-source cross-validation
- Date-aware sourcing (prefers recent)
- Source credibility scoring
- Bias detection & flagging
- Citation-ready output

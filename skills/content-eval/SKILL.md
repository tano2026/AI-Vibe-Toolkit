---
name: content-eval
description: "Content evaluation framework: score content across quality dimensions, benchmark vs competitors, identify improvement opportunities."
allowed-tools:
  - Bash
  - Python
user-invocable: true
---

# Content Eval — Quality Scoring & Benchmarking

Từ ai-marketing-skills repo.

## Usage
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/content-eval/evaluate_content.py" --file content.md --type blog-post

# Compare multiple pieces
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/content-eval/evaluate_content.py" --files article1.md article2.md --type landing-page
```

## Scoring Dimensions
| Dimension | Weight | What It Measures |
|-----------|--------|-----------------|
| Relevance | 20% | Match to target audience + intent |
| Clarity | 15% | Readability + structure + scannability |
| Persuasiveness | 20% | Hook + social proof + CTA strength |
| Originality | 15% | Unique angle vs competitors |
| SEO | 15% | Keyword usage + headers + meta |
| Authority | 10% | Data sources + expert quotes + links |
| Actionability | 5% | Clear next steps for reader |

## Output
- Score per dimension (0-100) + overall
- Top 3 improvement suggestions
- Competitor benchmark (if URLs provided)
- Readability grade (Flesch-Kincaid)
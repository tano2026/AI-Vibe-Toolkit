---
name: deck-generator
description: "AI pitch deck generator: investor decks, sales decks, product launch decks. Slide structure + content + design suggestions."
allowed-tools:
  - Bash
  - Python
user-invocable: true
---

# Deck Generator — Pitch Deck & Sales Deck

Từ ai-marketing-skills repo.

## Usage
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/deck-generator/generate_deck.py" \
  --company "Your Company" \
  --tagline "Your tagline" \
  --problem "Problem description" \
  --solution "Solution description" \
  --market "TAM/SAM/SOM" \
  --traction "Key metrics" \
  --team "Team highlights" \
  --ask "Funding ask" \
  --type investor
```

## Deck Types
| Type | Slides | Tone |
|------|--------|------|
| investor | 10-12 slides | Vision + Traction + Ask |
| sales | 8-10 slides | Problem + Solution + ROI |
| product | 6-8 slides | Features + Demo + Roadmap |
| partner | 7-9 slides | Market + Win-Win + Terms |

## Output
- Slide-by-slide content in markdown
- Design suggestions (layout, colors, font)
- Speaker notes per slide
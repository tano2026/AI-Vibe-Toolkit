---
name: skill-creator
description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
category: development
---

# Skill Creator

A skill for creating new skills and iteratively improving them.

## Process Overview

1. **Capture Intent** — Understand what the skill should do, when it should trigger, and what output format is expected
2. **Interview & Research** — Proactively ask about edge cases, input/output formats, example files, success criteria, and dependencies
3. **Write the SKILL.md** — Fill in name, description, body instructions, and optional resources
4. **Create Test Cases** — Write test prompts that verify the skill works
5. **Run Evals** — Parallel runs (with and without the skill), compare outputs
6. **Review & Iterate** — Evaluate qualitative and quantitative results, rewrite based on feedback
7. **Optimize Description** — Run the description improver for better triggering accuracy

## Skill Structure

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
```

### SKILL.md Components

- **name**: Skill identifier (lowercase, hyphens)
- **description**: When to trigger, what it does. Include specific contexts AND triggering phrases. Make it slightly "pushy" to combat undertriggering.

### Skill Writing Guide

- Be specific about when to use and when NOT to use
- Include step-by-step instructions
- Add a Limitations section
- Reference bundled resources (templates, scripts) via relative paths
- Use YAML frontmatter for metadata

## Best Practices

- ✅ Interview the user to extract the workflow they want to capture
- ✅ Include both what the skill does AND when it should trigger
- ✅ Write test cases alongside the skill for verification
- ✅ Run baseline comparisons (with/without skill) to measure impact
- ❌ Don't skip the description optimization step
- ❌ Don't make descriptions too narrow — the skill won't trigger when needed

## When NOT to create a skill
- One-off tasks that won't be repeated
- Simple instructions that fit in a system prompt
- When the workflow is not well-defined enough

## Importing from External Repositories

When importing skills from a GitHub repo (e.g. a user's own skill collection, or community repos):

See `references/skills-import-from-repo.md` for the full workflow: clone → compare → classify → install local + VPS.

Key steps:
1. Clone with `--depth 1` for speed
2. Compare names to avoid duplicates
3. Classify as lightweight (text-only) vs heavy (needs install)
4. Lightweight: copy SKILL.md to Hermes skills dir
5. Heavy: install locally, keep reference only on VPS

## Limitations
- Skills can reference bundled files but cannot execute external code directly
- Skill descriptions are the primary triggering mechanism — invest time in getting them right
- Test this skill on diverse inputs to ensure it triggers at the right times

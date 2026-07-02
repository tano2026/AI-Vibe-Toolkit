---
name: blueprint
description: "Turn a one-line objective into a step-by-step construction plan any coding agent can execute cold. Each step has a self-contained context brief — a fresh agent in a new session can pick up any step without reading prior steps."
category: planning
---

# Blueprint — Construction Plan Generator

Turn a one-line objective into a step-by-step plan any coding agent can execute cold.

## When to Use This Skill

- Use when the task requires multiple PRs or sessions
- Use when multiple agents or team members need to share execution
- Use when you want adversarial review of the plan before execution
- Use when parallel step detection and dependency graphs matter

## How It Works

1. **Research** — Scans the codebase, reads project memory, runs pre-flight checks
2. **Design** — Breaks the objective into one-PR-sized steps, identifies parallelism, assigns model tiers
3. **Draft** — Generates the plan from a structured template with branch workflow rules, CI policy, and rollback strategies inline
4. **Review** — Delegates adversarial review to a strongest-model sub-agent (falls back to default model if unavailable)
5. **Register** — Saves the plan and updates project memory

## Best Practices

- ✅ Use for tasks requiring 3+ PRs or multiple sessions
- ✅ Let Blueprint auto-detect git/gh availability — it degrades gracefully
- ❌ Don't invoke for tasks completable in a single PR
- ❌ Don't invoke when the user says "just do it"

## Key Differentiators

- **Cold-start execution**: Every step has a self-contained context brief
- **Adversarial review gate**: Strongest-model review before execution
- **Zero runtime risk**: Pure markdown — no hooks, no scripts, no executable code
- **Plan mutation protocol**: Steps can be split, inserted, skipped with audit trail

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

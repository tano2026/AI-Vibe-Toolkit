---
name: production-code-audit
description: "Autonomously deep-scan entire codebase line-by-line, understand architecture and patterns, then systematically transform it to production-grade, corporate-level professional quality with optimizations"
category: code-quality
---

# Production Code Audit

Autonomously analyze the entire codebase to understand its architecture, patterns, and purpose, then systematically transform it into production-grade, corporate-level professional code.

## When to Use This Skill

- Use when user says "make this production-ready"
- Use when user says "audit my codebase"
- Use when user says "make this professional/corporate-level"
- Use when user says "optimize everything"
- Use when preparing for production deployment
- Use when code needs to meet corporate standards

## How It Works

### Multi-Agent Strategy

For deep audits, **delegate to a subagent** (like Goose) for the reading/analysis phase, then execute fixes yourself:
1. `delegate_task(goal="Audit codebase at path X", context="Scan every file, no changes")`
2. Receive the structured report from subagent
3. Prioritize fixes yourself — subagent only reports, does not modify
4. Execute fixes with proper syntax verification after each change

### Step 1: Autonomous Codebase Discovery
1. Read all files - Scan every file in the project recursively
2. Identify tech stack - Detect languages, frameworks, databases, tools
3. Understand architecture - Map out structure, patterns, dependencies
4. Identify purpose - Understand what the application does
5. Find entry points - Locate main files, routes, controllers
6. Map data flow - Understand how data moves through the system

### Step 2: Comprehensive Issue Detection

**Architecture Issues:** Circular dependencies, tight coupling, god classes, missing separation of concerns, poor module boundaries, violation of design patterns

**Security Vulnerabilities:** SQL injection, XSS, hardcoded secrets, missing auth, weak password hashing, missing input validation, CSRF, insecure dependencies

**Performance Problems:** N+1 queries, missing indexes, sync ops that should be async, missing caching, inefficient algorithms, large bundle sizes, unoptimized images, memory leaks

**Code Quality Issues:** High cyclomatic complexity, code duplication, magic numbers, poor naming, missing error handling, inconsistent formatting, dead code, TODO/FIXME comments

**Testing Gaps:** Missing tests for critical paths, low test coverage, no edge case testing, flaky tests, missing integration tests

**Production Readiness:** Missing env vars, no logging/monitoring, no error tracking, missing health checks, incomplete documentation, no CI/CD pipeline

### Common Production Security Findings (checklist)

These ship together in production backends — look for ALL of them:

| # | Finding | Severity | Fix |
|---|---------|----------|-----|
| 1 | `allow_origins=["*"]` with `allow_credentials=True` | 🔴 CRITICAL | Replace `["*"]` with explicit domains AND remove `allow_credentials=True` line. Fix: set `allow_origins=["https://yourdomain.com"]` and remove `allow_credentials=True` |
| 2 | Hardcoded API key fallback in source code | 🔴 CRITICAL | `os.getenv("KEY", "hardcoded_fallback")` — remove the fallback string entirely. Even if .env is missing, the key is leaked to anyone who reads the file. |
| 3 | MOCK/DEBUG mode enabled in production | 🟠 HIGH | Check .env files for `MOCK_*` or `DEBUG=True` flags. Must be `False` in production. |
| 4 | Hardcoded ABTRIP/API private keys in config.py | 🔴 CRITICAL | Same pattern as #2 — `os.getenv("KEY", "plaintext_fallback")` exposes keys in source |
| 5 | No authentication on API endpoints | 🔴 CRITICAL | All endpoints open — anyone can call the API, consume credits, access data |
| 6 | `nest_asyncio.apply()` + `loop.run_until_complete()` inside async | 🟠 HIGH | Known anti-pattern: blocks the entire event loop. Use `asyncio.run()` in sync contexts or make the caller async. |
| 7 | In-memory session store with no limits | 🟠 MEDIUM | `Dict[str, List]` grows without bound — no TTL, no size cap, lost on restart |
| 8 | Provider/API keys in config.yaml `provider_keys` section | 🔴 CRITICAL | Move to .env (or secret manager). Config files get shared, backed up, committed. |

**Fix pitfalls learned in production:**

- **CORS fix**: Removing `allow_origins=["*"]` while keeping `allow_credentials=True` causes FastAPI's middleware to error. Must remove BOTH `allow_origins=["*"]` AND `allow_credentials=True`, or replace with explicit origins WITHOUT credentials.
- **File corruption from iterative patching**: After 3+ patches to the same file, the file accumulates broken artifacts (`AUTH_TOKENS=*** in a Python source). At this point, stop patching and SCP a clean replacement instead. The threshold: if syntax check fails twice in a row on different lines, it's faster to rewrite the entire file.
- **AUTH_TOKENS=*** Python syntax error**: Writing `AUTH_TOKENS=*** directly in a Python file causes `SyntaxError: cannot assign to literal` because Python parses it as assigning to a string literal. This is NOT valid Python — it was created by a broken patch. Fix: find and delete the line, or restore from backup and re-apply patches one at a time with syntax verification after each.

### Step 3: Automatic Fixes and Optimizations

**IMPORTANT — Syntax verification pattern after each fix:**
```python
import py_compile
py_compile.compile("target.py", doraise=True)
```

Always backup before patching: `cp target.py target.py.bak`

**Common fix pitfalls:**
- **CORS fix**: Never just remove `allow_origins=["*"]` — FastAPI's middleware validator errors on `allow_credentials=True` without origins. Either remove both or replace with explicit domains.
- **Hardcoded key removal**: `text.replace('"hardcoded_fallback"', '')` — simple find-and-replace, then verify the resulting `os.getenv("KEY")` call has no trailing comma or syntax issues.
- **Mock mode switch**: Change both .env AND the default in config.py (where `os.getenv("MOCK", "True")` often has a built-in default)
- **File corruption from iterative patching**: After 3+ patches to the same file, the file accumulates broken artifacts (`AUTH_TOKENS=***` in a Python source). At this point, stop patching and SCP a clean replacement instead. The threshold: if syntax check fails twice in a row on different lines, it's faster to rewrite the entire file.
- **AUTH_TOKENS=*** is NOT valid Python syntax**: `AUTH_TOKENS=***` causes `SyntaxError: cannot assign to literal` because Python parses it as assigning to a string literal. This is created by a broken patch script. Fix: find and delete the line, or restore from backup and re-apply patches one at a time with syntax verification after each.

1. Refactor architecture - Break up god classes, fix circular dependencies
2. Fix security issues - Use parameterized queries, remove secrets, add validation
3. Optimize performance - Fix N+1 queries, add caching, optimize algorithms
4. Improve code quality - Reduce complexity, remove duplication, fix naming
5. Add missing tests - Write tests for untested critical paths
6. Add production infrastructure - Logging, monitoring, health checks

### Step 4: Verify and Report

Generate comprehensive report using this severity-sorted structure (proven effective in multi-instance audit):

```markdown
## 🔴 CRITICAL ISSUES
| # | Issue | Location | Severity |
|---|-------|----------|----------|
| CRIT-N | Title | path:line | P0/P1 |

Each entry: finding, exact location, risk assessment, specific fix.

## 🟠 MEDIUM ISSUES
Same format — includes code quality, missing tests, architecture concerns.

## 🟡 LOW ISSUES
Style, documentation, minor maintainability concerns.

## 🏗️ ARCHITECTURE OBSERVATIONS
High-level structural feedback (god functions, module boundaries, patterns).

## 🚀 PRODUCTION READINESS
Two tables: ❌ Missing and ✅ Present (health check, logging, auth, rate limiting, etc.)

## 📋 RECOMMENDATIONS (Sorted by Priority)
Immediate > Short-term > Medium-term > Long-term

## 📊 FILE-LEVEL SUMMARY
| File | Lines | Issues Found | Severity |
```

### Step 5: After reporting, fix in this order
1. 🔴 CRITICAL security issues first (keys, CORS, auth)
2. 🟠 MEDIUM reliability issues (mock mode, memory leaks, fragile parsing)
3. 🟡 LOW items last (comments, naming, docs)
4. For each fix: backup -> patch -> syntax verify -> commit

## Best Practices

### ✅ Do This
- Scan Everything - Read all files, understand entire codebase
- Fix Automatically - Don't just report, actually fix issues
- Prioritize Critical - Security and data loss issues first
- Measure Impact - Show before/after metrics
- Verify Changes - Run tests after making changes
- Be Comprehensive - Cover architecture, security, performance, testing

### ❌ Don't Do This
- Don't Ask Questions — Understand the codebase autonomously. This user (Nobitano) particularly hates being asked diagnostic questions. Try alternatives autonomously and deliver.
- Don't Report Only — Actually make the fixes
- Don't Skip Files - Scan every file in the project
- Don't Break Things - Verify tests pass after changes

## Related References

- `references/abtrip-backend-audit-2026-06-20.md` — Full audit report from Goose (6 critical, 8 medium, 6 low findings)
- `references/production-fix-sequence-2026-06-20.md` — Exact fix sequence applied to ABTRIP backend (MOCK, CORS, keys, auth)
- `references/patch-accumulation-threshold.md` — When to stop patching and rewrite instead (after 3+ failed syntax checks, the backup+full-rewrite is faster than iterative patching)

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Focus on critical/high priority issues when there are 200+ findings.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.

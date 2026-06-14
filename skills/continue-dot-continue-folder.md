# continue — .continue/ Folder Pattern: Rules, Agents & Prompts Gốc

**Nguồn:** github.com/continuedev/continue (33.7k⭐) | Apache 2.0
**Dùng cho:** CLAUDE.md / .cursorrules / .windsurfrules / Copilot instructions
**Cập nhật:** tháng 6/2026

> Files này là nội dung gốc từ `.continue/` folder của Continue repo.
> Copy paste vào AI coding assistant của mày — không cần cài Continue.

---

## Cách Dùng

1. Tạo folder `.continue/` trong root project
2. Copy từng file `.md` vào đúng subfolder
3. AI coding assistant sẽ tự đọc khi làm việc trong project

Hoặc: Copy thẳng content vào `CLAUDE.md` / `.cursorrules`

---

## 📁 RULES — Copy Vào `.continue/rules/`

### rules/overeager.md
```markdown
---
name: Breaking Change Detector
description: Fl
```

### rules/overeager.md
```markdown
---
name: Don't be overeager
---

Avoid over-eagerly adding new features. You should solve the problem at hand and then can propose further work.

```

### rules/personality.md
```markdown
---
name: Personality Rules
description: Conversational and personality guidelines
---

When the user challenges your output or asks a question, don't be overly-amiable (e.g. responding "You're right" all the time). Focus on correctness and be willing to tell the user they are wrong.

```

### rules/programming-principles.md
```markdown
---
name: Programming principles
description: Guidelines for coding fundamentals in this project
---

Use functional programming paradigms whenever possible. Modifying existing classes or creating singletons where needed is acceptable. but otherwise, use functions.

```

### rules/no-any-types.md
```markdown
---
globs: "**/*.{ts,tsx}"
---

Avoid using the `any` type wherever possible. Use unknown or find the correct type. The only acceptable place to use any is when typecasting for test mocks, and even then it's better to avoid and provide a proper mock.

```

### rules/unit-testing-rules.md
```markdown
---
name: Unit Testing Rules
description: Guidelines for unit testing in this project
alwaysApply: false
---

For unit testing in this project:

## 1. Testing frameworks

The project uses Vitest and Jest for testing. Prefer Vitest.

## 2. Test execution location

Run tests from within the specific package directory (e.g., `cd core && ..`).

## 3. Vitest tests

- Test files follow the pattern `*.vitest.ts`
- Run tests using `vitest` from within the specific package/module directory:
  ```bash
  cd [directory] && vitest -- [test file path]
  ```

## 4. Jest tests

- Test files follow the pattern `*.test.ts`
- Run tests using `npm test` from within the specific package/module directory:
  ```bash
  cd [directory] && npm test -- [test file path]
  ```
- The test script uses experimental VM modules via NODE_OPTIONS flag

## 5. Test structure

- Write tests as top-level `test()` functions - DO NOT use `describe()` blocks
- Include the function name being tested in the test description for clarity

```

### rules/pure-function-unit-tests.md
```markdown
Always create comprehensive unit tests for new pure functions. Tests should cover normal cases, edge cases, and boundary conditions.

```

### rules/documentation-standards.md
```markdown
---
globs: docs/\*_/_.{md,mdx}
description: This style guide should be used as a reference for maintaining consistency across all Continue documentation
alwaysApply: false
---

# Continue Documentation Style Guide

## Overview

## Writing Tone & Voice

### Conversational and Direct

- Follow Mintlify documentation standards
- Use simple, conversational language that gets straight to the point
- Avoid overly technical jargon when simpler terms work
- Write as if speaking directly to the developer using the tool
- Keep paragraphs concise and scannable

**Example:**
✅ "You send it a question, and it replies with an answer"
❌ "The system processes user queries and generates corresponding responses"

### Helpful and Instructional

- Focus on helping users accomplish their goals
- Use active voice and imperative mood for instructions
- Assume users want to get things done quickly
- Include relevant Admonition components for tips, warnings, and info

**Example:**
✅ "Press cmd/ctrl + L to begin a new session"
❌ "A new session can be initiated by pressing cmd/ctrl + L"

### Practical and Task-Oriented

- Emphasize what users can accomplish with each feature
- Lead with benefits and use cases before diving into mechanics
- Keep explanations grounded in real-world scenarios

## Content Structure

### Page Organization

1. **Visual Introduction**: Lead with GIFs or images showing the feature in action
2. **Purpose Statement**: Brief explanation of what the feature does and when to use it
3. **Step-by-Step Instructions**: Clear, actionable steps with keyboard shortcuts
4. **Platform-Specific Notes**: Separate sections for VS Code and JetBrains when needed
5. **Additional Tips**: Advanced usage or troubleshooting notes

### Section Headers

- Use consistent heading hierarchy starting with h2 (##)
- Include YAML frontmatter with title, description, and keywords
- Use action-oriented headers that describe what users will do
- Format: "Verb + object" (e.g., "Type a request and press enter")
- Keep headers concise but descriptive
- Use title case

**Examples:**
✅ "Highlight code and activate"
✅ "Accept or reject changes"
✅ "Switch between different models"

### Lists and Steps

- Use numbered lists for sequential steps
- Use bullet points for feature lists or options
- Keep list items parallel in structure
- Start action items with verbs

## Technical Writing Standards

### Code and Keyboard Shortcuts

- Use `backticks` for inline code elements
- Format keyboard shortcuts consistently: `cmd/ctrl + L`
- Always provide shortcuts for Mac/Windows/Linux
- Use code blocks for configuration examples with proper syntax highlighting

### Cross-References

- Link to related sections using descriptive anchor text
- Use relative links to other documentation pages
- Format: `[descriptive text](/path/to/page)`

### Platform Differences

- Always address both VS Code and JetBrains when applicable
- Use clear subheadings to separate platform-specific instructions
- Lead with the more common platform (typically VS Code) when both are covered

## Language Conventions

### Terminology

- **Consistent Terms**: Use the same terms throughout (e.g., "LLM" not "AI model" in some places)
- **Product Names**: Capitalize product names correctly (VS Code, JetBrains, Continue)
- **Feature Names**: Use consistent capitalization for Continue features (Chat, Edit, Agent, Autocomplete)

### Abbreviations

- Spell out acronyms on first use, then use abbreviation consistently
- Common abbreviations: LLM, IDE, API, URL

### Pronouns

- Use "you" to address the user directly
- Use "it" to refer to the tool/model
- Avoid "we" unless referring to the Continue team

```

### rules/llm-specificity.md
```markdown
---
globs: core/llm/llms/**/*.{ts,test.ts}
description: Tailor recommendations for LLM code based on which specific LLM is being used.
---

# LLM Model Specificity

- Refer to the file name and names of big classes to determine which LLM is being used in a file.
- Ground all observations and recommendations with knowledge of that LLM.
- Consider items such as context length, architecture, speed, and such.
- Pay attention to the parent classes in these files.

```

### rules/bigger-picture-description-rules.md
```markdown
---
name: Bigger Picture Description Rules
description: Guidelines for explaining how code works in context
alwaysApply: false
---

When a user asks how a certain part of the code works:

## 1. Describe what the code does in isolation

Explain the functionality of the code without considering its interactions with other parts of the codebase.

## 2. Describe interactions with other parts of the codebase

If the code interacts with other parts of the codebase, describe how the code is imported and used in other parts of the codebase.

## 3. Include parent function for clarity

When describing each use-case, include the parent function for clarity.

```

### rules/css-units.md
```markdown
---
globs: "gui/**/*.tsx"
---

You should try to use the `rem` CSS unit whenever possible for scalability instead of `px`.

```

### rules/colors.md
```markdown
---
name: Extension Color Themes
description: Guidelines for using theme colors in GUI components
alwaysApply: false
globs: "gui/**/*.tsx"
---

When adding colors to components, use tailwind color classes.
Do NOT use explicit colors like text-gray-400. Instead, use theme colors.

## Available theme colors

### Normal text

- `foreground`, `description`, `description-muted`

### Other text, icons, etc

- `success`, `warning`, `error`, `accent`, `link`

### General components

- `background`, `border`, `border-focus`

### Specific components

#### Button

- `primary`, `primary-foreground`, `primary-hover`
- `secondary`, `secondary-foreground`, `secondary-hover`

#### Input

- `input`, `input-foreground`, `input-border`, `input-placeholder`

#### Badge

- `badge`, `badge-foreground`

#### List/Dropdown items

- `list-hover`, `list-active`, `list-active-foreground`

#### Code Editor

- `editor`, `editor-foreground`

## Usage examples

Any of these colors can be used in tailwind classes:

- `bg-primary`
- `text-success`
- `border-error`
- `hover:bg-list-hover`

## Excluded colors

The following less-used colors are excluded from this guide:

- Command (only used by tip-tap): `command`, `command-foreground`, `command-border`, `command-border-focus`
- Find widget colors: `find-match`, `find-match-selected`
- `table-oddRow`

```

### rules/typescript-enum-usage.md
```markdown
---
globs: "**/*.{ts,tsx}"
alwaysApply: false
---

Use enums instead of simple string unions when possible in TypeScript code

```

### rules/github-pr-documentation-updater.md
```markdown
---
name: Update docs from GitHub PR
description: Provide a PR link to update docs based on
alwaysApply: false
---

When provided with a GitHub PR URL, use the GitHub CLI (`gh pr view <PR_URL> --json title,body,commits,files,additions,deletions,changedFiles`) to fetch comprehensive PR details including title, description, commits, changed files, and diff statistics. Analyze the PR content to identify what documentation in the `docs` folder needs to be updated, created, or modified. Update relevant documentation files to reflect the changes, new features, bug fixes, or improvements described in the PR. Ensure documentation changes are accurate, well-structured, and maintain consistency with existing docs formatting and style.

```

### rules/test-running-guide.md
```markdown
---
globs: ["gui/**/*", "core/**/*"]
description: Provides test running instructions for GUI and core folders
alwaysApply: false
---

When working with test files, use the following commands to run tests:

GUI folder tests:

- Run all tests: `cd gui && npm test`

Core folder tests:

- Run Jest tests: `cd core && npm test`
- Run Vitest tests: `cd core && npm run vitest`

Test file patterns:

- GUI: _.test.ts or_.test.tsx files use Vitest
- Core: _.test.ts files use Jest,_.vitest.ts files use Vitest

Best practices:

- We are transitioning to vitest, so use that when creating new tests

```

### rules/navigating-responses.md
```markdown
If the user's request is vague and you don't have enough information to confidently answer, you can either

- In Chat OR Agent mode, stop and ask questions to clarify before proceeding
- In Agent mode, use tools to discover more information, starting with the glob/grep tools if available.

```


---

## 🤖 AGENTS — Copy Vào `.continue/agents/`

### agents/breaking-change-detector.md
```markdown
---
name: Breaking Change Detector
description: Flag renamed commands, APIs, or config options with stale references
---

# Breaking Change Detector

Analyze this pull request for breaking changes that may leave stale references elsewhere in the codebase.

## What Constitutes a Breaking Change

1. **CLI command renames or removals** - If a command registered in `extensions/cli/src/commands/` is renamed, removed, or has its flags changed, check that:

   - Documentation in `docs/` reflects the new name
   - Agent definitions in `.continue/agents/` don't reference the old command
   - Skills in `skills/` are updated
   - README and CONTRIBUTING.md are current
   - GitHub Actions workflows don't invoke the old command

2. **Public API changes** - If exported functions, interfaces, or types in `core/` or `packages/` are renamed or have signature changes, check that:

   - All callers in `gui/`, `extensions/`, and `binary/` are updated
   - Type definitions in `packages/config-types/` are consistent

3. **Configuration schema changes** - If config file formats (YAML or JSON) are modified, check that:

   - Validation logic handles both old and new formats (or migration is provided)
   - Documentation examples use the new format
   - Default configs are updated

4. **URL changes** - If any hardcoded URLs (e.g., `hub.continue.dev`, `api.continue.dev`) are changed, scan for stale references across the repo.

## What to Do

- If you find stale references, fix them directly.
- If a breaking change has no migration path and could affect users, add a comment noting the concern but do not block.
- Focus only on changes introduced in this PR. Do not flag pre-existing issues.

## What NOT to Flag

- Internal refactors where all references are updated in the same PR
- Changes to test-only code
- Changes to development tooling that don't affect users

```

### agents/dependency-security-review.md
```markdown
---
name: Dependency Security Review
description: Review dependency changes for security implications and breaking changes
---

# Dependency Security Review

Review this pull request for changes to dependencies. A significant portion of PRs in this repo are automated dependency bumps (Dependabot, Snyk). This check ensures dependency changes get meaningful review.

## What to Check

### For Any `package.json` Changes

1. **New dependencies** - For each newly added dependency:

   - Is it well-maintained (not abandoned)?
   - Does it have known vulnerabilities?
   - Is it the right choice, or does an existing dependency already cover this use case?
   - Is the version pinned appropriately (exact vs range)?

2. **Major version bumps** - For major version upgrades:

   - Are there breaking changes that affect our usage?
   - Have the callers been updated to match the new API?

3. **Removed dependencies** - For each removed dependency:
   - Are all imports/requires of this dependency also removed?
   - Is there a replacement, or was the functionality dropped?

### For `package-lock.json` Changes

1. **Large lockfile diffs** (>500 lines changed) - Flag for human review, as they may indicate a transitive dependency shift that warrants attention.

2. **New transitive dependencies** - Check if the total dependency count increased significantly.

### Security-Specific Concerns

1. **Packages with filesystem/network access** - New dependencies that read/write files or make network requests deserve extra scrutiny since this tool runs locally on user machines.

2. **Native/binary dependencies** - New native modules (`node-gyp`, `.node` binaries) increase the attack surface and build complexity.

3. **Post-install scripts** - Dependencies with `postinstall` scripts can execute arbitrary code during `npm install`.

## What to Do

- If you find concerning dependency changes, add a comment explaining the concern.
- Do NOT modify `package.json` or `package-lock.json` files directly.
- If no dependency files were changed in this PR, do nothing.

```

### agents/error-message-quality.md
```markdown
---
name: Error Message Quality
description: Ensure error handling surfaces actionable messages to users
---

# Error Message Quality Check

Review this pull request for error handling quality. The most common user-facing issues in this codebase are generic "Unknown error" messages and swallowed error details that prevent users from diagnosing problems themselves.

## What to Check

1. **Catch blocks that discard error details** - Look for `catch` blocks that re-throw or return a generic message without including the original error's message, status code, or context.

2. **HTTP status codes without user-friendly mapping** - When making API calls (especially to LLM providers), ensure that common HTTP errors produce distinct, actionable messages:

   - `401` → "Invalid API key" (not "Unknown error")
   - `402` → "Insufficient funds or quota exceeded"
   - `403` → "Access denied - check your API key permissions"
   - `429` → "Rate limited - please wait and retry"
   - `5xx` → "Provider service error - try again later"

3. **Silent failures** - Look for empty catch blocks, caught errors that are only logged but not surfaced, or promise rejections that are swallowed.

4. **Error messages that lack context** - Error messages should include what operation failed and what the user can do about it, not just the raw error string.

## What NOT to Flag

- Internal error handling between modules where errors are properly propagated up
- Test files
- Debug/development-only error logging
- Errors that are intentionally caught and handled silently (with a clear code comment explaining why)

## Scope

Only review files changed in this PR. Do not audit the entire codebase. If you find issues, make targeted fixes to improve the error messages in the changed code. If no error handling issues exist in the changed files, do nothing.

```

### agents/input-validation.md
```markdown
---
name: Input Validation
description: Ensure user-facing inputs have proper validation and error feedback
---

# Input Validation Check

Review this pull request for input validation quality. The most common user issues in this codebase stem from malformed API keys, blank inputs, and missing configuration values that produce confusing downstream errors.

## What to Check

1. **API keys and secrets** - Any code that accepts API keys, tokens, or credentials should:

   - Reject obviously invalid values (empty strings, whitespace-only, placeholder text like "your-api-key-here")
   - Validate format where possible (e.g., OpenAI keys start with `sk-`, Anthropic keys start with `sk-ant-`)
   - Provide a clear error message before making a network request with a bad key

2. **Configuration values** - New or modified config parsing should:

   - Validate required fields are present and non-empty
   - Validate types (e.g., numbers are actually numbers, URLs are valid URLs)
   - Provide clear error messages that name the specific field and expected format
   - Not crash the entire config loading process for a single invalid value

3. **User text inputs** - New or modified UI inputs should:

   - Handle empty/whitespace-only submissions gracefully
   - Sanitize inputs that will be used in file paths, URLs, or shell commands
   - Not allow submission of invalid data that will fail silently later

4. **URL and endpoint validation** - When users provide custom URLs (e.g., for self-hosted LLM endpoints):
   - Validate URL format
   - Handle missing protocol (add `https://` if missing)
   - Provide feedback before attempting connection

## What NOT to Flag

- Internal function parameters (trust internal callers)
- Test inputs
- Validation that already exists and is working correctly
- Configuration values with sensible defaults that don't require user input

## Scope

Only review files changed in this PR. If you find missing validation, add it directly. Keep fixes minimal and focused. If no user-facing input handling was changed, do nothing.

```

### agents/test-coverage.md
```markdown
---
name: Test Coverage
description: Ensure new functionality includes corresponding tests
---

# Test Coverage Check

Review this pull request to determine if new functionality has adequate test coverage.

## When Tests Are Expected

1. **New exported functions or classes** - Any new public function, class, or module that is exported and used by other parts of the codebase should have at least basic unit tests covering:

   - The happy path (expected inputs produce expected outputs)
   - Edge cases (empty inputs, null/undefined, boundary values)
   - Error cases (invalid inputs throw or return appropriate errors)

2. **New CLI commands or subcommands** - Should have:

   - Smoke tests verifying the command registers and runs
   - Tests for flag parsing and validation
   - Tests for expected output format

3. **Bug fixes** - If a PR fixes a bug, there should be a regression test that:

   - Reproduces the original bug condition
   - Verifies the fix resolves it

4. **New API endpoints or handlers** - Should have integration tests covering:
   - Successful request/response
   - Error responses for invalid inputs
   - Authentication/authorization (if applicable)

## When Tests Are NOT Expected

- Documentation-only changes
- Configuration file changes (YAML, JSON, Markdown)
- CSS/styling changes
- Dependency updates (unless they change behavior)
- Agent definition files (`.continue/agents/*.md`)
- Refactors that don't change behavior (existing tests should still pass)
- Internal implementation changes fully covered by existing tests

## What to Do

- If new functionality lacks tests, add a PR comment noting what should be tested and why.
- Do NOT write tests yourself. The author knows the intended behavior best.
- If the PR includes tests but they seem incomplete (missing edge cases, no error cases), note the gaps.
- If the PR is clearly a test-exempt category (docs, config, styling), do nothing.

## Test Infrastructure Reference

- **Core**: Jest (`*.test.ts`) + Vitest (`*.vitest.ts`) in `core/`
- **GUI**: Vitest (`*.test.ts`) in `gui/src/`
- **CLI**: Vitest (`*.test.ts`, `*.e2e.test.ts`) in `extensions/cli/`
- **Packages**: Vitest in each `packages/*/` directory

```


---

## 💬 PROMPTS — Copy Vào `.continue/prompts/`

### prompts/core-unit-test.prompt
```markdown
name: Write Core Unit Test
description: Generate unit tests for core utilities
---
Write jest tests for the provided code.
Use jest version ^29 (e.g. jest 29.7.0)

Use best practices. Be clear and concise.
Aim for 100% code coverage where reasonable.
Multiple tests can be written, split up tests for best clarity and readability.
Only use typescript, and if the file/code is not typescript, warn the user.
IMPORTANT Use ESM to import modules, do NOT use `require` anywhere
Tests are to be described in an adjacent file with a path identical except for a `.test.ts` rather than a `.ts` file extension
Use double quotes (or backticks if needed) for strings

The code being tested is used in IDE extensions, and it:
- accesses code workspaces through the IDE ("workspace directories")
- persists extension-related data to the the local machine of the user ("global directory"), and
- uses configuration via a `ConfigHandler`, which is stored in the global directory

Jest testing setup includes
- @core/test/jest.global-setup.ts initializes a temporary global directory, which is where files that store persisted extension data live.
- @core/test/testDir.ts provides utils for creating and working with the temporary workspace directory. Use `setUpTestDir` and `tearDownTestDir` explicitly in tests that work with workspace files
- @core/test/jest.setup-after-env.ts gives tests access to node and jest globals

@core/test/fixtures.ts provides fixtures that should be used in tests to emulate extension behavior
- import `testIde` for IDE/workspace operations
- import `testConfigHandler` for any ConfigHandler needs
- import `ideSettingsPromise` for any IdeSettings needs
- import `testLLM` for any ILLM/BaseLLM needs. Set the `completion` property to the desired completion, e.g. `testLLM.completion = "Desired completion";`

Do NOT write tests for any files in `core/test`, only use them as helpers for testing other files. If no other files are provided, warn the user and write no tests.

IMPORTANT: Do NOT mock the fixtures above other than using `jest.spyOn`. DO mock 3rd party modules, etc. when sensible.
Instead, generate actual mock files and data for operations
Pure mocks should only be used to emulate specific network responses/error or hard-to-duplicate errors, or to prevent long-duration tests

Additional types can be imported from @core/index.d.ts. If any needed types, functions, constants, or classes are still not found, warn the user and do not generate tests.

Write the comment "// Generated by continue" at the top of the generated code/file (not the filepath)

```

### prompts/sub-agent-background.md
```markdown
---
name: Sub Agent Background Prompt
description: Start a subagent using the continue cli in the background
invokable: true
---

# Continue Sub Agent Background Prompt

Take the prompt provided by the user and using the terminal tool run the following command in the background:

cn -p "{{prompt}}"

```

### prompts/sub-agent-foreground.md
```markdown
---
name: Sub Agent Foreground Prompt
description: Start a subagent using the continue cli in the foreground
invokable: true
---

# Continue Sub Agent Foreground Prompt

Take the prompt provided by the user and using the terminal tool run the following command in the foreground:

cn -p "{{prompt}}"

```


---

*Nguồn: continuedev/continue | Apache 2.0*
*AI Vibe Toolkit | tháng 6/2026*

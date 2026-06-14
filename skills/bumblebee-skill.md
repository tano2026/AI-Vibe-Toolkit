# bumblebee (Perplexity) — Scan MCP An Toàn Trước Khi Cài

**Repo:** github.com/perplexityai/bumblebee | Apache 2.0 | Perplexity AI
**Dùng cho:** Security scan MCPs, extensions, packages trước khi cài

---

## Cài Nhanh

```bash
pip install bumblebee-scanner
# hoặc
npx bumblebee-scan
```

## Scan Trước Khi Cài Bất Kỳ MCP Nào

```bash
# Scan MCP package
bumblebee scan --package @modelcontextprotocol/server-brave-search

# Scan config file
bumblebee scan --config ~/.claude/claude_desktop_config.json

# Scan toàn bộ .claude folder
bumblebee scan --dir ~/.claude/

# Scan repo trước khi clone
bumblebee scan --repo https://github.com/user/some-mcp-server
```

## Output Ví Dụ

```
✅ SAFE: @modelcontextprotocol/server-brave-search
   - No malicious patterns found
   - Dependencies verified
   - Publisher: Anthropic (verified)

⚠️  WARNING: some-random-mcp
   - Unverified publisher
   - Requests excessive permissions: file system, network
   - Recommend: manual review before install

❌ DANGER: evil-mcp-server
   - Prompt injection patterns detected
   - Data exfiltration code found
   - DO NOT INSTALL
```

## Checklist Trước Khi Cài MCP

```
□ Chạy: bumblebee scan --package [name]
□ Check publisher (verified vs random)
□ Review permissions requested
□ Check stars + last commit date
□ Đọc source code nếu < 1k stars
```

## Rule Of Thumb

- **> 1k stars + verified publisher** → bumblebee scan → cài
- **< 100 stars + unknown publisher** → đọc source code trước
- **0 stars + mới tạo** → skip hoặc isolate trong sandbox

---
*skills/bumblebee-skill.md | AI Vibe Toolkit | tháng 6/2026*

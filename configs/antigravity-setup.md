# Antigravity — Setup Guide (Google Antigravity IDE)

> Viết lại 29/09/2026. Bản cũ mô tả Antigravity như một "package manager" chạy lệnh `agy install` / `agy plugin install` để cài Hermes, OpenClaw và plugin — phần đó chưa xác minh được nên đã gỡ, đừng chạy lại. Antigravity trong file này là **Google Antigravity** (antigravity.google), IDE agent-first của Google, chạy trên Windows của Nobitano.

---

## Antigravity làm gì trong hệ thống Tano

| Vai | Mô tả | Tần suất |
|-----|-------|----------|
| Hỗ trợ code nặng | Làm cùng DSH trên máy local (Windows 11), ví dụ portal TMC, dashboard, Remotion | Thường xuyên |
| Deploy VPS | Cài, deploy, restart service trên Tencent VPS theo `agents/ANTIGRAVITY-PLAYBOOK.md` | Thấp, theo milestone |

Hermes và OpenClaw KHÔNG chạy qua Antigravity. Chúng chỉ đọc kho.

---

## MCP khuyến nghị (Customizations > Installed MCP Servers)

| MCP | Quyết định | Lý do |
|-----|-----------|-------|
| github-mcp-server | Giữ | Đọc kho, đọc/ghi repo dự án. Dùng token fine-grained, chỉ cấp cho đúng repo dự án |
| filesystem | Giữ, khóa vào thư mục project | Sửa code, `.env`, docker-compose |
| gemini-api-docs | Giữ | Nhẹ, chỉ tra docs |
| chrome-devtools-mcp | Giữ | Debug console/network khi build giao diện |
| context7 | Thêm | Tra docs đúng phiên bản (xem `mcps/context7.md`) |
| sequential-thinking | Thêm | Chia task nhiều bước thành từng bước rõ (xem `mcps/sequential-thinking.md`) |
| claude-code | Tắt | Trùng DSH, hai agent code cùng lúc dễ đạp file nhau |
| genkit-mcp-server | Tắt | Không có project Genkit |
| composio | Tắt | Chưa authenticate, bật khi thật sự cần |
| lovable | Tắt | Nặng (~40 tools), không cần khi Antigravity tự dựng UI |

Thêm 2 MCP mới: bấm **Open MCP Config** rồi thêm vào `mcpServers`:

```json
"context7": {
  "command": "npx",
  "args": ["-y", "@upstash/context7-mcp"]
},
"sequential-thinking": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
}
```

---

## Skills và Rules — nằm ở đâu

| Loại | Global (mọi project) | Theo project |
|------|---------------------|--------------|
| Skills (thư mục có `SKILL.md`) | `~/.gemini/antigravity/skills/` | `<project>/.agent/skills/` |
| Rules | `~/.gemini/GEMINI.md` | `<project>/.agent/rules/` |

Nguyên tắc: bộ nào ép quy trình (Superpowers) thì cài **theo project**, không cài global.

---

## Cài Superpowers cho Antigravity

Superpowers bản gốc (obra/superpowers) hỗ trợ chính thức Claude Code, Codex, OpenCode — Antigravity chạy nhờ bản port cộng đồng. Dùng bản `bonnguyenitc/antigravity-superpowers` (MIT, còn nhỏ, chưa ai audit). Chi tiết ở `repos/superpowers.md`.

Cách cài an toàn (clone + copy, không chạy script lạ), PowerShell:

```powershell
git clone https://github.com/bonnguyenitc/antigravity-superpowers $env:TEMP\agy-sp
# ĐỌC trước: rules\superpowers.md và thư mục skills\
Get-Content $env:TEMP\agy-sp\.agent\rules\superpowers.md
Copy-Item -Recurse $env:TEMP\agy-sp\.agent <thư-mục-project>\.agent
```

Sau đó tạo `<project>\.agent\config.yml`:

```yaml
auto_commit: false
```

Vì sao `auto_commit: false`: mặc định bản port này để AI tự commit sau mỗi task. Antigravity và DSH làm chung repo thì phải tự tay kiểm soát commit.

Test: mở project trong Antigravity, gõ `/brainstorm thêm nút dark mode` — agent phải hỏi ngược lại chứ không nhảy vào code.

Lưu ý:
- Có cả `npx agy-superpowers@latest init` nhưng nó chạy code từ npm của tác giả lạ. Chỉ dùng nếu đã đọc package.
- Rule của nó `alwaysApply: true` nên tốn thêm token mỗi lượt. Task nhỏ (đổi tên, sửa typo) cứ hỏi thẳng, đừng `/brainstorm`.
- Đừng chạy `/update-superpowers` tự động: nó dùng AI viết lại rules. Muốn update thì tự đọc diff.

---

## Cài Karpathy guidelines (rule, không tốn tool)

1. Mở `skills/karpathy-coding-guidelines/SKILL.md` trong kho.
2. Copy nội dung (bỏ phần frontmatter) vào `<project>\.agent\rules\karpathy.md`.

---

## Phối hợp Antigravity với DSH trên cùng repo

- Mỗi agent một branch git riêng, hoặc chỉ một con "cầm bàn phím" tại một thời điểm.
- Antigravity push code được thì chỉ cấp token fine-grained cho repo dự án. Token có quyền vào kho `AI-Vibe-Toolkit` chỉ Claude giữ.
- Không bật MCP `claude-code` trong Antigravity.

---

## Deploy lên VPS

Antigravity dùng terminal `ssh` thẳng vào Tencent VPS, không cần MCP. Quy trình deploy, health check, báo endpoint cho Hermes: xem `agents/ANTIGRAVITY-PLAYBOOK.md`. Đọc kho bằng token read-only.

---

## Checklist sau khi setup

- [ ] MCP còn khoảng 75 tools (không còn lovable, claude-code, genkit, composio)
- [ ] `context7` xuất hiện trong Installed MCP Servers, có tool
- [ ] `.agent/` có trong project, đã đọc `rules/superpowers.md`
- [ ] `.agent/config.yml` có `auto_commit: false`
- [ ] `/brainstorm` làm agent hỏi ngược lại
- [ ] Không có token thật nằm trong file nào của `.agent/`

---

## Preset cài sẵn (v1, 29/09/2026)

Bộ luật + skill tra kho + workflow + DESIGN.md mẫu, cài bằng 1 script: xem `configs/antigravity-preset/README.md`. Chưa test thật trên máy Nobitano tại thời điểm viết.

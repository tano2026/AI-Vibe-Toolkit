# OpenWork (different-ai) — GitHub Repo

## TL;DR
"Bản mã nguồn mở thay thế Claude Cowork", chạy trên nền `opencode`. 18.8k sao, 1.9k fork — repo phổ biến nhất trong 3 project cùng tên "Openwork". Điểm khác biệt lớn nhất: không bắt buộc dùng desktop app riêng — expose qua **1 MCP server duy nhất** (`search_capabilities` + `execute_capability`) để add thẳng vào Claude Code, Cursor, Codex hoặc bất kỳ MCP client nào đang có sẵn.

## Repo này dùng để làm gì
Gom skill, MCP connection, và các dịch vụ đã kết nối (Google Workspace, Microsoft 365...) thành 1 lớp dùng chung, rồi cho phép truy cập lại từ bất kỳ agent nào hỗ trợ MCP — không cần cài lại từng nơi. Với team nhiều người, có thêm "OpenWork Den" — control plane quản lý ai được dùng model nào, publish skill/plugin qua marketplace nội bộ, và import được plugin tương thích Anthropic.

## Setup từng bước
1. Cách nhanh nhất — dán prompt cài đặt thẳng vào agent hiện có (Claude Code/Cursor/Codex):
   ```
   Install OpenWork on my computer, set up my first workspace, and open it ready to use.
   Follow the steps in https://openworklabs.com/start.md?v=hero
   ```
2. Hoặc add MCP thủ công — với Claude Code:
   ```bash
   claude mcp add --transport http openwork https://api.openworklabs.com/mcp/agent
   ```
3. Sau khi add, client sẽ mở trình duyệt để đăng nhập và chọn OpenWork organization.
4. Không bắt buộc cài desktop app — dùng được ngay từ agent hiện tại thông qua remote MCP URL: `https://api.openworklabs.com/mcp/agent`
5. Muốn quản lý team/tổ chức → dùng "OpenWork Den" để cấp quyền theo người/team, giới hạn model, và publish skill dùng chung.

## Ví dụ thực tế
Tạo 1 skill riêng (vd quy trình duyệt content cho Trùm Sân Bay) trong OpenWork Den, publish lên workspace nội bộ — sau đó bất kỳ máy nào trong team add MCP OpenWork vào Claude Code/Cursor là dùng lại được skill đó ngay, không phải copy file .md thủ công qua từng máy như cách kho AI-Vibe-Toolkit đang làm.

## Lưu ý / Lỗi thường gặp
- **Phụ thuộc dịch vụ ngoài (`api.openworklabs.com`)** — dù code mã nguồn mở, phần MCP relay + org control plane chạy qua cloud của họ, không phải tự host 100% trừ khi tự deploy lại từ source.
- **`search_capabilities`/`execute_capability` là lớp trừu tượng** — che giấu chi tiết tool thật bên dưới, tiện cho người dùng cuối nhưng khó debug sâu khi có lỗi vì không thấy trực tiếp tool nào đang chạy.
- Repo dùng monorepo lớn (`apps/`, `packages/`, `ee/` — bản Enterprise Edition riêng) — muốn tự host đầy đủ tính năng Den cần đọc kỹ phần `ee/`, không phải mọi thứ đều free/open.

## Đánh giá cá nhân
- **Điểm mạnh:** Không cần desktop app riêng là lợi thế lớn — dùng ngay từ Claude Code hiện có qua 1 dòng lệnh `claude mcp add`. Ý tưởng "1 MCP gom hết skill/connector, share lại cho cả team" giải quyết đúng vấn đề Tano đang gặp: kho AI-Vibe-Toolkit hiện đang là file .md tĩnh, Hermes/OpenClaw phải tự fetch GitHub mỗi lần — nếu có lớp MCP tương tự thì đỡ phải fetch lại.
- **Điểm yếu:** Core service quan trọng (Den, MCP relay) đi qua domain của bên thứ 3 — không hợp nếu Tano ưu tiên tự chủ hạ tầng hoàn toàn (giống nguyên tắc "claude-mem routing qua hhtechapi.com = security concern" đã ghi nhận trước đây). Cần đọc kỹ license phần `ee/` trước khi định tự host thay thế OmniRoute.
- **Có nên dùng không:** 6/10 — ý tưởng kiến trúc (MCP gom skill dùng chung toàn team) đáng học và có thể tự làm phiên bản riêng cho AI-Vibe-Toolkit, nhưng dùng thẳng sản phẩm của họ thì phụ thuộc hạ tầng ngoài, không khớp nguyên tắc tự chủ hiện tại.

## Link
- Repo: https://github.com/different-ai/openwork
- Docs/Demo: https://openworklabs.com/docs

---

## 🤖 Agent Integration

### Hermes (Python)
Không tích hợp trực tiếp — Hermes hiện dùng urllib thuần gọi GitHub API, không qua MCP. Nếu sau này Tano tự build lớp MCP tương tự cho kho AI-Vibe-Toolkit, đây là kiến trúc tham khảo tốt nhất (search_capabilities/execute_capability pattern).

### OpenClaw
```bash
# Nếu muốn thử nghiệm nhanh — add MCP OpenWork vào 1 agent client hỗ trợ MCP
# (không phải OpenClaw trực tiếp, cần agent trung gian hỗ trợ MCP protocol)
claude mcp add --transport http openwork https://api.openworklabs.com/mcp/agent
```

### Antigravity
```bash
# Tự host toàn bộ thay vì dùng api.openworklabs.com — cần build từ source
git clone https://github.com/different-ai/openwork
cd openwork && pnpm install && pnpm dev
# Lưu ý: phần "ee/" (Enterprise Edition) có license riêng, kiểm tra trước khi tự host production
```
> ⚠️ Nếu tích hợp, ưu tiên tự host thay vì phụ thuộc `api.openworklabs.com` —
> đúng nguyên tắc bảo mật Tano đang áp cho các dịch vụ trung gian khác (vd
> claude-mem qua hhtechapi.com đã bị flag là security concern trước đó).

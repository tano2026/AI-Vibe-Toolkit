# claude-code-templates (aitmpl.com) — GitHub Repo

## TL;DR
Thư viện "app store" cho Claude Code của `davila7`: 1000+ agent, command, skill, MCP, hook, settings, plugin xếp sẵn, cài bằng 1 lệnh `npx claude-code-templates@latest` hoặc chọn trên web aitmpl.com (có Stack Builder gộp nhiều thành phần). MIT, ~32K sao, release v1.29.6 (17/09/2026). **Cần Claude Code để dùng → hiện bị chặn vì Claude Code trên máy Windows chưa chạy được.**

## Repo này dùng để làm gì
Thay vì tự viết từng skill/agent/hook, mở web chọn thành phần cần (ví dụ: agent review code, command deploy, hook chặn lệnh nguy hiểm), copy lệnh cài về, nó ghi vào `.claude/` của dự án. Có thêm lệnh `/aitmpl` trong Claude Code.

## Số liệu đã kiểm (07/10/2026)
- `davila7/claude-code-templates`: MIT, ~32.422 sao, release mới nhất v1.29.6 (17/09/2026)
- Số trên web aitmpl.com: ~1,34 triệu lượt tải, ~239 nghìn lượt cài npm, 270 PR thành phần từ cộng đồng
- Những con số này lấy từ chính trang của dự án, tao chưa kiểm độc lập

## Setup
```bash
# Trong thư mục dự án (cần Node.js và Claude Code đã chạy được)
npx claude-code-templates@latest
# hoặc chọn thành phần trên https://aitmpl.com rồi chạy lệnh nó sinh ra
```

## Ví dụ thực tế
Cần 1 hook chặn lệnh nguy hiểm cho Hermes/Claude Code → so với `destructive-command-guardrail` đã có trong kho, vào aitmpl tìm hook cùng loại để đối chiếu cách viết, rồi VIẾT LẠI bản của mình theo luật kho, không cài nguyên xi.

## Lưu ý / Lỗi thường gặp
- **Thành phần do cộng đồng đóng góp** (270 PR) — không phải hàng đã duyệt bảo mật. Cài hook/command nguyên xi nghĩa là chạy code người lạ trên máy. Luôn đọc nội dung trước khi cài (đặc biệt hook và command có chạy shell)
- 1000+ thành phần = trùng lặp nhiều với kho đã có (590 skill, 57 mcp). Dùng để **tra và học cách viết**, không phải để nhân đôi kho
- Chưa chạy thử lần nào
- Điều kiện tiên quyết là Claude Code chạy được (xem OPERATING-MODEL.md)

## Ghi chú — SKILL.md là chuẩn mở? (chưa kiểm chứng)
Có nguồn nói định dạng `SKILL.md` đã thành chuẩn mở, đọc được bởi ~32 công cụ agent (kể cả Codex CLI, Gemini CLI). Tao CHƯA tự kiểm danh sách đó. Nếu đúng, skill viết theo `SKILL.md` trong kho dùng lại được ngoài Claude Code. Kiểm tra bằng cách: copy 1 skill ngắn sang `~/.gemini/` hoặc thư mục skill của Codex rồi gọi thử. Chưa có kết quả thì đừng hứa với team là "mọi agent đọc được".

## Đánh giá cá nhân
- Điểm mạnh: MIT, kho lớn, có Stack Builder, cài nhanh, cộng đồng sống
- Điểm yếu: chất lượng không đồng đều, rủi ro chuỗi cung ứng, bị chặn bởi Claude Code, trùng nhiều với kho
- Có nên dùng: 5/10 lúc này. Dùng làm thư viện tham khảo; chưa cài thật cho tới khi Claude Code chạy và có quy trình đọc-duyệt trước khi cài

## Link
- Repo: https://github.com/davila7/claude-code-templates
- Web: https://aitmpl.com
- Liên quan: `agents/infra-ops-agent/skills/destructive-command-guardrail`, `agents/company/skills/skill-lifecycle-management/SKILL.md`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Không dùng trực tiếp — công cụ này sinh file cho Claude Code.
# Hermes chỉ cần ĐỌC danh sách thành phần để tham khảo:
import urllib.request
html = urllib.request.urlopen("https://aitmpl.com", timeout=20).read().decode()
```

### OpenClaw
```bash
# Không áp dụng (thiết kế cho Claude Code).
```

### Antigravity
```bash
# Không áp dụng. Nếu thử với agy: chỉ copy SKILL.md thủ công, xem mục Ghi chú.
```
> ⚠️ Không cài nguyên xi thành phần cộng đồng chưa đọc.

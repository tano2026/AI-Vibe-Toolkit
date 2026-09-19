# Ponytail — Prompt Template / System Prompt

## TL;DR
Ruleset viral nhất GitHub gần đây (~44k star trong 9 ngày) — nhồi vào AI coding agent tính cách "ông senior lười biếng nhất công ty": hỏi cái date picker thì trả về đúng `<input type="date">` thay vì cài thêm library, viết wrapper component, thêm stylesheet. Bài toán giải quyết: AI code agent mặc định có xu hướng over-engineer, ponytail ép nó chọn giải pháp tối thiểu trước khi cho phép build thêm.

## Khi nào dùng
Bật cho mọi task code với agent (Claude Code, Codex, Cursor, Windsurf, OpenCode, Gemini CLI, GitHub Copilot CLI, Antigravity...) khi muốn agent tự hỏi "có cái gì có sẵn (native feature, thư viện chuẩn, code cũ trong repo) trước khi viết mới không" — đặc biệt hợp cho task nhỏ/vừa (form, validation, formatting) dễ bị agent "sáng tạo" quá tay.

## Nội dung skill / prompt
Nguồn thật nằm ở `skills/ponytail/SKILL.md` trong repo — đây là file gốc duy nhất, mọi bản copy cho Cursor/Windsurf/Copilot/Kiro... đều build lại từ file này (có script CI tự check nếu bản copy nào bị lệch). Cốt lõi là 1 "hierarchical decision ladder": ưu tiên native feature của platform > standard library > asset đã có trong codebase > mới viết code mới, và luôn giữ nguyên security/error handling/validation/accessibility — "lười nhưng không cẩu thả". Có 2 mode: mặc định và `ultra` (cực đoan hơn, dám thách lại cả yêu cầu, ưu tiên xoá code hơn thêm code).

## Setup từng bước
1. Claude Code / Codex / OpenCode / Gemini CLI / pi (host có hỗ trợ skill) — cài như 1 skill/plugin chuẩn, gọi bằng `/ponytail` hoặc `@ponytail-review` (Codex).
2. Cursor / Windsurf / Cline / GitHub Copilot Chat / Aider / Kiro / Zed / Qoder (chỉ đọc rule, không có command) — copy đúng file rule tương ứng từ repo vào:
   - Cursor: `.cursor/rules/`
   - Windsurf: `.windsurf/rules/`
   - Cline: `.clinerules/`
   - Copilot: `.github/copilot-instructions.md`
   - Kiro: `.kiro/steering/`
   - Qoder: `.qoder/rules/`
3. Antigravity / VS Code Codex extension — đọc thẳng `AGENTS.md` ở root repo, không cần setup gì thêm (repo đã ship sẵn file này).
4. Muốn dùng qua MCP cho host bất kỳ hỗ trợ MCP — cài `ponytail-mcp` (package riêng, expose ruleset vừa làm prompt vừa làm tool).
5. Muốn chặn subagent con không bị áp rule (vd giữ agent chỉ đọc/search khỏi bị ảnh hưởng) — set env `PONYTAIL_SUBAGENT_MATCHER` là 1 regex khớp với `agent_type` của subagent đó.

## Ví dụ thực tế
Trước: hỏi agent "làm cho tao 1 color picker" → agent tự cài thêm library, viết component riêng, ra ~287 dòng code.
Sau khi bật ponytail: agent nhận ra browser đã có `<input type="color">` sẵn, trả về ~23 dòng — comment kèm `<!-- ponytail: browser has one -->` để đánh dấu rõ đây là chỗ đã rút gọn, không giấu quyết định.

## Lưu ý / Lỗi thường gặp
- Số liệu "80-94% ít code hơn" trong bản benchmark đầu là **single-shot** (1 lần chấm), không phải baseline agent thật đang làm việc nhiều bước — bản sau đo lại trên agent thật (Claude Code chạy 12 ticket thật trên repo FastAPI+React) thì số đó là **mức trần cho từng task riêng lẻ**, không phải trung bình chung — đọc kỹ phần "Full writeup" trước khi lấy số liệu đi PR cho ai.
- Có rất nhiều fork/repo trùng tên xuất hiện chỉ trong vài ngày (UberGuidoZ, djpken, krissman, Adek06, dkfish...) — bản gốc/canonical là **DietrichGebert/ponytail**, ưu tiên theo dõi bản này để cập nhật.
- Đã có tranh luận trên Hacker News nghi ngờ "chỉ là 1 file prompt to đùng, có cần cả repo không" — đúng là bản chất chỉ là ruleset, không có gì huyền bí, giá trị nằm ở việc đã được test kỹ và đóng gói sẵn cho >10 agent khác nhau.
- Không có config file — muốn ép agent viết class phức tạp hơn mức cần thì vẫn viết được, chỉ là nó sẽ làm "chậm, đúng, và vừa làm vừa nhìn mày" (đùa của tác giả, nhưng thực tế là agent sẽ hỏi lại xác nhận trước khi over-build).

## Đánh giá cá nhân
- **Điểm mạnh:** Giải quyết đúng pain point rất thật của AI coding agent (thói quen cài thêm dependency/viết dư code cho việc đơn giản), hỗ trợ sẵn 10+ agent/editor khác nhau với 1 nguồn sự thật duy nhất (không phải ai tự chế lại), có benchmark đo trên agent thật chứ không chỉ nói mồm.
- **Điểm yếu:** Viral quá nhanh (44k star/9 ngày) kéo theo hàng loạt fork tên giống nhau gây rối khi tìm bản gốc, số liệu marketing (80-94%) dễ bị hiểu nhầm là trung bình trong khi là mức trần. Bản chất vẫn chỉ là ruleset/prompt, không có gì đảm bảo 100% agent tuân theo nếu người dùng cố tình ép.
- **Có nên dùng không:** 8/10 — đáng bật mặc định cho hầu hết coding agent đang dùng, đặc biệt nếu hay thấy agent "sáng tạo" quá tay cho task nhỏ. Cân nhắc kỹ trước khi bật `ultra` cho code quan trọng vì nó có xu hướng thách lại yêu cầu, có thể gây khó chịu nếu không quen.

## Link
- Nguồn gốc skill: https://github.com/dietrichgebert/ponytail
- Bài phân tích thêm: https://dev.to/yashddesai/ponytail-the-ai-coding-skill-taking-github-by-storm-and-the-one-question-nobodys-answered-yet-46mc

---

## 🤖 Agent Integration

### Hermes (Python)
Không có REST API riêng — bản chất là prompt/ruleset, không phải service gọi được. Nếu Hermes tự viết code, có thể tự nhồi nguyên văn nội dung `skills/ponytail/SKILL.md` vào system prompt của chính nó để có hiệu ứng tương tự.

### OpenClaw
```bash
# Nếu OpenClaw dùng OpenCode/Claude Code/Gemini CLI làm coding agent bên trong,
# cài như skill bình thường của host đó — thường chỉ cần copy file vào đúng thư mục rules
mkdir -p .agents/rules   # ví dụ với Antigravity-style, tuỳ host thật OpenClaw dùng
curl -fsSL https://raw.githubusercontent.com/dietrichgebert/ponytail/main/AGENTS.md -o AGENTS.md
```
> ⚠️ Kiểm tra đúng host coding agent OpenClaw đang chạy bên trong để copy đúng file rule tương ứng (Cursor/Windsurf/Copilot khác thư mục nhau).

### Antigravity
```bash
# Antigravity đọc thẳng AGENTS.md ở root — không cần setup gì thêm nếu copy file này vào repo
curl -fsSL https://raw.githubusercontent.com/dietrichgebert/ponytail/main/AGENTS.md -o AGENTS.md
```
> ⚠️ File `.agents/rules/` là cách để biến thành rule luôn bật (always-on) trong Antigravity, thay vì chỉ đọc 1 lần.

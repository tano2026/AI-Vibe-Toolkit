# stitch-skills (google-labs-code) — GitHub Repo

## TL;DR
Bộ skill chính thức của Google cho Stitch (tool AI vẽ UI của Google Labs) — gắn vào Claude Code/Cursor/Codex/Gemini CLI/Antigravity để agent tự sinh design, convert design sang React/React Native/shadcn, và lặp vòng feedback design-to-code. 6.5K stars, TypeScript, Apache-2.0.

## Repo này dùng để làm gì
Stitch là tool AI-powered design của Google Labs (như một dạng "Figma AI" — sinh UI từ text prompt, ảnh, hoặc sketch tay). `stitch-skills` là thư viện skill official gắn Stitch vào coding agent qua Stitch MCP server, đóng gói thành 3 plugin pack:
- **stitch-design** — plugin lõi: `code-to-design` (từ code hiện có sinh ngược lại design), `generate-design` (sinh screen mới từ data), `manage-design-system` (giữ nhất quán token design)
- **stitch-build** — convert design Stitch thành code thật: `react-components`, `react-native` (kèm StyleSheet + platform code), stack React+Vite với TanStack Query
- **stitch-utilities** — công cụ phụ: `enhance-prompt` (nâng cấp prompt UI mơ hồ thành prompt chuẩn Stitch), `design-md` (tạo file DESIGN.md từ ảnh/PDF/link tham khảo), `remotion` (sinh video walkthrough app từ design Stitch), `shadcn-ui`, `stitch-loop` (vòng lặp design→code→feedback→sửa design)

Nói ngắn: agent nhận 1 mô tả UI mơ hồ → dùng `enhance-prompt` làm rõ → `generate-design` sinh screen trong Stitch → `stitch-loop` duyệt qua vài vòng chỉnh sửa → `react-components`/`react-native` convert ra code production-ready, kèm `design-md` giữ token nhất quán xuyên suốt.

## Setup từng bước
1. Bắt buộc có tài khoản Stitch + Stitch MCP server đã cấu hình trước (xem `stitch.withgoogle.com`), skill không chạy được nếu thiếu MCP.
2. Cài trọn bộ plugin (khuyên dùng, nhanh nhất):
```bash
npx plugins add google-labs-code/stitch-skills --scope project --target claude-code
```
3. Hoặc cài lẻ từng skill cần dùng:
```bash
npx skills add google-labs-code/stitch-skills --skill design-md --global
npx skills add google-labs-code/stitch-skills --skill enhance-prompt --global
```
4. Với Codex: add repo làm plugin marketplace, source `https://github.com/google-labs-code/stitch-skills`, git ref `main`, sparse path `plugins/stitch-design` / `plugins/stitch-build` / `plugins/stitch-utilities` (không dùng `plugins/codex` — path này không tồn tại).
5. Trigger bằng câu lệnh tự nhiên, vd: `"Convert all screens in Stitch project projects/123 to React components."` hoặc `"Sync the app to the last updates of the Stitch project [ID]."`

## Ví dụ thực tế
Làm landing page mới cho ABTRIP (An Bình Airport Services): mô tả sơ "landing page Fast Track Nội Bài, tông Deep Navy + Hanoi Gold" → `enhance-prompt` bơm thêm vocab UI/UX chuẩn + design system context → `generate-design` sinh vài phương án screen trong Stitch → chọn 1 bản ưng, `design-md` xuất ra file DESIGN.md làm nguồn chân lý token màu/font → `react-components` convert thẳng sang component React kèm Tailwind, dev nhận code chạy được ngay thay vì phải đo lại pixel từ ảnh design.

## Lưu ý / Lỗi thường gặp
- Không có Stitch MCP server = skill vô dụng, đây là điều kiện tiên quyết chứ không phải optional.
- README nói rõ đây **không phải sản phẩm chính thức được Google support** (dù nằm dưới org `google-labs-code`) — dùng thận trọng cho việc thương mại, review kỹ code/design sinh ra trước khi merge/publish.
- Dữ liệu gửi qua Stitch MCP có thể gồm: source code frontend, HTML tĩnh, screenshot, ảnh, file design-system, project ID, prompt text, asset UI sinh ra — **không** upload thiết kế sản phẩm độc quyền, dữ liệu khách hàng, brand asset chưa công bố, hay credential nếu tổ chức chưa duyệt workflow này.
- Giữ credential Stitch, biến môi trường MCP, project ID tránh lộ trong prompt, issue công khai, screenshot, hay config đã commit.
- Skill `remotion` (sinh video walkthrough) chỉ là 1 phần nhỏ trong bộ, không mạnh bằng dùng Remotion/HyperFrames trực tiếp cho video sản xuất thật.

## Đánh giá cá nhân
- Điểm mạnh: bộ skill chính thức từ Google Labs nên chất lượng + maintenance ổn định (6.5K stars, push gần nhất cuối tháng 6/2026); pipeline design→code khép kín từ prompt mơ hồ tới component React thật, tiết kiệm hẳn bước "dev tự đo pixel"; tương thích rộng (Claude Code, Cursor, Codex, Gemini CLI, Antigravity).
- Điểm yếu: phụ thuộc hoàn toàn Stitch MCP + tài khoản Google Stitch, không dùng độc lập được; không phải sản phẩm Google chính thức support nên rủi ro về độ ổn định lâu dài vẫn có; cần cẩn trọng bảo mật vì gửi asset/design qua MCP bên thứ 3.
- Có nên dùng không: 7/10 — hợp nếu team đã/định dùng Stitch làm design tool chính (thay Figma/Penpot cho phần sinh UI nhanh bằng AI); không cần thiết nếu đã ổn định với luồng Figma/Penpot + `frontend-design`/`ui-component-forge` skill hiện có.

## Link
- Repo: https://github.com/google-labs-code/stitch-skills
- Stitch (Google Labs): https://stitch.withgoogle.com

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# stitch-skills là skill library gắn coding agent, không phải REST API độc lập.
# Hermes muốn dùng gián tiếp: gọi Stitch MCP server thẳng nếu cần list/sync project,
# nhưng cần bearer token Stitch — không hardcode, lấy từ env var qua pm2 ecosystem.
import urllib.request, json, os

def stitch_mcp_call(method, params):
    token = os.environ.get("STITCH_MCP_TOKEN")  # set qua pm2 set, không export shell
    req = urllib.request.Request(
        "https://mcp.stitch.withgoogle.com/rpc",  # kiểm tra endpoint thật trong docs Stitch MCP
        data=json.dumps({"method": method, "params": params}).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST")
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
# Cài trọn bộ plugin vào project trước khi giao task UI cho Claude Code
npx plugins add google-labs-code/stitch-skills --scope project --target claude-code
```

### Antigravity
```bash
# Antigravity nằm luôn trong danh sách agent hỗ trợ native — chỉ cần đảm bảo
# Stitch MCP server đã cấu hình env trên VPS trước khi Antigravity giao task design
npx plugins add google-labs-code/stitch-skills --scope project --target antigravity
```
> ⚠️ Bắt buộc set up Stitch MCP server (tài khoản Google Stitch) trước — không có bước này thì mọi lệnh trên đều fail. Đừng upload brand asset/data khách hàng chưa được duyệt qua MCP bên thứ 3 này.

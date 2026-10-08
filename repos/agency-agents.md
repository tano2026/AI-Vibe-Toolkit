---
name: agency-agents
description: >
  Kho ~280 "persona" agent chuyên biệt (kỹ thuật, marketing, bán hàng, thiết kế,
  tài chính...) theo nhóm phòng ban, có script cài sẵn cho 17 công cụ — gồm CẢ
  Hermes (plugin lazy-router), OpenClaw, DeepSeek Harness (dsh), Antigravity,
  Claude Code. MIT. Dùng làm thư viện tham khảo/mượn persona, KHÔNG thay Pro Agent của kho.
---

# agency-agents — GitHub Repo

## TL;DR
Thư viện ~280 prompt "chuyên gia" (mỗi file = 1 persona có vai trò, quy trình, tiêu chí đánh giá) chia theo nhóm: engineering (65), specialized (59), marketing (37), game-dev (21), gis (13), security (12), design (10), sales (9), testing (9), paid-media (7)... MIT. Điểm đáng giá nhất với Tano: **có sẵn script cài cho đúng bộ Trio** — `--tool hermes` (plugin định tuyến lười), `--tool openclaw`, `--tool dsh` (DeepSeek Harness), `--tool antigravity`, ngoài Claude Code/Cursor/Gemini CLI... **Nhưng đây là persona prompt, không phải "luật + kỷ luật" như 8 Pro Agent của kho. Dùng để MƯỢN và tra cứu, đừng cài hết.**

> Cập nhật 08/10/2026 từ repo thật (commit f99f6aa, 08/10): bản cũ ghi 232 agent/16 phòng/117K sao và thiếu hẳn đường cài cho Hermes + DeepSeek Harness. Số sao hiện tại tao chưa lấy được (lần cuối ghi: 117K, 29/06/2026).

## Số liệu đã đếm (08/10/2026)
- File persona có frontmatter `name:` trong các thư mục nhóm: **282** (README plugin Hermes ghi sinh ra **279** agent — lệch vì cách đếm; dùng "~280")
- License: MIT. Có app desktop riêng (`agency-agents-app`, xem `repos/agency-agents-app.md`)
- Mỗi persona là 1 file `.md`: frontmatter + vai trò + quy trình + deliverable + chỉ số thành công

## Cài cho từng thành viên của Trio
```bash
git clone https://github.com/msitarzewski/agency-agents && cd agency-agents
./scripts/install.sh --help          # đọc trước, xem các tuỳ chọn

# Hermes — KHUYÊN dùng cho Hermes: 1 plugin, 4 tool, kho nằm trên đĩa, nạp lười
./scripts/install.sh --tool hermes         # -> ~/.hermes/plugins/agency-agents-router
# Tool Hermes nhận được: agency_agents_search / _inspect / _load / _delegate

# OpenClaw — mỗi agent thành 1 workspace (SOUL.md, AGENTS.md, IDENTITY.md)
./scripts/convert.sh --tool openclaw && ./scripts/install.sh --tool openclaw
openclaw gateway restart

# DeepSeek Harness (dsh) — mỗi agent thành 1 skill tên agency-<slug>
./scripts/install.sh --tool dsh            # -> ~/.dsh/skills ; dùng: /agency-frontend-developer ...

# Antigravity — skill có tiền tố agency-
./scripts/install.sh --tool antigravity    # -> ~/.gemini/config/skills/

# Claude Code
./scripts/install.sh --tool claude-code    # -> ~/.claude/agents/
```
Chọn lọc thay vì cài hết: `--division marketing,design` hoặc `--agent <slug>` hoặc `--agents-file danh-sach.txt`. Có `--link` (symlink để cập nhật theo).

## Hermes: cách dùng đúng
Plugin KHÔNG nhét 279 skill vào Hermes. Hermes chỉ thấy 4 tool; muốn persona nào thì tìm → nạp:
```
Dùng plugin agency-agents-router. Tìm chuyên gia phù hợp, chỉ nạp/uỷ quyền đúng agent cần cho bước hiện tại.
Không preload cả roster và không thêm agency-agents vào skills.external_dirs.
```
Đây là cách duy nhất hợp lý với Hermes (tránh làm phình ngữ cảnh).

## Quan hệ với 8 Pro Agent của kho — KHÔNG thay thế
| | Pro Agent (kho) | agency-agents |
|---|---|---|
| Bản chất | Vai trò + luật + ranh giới tự chủ + guardrail + kiểm chứng | Persona prompt (giọng, quy trình, deliverable) |
| Mức tự chủ/guardrail | Có, ghi rõ | Không thống nhất, tuỳ tác giả đóng góp |
| Dùng khi | Việc thật của Tano Agency và khách (brand chỉ là ví dụ) | Cần "góc nhìn chuyên gia" nhanh cho 1 bước; mượn ý tưởng |
Cách dùng hợp lý: lấy persona đúng nghề làm "lớp giọng" bên dưới luật của kho (`EXPERT-CORE`), không để persona ghi đè luật.

## Ví dụ thực tế (brand chỉ để minh hoạ — thay bằng brand/khách đang làm)
- **ABTRIP:** Social Media Strategist + Offer & Lead Gen Strategist cho kế hoạch nội dung; Xiaohongshu Specialist để theo dõi xu hướng du lịch
- **Wonder Mart:** PPC Campaign Strategist, Paid Social Strategist, App Store Optimizer
- **Kênh nội dung (ví dụ Tano):** TikTok Strategist, Content Creator, Growth Hacker
- **Dev/Infra:** Backend Architect, DevOps Automator; **Security** có nhóm riêng (12) — hữu ích khi review Twenty/portal
Chuỗi 3 bước điển hình: Research (Xiaohongshu Specialist) → Strategy (TikTok Strategist) → Copy (Content Creator), mỗi bước một phiên/agent.

## Lưu ý / Lỗi thường gặp
- ~280 persona = quá nhiều, cài hết là rác ngữ cảnh. Chọn 10–15, hoặc dùng plugin lười của Hermes
- Chất lượng không đồng đều (nhiều người đóng góp); một số persona hướng thị trường Mỹ/Trung, cần chỉnh cho Việt Nam
- File persona chỉ là system prompt — chất lượng đầu ra vẫn phụ thuộc model
- Nguồn đóng góp cộng đồng: đọc nội dung persona trước khi cài vào agent có quyền chạy lệnh; repo có kiểm tra lint/originality nhưng không phải bảo đảm an toàn
- `install.sh` có lệnh `rm -rf` dọn thư mục đầu ra: dùng đích mặc định, **đọc `--help` và kiểm tra trước khi dùng `--path`**
- **Chưa cài thử lần nào**; mọi chi tiết trên từ README/integrations/script đọc ngày 08/10/2026

## Đánh giá cá nhân
- Điểm mạnh: MIT; **hỗ trợ trực tiếp Hermes, OpenClaw, DeepSeek Harness, Antigravity** — hiếm repo phủ đủ Trio; plugin lazy-router của Hermes thiết kế đúng; dễ chọn theo nhóm
- Điểm yếu: persona ≠ kỷ luật; chất lượng không đều; dễ biến thành "sưu tầm thêm" mà không dùng (đúng điểm yếu Nobitano đã tự nhận)
- Có nên dùng: **7/10** (bản cũ chấm 9,5 là quá tay). Làm 1 thử nghiệm nhỏ: cài plugin Hermes, gọi `agency_agents_search` với 1 nhu cầu thật của một brand/khách đang làm, ghi PASS/FAIL. Chưa PASS thì không cài thêm gì

## Link
- Repo: https://github.com/msitarzewski/agency-agents
- App: https://agencyagents.app (xem `repos/agency-agents-app.md`)
- Liên quan: `skills/agency-agents-skill/SKILL.md`, `agents/` (8 Pro Agent), `agents/company/skills/skill-lifecycle-management/SKILL.md`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Sau khi cài plugin (install.sh --tool hermes), Hermes gọi 4 tool có sẵn.
# Không cần code thêm. Luồng: search -> inspect/load -> delegate.
# Gợi ý lệnh giao việc cho Hermes:
#   "Dùng agency-agents-router: tìm chuyên gia 'paid social' rồi nạp đúng 1 agent cho bước này."
```

### OpenClaw
```bash
git clone https://github.com/msitarzewski/agency-agents && cd agency-agents
./scripts/convert.sh --tool openclaw && ./scripts/install.sh --tool openclaw && openclaw gateway restart
```

### Antigravity
```bash
./scripts/install.sh --tool antigravity     # skill tiền tố agency-, ở ~/.gemini/config/skills/
# DeepSeek Harness:
./scripts/install.sh --tool dsh
```
> ⚠️ Chưa chạy thử. Cài chọn lọc bằng --division/--agent, không cài cả bộ.

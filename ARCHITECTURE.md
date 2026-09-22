# ARCHITECTURE.md — Sơ đồ hệ thống AI Vibe Toolkit
> Cập nhật 22/08/2026 (bản trước ghi cứng "tháng 6/2026", số liệu lệch
> xa thực tế — 49 repos/34 MCPs/406 skills khi thật đã là 236/57/591).
> Agents đọc file này để hiểu mình đứng ở đâu trong hệ thống.

---

## Sơ đồ tổng quan (v2 — Vessel/Talent, xem COMPANY-CHARTER.md đầy đủ)

```
Nobitano (CEO — người duy nhất)
      |
      v
task-intake-quality-gate (vai "EA" — gác cổng chất lượng TRƯỚC dispatch)
      |
      |---------------|---------------|
      v               v               v
  VESSEL LAYER    VESSEL LAYER    VESSEL LAYER
 Hermes/OpenClaw/   Claude Code    Google Antigravity 2.0
 DeepSeek Harness                  (đã xác nhận SẢN PHẨM
 ("Team Thục Hán",                  THẬT của Google, không
  project OPC)                      phải tự đặt tên trùng)
      |
      v
  TALENT LAYER — 8 Pro Agent
  Research . Content . Sales . Marketing . Dev . Media . Designer .
  Customer Satisfaction
  = EXPERT-CORE.md (luật) + skill riêng
      |
      v
[AI-Vibe-Toolkit Repo] <- Claude (chat) ghi, mọi Vessel đọc
      |
      |---------------------------|
      v                           v
  /agents (playbooks + Pro Agent)  /mcps /repos /skills (591 skill,
  (biết phải làm gì)                đã dọn ecc/ trùng 271 file)
```

## Phân công

| Ai | Vai trò | Được phép |
|---|---|---|
| Claude (chat) | Viết & push kho, cố vấn | Ghi repo, KHÔNG thực thi VPS/local trực tiếp |
| Hermes | Thực thi task Python | Đọc kho, gọi API, research — chỉ urllib, không pip |
| OpenClaw | Orchestrator chính | Nhận lệnh, chạy EA gate, điều phối |
| DeepSeek Harness | Code phức tạp qua GitHub workflow | Còn breaking changes, dùng thận trọng |
| Antigravity | Hạ tầng (Google Antigravity 2.0) | Deploy, install, maintain VPS, cron/Scheduled Tasks, có pip/npm |
| Claude Code | Local Windows, làm việc file thật | Đọc/ghi/thực thi local, đã symlink skills/ từ kho |
| Nobitano | Ra lệnh & kiểm soát | Tất cả |

## Model routing

Vessel tự chọn model theo task — không còn cố định DeepSeek/Gemini như bản cũ:
- Google Antigravity 2.0 hỗ trợ đổi model: Gemini 3.1/3.5, Claude Sonnet 4.5, GPT-OSS
- Jev (TypeSafe) — lớp lọc quyết định nhanh (Choice/Score/Noul) đứng TRƯỚC các Vessel, còn early access/waitlist, có kiến trúc cascade riêng (xem repos/typesafe-jev.md)
- Claude (Anthropic) — cố vấn + viết kho, qua chat này

## Data layers

| Lớp | File | Nội dung | Thay đổi |
|---|---|---|---|
| Luật cứng | agents/company/EXPERT-CORE.md | Ngưỡng số 8 vai trò | Hiếm, cần research thật khi thêm |
| Đầu Não | agents/company/CORE-META-SKILLS.md | Harness/loop/superpowers — dùng chung mọi Vessel | Hiếm |
| Talent | agents/<8-pro-agent>/ | Spec + skill riêng từng agent | Khi cần |
| Instance | agents/trum-san-bay/ v.v. | Cá nhân hoá cho brand cụ thể, CHƯA audit chéo EXPERT-CORE | Thường xuyên |
| Tri thức chung | /mcps /repos /skills /content | Thư viện dùng chung | Liên tục |

## Luồng content factory (giữ nguyên, vẫn đúng)

```
Claude research + viết .md + script
      v
Push GitHub (kho được cập nhật)
      v
Vessel tương ứng fetch khi cần (qua Adapter riêng)
      v
Antigravity deploy -> Vessel chạy loop -> Content tự publish
```

## Trạng thái thật (22/08/2026, đếm trực tiếp qua GitHub API — không suy đoán)

- Kho: 236 repos / 57 MCPs / 591 skills (đã dọn ecc/ 271 file trùng)
- 8 Pro Agent hoàn chỉnh, đồng chuẩn (README+ARCHITECTURE+system-prompt+skills+HERMES-ADAPTER)
- Antigravity: xác nhận là Google Antigravity 2.0 thật, đã cài trên máy Nobitano
- Claude Code: đã symlink ~/.claude/skills -> kho, verify parse thành công phần lớn (30/591 file có lỗi frontmatter, chưa sửa hết)
- Jev: thiết kế cascade xong, chưa có API key thật (waitlist)

---

*AI Vibe Toolkit | ARCHITECTURE.md v2 | 22/08/2026*

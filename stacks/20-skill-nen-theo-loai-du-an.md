# 20 Skill Nền — Combo Skill theo Loại Dự Án (nâng cấp từ bundle 10)

## TL;DR
Nâng cấp từ `10-skill-bat-buoc-du-an-moi.md` — thêm 10 skill mới, và quan trọng hơn: **gắn tag
loại dự án cho từng skill**, để 1 dự án mới không phải nạp cả 20 mà chỉ tự lấy đúng nhóm cần.
Không còn "bundle cứng nạp hết" — thành **bộ lọc theo đặc điểm dự án**.

## Cơ chế tự chọn — đọc trước khi dùng bảng bên dưới

Mỗi dự án mới trả lời nhanh 6 câu hỏi (không cần hỏi CEO, tự suy từ brief/Domain Pack):

| Câu hỏi | Nếu CÓ → bật nhóm tag |
|---|---|
| Có sửa/viết code không? | `CODE` |
| Có giao diện người dùng thấy không? | `UI` |
| Có database/API/schema không? | `DATA` |
| Có nội dung/content/copy/video cho người đọc không? | `CONTENT` |
| Sắp deploy lên production thật (có user thật dùng)? | `DEPLOY` |
| Có research/tra cứu/fact cần đúng không? | `RESEARCH` |

`ALWAYS` luôn bật, không cần hỏi. Skill nào có tag khớp ít nhất 1 nhóm đã bật → nạp. Không khớp
tag nào đã bật → bỏ qua, không cần đọc.

## 20 skill — kèm tag để tự lọc

| # | Skill | File | Tag | Vai trò |
|---|---|---|---|---|
| 1 | Karpathy Coding Guidelines | `agents/KARPATHY-CODING-GUIDELINES.md` | `CODE` | Hành vi nền khi code |
| 2 | sanyuan-skills | `repos/sanyuan-skills.md` | `CODE` | Review SOLID/hiệu năng/edge case |
| 3 | Kiểm tra bảo mật trước deploy | `skills/kiem-tra-bao-mat-truoc-deploy.md` | `DEPLOY` | 7 lỗi toang ngầm |
| 4 | agent-browser | `repos/agent-browser.md` | `UI` | Tự verify bằng browser thật |
| 5 | supermemory | `repos/supermemory.md` | `ALWAYS` | Nhớ context xuyên session |
| 6 | Write a Skill | `skills/write-a-skill.md` | `ALWAYS` | Đóng gói quy trình verify ≥2-3 lần |
| 7 | Hand Off | `skills/handoff.md` | `ALWAYS` | Tóm tắt context khi chuyển giao |
| 8 | Hallmark / Huashu Design | `repos/hallmark.md` / `repos/huashu-design.md` | `UI` | Chặn UI "nhìn rõ AI làm" |
| 9 | Prompt Master + Grill Me | `skills/prompt-master.md` + `skills/grill-me.md` | `ALWAYS` | Làm sạch brief mơ hồ |
| 10 | awesome-claude-skills | `repos/awesome-claude-skills.md` | `ALWAYS` | Tra cứu trước khi tự viết skill mới |
| 11 | **Database Migrations** | `skills/database-migrations` | `DATA` | Đổi schema an toàn — rollback plan, không mất data |
| 12 | **Fact Checker** | `skills/fact-checker.md` | `RESEARCH` `CONTENT` | Verify trước khi tin — đúng bài học "sanyuan-skills tưởng giả hoá ra thật" |
| 13 | **Anti-AI-Tells** | `skills/anti-ai-tells.md` | `CONTENT` | Chặn văn phong "rõ AI viết" (khác Hallmark — đây là chữ, không phải UI) |
| 14 | **Personal Voice** | `skills/personal-voice.md` | `CONTENT` | Giữ giọng thương hiệu nhất quán qua nhiều bài |
| 15 | **Architecture Decision Records** | `skills/architecture-decision-records` | `ALWAYS` | Ghi quyết định kiến trúc kèm lý do — chính thức hoá `CHANGELOG-DECISIONS.md` |
| 16 | **API Design** | `skills/api-design` | `DATA` | Chuẩn REST/endpoint trước khi build, không phải sửa sau |
| 17 | **Production Code Audit** | `skills/production-code-audit.md` | `DEPLOY` | Audit rộng hơn checklist bảo mật — performance, observability, rollback |
| 18 | **Git Workflow** | `skills/git-workflow` | `CODE` | Kỷ luật branch/commit — tránh conflict, dễ revert |
| 19 | **Token Budget Advisor** | `skills/token-budget-advisor` | `ALWAYS` | Ý thức chi phí LLM — khớp triết lý OmniRoute routing rẻ/đắt theo việc |
| 20 | **Duplicate Checker** | `skills/duplicate-checker` | `ALWAYS` | Check trùng trước khi tạo mới — chính là Bước 1 trong `Quy_trình` đã có |

## Ví dụ tự lọc theo dự án thật

**Dự án 1 — "Form đặt Fast Track Nội Bài" (1 trong 9 job đang kẹt):**
```
Có code? CÓ → CODE bật. Có UI? CÓ (form) → UI bật. Có DB? CÓ (lưu đơn đặt) → DATA bật.
Sắp deploy thật? CÓ → DEPLOY bật. Content? KHÔNG. Research? KHÔNG.
→ Nạp: 1,2,3,4,5,6,7,8,9,10 (ALWAYS) + 11,16 (DATA) + 17,18 (CODE/DEPLOY thêm) = 16/20
→ KHÔNG cần: 12,13,14 (RESEARCH/CONTENT — form không viết content dài)
```

**Dự án 2 — "Script EP02 GMSP — Thiên Cơ" (job kẹt #1, role marketing):**
```
Có code? KHÔNG. Có UI? KHÔNG. Có DB? KHÔNG. Content? CÓ → CONTENT bật. Research? CÓ (tử vi
cần đúng dữ kiện) → RESEARCH bật. Deploy? KHÔNG.
→ Nạp: 5,6,7,9,10,15,19,20 (ALWAYS) + 12,13,14 (RESEARCH/CONTENT) = 11/20
→ KHÔNG cần: 1,2,3,4,8,11,16,17,18 (toàn bộ nhóm CODE/UI/DATA/DEPLOY)
```

Rút gọn rõ — dự án content không cần đọc 9 skill về code/deploy, dự án code không cần đọc 3
skill về content/research. Tự lọc đúng, không phải nạp hết 20 mỗi lần.

## Lưu ý / Lỗi thường gặp
- `ALWAYS` (8 skill: #5, 6, 7, 9, 10, 15, 19, 20) luôn nạp bất kể loại dự án — đây là phần
  không thương lượng, khác 10 skill bundle cũ vốn coi cả 10 là bắt buộc đều nhau.
- Tag không loại trừ lẫn nhau — 1 dự án có thể bật cả 6 nhóm cùng lúc (dự án lớn, đủ mọi mặt).
- 10 skill mới (#11-20) chưa được test thật trong pipeline Tano Agency như 3 phát hiện cũ
  (agent-browser, supermemory, sanyuan-skills) — nên áp thử trên 1-2 job trong 9 job đang kẹt
  trước khi coi là chính thức bắt buộc.

## Đánh giá cá nhân
- Điểm mạnh: giải đúng vấn đề bundle cũ tự nhận ("10 là nhiều, khó nhớ hết") bằng cách phân loại
  thay vì bắt nạp hết; 10 skill mới lấp đúng khoảng trống thật (DATA, ADR chính thức hoá, verify
  trước khi tin, giọng content nhất quán).
- Điểm yếu: cơ chế tự lọc dựa vào tự suy luận từ brief — nếu brief mơ hồ, phân loại sai nhóm có
  thể bỏ sót skill cần thiết. Nên kết hợp với skill #9 (Grill Me) làm rõ brief trước khi tự lọc.
- Có nên dùng không: 8.7/10 — thay thế hoàn toàn bundle 10 cũ, dùng bundle này làm chuẩn từ nay.

## Link
- Bundle cũ (10 skill, đã superseded bởi file này): `stacks/10-skill-bat-buoc-du-an-moi.md`
- 10 skill mới: xem cột File ở bảng trên, tất cả đã có sẵn trong kho, không cần research thêm

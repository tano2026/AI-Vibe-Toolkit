# Changelog Decisions — Nguồn quyết định chung (Hermes / OpenClaw / Claude)

> Ghi lại đây MỌI quyết định kiến trúc/thiết kế quan trọng, ngay khi chốt — để phiên làm việc
> khác (chat khác, agent khác) không phải tự dò lại từ đầu. Tham chiếu bởi `SENIOR-ADVISOR.md`,
> `HERMES-SOUL.md` (case 3, case 4). Append-only, không sửa/xoá entry cũ.

---

## 2026-07-28 — Phát hiện mâu thuẫn: OPENCLAW-WORKER-STRUCTURE.md vs UNIFIED-ARCHITECTURE.md

**Người phát hiện:** Claude (Senior Advisor), qua yêu cầu Nobitano tổng hợp lại các file mới.

**Mâu thuẫn:** 2 file cùng ngày 25/07/2026 mô tả 2 cấu trúc agent khác nhau:
- `UNIFIED-ARCHITECTURE.md` (dựa trên audit thật `agents/__init__.py`) — 9 agent THẬT đang chạy:
  `ceo, research, dev, sales, marketing, media, operations, support, analytics`. File tự ghi rõ
  "thắng" khi có xung đột. Khuyến nghị: KHÔNG build `hr-admin` riêng lúc này, gộp tạm vào
  `operations`.
- `OPENCLAW-WORKER-STRUCTURE.md` (viết sau, cùng ngày) — yêu cầu build 9 folder khác:
  `research, marketing, sales, content, dev, designer, media, ops-finance, hr-admin` — theo
  ORG-v2.md lý thuyết cũ, KHÔNG tham chiếu audit thật ở file kia.

**Đây đúng pattern "case 4" đã ghi trong `HERMES-SOUL.md`** — 2 lớp thiết kế đá nhau, viết cách
nhau vài giờ trong cùng 1 ngày, không phiên nào biết phiên kia.

**Việc liên quan trực tiếp:** Role ⑨ HR & Admin và ⑩ Legal & Compliance được thêm vào
`ORG-v2.md` ở 1 phiên chat khác (trước ngày 25/07) — theo audit thật trong
`UNIFIED-ARCHITECTURE.md`, agent-core KHÔNG có agent nào cho 2 role này. Legal & Compliance
chưa được nhắc tới ở bất kỳ file audit nào.

**Trạng thái:** CHƯA CHỐT — cần Nobitano quyết định 1 trong các hướng:
1. Theo `UNIFIED-ARCHITECTURE.md` (audit thật thắng) — bỏ build `hr-admin`/`content`/`designer`
   riêng, gộp theo đúng 9 agent thật; xem lại có cần giữ role ⑨/⑩ trong ORG-v2.md hay đổi thành
   "định hướng tương lai, chưa build" thay vì role đang hoạt động.
2. Theo `OPENCLAW-WORKER-STRUCTURE.md` (ORG-v2 lý thuyết thắng) — build đủ 9 folder tách biệt,
   chấp nhận lệch với agent-core thật đang chạy, cần đồng bộ code lại sau.
3. Hybrid — quyết định riêng từng điểm lệch (xem bảng "Đối chiếu" trong
   `UNIFIED-ARCHITECTURE.md`).

**Không tự chốt thay Nobitano** — đây là quyết định kiến trúc, đúng loại phải escalate theo
`SENIOR-ADVISOR.md` mục "Khi nào escalate", không phải việc Claude tự quyết rồi ghi đè.

**Việc khác phát hiện cùng lúc, cần xác nhận riêng:**
- Bảo mật: `.env` VPS lộ `ZALO_ACCESS_TOKEN` + `DEEPSEEK_API_KEY` plaintext — kế hoạch vá đã có
  (`SECURITY-WALL.md`), CHƯA xác nhận đã rotate 2 key này chưa.
- Hạ tầng: VPS đang down, IP `100.64.173.75` là dải CGNAT không phải IP public thật — chờ
  Nobitano reboot + xác định đúng IP public trước khi build OpenClaw mới.


---

## 2026-07-28 — QUYẾT ĐỊNH CHỐT: theo audit thật, không theo lý thuyết

**Người chốt:** Nobitano, sau khi Senior Advisor trình bày 2 phương án.

**Kết quả:** Theo hướng `UNIFIED-ARCHITECTURE.md` (audit thật) — giữ nguyên 9 agent thật đang
chạy trong agent-core, KHÔNG build agent thứ 10/11 cho HR&Admin/Legal&Compliance.

**Đã thực thi:**
1. `agents/company/ORG-v2.md` viết lại thành v3.0 — bảng 9 agent thật thay 10-role lý thuyết cũ.
2. `roles/hr-admin.md` v2.0 — đổi từ "Role Pack vị trí ⑨" thành "Extension pack nạp vào agent
   `operations`". Nội dung SOP/skill giữ nguyên 100%, chỉ đổi vai trò gọi.
3. `roles/legal-compliance.md` v2.0 — đổi từ "Role Pack vị trí ⑩" thành "Extension pack nạp
   vào agent `sales`". Nội dung giữ nguyên 100%, chỉ đổi vai trò gọi.
4. `OPENCLAW-WORKER-STRUCTURE.md` v2.0 — sửa lại đúng 8 folder worker (research, dev, sales,
   marketing, media, operations, support, analytics — không tính `ceo` vì đó là Hermes/bộ não,
   không phải OpenClaw worker), xoá `content/`, `designer/`, `ops-finance/`, `hr-admin/` riêng
   biệt khỏi kế hoạch build.

**Còn treo, CHƯA xử lý trong lượt này (cần theo dõi riêng):**
- Bảo mật: rotate `ZALO_ACCESS_TOKEN` + `DEEPSEEK_API_KEY` sau khi phát hiện lộ plaintext
  (xem `SECURITY-WALL.md`) — CHƯA xác nhận đã làm.
- Hạ tầng: VPS đang down, cần Nobitano tự reboot + xác định đúng IP public trước khi build
  OpenClaw mới theo cấu trúc 8 folder ở trên.
- `HERMES-PLAYBOOK.md` dòng 16 vẫn còn mô tả sai "Hermes chạy trong OpenClaw trên VPS" — cần
  sửa theo đúng `UNIFIED-ARCHITECTURE.md` (Hermes = agent-core, Local Windows) ở lượt sau.


---

## 2026-07-28 (tiep) — Da sua HERMES-PLAYBOOK.md theo dung audit that

Thuc thi viec con treo #3 tu entry truoc. Da sua HERMES-PLAYBOOK.md len v3.0:
1. Phan "May la Hermes" - sua tu "AI agent chay trong OpenClaw tren VPS" thanh dung
   "agent-core, runtime Python, Local Windows, la BO NAO khong phai worker".
2. Phan "Marketing/Content/Designer/Media Agent (4 vi tri)" - sua thanh "Marketing/Media (2
   agent that)", sua chieu delegate cho dung (Hermes dispatch -> OpenClaw thuc thi, khong phai
   nguoc lai).

Con treo (chua sua, uu tien thap hon bao mat + VPS): OPENCLAW-PLAYBOOK.md co the con vai cho
tham chieu kien truc cu, can ra soat lai lan sau.

**Kho: 145 repos | 40 MCPs | 99 skills | 202 scripts | 7 agent packages | 7 stacks | 9 agent that**

---

## 2026-08-01 — Đã cài claude-mem, CHỈ áp cho Claude Code sessions, KHÔNG áp cho runtime Hermes/OpenClaw

**Người quyết định:** Nobitano, sau khi Claude (Senior Advisor) research và giải thích phạm vi.

**Bối cảnh:** Nobitano cài `claude-mem` (thedotmack/claude-mem, plugin trong `skills/claude-mem.md`)
trên máy Windows local. Cài thành công — worker chạy tại `http://127.0.0.1:37777`, plugin dir
`C:\Users\Nguyen Ngoc Tan\.claude\plugins\marketplaces\thedotmack`, version 13.12.4.

**Quyết định chốt — phạm vi áp dụng:**
- claude-mem CHỈ hoạt động qua lifecycle hook của Claude Code (SessionStart, UserPromptSubmit,
  PostToolUse, Stop, SessionEnd) — 4 CLI được hỗ trợ chính thức: Claude Code, Gemini CLI,
  OpenCode, Codex.
- **Hermes** (Python executor thuần, tự gọi API qua `urllib.request`) và **OpenClaw** (Node.js
  orchestrator, PM2-managed, gọi LLM qua OmniRoute) KHÔNG chạy trong khung Claude Code, KHÔNG
  phát ra các lifecycle event trên → claude-mem KHÔNG cấp trí nhớ được cho runtime của 2 agent
  này.
- claude-mem giờ chỉ phục vụ session Claude Code của Nobitano khi code/debug trực tiếp trên máy
  Windows (nơi Hermes cũng chạy local) — ví dụ nhớ lại hôm qua đã sửa gì trong codebase Hermes/
  OpenClaw đang rebuild dở, không phải cấp bộ nhớ cho bản thân bot lúc chạy production.

**Tham khảo kiến trúc cho vấn đề khác:** claude-mem dùng cặp SQLite (session/observation/summary)
+ Chroma vector DB, cộng cơ chế search 3 lớp tăng dần chi tiết (index gọn → context xung quanh →
full detail) để tiết kiệm token. Đây đúng pattern có thể tham khảo để giải quyết việc còn treo
"RIO Bot chưa có vector store layer (chỉ có SQLite relational, thiếu semantic search)" — KHÔNG
phải cài claude-mem trực tiếp cho RIO Bot, mà tự build tương tự (SQLite + Chroma/sqlite-vec +
pattern search 3 lớp) trong runtime của Hermes.

**Việc treo:** chưa quyết định có build lại vector store layer cho RIO Bot theo pattern này hay
không — để dành, ưu tiên thấp hơn các việc bảo mật/VPS đang xử lý.


## 2026-08-05 — Chuẩn hóa path skill: folder/SKILL.md, bỏ flat .md

**Vấn đề:** 113 skill tồn tại song song 2 dạng — `skills/ten.md` (phẳng) và `skills/ten/SKILL.md` (folder).
Gây lỗi "skill not found" cho Hermes/OpenClaw khi loader không biết ưu tiên path nào (phát hiện qua cron
job ABTRIP Content Writer báo thiếu skill `ai-content-writing`, `content-ops` dù thực ra có trong kho).

**Quyết định:** Chuẩn path skill DUY NHẤT từ nay là `skills/<ten-skill>/SKILL.md` (folder format).
Đã xóa toàn bộ 113 bản `skills/<ten-skill>.md` phẳng trùng lặp, giữ bản folder làm canonical
(folder version có frontmatter chuẩn hơn cho agent — description tiếng Anh ngắn gọn + field category).

**Đã fix kèm:**
- TRACKER.md: sửa 69 reference path cũ -> path folder mới
- KHO-INDEX.md: sửa 13 reference path cũ -> path folder mới
- 3 file (`content-creator`, `fact-checker`, `token-efficient-research`) được kiểm tra thủ công
  trước khi xóa vì bản phẳng dài hơn đáng kể — xác nhận nội dung cốt lõi vẫn nguyên trong bản folder.

**Action cho Hermes/OpenClaw:** Khi load skill, LUÔN dùng path `skills/<ten>/SKILL.md`. Nếu 404,
báo lỗi rõ ràng thay vì fallback im lặng — không còn bản `.md` phẳng để fallback nữa.

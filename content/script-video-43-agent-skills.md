# Script Video #43 — agent-skills: Senior Engineer Của Google Distill 24 Skill Vào 1 Plugin

**Repo:** https://github.com/addyosmani/agent-skills
**Stars:** 59k⭐ | **Tác giả:** Addy Osmani — Google Chrome Lead
**Thời lượng:** 90-120 giây
**Hook angle:** "Đây không phải AI rules bình thường — đây là cách senior engineer Google làm việc, đóng gói thành 24 skill"

---

## 🎬 SCRIPT

---

**[HOOK — 0:00-0:08]**
*(Text on screen: "Addy Osmani — Google Chrome Engineering Lead — vừa public bộ skills cá nhân ông dùng hàng ngày")*

Addy Osmani.
Google Chrome Engineering Lead.
Tác giả Learning JavaScript Design Patterns.
15 năm làm ở Google.

Ông vừa public bộ skills cá nhân ông dùng hàng ngày.
59 nghìn người đã star trong vài tuần.

---

**[VẤN ĐỀ — 0:08-0:20]**
*(Screen: AI coding agent nhảy vào code không có plan)*

AI coding agent mặc định:
- Nhận task → code ngay
- Không viết spec
- Không có tests
- Deploy mà không có monitoring
- Ship rồi mới phát hiện bug

**Đây không phải cách senior engineer làm việc.**

---

**[GIẢI PHÁP — 0:20-0:38]**
*(Screen: Dev lifecycle diagram)*

agent-skills mã hóa **toàn bộ workflow senior engineer** thành 6 phase:

```
DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP
 /spec   /plan  /build   /test   /review  /ship
```

*(Screen: Cài plugin)*

```bash
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
```

---

**[7 COMMANDS — 0:38-0:58]**
*(Screen: Commands list)*

7 slash commands — mỗi cái activate đúng skills:

`/spec` — Viết spec TRƯỚC khi code. Không có spec = đoán mò.
`/plan` — Break task thành steps nhỏ, verifiable.
`/build` — Code từng slice. Test từng bước.
`/build auto` — *(highlight)* **Approve plan 1 lần → AI tự chạy hết.**
`/test` — Tests = proof it works. Không phải optional.
`/review` — 5 axes: correctness, readability, arch, security, perf.
`/ship` — Pre-launch checklist + rollback plan. Mọi deploy cần cái này.

---

**[AUTO SKILL ACTIVATION — 0:58-1:10]**
*(Screen: Code editing, skills auto-trigger)*

Điểm hay nhất:
**Skills tự kích hoạt theo context.**

Đang design API → `api-and-interface-design` bật lên tự động.
Đang build UI → `frontend-ui-engineering` bật lên.
Code có lỗi → `debugging-and-error-recovery` bật lên.

Không cần nhớ dùng skill nào.
AI tự biết.

---

**[24 SKILLS NHANH — 1:10-1:18]**
*(Screen: Scroll qua list skills)*

24 skills cover toàn bộ:
Define → Plan → Build → Verify → Review → Ship

Mỗi skill có: When to use, Process, Red Flags, Verification.
Không phải lý thuyết — là checklist thực tế.

---

**[CTA — 1:18-1:28]**
*(Screen: GitHub + 59k stars)*

MIT license. Free.
Link trong bio.

Cài xong → thử `/spec` với task tiếp theo của mày.
Khác hoàn toàn với cách mày đang làm.

*(Text on screen: "24 skills. 1 senior engineer. 15 năm Google.")*

---

## 📋 METADATA

**Hook chính:** "Google Chrome Lead vừa public bộ skills cá nhân — 59k người đã star"
**Hook phụ:** "AI coding agent của mày đang skip 5 bước quan trọng — đây là fix"

**Tags:** #claudecode #vibecoding #aivietnam #aitools #softwareengineering #google #opensource

**Thumbnail:**
- Portrait Addy Osmani (tìm ảnh public) hoặc Google Chrome logo
- Text: "24 SKILLS / GOOGLE ENGINEER"
- Sub: "addyosmani/agent-skills — 59k⭐"
- Màu: Chrome blue + white

**Cảnh quay:**
1. GitHub repo — stars, Addy Osmani profile
2. Lifecycle diagram: DEFINE→PLAN→BUILD→VERIFY→REVIEW→SHIP
3. Terminal: cài plugin 2 lệnh
4. `/spec` command → AI viết spec thay vì code ngay
5. `/build auto` → AI tự chạy hết sau approve plan
6. Skills auto-activate: đang code → skill tự hiện
7. Quick scroll 24 skills list

---
*Script by AI Vibe Toolkit | Video #43*

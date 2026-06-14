# Script Video #40 — Continue: Repo Đã Chết Nhưng Concept Này Thay Đổi Cách Mày Dùng AI Để Code

**Repo:** https://github.com/continuedev/continue
**Stars:** 33.7k⭐ | **Thời lượng:** 90-120 giây
**Hook angle:** "Repo 33k stars vừa chết — nhưng có 1 concept mày phải học từ nó"

---

## 🎬 SCRIPT

---

**[HOOK — 0:00-0:10]**
*(Text on screen: "33.000 stars. Vừa bị khai tử.")*

Repo này có 33 nghìn stars.
Được gọi là "pioneering open-source coding agent."
Và vừa bị khai tử tháng này.

Nhưng trước khi mày bỏ qua —
có **1 concept trong đây mày phải học.**

---

**[BỐI CẢNH — 0:10-0:22]**
*(Screen: GitHub repo, badge "read-only")*

Continue — coding agent ra từ 2023.
Trước cả Cursor, trước cả GitHub Copilot Workspace.

Tháng 6/2026: team thông báo repo read-only, không maintain nữa.
Final version: v2.0.0.

Nhưng 33k stars và 4.7k forks không biến mất.
Và concept cốt lõi của nó thì không chết.

---

**[CONCEPT CỐT LÕI — 0:22-0:50]**
*(Screen: Folder .continue/ trong VS Code)*

Concept đó là: **`.continue/` folder.**

Thay vì mỗi dev dùng AI theo cách riêng —
Continue cho mày lưu **AI rules của team** ngay trong source code.

*(Screen: Mở file rules/no-any-types.md)*

```
.continue/
├── rules/
│   ├── no-any-types.md        ← "AI không được dùng any trong TypeScript"
│   ├── unit-testing-rules.md  ← "Mọi function phải có unit test"
│   └── programming-principles.md
├── agents/
│   ├── breaking-change-detector.md
│   └── dependency-security-review.md
└── checks/                    ← Chạy trong CI pipeline
```

*(Screen: Git commit với .continue/ files)*

Commit lên Git cùng với code.
Team review rules như review code.
CI enforce tự động.

---

**[TẠI SAO QUAN TRỌNG — 0:50-1:05]**
*(Screen: So sánh 2 scenario)*

**Không có pattern này:**
- Dev A dùng Claude → code style X
- Dev B dùng Cursor → code style Y
- AI không biết conventions của team
- Review PR mất gấp đôi thời gian

**Có pattern này:**
- Mọi AI đều đọc cùng một rules file
- Rules trong Git → có thể review, track, rollback
- Checks trong CI → enforce tự động, không cần nhắc

---

**[APPLY VÀO 2026 — 1:05-1:18]**
*(Screen: Claude Code với .claude/ folder)*

Repo đã freeze — nhưng **pattern này mày áp dụng được ngay hôm nay.**

Với Claude Code: `.claude/` folder + `CLAUDE.md`
Với Cursor: `.cursorrules` file
Với bất kỳ AI nào: lưu rules trong repo, commit cùng code

Continue là người đi tiên phong cái này từ 2023.
Bây giờ mọi tool lớn đều follow pattern đó.

---

**[CTA — 1:18-1:30]**
*(Screen: Link GitHub)*

Link trong bio — Apache 2.0, fork thoải mái.

Không cần cài để dùng production.
Cần đọc để **học cách setup `.continue/rules/`** cho project của mày.

*(Text on screen: "Concept không chết theo repo.")*

---

## 📋 METADATA

**Hook chính:** "33k stars. Vừa bị khai tử. Nhưng concept này mày phải học."
**Hook phụ:** "Coding agent open-source đầu tiên vừa chết — đây là thứ nó để lại"

**Tags:** #vibecoding #aitools #claudecode #cursor #opensource #aivietnam #devtools

**Thumbnail concept:**
- Nền: màu đỏ tối hoặc đen
- Text lớn: "33.000 ⭐ → DISCONTINUED"
- Subtext nhỏ hơn: "Nhưng concept này không chết"
- Icon: folder `.continue/` phát sáng giữa màn hình tối

**Cảnh quay cần:**
1. GitHub repo — chỉ rõ dòng "no longer actively maintained"
2. Số stars 33.7k hiển thị rõ
3. VS Code: folder `.continue/` mở ra, thấy rules/ agents/ checks/
4. Mở 1-2 file .md trong rules/ — show content ngắn gọn
5. Git commit có `.continue/` files
6. Slide so sánh: "Không có" vs "Có" pattern
7. Claude Code / Cursor — show `.claude/` hoặc `.cursorrules` tương đương

---

*Script by AI Vibe Toolkit | Video #40*

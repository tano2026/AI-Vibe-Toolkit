# Continue — Coding Agent Open-Source (VS Code + JetBrains + CLI)

**GitHub:** https://github.com/continuedev/continue
**Stars:** 33.7k⭐ | **Forks:** 4.7k | **License:** Apache 2.0
**Tác giả:** Continue Dev, Inc. | **Tạo:** 5/2023
**Docs:** docs.continue.dev

> ⚠️ **QUAN TRỌNG:** Repo này đã **read-only, không còn được maintain** (theo thông báo chính thức trong README). Final release là v2.0.0. Codebase vẫn dùng được nhưng sẽ không có update mới.

---

## Continue Là Gì

Coding agent open-source — chạy trong VS Code, JetBrains, hoặc CLI.

Ý tưởng cốt lõi: **AI checks được lưu trong source control và có thể enforce trong CI.** Không phải chỉ dùng AI để gợi ý code — mà dùng AI để kiểm tra code theo rules của team, tích hợp vào pipeline CI/CD.

---

## 3 Cách Dùng

| Platform | Cài ở đâu | Ghi chú |
|----------|-----------|---------|
| **VS Code Extension** | VS Code Marketplace | Recommend dùng cái này |
| **CLI (`cn`)** | npm: `@continuedev/cli` | Dùng trong CI/CD pipeline |
| **JetBrains Plugin** | GitHub Releases | Khuyên dùng CLI thay thế |

---

## Cài Đặt

**VS Code:**
1. Mở VS Code
2. Extensions → tìm "Continue"
3. Install → xong

**CLI:**
```bash
npm install -g @continuedev/cli
cn --help
```

---

## Cấu Trúc `.continue` Folder — Trái Tim Của Tool

Toàn bộ config lưu trong folder `.continue/` trong project — **source-controlled cùng với code.**

```
.continue/
├── agents/          # AI agents cho các task cụ thể
│   ├── breaking-change-detector.md
│   ├── dependency-security-review.md
│   └── test-coverage.md
├── checks/          # Checks chạy trong CI
├── rules/           # Rules cho AI tuân theo
│   ├── no-any-types.md
│   ├── programming-principles.md
│   ├── typescript-enum-usage.md
│   └── unit-testing-rules.md
├── prompts/         # Prompt templates
└── environment.json # Config môi trường
```

**Điểm đặc biệt:** Rules và agents là file `.md` — team có thể review, edit, version control như code bình thường.

---

## Agents Có Sẵn (Ví Dụ Từ Repo)

Continue tự dùng Continue để maintain code — các agents này là ví dụ thật:

- **breaking-change-detector** — phát hiện breaking changes trước khi merge
- **dependency-security-review** — review security cho dependencies mới
- **error-message-quality** — check chất lượng error messages
- **input-validation** — kiểm tra input validation patterns
- **test-coverage** — phân tích coverage, suggest tests còn thiếu

---

## Rules Ví Dụ (Từ Repo)

Rules là instructions AI phải tuân theo khi làm việc trong project:

- `no-any-types.md` — cấm dùng `any` trong TypeScript
- `programming-principles.md` — nguyên tắc coding của team
- `typescript-enum-usage.md` — quy tắc dùng enum
- `unit-testing-rules.md` — rules viết unit tests
- `pure-function-unit-tests.md` — test pure functions

---

## Tại Sao Concept Này Quan Trọng

**Vấn đề với AI coding hiện tại:**
- Mỗi dev dùng AI theo cách riêng → code style không đồng nhất
- AI không biết conventions của team
- Không có cách enforce AI rules trong CI

**Continue giải quyết:**
- Rules lưu trong `.continue/rules/` → AI biết conventions của team
- Checks chạy trong CI → enforce tự động
- Agents tự động review PR → giảm effort manual review

---

## Tình Trạng Hiện Tại (6/2026)

| Điều | Thực tế |
|------|---------|
| Repo status | ⚠️ Read-only, không maintain |
| Final version | v2.0.0 (VS Code) / v1.2.22 |
| Vẫn dùng được không? | ✅ Có — code vẫn hoạt động |
| Có update mới không? | ❌ Không |
| Codebase có giá trị không? | ✅ Cao — foundation tốt cho fork/học |

---

## Dùng Như Thế Nào Trong 2026

Dù repo đã freeze, vẫn có 3 cách khai thác:

**1. Dùng VS Code extension v2.0.0** — vẫn hoạt động bình thường cho daily coding

**2. Học kiến trúc `.continue/` folder** — concept source-controlled AI rules rất hay, apply vào project của mày với Claude Code hoặc Cursor

**3. Fork và tự maintain** — 4.7k forks, codebase TypeScript sạch, Apache 2.0 license

---

## Đánh Giá Cá Nhân

33.7k stars — chứng tỏ concept được validate mạnh. Pioneering open-source coding agent từ 2023, trước khi GitHub Copilot Workspace hay Cursor ra.

Nhưng thực tế tháng 6/2026: **repo đã chết**. Không còn maintain. Đây là điểm mày phải nói thẳng với audience nếu làm video.

Điểm cực kỳ giá trị vẫn còn đó: **concept `.continue/` folder** — lưu AI rules trong source control, enforce trong CI. Đây là pattern mày có thể apply ngay với Claude Code, Cursor, hoặc bất kỳ coding AI nào khác.

Angle video tốt nhất: "Repo này đã chết — nhưng concept này thay đổi cách mày dùng AI để code."

**Rating: 7/10** — Concept 10/10, nhưng trừ điểm vì đã discontinued. Xem để học pattern, không phải để dùng production lâu dài.

---

*Nguồn: github.com/continuedev/continue*
*Stars: 33.7k⭐ (tháng 6/2026) | Apache 2.0 | Read-only / Discontinued*
*Cập nhật: tháng 6/2026*

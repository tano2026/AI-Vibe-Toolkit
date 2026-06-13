# html-anything — Biến Markdown thành HTML đẹp bằng AI, $0 API key

**GitHub:** https://github.com/nexu-io/html-anything
**Stars:** 6.2k | **License:** Apache 2.0
**Tác giả:** nexu-io team | **Ra mắt:** tháng 5/2026
**Built in:** ~3 ngày, ~15,000 dòng code

---

## Vấn đề nó giải quyết

Mày có content — notes, CSV, Markdown, data — muốn biến thành trang HTML đẹp để share lên WeChat, X, Zhihu, hoặc làm slide deck, poster, report.

Cách cũ: copy vào Canva, dùng template, chỉnh tay. Tốn thời gian.

html-anything: paste content → chọn template → ⌘+Enter → HTML/PNG xuất ra ngay. **AI agent (cái mày đã cài sẵn) viết HTML, mày ship nó.**

Điểm khác biệt lớn nhất: **$0 API key**. Nó không tạo API key mới — nó dùng session của Claude Code, Cursor, Codex, Gemini CLI... cái mày đã đăng nhập sẵn.

---

## Cách Hoạt Động

```
Mày paste content (Markdown/CSV/JSON...)
        ↓
html-anything detect coding agent CLI trên máy
(Claude Code / Cursor / Gemini CLI / Codex / Aider...)
        ↓
Gửi prompt + content đến agent đó
        ↓
Agent generate HTML, stream real-time vào iframe
        ↓
Mày export: download .html / .png / copy cho WeChat
```

Không có server. Không có API key riêng. Chạy local hoàn toàn.

---

## Cài

```bash
pnpm -F @html-anything/next dev
```

Hoặc:
```bash
git clone https://github.com/nexu-io/html-anything
cd html-anything
pnpm install
pnpm dev
```

Mở browser → auto detect agent CLI đã login → chọn template → dùng.

---

## 75 Templates × 9 Surfaces

| Surface | Ví dụ templates |
|---------|----------------|
| **magazine** | Editorial layout, long-form article |
| **deck** | Keynote, Swiss International, XHS Pastel |
| **poster** | Event poster, infographic |
| **social** | X card, Xiaohongshu card, Spotify card |
| **resume** | Clean CV, creative resume |
| **prototype** | SaaS landing, dashboard, data report |
| **frame** | Hyperframes video frames |
| **report** | Data report với charts |
| **web** | Web prototype |

---

## 8 Agent CLIs Được Hỗ Trợ

Claude Code · Cursor Agent · OpenAI Codex · Gemini CLI · GitHub Copilot CLI · OpenCode · Qwen Coder · Aider

Auto-detected trên startup — mày đang dùng cái nào, nó dùng cái đó.

---

## Ví Dụ Thực Tế

**Từ CSV thành data report:**
```
Input: sales_q2.csv
Template: Data Report
Output: HTML page với charts, tables, summary
```

**Từ notes thành slide deck:**
```
Input: meeting_notes.md (gạch đầu dòng)
Template: Keynote deck
Output: Professional presentation HTML
```

**Từ text thành Xiaohongshu card:**
```
Input: bài viết về AI tools
Template: XHS Pastel card
Output: 1080×1350px visual card
```

---

## Điểm Trừ Thẳng Thắn

**Cần có sẵn coding agent CLI:** Nếu mày chưa cài Claude Code hay Cursor thì không dùng được. Không phải tool cho người dùng web interface.

**Mới:** Ra mắt tháng 5/2026, còn bugs. Community đang grow nhưng support chưa nhiều.

**Output phụ thuộc vào agent:** Template giống nhau nhưng Claude Code vs Gemini CLI có thể ra HTML khác nhau.

**Chủ yếu cho East Asian platforms:** WeChat, Xiaohongshu, Zhihu là focus chính. Dùng cho Western platforms vẫn được nhưng templates ít hơn.

---

## Đánh Giá Cá Nhân

html-anything là ý tưởng thú vị: thay vì pay thêm cho tool mới, tái dụng agent subscription mày đã có. Zero marginal cost là real value proposition.

6.2k stars trong 1 tháng cho thấy timing đúng — mọi người đang tìm cách tận dụng coding agent subscription cho nhiều hơn chỉ coding.

Template system với 75 skills là điểm mạnh lớn — không phải prompt blank, mà mỗi template đã được craft để output đẹp ngay. Concept này giống marketingskills nhưng cho visual output.

Tao thấy nó hữu ích nhất cho: nhanh tạo content visual để share social media, không muốn mở Canva. Không phải replacement cho design tool, nhưng là shortcut tốt.

**Rating: 7.5/10** — deduct vì còn non, dependency vào coding agent CLI là barrier với nhiều người.

---

*Nguồn: github.com/nexu-io/html-anything*
*Cập nhật: tháng 6/2026*

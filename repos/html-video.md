# html-video (nexu-io) — AI Agent Viết HTML, Mày Nhận MP4

**GitHub:** https://github.com/nexu-io/html-video
**Stars:** ~346 | **Forks:** 12 | **License:** Apache 2.0
**Tác giả:** nexu-io (Open Design team)
**Dùng với:** Claude Code, Cursor, Codex, Gemini CLI, Windsurf, Grok, Qwen...

---

## Concept Đơn Giản Nhưng Mạnh

Thay vì kéo thả timeline trong Premiere hay CapCut — mày mô tả video bằng ngôn ngữ tự nhiên, hoặc paste link GitHub repo / bài viết, AI agent viết HTML + CSS + JS tạo animation, rồi render ra MP4 thật trên máy mày.

```
Mày: "Tạo video giải thích DiffusionGemma của Google"
→ Agent fetch GitHub repo hoặc tìm thông tin
→ Agent viết HTML multi-frame có animation
→ html-video render từng frame
→ Ghép thành MP4 thật — có audio nếu cần
```

Không có server. Không có per-render fee. Chạy local hoàn toàn.

---

## 3 Kiểu Input

**1. GitHub repo link:**
```bash
# Agent tự fetch README + structure + top-level files
"Tạo video giải thích repo này: github.com/google/magika"
→ Video "explain this open-source project" tự động
```

**2. URL / bài viết:**
```bash
"Tạo video tóm tắt bài này: [URL]"
→ Agent đọc content → tạo video
```

**3. Prompt thuần:**
```bash
"Tạo video 30 giây về cách Decision Tree hoạt động"
→ Agent tự viết content + animation
```

---

## 21 Templates Sẵn Có

| Template | Dùng cho |
|----------|---------|
| `frame-data-chart-nyt` | Data viz style NYT — line chart có annotation |
| `frame-code-explainer` | Giải thích code step-by-step |
| `frame-product-launch` | Product announcement |
| `frame-timeline` | Timeline events |
| `frame-comparison` | So sánh A vs B |
| `frame-stats-dashboard` | Dashboard metrics |
| + 15 templates khác | ... |

Mỗi template là **animated single-file HTML** — agent fill content vào, render ra MP4.

---

## Cài & Dùng

```bash
git clone https://github.com/nexu-io/html-video
cd html-video
npm install

# Với Claude Code
npx skills add nexu-io/html-video

# Mô tả video
"Create a 60-second explainer video about browser-use library"
```

**Render engines hỗ trợ:**
- Puppeteer (default, local)
- Playwright
- Remotion (nếu đã cài)

---

## AI Soundtrack

```bash
# Thêm nhạc nền tự động
"Create video with ambient background music"
→ AI generate soundtrack phù hợp với tone video
```

---

## Workflow Cho Content Creator

Kết hợp với pipeline của mày:
```
GitHub repo hay → html-video agent → MP4 video giải thích
→ CapCut thêm sub tiếng Việt → TikTok/YouTube
```

Thay thế bước quay screen record + voiceover cho video giải thích repo — AI làm hết.

---

## Đánh Giá Cá Nhân

html-video là thứ tao đang thử nghiệm cho pipeline video. Ý tưởng cốt lõi rất hay: thay vì giải thích repo bằng cách quay màn hình, để AI tạo motion graphics giải thích luôn.

346 stars là còn nhỏ nhưng đây là project của nexu-io — team đứng sau open-design (64k stars) và html-anything (6.2k stars). Quality và maintenance đáng tin.

Điểm trừ: template library còn ít, output MP4 chưa đẹp bằng Remotion. Nhưng zero per-render fee và không cần biết React là lợi thế lớn.

**Rating: 7.5/10** — tiềm năng cao, ecosystem còn đang grow.

---

*Nguồn: github.com/nexu-io/html-video | Cập nhật: tháng 6/2026*

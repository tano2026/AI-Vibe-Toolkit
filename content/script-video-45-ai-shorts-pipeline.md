# Script Video #45 — AI Shorts Generator: Playwright + Claude → MP4 Tự Động

**Concept:** Pipeline từ TikTok @Meii
**Stack:** Claude Code + Playwright + FFmpeg + ElevenLabs/Supertonic
**Thời lượng:** 60-90 giây
**Hook:** "Gõ 1 lệnh, nhận MP4 cho YouTube và TikTok"

---

## 🎬 SCRIPT

---

**[HOOK — 0:00-0:08]**
*(Text: "/promo [link] → 28 giây MP4 cho YouTube + TikTok")*

Mày paste link GitHub.
Claude fetch, analyze, draft storyboard.
Playwright render.
FFmpeg mux voiceover.

Output: 16×9 cho YouTube, 9×16 cho TikTok.
Cùng 1 lệnh.

---

**[PIPELINE — 0:08-0:40]**
*(Screen: Flow diagram từ ảnh)*

**Bước 1:** `/promo [URL]`
Claude tự fetch README, đọc stars, features.
→ Draft storyboard 6 scenes, 25-32 giây.

**Bước 2:** Mày review `storyboard.json`
*(Human-in-the-loop — approve trước khi render)*

**Bước 3:** Playwright record `render.html`
Chụp 2 viewport: 1920×1080 và 1080×1920

**Bước 4:** FFmpeg
WebM → MP4
+ mux voiceover ElevenLabs hoặc Supertonic free

**Output:** 2 files ready to upload.

---

**[SCENES — 0:40-0:55]**
*(Screen: Scene templates)*

6 scene templates:
- `hero-text` — hook lớn, animation
- `terminal` — demo command animated
- `stats-grid` — số: stars, time saved
- `iframe` — live demo
- `quote` — testimonial
- `cta-url` — call to action

Claude chọn đúng template cho từng moment.

---

**[DEMO — 0:55-1:05]**
*(Screen: Terminal chạy lệnh)*

```
/promo https://github.com/addyosmani/agent-skills
```

→ 15 giây sau: storyboard.json draft xong.
Review. Approve.
→ 2 phút sau: 2 MP4 files.

---

**[CTA — 1:05-1:15]**
*(Text: "Stack: Claude Code + Playwright + FFmpeg")*

Stack free hoàn toàn trừ ElevenLabs.
Thay ElevenLabs bằng Supertonic → $0.

Link pipeline diagram trong bio.

---

## 📋 METADATA

**Tags:** #claudecode #playwright #vibecoding #aivietnam #videoautomation #aitools

**Thumbnail:**
- Flow diagram đơn giản: /promo → Claude → Playwright → MP4
- Text lớn: "1 LỆNH → 2 VIDEO"
- Màu: dark + purple accent

**Cảnh quay:**
1. Terminal: `/promo [url]` command
2. storyboard.json mở trong editor
3. Playwright đang record browser
4. FFmpeg chạy
5. 2 files .mp4 xuất hiện trong folder

---
*Script by AI Vibe Toolkit | Video #45*

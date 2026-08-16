# Copywriting Prose Creator — Skill

## TL;DR
Skill mã hóa CÁCH một brand/con người viết (từ vựng, cấu trúc câu, nhịp điệu, chiêu đặc trưng) thành file `PROSE.md` — tách biệt hẳn khỏi tông cảm xúc (tone). Dùng để xây content factory nhiều người viết mà vẫn ra giọng nhất quán.

## Tool này dùng để làm gì
Slogan của skill: **"tone là nhạc, prose là bản nhạc"** (tone is the music, prose is the score). Ý là 2 brand có thể giống tông cảm xúc y hệt nhau nhưng cách viết (câu dài/ngắn, cách mở đoạn, từ hay lặp) khác hẳn — skill này chỉ codify phần "bản nhạc" đó thôi, không đụng tới cảm xúc.

3 mode:
- **BUILD** — tạo `PROSE.md` mới từ `SOUL.md` + `TONE.md` + phỏng vấn khám phá
- **ADAPT** — port `PROSE.md` có sẵn sang kênh mới (vd từ blog sang TikTok caption)
- **AUDIT** — quét kho nội dung cũ (>50 bài thì tự fan-out sub-agent song song) để rút ra pattern viết hiện tại trước khi mã hóa thành rule

Output `PROSE.md` này chính là nền tảng để các skill viết nội dung khác (linkedin-ghostwriting, technical-article-writer, press-release-writer trong cùng repo) bám vào, đảm bảo dù AI hay ghostwriter thật viết cũng ra cùng 1 "vân tay văn phong".

## Setup từng bước
1. Cài 1 skill lẻ từ repo:
```
npx skills add https://github.com/samber/cc-skills --skill copywriting-prose-creator
```
2. Claude Code: `/plugin install cc-skills@samber` (cài trọn bộ, gồm cả skill này)
3. Chuẩn bị input tùy mode:
   - BUILD: cần `SOUL.md` (nếu có), `TONE.md` (nếu có, từ skill `copywriting-tone-of-voice-creator` cùng repo) — không có thì skill tự phỏng vấn
   - AUDIT: gom link/text bài viết cũ của brand lại
4. Gọi skill, chọn mode, trả lời phỏng vấn (agent hỏi từng câu, không hỏi dồn).

## Ví dụ thực tế
Input: "Build PROSE.md cho kênh Trùm Sân Bay — giọng insider sân bay, hài hước nhưng đáng tin."
→ Skill hỏi thêm vài câu (câu dài trung bình bao nhiêu từ, có dùng emoji không, từ nào cấm dùng...) rồi ra `PROSE.md` với bảng quy tắc cụ thể theo 4 nhóm kênh: bài dài (blog/script YouTube full), social post (TikTok caption, Facebook), email, marketing copy (landing page ABTRIP, quảng cáo).
Từ đó, mọi script video Trùm Sân Bay Hermes/OpenClaw generate ra đều bám theo cùng 1 file này thay vì mỗi lần Claude viết một giọng khác.

## Lưu ý / Lỗi thường gặp
- Không dùng để viết nội dung thật — skill này CHỈ ra rule, viết bài thật phải gọi skill khác (linkedin-ghostwriting, technical-article-writer...).
- Không xử lý việc xóa "mùi AI" (từ sáo rỗng, em-dash lạm dụng...) — cái đó là skill `humaniseur-fr` (bản tiếng Pháp) riêng trong cùng repo, kho hiện có bản tương đương `humanizer`.
- File PROSE.md khá nặng nếu load full (~23k token cả directory) — chỉ nên load khi thật sự cần build/audit, đừng giữ thường trực trong context.

## Đánh giá cá nhân
- Điểm mạnh: tách tone/prose rất rõ ràng, đúng vấn đề của content factory nhiều agent viết (Hermes/OpenClaw/Claude) dễ bị lệch giọng theo thời gian — có PROSE.md neo lại thì đỡ trôi.
- Điểm yếu: cần input chất lượng (SOUL.md/TONE.md hoặc corpus đủ lớn) mới ra rule tốt — nếu chỉ trả lời qua loa phỏng vấn thì output PROSE.md chung chung, không khác gì rule mặc định của LLM.
- Có nên dùng không: 8/10 — nên ghép với `voice-profile-builder` đang "để dành làm sau" trong kho, 2 cái này bổ sung nhau (voice-profile lo giọng nói audio, PROSE.md lo giọng viết text).

## Link
- Repo: https://github.com/samber/cc-skills
- SKILL.md gốc: https://github.com/samber/cc-skills/blob/main/skills/copywriting-prose-creator/SKILL.md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request
url = "https://raw.githubusercontent.com/samber/cc-skills/main/skills/copywriting-prose-creator/SKILL.md"
content = urllib.request.urlopen(url).read().decode()
with open("skills_local/copywriting-prose-creator/SKILL.md", "w") as f:
    f.write(content)
```

### OpenClaw
```bash
git clone https://github.com/samber/cc-skills.git ~/.openclaw/skills/cc-skills-prose
```

### Antigravity
```bash
git clone https://github.com/samber/cc-skills.git ~/.antigravity/skills/cc-skills
```
> ⚠️ Cần chạy BUILD mode 1 lần cho mỗi brand (Trùm Sân Bay, Tano, Wonder Mart, GMSP) — output PROSE.md khác nhau, đừng dùng chung 1 file cho tất cả brand.

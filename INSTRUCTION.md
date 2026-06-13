# 📖 Hướng Dẫn Sử Dụng AI Vibe Toolkit

> Đọc cái này trước khi dùng kho. 5 phút đọc, tiết kiệm cả tiếng mày tự mò.

---

## 🎯 Project này là gì

Kho tổng hợp MCP, Skills, Repos và Tools hay nhất cho **vibe coders** — được research thực tế, viết lại bằng tiếng người, kèm script video sẵn sàng để làm content.

**2 mục đích chính:**
1. **Kho kiến thức** — tra cứu và dùng tools AI hiệu quả hơn
2. **Content factory** — mỗi entry trong kho = 1 video TikTok/YouTube

---

## 📁 Cấu trúc kho

```
AI-Vibe-Toolkit/
│
├── INSTRUCTION.md      ← Mày đang đọc cái này
├── TRACKER.md          ← Theo dõi toàn bộ kho + lịch đăng
│
├── mcps/               ← MCP Servers
├── skills/             ← Prompt templates & System prompts  
├── repos/              ← GitHub repos hay
├── stacks/             ← Combo tools theo use case
└── content/            ← Script video sẵn sàng quay
```

---

## 🔄 Workflow hàng ngày

### Mày làm (5-10 phút/ngày)
```
Thấy gì hay → Chụp ảnh hoặc copy link
            → Quẳng vào chat với Claude (tao)
            → Tao research + viết file .md + script video
            → Push tự động lên GitHub
```

### Tao làm (phần còn lại)
```
Research tool/repo
→ Viết file .md vào đúng folder
→ Viết script video kèm theo
→ Update TRACKER.md
→ Push lên GitHub
```

---

## 📂 Từng folder dùng thế nào

### `/mcps` — MCP Servers
Mỗi file = 1 MCP server đã được test.

**Cách dùng:**
- Đọc phần "Setup trong 3 bước" → copy config → paste vào Claude Desktop
- Đọc phần "Dùng thế nào" → có prompt mẫu copy luôn

**Format tên file:** `tên-mcp.md` (ví dụ: `context7.md`, `firecrawl.md`)

---

### `/skills` — Prompt Templates
Mỗi file = 1 prompt template hoặc system prompt đã được test.

**Cách dùng:**
- Copy phần "Prompt Template" → paste vào Claude
- Điền vào chỗ `[IN HOA TRONG NGOẶC]`
- Chạy luôn

**Format tên file:** `tên-skill.md` (ví dụ: `research-agent.md`)

---

### `/repos` — GitHub Repos
Mỗi file = 1 repo đáng học/dùng, đã được tóm tắt bằng tiếng người.

**Cách dùng:**
- Đọc "Bắt đầu nhanh" → làm theo
- Đọc "Kết hợp với AI thế nào" → có prompt mẫu

**Format tên file:** `tên-repo.md` (ví dụ: `superpowers.md`)

---

### `/content` — Script Video
Mỗi file = 1 script video hoàn chỉnh sẵn sàng quay.

**Cách dùng:**
1. Mở file script
2. Đọc phần Visual → biết cần quay/chụp gì
3. Đọc Script → đây là lời thoại (feed vào ElevenLabs để tạo voiceover)
4. Dùng Caption khi đăng TikTok/YouTube
5. Dùng Thumbnail concept khi làm thumbnail

**Format tên file:** `script-video-XX-tên.md`

---

### `/stacks` — Combo Tools
Mỗi file = combo tools cho 1 use case cụ thể.

**Cách dùng:** Đọc và làm theo thứ tự setup trong file.

---

## 📊 TRACKER.md — File quan trọng nhất

Mở `TRACKER.md` để biết:
- Kho có gì rồi
- Cái nào đã có script, cái nào chưa
- Lịch đăng content

**Update TRACKER** mỗi khi thêm nội dung mới vào kho.

---

## 🤖 Cách làm việc với Claude (tao)

### Thêm nội dung mới vào kho
```
Mày: [paste link hoặc ảnh]
Tao: research → viết .md → viết script → push GitHub
```

### Lấy script video ra làm content
```
Mày: "Làm script video cho [tên tool]"
Tao: viết script theo format chuẩn → push vào /content/
```

### Tìm tool theo nhu cầu
```
Mày: "Tao cần tool để làm X"
Tao: search kho + search internet → recommend tool phù hợp
```

### Update hàng tuần
```
Mày: "Tìm trending mới tuần này"
Tao: check GitHub Trending + Reddit + Product Hunt
   → top 5 tool đáng làm content
   → mày chọn → tao viết
```

---

## 🎬 Pipeline làm video (không cần quay mặt)

```
Script (từ /content/) 
    → ElevenLabs (tạo voiceover AI tiếng Việt)
    → OBS hoặc CapCut (screen recording demo tool)
    → CapCut (ghép audio + video + auto sub)
    → Canva (thumbnail)
    → Đăng TikTok/YouTube
```

**Thời gian mỗi video:** ~30-45 phút (khi đã quen pipeline)

---

## 📅 Lịch làm việc gợi ý

| Thời điểm | Việc |
|-----------|------|
| Hàng ngày | Quẳng link/ảnh hay thấy cho Claude |
| Thứ 2 | Tao tìm GitHub Trending tuần mới |
| Thứ 4 | Làm video từ script sẵn có |
| Thứ 6 | Đăng video + lên lịch post tuần sau |

---

## ❓ FAQ

**Q: Tao không biết code, dùng được không?**
A: Được. Mọi file đều có hướng dẫn từng bước, không cần biết code.

**Q: MCP là gì?**
A: Xem `/mcps/README.md` — giải thích đơn giản nhất có thể.

**Q: Muốn thêm tool vào kho thì làm thế nào?**
A: Quẳng link/ảnh cho Claude trong chat, tao làm hết.

**Q: Script video dùng thế nào nếu không biết dựng?**
A: Feed lời thoại vào ElevenLabs → lấy audio. Quay screen demo bằng OBS. Ghép bằng CapCut. Tao sẽ hướng dẫn chi tiết khi cần.

**Q: Tao muốn đổi format hoặc thêm section mới?**
A: Bảo Claude, tao update template và format cho toàn kho.

---

## 🔑 GitHub Token

Token đã được setup để Claude có thể tự push lên repo.  
**KHÔNG share token này cho ai.**  
Nếu cần revoke → GitHub → Settings → Developer Settings → Personal Access Tokens.

---

*AI Vibe Toolkit — by tano2026 | Cập nhật: 06/2025*

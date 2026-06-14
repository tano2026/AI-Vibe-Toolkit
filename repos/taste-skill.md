# taste-skill — Anti-Slop Frontend Framework Cho AI Agent

**GitHub:** https://github.com/Leonxlnx/taste-skill
**Stars:** 43.3k⭐ | **Forks:** 3k | **License:** MIT
**Tác giả:** Leonxlnx (@lexnlin) | **Tạo:** 02/2026
**Website:** tasteskill.dev

---

## Đây Là Gì

Bộ **Agent Skills** — files hướng dẫn AI (Claude Code, Cursor, Codex) tạo UI có gu thay vì UI boilerplate nhàm chán.

**Vấn đề cụ thể:** Mày nhờ AI làm landing page → nó ra trang xanh dương + Inter font + gradient hero + card shadow kiểu mặc định. Nhìn giống hệt 10 triệu trang khác trên internet.

**taste-skill fix cái đó.** Cài skill vào → AI đọc brief của mày trước, suy ra design direction phù hợp, rồi mới viết code — với typography, spacing, motion đúng level.

---

## 10 Skills — Mỗi Cái Làm 1 Việc

| Skill | Install name | Dùng khi nào |
|-------|-------------|--------------|
| **taste-skill** (v2) | `design-taste-frontend` | Default — landing page, portfolio, redesign |
| **taste-skill-v1** | `design-taste-frontend-v1` | Giữ behavior v1 cũ nếu cần |
| **gpt-tasteskill** | `gpt-taste` | Cho GPT/Codex — stricter, GSAP mạnh hơn |
| **redesign-skill** | `redesign-existing-projects` | Audit + fix UI có sẵn, không rewrite từ đầu |
| **soft-skill** | `high-end-visual-design` | Agency $150k tier — Awwwards level |
| **minimalist-skill** | `minimalist-ui` | Notion/Linear vibe — warm mono, bento grid |
| **brutalist-skill** | `industrial-brutalist-ui` | Swiss type, sharp contrast, experimental layout |
| **output-skill** | `full-output-enforcement` | Khi AI cứ truncate code không viết đủ |
| **stitch-skill** | `stitch-design-taste` | Google Stitch compatible |
| **image-to-code-skill** | `image-to-code` | Generate ảnh ref → analyze → code |

### Image Generation Skills (xuất ảnh, không phải code)
- `imagegen-frontend-web` — Website comps, hero, landing
- `imagegen-frontend-mobile` — Mobile screens, flows
- `brandkit` — Logo directions, palettes, identity

---

## Cài Đặt — 1 Lệnh

```bash
# Cài tất cả skills
npx skills add https://github.com/Leonxlnx/taste-skill

# Cài 1 skill cụ thể
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"

# Update từ v1 lên v2
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

Hoặc copy thẳng file `SKILL.md` vào project / paste vào ChatGPT conversation.

---

## 3 Dial Điều Chỉnh (taste-skill v2)

Số từ 1-10 ở đầu file SKILL.md:

| Dial | Ý nghĩa | Thấp → Cao |
|------|---------|------------|
| **DESIGN_VARIANCE** | Độ táo bạo layout | Centered/clean → Asymmetric/modern |
| **MOTION_INTENSITY** | Độ animation | Hover only → Scroll + magnetic effects |
| **VISUAL_DENSITY** | Thông tin mỗi viewport | Spacious/airy → Dense dashboard |

---

## Cách AI Làm Việc Với Skill Này

**Bước 0 — Brief Inference (quan trọng nhất):**
AI đọc brief của mày trước, suy ra:
- Page kind: landing SaaS / portfolio / redesign / editorial
- Vibe words: "minimalist", "brutalist", "premium", "playful"
- Reference signals: URLs mày link, screenshots mày paste
- Audience: B2B hay consumer hay recruiter

Sau đó mới chọn aesthetic phù hợp. Không jump vào default template.

**Anti-patterns bị cấm tuyệt đối:**
- ❌ Font: Inter, Roboto, Arial, Open Sans
- ❌ Icon: Lucide thick-stroke, FontAwesome, Material Icons generic
- ❌ Border: 1px solid gray generic
- ❌ Shadow: shadow-md / shadow-lg mặc định
- ❌ Gradient: hero gradient màu mè
- ❌ Button: rounded-full + blue primary + hover:opacity-90

**Thay bằng:**
- ✅ Font: Geist, Clash Display, Satoshi, Cabinet Grotesk, PP Editorial New
- ✅ Icon: Phosphor Light, Remix Line — ultra-thin precision
- ✅ Shadow: diffuse, opacity < 0.05
- ✅ Motion: GSAP ScrollTrigger, spring physics, magnetic hover

---

## Redesign Skill — Đặc Biệt Hữu Ích

Nếu mày có website có sẵn muốn upgrade:

```
# Paste redesign-skill SKILL.md → nhờ AI:
1. Scan codebase — đọc framework, styling method
2. Diagnose — list generic patterns, weak points
3. Fix — targeted upgrades, không rewrite từ đầu
```

Nó check: typography, color system, spacing, component states, motion, border radius, shadow...

---

## Workflow Image-First

```
1. Dùng imagegen-frontend-web → generate website comps reference
2. Feed renders vào Cursor/Claude Code + image-to-code-skill
3. AI analyze ảnh → implement frontend match ảnh
```

Hữu ích khi mày có vision rõ trong đầu nhưng khó diễn đạt bằng text.

---

## Đánh Giá Cá Nhân

43.3k stars trong 4 tháng — fastest growing frontend skill repo trên GitHub. Không phải hype: vấn đề "AI UI trông nhàm chán" là vấn đề thật mà mọi vibe coder đều gặp.

Điểm tao thấy thực dụng nhất: **Brief Inference ở Bước 0** — thay vì AI đoán mò aesthetic, nó đọc vibe words và references của mày trước. Đây là thứ phân biệt output có gu vs output generic.

Điểm trừ: Cần biết dùng `npx skills add` và hiểu AI coding workflow cơ bản. Không phải tool cho người hoàn toàn mới.

Dùng với Claude Code hoặc Cursor — cài `design-taste-frontend` là default đủ tốt cho 80% cases. Thêm `redesign-existing-projects` nếu có project cũ cần lift.

**Rating: 9.5/10** — Must-have cho bất kỳ vibe coder nào làm frontend.

---

*Nguồn: github.com/Leonxlnx/taste-skill*
*Stars: 43.3k⭐ (tháng 6/2026) | MIT License*
*Cập nhật: tháng 6/2026*

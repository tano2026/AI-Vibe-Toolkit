# taste-skill — Index & Hướng Dẫn Dùng Nhanh

**Nguồn:** github.com/Leonxlnx/taste-skill (43.3k⭐) | MIT
**Cập nhật:** tháng 6/2026

---

## Cài Nhanh (Không Cần Đọc Gì Thêm)

```bash
# Cài 1 lệnh — tất cả skills
npx skills add https://github.com/Leonxlnx/taste-skill

# Hoặc cài từng skill
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

---

## Chọn Skill Nào?

| Situation | Dùng file | Install name |
|-----------|-----------|--------------|
| Landing page / portfolio mới | `taste-skill.md` | `design-taste-frontend` |
| Fix/upgrade UI cũ có sẵn | `redesign-skill.md` | `redesign-existing-projects` |
| Muốn Awwwards / agency tier | `soft-skill.md` | `high-end-visual-design` |
| Notion/Linear/SaaS tool vibe | `minimalist-skill.md` | `minimalist-ui` |
| Swiss type, experimental brutalist | `brutalist-skill.md` | `industrial-brutalist-ui` |
| Dùng với GPT/Codex (strict) | `gpt-tasteskill.md` | `gpt-taste` |
| AI cứ truncate code không viết đủ | `output-skill.md` | `full-output-enforcement` |
| Google Stitch workflow | `stitch-skill.md` | `stitch-design-taste` |
| Generate ảnh ref rồi code theo | `image-to-code-skill.md` | `image-to-code` |

---

## Cách Dùng Thủ Công (Không Cần npx)

1. Mở file `.md` tương ứng trong folder này
2. Copy toàn bộ content
3. Paste vào:
   - **Claude Code:** đầu conversation hoặc vào `CLAUDE.md`
   - **Cursor:** vào `.cursorrules`  
   - **ChatGPT:** paste vào system prompt hoặc đầu chat

---

## 3 Dials (Chỉnh Trong taste-skill.md)

Tìm dòng đầu SKILL.md, chỉnh số 1-10:
```
DESIGN_VARIANCE: 7    ← layout táo bạo (1=clean, 10=experimental)
MOTION_INTENSITY: 5   ← animation depth (1=hover, 10=cinematic)
VISUAL_DENSITY: 4     ← info density (1=airy, 10=dense)
```

---

## Anti-Patterns Bị Cấm (Nhớ Thuộc)

### ❌ Font KHÔNG dùng
Inter · Roboto · Arial · Open Sans · Helvetica

### ✅ Font NÊN dùng  
Geist · Satoshi · Cabinet Grotesk · Clash Display · PP Editorial New · Plus Jakarta Sans · Outfit

### ❌ Patterns KHÔNG dùng
- shadow-md / shadow-lg (generic shadows)
- rounded-full + blue primary button
- 1px solid gray borders
- Gradient hero sections màu mè
- Glassmorphism nặng
- Lucide thick-stroke icons

### ✅ Thay bằng
- Diffuse shadows, opacity < 0.05
- GSAP ScrollTrigger animations
- Spring physics, magnetic hover
- Phosphor Light / Remix Line icons
- OKLCH color system

---

## Files Trong Folder Này

| File | Kích thước | Dùng cho |
|------|-----------|---------|
| `taste-skill.md` | ~87k chars | Main skill — v2 experimental |
| `taste-skill-v1.md` | ~21k chars | V1 cũ — stable behavior |
| `redesign-skill.md` | ~15k chars | Fix UI cũ |
| `soft-skill.md` | ~10k chars | High-end agency |
| `minimalist-skill.md` | ~8k chars | Notion/Linear |
| `brutalist-skill.md` | ~8k chars | Experimental |
| `gpt-tasteskill.md` | ~8k chars | GPT/Codex strict |
| `stitch-skill.md` | ~12k chars | Google Stitch |
| `image-to-code-skill.md` | ~36k chars | Image → analyze → code |
| `output-skill.md` | ~2.5k chars | Fix AI truncate output |

---

*Tất cả files là SKILL.md gốc từ repo, không chỉnh sửa*

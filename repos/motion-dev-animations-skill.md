# motion-dev-animations-skill (199-biotechnologies) — GitHub Repo

## TL;DR
Skill Claude Code của tổ chức `199-biotechnologies` (MIT) sinh code animation cho web bằng thư viện Motion.dev: hero fade-up, scroll reveal, parallax, hover lift, magnetic button, kéo-thả. Cài xong là skill tự kích hoạt khi mày nhắc tới animation. **Cảnh báo:** skill nhắm **Motion.dev v11+**, ghi ngày tạo/cập nhật 07–08/11/2025, trong khi npm hôm nay là **v14.1.0**; commit cuối 30/03/2026; và README có nhiều con số tự khen chưa kiểm được.

> Ghi chú tên: link trong bài post bị cụt ("github.com/199.../motion-dev-animations-skill"). Chủ repo là **`199-biotechnologies`** (✅ clone và đọc được repo, tìm ra qua kết quả tìm kiếm, đối chiếu badge trong README).

## Repo này dùng để làm gì
Cho Claude quy trình 4 bước: **Clarify** (hỏi framework: React 19+, Next 15+, Svelte 5+, Astro 4+) → **Plan** (chọn pattern, spring) → **Implement** (TypeScript/JSX chỉ animate transform/opacity/filter) → **Verify** (kiểm 60fps+, `prefers-reduced-motion`, bàn phím, bundle < 50 KB). Có 5 ví dụ (`card-hover`, `hero-fade-up`, `magnetic-button`, `parallax-layers`, `scroll-reveal`), template, schema JSON và script `validate_motion_config.py`.

## Số liệu đã kiểm (2026-10-12)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao / Fork | **chưa đo** | ❓ lần fetch trang repo bị từ chối vì URL đầy đủ không có trong tin nhắn |
| License | MIT | 📖 badge README + file `LICENSE` ✅ |
| Commit gần nhất | 2026-03-30 | ✅ `git log` trên bản clone nông |
| Phiên bản skill | 3.0.0 (metadata ghi tạo 2025-11-07, cập nhật 2025-11-08) | ✅ đọc frontmatter `SKILL.md` |
| Motion mục tiêu | "v11+" | ✅ `SKILL.md`. npm hôm nay: **14.1.0** (✅ `npm view motion version`) |
| CLI `skills` nhận ra | 1 skill (`motion-dev-animations`) | ✅ `npx skills add <clone cục bộ> --list` |

## Đối chiếu với bài post
- "Gõ đúng một câu lệnh là Claude Code tự động gắn animation chuẩn production": README nói cài xong thì dùng câu tự nhiên, skill **hỏi lại framework** trước khi làm. Không phải một câu là xong.
- "Kèm hiệu ứng cuộn trang sống động": đúng, có scroll reveal và parallax.
- README tự ghi "10M+ downloads/month" cho Motion.dev và "87% ít context hơn nhờ nạp dần": **cả hai chưa kiểm** (API downloads bị chặn; con số 87% là của tác giả).

## Setup
📖 Theo README, **chưa chạy trong dự án thật**:
```bash
git clone https://github.com/199-biotechnologies/motion-dev-animations-skill.git ~/.claude/skills/motion-dev-animations
```
Hoặc `npx skills add 199-biotechnologies/motion-dev-animations-skill` (CLI nhận ra cấu trúc ✅ trên clone cục bộ).

## ⚠️ License / Bảo mật / Quyền riêng tư
- MIT. ✅ `scripts/validate_motion_config.py` (172 dòng) chỉ import `json`, `sys`, `pathlib`, `typing`, không gọi mạng. Chưa đọc kỹ từng dòng logic, chưa chạy.
- Repo còn file tạp: `DEPLOYMENT_STATUS.md`, `VALIDATION_V3.md`, `ACTIVATION_TEST.md`, `SKILL.md.backup`, `RESEARCH_SYNTHESIS.md`. Là dấu vết quy trình của tác giả bị commit vào, không hại gì nhưng là tín hiệu "dọn chưa kỹ".

## Ví dụ thực tế
1. Hero section với tiêu đề, phụ đề, CTA vào cảnh lần lượt cho landing page [SẢN PHẨM].
2. Card hover lift + bóng đổ cho danh sách dịch vụ.

## Lưu ý / Lỗi thường gặp
- Skill dạy API cũ có thể sinh code import/API không còn khớp v14. **Luôn chạy build và đọc docs Motion hiện hành** sau khi skill sinh code.
- Dùng cùng `repos/gsap-skills.md` và `repos/motiondivision-motion.md` dễ chồng: chọn một thư viện animation cho cả dự án.

## Đánh giá cá nhân
**Chưa chấm điểm. Ưu tiên thấp** trong nhóm web UI: ít được cập nhật hơn thư viện nó nhắm tới, nhiều con số tự khen, chưa rõ số sao. Nếu mày dùng Motion thì tin tài liệu chính thức của Motion hơn skill này; nếu vẫn thử thì thử trên một component nhỏ rồi so với docs hiện hành.

## Link
- Repo: https://github.com/199-biotechnologies/motion-dev-animations-skill
- Thư viện: https://github.com/motiondivision/motion
- Liên quan trong kho: `repos/motiondivision-motion.md`, `repos/gsap-skills.md`, `skills/motion-ui/`

---

## 🤖 Agent Integration

> Skill dạng prompt cho Claude Code, không có HTTP API.

### Hermes (Python)
```python
# ✅ Đã chạy thật 2026-10-12: so version skill nhắm tới với bản npm hiện hành.
import subprocess

def latest_motion() -> str:
    return subprocess.run(["npm", "view", "motion", "version"],
                          capture_output=True, text=True, timeout=60).stdout.strip()

# print(latest_motion())   # 14.1.0 ngày 2026-10-12, skill nhắm v11+
```

### OpenClaw
```bash
# ❓ chưa chạy
npx skills add 199-biotechnologies/motion-dev-animations-skill
```

### Antigravity
```bash
# ❓ chưa chạy
npm view motion version
```
> ⚠️ Sau khi skill sinh code, build và đọc docs Motion hiện hành. Skill ghi cập nhật lần cuối 11/2025.

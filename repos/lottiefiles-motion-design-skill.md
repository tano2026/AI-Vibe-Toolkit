# motion-design-skill (LottieFiles) — GitHub Repo

## TL;DR
Skill của **LottieFiles** (MIT) dạy AI agent nghĩ như đạo diễn chuyển động trước khi viết một dòng code animation: chọn thời lượng, easing, thứ tự vào cảnh và cảm xúc trước, **12 nguyên tắc hoạt hình của Disney được chuyển cho UI**. Triết lý trước, không gắn với thư viện nào (CSS, Framer Motion, GSAP, Lottie, spring đều dùng được). 2,1k sao. **Điểm cần nói rõ:** đây là chuyển động **giao diện** (nút, card, modal, trạng thái loading/success/error), không phải làm video hay hoạt hình nhân vật.

## Repo này dùng để làm gì
- `SKILL.md` (dưới 500 dòng): checklist 8 bước, 4 kiểu "tính cách chuyển động", bảng thời lượng/easing, chọn thuộc tính, mẫu hay dùng.
- `director/`: triết lý, 12 nguyên tắc Disney cho UI, ánh xạ cảm xúc → chuyển động, choreography nhiều phần tử, kể chuyện vi mô, thích nghi theo ngữ cảnh (nền tảng, truy cập, hiệu năng).
- `patterns/`: công thức vào/ra cảnh, phản hồi trạng thái, chuyển động nền/lặp, nhiều phần tử.
- `reference/`: bảng tra, checklist chất lượng, xử lý lỗi hoạt hình.

## Số liệu đã kiểm (2026-10-12)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao / Fork | 2,1k / 133 | 📖 trang repo qua fetch, chưa đối chiếu API |
| License | MIT | 📖 trang repo + README |
| Số commit | 4 | 📖 trang repo |
| Commit gần nhất | 2026-05-18 | ✅ `git log` trên bản clone nông |
| Nội dung | 100% markdown, **không có script** | ✅ liệt kê file trong clone |
| CLI `skills` nhận ra | 1 skill (`motion-design`) | ✅ `npx skills add <clone cục bộ> --list` (chạy thật, thấy mô tả đầy đủ) |

## Đối chiếu với bài post
Post: "12 nguyên tắc hoạt hình kinh điển của Walt Disney được LottieFiles viết lại dành riêng cho AI Agents". Đúng, có `director/disney-principles.md` ghi "12 principles, UI-adapted". **Phạm vi là UI/UX motion**, README liệt kê chính xác loại việc kích hoạt skill: nút, card, modal, chuyển trang, micro-interaction, loading/success/error, scroll-triggered, nhận diện chuyển động thương hiệu.

## Setup
```bash
# ✅ phần --list chạy được trên clone cục bộ. Lệnh cài từ GitHub ❓ chưa chạy (sandbox chặn)
npx skills add LottieFiles/motion-design-skill
```
README nói hỗ trợ 40+ agent (Claude Code, Cursor, Codex, GitHub Copilot...) qua skills.sh.

## ⚠️ License / Bảo mật / Quyền riêng tư
- MIT, chỉ là markdown, không script, không gọi mạng. **Rủi ro thấp nhất trong cả đợt 11 repo.**

## Ví dụ thực tế (prompt mẫu trong README)
1. "Add a playful entrance animation to these card components"
2. "Create a loading → success → error state transition for this form submit button"
3. "Review my animation code and suggest improvements based on motion design principles", dùng để **review** animation có sẵn của [DỰ ÁN].

## Lưu ý / Lỗi thường gặp
- Skill nghiêng "triết lý" nên không cho API cụ thể. Dùng cùng một skill thư viện (`repos/gsap-skills.md`) để có code đúng.
- Chỉ 4 commit: ổn định hay ít cập nhật chưa phân biệt được.

## Đánh giá cá nhân
**Chưa chấm điểm. Ưu tiên cao để thử đầu tiên:** nhiều sao nhất trong nhóm skill, không script, license sạch, `--list` chạy được ngay, và chất lượng dễ kiểm (đọc `SKILL.md` 5 phút là biết có đáng không). Hạn chế: không thay thế skill dựng video, chỉ nâng chất lượng chuyển động UI.

## Link
- Repo: https://github.com/LottieFiles/motion-design-skill
- Liên quan trong kho: `repos/gsap-skills.md`, `repos/motiondivision-motion.md`, `skills/motion-foundations/`, `skills/motion-patterns/`

---

## 🤖 Agent Integration

> Skill dạng markdown, không có HTTP API.

### Hermes (Python)
```python
# ✅ Đã chạy thật 2026-10-12 trên clone cục bộ: liệt kê skill mà CLI nhận ra.
import subprocess

def list_skills(path: str) -> str:
    return subprocess.run(["npx", "-y", "skills", "add", path, "--list"],
                          capture_output=True, text=True, timeout=120).stdout

# print(list_skills("/path/to/motion-design-skill"))
```

### OpenClaw
```bash
# ❓ chưa chạy từ GitHub
npx skills add LottieFiles/motion-design-skill
```

### Antigravity
```bash
# ❓ chưa chạy
npx -y skills add LottieFiles/motion-design-skill --list
```
> ⚠️ Chỉ cho UI motion. Muốn dựng video thì dùng `repos/product-launch-motion.md` hoặc `repos/hyperframes.md`.

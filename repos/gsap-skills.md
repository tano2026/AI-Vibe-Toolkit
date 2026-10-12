# gsap-skills (greensock) — GitHub Repo

## TL;DR
Bộ skill **chính chủ GreenSock** (MIT) dạy coding agent dùng GSAP đúng cách: 8 skill (core, timeline, ScrollTrigger, plugins, utils, React, performance, frameworks). 14,1k sao. README ghi "GSAP is 100% free — including every plugin", kể cả SplitText, MorphSVG... cho cả mục đích thương mại, sau khi Webflow mua GSAP. **Một lưu ý quan trọng:** gói npm `gsap` có license `Standard 'no charge' license`, **không phải MIT**. Đọc kỹ license đó trước khi nhúng vào sản phẩm bán lại.

## Repo này dùng để làm gì
Tránh việc AI viết GSAP kiểu cũ/sai (tween rời rạc, quên cleanup trong React, dùng sai ScrollTrigger):
| Skill | Nội dung |
|---|---|
| `gsap-core` | `to`, `from`, `fromTo`, easing, duration, stagger |
| `gsap-timeline` | timeline, position parameter, label, lồng nhau |
| `gsap-scrolltrigger` | animation theo cuộn, pin, scrub, refresh |
| `gsap-plugins` | ScrollToPlugin, ScrollSmoother, Flip, Draggable, SplitText, MorphSVG... |
| `gsap-utils` | `gsap.utils` |
| `gsap-react` | hook `useGSAP`, refs, `gsap.context()`, cleanup, SSR |
| `gsap-performance` | tối ưu hiệu năng |
| `gsap-frameworks` | Vue, Svelte, framework khác |

## Số liệu đã kiểm (2026-10-12)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao / Fork | 14,1k / 830 | 📖 trang repo qua fetch, chưa đối chiếu API |
| License repo | MIT | 📖 trang repo |
| License gói `gsap` | **"Standard 'no charge' license"** (https://gsap.com/standard-license) | ✅ `npm view gsap license` |
| Phiên bản `gsap` | 3.15.0 | ✅ `npm view gsap version` |
| Số commit | 24 | 📖 trang repo |
| Commit gần nhất | 2026-04-21 | ✅ `git log` trên bản clone nông |
| CLI `skills` nhận ra | 8 skill | ✅ `npx skills add <clone cục bộ> --list` |

## Đối chiếu với bài post
- "Kỹ năng chính thức của GreenSock": đúng, repo thuộc tổ chức `greensock`.
- "Toàn bộ plugin đỉnh cao của GSAP hiện đã mở miễn phí cho thương mại": đúng theo README (nguyên văn: "free for everyone, including commercial use", nhắc SplitText và MorphSVG làm ví dụ, và plugin cài từ gói npm `gsap` công khai, không cần Club membership hay token). **Nhưng** nó nằm trong "Standard 'no charge' license" có điều khoản riêng, tao chưa đọc toàn văn nên chưa kết luận mọi trường hợp được phép.

## Setup
📖 Theo README, **chưa chạy từ GitHub**:
```bash
npx skills add https://github.com/greensock/gsap-skills
# chỉ định agent:  --agent antigravity
# Claude Code (plugin):
/plugin marketplace add greensock/gsap-skills
# Hoặc copy thư mục skills/ vào ~/.claude/skills/
```

## ⚠️ License / Bảo mật / Quyền riêng tư
- **Đọc https://gsap.com/standard-license trước khi** đưa GSAP vào một sản phẩm/công cụ bán cho người khác (đặc biệt nếu sản phẩm cho người dùng tạo animation). Entry này không thay thế bản license.
- Skill chỉ là tài liệu markdown, không script (✅ danh sách file), rủi ro thấp.

## Ví dụ thực tế
1. Timeline vào cảnh cho hero section của [SẢN PHẨM] với `gsap-timeline` + `gsap-scrolltrigger`.
2. Component React có animation, dọn đúng cách bằng `useGSAP` (`gsap-react`).
3. Nền tảng animation cho video dựng bằng HTML (HyperFrames và product-launch-motion đều dùng GSAP).

## Lưu ý / Lỗi thường gặp
- `gsap-react`: cleanup bằng `gsap.context()`/`useGSAP`, nếu không sẽ rò animation khi unmount.
- Tải GSAP về `vendor/` khi render video để không phụ thuộc mạng (khuyến nghị từ `repos/product-launch-motion.md`).

## Đánh giá cá nhân
**Chưa chấm điểm. Ưu tiên cao trong nhóm web/HTML-video**: chính chủ, nhiều sao, chỉ là tài liệu nên rủi ro thấp, và GSAP là nền của nhiều repo khác trong danh sách. Điểm cần cẩn thận duy nhất là license gói npm.

## Link
- Repo: https://github.com/greensock/gsap-skills
- License: https://gsap.com/standard-license
- Liên quan trong kho: `repos/hyperframes.md`, `repos/product-launch-motion.md`, `repos/taste-skill.md`, `repos/motiondivision-motion.md`

---

## 🤖 Agent Integration

> Skill dạng tài liệu markdown, không có HTTP API.

### Hermes (Python)
```python
# ✅ Đã chạy thật 2026-10-12: lấy version và license của gói gsap từ npm.
import subprocess

def gsap_license() -> str:
    return subprocess.run(["npm", "view", "gsap", "version", "license"],
                          capture_output=True, text=True, timeout=60).stdout.strip()

# print(gsap_license())   # 3.15.0 / Standard 'no charge' license
```

### OpenClaw
```bash
# ❓ chưa chạy từ GitHub
npx skills add https://github.com/greensock/gsap-skills
```

### Antigravity
```bash
# ❓ chưa chạy
npm view gsap version license
```
> ⚠️ Gói `gsap` không phải MIT. Ghi nguồn license trong hợp đồng với khách nếu bán sản phẩm có nhúng GSAP.

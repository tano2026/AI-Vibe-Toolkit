# motion (motiondivision) — GitHub Repo

## TL;DR
Thư viện animation mã nguồn mở **cho giao diện web**, tên cũ là Framer Motion: gói npm `motion` hỗ trợ React, JavaScript thuần, và Vue qua `motion-v`. MIT, 34,0k sao, 8.267 commit, bản npm hiện tại 14.1.0. Đây là **thư viện thật, trưởng thành**, không phải skill: nó không làm video, nó làm hiệu ứng nút bấm, thẻ card, chuyển trang, cuộn trang trong web app. Cảnh báo: "120fps" là lời README về việc dùng API gốc của trình duyệt, tốc độ thật phụ thuộc máy và màn hình.

## Repo này dùng để làm gì
Cho dev web viết animation gọn mà không tự quản lý requestAnimationFrame:
```js
// 📖 ví dụ ngắn nhất trong README (JS thuần), chưa chạy
import { animate } from "motion"
animate("#box", { x: 100 })
```
Cài: `npm install motion` (React/JS), `npm install motion-v` (Vue).

## Số liệu đã kiểm (2026-10-12)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao / Fork | 34,0k / 1,4k | 📖 trang repo qua fetch, chưa đối chiếu API |
| License | MIT | 📖 README "Motion is MIT licensed" + ✅ `npm view motion license` = MIT |
| Phiên bản npm | 14.1.0 | ✅ `npm view motion version` (2026-10-12). `framer-motion` cũng ra 14.1.0 |
| Số commit | 8.267 | 📖 trang repo. Ngày commit gần nhất: **chưa đo** |
| Lượt tải/tháng | **chưa kiểm** | ❓ API downloads của npm bị proxy chặn |

## Đối chiếu với bài post
- "Framer Motion thế hệ mới": đúng, `motion` là gói kế nhiệm và `framer-motion` ra cùng số phiên bản.
- "120fps cho React, Vue và JS thuần": README có chữ "120fps, GPU-accelerated animations" dựa trên API animation gốc của trình duyệt. Đó là **trần lý thuyết**, không phải cam kết. Hiệu năng thật phụ thuộc thiết bị và thuộc tính animate (transform/opacity nhanh, layout chậm).
- "Tối ưu nút bấm, thẻ card, chuyển trang": đúng loại việc, nhưng README không cam kết tối ưu tự động, vẫn phải viết đúng thuộc tính.

## Setup
```bash
npm install motion
```
Thử phiên bản: ✅ `npm view motion version license` chạy được ngay trong sandbox.

## ⚠️ License / Bảo mật / Quyền riêng tư
- Phần miễn phí là MIT. **Motion+** là gói trả phí (450+ ví dụ, 110+ hướng dẫn, API cao cấp, trình chỉnh transition, công cụ AI): mua cá nhân một lần hoặc theo ghế cho nhóm. Đừng nhầm "công cụ AI của Motion+" với skill miễn phí.
- Khi dùng với agent: nhớ kiểm skill nào bạn cài có khớp bản v14 không (xem `repos/motion-dev-animations-skill.md`, bản đó nhắm v11+).

## Ví dụ thực tế
1. Hiệu ứng vào cảnh cho card sản phẩm trên landing page của [SẢN PHẨM].
2. Chuyển trang mượt cho app Next.js của [DỰ ÁN].

## Lưu ý / Lỗi thường gặp
- Chỉ animate `transform`/`opacity` để giữ mượt, tránh animate layout.
- Tôn trọng `prefers-reduced-motion` (tiêu chuẩn truy cập, không phải tuỳ chọn).
- Không phải công cụ dựng video. Muốn video dùng `hyperframes`/`remotion`.

## Đánh giá cá nhân
**Chưa chấm điểm theo kiểu skill** vì đây là thư viện lõi, đủ độ phổ biến để tin (34k sao, MIT, phiên bản mới). Điểm yếu duy nhất đáng nhắc: nó là web UI, nên đừng kỳ vọng thay thế bộ dựng video. Dùng khi mày viết giao diện React/Next/Vue và cần animation đàng hoàng.

## Link
- Repo: https://github.com/motiondivision/motion
- Liên quan trong kho: `repos/gsap-skills.md`, `repos/motion-dev-animations-skill.md`, `repos/lottiefiles-motion-design-skill.md`, `skills/motion-ui/`

---

## 🤖 Agent Integration

> Thư viện JavaScript chạy trong trình duyệt, không có HTTP API. Phần dưới chỉ kiểm phiên bản.

### Hermes (Python)
```python
# ✅ Đã chạy thật 2026-10-12: trả về version và license mới nhất từ npm.
import subprocess

def npm_info(pkg: str = "motion") -> str:
    return subprocess.run(["npm", "view", pkg, "version", "license"],
                          capture_output=True, text=True, timeout=60).stdout.strip()

# print(npm_info())   # ví dụ: version = '14.1.0' / license = 'MIT'
```

### OpenClaw
```bash
# ❓ chưa chạy trong dự án thật
npm install motion
```

### Antigravity
```bash
# ❓ chưa chạy
npm view motion version license
```
> ⚠️ Số lượt tải/tháng chưa kiểm được, đừng trích trong video.

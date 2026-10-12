# claude-motion (whaleyxbt) — GitHub Repo

## TL;DR
Bộ công cụ motion cho coding agent của `whaleyxbt` (MIT). Khác các repo "dạy API Remotion": cái này dạy Claude **gu thẩm mỹ bằng con số** (easing, spring, khoảng cách chữ), bắt nó **tự xem lại khung hình** bằng contact sheet, kèm **sound engine Python thuần** (không sample, tự master -14 LUFS) và đường dẫn thứ hai render **mô phỏng web (three.js) ra video 60 fps**. 0 sao, 8 commit. **Cảnh báo:** phần Remotion dính license công ty, và con số "340K views" trong README là lượt xem video trên X, không phải độ phổ biến của repo.

## Repo này dùng để làm gì
Hai pipeline:
1. **Remotion (React)**: motion graphic 15–22 giây, có ví dụ `examples/01-effort/`.
2. **`sims/` (HTML + three.js + headless Chromium → ffmpeg)**: mô phỏng (256 agent bò trên tường website, truy vết một username thành hồ sơ, động cơ tên lửa camera bay xuyên). Mỗi piece là **một file HTML** chạy offline, `render(t)` là hàm thuần theo thời gian, capture 60 fps 1440×1800.

4 skill trong `.claude/skills/`: `motion-design`, `review-loop`, `sound-design`, `web-sims`.

## Số liệu đã kiểm (2026-10-12)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao / Fork | 0 / 1 | 📖 trang repo qua fetch, đã hỏi lại 2 lần cho khớp tên repo |
| License | MIT (code). Remotion có license riêng | 📖 README |
| Số commit | 8 | 📖 trang repo |
| Commit gần nhất | 2026-10-09 | ✅ `git log` trên bản clone nông |
| CLI `skills` nhận ra | 4 skill | ✅ `npx skills add <clone cục bộ> --list` |

## Đối chiếu với bài post
- "Ép AI tự soi lại từng khung hình": đúng cơ chế, README giải thích agent không xem được video nhưng xem được khung, nên render nháp → contact sheet có mốc thời gian mỗi beat → kiểm danh sách (va chạm, bị cắt, thời gian giữ, vùng an toàn, đọc được trên điện thoại).
- "Render mô phỏng 60fps mượt mà": đúng cho `sims/`, capture từng khung nên 60 fps bất kể khung nào chậm bao nhiêu. Mượt trên video, **không** có nghĩa preview live mượt.
- "Tích hợp sound engine": đúng, Python stdlib, không sample, không license âm thanh.

## Setup
📖 Theo README, **chưa chạy**:
```bash
git clone https://github.com/whaleyxbt/claude-motion && cd claude-motion
npm install
npm run build          # ví dụ có tiếng → out/effort.mp4
npm run studio         # preview live (Remotion)
# sims:
npx playwright install chromium
npm run sims
npm run capture -- engine --size 1080x1350 --out out/engine.mp4
```
Cần Node 20+, Python 3, ffmpeg.

## ⚠️ License / Bảo mật / Quyền riêng tư
- **Remotion:** README ghi miễn phí cho cá nhân và nhóm nhỏ, công ty trên ngưỡng cần license công ty (xem `repos/remotion.md`). Phần `sims/` theo README là pipeline thứ hai không đi qua Remotion. Chưa kiểm sâu code.
- Ví dụ có thể nhắc tới tên thật (website, username). Không dùng lại các ví dụ "truy vết một username" cho người thật; chỉ học kỹ thuật.

## Ví dụ thực tế
1. Motion graphic 15 giây 1080×1080 thông báo [TÍNH NĂNG MỚI].
2. Mô phỏng 20 giây "[QUY TRÌNH] chạy song song" dưới dạng đàn agent, bản 1080×1350.

## Lưu ý / Lỗi thường gặp (theo chính README)
- Mọi mốc là timestamp có tên trong một file JSON, nên đổi nhịp video thì âm thanh và bước kiểm đổi theo.
- Hệ thống Chromium tại `/usr/bin/chromium` được dùng nếu có, không thì Remotion tải về lần đầu.
- Khuyến nghị đi cùng skill chính thức của Remotion để có đủ API, repo này chỉ là lớp thiết kế.

## Đánh giá cá nhân
**Chưa chấm điểm.** Điểm mạnh: ý tưởng "luật có số + vòng tự xem khung + sound engine" gọn, `sims/` là khả năng độc nhất trong nhóm. Điểm yếu: 0 sao, chưa ai kiểm, nặng tính "demo viral". Dùng `sound-design` và `review-loop` như **lớp thiết kế** đặt lên engine khác là hợp lý hơn dùng cả bộ.

## Link
- Repo: https://github.com/whaleyxbt/claude-motion
- Liên quan trong kho: `repos/remotion.md`, `repos/claude-remotion-skill.md`, `repos/ffmpeg.md`, `stacks/motion-design-studio-claude-code.md`

---

## 🤖 Agent Integration

> Bộ skill + script, không có HTTP API.

### Hermes (Python)
```python
# ✅ Hàm đã chạy thật 2026-10-12.
import shutil

def check_env(tools=("node", "python3", "ffmpeg")) -> dict:
    return {t: bool(shutil.which(t)) for t in tools}
```

### OpenClaw
```bash
# ❓ chưa chạy
git clone https://github.com/whaleyxbt/claude-motion && cd claude-motion && npm install
```

### Antigravity
```bash
# ❓ chưa chạy
npx playwright install chromium
npm run sims
```
> ⚠️ Render 60 fps 1440×1800 từng khung tốn CPU/RAM. Chạy thử ở kích thước nhỏ (`--size 540x675`) trước.

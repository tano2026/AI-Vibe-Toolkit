# claude-remotion-skill (haidrrrry) — GitHub Repo

## TL;DR
Một skill Claude Code của `haidrrrry` (MIT) cho **Remotion**: mười luật motion "không thương lượng" (spring + bezier thay vì nội suy tuyến tính, vào cảnh 3 thuộc tính, stagger 3–6 khung, nền gradient + grain + vignette, Ken Burns cho ảnh tĩnh) cộng vòng bắt buộc **render → trích khung → xem → sửa → render lại**. 245 sao. **Cảnh báo:** README viết kiểu SEO/quảng cáo ("dứt điểm" mọi lỗi AI video), chồng chéo mạnh với skill chính thức của Remotion và `claude-motion`, và vẫn dính license công ty của Remotion.

## Repo này dùng để làm gì
Dạy Claude dựng motion graphics, reel/Shorts, caption chạy chữ, kinetic typography bằng Remotion mà không ra kiểu "fade lẻ + chuyển động tuyến tính":
- `remotion-motion-graphics/SKILL.md` (workflow + luật),
- `references/` (mẫu motion, luật thiết kế), `assets/theme.ts`,
- `examples/` (React/TS: CTA, Hook, FocusCat, CodeEdit, SkillPromo...).

## Số liệu đã kiểm (2026-10-12)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao / Fork | 245 / 25 | 📖 trang repo qua fetch, đã hỏi lại cho khớp tên repo |
| License | MIT | 📖 trang repo |
| Số commit | 9 | 📖 trang repo |
| Commit gần nhất | 2026-08-12 | ✅ `git log` trên bản clone nông |
| CLI `skills` nhận ra | 1 skill (`remotion-motion-graphics`) | ✅ `npx skills add <clone cục bộ> --list` |

## Đối chiếu với bài post
Post: "Trị dứt điểm lỗi chuyển cảnh mờ mờ và chuyển động đơ cứng cố hữu của video AI". README nói gì thật: bảng đối chiếu "không có skill / có skill" (nội suy tuyến tính → spring, fade lẻ → vào cảnh 3 thuộc tính, mọi thứ vào cùng lúc → stagger, nền phẳng → nền nhiều lớp, ảnh tĩnh → Ken Burns, render mù → trích khung bằng ffmpeg để xem). Đó là luật cụ thể, **nhưng "dứt điểm" là lời quảng cáo**, chưa có thử nghiệm đối chứng. Lỗi "chuyển cảnh mờ" không được README nêu tên.

## Setup
📖 Theo README, **chưa chạy**:
```bash
# Cài như một skill Claude Code (README có script build-skill.sh để đóng gói)
npx skills add haidrrrry/claude-remotion-skill
```
Cần Remotion (React + TypeScript) và Claude Code/Desktop. README nói model-agnostic (Sonnet hoặc Opus).

## ⚠️ License / Bảo mật / Quyền riêng tư
- Code skill MIT, nhưng **Remotion** có license riêng: theo `repos/remotion.md`, công ty 4+ người cần license thương mại. Kiểm lại trang license của Remotion trước khi dùng cho khách.
- `scripts/build-skill.sh`: chưa đọc kỹ, chưa chạy.

## Ví dụ thực tế
1. Reel 9:16 giới thiệu [SẢN PHẨM] với caption chạy chữ khớp lời.
2. Lower third + intro logo 5 giây cho video của [KÊNH].

## Lưu ý / Lỗi thường gặp
- Chồng chéo với: skill chính thức `remotion-dev/skills` (đã có trong `repos/remotion.md`), `repos/remotion-superpowers.md`, `repos/claude-motion.md`. **Cài một lớp "design" thôi**, đừng cài cả ba (ăn context).
- Nội dung README dài và lặp từ khoá SEO, đọc SKILL.md và `references/` mới là phần có giá trị.

## Đánh giá cá nhân
**Chưa chấm điểm.** Điểm mạnh: luật cụ thể, vòng tự kiểm bằng khung hình. Điểm yếu: chồng chéo cao, quảng cáo nặng, chưa chạy, buộc dùng Remotion (license). **Ưu tiên thấp**: nếu đã chọn Remotion thì dùng skill chính thức + lớp design của `claude-motion`; nếu muốn né license thì đi HyperFrames.

## Link
- Repo: https://github.com/haidrrrry/claude-remotion-skill
- Liên quan trong kho: `repos/remotion.md`, `repos/remotion-superpowers.md`, `repos/claude-motion.md`, `skills/remotion-skill/`

---

## 🤖 Agent Integration

> Skill dạng prompt cho Claude Code, không có HTTP API.

### Hermes (Python)
```python
# ✅ Hàm đã chạy thật 2026-10-12.
import shutil

def check_env(tools=("node", "npx", "ffmpeg")) -> dict:
    return {t: bool(shutil.which(t)) for t in tools}
```

### OpenClaw
```bash
# ❓ chưa chạy từ GitHub
npx skills add haidrrrry/claude-remotion-skill
```

### Antigravity
```bash
# ❓ chưa chạy
node --version
ffmpeg -version | head -1
```
> ⚠️ Kiểm license Remotion trước khi render sản phẩm cho khách.

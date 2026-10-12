# product-launch-motion — GitHub Repo

## TL;DR
Skill Claude Code của `AbubakrChan` (MIT) dạy Claude **đạo diễn** một video launch sản phẩm khoảng 45 giây bằng HTML + CSS + GSAP, render từng khung ra MP4 (mặc định qua HyperFrames, chạy được với Remotion). Không phải "quẳng link là xong": nó viết 3 hướng hình ảnh rồi bỏ 2, cần voiceover trước, rồi mới dựng từng cảnh. **Cảnh báo lớn nhất:** repo mới (1 sao, 11 commit), phần "evals" do chính tác giả tự chạy, và tao chưa chạy thử lần nào.

## Repo này dùng để làm gì
Cho Claude một quy trình 14 bước để ra video launch có "chất đạo diễn" thay vì slideshow có hiệu ứng:
1. Viết brief (sản phẩm, người xem, một claim duy nhất).
2. Viết 3 hướng nhìn khác nhau, giết 2 hướng.
3. Có voiceover trước, độ dài từng cảnh lấy theo bản thu thật.
4. Lấy thời điểm từng từ (word timings) để mỗi hiệu ứng rơi đúng từ mô tả nó.
5. Dựng mỗi cảnh là một file HTML có sẵn camera rig + con trỏ chuột.
6. Ghép phim, render, master âm lượng, rồi đo xem âm thanh có thật sự nghe được không.

## Số liệu đã kiểm (2026-10-12)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao / Fork | 1 / 0 | 📖 trang repo qua fetch, chưa đối chiếu API |
| License | MIT | 📖 trang repo |
| Số commit | 11 | 📖 trang repo |
| Commit gần nhất | 2026-08-27 | ✅ `git log` trên bản clone nông |
| Nội dung | 12 tài liệu tham chiếu, 8 script, 5 template, bộ evals | ✅ liệt kê file trong clone |
| CLI `skills` nhận ra | 1 skill (`product-launch-motion`) | ✅ `npx skills add <clone cục bộ> --list` |

## Đối chiếu với bài post
| Bài post nói | README thật nói | Kết luận |
|---|---|---|
| "Chỉ cần đưa link hoặc ảnh sản phẩm" | Ví dụ prompt: "Make a 45-second launch video for my product at example.com", nhưng skill "will ask you the things it needs" và có bước brief + chọn hướng | Đúng một phần: nó hỏi lại, không tự chạy một mạch |
| "Lồng tiếng khớp từng từ" | Hiệu ứng được gắn theo thời điểm từng từ lấy từ transcript. Giọng đọc là model local miễn phí, giọng của mày, hoặc TTS mày đang trả tiền | Đúng một phần: skill **không có giọng riêng**, mày phải mang TTS |
| "Lia camera 3D, cân màu điện ảnh" | Có camera rig, script `wire-grade.mjs`, `master.sh` | Có trong repo, chưa chạy nên chưa biết đẹp tới đâu |

## Setup
📖 Theo README, **chưa chạy từ GitHub** (sandbox chặn `api.github.com`):
```bash
npx skills add AbubakrChan/product-launch-motion
```
Rồi mở Claude Code và nói: "Make a 45-second launch video for [SẢN PHẨM] at [URL]".

Cần: Node ≥ 20, FFmpeg, một renderer (HyperFrames mặc định, Remotion cũng được). GSAP nên tải về thư mục `vendor/` để render không phụ thuộc mạng. Python 3.10+ và Whisper chỉ cần nếu muốn TTS offline / lấy word timings.

## ⚠️ License / Bảo mật / Quyền riêng tư
- File `NOTICE` nói rõ: MIT chỉ phủ phần tác giả viết (SKILL.md, references, scripts, assets, evals, văn bản README). **Phim mẫu và ảnh still là của công ty được làm phim cho**, không có quyền dùng lại.
- GSAP trên npm có license `Standard 'no charge' license`, **không phải MIT** (✅ `npm view gsap license`, 2026-10-12). Xem `repos/gsap-skills.md` trước khi nhúng vào sản phẩm bán cho khách.
- Nếu chọn Remotion làm renderer: xem `repos/remotion.md` (công ty đủ lớn cần license thương mại). Chọn HyperFrames để tránh.

## Ví dụ thực tế
1. Video 45 giây giới thiệu [SẢN PHẨM/ƯU ĐÃI] cho một khách của agency: brief 1 trang, voiceover 1 bản, 11 cảnh.
2. Video launch tính năng mới cho SaaS của chính mày: dùng ảnh chụp UI thật làm cảnh, không vẽ lại.

## Lưu ý / Lỗi thường gặp (theo chính README)
- README tự liệt kê **34 cái bẫy**, mỗi cái kèm phép đo. Ví dụ: tiếng gõ phím thêm vào nhưng nhỏ hơn voiceover khoảng 20 dB nên thực tế không nghe được. `verify-cue.sh` có để kiểm.
- Thứ tự ghép phim cố định: `assemble` → `transitions` → `wire-audio` → `wire-grade`. Đảo thứ tự là hỏng.
- Dựng 11 cảnh nhiều bước = tốn token, chưa có số đo.

## Đánh giá cá nhân
**Chưa chấm điểm.** Điểm mạnh: nặng về "đạo diễn và đo đạc" chứ không chỉ API, có file `CASE-STUDY.md` ghi từng vòng sửa. Điểm yếu: 1 sao, một tác giả, bản eval tự công bố chưa ai kiểm lại, phải tự lo giọng đọc. Nếu đã dùng HyperFrames trong kho thì đây là skill launch-video **nên thử đầu tiên** trong nhóm (trước `claude-motion-design` và `motion-graphics-skills`), thử đúng một brief ngắn rồi đo thời gian và token.

## Link
- Repo: https://github.com/AbubakrChan/product-launch-motion
- Renderer: https://github.com/heygen-com/hyperframes
- Liên quan trong kho: `repos/hyperframes.md`, `repos/motion-graphics-skills.md`, `repos/claude-motion-design.md`, `repos/gsap-skills.md`, `stacks/motion-design-studio-claude-code.md`

---

## 🤖 Agent Integration

> Skill dạng prompt cho Claude Code, không có HTTP API. Phần dưới chỉ kiểm điều kiện chạy.

### Hermes (Python)
```python
# ✅ Hàm này đã chạy thật 2026-10-12 trên sandbox: ffmpeg, ffprobe, node, npx, python3 đều có.
import shutil

def check_env(tools=("node", "npx", "ffmpeg", "ffprobe", "python3")) -> dict:
    return {t: bool(shutil.which(t)) for t in tools}

# print(check_env())   # thiếu ffmpeg thì bước master/verify-cue không chạy được
```

### OpenClaw
```bash
# ❓ chưa chạy từ GitHub. Phần --list trên clone cục bộ đã chạy ✅.
npx skills add AbubakrChan/product-launch-motion
npx skills add heygen-com/hyperframes
```

### Antigravity
```bash
# ❓ chưa chạy. Chỉ kiểm điều kiện.
node --version   # cần >= 20
ffmpeg -version | head -1
```
> ⚠️ README tác giả dùng phim mẫu của bên thứ ba. Đừng copy ảnh/phim mẫu vào sản phẩm của khách.

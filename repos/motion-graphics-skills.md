# motion-graphics-skills — GitHub Repo

## TL;DR
13 skill cho Claude Code của Charlie Hills (`charlie947`) để dựng motion graphics "launch-grade" hoàn toàn bằng code, không After Effects, không công cụ sinh video: video giới thiệu sản phẩm, biểu đồ chuyển động, explainer, loop GIF, xuất Reels/TikTok. License MIT. **Cảnh báo lớn nhất:** repo rất nhỏ (9 sao) và README yêu cầu chạy trên **Opus 5.5**, nên tao chưa chạy thử skill nào, mọi đánh giá bên dưới chỉ là đọc README.

## Repo này dùng để làm gì
Cho Claude biết quy trình dựng video chuyển động theo đúng thương hiệu:
1. Chạy `brand-intake` trước, ra `brand.md` + `MOTION.md` (màu, font, logo, giọng chuyển động).
2. Các skill khác đọc hai file đó rồi dựng.
3. Ra HTML có `window.seek()`, rồi xuất MP4 bằng HyperFrames (hoặc ffmpeg + Chrome).

Hợp với việc làm video ngắn cho social, đặc biệt khi đã có HyperFrames trong kho (`repos/hyperframes.md`).

## Số liệu đã kiểm (2026-10-10)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao | 9 | 📖 trang repo qua fetch, chưa đối chiếu bằng API |
| Fork | 1 | 📖 cùng nguồn |
| License | MIT | 📖 trang repo + README |
| Số commit | 22 | 📖 trang repo |
| Số skill | 13 | 📖 README |
| Commit gần nhất | **chưa đo** | ❓ |

Lưu ý: infographic mày gửi ghi **112 sao**, còn trang repo tao đọc ra **9 sao**. Hai con số lệch nhiều. Tao tin số đọc từ trang repo hơn, nhưng chưa đối chiếu bằng API. Có thể infographic chụp lúc khác hoặc lẫn repo khác, kiểm lại trước khi trích.

13 skill (📖 README):
`brand-intake`, `motion-brief-writer`, `launch-video`, `apple-launch-film`, `vox-explainer`, `animated-chart`, `milestone-reveal`, `motion-effects`, `title-sequence-3d`, `model-showdown`, `newsletter-promo`, `loop-cover`, `reel-export`.

## Setup
📖 Theo README, **chưa chạy**:
```bash
# Cài nhanh
npx skills add charlie947/motion-graphics-skills

# Export MP4: cài HyperFrames một lần (miễn phí, mã nguồn mở)
npx skills add heygen-com/hyperframes
```
Rồi mở Claude Code, chọn model bằng `/model` và chạy `brand-intake` **đầu tiên**.

Yêu cầu theo README:
| Việc | Cần |
|---|---|
| Dựng animation | Claude Code trên Opus 5.5 |
| Xuất MP4 | HyperFrames, hoặc ffmpeg + Chrome |
| `loop-cover` | ffmpeg + Python 3 |
| `reel-export`, `model-showdown` | ffmpeg + ffprobe |
| `model-showdown` | tài khoản truy cập từng model |
| `apple-launch-film` | skill `apple-design` của tác giả khác (tuỳ chọn) |

README ghi **không cần API key** cho phần dựng.

## ⚠️ License / Bảo mật / Quyền riêng tư
- MIT. Tác giả xin (không bắt buộc) ghi link về newsletter của ông ấy.
- README nhắc một "export kit" lưu trên Google Drive của tác giả. Tao **chưa kiểm** file đó, đừng tải rồi chạy khi chưa đọc.
- Skill được thiết kế dùng logo và ảnh chụp **thật**, không vẽ lại logo từ trí nhớ. Hợp với quy tắc không dựng logo giả.

## Ví dụ thực tế
1. **Video giới thiệu 30–45 giây** cho một sản phẩm/ưu đãi: `brand-intake` một lần, rồi `launch-video`.
2. **Biểu đồ chuyển động** giữ nguyên số liệu như đã nhập (README nói skill không đổi giá trị): `animated-chart`.
3. **Cắt bản dọc cho TikTok/Reels:** `reel-export` ra 1080x1920 (phần ffmpeg bên dưới đã kiểm, xem `repos/ffmpeg.md`).

## Lưu ý / Lỗi thường gặp (theo chính README)
- Không có `brand.md` và `MOTION.md` thì skill hỏi mã màu, font, logo và không gọi kết quả là "đúng thương hiệu".
- Thiếu công cụ export thì chỉ ra HTML, việc xuất MP4 bị treo ở trạng thái "pending".
- `loop-cover` cần ffmpeg + Python để đo chỗ nối vòng lặp, thiếu thì không dám nói là xong.
- Khuôn mặt người thật cần model ảnh riêng, README tự gọi đây là "giới hạn thành thật".
- `model-showdown` chỉ so được các model mày có quyền dùng.

## Đánh giá cá nhân
**Chưa chấm điểm.** Chưa chạy skill nào, và repo mới, nhỏ, một tác giả. Điểm đáng chú ý: README viết thẳng điều kiện "thiếu X thì ra Y, không gọi là xong", cách nói trung thực hơn đa số repo cùng loại. Điểm yếu: yêu cầu Opus 5.5 (đắt hơn), tồn tại chồng chéo với `hyperframes` và `remotion` đã có trong kho, và cộng đồng gần như chưa có (9 sao). Nên thử đúng một skill (`launch-video` hoặc `reel-export`) trước khi tin cả bộ.

## Link
- Repo: https://github.com/charlie947/motion-graphics-skills
- HyperFrames: https://github.com/heygen-com/hyperframes
- Liên quan trong kho: `repos/hyperframes.md`, `repos/remotion.md`, `repos/ffmpeg.md`

---

## 🤖 Agent Integration

> Đây là skill dạng prompt cho Claude Code, không có HTTP API. Phần dưới chỉ kiểm điều kiện để chạy và gọi bước export.

### Hermes (Python)
```python
# ✅ Hàm check_motion_env đã chạy thật 2026-10-10 (ffmpeg, ffprobe, npx đều có). Lệnh `npx skills add` chưa chạy (❓).
import shutil

def check_motion_env() -> dict:
    return {
        "ffmpeg": bool(shutil.which("ffmpeg")),
        "ffprobe": bool(shutil.which("ffprobe")),
        "node/npx": bool(shutil.which("npx")),
    }

# print(check_motion_env())   # thiếu cái nào thì skill tương ứng báo "pending"
```

### OpenClaw
```bash
npx skills add charlie947/motion-graphics-skills
npx skills add heygen-com/hyperframes
```

### Antigravity
```bash
# ❓ chưa chạy. Kiểm điều kiện export, không cài thứ gì ngoài danh sách README.
ffmpeg -version | head -1
ffprobe -version | head -1
python3 --version
node --version
```
> ⚠️ README yêu cầu Opus 5.5 để dựng. Chạy bằng model rẻ hơn sẽ khác kết quả tác giả mô tả. Đừng coi bản demo của tác giả là thứ chắc chắn lặp lại được.

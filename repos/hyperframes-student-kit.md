# hyperframes-student-kit — GitHub Repo

## TL;DR
Bộ dựng video cho Claude Code/Codex của Nate Herk (`nateherkai`): đưa **video quay sẵn** vào, nó cắt khoảng lặng, đề xuất các đoạn nói vấp để mày duyệt, lên kế hoạch kể chuyện và chèn motion graphics bằng HyperFrames + GSAP. README ghi 15 skill, **406 thẻ motion graphics bản nháp** (draft) trong 2 style. 527 sao, thuộc nhóm đông nhất trong đợt này. **Cảnh báo:** transcribe mặc định dùng ElevenLabs Scribe (trả phí, footage của mày đi ra ngoài), và đây là "agent-guided workflow", README tự dặn phải xem lại hình và tiếng trước khi đăng.

## Repo này dùng để làm gì
Hậu kỳ video nói chuyện (talking head, hướng dẫn, reel):
- `cut-silences`: cắt khoảng lặng (dead air).
- `cut-mistakes`: tìm đoạn vấp, **cho mày xem danh sách cắt trước**, rồi mới render bản đã duyệt.
- `video-storytelling`, `short-form-edit`: lên hook/payoff, caption chính xác, B-roll chuyển động, dựng bản dọc 9:16.
- `style-library`: 406 thẻ nháp (graph paper tối, kính mờ popout) có CSS token, có ô sửa được.
- `motion-showreel`: showreel 15 giây theo lưới nhịp.

## Số liệu đã kiểm (2026-10-12)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao / Fork | 527 / 193 | 📖 trang repo qua fetch, đã hỏi lại 2 lần cho khớp |
| License | MIT (c) 2026 Nate Herk + "Student Kit Use Permission" | ✅ đọc file `LICENSE` và `licenses/` trong clone |
| Số commit | 1 (trên trang) | 📖 |
| Commit gần nhất | 2026-09-28 | ✅ `git log` trên bản clone nông |
| Số skill | 15 thư mục trong `.claude/skills/` | ✅ liệt kê file. CLI `skills --list` chỉ ra 9 (chưa giải thích chênh lệch) |

## Setup
📖 Theo README, **chưa chạy**:
```bash
git clone https://github.com/nateherkai/hyperframes-student-kit.git
cd hyperframes-student-kit
npm ci && npm run setup && npm test
npm run demo   # ví dụ 8 giây, không cần footage hay API key
```
Cần Node **22+**, Git, FFmpeg (kèm ffprobe), Chrome/Chromium. Trong Claude Code: `/edit-video`, `/short-form-edit`, `/motion-showreel`.

## ⚠️ License / Bảo mật / Quyền riêng tư
- **Footage thô và transcript:** transcribe mặc định qua ElevenLabs Scribe, tạo video/ảnh qua Kie.ai (cả hai trả phí, key riêng). Video có thông tin khách hàng hoặc nội bộ thì dùng Whisper local hoặc transcript có sẵn (README cho phép).
- "Student Kit Use Permission": cho dùng, sửa, chia sẻ code/template/tài liệu của kit và dùng để làm video cá nhân hoặc thương mại, giữ nguyên notice.
- **Logo, brand guideline, media ví dụ của tác giả (bộ "AIS") không có quyền dùng lại** (file `THIRD_PARTY_NOTICES.md` ghi rõ). Đừng đem nguyên vào video của khách.
- HyperFrames bundled theo Apache-2.0 (kèm file license). GSAP cài từ npm theo license riêng (xem `repos/gsap-skills.md`).

## Ví dụ thực tế
1. Video hướng dẫn 10 phút: cắt lặng + duyệt đoạn vấp, ra bản draft để dựng tiếp.
2. Cắt một đoạn quay dài thành 3 reel 9:16, mỗi reel có hook và caption bám lời.

## Lưu ý / Lỗi thường gặp (theo chính README)
- "406 mẫu" là **draft**, không phải mẫu đã kiểm duyệt.
- Có `scripts/validate-beat-sync.mjs` kiểm khớp nhịp, nhưng README vẫn dặn xem lại thật.
- Bản demo dùng GSAP local, HyperFrames có thể tải font thay thế ở lần render đầu.

## Đánh giá cá nhân
**Chưa chấm điểm.** Điểm mạnh: là repo duy nhất trong nhóm xử lý **footage quay thật**, có bước duyệt trước khi cắt, có starter không cần key để thử. Điểm yếu: phụ thuộc dịch vụ trả phí cho transcribe/gen, kit gắn với brand của tác giả (dọn tài sản AIS trước khi dùng), chưa chạy. Nếu mày hay quay talking head thì đây là **repo ưu tiên số 2 để thử** (sau skill launch video), thử trên 1 clip ngắn không nhạy cảm.

## Link
- Repo: https://github.com/nateherkai/hyperframes-student-kit
- HyperFrames: https://github.com/heygen-com/hyperframes
- Liên quan trong kho: `repos/hyperframes.md`, `repos/ffmpeg.md`, `repos/whisper.md`, `repos/elevenlabs-skills.md`

---

## 🤖 Agent Integration

> Pipeline dạng skill + script Node, không có HTTP API.

### Hermes (Python)
```python
# ✅ Hàm đã chạy thật 2026-10-12. Kit cần Node 22+; sandbox này có node nhưng chưa kiểm số phiên bản trong hàm.
import shutil, subprocess

def check_env() -> dict:
    out = {t: bool(shutil.which(t)) for t in ("node", "npm", "ffmpeg", "ffprobe", "git")}
    if out["node"]:
        out["node_version"] = subprocess.run(["node", "--version"], capture_output=True, text=True).stdout.strip()
    return out
```

### OpenClaw
```bash
# ❓ chưa chạy
git clone https://github.com/nateherkai/hyperframes-student-kit.git
cd hyperframes-student-kit && npm ci && npm run setup && npm test
```

### Antigravity
```bash
# ❓ chưa chạy. Chỉ kiểm điều kiện.
node --version   # cần >= 22
ffmpeg -version | head -1
```
> ⚠️ Không đưa footage của khách vào ElevenLabs/Kie.ai khi chưa có đồng ý. Dùng Whisper local.

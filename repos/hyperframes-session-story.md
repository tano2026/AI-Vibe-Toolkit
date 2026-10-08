# hyperframes-community-skills / session-story — GitHub Repo

## TL;DR
Skill của cộng đồng HyperFrames (HeyGen), tác giả Jake Moran, commit mới nhất 24/09/2026: agent **đọc lịch sử chat cục bộ của chính nó với bạn** (Claude Code / Codex), chọn một phiên "điển hình" rồi dựng phim hoạt hình 40–70 giây — lời bạn bay vào như máy bay giấy, lời sửa là cái búa cartoon, lời khen là con bướm, agent tự soạn nhạc phối khí. Vui, có ý tưởng, nhưng là **đồ chơi cá nhân, không phải công cụ sản xuất** — và **chạm vào dữ liệu nhạy cảm**.

## Repo này dùng để làm gì
Repo `heygen-com/hyperframes-community-skills` (Apache-2.0) là kho skill lẻ quanh HyperFrames: ngoài `session-story` còn `day-in-my-life`, `vox-explainer` (explainer 60–90 giây), `p5-paint-animation`, `camera-3d-captions`, `duo`, `prod-by-claude`. Mỗi thư mục trong `skills/` cài độc lập. `session-story` là cái prompt-motion.com giới thiệu.

## Số liệu đã kiểm (08/10/2026, đọc bản clone nông)
- Repo: Apache-2.0; `session-story` kéo thêm p5 2.3.3 (LGPL-2.1), p5.brush (MIT), font Permanent Marker (Apache-2.0) qua `npm ci` có khoá lockfile
- README repo tự cảnh báo: skill cộng đồng KHÔNG thuộc bản HyperFrames được duyệt; skill có thể bảo agent chạy lệnh, đọc file, gọi mạng, tiêu tiền → phải đọc SKILL.md và script trước
- Số sao: **chưa đo**. Chưa chạy `harvest.py` trên dữ liệu thật (chưa có lịch sử Claude Code nào để đọc trong sandbox này)

## Setup
```bash
npx skills add heygen-com/hyperframes-community-skills --skill session-story
sh scripts/setup.sh        # chạy tay 1 lần: npm ci từ lockfile
```
Cần: Node 22+, Python 3.9+ (chỉ stdlib), ffmpeg, HyperFrames CLI ghim `0.8.71` (npx tải lần đầu). Nhạc: macOS dùng `swift` (bank General MIDI có sẵn của Apple); Linux dùng `fluidsynth` + soundfont General MIDI tự cung cấp (biến `SOUNDFONT`).

## ⚠️ Quyền riêng tư — phần quan trọng nhất
Theo chính SKILL.md, skill này:
- **Đọc** `~/.claude/projects/<dự án>/*.jsonl` (Claude Code) và `~/.codex/sessions` (Codex) — nguyên văn lời bạn gõ; chỉ làm sau khi hỏi bạn "có". `--all-projects` đọc toàn bộ
- **Ghi** `session-story-candidates.json` và thư mục dự án — đều chứa lời bạn: **không commit, không chia sẻ**
- **Mạng khi build: không có** — NHƯNG nếu có biến `GEMINI_API_KEY`, lệnh `snapshot` gửi khung hình (chứa lời bạn) sang Gemini, trừ khi truyền `--describe false`. Skill dặn truyền cờ này; agent phải làm đúng
- Có cổng duyệt: lập bảng mọi dòng sẽ lên màn hình + nguồn; chưa `"approved": true` thì mỗi khung có dấu DRAFT
- `harvest.py` có gắn cờ `secret/email/path/url/name?/person?` cho từng tin nhắn, nhưng tự thừa nhận "bỏ sót tên viết thường" → phải đọc từng dòng bằng mắt

**Quy tắc cho kho này**: KHÔNG chạy trên phiên làm việc ABTRIP có dữ liệu khách/PNR/hợp đồng PVN, và KHÔNG chạy trên thư mục dự án chứa token. Nếu muốn thử, dùng dự án sạch hoặc dán tay vài tin nhắn mẫu (skill cho phép).

## Ví dụ thực tế
Dùng đúng cách: làm 1 clip ~50 giây "một buổi làm việc của Tan với Claude" cho kênh Tano — từ một phiên trong dự án kho này **sau khi lọc**: bỏ mọi dòng có token, tên khách, số liệu ABTRIP. Mày duyệt bảng từng dòng, đồng ý rồi mới render. Đầu ra: `renders/session-story.mp4` (24 fps, CRF 12). Giá trị: nội dung "behind the scenes vibe coding" cho personal brand, không phải nội dung bán hàng.

## Lưu ý / Lỗi thường gặp
- Chỉ đọc được lịch sử **Claude Code và Codex**. Hermes / OpenClaw / DeepSeek Harness / Antigravity không được hỗ trợ sẵn (phải tự dựng cùng định dạng — `references/sources.md`)
- **Claude Code trên máy Windows của mày chưa chạy được** → chưa có lịch sử để harvest. Skill gần như không dùng được lúc này
- Đây là skill của agent: phải có agent thật sự nói chuyện với bạn đủ lâu mới có "phiên điển hình"
- Nhạc trên Linux cần soundfont tự kiếm; chưa kiểm chất lượng
- Chưa chạy thử lần nào. Lệnh `schedule.mjs` cần thư mục dự án có `story.json` (tạo bằng `new-project.mjs`)

## Đánh giá cá nhân
- Điểm mạnh: ý tưởng kể chuyện hay, có cổng duyệt quyền riêng tư và danh sách tác dụng phụ viết rõ ràng, trích dẫn nguyên văn không bịa, lockfile ghim phiên bản
- Điểm yếu: rủi ro dữ liệu cao nếu agent bất cẩn, phụ thuộc lịch sử Claude Code/Codex, nhạc Linux phức tạp, mục đích hẹp (phim về chính bạn)
- Có nên dùng: 3/10 cho công việc của mày lúc này. Để dành làm nội dung cá nhân Tano khi Claude Code chạy ổn và có dự án sạch. Cái đáng tham khảo hơn trong cùng repo là `vox-explainer` (chưa đọc kỹ)

## Link
- Repo: https://github.com/heygen-com/hyperframes-community-skills
- Skill: https://github.com/heygen-com/hyperframes-community-skills/tree/master/skills/session-story
- Liên quan: `repos/hyperframes.md`, `repos/prompt-motion.md`, `repos/cinetic.md`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Không có API. Hermes CHỈ nên làm bước vô hại: cài skill. KHÔNG tự harvest lịch sử.
import subprocess
subprocess.run(["npx", "--yes", "skills", "add", "heygen-com/hyperframes-community-skills",
                "--skill", "session-story"], timeout=300)
# Bước đọc lịch sử (harvest.py) phải do người duyệt chấp thuận từng lần.
```

### OpenClaw
```bash
npx skills add heygen-com/hyperframes-community-skills --skill session-story
```
`harvest.py` chỉ đọc định dạng Claude Code và Codex (theo SKILL.md) → OpenClaw không có gì để đọc. Không dùng.

### Antigravity
```bash
# Không deploy. Nếu thử trên VPS: cần ffmpeg, Node 22+, fluidsynth + soundfont.
# Nhưng VPS không có lịch sử Claude Code của mày → để trống, không có gì để harvest.
```
> ⚠️ Mọi lệnh `snapshot` phải có `--describe false` (tránh gửi khung hình sang Gemini). Không bao giờ commit `session-story-candidates.json` hay thư mục dự án lên kho.

# SkillUI (amaancoderx/npxskillui) — GitHub Repo

## TL;DR
CLI Node, giấy phép MIT, đọc một website, thư mục code hoặc repo git rồi sinh ra gói "design system" (`DESIGN.md`, `SKILL.md`, `CLAUDE.md`, file `.skill`) để Claude Code đọc và dựng giao diện đúng màu, font, khoảng cách. Chạy hoàn toàn cục bộ, không cần AI hay API key. Tao đã cài và chạy thử trên một project mẫu nhỏ: chạy được, nhưng bản trích ra **sai so với CSS gốc ở nhiều chỗ** (thiếu màu chính, sai cỡ chữ và bo góc, có dòng tự mâu thuẫn). Dùng như bản nháp, phải đối chiếu lại.

## Repo này dùng để làm gì
Vấn đề nó giải: bảo Claude Code "làm giao diện giống site X" hoặc "đúng phong cách app của tao" thì nó đoán màu và font. SkillUI quét CSS/HTML rồi gom token thật thành một skill, để lần sau Claude Code tự đọc.

Ba nguồn đầu vào:
| Cờ | Quét gì |
|---|---|
| `--dir <path>` | Thư mục code local (`.css`, `.scss`, `.ts`, `.tsx`, `.js`, `.jsx`) |
| `--repo <url>` | Clone repo git công khai rồi quét như `--dir` |
| `--url <url>` | Cào một website đang chạy |

Hai chế độ: mặc định (phân tích tĩnh HTML/CSS) và `--mode ultra` (dùng Playwright chụp cuộn trang, so sánh hover/focus, phát hiện animation). README ghi "No AI, no API keys" đúng với chế độ mặc định, còn `ultra` thì điều khiển trình duyệt thật nên không còn "tĩnh thuần".

## Setup từng bước
1. Cần Node 18+. Cài: `npm install -g skillui` (tao cài cục bộ trong thư mục cách ly, bản npm là `1.3.4`; README ghi 1.3.2, hai nguồn lệch nhau).
2. Chạy: `skillui --dir ./src --out ./design --name ten-du-an`. Nó tạo thư mục `<tên>-design/` trong `--out`.
3. Mở Claude Code trong thư mục đó: `cd ten-du-an-design && claude`. README nói Claude Code tự đọc `CLAUDE.md` và `SKILL.md`, rồi bảo "Build me a UI that matches this design system".
4. Chế độ `ultra` cần cài thêm: `npm install playwright` và `npx playwright install chromium`. Tao chưa thử.
5. Cờ khác: `--format design-md|skill|both`, `--no-skill` (chỉ ra `DESIGN.md`), `--screens <n>` (ultra, mặc định 5, tối đa 20).

## Ví dụ thực tế
**Tao đã chạy thật, trên project mẫu 2 file (1 CSS, 1 TSX) do tao tự viết**, dùng `--dir`. Kết quả là 5 file: `CLAUDE.md`, `DESIGN.md`, `SKILL.md`, `references/DESIGN.md` và file `.skill` (một file zip chứa `DESIGN.md`, `SKILL.md`, `references/`). Chế độ `--dir` không ra các thư mục `tokens/`, `screens/`, `fonts/` mà README nhắc.

**So bản trích với CSS gốc (đây là phần quan trọng):**
| CSS gốc của tao | SkillUI trích ra |
|---|---|
| Màu chính `#0b5fff` (nền nút) và `#073ea8` (hover) | **Không có.** Mất hoàn toàn |
| Màu chữ `#14181f` | Không có |
| Nền `#f7f8fa` | `#ffffff` |
| Màu nhấn `#ff7a1a` | Đúng, nhưng skill ghi "đây là điểm màu DUY NHẤT", sai vì màu chính là xanh |
| Chữ H1 `40px` | `48px` |
| Bo góc `12px` | `8px` |
| Thang khoảng cách chỉ có 4, 8, 16 | Thêm 12, 20, 24, 32, 40, 48, 64 |
| Poppins cho tiêu đề, Inter cho thân bài | Bảng đúng, nhưng phần quy tắc lại ghi ngược "Poppins cho thân bài, Inter cho tiêu đề" |
| Có `.btn` và `.card` | "Components: 0" |

Nếu đưa nguyên bản này cho Claude Code, nó sẽ dựng giao diện bằng token sai và tự tin là đúng.

Đây chỉ là **một project mẫu nhỏ**. Trên project thật có thể khá hơn hoặc tệ hơn. Tao chưa thử `--url`, `--repo`, `ultra`.

**Tình huống áp dụng (minh hoạ, chưa chạy thật):** chạy trên CSS của chính trang đặt vé của mày để sinh `DESIGN.md`, rồi mở lại từng token đối chiếu với file CSS trước khi giao cho Claude Code dựng thêm trang mới.

## Lưu ý / Lỗi thường gặp
- **Trích xuất theo heuristic**: đã thấy thiếu màu, sai số, và thêm giá trị mặc định không có trong nguồn. Luôn đối chiếu `DESIGN.md` với CSS gốc.
- **Bản cũ**: bản phát hành cuối ghi ngày 10/04/2026, tức cách đây khoảng 7 tháng. Trang tải tin ghi "6 tháng trước".
- **Quét website người khác**: README lấy ví dụ trên site của các thương hiệu lớn. Sao chép nhận diện hình ảnh của thương hiệu khác có thể vướng bản quyền hay nhãn hiệu. Dùng cho site của mày hoặc để tham khảo. Tao không phải luật sư.
- **Repo mode chỉ cho repo công khai**, dir mode chỉ quét vài đuôi file nên CSS nằm ở chỗ lạ có thể bị bỏ sót.
- Nhiều site chặn crawler hoặc render bằng JS nặng nên chế độ mặc định (không chạy trình duyệt) có thể thấy ít. Tao chưa thử.

## Đánh giá cá nhân
- Điểm mạnh: miễn phí, MIT, một lệnh, không cần khoá API, đầu ra đúng định dạng skill cho Claude Code, chạy nhanh.
- Điểm yếu: trích xuất sai trên mẫu thử, ít bảo trì, chưa kiểm site thật, rủi ro bản quyền khi quét site người khác.
- Có nên dùng không: 6/10. Dùng làm điểm xuất phát trên code của chính mày, sau đó sửa tay `DESIGN.md`. Không tin nó trên site lạ và không coi đầu ra là đúng chỉ vì định dạng gọn.

## Link
- Repo: https://github.com/amaancoderx/npxskillui
- npm: https://www.npmjs.com/package/skillui
- Trang giới thiệu: https://skillui.vercel.app/
- README: https://cdn.jsdelivr.net/npm/skillui@1.3.4/README.md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# SkillUI là CLI Node, không có REST API. Hermes gọi qua subprocess (khác ràng buộc "chỉ urllib").
# Cần Node 18+ trên máy chạy. Đầu ra luôn cần người đối chiếu, đừng tự động đưa vào sản xuất.
import subprocess

def skillui_from_dir(src_dir, out_dir, name):
    r = subprocess.run(
        ["skillui", "--dir", src_dir, "--out", out_dir, "--name", name],
        capture_output=True, text=True, timeout=180,
    )
    return r.returncode == 0, (r.stdout or r.stderr)[-500:]
```
> ⚠️ Tao đã chạy lệnh CLI tương đương, chưa chạy riêng đoạn Python này.

### OpenClaw
```bash
npx skillui --dir ./app --out ./design --name app
```
> ⚠️ Chạy xong phải có người xem lại `DESIGN.md` trước khi dùng.

### Antigravity
```bash
npm install -g skillui
# Chỉ khi cần chế độ ultra:
npm install playwright && npx playwright install chromium
```
> ⚠️ Ultra mở trình duyệt thật và tải nhiều trang. Chỉ trỏ vào site của mày hoặc site được phép.

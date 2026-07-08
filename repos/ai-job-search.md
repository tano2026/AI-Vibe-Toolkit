# ai-job-search (MadsLorentzen/ai-job-search) — GitHub Repo

## TL;DR
Framework xin việc chạy trên Claude Code — fork về, điền profile 1 lần, xong Claude tự chấm độ phù hợp công việc, viết CV + cover letter riêng cho từng job, và chuẩn bị phỏng vấn. Đang trending trên GitHub.

## Repo này dùng để làm gì
Đây không phải app chạy sẵn mà là một bộ workflow + skill cho Claude Code. Mày fork repo, điền hồ sơ cá nhân (CV cũ, LinkedIn export, hoặc trả lời phỏng vấn từng mục), Claude tổng hợp thành profile chuẩn. Sau đó 3 lệnh chính:
- `/setup` — thiết lập profile ban đầu
- `/scrape` — tìm job trên các portal (mặc định làm cho thị trường Đan Mạch: Jobindex, Jobnet..., nhưng có lệnh `/add-portal` để tự sinh skill scrape cho portal khác, kể cả VN)
- `/apply <url>` — Claude chấm độ fit, viết CV + cover letter bằng LaTeX riêng cho job đó

Điểm hay nhất: dùng kiến trúc "drafter-reviewer" — 1 Claude agent viết draft, 1 Claude agent khác (context sạch) đóng vai reviewer, research công ty rồi phản biện bản draft, agent viết sửa lại theo phản biện. Xong còn có bước tự biên dịch PDF và soi layout (căn 2 trang CV, 1 trang cover letter, không lỗi font) trước khi giao output cuối.

## Setup từng bước
1. Fork + clone:
```bash
gh repo fork MadsLorentzen/ai-job-search --clone
cd ai-job-search
```
2. Cần Claude Code (API key hoặc Claude Pro/Team sub) + Python 3.10+ (cho tool tra lương) + Bun (chạy CLI scrape portal, viết bằng TypeScript).
3. Cài dependency cho từng portal CLI:
```bash
for tool in jobbank-search jobdanmark-search jobindex-search jobnet-search linkedin-search; do
  cd .agents/skills/$tool/cli && bun install && cd ../../../..
done
```
4. Cần LaTeX distro có package `moderncv` — CV compile bằng `lualatex`, cover letter compile bằng `xelatex` (vì cần fontspec cho font Lato/Raleway custom).
5. Chạy `/setup` trong Claude Code, chọn 1 trong 3 cách nạp profile: thư mục `documents/` (nhiều file nguồn), import 1 file CV duy nhất, hoặc trả lời phỏng vấn từng mục.
6. Không ở Đan Mạch → chạy `/add-portal` để Claude tự scaffold CLI scrape cho job portal nội địa của mày, test luôn 1 query thật trước khi đăng ký chính thức.

## Ví dụ thực tế
Áp cho Tano Agency khi cần tuyển content writer part-time: fork repo, chạy `/add-portal` trỏ vào VietnamWorks/TopCV thay vì Jobindex Đan Mạch, `/setup` nạp profile công ty (không phải profile ứng viên — dùng ngược để mô tả job cần tìm ứng viên phù hợp cũng được nếu tùy biến prompt), rồi dùng nhánh CV/cover letter cho ứng viên demo thử tool trước khi apply job thật ở nước ngoài.

## Lưu ý / Lỗi thường gặp
- `pdflatex` hay lỗi font-expansion với `fontawesome5` trên MiKTeX bản mới → dùng `lualatex` cho CV thay vì pdflatex.
- Bản cũ của repo từng commit kèm `.claude/settings.local.json` pre-approve quyền `Bash(curl:*)`, `Bash(python:*)`, `Bash(bun:*)` khá rộng — nếu clone bản cũ, file này vẫn còn trong working copy dù đã update, cần tự dọn để tránh Claude Code có quyền chạy bash rộng hơn cần thiết.
- Cover letter cần font Lato/Raleway đặt đúng thư mục `cover_letters/OpenFonts/fonts/`, thiếu là compile lỗi.
- Job portal skill mặc định chỉ cover thị trường Đan Mạch — bắt buộc phải tự thêm portal cho VN, không có sẵn.

## Đánh giá cá nhân
- Điểm mạnh: kiến trúc drafter-reviewer thông minh, tự verify claim trong CV không cho bịa kỹ năng, tự ATS-check bằng cách extract text layer PDF rồi chấm keyword coverage, pattern add-portal linh hoạt cho market khác.
- Điểm yếu: setup nặng (cần LaTeX + Bun + Python cùng lúc), phụ thuộc Claude Code (không chạy được với Claude.ai thường), job portal cho VN phải tự làm từ đầu qua `/add-portal`, chưa test rộng ngoài thị trường Đan Mạch.
- Có nên dùng không: 6/10 — ý tưởng và kỹ thuật hay để học pattern reviewer-agent, nhưng cần đầu tư setup và tự viết portal VN mới dùng thực chiến được ngay.

## Link
- Repo: https://github.com/MadsLorentzen/ai-job-search
- Docs: README.md và SETUP.md trong repo

---

## 🤖 Agent Integration

### Hermes (Python)
> Không áp dụng — đây là bộ skill/command dành riêng cho Claude Code (CLI), không phải service có REST API. Hermes (chạy Python độc lập trên VPS) không gọi được framework này trực tiếp.

### OpenClaw
```bash
# Không tích hợp qua MCP — phải chạy trong môi trường Claude Code thật
gh repo fork MadsLorentzen/ai-job-search --clone
cd ai-job-search
# rồi mở bằng Claude Code, không phải lệnh gọi từ OpenClaw
```

### Antigravity
```bash
# Nếu muốn dựng máy riêng chạy thử framework này (không phải service deploy 24/7):
sudo apt install texlive-full  # cần lualatex + xelatex + moderncv
curl -fsSL https://bun.sh/install | bash  # cần Bun cho CLI scrape
```
> ⚠️ Đây là workflow chạy tương tác qua Claude Code, không phải agent chạy nền — không hợp để Antigravity deploy như service, chỉ dùng khi có người ngồi tương tác trực tiếp với Claude Code.

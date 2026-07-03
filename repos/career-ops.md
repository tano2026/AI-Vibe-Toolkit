# Career-Ops — GitHub Repo

## TL;DR
Hệ thống tìm việc tự động chạy trên Claude Code (và Codex/Gemini/OpenCode) — chấm điểm A-F cho từng offer theo 10 tiêu chí, tự quét 45+ portal tuyển dụng, tự sinh CV/cover letter tối ưu ATS dạng PDF, có dashboard Go riêng. Tác giả dùng chính nó đánh giá 740+ offer và lấy được vị trí Head of Applied AI. 57k+ sao.

## Repo này dùng để làm gì
Không phải "viết CV bằng AI" đơn giản — đây là 1 pipeline đầy đủ: quét portal (Greenhouse/Lever/Workday/LinkedIn qua Playwright) → chấm điểm offer theo khung 10 tiêu chí trọng số → sinh CV/cover letter riêng cho từng offer → track trạng thái tất cả trong 1 nguồn sự thật duy nhất. 14 "skill mode" khác nhau (đơn đánh giá 1 offer, batch xử lý 10+ offer song song, sinh PDF, quét portal...).

Điểm hay: hệ thống được thiết kế để CHÍNH AI CLI tự sửa cho khớp người dùng — nói "đổi archetype sang vai trò backend engineering" là nó tự sửa file cấu hình, không cần tự tay edit YAML.

## Setup từng bước
1. Clone + cài:
```bash
git clone https://github.com/santifer/career-ops.git
cd career-ops && npm install
npx playwright install chromium  # chỉ cần nếu dùng sinh PDF
```
2. Check môi trường: `npm run doctor`
3. Cấu hình:
```bash
cp config/profile.example.yml config/profile.yml
cp templates/portals.example.yml portals.yml
```
4. Tạo `cv.md` ở thư mục gốc — CV dạng markdown
5. Mở AI CLI ngay trong thư mục: `claude` (hoặc `gemini`/`codex`/`opencode`/`agy`) — hệ thống tự hỏi setup qua chat, không cần sửa tay
6. Ví dụ ra lệnh tự nhiên: *"Change the archetypes to backend engineering roles"*, *"Translate the modes to English"*

## Ví dụ thực tế
Chạy `/career-ops "Senior AI Engineer at Anthropic..."` → hệ thống tự chấm A-F theo 10 tiêu chí trọng số + block G riêng cho "Posting Legitimacy" (phát hiện tin giả/spam), xuất báo cáo dạng `{số}-{tên-công-ty}-{ngày}.md` kèm khối YAML machine-readable ở cuối để script khác đọc được.

## Lưu ý / Lỗi thường gặp
- Là tool local 100% — CV và data cá nhân không rời máy, chỉ gửi thẳng tới AI provider mình chọn (Anthropic/OpenAI), tác giả không thu thập gì
- Prompt mặc định dặn AI KHÔNG tự động nộp đơn — nhưng nếu tự sửa prompt hoặc đổi model, rủi ro AI hành xử khó lường là có thật, tác giả cảnh báo rõ trong README
- Phải tự tuân thủ ToS của từng portal tuyển dụng khi dùng — không được dùng để spam nhà tuyển dụng
- Cần Playwright + Chromium riêng cho phần sinh PDF, không phải cài 1 lần là xong hết mọi tính năng

## Đánh giá cá nhân
- Điểm mạnh: có track record thật (740+ offer đánh giá, tác giả dùng chính nó lấy được việc) chứ không phải demo suông; kiến trúc "AI tự sửa config theo lệnh tự nhiên" là pattern hay, đáng học cho các skill khác trong kho
- Điểm yếu: domain quá hẹp (chỉ tìm việc) — không liên quan trực tiếp đến content factory/agency của Nobitano, giá trị chính là **học kiến trúc** (batch processing, scoring framework, multi-CLI support) hơn là dùng trực tiếp
- Có nên dùng không: 6/10 cho việc dùng trực tiếp (không đúng nhu cầu), nhưng 8/10 nếu chỉ để tham khảo kiến trúc — đặc biệt khung chấm điểm 10-tiêu-chí trọng số có thể áp dụng lại cho việc chấm điểm lead/khách hàng trong SMB AI Team

## Link
- Repo: https://github.com/santifer/career-ops
- Stars: ~57.000-58.000+
- License: MIT

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Career-ops chay qua slash command trong AI CLI, khong co REST API rieng
# de Hermes goi tu dong (Python script goi Playwright/CLI subprocess neu can):
import subprocess

def run_career_ops_scan(project_dir="./career-ops"):
    # Chay quet portal qua Claude Code CLI trong thu muc project
    result = subprocess.run(
        ["claude", "/career-ops", "scan"],
        cwd=project_dir, capture_output=True, text=True
    )
    return result.stdout
```

### OpenClaw
```bash
cd career-ops
agy  # hoac opencode
# /career-ops "ten offer..."
# /career-ops pipeline
# /career-ops scan
```

### Antigravity
```bash
# Neu can chay dinh ky quet portal (vd Tano Agency tuyen dung)
git clone https://github.com/santifer/career-ops.git
cd career-ops && npm install && npx playwright install chromium
```
> ⚠️ Không liên quan trực tiếp business hiện tại — chỉ deploy nếu Nobitano cần tuyển người cho Tano Agency, không phải ưu tiên cho content factory.

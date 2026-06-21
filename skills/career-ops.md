# Career Ops — Hệ Thống Tìm Việc AI Xây Bằng Claude Code

## TL;DR
Hệ thống tìm việc AI-powered xây bằng Claude Skills: tự động navigate job listings, so sánh CV với JD, adapt resume theo từng listing. 14 skill modes, Go dashboard, PDF generation.

## Tool này dùng để làm gì
Tác giả dành tháng trời apply việc theo cách truyền thống và quyết định build system AI như công ty dùng để filter CV — nhưng ngược lại, để ứng viên filter công ty và tự động hóa toàn bộ quy trình.

Career Ops gồm:
- **14 skill modes** — từ job discovery, CV matching đến interview prep
- **Agentic job search** — tự động tìm và navigate job listings
- **CV vs JD adapter** — so sánh CV mày với từng JD và suggest chỉnh sửa
- **Go dashboard** — web interface theo dõi pipeline ứng tuyển
- **PDF generation** — export CV và cover letter chuẩn

Hỗ trợ nhiều ngôn ngữ: EN, ES, PT-BR, KO, JA, RU, ZH-TW.

## Setup từng bước
```bash
# Prerequisites: Go 1.21+, Claude Code

# Clone repo
git clone https://github.com/FullStackFang/career-ops
cd career-ops

# Install Go dependencies
go mod download

# Chạy dashboard
go run main.go

# Mở browser tại localhost:8080
# Add Claude skills vào project
cp -r .claude/ ./
```

Trong Claude Code:
```
/job-search "Senior React Developer" --location="Vietnam" --remote=true
/cv-match --jd="path/to/jd.txt" --cv="path/to/cv.pdf"
/adapt-resume --style="startup"
```

## Ví dụ thực tế
**Workflow thực tế:**
1. `/job-search "Product Manager" --remote` → Claude tìm và list 20 job phù hợp
2. `/cv-match job-001` → So sánh CV mày với JD, score match %, highlight gaps
3. `/adapt-resume job-001` → Tự động viết lại CV emphasize đúng skills JD cần
4. `/cover-letter job-001 --tone="professional"` → Draft cover letter personalized
5. Track tất cả trong Go dashboard

## Lưu ý / Lỗi thường gặp
- Cần Go 1.21+ (nhiều người không có sẵn)
- Agentic job search cần configure source (LinkedIn, Indeed...) — không ra-of-the-box
- CV adapter tốt nhất khi CV đã có structure rõ ràng
- Dashboard đẹp nhưng còn beta, đôi khi cần restart

## Đánh giá cá nhân
- **Điểm mạnh:** Ý tưởng thực chiến, 14 skill modes cover đủ workflow tìm việc. Dashboard Go là điểm cộng lớn
- **Điểm yếu:** 0 star trên GitHub (repo mới, chưa viral), Go requirement là barrier. Cần test thêm với thị trường VN
- **Có nên dùng không:** 6.5/10 — promising nhưng còn early. Theo dõi thêm, chưa cần rush

## Link
- Repo: https://github.com/FullStackFang/career-ops
- Tác giả: https://x.com/santifer

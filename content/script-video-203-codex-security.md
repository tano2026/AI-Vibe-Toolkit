# Script Video 203 — Codex Security: OpenAI tự vá lỗ hổng bảo mật, tìm ra 14 CVE thật

## Thông tin
- Tool/Repo/Skill liên quan: /repos/codex-security.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

## Hook (3 giây đầu)
"OpenAI vừa mở nguồn công cụ đã tìm ra mười bốn lỗ hổng thật trên Chromium, OpenSSH."

## Script voiceover (ElevenLabs-ready)
Đây là công cụ chính thức của OpenAI, dựng riêng một mô hình mối đe doạ cho từng dự án trước khi quét, thay vì chỉ so khớp mẫu như công cụ phân tích tĩnh thông thường.
Trong ba mươi ngày thử nghiệm, nó quét qua một triệu hai trăm nghìn commit, tìm ra hơn mười nghìn lỗi mức độ cao, và được gán mười bốn mã CVE thật trên những phần mềm lớn như Chromium, OpenSSH, GnuTLS.
Điểm khác biệt là nó tự kiểm chứng phát hiện trong môi trường cách ly trước khi báo cáo, giảm hẳn tình trạng báo động giả. Cài chỉ một dòng lệnh, mã nguồn mở hoàn toàn.
Lưu ý quan trọng, tên gói bắt đầu bằng openai rất dễ bị giả mạo, luôn cài đúng từ nguồn chính thức, kiểm tra kỹ tên gói trước khi chạy bất kỳ lệnh nào.

## Ghi chú quay (OBS)
- Cảnh 1: Terminal chạy npx codex-security scan
- Cảnh 2: Danh sách CVE thật tìm được trên các dự án lớn
- Cảnh 3: Cảnh báo về rủi ro giả mạo tên gói npm

## Caption/Sub note (CapCut)
Highlight: "14 CVE thật", "chính thức OpenAI", "cẩn thận giả mạo tên gói". Nhấn cảnh cảnh báo giả mạo ở cuối.

## Thumbnail idea (Canva)
Kính lúp soi vào dòng code, phát hiện ra biểu tượng khiên cảnh báo, chữ to "AI TỰ TÌM RA 14 LỖ HỔNG THẬT".

## CTA cuối video
Follow nếu quan tâm bảo mật code trước khi deploy, chi tiết ở bio.

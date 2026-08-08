# Script Video 206 — Bộ nhớ agent 4 tầng của Tencent, debug được từng bước thay vì dò mù

## Thông tin
- Tool/Repo/Skill liên quan: /repos/tencentdb-agent-memory.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

## Hook (3 giây đầu)
"AI nhớ sai mà không biết sai ở đâu? Đây là cách Tencent giải quyết."

## Script voiceover (ElevenLabs-ready)
Đa số hệ thống bộ nhớ AI băm nhỏ mọi thứ vào một kho vector phẳng, khi nhớ sai chỉ thấy điểm số, không biết vì sao sai.
Hệ thống này chia bộ nhớ thành bốn tầng, lưu dưới dạng file đọc được trực tiếp, không phải hộp đen. Muốn debug, chỉ cần đi ngược chuỗi từ hồ sơ tổng hợp về tới đúng đoạn hội thoại gốc sinh ra nó.
Nó còn tự động đọc cả một codebase, dựng bản đồ liên kết giữa các file, hàm, lời gọi hàm với nhau, giúp agent mới không phải học lại dự án từ đầu mỗi lần.
Chạy hoàn toàn local, không phụ thuộc dịch vụ ngoài, mã nguồn mở từ chính Tencent.

## Ghi chú quay (OBS)
- Cảnh 1: Sơ đồ 4 tầng bộ nhớ từ hội thoại thô tới hồ sơ tổng hợp
- Cảnh 2: Mở file Markdown đọc trực tiếp thay vì nhìn điểm vector số
- Cảnh 3: CodeGraph tự vẽ liên kết giữa các file trong 1 codebase

## Caption/Sub note (CapCut)
Highlight: "debug được từng bước", "4 tầng bộ nhớ", "tự đọc codebase". Nhấn cảnh mở file Markdown trực tiếp.

## Thumbnail idea (Canva)
4 lớp xếp chồng từ mờ tới rõ, chữ to "BỘ NHỚ AI DEBUG ĐƯỢC, KHÔNG PHẢI HỘP ĐEN".

## CTA cuối video
Follow nếu đang xây hệ thống nhiều agent cần nhớ context lâu dài, chi tiết ở bio.

# Script Video 195 — PixelRAG

## Thông tin
- Tool/Repo/Skill liên quan: /repos/pixelrag.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

## Hook (3 giây đầu)
AI vẫn đọc web sai vì nó không biết nhìn bảng giá — cái tool này cho AI đôi mắt thật.

## Script voiceover (ElevenLabs-ready)
Mọi AI research tool hiện tại đều làm một việc giống nhau. Nó lấy trang web, chuyển hết thành chữ, rồi mới đọc. Nghe hợp lý, nhưng có một vấn đề lớn. Khi trang web có bảng giá phức tạp, biểu đồ, hay layout nhiều cột, bước chuyển thành chữ đó làm mất hết cấu trúc. AI đọc nhầm cột, lẫn hàng, bỏ sót ghi chú nhỏ.

PixelRAG, một dự án mã nguồn mở từ Berkeley, giải quyết vấn đề này theo cách ngược lại hoàn toàn. Thay vì đọc chữ, nó chụp ảnh cả trang web, rồi để một model AI có mắt nhìn trực tiếp vào ảnh đó để tìm câu trả lời. Bảng giá, biểu đồ, layout được giữ nguyên y như con người nhìn thấy.

Team nghiên cứu đã test trên sáu bộ benchmark khác nhau, và PixelRAG thắng RAG kiểu chữ truyền thống trên cả sáu. Đặc biệt với câu hỏi liên quan tới bảng số liệu, độ chính xác tăng rõ rệt.

Điều thú vị nhất là nó có sẵn một skill cho Claude Code, tên là pixelbrowse. Cài một dòng lệnh, và Claude sẽ tự chụp ảnh trang web thay vì đọc HTML thô. Với dân research, đây là cách nhanh nhất để AI đọc đúng những trang web phức tạp mà cách cũ hay đọc sai.

Repo đang trending mạnh trên GitHub, mã nguồn mở hoàn toàn, cài một lệnh pip install là dùng được ngay.

## Ghi chú quay (OBS)
- Cảnh 1: Quay màn hình 1 trang web có bảng giá phức tạp, zoom vào để thấy cấu trúc bảng rối
- Cảnh 2: Terminal chạy lệnh `pixelshot` chụp trang đó, kết quả ra ảnh tile
- Cảnh 3: So sánh song song — bên trái RAG text đọc sai bảng, bên phải PixelRAG đọc đúng (dùng ảnh minh hoạ từ paper nếu được phép, hoặc tự dựng lại bằng demo thật)
- Cảnh 4: Cài đặt pixelbrowse skill cho Claude Code, demo câu lệnh `claude -p "screenshot ... và tóm tắt"`

## Caption/Sub note (CapCut)
Highlight từ khóa: "chụp ảnh trang web", "AI có mắt nhìn", "pixelbrowse", "Claude Code skill". Cắt cảnh nhanh ở đoạn so sánh RAG text vs PixelRAG để tạo tương phản rõ.

## Thumbnail idea (Canva)
Chia đôi màn hình: bên trái icon mắt bị che/mờ + chữ "AI đọc sai", bên phải icon mắt sáng rõ + chữ "AI đọc đúng". Overlay text lớn: "CHO AI ĐÔI MẮT THẬT".

## CTA cuối video
Follow để xem thêm AI tool mới mỗi ngày. Comment nếu muốn video hướng dẫn setup pixelbrowse chi tiết.

# Script Video 215 — OpenWorker (Andrew Ng)

## Thông tin
- Tool/Repo/Skill liên quan: /repos/openworker-andrew-ng.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~40 giây

## Hook (3 giây đầu)
"Andrew Ng vừa mở mã nguồn 1 AI coworker — điểm hay nhất không phải AI nó làm được gì, mà là cách nó biết khi nào phải dừng lại hỏi."

## Script voiceover (ElevenLabs-ready)
[Đoạn 1 — vấn đề/pain point]
Agent AI hành động tự do là con dao hai lưỡi. Cho nó quyền gửi tin nhắn, sửa lịch, chạy lệnh — mà không kiểm soát được lúc nào nó tự làm lúc nào phải hỏi, là rủi ro thật.

[Đoạn 2 — giới thiệu giải pháp]
OpenWorker giải bằng cách phân loại mọi hành động thành bốn mức rủi ro. Đọc dữ liệu thì làm luôn không cần hỏi. Ghi file cục bộ, chạy lệnh, hay gọi ra bên ngoài như gửi Slack thì phải qua cổng duyệt. Năm chế độ quyền, từ chỉ đọc cho tới tự động hoàn toàn, đều tôn trọng đúng bốn mức đó.

[Đoạn 3 — demo/cách làm]
Giao nó một câu, ví dụ chuẩn bị brief cho cuộc gọi renewal khách hàng. Nó tự đọc lịch sử tương tác, kiểm tra ticket còn mở, tổng hợp số liệu, rồi trả về đúng một đoạn brief dùng được luôn, không phải danh sách để tự gộp lại.

[Đoạn 4 — kết + CTA]
Điều đáng học không phải công cụ này, mà cách nó thiết kế quyền hạn. Lưu lại nếu team mày cũng đang build agent tự hành động.

## Ghi chú quay (OBS)
- Cảnh 1: Sơ đồ 4 mức rủi ro read/write_local/exec/external hiện dần
- Cảnh 2: Demo gõ 1 yêu cầu, agent hỏi xin duyệt trước khi gửi Slack
- Cảnh 3: Output brief hoàn chỉnh hiện ra
- Cảnh 4: Cảnh báo nhỏ "chỉ chạy desktop, không chạy VPS headless"

## Caption/Sub note (CapCut)
Highlight: "4 mức rủi ro", "xin duyệt trước", "outcome không phải chat". Nhấn mạnh câu cảnh báo desktop-only ở cuối để tránh hiểu nhầm dùng được trên server.

## Thumbnail idea (Canva)
Chữ lớn "AI TỰ HÀNH ĐỘNG — AI BIẾT DỪNG LÚC NÀO?" trên nền 4 ô màu từ xanh (an toàn) tới đỏ (cần duyệt), icon ổ khóa ở ô đỏ cuối.

## CTA cuối video
Follow để xem thêm review công cụ agent AI, comment "WORKER" để nhận link repo.

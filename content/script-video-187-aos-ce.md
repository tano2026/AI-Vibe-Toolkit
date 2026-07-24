# Script Video 187 — AOS Community Edition (aos-ce)

## Thông tin
- Tool/Repo/Skill liên quan: /repos/aos-ce.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

## Hook (3 giây đầu)
Nếu AI agent của mày có quyền chạy shell tuỳ tiện trên server, mày đang ngồi trên một quả bom hẹn giờ.

## Script voiceover (ElevenLabs-ready)
Càng nhiều agent AI chạy tự động trên server, rủi ro càng lớn. Một dòng lệnh độc trong nội dung agent đọc phải, nó có thể tự chạy luôn mà mày không biết.

AOS Community Edition giải quyết bài toán này bằng cách coi agent như một process trong hệ điều hành. Mỗi năng lực agent được dùng phải đóng gói thành một capsule riêng, chỉ có đúng quyền nó cần, không hơn.

Có một công cụ tên Forge bên trong, cho phép chính agent tự soi hệ thống, tự phát hiện năng lực còn thiếu, và tự xây dựng capsule mới đúng chuẩn giới hạn quyền tối thiểu.

Và mỗi khi agent muốn làm gì đó nhạy cảm, hệ thống bắt buộc phải qua một cửa sổ xác nhận thật, không tự động chạy ngầm.

Sáu nghìn tám trăm sao trên GitHub, viết bằng Rust, do đội Unicity phát triển.

## Ghi chú quay (OBS)
- Cảnh 1: Quay terminal chạy aos status --json
- Cảnh 2: Sơ đồ đơn giản vẽ tay hoặc Figma: agent -> capsule -> approval gate
- Cảnh 3: Quay lệnh aos capsule build đang chạy

## Caption/Sub note (CapCut)
Highlight: "quả bom hẹn giờ", "capsule", "Forge", "cửa sổ xác nhận thật". Nhịp cắt nhanh ở đoạn liệt kê rủi ro.

## Thumbnail idea (Canva)
Nền đỏ cam cảnh báo, chữ lớn "AGENT CỦA MÀY CÓ ĐANG CHẠY TỰ DO KHÔNG?", icon khoá + icon terminal.

## CTA cuối video
Follow nếu mày đang build hệ thống agent tự động, xem thêm cách bảo mật agent trong các video khác.

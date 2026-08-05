# Script Video 218 — System Design Primer

## Thông tin
- Tool/Repo/Skill liên quan: /repos/system-design-primer.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~40 giây

## Hook (3 giây đầu)
"360 nghìn sao GitHub cho một repo không có nổi một dòng code chạy được — vậy nó dạy cái gì?"

## Script voiceover (ElevenLabs-ready)
[Đoạn 1 — vấn đề/pain point]
Xây agent, xây pipeline, đến lúc nào đó sẽ tự hỏi database này nên tách bảng hay không, chỗ nào cần cache, chỗ nào chấp nhận dữ liệu chậm cập nhật một chút để đổi lấy tốc độ. Không có tài liệu nào tổng hợp rõ ràng thì cứ đoán mò.

[Đoạn 2 — giới thiệu giải pháp]
System Design Primer gom hết những khái niệm đó lại có tổ chức. Load balancer, caching, sharding, message queue, và quan trọng nhất là mỗi khái niệm đều nói rõ đánh đổi cái gì lấy cái gì, không có giải pháp nào miễn phí.

[Đoạn 3 — demo/cách làm]
Có sẵn case study mẫu, kiểu thiết kế một hệ thống mạng xã hội hay một hệ thống giao dịch, đi từ gom yêu cầu, tới thiết kế tổng quan, rồi đào sâu từng phần và bàn bottleneck sẽ nằm ở đâu. Đúng cấu trúc cần khi phải giải thích một quyết định kiến trúc cho người khác nghe.

[Đoạn 4 — kết + CTA]
Không có phần nào nói về kiến trúc multi agent hay AI infra hiện đại, nhưng nền tảng tư duy thì vẫn đúng. Lưu lại nếu đang chuẩn bị thiết kế hệ thống mới.

## Ghi chú quay (OBS)
- Cảnh 1: Hiện số sao 360k trên GitHub
- Cảnh 2: Cuộn qua danh sách khái niệm (load balancer, caching, sharding...)
- Cảnh 3: Zoom vào 1 case study mẫu, chỉ rõ cấu trúc 4 bước
- Cảnh 4: Cảnh báo nhỏ "không cover AI-agent infra, cần nguồn khác bổ sung"

## Caption/Sub note (CapCut)
Highlight: "360k sao", "mọi thứ đều đánh đổi", "không có code chạy". Nhấn chậm ở câu "everything is a trade-off" vì đây là ý chính của cả repo.

## Thumbnail idea (Canva)
Chữ lớn "360K SAO — KHÔNG 1 DÒNG CODE" trên nền sơ đồ kiến trúc hệ thống đơn giản (load balancer, server, database) vẽ tay kiểu whiteboard.

## CTA cuối video
Follow để xem thêm tài liệu nền tảng cho dân build hệ thống, comment "DESIGN" để nhận link repo.

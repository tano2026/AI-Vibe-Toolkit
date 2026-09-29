# Animasyon Stil Katalogu — GitHub Repo

## TL;DR
Catalog 20 phong cách animation cho video — mỗi phong cách có clip mẫu 9-10 giây để xem trước khi chọn. Nói tên phong cách (vd "blueprint") là ra đúng chất liệu hình ảnh đó, không cần tự mô tả style dài dòng mỗi lần.

## Repo này dùng để làm gì
20 phong cách đã thử nghiệm thật (không phải lý thuyết), mỗi cái có clip minh hoạ riêng: Kurzgesagt, Isometric, Bauhaus, Memphis, **Whiteboard** (trùng khớp `srt-whiteboard-animation` đã research trước), Blackboard, Blueprint, Single-line, Paper-cutout, Pencil sketch, Linocut, Clay, 70s style, Pixel art, 16mm documentary, Comic book, Terminal/code aesthetic, và vài phong cách nữa. Cách dùng: chọn tên style trước, ra lệnh kiểu "giải thích chủ đề X theo phong cách blueprint".

## Điểm kết nối quan trọng — đây chính là phần "[Style]" trong công thức đã viết

`image-prompt-formula-core` (Designer Pro) có công thức 7 phần, trong đó `[Style]` hiện chỉ ghi ví dụ chung ("photorealistic/illustration"). Catalog này cho **20 lựa chọn cụ thể, đã kiểm chứng** thay vào đúng chỗ đó — không cần tự nghĩ style mỗi lần, chỉ cần chọn tên.

## Setup từng bước
1. Xem repo, chọn 1 trong 20 phong cách khớp nội dung cần làm
2. Xem clip mẫu (9-10s) để chắc đúng ý trước khi áp dụng
3. Điền tên phong cách vào phần `[Style]` của công thức prompt (`image-prompt-formula-core`)
4. Gọi công cụ tạo ảnh/video thật (google-flow-mcp hoặc tương đương)

## Ví dụ thực tế
GMSP cần giải thích khái niệm tử vi — thay vì tự nghĩ style, chọn thẳng "Blueprint" (phong cách bản vẽ kỹ thuật, tạo cảm giác "giải mã" hợp chủ đề) hoặc "Whiteboard" (đã có sẵn tool riêng `srt-whiteboard-animation` để làm đúng phong cách này). Nội dung ABTRIP giải thích quy trình Fast Track có thể hợp "Isometric" (rõ ràng, có cấu trúc, hợp nội dung quy trình/hướng dẫn).

## Lưu ý / Lỗi thường gặp
- Chỉ có 18-20 style tên bằng tiếng Thổ Nhĩ Kỳ trong README gốc — cần tự dịch/hiểu đúng ý nghĩa hình ảnh trước khi áp dụng, đừng dịch máy mù
- Đây là catalog THAM KHẢO/chọn style, không phải tool tự tạo animation — vẫn cần công cụ thực thi riêng (google-flow-mcp cho ảnh tĩnh, srt-whiteboard-animation cho phong cách Whiteboard cụ thể)

## Đánh giá cá nhân
- Điểm mạnh: 20 lựa chọn cụ thể, đã test thật (có clip minh hoạ, không phải liệt kê suông), giải quyết đúng vấn đề "không biết nên chọn style nào" khi viết prompt
- Điểm yếu: chỉ là catalog tham khảo, không tự tạo ra animation — cần ghép với tool thực thi khác
- Có nên dùng: 7/10 — nhẹ, dễ dùng, đáng tham khảo mỗi khi cần đa dạng hoá phong cách hình ảnh cho các brand

## Link
- Repo: https://github.com/yasinozmeen/animasyon-stil-katalogu
- Dùng cùng: image-prompt-formula-core (điền vào phần [Style]), srt-whiteboard-animation (style #05 Whiteboard)

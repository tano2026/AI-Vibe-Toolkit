# Awesome Claude 5.5 Videos — GitHub Repo

## TL;DR
Danh mục tham khảo (không phải 1 tool cài đặt) tổng hợp cách dùng Claude Opus/Sonnet 5.5 để điều phối tạo video/motion graphics — có nguồn dẫn chứng (source-linked), không phải liệt kê suông.

## ⚠️ Làm rõ ngay — Claude KHÔNG tự tạo video

Đọc kỹ mô tả: Claude Code (qua plugin + Ruby toolkit) **lên kế hoạch + LẮP RÁP** motion graphics từ bài hát/brief có sẵn — dùng workflow p5.js **gọi model ngoài** (Fal image/video/audio) để tạo nội dung thật. Claude đóng vai trò **điều phối + viết code dựng**, không phải model tự sinh video. Đúng pattern đã quen: `product-film-skill` (Claude Code đọc UI thật rồi dựng bằng Remotion) — đây là biến thể cho nhạc/motion graphics.

## Repo này dùng để làm gì
Tổng hợp case thật (77 file music video, 215 file ads/launch) kèm phân tích thị số liệu màu sắc (độ "sặc sỡ" trung bình 45,5% cho MV, 17,6% cho ads) — dùng để tham khảo phong cách/tỷ lệ màu khi brief cho AI dựng video, không phải random.

## 1 điểm chưa chắc chắn — "next-Fable", cần thận trọng

Repo nhắc tới *"separately labeled next-Fable testing reports"* và *"provisional Fable demos"*. Fable là tên model tầng **Mythos** của chính Anthropic (Claude Fable 5.1 hiện có, thêm bảo mật sinh học/an ninh mạng/LLM R&D so với Mythos gốc). Đây là **báo cáo thử nghiệm CỘNG ĐỒNG** về 1 bản Fable mới hơn, **KHÔNG PHẢI thông báo chính thức từ Anthropic** — không nên coi là xác nhận sản phẩm thật, chỉ là quan sát/đồn đoán từ người dùng thử. Cần thận trọng khi trích dẫn phần này.

## Setup từng bước
Đây là danh mục tham khảo, không có lệnh cài chung — vào từng mục (vd "Motion Graphics Music Video skill" của tác giả makevoid) để lấy plugin/toolkit cụ thể đó.

## Ví dụ thực tế
Khi làm video nhạc nền cho GMSP (ghép với YuE2 Studio đã research trước) — tham khảo tỷ lệ màu/phong cách trong danh mục này để brief đúng hướng, thay vì đoán mò.

## Lưu ý / Lỗi thường gặp
- Hiểu nhầm "Claude 5.5 tạo video" — SAI, Claude điều phối + gọi model ngoài (Fal), không tự sinh video
- Tin ngay phần "next-Fable" như thông báo chính thức — đây là báo cáo cộng đồng, chưa xác nhận từ Anthropic

## Đánh giá cá nhân
- Điểm mạnh: có nguồn dẫn chứng thật (source-linked), số liệu phân tích màu sắc cụ thể, đúng pattern đã quen (Claude Code điều phối + model ngoài) nên dễ tích hợp
- Điểm yếu: chỉ là danh mục tham khảo, không phải tool cài đặt trực tiếp; phần "next-Fable" chưa kiểm chứng được
- Có nên dùng: 6/10 — tham khảo tốt khi cần ý tưởng phong cách video, không phải ưu tiên hành động ngay

## Link
- Repo: https://github.com/athemeroy/awesome-claude-5-5-videos
- Dùng cùng: repos/product-film-skill.md, repos/yue2-studio.md, repos/remotion.md (đã có trong kho)

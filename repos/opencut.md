# OpenCut — GitHub Repo

## TL;DR
Video editor mã nguồn mở, được gọi là "CapCut alternative" — chạy trên web, desktop, mobile. 69k+ star, MIT license. ĐANG được viết lại toàn bộ (rewrite), bản dùng được hiện tại là bản "classic" cũ, không phải bản trên nhánh main.

## Repo này dùng để làm gì
OpenCut là editor video kéo-thả kiểu CapCut nhưng free và mở mã nguồn, chạy được trên nhiều nền tảng từ 1 codebase. Bản đang phát triển (rewrite, Rust core) hứa hẹn thêm: Editor API, hệ plugin bên thứ ba, MCP server để AI agent điều khiển editor trực tiếp, headless mode (tự động hoá render hàng loạt), và 1 tab scripting ngay trong editor. Đây chính là các tính năng đáng chú ý cho ai đang xây content factory tự động (như pipeline video của Nobitano).

## Setup từng bước
1. **QUAN TRỌNG:** bản `main` hiện tại đang rewrite, CHƯA dùng được cho production. Muốn dùng thật, lấy bản classic:
   ```bash
   git clone https://github.com/opencut-app/opencut-classic.git
   ```
   Hoặc dùng bản host sẵn tại https://opencut.app (vẫn chạy bản classic).
2. Nếu muốn theo dõi/đóng góp cho bản rewrite (chưa nhận contribution ngoài lúc này):
   ```bash
   bash <(curl -fsSL https://moonrepo.dev/install/proto.sh)   # cài proto trước
   git clone https://github.com/OpenCut-app/OpenCut.git
   cd OpenCut && proto use
   moon run web:dev       # localhost:5173
   moon run api:dev       # localhost:8787
   ```
3. Theo dõi tiến độ rewrite qua Discord chính thức của dự án nếu quan tâm tính năng MCP server/headless mode.

## Ví dụ thực tế
Đang cần 1 editor tự host để cắt/ghép clip cho pipeline `vibeforge` (music channel) hoặc
`yt-cashcow` (video review) mà không phụ thuộc CapCut trả phí → có thể thử bản classic ngay,
nhưng KHÔNG nên đặt cược automation dài hạn vào tính năng MCP/headless của bản rewrite vì
chưa release, timeline chưa rõ.

## Lưu ý / Lỗi thường gặp
- Nhầm lẫn phổ biến nhất: clone nhánh `main` của `OpenCut-app/OpenCut` tưởng dùng được ngay —
  thực ra đây là bản đang viết lại từ đầu, thiếu tính năng so với bản classic.
- Repo hiện KHÔNG nhận external contribution trong lúc kiến trúc rewrite còn đang thiết kế —
  không tốn công gửi PR lúc này.
- Tính năng MCP server (cho AI agent điều khiển editor) mới chỉ là roadmap, chưa có timeline
  release cụ thể — đừng lên kế hoạch phụ thuộc vào nó cho quý này.

## Đánh giá cá nhân
- Điểm mạnh: bản classic đã đủ dùng cho nhu cầu cắt ghép cơ bản, free và self-host được, MIT
  license thoải mái sửa/dùng thương mại; roadmap MCP server rất đáng để dõi theo cho content
  automation.
- Điểm yếu: đúng lúc này dự án đang ở trạng thái chuyển giao (rewrite), tài liệu/hướng dẫn cho
  bản mới còn thiếu, rủi ro nếu build automation phụ thuộc tính năng chưa ra mắt.
- Có nên dùng không: 6/10 cho lúc này (dùng bản classic ổn định) — nên quay lại đánh giá lại
  khi bản rewrite có MCP server + headless mode release chính thức, lúc đó điểm sẽ tăng vì
  khớp thẳng nhu cầu automation video của content factory.

## Link
- Repo (rewrite, đang phát triển): https://github.com/OpenCut-app/OpenCut
- Repo (bản classic, dùng được ngay): https://github.com/opencut-app/opencut-classic
- Docs/Demo: https://opencut.app

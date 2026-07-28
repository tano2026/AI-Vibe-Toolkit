# TikTok Ads/Posting MCP — MCP Server

## TL;DR
TikTok **công bố** MCP chính thức tại TikTok World 13/5/2026, nhưng **CHƯA generally available** (không có endpoint public, không docs, không ngày ra mắt) tính tới thời điểm gần nhất được ghi nhận. Muốn dùng THẬT ngay bây giờ phải qua bên thứ 3: **Outstand** (post nội dung, đã live từ 3/2026) hoặc **Pipeboard** (quản lý ads đa nền tảng gồm TikTok).

## Dùng để làm gì
**Outstand** (`mcp.outstand.so/mcp`) — 27 tool trên 11 platform, riêng TikTok qua Official Content
Posting API: `create_post` (đăng/lên lịch video, ảnh), `get_post_analytics` (view/like/comment/
share), `list_posts`, `upload_media`. Không cần tự đăng ký TikTok Developer App — Outstand quản
lý OAuth luôn. $19/tháng, 3000 post đi kèm.

**Pipeboard** — quản Meta + Google + TikTok + Snap + Reddit Ads trong 1 kết nối, có gói free.
Hợp nếu cần nhìn tổng ads đa nền tảng cùng lúc thay vì riêng TikTok.

## Setup từng bước
**Outstand (đăng nội dung TikTok/đa nền tảng):**
```bash
claude mcp add -t http \
  -H "Authorization: Bearer ost_your_key" \
  outstand https://mcp.outstand.so/mcp
```
Không cần đăng ký TikTok Developer App riêng — connect qua OAuth hosted của Outstand.

**Pipeboard (quản ads đa nền tảng gồm TikTok):**
Đăng ký tại pipeboard.co, connect tài khoản TikTok Ads, thêm MCP server vào Claude theo hướng
dẫn trên trang — có gói free để thử trước.

## Ví dụ thực tế
Đăng video mới cho kênh Trùm Sân Bay lên TikTok + đồng thời Instagram Reels/Facebook — dùng
Outstand, 1 lệnh `create_post` với danh sách platform, không phải tự đăng tay từng nền tảng.

## Lưu ý / Lỗi thường gặp
- **KHÔNG nhầm MCP TikTok chính thức đã có sẵn** — tính tới thời điểm ghi nhận gần nhất, TikTok
  mới DỰ ĐỊNH, chưa có endpoint public. Mọi nguồn quảng cáo "TikTok MCP chính thức" hiện tại đều
  là bên thứ 3 dùng lại TikTok Official API có sẵn (Content Posting API), không phải MCP do
  TikTok trực tiếp vận hành.
- Outstand/Pipeboard đều thu phí — kiểm tra hạn mức post/tháng có đủ nhịp đăng của Trùm Sân
  Bay/Tano Cafe không trước khi cam kết gói trả phí.
- Khi TikTok ra MCP chính thức thật (theo mô hình Meta: OAuth-native, không rủi ro khoá tài
  khoản như dùng personal token) — nên chuyển sang dùng bản chính thức, các bên thứ 3 này chỉ
  là giải pháp tạm trong lúc chờ.

## Đánh giá cá nhân
- Điểm mạnh: dùng được NGAY hôm nay (khác chờ TikTok chính thức chưa biết ngày ra mắt); Outstand
  gọn cho việc đăng nội dung, Pipeboard hợp nếu cần nhìn ads đa nền tảng 1 chỗ.
- Điểm yếu: đều là lớp trung gian bên thứ 3, phụ thuộc dịch vụ đó còn duy trì hay không; tốn phí
  hàng tháng thay vì miễn phí như Meta MCP đang trong giai đoạn beta.
- Có nên dùng không: 7/10 — dùng tạm cho nhu cầu đăng bài thật ngay bây giờ, theo dõi tin TikTok
  MCP chính thức ra mắt để chuyển sau.

## Link
- Outstand: https://www.outstand.so/mcp/tiktok
- Pipeboard: https://pipeboard.co/guides/tiktok-ads-mcp

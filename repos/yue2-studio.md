# YuE2 Studio — GitHub Repo

## TL;DR
App desktop tạo nhạc AI đầy đủ (lời + hát + nhạc đệm) chạy local trên GPU của mày, dựa trên model mở YuE2 (M-A-P) — chất lượng cạnh tranh trực tiếp với Suno v5/v6 theo benchmark công bố. Có bản Windows tích hợp sẵn MCP server cho Claude gọi trực tiếp.

## ⚠️ Cảnh báo quan trọng nhất — license giới hạn thương mại

```
Studio (phần mềm bọc ngoài): MIT/Apache-2.0 — dùng thoải mái
Model weights YuE2/SheetSage2 (phần TẠO RA nhạc thật):
  CC BY-NC 4.0 — CHỈ dùng phi thương mại
```

**Ảnh hưởng trực tiếp tới Tano Agency:** nếu dùng nhạc tạo ra để đăng content bán hàng/quảng cáo cho ABTRIP/Tano Cafe/Wonder Mart (mục đích thương mại) — **vi phạm license**. Chỉ an toàn cho thử nghiệm cá nhân/nội dung phi thương mại, hoặc phải tự liên hệ tác giả model xin giấy phép thương mại riêng.

## Repo này dùng để làm gì
Nhận lời bài hát + mô tả phong cách → **viết bản nhạc (score) TRƯỚC**, có thể sửa tay, rồi mới tổng hợp thành bài hát hoàn chỉnh có giọng hát + nhạc đệm — khác cách tạo trực tiếp "đoán mò" của nhiều tool khác. Hỗ trợ cover bài có sẵn (khoá đúng giai điệu gốc), chuyển giọng (RVC/Seed-VC), master âm thanh.

## Nhiều bản fork khác nhau — chọn đúng theo nền tảng

| Fork | Nền tảng | Điểm khác biệt |
|---|---|---|
| `smittyPNW/YuE-Studio` | macOS (Apple Silicon) | Bản gốc do Tony Weston khởi tạo |
| `timoncool/YuE2-Studio` | **Windows** | **Có MCP server sẵn** — `claude mcp add --transport http yue2-studio http://127.0.0.1:8791/mcp`, kèm `docs/mcp-skill.md` cho agent đọc |
| `suoya437-oss/YuE2-Studio` | Cloud/Linux GPU (≥24GB) | Deploy qua script, dùng khi không có GPU máy local đủ mạnh |

Với máy Windows đã có (theo local skill index đã thấy), **`timoncool/YuE2-Studio` khớp nhất** — vừa đúng OS, vừa có MCP tích hợp sẵn.

## Setup từng bước (bản Windows, timoncool)
1. Tải installer từ GitHub Releases (`YuE2.Studio_x.x.x_x64-setup.exe`) hoặc bản portable
2. Cài, mở app lần đầu — tự tải model từ trong studio (không cần tải tay)
3. Kết nối Claude: `claude mcp add --transport http yue2-studio http://127.0.0.1:8791/mcp`
4. Claude đọc `docs/mcp-skill.md` để biết đúng cách gọi — quy trình: viết score trước → sửa lời/nhạc nếu cần → tổng hợp bài hát

## Ví dụ thực tế
Kênh "Giải Mã Số Phận" cần nhạc nền phù hợp không khí tâm linh/tử vi — có thể thử tạo nhạc nền riêng thay vì dùng nhạc có sẵn (né bản quyền nhạc thương mại) — nhưng PHẢI kiểm tra kỹ license CC BY-NC trước, kênh này nếu có kiếm tiền/quảng cáo thì tính là mục đích thương mại.

## Lưu ý / Lỗi thường gặp
- Cần GPU đủ mạnh (bản nhẹ nhất Q5_K_M vẫn cần tài nguyên đáng kể) — kiểm tra cấu hình máy trước khi cài
- Nhầm giữa `YuE-Studio` (không số 2, macOS, ít tính năng hơn) và `YuE2-Studio` (bản đầy đủ, có score editing) — dễ tải nhầm bản cũ

## Đánh giá cá nhân
- Điểm mạnh: chất lượng cạnh tranh Suno, chạy local không tốn subscription, bản Windows có MCP tích hợp sẵn cho Claude — setup nhanh
- Điểm yếu: **license non-commercial là rào cản thật cho use case Tano Agency** (bán dịch vụ, cần thương mại hoá được) — không phải "có nên dùng" mà là "có được phép dùng cho mục đích thương mại không", câu trả lời hiện tại là KHÔNG
- Có nên dùng: 5/10 cho Tano Agency cụ thể (giảm điểm nặng vì rào cản license, dù kỹ thuật tốt) — 8/10 nếu chỉ dùng thử nghiệm cá nhân không mục đích thương mại

## Link
- Model gốc: https://map-yue2.github.io/ (M-A-P, Tokenwave.AI, MBZUAI, ACE Studio)
- Bản Windows + MCP: https://github.com/timoncool/YuE2-Studio
- Bản macOS gốc: https://github.com/smittyPNW/YuE-Studio

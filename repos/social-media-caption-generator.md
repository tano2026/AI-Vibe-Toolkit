# Social Media Caption Generator (rediumvex/theromanknox) — GitHub Repo

## TL;DR
1 prompt vào → caption tối ưu riêng cho từng nền tảng (Instagram Reels, Carousel, TikTok, Threads, Facebook, YouTube Shorts) ra cùng lúc — mỗi caption kèm breakdown công thức/loại hook/loại CTA đã dùng. MIT, public thật, tác giả dùng chính cho tài khoản 280K follower của mình.

## Repo này dùng để làm gì
Vấn đề: đa số creator copy-paste 1 caption cho mọi nền tảng — mất reach vì mỗi thuật toán 2026 thưởng tín hiệu khác nhau. Skill này viết riêng caption cho từng nền tảng theo đúng tín hiệu thuật toán đó, không dùng hashtag rác kiểu #fyp #viral, không câu tương tác giả trân, không dùng từ khoá bị Facebook hạ reach.

## Setup từng bước
```bash
cd ~/.claude/skills
git clone https://github.com/rediumvex/social-media-caption-generator-claude.git social-captions
```
Restart Claude Code, gọi qua `/social-captions`.

## Ví dụ thực tế
Video mới cho Tano Cafe (clip cà phê sáng) → đưa script/mô tả video vào skill → ra 6 bản caption riêng biệt cho IG Reels, Carousel, TikTok, Threads, Facebook, YouTube Shorts, mỗi bản đúng "giọng" thuật toán nền tảng đó — đăng đồng loạt mà không phải tự viết lại 6 lần.

## Lưu ý / Lỗi thường gặp
- Input tốt nhất là script/text/screenshot có nội dung rõ ràng — mô tả mơ hồ ra caption chung chung.
- Không thay được giọng văn thương hiệu riêng (vd tông GMSP) — cần review lại trước khi đăng.

## Đánh giá cá nhân
- Có nên dùng không: 8/10 — tiết kiệm đúng khâu tốn thời gian nhất (30 phút/post viết caption đa nền tảng theo tác giả tự ước tính), hợp cho nhịp đăng hàng ngày Trùm Sân Bay/Tano Cafe.

## Link
- Repo: https://github.com/rediumvex/social-media-caption-generator-claude

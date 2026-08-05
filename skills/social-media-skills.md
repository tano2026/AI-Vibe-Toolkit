# Social Media Skills — Prompt Template / System Prompt

## TL;DR
Bộ skill mã nguồn mở (charlie947/social-media-skills, mở rộng thành social-media-skills/skills với 106 skill) phủ toàn bộ vòng đời content: chiến lược, viết, video, design, đăng bài, phân tích. Điểm mạnh nhất: mọi skill đều đọc chung 1 file `voice.md`/`about-me.md` làm nền — không viết lệch giọng thương hiệu giữa các skill khác nhau.

## Khi nào dùng
- Cần chuẩn hoá giọng viết xuyên suốt nhiều kênh (Trùm Sân Bay, Airfare Decoded, GMSP) mà không lệch tone giữa các lần tạo content khác nhau.
- Muốn 1 bộ skill có sẵn thay vì tự viết lại từng skill lẻ (hook-writer, caption-writer, content-pillars...) như đang làm thủ công trong kho.
- Không dùng khi: chỉ cần 1 tác vụ đơn lẻ nhanh — bộ này có giá trị nhất khi dùng nhiều skill liên tục trên cùng 1 nền voice, không phải cho việc dùng 1 lần.

## Nội dung skill / prompt
Không phải 1 prompt đơn — là bộ 17-106 skill riêng biệt, mỗi skill 1 folder chuẩn `SKILL.md` + `evals/`, `references/`, `scripts/`. Cấu trúc lõi:
```
voice-builder       → phỏng vấn + phân tích mẫu viết, ra about-me.md + voice.md (NỀN TẢNG — mọi skill khác đọc file này trước khi viết)
brand-profile        → hồ sơ thương hiệu
audience-research     → nghiên cứu đối tượng
content-pillars       → trụ cột nội dung
content-calendar      → lịch đăng
hook-writer            → viết hook mở đầu
caption-writer          → viết caption
short-form-video-script  → kịch bản video ngắn
cross-platform-repurposing → chuyển 1 nội dung thành nhiều định dạng
engagement-routine       → thói quen tương tác
scheduling-and-queue      → lên lịch đăng
```

## Setup từng bước
1. Cách nhanh với Claude: Customize → Skills → + Create skill → upload từng file ZIP trong pack (yêu cầu bật code execution trong Settings).
2. Với OpenClaw: copy folder skill vào `~/.openclaw/skills/` — theo đúng chuẩn SKILL.md OpenClaw đang dùng.
3. Với Hermes (nếu build theo chuẩn tương thích): copy vào `~/.hermes/skills/` hoặc thư mục `skills/` của project.
4. **Bước bắt buộc đầu tiên:** chạy `voice-builder` trước — mọi skill khác phụ thuộc `about-me.md`/`voice.md` do bước này tạo ra, bỏ qua bước này các skill sau sẽ viết generic.
5. Cài chọn lọc, không cài hết 106 skill cùng lúc — chỉ cài đúng nhóm cần (vd chỉ content-calendar + hook-writer + caption-writer nếu chỉ cần vòng lặp viết-đăng cơ bản).

## Ví dụ thực tế
Chạy `voice-builder` cho kênh **Airfare Decoded** (tiếng Anh, B2B, aviation) riêng biệt với kênh **Trùm Sân Bay** (tiếng Việt, TikTok, casual) — 2 file `voice.md` khác nhau. Sau đó mọi skill viết caption/script cho từng kênh tự động bám đúng giọng riêng, không lẫn giữa 2 kênh dù dùng chung bộ skill.

## Lưu ý / Lỗi thường gặp
- **Bỏ qua `voice-builder` là lỗi phổ biến nhất** — skill khác vẫn chạy được nhưng ra content generic, mất hết lợi thế của bộ này.
- Có nhiều fork trùng tên (`charlie947/social-media-skills` bản gốc 17 skill, `blacktwist/social-media-skills` bản khác, `social-media-skills/skills` bản mở rộng 106 skill) — kiểm tra đúng nguồn trước khi cài, tránh lẫn version.
- Một số skill tạo ảnh (gemini-infographic, gemini-carousel, quote-post) chỉ ra **prompt để dán vào tool khác**, không tự sinh ảnh — giống lỗi "Gemini không edit video thật" đã ghi nhận ở skill Gemini Video Content Kit.

## Đánh giá cá nhân
- Điểm mạnh: kiến trúc "1 nguồn giọng, nhiều skill dùng chung" là pattern tốt nhất trong các bộ skill content đã research — giải đúng vấn đề giọng lệch giữa các kênh của Tano.
- Điểm yếu: 106 skill là quá nhiều để cài hết, dễ ngợp; phải tự chọn lọc đúng nhóm cần, không có hướng dẫn ưu tiên rõ ràng cho từng loại kênh (aviation B2B khác hẳn TikTok casual).
- Có nên dùng không: 7/10 — pattern voice-builder đáng học và áp dụng cho toàn bộ kênh Tano, nhưng nên chọn lọc kỹ, không copy nguyên bộ.

## Link
- Repo gốc: https://github.com/charlie947/social-media-skills
- Repo mở rộng (106 skill): https://github.com/social-media-skills/skills
- Trang cài đặt: https://www.social-media-skills.com/

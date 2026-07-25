# AI Video Generator (rediumvex/theromanknox) — GitHub Repo

## TL;DR
10 skill viết prompt cho Seedance 2.0 (qua Higgsfield) — mô tả ý tưởng ngắn, ra prompt 15-25 dòng chuẩn production (timing, góc máy, ánh sáng, âm thanh) paste thẳng vào Higgsfield. Của Roman Knox (@theromanknox, 280K IG) — repo public thật, dùng chính trong công việc thật của tác giả.

## Repo này dùng để làm gì
Đây KHÔNG phải tool tự sinh video — là skill viết **prompt cho người khác/model khác sinh video**. Đưa ý tưởng ngắn kiểu "video 10s ra mắt sản phẩm, giao diện tối, tối giản" → skill trả về prompt Seedance 2.0 đầy đủ: hook 2 giây đầu (10+ pattern giật attention), hướng chuyển động camera (dolly/orbit/whip pan/snap zoom/rack focus), preset ánh sáng, thiết kế âm thanh — copy thẳng vào Higgsfield là chạy.

## Setup từng bước
```bash
mkdir -p ~/.claude/skills
git clone https://github.com/rediumvex/ai-video-generator-claude.git ~/.claude/skills/ai-video-generator
```
Restart Claude Code, gọi bằng mô tả ý tưởng tự nhiên — skill tự nhận diện và trả prompt.

## Ví dụ thực tế
Cần B-roll động cho video giới thiệu Fast Track Nội Bài trên kênh Trùm Sân Bay — mô tả: "video 8 giây, cảnh sân bay sang trọng, tông Deep Navy + Hanoi Gold, cảm giác VIP fast track" → skill trả prompt Seedance 2.0 đầy đủ, paste vào Higgsfield ra clip mà không cần tự nghĩ thuật ngữ đạo diễn (dolly-in, rack focus...).

## Lưu ý / Lỗi thường gặp
- Chỉ viết PROMPT, không tự sinh video — vẫn cần tài khoản Higgsfield/Seedance 2.0 để chạy ra clip thật (có phí theo nền tảng đó).
- MIT license — tác giả ghi rõ "fork it, modify it, ship it in your product".

## Đánh giá cá nhân
- Có nên dùng không: 7.5/10 — hợp cho B-roll nhanh cho Trùm Sân Bay/kênh AI review, tiết kiệm công tự nghĩ thuật ngữ đạo diễn khi viết prompt video AI.

## Link
- Repo: https://github.com/rediumvex/ai-video-generator-claude

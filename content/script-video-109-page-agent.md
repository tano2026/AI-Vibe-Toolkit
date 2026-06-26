# Script Video 109 — Page Agent: Control Web Bằng Tiếng Tự Nhiên, Không Cần Backend

## Thông tin
- Repo liên quan: /repos/page-agent.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~55 giây

## Hook (3 giây đầu)
"Điều khiển bất kỳ web app nào bằng câu nói. Không cần Playwright, không cần server."

## Script voiceover (ElevenLabs-ready)
[Đoạn 1 — pain point]
Playwright, Selenium — muốn tự động hóa web phải setup server, viết selector, xử lý timing. Phức tạp.

[Đoạn 2 — giải pháp]
Page Agent của Alibaba là JavaScript library nhúng thẳng vào trang. Mày gọi `agent.act("Click nút Submit")` — nó tự tìm, tự click. Hoặc `agent.query("Giá bao nhiêu?")` — trả về con số thật.

[Đoạn 3 — demo]
Không cần biết CSS selector. Không cần Puppeteer server. Chỉ cần npm install, 5 dòng code, và API key Claude. Web app của mày có natural language interface ngay lập tức.

[Đoạn 4 — kết + CTA]
19.8 nghìn star. Alibaba ra. Dùng ngay cho automation test hoặc add AI control vào web app. Link trong bio.

## Ghi chú quay (OBS)
- Cảnh 1: Code đơn giản — agent.act("...") chỉ vài dòng
- Cảnh 2: Demo real-time: agent click, fill form, query UI
- Cảnh 3: So sánh vs Playwright (nhiều code hơn nhiều)

## Thumbnail idea (Canva)
Browser window + chat bubble "Click nút Submit". Text: "Control Web = 1 câu nói"

## CTA cuối video
"Follow nếu mày muốn build web app có AI control. Link Page Agent trong bio."

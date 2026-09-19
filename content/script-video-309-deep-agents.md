# Script Video 309 — Deep Agents

## Thông tin
- Tool/Repo/Skill liên quan: /repos/deep-agents.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

## Hook (3 giây đầu)
"LangChain vừa đóng gói sẵn 'bộ giáp' Claude Code cho mọi model."

## Script voiceover (ElevenLabs-ready)
[Đoạn 1 — vấn đề/pain point]
Muốn agent tự lập kế hoạch, đọc ghi file, gọi được sub-agent riêng, tự tóm gọn hội thoại dài, bình thường phải tự ghép từng phần trên LangGraph, tốn cả tuần mới ra được khung sườn ổn.

[Đoạn 2 — giới thiệu giải pháp]
Deep Agents gói sẵn hết bốn thứ đó vào một hàm, gọi là có agent chạy được ngay, và mọi phần đều chỉnh lại được nếu không thích mặc định. Không kén model, chạy được với OpenAI, Anthropic, Google, hay cả model chạy local.

[Đoạn 3 — demo/cách làm]
Cài bằng một dòng lệnh, viết vài dòng Python là xong. Agent tự lập danh sách việc cần làm, tách việc con ra cho sub-agent riêng để không bị tràn context khi làm task dài.

[Đoạn 4 — kết + CTA]
Hai mươi bảy nghìn năm trăm sao trên GitHub, đứng sau là chính LangChain nên tài liệu rất dày. Có một điều quan trọng phải nhớ, đây theo triết lý tin tưởng hoàn toàn vào model, nên phải tự chặn ở tầng công cụ chứ không trông chờ agent tự biết dừng. Link cài đặt tao để trong kho, comment "deep agent" là gửi.

## Ghi chú quay (OBS)
- Cảnh 1: Hình ảnh code rối rắm tự ghép agent bằng tay — lúc hook/pain point
- Cảnh 2: Logo Deep Agents + list 4 tính năng (planning, filesystem, sub-agent, context) — lúc giới thiệu
- Cảnh 3: Terminal gõ `uv add deepagents` rồi code mẫu chạy `agent.invoke()` — lúc demo
- Cảnh 4: Show GitHub star 27.5k — lúc kết

## Caption/Sub note (CapCut)
Highlight: "gói sẵn hết", "không kén model", "tự lập danh sách việc cần làm", "tin tưởng hoàn toàn vào model". Nhấn mạnh cảnh báo bảo mật ở đoạn cuối bằng màu chữ đỏ/cam.

## Thumbnail idea (Canva)
Icon robot mặc "bộ giáp" (planning, filesystem, sub-agent, context như từng mảnh giáp ghép vào), text to: "1 DÒNG LỆNH = AGENT ĐẦY ĐỦ GIÁP".

## CTA cuối video
Comment "deep agent" nhận link cài đặt + ví dụ code mẫu, follow để xem thêm thư viện agent đáng dùng.

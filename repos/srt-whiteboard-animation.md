# SRT Whiteboard Animation — GitHub Repo

## TL;DR
Chuyển file phụ đề SRT thành video hoạt hình vẽ tay phong cách bảng trắng (nền giấy vàng kem ấm, nét bút chảy dần) — mỗi cảnh vẽ theo đúng thứ tự phụ đề. Bản gốc `geeklee/srt-whiteboard-animation` 2,6k sao, 421 fork — có nhiều fork mô tả y hệt (zjx516500, HuyAK47, 899ms, chixig...), dùng đúng bản gốc này.

## Repo này dùng để làm gì
Nhận file SRT (phụ đề đã có sẵn, từ voiceover/TTS) → tự tách cảnh theo thứ tự kể chuyện → tạo storyboard + line art → render thành video MP4 nét bút vẽ tay chảy liên tục (ink→màu). Hợp cho: giảng giải kiến thức, kể chuyện bằng giọng đọc, phụ đề khoá học, kịch bản video ngắn.

**Điểm thiết kế hay nhất:** *"subtitle-driven, step-by-step confirmation"* — mỗi bước (storyboard/line art/annotation) đều DỪNG LẠI chờ xác nhận trước khi render — tránh phí tài nguyên render khi bản nháp chưa chốt.

## Bản nâng cao hơn, đáng biết — `storyboard-ai` (khác tác giả)

Repo `yogendra-yatnalkar/storyboard-ai` đi xa hơn: nhận **1 câu prompt text** (không cần SRT có sẵn) → tự động cả pipeline (tạo ảnh, canh giọng đọc, ghép video) → có thể tích hợp **Veo** để chèn đoạn video AI thật vào giữa các cảnh vẽ tay. Phức tạp hơn, cần GPU/SAM 3 nếu bật segmentation.

## Setup từng bước (bản geeklee, đơn giản hơn)
1. Clone repo, chạy `prepare_env.py` — lệnh đầu tiên xuất ra `ENV_PY=<đường dẫn>`, dùng đúng Python này cho các bước render sau (cách ly dependency)
2. `parse_srt.py` — đọc file SRT, tự đề xuất cách chia cảnh
3. Xác nhận từng bước (storyboard → line art → annotation) trước khi render — ĐÚNG THEO THIẾT KẾ, không bỏ qua bước xác nhận
4. `render_stream_whiteboard.py` — render MP4 nét vẽ tay
5. `merge_scenes.py` nếu có nhiều cảnh cần ghép lại

## Ví dụ thực tế
Kênh GMSP (Giải Mã Số Phận) cần giải thích khái niệm tử vi/triết lý — phong cách vẽ tay bảng trắng hợp với nội dung "giảng giải kiến thức" hơn video quay thật hay ảnh AI photorealistic. Luồng: Content Pro viết kịch bản → TTS tạo voiceover + SRT → công cụ này vẽ animation theo đúng nhịp phụ đề.

## Lưu ý / Lỗi thường gặp
- Nhiều fork mô tả y hệt bản gốc (đúng kiểu FlowKit trước đây) — dùng `geeklee/srt-whiteboard-animation` (nhiều sao/fork nhất, có Activity log thật)
- File `agents/openai.yaml` trong repo cho thấy metadata hướng về **Codex** — chưa xác nhận chạy mượt trên Claude Code, cần test trước khi tin dùng production
- Cần SRT có sẵn (không tự tạo giọng đọc) — phải có bước TTS trước đó trong pipeline

## Đánh giá cá nhân
- Điểm mạnh: cơ chế "dừng xác nhận từng bước trước khi render" rất đáng học — tránh phí tài nguyên, đúng tinh thần thận trọng đã áp dụng nhiều nơi khác trong kho; phong cách vẽ tay khác biệt, không giống mọi tool AI-generated ảnh khác đã có
- Điểm yếu: hướng về Codex (chưa xác nhận Claude Code dùng mượt), quy trình nhiều bước hơn so với gọi thẳng 1 API ảnh
- Có nên dùng: 7/10 — đáng thử cho GMSP/nội dung giảng giải, chưa nên dùng cho pipeline chính (ABTRIP/Trùm Sân Bay) vốn đã có google-flow-mcp chạy ổn

## Link
- Bản gốc: https://github.com/geeklee/srt-whiteboard-animation (2.6k sao, 421 fork)
- Bản nâng cao (text-to-video, có Veo): https://github.com/yogendra-yatnalkar/storyboard-ai

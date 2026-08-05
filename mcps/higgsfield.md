# Higgsfield — MCP Server

> ⚠️ **Lưu ý trùng tên:** Tài liệu chính thức của Higgsfield MCP nhắc tới việc
> tương thích với "OpenClaw" và "Hermes Agent" như tên framework agent phổ
> biến ngoài cộng đồng. Đây là trùng tên ngẫu nhiên với 2 agent nội bộ của Tano
> (OpenClaw = orchestrator VPS, Hermes = executor Python) — không phải cùng 1
> hệ thống, không liên quan gì tới nhau.

## TL;DR
MCP chính thức của Higgsfield — mở khoá 30+ model tạo ảnh/video cinematic (Veo 3.1, Kling 3.0, Sora 2, Seedance, Soul, Cinema Studio) ngay trong chat, không cần API key, không cần vào từng web riêng của mỗi model.

## Tool này dùng để làm gì
Claude nhận mô tả cảnh quay bằng ngôn ngữ tự nhiên, tự chọn model phù hợp (hoặc theo tên model chỉ định), viết prompt đúng format riêng của model đó, gọi generate, và trả kết quả ảnh/video thẳng vào chat.

## Setup từng bước
1. Trong Claude web/desktop: Settings → Connectors → thêm "Higgsfield" → xác thực OAuth qua tài khoản Higgsfield (không cần API key thủ công).
2. Có 5 tool chính: `generate_image`, `generate_video`, train character (giữ nhân vật nhất quán qua nhiều cảnh), browse lịch sử tạo, và style preset.
3. Test: "tạo ảnh sản phẩm [tên] đặt trên mặt bàn đá cẩm thạch, ánh sáng buổi sáng ấm" — kiểm tra output trước khi dùng cho việc thật.
4. Muốn dùng ngoài Claude (Hermes/OpenClaw thật của Tano): cần server MCP riêng qua FastMCP wrapper (vd `geopopos/higgsfield_ai_mcp` trên GitHub) với `HF_API_KEY`/`HF_SECRET` — bản này cần API key, khác bản hosted không cần key.

## Ví dụ thực tế
Cho kênh **AI review (TikTok/Shorts)**: mô tả "cảnh mở đầu điện thoại rơi chậm xuống bàn, slow motion cinematic, ánh sáng neon" — Higgsfield tự chọn model video phù hợp (kiểu Cinema Studio) và trả clip 5-10 giây dùng làm B-roll, không cần quay dựng thật.

## Lưu ý / Lỗi thường gặp
- Bản hosted (không cần key) tiện nhưng gắn với tài khoản Higgsfield — chi phí theo credit của họ, cần kiểm tra hạn mức trước khi dùng batch lớn.
- Chất lượng video phụ thuộc model được chọn tự động — với brief phức tạp nên chỉ định rõ tên model muốn dùng thay vì để tự chọn.
- Đừng nhầm tên "OpenClaw"/"Hermes Agent" trong tài liệu Higgsfield với agent thật của Tano — 2 hệ thống hoàn toàn khác nhau dù trùng tên.

## Đánh giá cá nhân
- Điểm mạnh: gom 30+ model vào 1 kết nối, không cần học prompt riêng từng model, tiết kiệm thời gian brainstorm B-roll cho content video.
- Điểm yếu: phụ thuộc credit/tài khoản Higgsfield, chưa rõ chi phí dài hạn nếu dùng volume cao cho nhiều kênh cùng lúc.
- Có nên dùng không: 7/10 — đáng thử cho B-roll/thumbnail động của Trùm Sân Bay và AI review channel, cần theo dõi chi phí trước khi đưa vào pipeline chính thức.

## Link
- MCP hosted: https://mcp.higgsfield.ai
- Repo self-host (cần API key): https://github.com/geopopos/higgsfield_ai_mcp
- Docs: https://higgsfield.ai/mcp

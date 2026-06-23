# Script Video 82 — codebase-memory-mcp

## Thông tin
- Tool/Repo liên quan: /mcps/codebase-memory-mcp.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~55 giây

## Hook (3 giây đầu)
"AI hay quên cấu trúc project lớn? MCP này giải quyết luôn — 11 nghìn sao trên GitHub."

## Script voiceover (ElevenLabs-ready)
[Đoạn 1 — vấn đề]
Bạn đang code project 500 file với Claude hay Cursor. Hỏi một câu đơn giản — function này ở đâu — AI phải đọc lại cả đống file, tốn 8000 token, đôi khi vẫn trả lời sai.

[Đoạn 2 — giải pháp]
codebase-memory-mcp là MCP server hơn 11 nghìn sao. Nó index toàn bộ codebase của mày thành một knowledge graph — 158 ngôn ngữ, index trong millisecond. Mỗi lần AI hỏi, nó query graph này thay vì đọc lại từ đầu.

[Đoạn 3 — demo]
Mình test trên Next.js app 500 file. Cùng câu hỏi "function handleAuth ở đâu" — trước đây tốn 8000 token, không chắc đúng. Sau khi cài MCP này: 200 token, trả lời ngay tên file và số dòng. Chính xác 100%.

[Đoạn 4 — kết + CTA]
Nếu bạn vibe code với project lớn, đây là MCP bắt buộc phải có. Tiết kiệm token là tiết kiệm tiền API thật sự. Link trong bio. Follow để xem thêm tool như này.

## Ghi chú quay (OBS)
- Cảnh 1: GitHub repo DeusData/codebase-memory-mcp — show 11.5k stars
- Cảnh 2: File claude_desktop_config.json — show thêm MCP config
- Cảnh 3: Claude Code — so sánh before/after token count
- Cảnh 4: Knowledge graph visualization (nếu có trong repo)

## Caption/Sub note (CapCut)
- Highlight: "11k sao", "158 ngôn ngữ", "tiết kiệm token", "millisecond"
- Cắt cảnh tại giây 12 (sang demo config), giây 32 (sang so sánh before/after)

## Thumbnail idea (Canva)
Nền tối, icon não bộ (brain) ở giữa với các đường kết nối ra nhiều file code xung quanh. Text: "AI NHỚ TOÀN BỘ CODE CỦA MÀY". Badge "11K STARS" góc trên.

## CTA cuối video
"npm install một lệnh — đọc README để config xong trong 5 phút."

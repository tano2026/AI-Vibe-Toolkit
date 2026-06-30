# Script Video — FreeLLMAPI

## Thông tin
- Tool/Repo liên quan: /repos/freellmapi.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

## Hook (3 giây đầu)
"1.7 tỷ token miễn phí mỗi tháng. 16 provider. 1 endpoint. Cài 30 giây."

## Script voiceover (ElevenLabs-ready)

[Đoạn 1 — pain point]
Mày đang code, tự nhiên Groq báo rate limit. Switch sang Gemini. Gemini cũng hết. Switch tiếp sang Mistral. Ba cửa sổ terminal, ba API key, mà vẫn bị block. Tao thấy nhiều người làm vậy lắm.

[Đoạn 2 — giới thiệu]
FreeLLMAPI gom hết 16 provider miễn phí đó thành 1 endpoint duy nhất. Groq, Gemini, Cerebras, Mistral, GitHub Models... tất cả ở sau 1 địa chỉ localhost:3001. Tool của mày chỉ biết 1 endpoint đó thôi.

[Đoạn 3 — features]
Hết quota provider này? Tự failover sang cái khác, thử lại 20 lần. Mày không cần làm gì. ~1.7 tỷ token tổng cộng mỗi tháng, hoàn toàn miễn phí. Format OpenAI-compatible — cắm vào Claude Code, Cursor, Hermes, OpenClaw là chạy, không cần sửa code.

[Đoạn 4 — kết + CTA]
Cài bằng 1 lệnh curl. 14 nghìn sao. Link repo trong bio.

## Ghi chú quay (OBS)
- Cảnh 1: Split screen 3 terminal đang bị "rate limit exceeded" ở 3 provider khác nhau
- Cảnh 2: Diagram: [Claude Code / Cursor / Hermes] → [FreeLLMAPI :3001] → [16 providers]
- Cảnh 3: Terminal: `curl -fsSL https://freellmapi.co/install.sh | bash` → done trong <30s
- Cảnh 4: Dashboard FreeLLMAPI — provider list, token stats, failover log

## Caption/Sub note (CapCut)
- Highlight: "1.7 TỶ TOKEN MIỄN PHÍ", "16 PROVIDER", "TỰ ĐỘNG FAILOVER"
- Sub chữ lớn khi nói "localhost:3001"

## Thumbnail idea (Canva)
Logo Groq + Gemini + Cerebras + Mistral bay vào logo FreeLLMAPI ở giữa. Text lớn: "1.7B TOKEN FREE/THÁNG". Background tối, accent màu xanh lá.

## CTA cuối video
"Comment 'TOKEN' nếu mày muốn danh sách đầy đủ 16 provider miễn phí và quota từng cái."

## So sánh với OmniRoute (nếu làm video so sánh)
- FreeLLMAPI: đơn giản hơn, setup nhanh hơn, 14.1K stars, focus free tier
- OmniRoute: compression token, 231 provider, Antigravity native, phức tạp hơn
- Stack tối ưu: dùng cả hai — FreeLLMAPI làm 1 provider trong OmniRoute fallback chain

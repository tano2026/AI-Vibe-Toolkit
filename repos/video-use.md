# video-use (browser-use) — GitHub Repo

## TL;DR
Dựng video từ footage thô bằng Claude Code, chỉ cần chat bằng tiếng tự nhiên — không dùng frame-dump (30,000 frame × 1,500 token = 45M token rác), mà đọc transcript + cắt theo ranh giới câu nói. 100% mã nguồn mở, dùng chung ElevenLabs API key đã có sẵn.

## Repo này dùng để làm gì
Thả footage thô vào 1 thư mục, chat với Claude Code, nhận về `final.mp4`. Cách hoạt động — khác hẳn cách AI thường "xem" video (dump từng frame ra ảnh, cực tốn token):
1. **Transcript trước (luôn load)** — gọi ElevenLabs Scribe 1 lần/nguồn, ra timestamp từng từ, phân biệt người nói, bắt cả sự kiện âm thanh (cười, vỗ tay, thở dài).
2. **LLM đọc transcript, không xem video** — 12KB text + vài ảnh PNG khi cần, thay vì hàng chục nghìn frame.
3. **Cắt theo ranh giới câu nói** — quy trình: Transcribe → Pack → LLM reasoning → EDL (edit decision list) → Render → Self-eval. Self-eval tự kiểm tra jump cảnh, audio pop, phụ đề ẩn tại mỗi điểm cắt, sai thì tự sửa + render lại (tối đa 3 lần) trước khi cho xem preview.
4. **Luôn hỏi xác nhận chiến lược cắt trước khi thực thi** — "Ask → confirm → execute → self-eval → persist", không tự ý cắt khi chưa được duyệt hướng.

Dùng được cho mọi loại nội dung: talking-head, phỏng vấn, montage, tutorial — không cần preset riêng từng loại.

## Setup từng bước
1. Clone và symlink vào thư mục skill của Claude Code:
```bash
git clone https://github.com/browser-use/video-use ~/Developer/video-use
ln -sfn ~/Developer/video-use ~/.claude/skills/video-use
```
2. Cài dependency:
```bash
cd ~/Developer/video-use
uv sync   # hoặc: pip install -e .
brew install ffmpeg   # bắt buộc
brew install yt-dlp   # optional, tải nguồn online
```
3. Thêm API key ElevenLabs (dùng cho bước transcribe — Tano Agency đã có sẵn key này trong tech stack):
```bash
cp .env.example .env
$EDITOR .env  # ELEVENLABS_API_KEY=...
```
4. Cách nhanh nhất: dán thẳng đoạn hướng dẫn cài đặt vào Claude Code, để nó tự clone + cài + xin key khi cần — README ghi rõ prompt mẫu cho việc này.
5. **Cho VPS/Telegram luôn bật:** có sẵn "Browser Use Box" — agent Claude Code 24/7 chạy chỉnh sửa video qua Telegram trên máy riêng, hợp mô hình always-on đang có với OpenClaw.

## Ví dụ thực tế
Có 1 giờ raw footage phỏng vấn cho GMSP Episode 01 (nhiều đoạn lặp, khoảng lặng, "à ừm" thừa) — thay vì tự ngồi CapCut nghe lại từng đoạn, thả file vào `video-use`, chat: "cắt bỏ khoảng lặng và câu lặp, giữ đúng mạch nội dung chính". Claude Code đọc transcript, đề xuất EDL, hỏi xác nhận trước khi render — ra bản cắt gọn kèm self-eval đã tự soi lỗi audio pop/jump cảnh.

## Lưu ý / Lỗi thường gặp
- Bắt buộc có ElevenLabs API key (chi phí theo mức dùng ElevenLabs hiện tại) — không chạy được nếu thiếu bước transcribe.
- Chỉ hoạt động khi agent (Claude Code/Codex) có thể discover được `SKILL.md` — qua thư mục skill toàn cục hoặc import trong CLAUDE.md/system-prompt, đúng quy ước đã dùng trong kho.
- README ghi rõ nguyên tắc "Do everything yourself" — agent tự lo hết việc cài đặt, chỉ hỏi user 2 thứ: API key và xác nhận trước khi `brew install` — không nên tự ý bỏ qua bước xác nhận này khi wire vào pipeline agent.
- Là công cụ CẮT GHÉP dựa trên footage có sẵn — không sinh video mới, không hợp cho việc cần motion graphics/animation (đó là việc của html-video/HyperFrames).

## Đánh giá cá nhân
- Điểm mạnh: cách tiếp cận "đọc transcript thay vì xem frame" cực kỳ tiết kiệm token và chính xác hơn (cắt đúng ranh giới câu nói, không cắt giữa từ); có self-eval loop tự sửa lỗi trước khi giao; tận dụng thẳng ElevenLabs key đã có sẵn trong stack, không phải trả thêm phí công cụ mới; có sẵn phương án always-on qua Telegram khớp mô hình OpenClaw đang dùng.
- Điểm yếu: phụ thuộc hoàn toàn ElevenLabs (chi phí theo dùng); chỉ mạnh cho content có thoại rõ ràng (talking-head, phỏng vấn) — kém hiệu quả với video không lời/nhạc nền chính.
- Có nên dùng không: 8.5/10 — rất hợp cho hậu kỳ GMSP/Airfare Decoded (nhiều thoại), tiết kiệm thời gian dựng đáng kể so với CapCut tay.

## Link
- Repo: https://github.com/browser-use/video-use
- SKILL.md: https://github.com/browser-use/video-use/blob/main/SKILL.md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# video-use là skill cho Claude Code, không phải REST API — Hermes không gọi trực tiếp.
# Nếu Hermes cần trigger việc dựng video, cách hợp lý: gửi task cho OpenClaw giao Claude Code
# xử lý (Claude Code đọc SKILL.md rồi tự chạy helpers/transcribe.py, render.py...).
```

### OpenClaw
```bash
git clone https://github.com/browser-use/video-use ~/Developer/video-use
ln -sfn ~/Developer/video-use ~/.claude/skills/video-use
cd ~/Developer/video-use && uv sync
# Thêm ELEVENLABS_API_KEY vào .env (key đã có sẵn trong stack Tano Agency)
```

### Antigravity
```bash
# Deploy "Browser Use Box" nếu muốn always-on video editing qua Telegram trên VPS riêng
# (không chạy chung VPS chính đang cõng Hermes/OpenClaw/Antigravity để tránh nghẽn tài nguyên)
```
> ⚠️ Video có thoại nhạy cảm (nội dung chưa công bố) không nên đẩy qua ElevenLabs Scribe nếu
> chưa xác nhận chính sách xử lý dữ liệu của ElevenLabs phù hợp với yêu cầu bảo mật content.

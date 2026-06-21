# Toonflow — Script Thành Phim Hoạt Hình Ngắn Tự Động

## TL;DR
Desktop app 10K+ stars biến script/tiểu thuyết thành animated short drama tự động. AI viết kịch bản, tạo storyboard, generate character và video. Cross-platform, deploy nhẹ. Hướng đi khác với content không lộ mặt: thay screen record bằng hoạt hình AI.

## Tool này dùng để làm gì
Toonflow là "nhà máy short drama AI" — nhập script hoặc đoạn tiểu thuyết vào, app tự động:

1. **AI scriptwriting** — phân tích và cấu trúc lại thành kịch bản có cảnh, có nhân vật
2. **Intelligent storyboarding** — tạo phân cảnh tự động, mỗi scene một keyframe
3. **Character generation** — tạo nhân vật consistent xuyên suốt video
4. **Video generation** — render thành animated video từng cảnh
5. **Export** — ghép lại thành video hoàn chỉnh

Stack: Electron + Vue3 + Node.js, chạy được trên Windows/Mac/Linux. Không cần server riêng.

## Setup từng bước
```bash
# Cách 1: Download bản release (dễ nhất)
# Vào https://github.com/HBAI-Ltd/Toonflow-app/releases
# Download bản phù hợp với OS (Windows .exe / Mac .dmg / Linux .AppImage)
# Cài như app thường

# Cách 2: Build từ source (nếu muốn customize)
git clone https://github.com/HBAI-Ltd/Toonflow-app
cd Toonflow-app
npm install
npm run dev

# Bước tiếp theo trong app:
# - Config API keys cho image/video gen (Stable Diffusion, FLUX, hoặc các API tương thích)
# - Nhập script hoặc text tiểu thuyết
# - Chọn style (anime, realistic, cartoon...)
# - Run pipeline
```

## Ví dụ thực tế
**Tình huống:** Muốn làm series content "top AI tools" dạng animated, không lộ mặt

1. Viết script: "Tập 1: Top 3 Claude Code skills hot nhất. Nhân vật: robot trẻ trung tên Vibe, giải thích từng tool..."
2. Nhập vào Toonflow, chọn style anime/cartoon
3. App generate: storyboard 10 scene, character Vibe nhất quán, video từng scene
4. Export video hoàn chỉnh ~60-90 giây
5. Add voiceover ElevenLabs + nhạc nền → TikTok

**Kết quả:** Content animated hoàn toàn, không cần screen record, không cần lộ mặt, character riêng có thể dùng nhiều video.

## Lưu ý / Lỗi thường gặp
- Cần API key cho image/video generation (FLUX, SD, hoặc các model tương thích) — đây là chi phí chính
- Generation mỗi video mất thời gian, đặc biệt nếu dùng local model
- Character consistency tốt nhưng không hoàn hảo 100% — đôi khi cần regenerate
- App chủ yếu phát triển cho thị trường CN, một số UI còn tiếng Trung dù có bản EN
- 10K stars nhưng community chủ yếu CN — support tiếng Anh còn hạn chế

## Đánh giá cá nhân
- **Điểm mạnh:** Ý tưởng độc đáo — animated content hoàn toàn AI, tạo được "mascot" riêng cho channel. Desktop app nhẹ, không cần cloud
- **Điểm yếu:** Chi phí API gen image/video không rẻ, character consistency chưa hoàn hảo, ecosystem CN nên support EN hạn chế
- **Có nên dùng không:** 6.5/10 — thú vị để experiment, nhưng với pipeline hiện tại (screen record) thì chưa cần thiết ngay. Theo dõi thêm 2-3 tháng xem cộng đồng EN phát triển không

## Link
- Repo: https://github.com/HBAI-Ltd/Toonflow-app
- Releases: https://github.com/HBAI-Ltd/Toonflow-app/releases
- Gitee (mirror): https://gitee.com/HBAI-Ltd/Toonflow-app

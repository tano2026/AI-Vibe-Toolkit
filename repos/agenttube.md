# AgentTube / youtube-automation-agent (darkzOGx) — GitHub Repo

## TL;DR
Repo mã nguồn mở (MIT, 2.5k sao, Node.js) tự vận hành 1 kênh YouTube từ A-Z: research chủ đề → viết script → tạo giọng đọc + hình ảnh → dựng video thật (MP4) → SEO → chờ duyệt → đăng → đọc analytics → tự học cải thiện vòng sau. Codename nội bộ trong code là "Lumen".

## Repo này dùng để làm gì
Đây không phải kiểu "AI viết script cho video" thông thường — nó chạy như 1 server Express (`npm start`, cổng 3456) có dashboard, với 7 agent chuyên biệt nối tiếp nhau (Content Strategy → Script Writer → Thumbnail Designer → SEO Optimizer → Production → Publishing → Analytics), có vòng feedback từ Analytics quay lại Strategy. Điểm khác biệt so với đa số repo "AI làm YouTube" khác trên GitHub: nó có cơ chế **fail-closed** thật sự — nếu giọng đọc lỗi/giả lập, video không được duyệt/lên lịch/đăng; nếu chưa qua "Production readiness check" (test thật kết nối YouTube + tạo/giải mã 1 MP4 thử), không cho chạy autonomous. Mọi bước sinh nội dung đều ghi checkpoint SQLite để resume khi bị timeout/crash giữa chừng.

## Setup từng bước
1. Yêu cầu: Node.js 18+, tài khoản Google + credentials YouTube Data API v3 (OAuth Desktop app), FFmpeg (tự cài qua `ffmpeg-static`)
2. Clone và cài:
```bash
git clone https://github.com/darkzOGx/youtube-automation-agent.git
cd youtube-automation-agent
npm install
npm run walkthrough   # wizard hỏi từng provider, test credentials, xin quyền YouTube
npm start
```
3. Mở `http://localhost:3456` — dashboard chính
4. Cấu hình ít nhất 1 AI text provider trong `.env` (Gemini free tier là lựa chọn không tốn tiền: `GEMINI_API_KEY`)
5. Vào **Autonomous operator** trong dashboard, mô tả mục tiêu kênh (objective, audience, content pillars, tần suất đăng/tuần) thay vì giao từng task lẻ — hệ thống tự lên editorial plan
6. Bắt buộc chạy **Production readiness check** trước khi bật autonomous — nó test thật (tạo/giải mã 1 MP4 thử, xác minh quyền kênh YouTube) chứ không phải check giả

## Ví dụ thực tế
Input: đặt objective "Own practical AI automation for small teams", audience "Small business operators", cadence 2 video/tuần, format mặc định "tutorial".
Output: hệ thống tự quét trend YouTube + đối thủ đã cấu hình, tạo editorial plan có ghi nguồn (evidence-labeled), chạy từng video qua 7 agent, dừng lại chờ duyệt ở Review Studio (factual review + media-rights confirmation) trước khi cho Publishing Agent lên lịch đăng thật. Sau 24h/7 ngày, Analytics tự so CTR/retention/watch-time với lịch sử chính kênh đó (không so với view-count chuẩn chung chung), đề xuất tối ưu title/thumbnail — nhưng đề xuất chỉ có hiệu lực sau khi mình bấm approve, không tự áp dụng ngầm.

## Lưu ý / Lỗi thường gặp
- **Tên chính thức trên GitHub gắn kèm 1 địa chỉ token dạng pump.fun** ("AgentTube - ECGHuNZSECqTXabaLjkVrTEnguiNZLkKF1qi8oBGpump") — repo có liên hệ với 1 memecoin. Code vẫn MIT license, mở, chạy độc lập không cần token gì để dùng, nhưng đây là dấu hiệu cần tỉnh táo trước khi tin tưởng roadmap dài hạn của tác giả.
- `Missing credentials for: an AI provider` → chạy `npm run credentials:setup`, không bắt buộc phải là OpenAI
- FFmpeg không nhận diện → chạy lại `npm install` (kéo binary có sẵn) hoặc set `FFMPEG_PATH` thủ công
- Video bị đánh dấu "simulated", không đăng được → xem dấu ✗ ở startup capability check, thường do thiếu key hoặc FFmpeg
- AI image generation qua Gemini yêu cầu paid tier — nếu không cấu hình, hệ thống fallback về ảnh gradient chứ không lỗi cứng
- Repo chỉ 39 commit trên GitHub nhưng README mô tả tính năng rất sâu (scene manifest, retention curve mapping) — cần tự kiểm tra kỹ code trước khi tin tưởng chạy autonomous 24/7 không giám sát

## Đánh giá cá nhân
- Điểm mạnh: kiến trúc nghiêm túc hơn hầu hết clone "AI YouTube automation" trên GitHub — có gate duyệt thật (approval-first), fail-closed cho TTS, checkpoint SQLite resume được, hỗ trợ nhiều provider text/video/TTS (kể cả Claude, ElevenLabs), có cả tính năng cắt Shorts từ video dài đã duyệt và scene-repair không cần làm lại toàn bộ
- Điểm yếu: gắn với 1 memecoin trong chính tên repo — rủi ro về độ tin cậy lâu dài của maintainer; self-host Node.js nên không cắm thẳng vào Hermes (Python/urllib-only) mà phải gọi qua REST API riêng; AI video provider (Seedance/Kling/Wan) đều trả phí, bản free chỉ chạy được text + TTS Gemini + slideshow local; chưa rõ độ ổn định lâu dài vì lịch sử commit còn ngắn
- Có nên dùng không: 7/10 — đáng thử cho brand phụ ít rủi ro (không phải ABTRIP) để test workflow YouTube tự động hoá thật, nhưng nên tự audit code trước khi để nó tự đăng video không giám sát, và không nên phụ thuộc vào roadmap dài hạn của tác giả này.

## Link
- Repo: https://github.com/darkzOGx/youtube-automation-agent
- Docs: https://darkzogx-youtube-automation-agent.mintlify.app/
- Changelog: https://github.com/darkzOGx/youtube-automation-agent/blob/master/CHANGELOG.md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# AgentTube tự chạy như Express server riêng (npm start, port 3456) trên VPS.
# Hermes gọi qua REST API thuần bằng urllib — không cần cài SDK Node vào Hermes.
import urllib.request, json

BASE_URL = "http://localhost:3456"  # đổi nếu AgentTube chạy port/host khác
API_KEY = "[AGENTTUBE_API_KEY]"     # chỉ cần nếu đã set API_KEY trong .env của AgentTube

def queue_video(topic, style="tutorial"):
    payload = json.dumps({"topic": topic, "style": style}).encode()
    req = urllib.request.Request(
        f"{BASE_URL}/generate", data=payload, method="POST",
        headers={"Content-Type": "application/json", "x-api-key": API_KEY})
    return json.loads(urllib.request.urlopen(req).read())

def check_health():
    req = urllib.request.Request(f"{BASE_URL}/health")
    return json.loads(urllib.request.urlopen(req).read())
```
> ⚠️ Route `/generate` chỉ tạo job — video vẫn phải qua Review Studio (factual review + media-rights) trước khi Publishing Agent thật sự đăng. Hermes không bypass được gate này qua API.

### OpenClaw
```bash
# Trigger job từ Telegram command qua OpenClaw, gọi thẳng route Express của AgentTube
curl -X POST http://localhost:3456/generate \
  -H "Content-Type: application/json" -H "x-api-key: $AGENTTUBE_API_KEY" \
  -d '{"topic": "chủ đề Nobitano gõ trong Telegram", "style": "tutorial"}'
```

### Antigravity
```bash
# Deploy AgentTube như service riêng trên VPS Tencent Cloud qua PM2 (không chung process với Hermes/OpenClaw)
git clone https://github.com/darkzOGx/youtube-automation-agent.git
cd youtube-automation-agent && npm install
pm2 start index.js --name agenttube
pm2 save
```
> ⚠️ Cần RAM riêng cho FFmpeg render — kiểm tra VPS còn đủ tài nguyên trước khi chạy song song với Hermes/OpenClaw/OpenMontage (đã ghi nhận constraint RAM tương tự với GMSP/OpenMontage trong kho).

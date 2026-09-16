---
name: voxstyle-prompt-engine
description: >
  System prompt dạng state machine (10 bước) dán vào bất kỳ AI agent nào (Claude/ChatGPT/Gemini)
  để tự sinh trọn bộ sản phẩm video documentary paper-collage kiểu Vox: 10 ý tưởng theo niche,
  kịch bản narration liền mạch kiểu Fern, voiceover ElevenLabs, beat breakdown, file .txt prompt
  ảnh cho từng beat, Universal Video Prompt animate bằng Gemini Omni Flash, và 3 prompt thumbnail.
  KHÔNG cần cài đặt hay API riêng — chạy ngay trong chat. Lưu ý: mặc định output tiếng Anh
  (script/ảnh/thumbnail), chỉ tin nhắn agent-user là tiếng Việt — cần sửa rule ngôn ngữ nếu
  muốn dùng cho nội dung tiếng Việt.
---

# Voxstyle Prompt Engine — Dựng Video Documentary Paper-Collage Bằng 1 Prompt

## TL;DR
Dán 1 đoạn system prompt vào Claude/ChatGPT/Gemini, agent tự dẫn dắt qua 10 bước (chọn niche →
10 ý tưởng → chọn độ dài → viết script → voiceover → chia beat → prompt ảnh hàng loạt → video
prompt → thumbnail), ra sản phẩm hoàn chỉnh sẵn sàng render. Không cần cài công cụ hay API riêng
ngoài ElevenLabs (voiceover) và 1 tool tạo ảnh/animate bất kỳ.

## Dùng để làm gì
Đây là bản đóng gói khác của kỹ thuật "paper-collage documentary" (giống `skills/vox-director.md`
đã có trong kho), nhưng thay vì 1 skill package cần cài + API key riêng, nó chỉ là 1 đoạn prompt
dài — copy dán vào ô chat của agent bất kỳ là chạy được ngay. Phù hợp khi muốn thử nhanh phong
cách này mà không muốn setup Atlas Cloud API như Vox Director.

**Niche mặc định:** tội phạm/điều tra, lịch sử, tiền bạc-quyền lực, thảm hoạ-sinh tồn, bí ẩn,
công nghệ, thể thao — đúng kiểu kênh true-crime/documentary tiếng Anh trên YouTube, không phải
nội dung tiếng Việt kiểu Trùm Sân Bay hay Tây Du Ký Thương Trường.

## Setup từng bước

1. Copy toàn bộ đoạn "ENGINE PROMPT" (từ "You are an Elite Documentary Writer..." đến hết phần
   STATE 9) dán vào system prompt / custom instructions của Claude, ChatGPT, hoặc Gemini.
2. Agent tự hỏi STATE 0 (file PDF phong cách gốc, gõ "skip" nếu không có) → STATE 1 (chọn niche).
3. Đi qua từng bước, mỗi bước agent dừng lại chờ phản hồi — không cần biết trước cả quy trình,
   cứ trả lời từng câu agent hỏi.
4. Tới STATE 7, agent xuất ra 1 file `.txt` chứa prompt ảnh cho từng beat, các block cách nhau
   bằng 1 dòng trống — copy nội dung này đưa vào tool tạo ảnh hàng loạt (Midjourney/Nano Banana...).
5. Tới STATE 8, dùng Universal Video Prompt (cố định, áp cho mọi ảnh) đưa vào Gemini Omni Flash
   (hoặc model animate ảnh tương đương) để biến từng ảnh tĩnh thành clip 6-10 giây.
6. STATE 9 ra 3 prompt thumbnail, xong thì gõ "again" làm chủ đề mới hoặc "redo [state]" sửa
   lại 1 bước bất kỳ.

## Ví dụ thực tế

Chọn niche "Tội phạm và điều tra" → agent sinh 10 ý tưởng kiểu `"The Hunt for D.B. Cooper"`,
`"How the Portland Heist Unfolded"` → chọn 1 ý, chọn độ dài "2 phút" → agent viết script mở đầu
kiểu: *"November 24, 1971. Portland International Airport. A man in a dark suit buys a one-way
ticket under the name Dan Cooper."* → chia thành ~45-60 beat (2 phút) → xuất file `.txt` prompt
ảnh paper-collage cho từng beat → animate bằng Gemini Omni Flash, camera khoá cứng, ảnh tĩnh lắp
ráp dần trong 7 giây đầu rồi "sống" nhẹ 3 giây cuối (giấy rung, bóng đổ nhẹ).

## Lưu ý / Lỗi thường gặp

- **Ngôn ngữ mặc định là tiếng Anh cho toàn bộ nội dung video** — muốn ra tiếng Việt phải tự sửa
  đoạn "LANGUAGE RULE" trong prompt gốc, đổi rule "script/prompts stay in English" thành tiếng Việt,
  và cả STATE 4 (word math 2.5 từ/giây là chuẩn tiếng Anh, tiếng Việt cần calibrate lại theo đúng
  kinh nghiệm đã rút ra ở template Remotion trước đó — đừng tin số 2.5 từ/giây này cho tiếng Việt).
- **Nguồn từ AICONG, có gắn link tool trả phí** (Voxstyle Studio, membership 13.8 triệu) ở cuối
  document — bản thân đoạn prompt dùng được độc lập, không bắt buộc phải mua gì.
- **Không có bước validate fact** — script kiểu true-crime/documentary cần số liệu/tên/ngày tháng
  chính xác, prompt chỉ dặn "nếu không chắc thì viết vòng, đừng bịa" nhưng không tự kiểm tra —
  người dùng vẫn phải tự fact-check trước khi publish.
- **STATE 8 (Universal Video Prompt) yêu cầu camera khoá cứng hoàn toàn** — nếu tool animate
  không hỗ trợ giữ camera tĩnh tuyệt đối, kết quả sẽ lệch khỏi thiết kế gốc (vốn được tối ưu cho
  hiệu ứng "giấy tự lắp ráp" — có motion tự phát sinh khác sẽ phá vỡ hiệu ứng này).

## Đánh giá cá nhân

- **Điểm mạnh:** setup gần như bằng 0 — không cần API key riêng ngoài ElevenLabs đã có sẵn trong
  stack, chạy thử ngay trong 1 lần chat. Rule viết script (cold open, cliffhanger, câu ngắn tách
  beat rõ ràng) được nghĩ kỹ, không phải prompt hời hợt. Universal Video Prompt rất chi tiết,
  đúng kiểu chuyên nghiệp thật sự dùng được, không chung chung.
- **Điểm yếu:** English-only mặc định là rào cản lớn nếu muốn dùng ngay cho content tiếng Việt —
  phải tự sửa, chưa test bản đã sửa có giữ được chất lượng không. Không có cơ chế lưu trạng thái
  giữa các phiên (mỗi lần chạy lại từ STATE 0), không tiện cho việc làm series nhiều tập như
  Remotion Template Factory đã build. Gắn quảng cáo tool trả phí ở cuối, hơi lộ mục đích lead magnet.
- **Có nên dùng không:** 6/10 cho content tiếng Việt hiện tại (cần sửa mới dùng được) — 8/10 nếu
  mày cân nhắc mở thêm 1 kênh documentary tiếng Anh riêng (mảng true-crime/history AI content đang
  hot, kiếm view quốc tế) vì prompt này gần như sẵn sàng dùng ngay không cần sửa gì cho mục đích đó.

## Link
- Gốc: [Google Doc VOX STYLE - AICONG](https://docs.google.com/document/d/10mbiy3QlhKkCYKfcdpiXP8vKE1gZnk6OAYSko7QDz8I)
- Tool trả phí liên quan (không bắt buộc): tool.aicong.vn/cong-cu-ai/vox-style-studio
- So sánh: `skills/vox-director.md` (bản đóng gói khác cùng kỹ thuật, cần Atlas Cloud API)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Prompt này thiết kế để chạy tương tác (state machine chờ user), không hợp để Hermes chạy
# headless hoàn toàn. Hermes CÓ THỂ dùng để tự động hoá riêng từng bước sau khi có output:
# - Gọi ElevenLabs API với script từ STATE 4 (xem code mẫu trong repos/elevenlabs tương ứng)
# - Gọi Atlas Cloud / Gemini Omni Flash API để animate ảnh từ STATE 7 theo Universal Video
#   Prompt cố định ở STATE 8 — vì prompt này KHÔNG đổi giữa các ảnh, có thể hardcode 1 lần
#   rồi loop qua toàn bộ ảnh trong file .txt, không cần hỏi lại agent mỗi ảnh.
```

### OpenClaw
```bash
# Dán nguyên văn ENGINE PROMPT làm system prompt cho 1 phiên chat riêng, chạy tương tác qua
# Telegram — mỗi STATE là 1 lượt tin nhắn qua lại, phù hợp OpenClaw vì đã quen luồng hỏi-đáp.
```

### Antigravity
```bash
# Không cần deploy gì — đây là prompt thuần, không phải service.
```
> ⚠️ Trước khi giao cho agent chạy tự động không giám sát, nhớ tự sửa LANGUAGE RULE nếu mục
> tiêu là nội dung tiếng Việt — bỏ qua bước này sẽ ra script tiếng Anh không đúng ý.

---
name: human-footage-editor
description: >
  Sản xuất content từ footage/ảnh THẬT khách tự quay/chụp — dành cho personal brand
  cần đúng con người thật lên hình (khác hẳn nhánh faceless của yt-cashcow, nơi
  KHÔNG dùng AI tạo mặt/giọng thay khách). Dùng khi brand-config có
  content_source_type: human_footage hoặc hybrid.
---

# Human Footage Editor — Sản xuất từ footage thật, không AI-gen thay người

## TL;DR
Khách gửi raw clip/ảnh tự quay → AI chỉ làm phần hậu kỳ nhẹ (caption, cắt ghép, thumbnail,
phụ đề) — KHÔNG bao giờ tạo mặt/giọng AI thay khách. Dùng cho brand kiểu Chi (lifestyle,
cần đúng con người thật), khác hẳn engine `yt-cashcow` (dành cho kênh faceless).

## Khi nào dùng
`brand-config.content_source_type` = `human_footage` hoặc pillar cụ thể được route sang
nhánh này trong trường hợp `hybrid` (xem `agents/brandscan/README.md`).

## ⛔ Guardrail cứng — không được vượt qua
- KHÔNG dùng HeyGen/SceneWorks/bất kỳ tool avatar/AI-face nào để thay hoặc bổ sung mặt
  người vào content loại này — phá vỡ chính giá trị "lifestyle thật" khách đang bán
- Mặc định giữ nguyên giọng gốc trong clip. CHỈ dùng TTS khi cần voice-over cho đoạn
  không có khách nói (vd text overlay cần đọc), và **BẮT BUỘC dùng F5-TTS clone ĐÚNG
  giọng của chính khách** (3 giây mẫu từ clip có sẵn của khách — xem `repos/f5-tts.md`),
  KHÔNG dùng giọng AI generic/ElevenLabs mặc định — nguyên tắc giống hệt guardrail mặt
  người: phải là bản sắc thật của khách, không phải AI chung chung
- Nếu raw footage thiếu/mờ/không đủ dùng → báo lại khách xin quay lại, KHÔNG tự bù bằng
  stock footage hay AI-gen để lấp chỗ trống

## Quy trình

### 1. Nhận raw material
Khách gửi qua Telegram/Drive — có thể là: clip video thô, chuỗi ảnh, hoặc voice memo kể
chuyện (chưa quay hình). Ghi nhận kèm ngữ cảnh khách mô tả (nếu có) — không tự suy diễn
nội dung clip nói gì nếu khách chưa mô tả.

### 2. Viết caption/script hậu kỳ
Dùng persona đã chốt từ `personal-branding-creator` (đã điều chỉnh theo Positioning Report
riêng khách) — viết caption đi kèm clip, không phải kịch bản trước khi quay (vì clip đã có
sẵn, đây là bước match caption với nội dung thật của clip).

### 3. Hậu kỳ nhẹ
- Cắt/ghép cơ bản nếu clip dài, giữ đúng thứ tự tự nhiên
- Phụ đề (nếu khách nói, dùng transcript từ chính giọng khách, không phải viết lại bằng AI
  voice)
- Thumbnail: Canva/Pollinations — CHỈ cho phần bìa tĩnh, không áp dụng cho nội dung video
  chính

### 4. Đối chiếu voice profile
Nếu có mẫu content cũ của khách (từ `brand-discovery-session` 1a hoặc channel audit 1b) →
kiểm tra caption mới có khớp giọng văn thật của khách không, không lệch sang giọng AI
chung chung.

### 5. Vào Review Queue
Như mọi content khác trong pipeline BrandScan — khách duyệt trước khi Postiz đăng.

## Output
1 bài đăng gồm: clip/ảnh gốc của khách (không chỉnh sửa nội dung cốt lõi) + caption khớp
giọng văn + phụ đề (nếu cần) + thumbnail rời (nếu là video dài).

## Đánh giá
- **Điểm mạnh:** giữ đúng tính xác thực — yếu tố sống còn của personal brand lifestyle,
  chi phí thấp (không tốn credit AI-gen video)
- **Điểm yếu:** phụ thuộc hoàn toàn vào việc khách chịu quay/gửi raw material đều đặn —
  nếu khách bận không gửi, pipeline này không có gì để sản xuất, khác hẳn nhánh faceless
  có thể tự chạy không cần input hình ảnh mới từ khách mỗi ngày
- **Có nên dùng:** 8/10 cho đúng đối tượng personal brand cá nhân thật (như Chi) — không
  dùng cho brand doanh nghiệp/faceless, những trường hợp đó dùng `yt-cashcow` engine

## Agent Integration

### Hermes (Python)
```python
# Nhận raw file qua Telegram Bot API, lưu vào /raw-inbox/<client_id>/, trigger
# Content Pro pillar-match rồi gọi bước viết caption qua OmniRoute route 'creative'
```

### OpenClaw
```bash
# Route tin nhắn có attachment media trong luồng chat khách -> /raw-inbox/, không
# tự động publish, luôn dừng ở Review Queue
```

### Antigravity
Không cần — skill này không đụng hạ tầng deploy.

> ⚠️ Skill này CHƯA test với client thật, kể cả Chi — cần chạy thử 1 vòng thủ công
> (không qua Hermes tự động) trước khi tự động hóa hoàn toàn.

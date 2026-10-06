---
name: ffmpeg-media-toolkit
description: >
  Bộ lệnh FFmpeg dùng CHUNG cho mọi agent cần xử lý video/audio —
  convert, cắt, ghép, trích âm, nén, chèn phụ đề, lấy thumbnail. Đặt ở
  tầng company/skills (cắt ngang) vì đã phát hiện srt-whiteboard-
  animation, product-film-skill, vox-explainer-skill đều ÂM THẦM cần
  FFmpeg riêng — giờ có 1 nơi chuẩn để tham chiếu, không tự viết lại.
---

# FFmpeg Media Toolkit (dùng chung)

## TL;DR
FFmpeg không phải việc riêng của Media Pro — bất kỳ agent nào tạo/xử lý video (Content Pro dựng theo `video-narrative-structure`, Designer Pro làm motion poster, Media Pro đăng bài) đều có thể cần. 1 bộ lệnh chuẩn, dùng lại, không mỗi skill tự viết command riêng dễ sai.

## Cài đặt — 1 lần, dùng cho mọi agent

```bash
# macOS
brew install ffmpeg-full   # KHÔNG dùng "ffmpeg" thường — thiếu libass,
                            # chèn phụ đề sẽ lỗi (bài học thật từ
                            # youtube-clipper-skill)

# Ubuntu/Linux (VPS Antigravity)
sudo apt install ffmpeg libass-dev

# Verify có hỗ trợ phụ đề
ffmpeg -filters 2>&1 | grep subtitles
```

## Bộ lệnh chuẩn — dùng lại, không tự nghĩ mỗi lần

### 1. Đổi định dạng
```bash
ffmpeg -i input.mov -c:v libx264 -c:a aac output.mp4
```

### 2. Trích âm thanh
```bash
ffmpeg -i video.mp4 -vn -acodec libmp3lame audio.mp3
```

### 3. Cắt đoạn (không encode lại — nhanh, giữ chất lượng)
```bash
ffmpeg -i input.mp4 -ss 00:00:10 -to 00:00:30 -c copy output.mp4
```

### 4. Ghép nhiều clip (cùng codec/resolution)
```bash
# Tạo file list.txt: file 'clip1.mp4' \n file 'clip2.mp4' ...
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4
```

### 5. Lấy thumbnail tại giây cụ thể
```bash
ffmpeg -i video.mp4 -ss 00:00:05 -vframes 1 thumbnail.jpg
```

### 6. Nén video (giữ chất lượng hợp lý, giảm dung lượng)
```bash
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k output.mp4
```

### 7. Chèn phụ đề cứng (burn-in, cần ffmpeg-full/libass)
```bash
ffmpeg -i video.mp4 -vf "subtitles=sub.srt" output.mp4
```

### 8. Resize đúng khung đã định (nối `visual-template-formula-core`)
```bash
# Poster/Story 1080x1920
ffmpeg -i input.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" output.mp4
```

## ⚠️ An toàn — nối đúng nguyên tắc guardrail đã có

```
KHÔNG dùng -y (ghi đè không hỏi) lên file người dùng đã cung cấp gốc —
chỉ -y lên file tạm/output riêng của agent
LUÔN giữ bản gốc, xuất ra tên file MỚI, không ghi đè input
Lệnh FFmpeg không nằm trong danh sách nguy hiểm gốc của
destructive-command-guardrail, nhưng áp cùng tinh thần: không chạy
lệnh xoá/ghi đè dữ liệu người dùng mà không xác nhận
```

## Agent nào dùng, dùng để làm gì

| Agent | Dùng để |
|---|---|
| Media Pro | Nén/convert trước khi đăng Postiz, lấy thumbnail |
| Content Pro | Lắp ráp video theo `video-narrative-structure` (sau khi có voiceover VieNeu + ảnh) |
| Designer Pro | Dựng motion poster/story ngắn, resize đúng khung `visual-template-formula-core` |
| Hermes (tự động) | Bước cuối trong pipeline `srt-whiteboard-animation`/`product-film-skill` khi chạy thật |

## Setup từng bước
1. Cài `ffmpeg-full` (không phải `ffmpeg` thường) — 1 lần trên mỗi máy/VPS chạy agent
2. Agent nào cần xử lý media — tham chiếu đúng lệnh mẫu ở trên, không tự viết command mới từ đầu
3. Luôn test lệnh trên file mẫu nhỏ trước khi chạy hàng loạt

## Lưu ý / Lỗi thường gặp
- Cài `ffmpeg` thay vì `ffmpeg-full` trên macOS — chèn phụ đề sẽ báo lỗi thiếu filter `subtitles`, đã xảy ra thật với skill khác trong hệ sinh thái Claude Code
- Dùng `-c copy` khi cắt đoạn nhưng điểm cắt không trùng keyframe — video lỗi/giật ở điểm cắt, cần encode lại (`-c:v libx264`) nếu cần cắt chính xác tới khung hình
- Ghép clip khác resolution/codec bằng `concat demuxer` (`-f concat`) — lỗi hoặc crash, cần chuẩn hoá cùng định dạng trước (dùng filter `concat` khác, phức tạp hơn) hoặc convert hết về cùng chuẩn trước khi ghép

## Đánh giá cá nhân
- Điểm mạnh: giải đúng vấn đề vừa phát hiện (FFmpeg âm thầm có mặt khắp kho, không ai gom) — giờ có 1 nơi chuẩn tham chiếu, dùng lại thay vì mỗi skill tự viết
- Điểm yếu: chỉ là bộ lệnh tham khảo, không phải wrapper tool tự động chọn lệnh đúng (khác FFHub/digitalsamba toolkit dùng AI dịch ngôn ngữ tự nhiên sang lệnh) — agent vẫn cần biết chọn đúng lệnh nào
- Có nên dùng: 8/10 — nền tảng cần thiết, nên dùng ngay cho mọi agent xử lý media thay vì để rải rác

## Link
- Bài học libass: op7418/Youtube-clipper-skill (wiki)
- Tool thay thế dùng AI dịch lệnh: digitalsamba/claude-code-video-toolkit, ffhub-io/ffhub-ffmpeg (cloud)
- Dùng cùng: srt-whiteboard-animation, product-film-skill, visual-template-formula-core, video-narrative-structure

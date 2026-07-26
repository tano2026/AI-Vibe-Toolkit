# Deploy Checklist — Shorts Affiliate System

## Trước khi chạy thật

- [ ] Playwright + Chromium cài xong (`npx playwright install chromium`)
- [ ] FFmpeg/FFprobe có sẵn trên VPS
- [ ] TTS provider (Supertonic/ElevenLabs) hoạt động, test 1 câu ngắn ra file mp3
- [ ] `skills/affiliate-skills.md` wiring xong với Hermes/OpenClaw (lệnh `/affiliate ...`
      chạy được thật, không chỉ là mô tả)
- [ ] Danh sách chương trình affiliate đã đăng ký — Nobitano cung cấp trước

## Test case bắt buộc (chạy cả 2, không được bỏ 1 case)

### Case 1 — Video CÓ affiliate link
- [ ] Chạy `examples/storyboard-example.json` (đổi `affiliate_link` thành 1 link test)
- [ ] Verify scene `cta-url` trong render.html hiện đúng link + badge "Link liên kết"
- [ ] Verify description có disclosure affiliate, không bị cắt mất bởi giới hạn ký tự
- [ ] Verify pinned comment có link rút gọn + từ "affiliate"/"liên kết"
- [ ] Verify link tracking hoạt động (click thử, kiểm tra redirect đúng)

### Case 2 — Video KHÔNG có affiliate (tool chưa có chương trình)
- [ ] Chạy với `affiliate_link: null`
- [ ] Verify pipeline chạy hết bình thường, không bị lỗi ở bước 8
- [ ] Verify KHÔNG có description rác do thiếu affiliate (bước 8 phải tự bỏ qua)
- [ ] Verify scene cta-url vẫn dùng link gốc tool, không bỏ trống

### Case 3 — Render đồng bộ 2 định dạng
- [ ] Verify `output_16x9.mp4` và `output_9x16.mp4` cùng khớp timing voiceover, không lệch
- [ ] Verify không có scene nào bị cắt cụt do resize 9:16

## Ngưỡng review trước khi bật auto-publish

- 3 video đầu tiên: **review thủ công 100%** trước khi publish, không có ngoại lệ.
- Sau 3 video: Nobitano quyết định ngưỡng tiếp theo dựa trên kết quả thực tế (số lỗi
  compliance, chất lượng affiliate disclosure, phản hồi audience).

## Rollback nếu có sự cố

- Nếu 1 video bị nền tảng gắn nhãn/hạn chế → dừng publish tự động ngay, review lại toàn
  bộ storyboard gần nhất qua Compliance Gate trước khi tiếp tục.
- Nếu affiliate link bị phát hiện sai/chết sau khi đã publish → sửa description ngay,
  không đợi video tiếp theo.

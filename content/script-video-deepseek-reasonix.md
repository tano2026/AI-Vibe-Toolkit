# Script Video — DeepSeek-Reasonix

## Thông tin
- Tool liên quan: /repos/deepseek-reasonix.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~55 giây

## Hook (3 giây đầu)
"Coding agent xịn như Claude Code mà rẻ hơn 5 lần — đây là cách."

## Script voiceover (ElevenLabs-ready)

Hầu hết coding agent đều tốn tiền theo kiểu này: mỗi lượt chat là một lần gửi toàn bộ context lên model. Session càng dài, càng đắt.

DeepSeek-Reasonix build khác hẳn. Nó giữ loop append-only, align với prefix cache của DeepSeek. Nghĩa là session 18 phút, cache hit 95%, tốn 4 cent thay vì 20 cent.

Cài 1 lệnh. Gõ reasonix trong thư mục code. Nó tự đọc file, sửa code, chạy test, báo kết quả.

Ai đang dùng DeepSeek API thì đây là tool phải có. Link repo trong bio.

## Ghi chú quay (OBS)

- Cảnh 1 (0-5s): Terminal mở, gõ lệnh `npm install -g reasonix@next`
- Cảnh 2 (5-20s): Màn hình config file `reasonix.toml` — highlight phần `base_url` và `model`
- Cảnh 3 (20-40s): Chạy `reasonix` → gõ task → xem nó tự sửa file → test pass
- Cảnh 4 (40-50s): Stats cuối session: cache hit %, total cost
- Cảnh 5 (50-55s): Text overlay CTA

## Caption/Sub (CapCut)

Highlight: "append-only loop", "95% cache hit", "4 cent/session"
Timing cắt: cảnh 3 phải thấy rõ agent đang tự edit file — đây là moment quan trọng nhất

## Thumbnail (Canva)

Background tối. Text lớn: "Coding Agent $0.04/session" màu xanh DeepSeek. Góc dưới: logo terminal + DeepSeek logo. Không cần ảnh mặt.

## CTA
"Follow để xem thêm tools AI tiết kiệm chi phí. Link repo trong bio."

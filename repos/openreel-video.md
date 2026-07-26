# OpenReel Video — GitHub Repo

## TL;DR
Editor video chạy thẳng trên browser, bản thay thế mã nguồn mở cho CapCut — không cần cài app, không upload lên cloud, không watermark. 4.4k sao, MIT license, dùng WebGPU + WebCodecs nên dựng/export nhanh dù chạy trong trình duyệt.

## Repo này dùng để làm gì
Mở trình duyệt (Chrome/Edge/Firefox/Safari bản mới) → vào thẳng editor, kéo thả video vào, dựng multi-track y như CapCut/Premiere: cắt/ghép, transition, color grading (color wheels, curves, LUT), audio mixing (EQ, noise reduction, beat detection), text animation 20+ kiểu, phụ đề karaoke-style (highlight từng từ theo nhạc), rồi export MP4/WebM/ProRes ngay tại máy — không có bước nào file phải rời khỏi máy.

## Setup từng bước
1. Cách nhanh nhất — dùng bản online, không cài gì cả:
```
Vào https://openreel.video, kéo thả video vào là dựng được luôn.
```
2. Chạy local (để tự host, không phụ thuộc uptime của bản online):
```bash
git clone https://github.com/Augani/openreel-video.git
cd openreel-video
pnpm install       # cần Node.js 18+
pnpm dev
# mở http://localhost:5173
```
3. Build bản production (deploy lên VPS/domain riêng):
```bash
pnpm build
pnpm preview
```
4. Kiểm tra máy đủ chuẩn trước khi dùng bản 4K: khuyến nghị 8GB+ RAM, có GPU rời, CPU nhiều nhân.

## Ví dụ thực tế
Dùng làm bước edit thủ công cuối cùng cho video Trùm Sân Bay/GMSP trước khi đăng — sau khi pipeline `trum-san-bay` hoặc `shorts-affiliate-system` render xong bản thô (visual + voiceover ghép tự động), mở file đó vào OpenReel để tinh chỉnh tay: chỉnh màu (LUT), thêm phụ đề karaoke-style, cắt/ghép đoạn cần sửa gấp — không cần cài CapCut hay đợi upload/xử lý cloud, làm ngay trên máy Windows local đang có.

## Lưu ý / Lỗi thường gặp
- README tự ghi "Status: Beta" — repo mới, còn nhiều tính năng "In Progress" (nested sequences, motion tracking, plugin system) chưa xong, không kỳ vọng ổn định như DaVinci/Premiere.
- Cần trình duyệt hỗ trợ WebCodecs bản mới: Chrome/Edge 94+, Firefox 130+, Safari 16.4+ — máy cũ hoặc trình duyệt cũ sẽ không chạy được tính năng hardware encoding.
- Repo có gắn kèm 1 **token crypto ($OPENREEL)** trong README — đây là tín hiệu cần cẩn trọng, không liên quan tới chất lượng code nhưng là dấu hiệu lạ cho 1 dự án dev tool nghiêm túc, nên tách bạch rõ: dùng tool thì được, không liên quan gì tới token đó.
- Dự án được ghi rõ là **"AI-managed development"** — Claude AI quản lý phần lớn việc triage issue, viết code, review, người chỉ giữ vai trò định hướng chiến lược cuối cùng — cùng mô hình "công ty 1 người + AI agent" mà Nobitano đang làm với Tano Agency, đáng tham khảo cách họ tổ chức quy trình.
- Có bản fork riêng cho ComfyUI (`WASasquatch/openreel-video-comfyui`) nếu cần edit video AI-gen ngay trong workflow ComfyUI, không phải bản chính.

## Đánh giá cá nhân
- Điểm mạnh: tính năng sâu ngang phần mềm trả phí (color grading pro, ProRes export, AI upscaling built-in), 100% riêng tư vì chạy local, miễn phí thật sự không giới hạn, tốc độ nhờ WebGPU/WebCodecs không hề "ì" như hình dung về web app.
- Điểm yếu: còn beta, nhiều tính năng lớn (nested sequences, plugin system) chưa xong, gắn token crypto trong README là điểm trừ về hình ảnh dự án dù không ảnh hưởng chất lượng code.
- Có nên dùng: 8/10 — rất đáng thay thế CapCut cho bước edit tay cuối cùng, đặc biệt hợp máy Windows local đang có sẵn, không cần cài đặt nặng nề.

## Link
- Repo: https://github.com/Augani/openreel-video
- Dùng online ngay: https://openreel.video
- Bản ComfyUI: https://github.com/WASasquatch/openreel-video-comfyui

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# OpenReel là web app tương tác tay (kéo thả, chỉnh UI), không có REST API để Hermes
# gọi tự động chỉnh sửa video — vai trò của Hermes ở đây là chuẩn bị file trước khi
# đưa cho Nobitano mở tay trong OpenReel, không phải tự động hoá toàn bộ bước edit.
import shutil

def prepare_for_manual_edit(rendered_video_path, staging_dir="/mnt/staging"):
    shutil.copy(rendered_video_path, staging_dir)
    return f"Đã sẵn sàng để mở tay trong OpenReel: {staging_dir}"
```

### OpenClaw
```bash
# Tự host bản OpenReel trên VPS để không phụ thuộc uptime bản public,
# truy cập qua trình duyệt trên máy Windows local
git clone https://github.com/Augani/openreel-video.git /opt/openreel
cd /opt/openreel && pnpm install && pnpm build && pnpm preview --host 0.0.0.0
```

### Antigravity
```bash
# Deploy như 1 static/dev server trên VPS, mở port cho Nobitano truy cập từ xa
pm2 start "pnpm preview --host 0.0.0.0 --port 5173" --name openreel-editor
```
> ⚠️ Đây là tool THAO TÁC TAY (giống CapCut), không phải agent tự động — dùng làm bước cuối
> con người can thiệp sau khi pipeline tự động (trum-san-bay/shorts-affiliate-system) render
> xong bản thô.

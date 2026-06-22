# Shortcast — GitHub Repo

## TL;DR
App macOS native: thả 1 video dài vào → AI tự cắt ra 3–6 đoạn dễ viral, tự caption, tự reframe dọc 9:16, tự schedule — **chạy 100% trên máy, không lên cloud**. 334⭐, ra mắt tháng 5/2026, Apache 2.0.

## Repo này dùng để làm gì
Mày có podcast, webinar, stream, hay video bài giảng dài → muốn cắt thành Shorts/Reels/TikTok nhưng ngại ngồi edit tay từng clip?

Shortcast làm hết:
1. Chép lời video (WhisperKit, chạy GPU máy Mac)
2. AI đọc toàn bộ transcript → tìm 3–6 đoạn hay nhất dễ viral
3. Cắt từng clip, reframe ngang → dọc 9:16 (tự track khuôn mặt người nói)
4. Viết caption riêng cho TikTok, Instagram Reels, YouTube Shorts (đúng tone từng nền tảng)
5. Review grid — xem từng clip có âm thanh, edit caption, approve
6. Schedule tự đăng 1 clip/ngày suốt tuần

Điểm khác biệt chính: **không upload video lên bất kỳ server nào**. Model AI (Gemma 4 12B + WhisperKit) chạy thẳng trên chip Apple Silicon. Privacy tuyệt đối.

## Setup từng bước

**Yêu cầu:**
- macOS 15+ (Sequoia trở lên)
- Apple Silicon bắt buộc (M1/M2/M3/M4)
- RAM tối thiểu 16GB (Gemma 4 12B cần ~12GB)

**Cài đặt:**
```bash
# Cách 1: Clone và build
git clone https://github.com/mutonby/shortcast.git
cd shortcast
open Shortcast.xcodeproj
# Build trong Xcode (Cmd+B)
```

```bash
# Cách 2: Tải DMG (nếu có release)
# Vào https://github.com/mutonby/shortcast/releases
# Tải Shortcast.dmg → kéo vào Applications
```

**Lần đầu chạy:**
1. App tự tải model WhisperKit large-v3 (~1.5GB) và Gemma 4 12B MLX (~7GB) — mất 10–15 phút tùy mạng
2. Thả video vào cửa sổ chính
3. Chờ transcribe + cut (video 1 tiếng mất ~5–10 phút)
4. Review grid → approve → publish hoặc schedule

**Để auto-post lên TikTok/Instagram/YouTube:**
- Kết nối tài khoản trong phần Settings → Social Accounts
- Dùng Upload-Post API (app tích hợp sẵn)

## Ví dụ thực tế
Mày có 1 video podcast 45 phút về "Vibe Coding cho người mới":
- Thả vào Shortcast
- 8 phút sau: 5 clip đã cắt sẵn
  - Clip 1: đoạn "Claude không cần biết code để dùng" → TikTok hook + caption ✅
  - Clip 2: đoạn demo live coding → caption 3 platform ✅
  - Clip 3: đoạn "sai lầm phổ biến nhất" → hook viral sẵn ✅
- Reframe tất cả sang 9:16 dọc, face tracking theo người nói
- Schedule: Thứ 2, 3, 4 mỗi clip 1 ngày

Từ 45 phút video → 5 Shorts sẵn sàng đăng, không cần mở CapCut.

## Lưu ý / Lỗi thường gặp
- **Chỉ chạy được trên Apple Silicon** — Intel Mac không hỗ trợ, không có workaround
- **RAM 8GB sẽ swap nặng** — khuyên dùng 16GB+, M2/M3 trở lên cho mượt
- **Lần đầu chạy chậm** — tải model ~9GB, cần mạng tốt, chỉ tải 1 lần
- **Video tiếng Việt**: WhisperKit hỗ trợ đa ngôn ngữ, caption sẽ ra tiếng Việt nếu video tiếng Việt — nhưng tone "punchy TikTok VN" chưa được optimize như EN
- **Face tracking thất bại** → fallback tự động sang blurred-background letterbox, không crash
- Nếu video không có khuôn mặt rõ (screencast, slides) → reframe sẽ không chuẩn, nên crop tay

## Đánh giá cá nhân
- **Điểm mạnh:** Privacy-first hoàn toàn (không upload video), pipeline một chạm từ raw video → ready-to-post, caption tự điều chỉnh theo từng platform, stack kỹ thuật xịn (Swift native, MLX, không Electron)
- **Điểm yếu:** Chỉ macOS Apple Silicon — Windows/Linux/Intel bị loại hoàn toàn; RAM yêu cầu cao; tiếng Việt chưa được tối ưu tone caption; mới ra (v1.0.0, tháng 5/2026) nên còn bug
- **Có nên dùng không: 8/10** — nếu mày dùng Mac Apple Silicon và làm content video dài, đây là tool tiết kiệm thời gian nhất trong pipeline. Chỉ trừ điểm vì lock cứng macOS và RAM cao.

## Link
- Repo: https://github.com/mutonby/shortcast
- Docs/Demo: README có demo GIF đầy đủ

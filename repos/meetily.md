---
name: meetily
description: >
  Trợ lý ghi chú họp AI chạy 100% local (Rust + Tauri), không gửi audio lên
  cloud. Đang trending mạnh trên GitHub (19k star), hợp cho ai cần note
  meeting mà không muốn data rời máy — kiểu tư vấn, luật, hoặc đơn giản là
  không tin cloud tool.
---

# Meetily (Zackriya-Solutions/meetily) — GitHub Repo

## TL;DR
Trợ lý ghi chú họp AI chạy 100% local (Rust + Tauri), không gửi audio lên cloud. Đang trending mạnh trên GitHub (~19k star), hợp cho ai cần note meeting mà không muốn data rời máy — kiểu tư vấn, luật, hoặc đơn giản là không tin cloud tool.

## Tool này dùng để làm gì
Meetily thu âm cuộc họp, transcribe bằng Whisper hoặc Parakeet (nhanh hơn Whisper ~4 lần), tách giọng từng người nói (speaker diarization), rồi tóm tắt bằng Ollama chạy local hoặc bằng Claude/Groq/OpenRouter nếu mày muốn nhanh hơn. Toàn bộ transcript + audio lưu trên máy, không có server nào của Meetily nhìn thấy nội dung. Bản Community free, có bản PRO trả phí cho enterprise (transcription xịn hơn, deploy có Terraform).

## Setup từng bước
1. Cài qua Homebrew (macOS) — 1 lệnh cài cả frontend + backend:
```bash
brew tap zackriya-solutions/meetily
brew install --cask meetily
```
2. Chạy backend server (chọn ngôn ngữ + model Whisper):
```bash
meetily-server --language en --model medium
```
3. Windows: tải file `meetily_x64-setup.exe` từ GitHub Releases, unblock file rồi chạy installer.
4. Muốn build từ source (dev) → cần Rust + Node.js, clone repo `meeting-minutes`, `cd frontend && pnpm install && ./build-gpu.sh`.
5. Vào app, chọn provider tóm tắt: Ollama (local, mặc định) hoặc dán API key Claude/Groq/OpenRouter nếu muốn nhanh/chất hơn.

## Ví dụ thực tế
Case dùng cho Tano Agency: họp với client ABTRIP bàn chốt scope, không muốn nội dung giá cả/hợp đồng lọt ra ngoài qua tool cloud như Otter/Fireflies → chạy Meetily local trên laptop, thu xong tự transcribe + tóm tắt bằng Ollama, export ra note đưa cho team mà không lo data đi đâu.

## Lưu ý / Lỗi thường gặp
- Model Whisper "medium" chạy CPU khá nặng máy yếu → nếu máy không GPU, cân nhắc model nhỏ hơn hoặc chấp nhận transcribe chậm.
- Bản Homebrew đôi lúc lỗi SHA-256 mismatch khi tải backend → xoá cache download (`~/Library/Caches/Homebrew/downloads/...`) rồi cài lại.
- Ollama phải chạy sẵn ở máy (và có pull model) thì tóm tắt local mới hoạt động — không tự cài kèm.
- Multi-language support cho phần tóm tắt còn đang là feature request mở (issue #233), tiếng Việt tóm tắt có thể chưa mượt.

## Đánh giá cá nhân
- Điểm mạnh: privacy thật sự (không cloud), tốc độ transcribe nhanh nhờ Parakeet, free và mã nguồn mở, linh hoạt chọn AI provider tóm tắt.
- Điểm yếu: setup nặng hơn app cloud (phải tự chạy Ollama, tự quản model), UI/UX chưa mượt bằng Otter/Fireflies, quality tóm tắt phụ thuộc model local chọn.
- Có nên dùng không: 7/10 — hợp nếu thật sự cần privacy (họp nhạy cảm với client/đối tác), không hợp nếu chỉ cần note nhanh và không ngại cloud.

## Link
- Repo: https://github.com/Zackriya-Solutions/meetily
- Docs/Demo: https://meetily.ai

---

## 🤖 Agent Integration

### Hermes (Python)
> Không có REST API public để Hermes gọi trực tiếp — Meetily là app desktop (Tauri) chạy local trên máy người dùng, không phải service network. Hermes trên VPS không tương tác được trừ khi tự deploy backend Meetily lên VPS và expose port.

### OpenClaw
```bash
# Không có tích hợp qua npx/skill — cài thủ công qua Homebrew hoặc installer
brew tap zackriya-solutions/meetily
brew install --cask meetily
```

### Antigravity
```bash
# Nếu muốn self-host backend trên VPS (headless, không cần Tauri UI):
git clone https://github.com/Zackriya-Solutions/meeting-minutes
cd meeting-minutes
# build backend theo BUILD.md của repo — cần Rust toolchain trên VPS
```
> ⚠️ Meetily thiết kế để chạy trên máy cá nhân (macOS/Windows), không phải service headless cho server — nếu deploy trên VPS Ubuntu cần tự build phần backend Rust riêng, chưa có hướng dẫn chính thức cho Linux server.

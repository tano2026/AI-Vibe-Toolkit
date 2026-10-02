---
name: vieneu-tts
description: >
  TTS tiếng Việt on-device, clone giọng tức thời (3-5 giây audio mẫu),
  song ngữ Việt-Anh, chạy offline hoàn toàn (không cần cloud API). Dùng
  cho voiceover video brand (ABTRIP/Tano Cafe/GMSP), chất lượng cao hơn
  TTS tiếng Việt chung chung vì train riêng ~1000 giờ giọng Việt thật.
---

# VieNeu-TTS — GitHub/HuggingFace

## TL;DR
TTS tiếng Việt tốt nhất đã thấy trong kho — clone giọng bất kỳ chỉ từ 3-5 giây mẫu, chạy offline trên máy (không tốn phí API), song ngữ Việt-Anh tự nhiên khi chuyển đổi giữa 2 ngôn ngữ.

## Repo này dùng để làm gì
Train trên ~1000 giờ giọng nói tiếng Việt thật, dựa trên backbone LLM 1.5B — phát âm chuẩn, ngữ điệu tự nhiên hơn TTS generic. Hỗ trợ "code-switching" (chen tiếng Anh vào câu tiếng Việt mượt mà) — hợp cho nội dung hàng không/du lịch hay chen thuật ngữ Anh (vd "Fast Track", "check-in").

## Setup từng bước
```bash
pip install vieneu
```
```python
from vieneu import Vieneu

tts = Vieneu()  # mặc định v3 Turbo, 48kHz, chất lượng cao nhất
audio = tts.infer("Xin chào, đây là VieNeu-TTS.", voice="Hải Đăng")
tts.save(audio, "output.wav")

# Giọng nhanh hơn, nhẹ hơn (24kHz) nếu cần tốc độ:
tts_nano = Vieneu(mode="v3nano")
```

Clone giọng riêng (vd giọng thương hiệu cố định cho 1 kênh): cung cấp 3-5 giây audio mẫu, model tự học giọng đó cho các lần tạo sau.

## Ví dụ thực tế
Kênh GMSP cần 1 giọng đọc nhất quán xuyên suốt các video — clone 1 lần từ giọng đã chọn, dùng lại cho mọi video sau, không cần thuê lồng tiếng mỗi lần hoặc phụ thuộc giọng TTS "robot" nghe lạ.

## Lưu ý / Lỗi thường gặp
- Bản fp32 mặc định chất lượng cao nhất nhưng chậm hơn — dùng `precision="int8"` nếu cần nhanh trên CPU (~4x nhỏ hơn)
- Nhiều fork/app bọc quanh (VieNeuTTSApp desktop, VieNeu-TTS.cpp, vietnamese-tts-local web) — bản gốc `pnnbao97/VieNeu-TTS` là chuẩn nhất để bắt đầu

## Đánh giá cá nhân
- Điểm mạnh: chất lượng giọng Việt thật sự tốt (không phải TTS generic chỉnh giọng Việt), offline hoàn toàn (không lệ thuộc quota API), license Apache-2.0 dùng thương mại thoải mái — khác `YuE2 Studio` (license hạn chế)
- Điểm yếu: cần máy đủ mạnh để chạy mượt (dù nhẹ hơn nhiều so với tạo nhạc/video)
- Có nên dùng: 9/10 — đáng thay thế bất kỳ TTS tiếng Việt nào đang dùng, không giới hạn thương mại

## Link
- Repo: https://github.com/pnnbao97/VieNeu-TTS
- PyPI: https://pypi.org/project/vieneu/
- Docs: https://docs.vieneu.io/

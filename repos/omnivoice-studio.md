---
name: omnivoice-studio
description: >
  VoiceStudio (trước đây tên OmniVoice Studio): ứng dụng desktop mã nguồn mở
  AGPL-3.0 để clone giọng, thiết kế giọng, lồng tiếng video, đọc chính tả và
  làm audiobook, chạy trên máy mình, có API cục bộ và MCP server. Trọng số model
  mặc định (OmniVoice) là phi thương mại, đọc mục Giấy phép trước khi dùng cho khách.
---

# VoiceStudio (trước đây OmniVoice Studio) — GitHub Repo

> Cập nhật 22/10/2026: repo `debpalash/OmniVoice-Studio` đã đổi tên thành **`debpalash/VoiceStudio`**. File giữ tên cũ (`omnivoice-studio.md`) để không gãy liên kết trong kho. Bản viết 2026-10 cũ ghi "miễn phí hoàn toàn, không giới hạn" và hướng dẫn `python main.py` — **cả hai không còn đúng** (xem Giấy phép và Setup).

## TL;DR
Ứng dụng desktop (Electron) AGPL-3.0 chạy trên máy của mày: clone giọng từ vài giây audio mẫu, thiết kế giọng bằng mô tả chữ, lồng tiếng video theo thời gian, chính tả, audiobook (nhận cả EPUB). Có API cục bộ cổng 3900 và **MCP server** để agent tự gọi. Mã ứng dụng dùng thương mại được theo AGPL, nhưng **trọng số model mặc định OmniVoice là CC-BY-NC (phi thương mại)** kèm tokenizer Higgs Audio 2 / Llama 3 — nên chưa thể coi là "miễn phí để làm video cho khách".

## Repo này dùng để làm gì
- Clone giọng (nói tác giả: khoảng 3 giây mẫu thường đủ), thiết kế giọng (giới tính, tuổi, cao độ, phong cách, accent) từ mô tả
- Lồng tiếng video: tách thoại, dịch, đặt giọng mới theo mốc thời gian (có giới hạn tốc độ Smart Fit)
- Chính tả bằng widget nổi; phiên âm; truyện nhiều giọng; audiobook; chạy hàng loạt, thư mục theo dõi
- 646 ngôn ngữ cho engine OmniVoice (bảng `docs/languages.md` có tiếng Việt, mã `vi`; engine khác có bộ ngôn ngữ riêng và sẽ dừng nếu chọn ngôn ngữ không hỗ trợ)
- Cho agent: MCP server gắn ở `/mcp` trên backend, API cục bộ `localhost:3900`

## Số liệu đã kiểm (22/10/2026, bản clone nông)
- License ứng dụng: **AGPL-3.0-only** (đã mở LICENSE và LICENSE-NOTICE.md). Dùng nội bộ/thương mại với ứng dụng được; nếu sửa rồi cho người khác dùng qua mạng phải công khai mã đã sửa. Giấy phép thương mại riêng chỉ cần khi nhúng vào sản phẩm đóng
- Commit mới nhất: 21/10/2026 (`28bf2c7`). Bản v0.5.3 là bản Tauri cuối; từ đó chỉ có Electron
- Số sao: trang EveryDev ghi hơn 32.900 sao và 221.000 lượt tải release — **chưa tự đo** (API GitHub bị chặn trong phiên này). Con số "7.500+ sao" trong bản cũ đã lỗi thời
- Chưa cài, chưa tạo giọng, chưa nghe thử chất lượng tiếng Việt, chưa chạy MCP. Chỉ đọc README, docs/mcp.md, docs/licensing, danh sách ngôn ngữ

## Giấy phép — đọc kỹ trước khi dùng cho khách
- README: AGPL-3.0 chỉ phủ **ứng dụng**; "model weights, tokenizers, voices và điều kiện của đầu ra là riêng"
- `docs/licensing/model-inventory.md`: 56 repo model được ghi nhận; **chưa mục nào được đánh dấu "đã rà và cho phép thương mại"**. `k2-fsa/OmniVoice` (model mặc định) ghi `CC-BY-NC (version unspecified); Higgs Audio 2; Meta Llama 3`, `commercial_use: false`. Bản GGUF cũng CC BY-NC 4.0
- Ứng dụng bắt chấp nhận giấy phép model trước khi dùng (model mặc định cần 1 lần xác nhận). Xác nhận nghĩa là mày tự nhận có quyền theo giấy phép model — ví dụ chỉ dùng phi thương mại
- Hệ quả cho agency: **video khách trả tiền, kênh kiếm tiền (affiliate, bán hàng) chưa nên dùng giọng sinh bằng model mặc định** nếu chưa có giấy phép riêng từ chủ model. Muốn dùng thương mại thì phải chọn engine khác và tự đọc giấy phép của từng engine (bản kiểm kê ghi nhiều model còn "chưa rà")
- Clone giọng người thật chỉ khi có sự đồng ý của họ (README nhắc rõ)

## Setup
Điều kiện: Windows (một số bản chạy qua WSL), macOS hoặc Linux; GPU NVIDIA (CUDA) hoặc Apple Silicon (MPS) cho nhanh; không có GPU vẫn chạy bằng CPU nhưng chậm (cần khoảng 5 GB trống cho bản PyTorch CPU).
```bash
# macOS / Linux
curl -fsSL https://voicestudio.sh/install | sh
# Windows (PowerShell)
irm https://voicestudio.sh/install | iex
```
Hoặc tải bản `.dmg`/`.exe`/`.AppImage`/`.deb` ở trang Releases, hoặc Docker (xem `docs/install/docker.md`). Lần đầu mở sẽ hỏi tải model (model OmniVoice khoảng 2,3 GB) và yêu cầu chấp nhận giấy phép model. Đọc script cài đặt trước khi pipe vào shell.
Cho agent: `npx skills add debpalash/VoiceStudio` (chọn `voicestudio` cho việc audio).

## Ví dụ thực tế
Bối cảnh: làm bản lồng tiếng thử cho video nội bộ của agency, **không phải sản phẩm giao khách** (vì giấy phép model).
```text
1. Mở Voice cloning → thêm đoạn ghi âm sạch 10–30 giây của chính mày
2. Nhập kịch bản tiếng Việt → Generate → xuất WAV
3. Nghe lại, so với ElevenLabs hoặc giọng CapCut trong cùng đoạn kịch bản
```
Kỳ vọng: giọng clone chạy được ngoại tuyến. **Chưa chạy thử — chưa biết tiếng Việt nghe thế nào.** Bản cũ viết tiếng Việt "chưa tốt bằng ElevenLabs" là nhận định không có đo kiểm.

## Lưu ý / Lỗi thường gặp
- **Giấy phép model là rào cản lớn nhất cho việc thương mại** (mục trên)
- AGPL: dựng dịch vụ cho khách dùng qua mạng trên bản đã sửa thì phải công khai mã đã sửa
- Windows trên ARM còn thử nghiệm; Mac Intel chỉ chạy giao diện và nối backend ở máy khác
- Cổng 3902 của bản Tauri đã bỏ (3902 giờ là cổng dev của Electron); điều khiển chính tả từ ngoài bị loại, dùng phím tắt trong app
- MCP: cần đặt `OMNIVOICE_MCP_BASE_PATH` thì tool mới đọc/ghi được file; không đặt thì tham số đường dẫn bị từ chối. Dùng chế độ `files` để khỏi nhồi WAV base64 vào ngữ cảnh agent
- Telemetry: README ghi phân tích sử dụng chỉ bật khi đồng ý
- Dự án có bản Pro/Cloud thương mại, chỉ qua liên hệ, chưa có giá công khai

## Đánh giá cá nhân
- Điểm mạnh: ứng dụng mở, đang hoạt động rất tích cực (commit 21/10), có MCP và API cục bộ nên nối agent dễ, có bảng giấy phép model minh bạch hiếm thấy, nhiều engine để thay
- Điểm yếu: model mặc định phi thương mại; chưa mục nào được rà cho thương mại; dự án lớn nên cài đặt và dung lượng nặng; chưa nghe chất lượng tiếng Việt; chưa chạy thử
- Có nên dùng: **6/10** cho agency (bản 2026-10 cũ chấm 8/10 vì chưa thấy giấy phép model). Dùng để thử nghiệm và nội dung nội bộ. Việc cho khách hoặc kiếm tiền: chọn engine có giấy phép thương mại rõ ràng, hoặc xin phép chủ model trước. Cần giọng thương mại ngay: `repos/capcut-tts-api.md` (không chính thức, dễ vỡ) hoặc giọng trả phí có điều khoản thương mại

## Link
- Repo: https://github.com/debpalash/VoiceStudio
- Trang chủ: https://voicestudio.sh
- Giấy phép model: `docs/licensing/model-inventory.md` trong repo
- Liên quan trong kho: `repos/ai-auto-generate-video.md` (dùng OmniVoice làm TTS), `repos/capcut-tts-api.md`, `repos/supertonic.md`, `content/script-video-96-omnivoice-studio.md`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# API cục bộ cổng 3900 (không cần mạng ngoài). Khám phá khả năng:
import json, urllib.request
BASE = "http://127.0.0.1:3900"
doc = json.load(urllib.request.urlopen(f"{BASE}/.well-known/voicestudio-speech"))
print(doc.get("schema") or list(doc)[:5])   # voicestudio.speech.v1
# Phiên âm: python -m backend.speech_client transcribe recording.wav
# Nếu đặt OMNIVOICE_API_KEY thì gửi header Authorization: Bearer <khoá>
```
Chưa chạy thử trên máy thật. Dùng MCP khi cần sinh giọng (xem OpenClaw).

### OpenClaw
```bash
# MCP server gắn tại /mcp của backend (HTTP hoặc stdio); công cụ: generate_speech, clone_voice,
# design_voice, describe_voice, transcribe, list_voices, check_health
export OMNIVOICE_MCP_OUTPUT_MODE=files          # trả đường dẫn thay vì WAV base64
export OMNIVOICE_MCP_BASE_PATH=/opt/voice/out   # vùng được đọc/ghi file
npx skills add debpalash/VoiceStudio
```

### Antigravity
```bash
# Docker hoặc bản cài theo docs/install/docker.md; backend cổng 3900
# Chưa chạy thử trên VPS. Không mở cổng 3900 ra internet; đặt OMNIVOICE_API_KEY nếu truy cập từ máy khác
```
> ⚠️ Trọng số model mặc định phi thương mại — không đưa vào luồng sản xuất cho khách khi chưa có giấy phép riêng. Người duyệt phải đọc `docs/licensing/model-inventory.md` trước khi bật cho agent.

---
name: mirage-tesseract
description: >
  Bộ công cụ edit video/motion graphics/compositing/âm thanh native cho AI agent, của Mirage
  (công ty rebrand từ Captions). Cài như 1 skill (npx skills add mirage-hq/Tesseract), agent
  tự thao tác layer/keyframe/mask/adjustment layer/sound thay vì phải mở Premiere/CapCut tay.
  QUAN TRỌNG: chỉ chạy macOS hoặc Windows local — không hỗ trợ Linux/WSL/cloud rendering, nên
  không chạy được trên VPS. Ra mắt 22/9/2026, free.
---

# Mirage Tesseract — Video Editor Native Cho AI Agent

## TL;DR
"Premiere và After Effects viết lại cho agent" — thay vì agent phải sinh code hay điều khiển UI
qua screenshot, Tesseract cho agent thao tác trực tiếp với khái niệm dựng phim thật (layer,
composition, keyframe, mask, adjustment layer, timing, sound) qua 1 project file có thể chỉnh
sửa lại được nhiều lần, không chỉ ra file MP4 cuối cùng không sửa được.

## Tool này dùng để làm gì
Trước giờ muốn AI agent "edit video" thì hoặc agent viết code (Remotion, kiểu mày đang làm),
hoặc agent phải điều khiển 1 app edit qua automation UI (chậm, dễ vỡ). Tesseract cho 1 hướng
thứ ba: engine dựng phim thật (chính là engine đứng sau app Captions) expose ra dưới dạng tool
mà agent gọi trực tiếp — tạo layer, chỉnh keyframe, thêm mask, mix âm thanh — kết quả là 1
project file giữ được cấu trúc, sửa lại được, không phải render 1 lần là xong.

## Setup từng bước

1. Cài skill vào agent (Claude Code, ChatGPT desktop, hoặc Antigravity):
```bash
npx skills add mirage-hq/Tesseract
```
2. Agent tự đọc hướng dẫn cài, dựng CLI tương ứng cho máy, verify checksum.
3. Đưa footage/ảnh/audio cho agent, mô tả video muốn làm.
4. Agent thao tác trực tiếp trên project (thêm layer, animate, mix nhạc), preview, chỉnh sửa
   theo phản hồi, cuối cùng render local.

## Ví dụ thực tế

Đưa cho agent 5 clip quay tay + 1 file voiceover, nói "cắt còn 40s, thêm caption động, giảm
noise nền, tăng vibrance cho đoạn ngoài trời" — agent tạo project Tesseract, cắt clip theo
timeline, thêm layer caption với keyframe animation, áp adjustment layer chỉnh màu riêng cho
đoạn cần, xuất preview cho duyệt trước khi render bản cuối — tất cả không cần mở Premiere.

## Lưu ý / Lỗi thường gặp

- **Chỉ macOS hoặc Windows, chạy local** — Linux, WSL, và cloud rendering đều KHÔNG được hỗ
  trợ. Không có cách nào chạy trên VPS Linux (agents/ANTIGRAVITY-PLAYBOOK.md, Hermes, OpenClaw
  của kho này đều chạy trên VPS Linux — Tesseract không ghép được vào pipeline 24/7 đó).
- **Cần Node.js/npm để cài** (bản thân Tesseract CLI thì không cần Node để chạy).
- **Rất mới (ra mắt 22/9/2026)** — chưa có nhiều case thực tế/review dài hạn để đối chiếu độ
  ổn định, dùng thận trọng cho việc quan trọng lúc đầu.
- Trong ChatGPT/Codex, chỉ dùng được qua desktop app với local execution — không dùng được bản
  web/cloud của ChatGPT.

## Đánh giá cá nhân

- **Điểm mạnh:** ý tưởng "agent thao tác concept dựng phim thật thay vì code hay điều khiển UI"
  là hướng đúng, giải quyết đúng khoảng trống giữa Remotion (code, không trực quan) và CapCut
  (trực quan, không agent-native). Free, không cần API key riêng.
- **Điểm yếu:** rào cản Linux/VPS là lớn nhất với setup của Tano Agency — không dùng được cho
  content factory chạy nền 24/7, chỉ dùng được khi ngồi máy cá nhân thao tác trực tiếp. Còn quá
  mới để đánh giá độ ổn định thật.
- **Có nên dùng không:** 7/10 — không thay thế được Remotion cho phần factory tự động, nhưng
  đáng thử cho công đoạn hậu kỳ cần tinh chỉnh tay (color grade, mix âm thanh) khi ngồi máy cá
  nhân, thay cho việc mở CapCut/Premiere thủ công.

## Link
- Repo: https://github.com/mirage-hq/Tesseract
- Docs: mirage.app/tesseract
- Công ty: mirage.app (trước là Captions)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# KHÔNG dùng được — Hermes chạy trên VPS Linux, Tesseract chặn Linux hoàn toàn.
# Nếu cần edit video trong pipeline Hermes, dùng Remotion (code-driven) hoặc ffmpeg thay thế.
```

### OpenClaw
```bash
# KHÔNG dùng được trên VPS. Nếu OpenClaw cần chạy Tesseract, phải trigger việc này trên máy
# cá nhân (Mac/Windows) có cài Antigravity 2.0 + skill Tesseract, không qua VPS.
```

### Antigravity (Google Antigravity 2.0, chạy local)
```bash
# Cài trong 1 agent session của Antigravity 2.0 (chạy trên máy Mac/Windows cá nhân, KHÔNG
# phải Antigravity-agent VPS riêng của kho này — 2 cái trùng tên, khác hệ thống):
npx skills add mirage-hq/Tesseract
# Sau đó mô tả video muốn làm trực tiếp trong chat của Antigravity IDE.
```
> ⚠️ Phân biệt rõ: "Antigravity" ở đây là Google Antigravity IDE (chạy máy cá nhân), khác với
> agent "Antigravity" của kho này (chạy VPS, xem `agents/ANTIGRAVITY-PLAYBOOK.md`) — 2 hệ thống
> trùng tên nhưng không liên quan, dễ nhầm khi đọc lại kho sau này.

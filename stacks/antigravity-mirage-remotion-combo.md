---
name: antigravity-mirage-remotion-combo
description: >
  Combo dựng video trên máy cá nhân (không phải VPS) — Google Antigravity 2.0 làm orchestrator
  chạy nhiều agent song song, Mirage Tesseract làm lớp hậu kỳ/motion graphics/âm thanh, Remotion
  làm lớp render code-driven cho phần factory/batch. Không thay thế pipeline VPS 24/7 hiện có,
  là quy trình bán tự động dùng khi ngồi máy cá nhân xử lý hậu kỳ kỹ hơn.
---

# Antigravity 2.0 + Mirage Tesseract + Remotion — Combo Dựng Video Trên Máy Cá Nhân

## TL;DR
Dùng khi cần dựng video chất lượng cao, cần tinh chỉnh tay (color grade, mix âm thanh, motion
graphics phức tạp) mà không muốn mở Premiere/CapCut thủ công — Antigravity 2.0 điều phối, một
agent session lo phần code-driven (Remotion), một agent session khác lo phần hậu kỳ tinh chỉnh
(Tesseract). Chạy trên máy cá nhân, không phải pipeline chạy nền 24/7 trên VPS.

## Các tool trong stack

1. **Google Antigravity 2.0** → IDE agentic, Manager view spawn tới 5 agent song song, chọn
   model (Gemini 3 Pro / Claude Sonnet 4.5 / GPT-OSS) cho từng agent.
2. **Mirage Tesseract** (`repos/mirage-tesseract.md`) → lớp hậu kỳ: layer, keyframe, mask,
   adjustment layer, mix âm thanh — thay CapCut/Premiere thủ công. Chỉ chạy Mac/Windows local.
3. **Remotion** (`stacks/remotion-template-factory.md`, `repos/remotion-superpowers.md`) → lớp
   render code-driven cho phần lặp lại theo template (data card, kinetic typography series).

## Workflow ghép nối

```
Mở Antigravity 2.0 trên máy cá nhân (Mac/Windows)
        ↓
Manager view: spawn 2 agent session song song
        ↓                              ↓
[Agent A — Remotion]            [Agent B — Tesseract]
render phần code-driven          nhận input thô (voice, ảnh AI-gen,
(data card, kinetic typography    B-roll) → cắt, layer, keyframe,
theo template có sẵn)             mix âm thanh, color grade
        ↓                              ↓
   MP4 phần A                     Project Tesseract (sửa lại được)
        └──────────┬───────────────────┘
                    ↓
        Ghép 2 phần bằng Tesseract (import MP4 từ Remotion làm 1 layer,
        overlay lên trên phần hậu kỳ đã làm) → render bản cuối
                    ↓
        Duyệt → đẩy lên Postiz / upload tay
```

## Ví dụ thực tế

Làm 1 tập Tây Du Ký Thương Trường: Agent A (Remotion) render phần kinetic typography (chữ chạy
theo giọng đọc, đã sync Whisper, badge "TDK X/16") như template đã build tuần trước. Agent B
(Tesseract) nhận file MP4 đó cộng thêm vài clip B-roll AI-gen (núi mờ sương, giấy cũ), ghép làm
intro 3 giây trước khi vào phần kinetic typography, thêm nhạc nền, chỉnh màu cho khớp giữa 2
nguồn — 2 agent chạy song song trong Manager view, xong cả 2 mới ghép bản cuối.

## Lưu ý / Lỗi thường gặp

- **Đây KHÔNG phải thay thế cho pipeline VPS 24/7** (Hermes/OpenClaw/Antigravity-agent VPS) —
  Tesseract chặn Linux hoàn toàn, combo này chỉ chạy khi ngồi máy cá nhân thao tác trực tiếp.
- **Tên trùng dễ nhầm:** "Antigravity" trong combo này là Google Antigravity 2.0 (IDE local),
  khác hẳn agent "Antigravity" của kho (VPS deploy, xem `agents/ANTIGRAVITY-PLAYBOOK.md`) —
  đọc lại kho sau này nhớ phân biệt theo ngữ cảnh, đừng nhầm 2 cái.
- **Cả 2 mảnh (Remotion + Tesseract) đều còn rất mới trong việc test thật** — Remotion đã type-
  check pass (chưa render MP4 thật do sandbox chặn domain), Tesseract mới ra mắt 22/9/2026, chưa
  có case thực tế nào chạy thử trong kho này.
- Manager view của Antigravity giới hạn tối đa 5 agent song song — với combo 2 agent (Remotion +
  Tesseract) còn dư chỗ chạy thêm việc khác cùng lúc nếu cần.

## Đánh giá cá nhân

- **Điểm mạnh:** giải đúng bài toán "cần tay nghề edit thật (color, sound) mà không muốn tự làm
  tay" — Remotion mạnh về lặp lại theo template, Tesseract mạnh về tinh chỉnh 1-lần, ghép 2 cái
  bù đắp điểm yếu cho nhau đúng chỗ.
- **Điểm yếu:** phải ngồi máy cá nhân, không tự động hoá được theo lịch như các skill khác trong
  kho (report-builder, monday-brief chạy được trên VPS theo lịch) — đây là quy trình "ngồi làm",
  không phải "chạy nền".
- **Có nên dùng không:** 7/10 — hợp cho video cần chất lượng cao/quan trọng (không phải content
  hàng ngày số lượng lớn dùng auto-router đã build tuần trước), làm khi có thời gian ngồi máy
  cá nhân xử lý kỹ.

## Link
- `repos/mirage-tesseract.md`
- `stacks/remotion-template-factory.md`
- `stacks/google-antigravity-notebooklm-combo.md` (combo Antigravity khác, dùng cho việc research)
- `agents/ANTIGRAVITY-PLAYBOOK.md` (agent VPS trùng tên, KHÔNG liên quan tới Google Antigravity)

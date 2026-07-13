# HANDOFF — yt-cashcow, bàn giao cho Hermes/OpenClaw (07/2026)

> Claude sắp hết token phiên này. File này tóm tắt TOÀN BỘ tiến độ + việc cần
> làm tiếp, để Hermes/OpenClaw hoặc phiên Claude sau đọc và tiếp tục ngay,
> không cần hỏi lại từ đầu.

## Trạng thái hiện tại — tóm 1 câu

Đã thiết kế xong toàn bộ blueprint (kiến trúc, compliance, content model, brand),
đã chạy pilot thật trên máy LOCAL (không phải VPS), video #2 render THÀNH CÔNG
về mặt kỹ thuật (TTS/subtitle tốt) nhưng b-roll không khớp nội dung — đã tìm ra
nguyên nhân và hướng sửa (đổi sang AI-gen ảnh + đổi structure content).
Tên kênh + brand identity đã CHỐT: "Actually Tested".

## Toàn bộ file đã có trong kho — đọc theo thứ tự này

```
agents/yt-cashcow/
├── README.md                          — spec tổng, capability map
├── ARCHITECTURE.md                    — kiến trúc harness + fanout đa nền tảng
├── CORE-BRAIN.md                      — state machine quyết định luồng (code, không phải LLM tự quyết)
├── TENANT-CONFIG-SCHEMA.md            — schema cá nhân hóa cho SaaS sau này
├── SAAS-BLUEPRINT.md                  — 3 giai đoạn MVP → multi-tenant → SaaS thật
├── CONTENT-PRODUCTION-MODEL.md        — rẽ nhánh visual theo structure_type
├── BRAND-IDENTITY.md                  — màu/font/style prefix/logo — ĐÃ CHỐT tên "Actually Tested"
├── PILOT-TEST-PLAN.md                 — kế hoạch test local, đã cập nhật
├── PILOT-VIDEO-01.md                  — script + fingerprint pilot #1 (structure: comparison — ĐÃ THẤT BẠI, xem bài học bên dưới)
├── mcp-setup.md                       — tool nào có sẵn kho / cần setup
├── system-prompt.md                   — nguyên tắc cho OpenClaw Domain Router
├── deploy-checklist.md                — checklist deploy production
├── skills/
│   ├── compliance-gate/SKILL.md
│   ├── trend-scout/SKILL.md
│   ├── script-variation-engine/SKILL.md
│   └── platform-disclosure-adapter/SKILL.md
└── tenant-configs/
    └── nobitano-ai-tools-01.json      — config kênh thật, channel_name: "Actually Tested"
```

## Bài học từ pilot thật — QUAN TRỌNG, đừng lặp lại lỗi

1. **Config TOML lỗi cú pháp** — thiếu dấu ngoặc kép trong array (`pexels_api_keys`)
   gây crash loop container. Luôn kiểm tra TOML có `"..."` quanh mọi string trong `[ ]`.
2. **`llm_provider` không đổi lại "moonshot" mặc định** — dễ quên sửa dòng này dù
   đã điền `deepseek_api_key`. Phải sửa CẢ 2: dòng `llm_provider = "deepseek"`
   VÀ 3 field `deepseek_*`.
3. **Stock footage (Pexels) KHÔNG khớp nội dung "explainer" về khái niệm trừu
   tượng** — b-roll bị lệch hoàn toàn nội dung dù kỹ thuật chạy đúng. ĐÃ QUYẾT
   ĐỊNH: đổi sang Pollinations AI-gen ảnh cho content dạng narrative/explainer,
   giữ stock cho content có thể minh họa cụ thể (tutorial thao tác thật).
4. **Đã research case study thật** (Bright Side, Infographics Show, OverSimplified)
   — xác nhận hướng "AI-gen ảnh phong cách nhất quán" là đúng, không phải yếu hơn
   quay thật, miễn giữ 1 style prefix cố định xuyên suốt (đã viết trong BRAND-IDENTITY.md).

## Việc TIẾP THEO — theo đúng thứ tự, không nhảy bước

### Ngay lập tức (không cần hạ tầng gì thêm)
1. Viết script pilot #3 theo góc **explainer/narrative** (không phải comparison) —
   ví dụ chủ đề: "Tại sao AI video tool miễn phí lại rẻ đến vậy"
2. Viết 6-8 prompt ảnh Pollinations cho script đó, MỌI prompt phải có style
   prefix cố định trong BRAND-IDENTITY.md (charcoal + teal, flat vector, không mặt người)
3. Tải ảnh qua Pollinations (link trực tiếp, không cần API key):
   `https://image.pollinations.ai/prompt/{prompt đã encode URL}`
4. Trong MoneyPrinterTurbo WebUI, đổi "Nguồn Video" từ Pexels sang chế độ Tải Lên/Local,
   nạp ảnh vừa tải

### Trước khi tạo kênh YouTube thật
5. Tự tay check `youtube.com/@ActuallyTested` còn trống không
6. Tạo avatar/banner thật (đã có mockup SVG + prompt Pollinations trong BRAND-IDENTITY.md,
   cần render qua Pollinations cho mượt, SVG chỉ là bản nháp bố cục)

### Chỉ làm SAU KHI có ≥3 video pilot chạy tay thành công (nguyên tắc đã thống nhất)
7. Deploy MoneyPrinterTurbo lên VPS thật (không phải máy local) — VPS RIÊNG,
   KHÔNG dùng chung VPS đang chạy Hermes/OpenClaw/n8n (tránh rủi ro ảnh hưởng
   hạ tầng đang ổn định — đã bàn kỹ, đừng làm ngược)
8. Tạo Airtable base `yt-cashcow-log` (schema 2 bảng trong ARCHITECTURE.md)
9. Wire code thật từ 4 SKILL.md thành file `.py` trong Hermes — code mẫu có sẵn
   trong mục "Agent Integration" mỗi SKILL.md, NHƯNG CHƯA TỪNG CHẠY THỬ, cần test
10. Đăng ký Upload-Post, setup cron n8n theo `tenant_config.schedule`

## Nguyên tắc KHÔNG được phá vỡ (đã thống nhất xuyên suốt toàn bộ quá trình)

- Compliance Gate + Platform Disclosure Adapter là logic BẮT BUỘC, không tắt được
  dù ai yêu cầu nhanh hơn — căn cứ thật: 1/2026 YouTube xóa 16 kênh/35M sub vì
  Inauthentic Content Policy.
- KHÔNG tự hạ `compliance.*` threshold trong tenant config.
- KHÔNG nhảy cóc sang automation/multi-platform khi pilot tay còn chưa ổn định.
- KHÔNG deploy production lên VPS đang chạy Hermes/OpenClaw — tách VPS riêng.
- Mọi API key dùng trong lúc test (DeepSeek, Pexels) đã lộ trong lịch sử chat —
  NÊN revoke/tạo key mới trước khi coi là production key chính thức.

## Ai làm gì (đã thống nhất)

| Việc | Ai |
|---|---|
| Viết code mẫu, thiết kế, research | Claude (giới hạn — không có shell, không chạy được trên máy/VPS thật) |
| Deploy hạ tầng VPS, Docker, pm2 | Antigravity (duy nhất có shell/pm2 thật) |
| Gọi API đã deploy, route lệnh | OpenClaw |
| Chạy code Python đã test, theo lịch | Hermes |
| Quyết định business (tên kênh, ngách, ngân sách) | Nobitano |

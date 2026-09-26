# BrandScan ("Xưởng Nội Dung") — Agency Personal Brand, multi-tenant

> Đây là bản consolidate — KHÔNG viết đè lên các package đã có. BrandScan là tầng
> orchestrator nối `content-pro` (chiến lược) + `yt-cashcow` video engine (sản xuất) +
> `personal-branding-creator` (persona/format) + `brand-strategy-sprint` (onboarding, đã
> viết ở phiên trước) + pattern publisher/review-queue của `trum-san-bay` — generalize
> sang multi-tenant, mỗi khách 1 brand-config riêng.

## Spec
- **Domain:** Dịch vụ phát triển thương hiệu cá nhân đa khách, gói theo tháng
- **Job-to-be-done:** Nhận khách mới → định vị (brand-strategy-sprint) → sản xuất nội
  dung hàng ngày đúng persona/pillar đã chốt → đăng qua Postiz → đo lường
- **Người dùng:** Nobitano vận hành; khách hàng (vd Chi) cung cấp input + duyệt + (tùy
  loại brand) tự quay footage
- **Khách hàng thật đầu tiên:** Chi — gói FB content/personal brand 1tr/tháng, định vị
  lại thành tích cực/năng lượng nhưng không giảng đạo, content lifestyle ngắn hàng ngày
- **Rủi ro cao nhất:** Nhầm nhánh sản xuất — dùng AI-gen/avatar cho brand cần người thật
  lên hình → mất chính "chất lifestyle thật" khách đang bán → guardrail: xác định
  `content_source_type` ngay từ brand-strategy-sprint Bước 2, không để Content Factory tự
  đoán

## Capability Map — TÁI SỬ DỤNG, không viết lại

| Tầng | Component | Nguồn |
|---|---|---|
| Onboarding | Brand Strategy Sprint (Discovery+Channel Audit → Alignment → Implementation Plan) | Đã viết phiên trước, cần **di chuyển đúng vị trí** — xem ghi chú cleanup cuối file |
| Chiến lược pillar/cluster | `content-pillar-cluster-architecture`, `editorial-workflow-quality-gates` | `agents/content-pro/skills/` |
| Persona/format viết | `personal-branding-creator` (phễu 3-5-2, format TikTok/FB) | `skills/personal-branding-creator/SKILL.md` |
| Sản xuất video — nhánh FACELESS | 4-lớp model nguyên bản (Visual/TTS/Thumbnail/Assembly, rẽ theo structure_type) | `agents/yt-cashcow/CONTENT-PRODUCTION-MODEL.md` — dùng nguyên, không sửa |
| Sản xuất video — nhánh NGƯỜI THẬT LÊN HÌNH | **MỚI** — xem `content_source_type: human_footage` bên dưới, yt-cashcow không có nhánh này | Cần viết mới |
| Sản xuất ảnh/text | Gemini API (`gemini-2.5-flash-image`) | Theo pattern đã dùng ở `trum-san-bay` |
| Publish | Postiz self-host | `agents/trum-san-bay/postiz-*` |
| Review Queue | Airtable, pattern PENDING/APPROVE/REJECT | `agents/trum-san-bay/orchestrator.py` |

## Nhánh video mới — content_source_type

Chốt ngay ở brand-strategy-sprint Bước 2 (Alignment), không để hệ thống tự suy đoán:

| `content_source_type` | Khi nào | Quy trình |
|---|---|---|
| `faceless` | Brand không cần mặt người thật (vd tin tức, kiến thức, số liệu) | Dùng nguyên engine `yt-cashcow` 4-lớp |
| `human_footage` | Brand cá nhân, lifestyle, cần đúng con người thật (vd Chi) | Khách tự quay raw clip bằng điện thoại → gửi qua Telegram/Drive → AI chỉ làm: caption tự động (ElevenLabs nếu cần voiceover phụ, không thay giọng thật), cắt/ghép nhẹ, thumbnail (Canva/Pollinations) — **không tạo mặt/giọng thay khách** |
| `hybrid` | Đăng cả 2 loại xen kẽ theo pillar (vd Chi vừa có clip thật vừa có post text+ảnh) | Route theo pillar đã định vị ở Bước 2, không cố định 1 loại cho cả brand |

## Kiến trúc orchestrator

```
Brand Strategy Sprint (đã có) → khách duyệt Positioning Report
        │ (brand-config riêng khách, gồm content_source_type)
        ▼
content-pro: xây pillar/cluster + editorial gate cho khách này
        │
        ▼
personal-branding-creator: viết caption/script theo persona đã chốt
        │
        ├── content_source_type=faceless  → yt-cashcow 4-lớp (nguyên bản)
        ├── content_source_type=human_footage → khách gửi raw → AI edit nhẹ + caption
        └── content_source_type=hybrid → route theo pillar
        │
        ▼
Review Queue (Airtable, PENDING → khách/Nobitano duyệt)
        │
        ▼
Publisher (Postiz)
        │
        ▼
Weekly: pull analytics → ghi lại performance_learnings → content-pro điều chỉnh pillar
```

## ⚠️ Cleanup cần làm — không phải việc mới, việc dọn lại
- `skills/brand-strategy-sprint/SKILL.md` (push phiên trước) đang SAI vị trí — đây là
  skill riêng của agent BrandScan, phải nằm ở `agents/brandscan/skills/brand-strategy-sprint/SKILL.md`,
  không phải tier `skills/` chung (tier đó dành cho skill dùng độc lập, không thuộc 1 agent
  cụ thể). Cần copy sang đúng chỗ rồi xóa bản cũ, không để tồn tại 2 bản.
- Thiếu: TL;DR ngắn, rating [x/10], Agent Integration section cho Hermes/OpenClaw/Antigravity
  trong `brand-strategy-sprint/SKILL.md` — bổ sung khi di chuyển
- Chưa có script video kèm theo (quy trình bắt buộc) — cần viết `content/script-video-XXX-brandscan.md`
  sau khi package ổn định, đánh số theo đúng scan `/content/` thực tế
- TRACKER.md chưa regenerate sau các thay đổi phiên này

## Việc thật còn thiếu để chạy được với Chi
1. Viết SKILL.md cho nhánh `human_footage` (chưa tồn tại ở đâu trong kho)
2. Multi-tenant hóa: brand-config riêng cho Chi, tách khỏi brand-config Trùm Sân Bay
3. Postiz self-host deploy xong (đang chờ, phiên trước)
4. Chạy thử Brand Strategy Sprint thật với Chi (hoặc dữ liệu Chi đã có sẵn nếu đã từng
   discovery rồi) → ra Positioning Report → khách duyệt → mới sản xuất

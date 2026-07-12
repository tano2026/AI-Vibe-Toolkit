# Tenant Config Schema

> Đây là "cá nhân hóa" — mọi thứ khác nhau giữa kênh A và kênh B nằm hết ở đây,
> không nằm trong code. Code (CORE-BRAIN.md) đọc config này, không hardcode gì.

## Schema đầy đủ

```json
{
  "tenant_id": "uuid-duy-nhat",
  "channel_name": "text",
  "niche": "text — vd: AI tools review, personal finance, history facts",
  "brand_voice": {
    "tone": "casual | formal | energetic | calm",
    "language": "en | vi | ...",
    "banned_topics": ["chính trị", "y tế cụ thể", "..."],
    "sample_scripts": ["url hoặc text mẫu để LLM học giọng"]
  },
  "platforms": {
    "youtube": {"enabled": true, "upload_credentials_ref": "vault-key-xxx"},
    "tiktok": {"enabled": true, "upload_credentials_ref": "vault-key-yyy"},
    "instagram": {"enabled": false},
    "facebook": {"enabled": false}
  },
  "compliance": {
    "structure_similarity_threshold": 8,
    "hook_similarity_threshold": 6,
    "claim_overlap_threshold": 0.4,
    "min_commentary_ratio": 0.15,
    "review_sample_rate": 0.1
  },
  "render_engine_config": {
    "engine": "moneyprinterturbo",
    "tts_provider": "edge | resona | f5-tts",
    "resolution_long": "1920x1080",
    "resolution_short": "1080x1920"
  },
  "schedule": {
    "trend_scan_frequency": "daily | 2x-daily | weekly",
    "publish_cap_per_day": 2
  },
  "billing_tier": "free | pro | agency"
}
```

## Nguyên tắc quan trọng: 2 loại giá trị không được để tenant tự chỉnh

| Loại | Ai chỉnh được | Vì sao |
|---|---|---|
| `compliance.*` threshold | Chỉ admin hệ thống (Nobitano/team vận hành), KHÔNG lộ ra UI cho tenant tự hạ | Nếu để khách hàng tự hạ ngưỡng compliance để "đăng nhanh hơn" → hệ thống chung mang tiếng, ảnh hưởng uy tín tất cả tenant khác dùng chung engine |
| Platform disclosure rule (YouTube/TikTok toggle logic) | Không ai chỉnh được — hardcode trong code, vì đây là luật platform thật, không phải sở thích | Sai 1 dòng là tenant nào cũng dính risk |

`brand_voice`, `niche`, `platforms.enabled`, `schedule` — đây mới là phần tenant
tự chỉnh được thoải mái, tương đương "cá nhân hóa" theo đúng nghĩa SaaS.

## Data isolation — mỗi tenant 1 rolling fingerprint_history riêng

Compliance Gate so sánh video mới với lịch sử — **phải partition theo tenant_id**,
không được so chéo giữa các kênh khác nhau (kênh A và kênh B là 2 khách hàng khác
nhau, không liên quan gì tới nhau về structural similarity).

```
Airtable/DB record:
fingerprint_history.tenant_id = "uuid-kenh-A"   ← chỉ so trong phạm vi này
fingerprint_history.tenant_id = "uuid-kenh-B"   ← độc lập hoàn toàn
```

## Giai đoạn hiện tại (MVP 1 tenant) vs giai đoạn SaaS (N tenant)

| | MVP hiện tại (Nobitano) | SaaS sau này |
|---|---|---|
| Số tenant | 1 (hardcode 1 config) | N, dynamic |
| Nơi lưu config | 1 file JSON trong repo | DB riêng (Supabase — xem SAAS-BLUEPRINT.md) |
| Upload credentials | Env var trực tiếp | Vault/secret manager theo `upload_credentials_ref`, không lưu plaintext |
| fingerprint_history | 1 Airtable base | Partition theo tenant_id, hoặc 1 base/tenant khi scale lớn |

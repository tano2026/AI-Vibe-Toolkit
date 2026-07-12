# SaaS Blueprint — Đường đi từ MVP 1 kênh sang đa khách hàng

## 3 giai đoạn — không nhảy cóc

```
Giai đoạn 1 — MVP (hiện tại)          Giai đoạn 2 — Multi-tenant nội bộ      Giai đoạn 3 — SaaS thật
─────────────────────────────         ──────────────────────────────         ─────────────────────
1 tenant (kênh Nobitano)               Vài kênh của Tano Agency tự vận         Khách hàng ngoài tự đăng ký,
Config hardcode trong repo             hành song song, config JSON riêng       tự cấu hình qua UI, billing
Airtable free tier đủ dùng             mỗi kênh, vẫn Airtable nhưng            thật, cần DB thật + auth +
Chạy trên VPS hiện có                  partition theo tenant_id                isolation chặt hơn nhiều
                                        VPS hiện có vẫn kham được               Cần hạ tầng riêng, không
                                                                                dùng chung VPS nội bộ nữa
```

**Không build thẳng giai đoạn 3 ngay** — rủi ro over-engineer trong khi chưa
biết pipeline có thật sự ổn định/an toàn compliance ở quy mô 1 kênh chưa.
Giai đoạn 1 chạy ổn tối thiểu 4-6 tuần, không dính strike, mới lên giai đoạn 2.

## Việc gì phải đổi khi lên Giai đoạn 2 (multi-tenant nội bộ)

| Thành phần | Giai đoạn 1 | Giai đoạn 2 |
|---|---|---|
| Config | 1 file JSON | N file JSON, hoặc 1 Airtable table `tenants` |
| fingerprint_history | 1 bảng | Thêm cột `tenant_id`, mọi query Compliance Gate filter theo tenant |
| Upload credentials | Env var | Mỗi tenant 1 bộ credentials riêng, không share |
| Orchestrator (CORE-BRAIN) | Hardcode gọi 1 tenant | Loop qua danh sách tenant active, mỗi tenant 1 lần chạy state machine độc lập |
| VPS resource | 1 luồng render | N luồng — cần check tài nguyên VPS có đủ chạy song song không, có thể phải queue thay vì chạy đồng thời |

## Việc gì phải đổi khi lên Giai đoạn 3 (SaaS thật, khách ngoài)

Đây là phần khác biệt lớn nhất — **Airtable không phù hợp nữa** ở quy mô này
(rate limit, không có row-level security thật, không hợp cho billing/auth phức tạp).

| Thành phần | Đổi thành |
|---|---|
| Database | Supabase (Postgres) — đã có MCP sẵn trong hệ thống Claude, row-level security theo tenant_id thật, auth built-in |
| Auth | Supabase Auth — khách tự đăng ký, không phải admin tạo config tay |
| Secret management | Không lưu credentials trong DB thường — dùng vault riêng (Supabase Vault hoặc tương đương) |
| Billing | Cần tích hợp payment (Stripe hoặc tương đương) theo `billing_tier` trong tenant config |
| Frontend | Cần UI thật cho khách tự chỉnh `brand_voice`, `platforms`, `schedule` — không phải sửa JSON tay |
| VPS | Không chạy trên VPS nội bộ Tencent Cloud nữa — cần hạ tầng scale được (dù VPS đơn giản vẫn render được, nhưng nhiều tenant đồng thời cần queue/worker pattern thật, vd job queue + worker pool) |
| Compliance threshold | KHÔNG BAO GIỜ để khách tự chỉnh xuống mức nguy hiểm — đây là phần giữ nguyên tắc dù ở SaaS tier nào (đã ghi rõ trong TENANT-CONFIG-SCHEMA.md) |

## Nguyên tắc xuyên suốt cả 3 giai đoạn — không đổi dù ở tier nào

1. Compliance Gate + Platform Disclosure Adapter là **hard-coded logic chung**,
   không phải feature bán theo tier, không phải thứ khách hàng tắt được.
2. CORE-BRAIN (state machine) là 1 codebase duy nhất phục vụ mọi tenant — không
   fork code riêng cho từng khách hàng, chỉ khác nhau ở config data.
3. Mọi thứ tenant tự chỉnh được phải đi qua TENANT-CONFIG-SCHEMA.md — không có
   đường tắt chỉnh trực tiếp vào code khi "khách VIP cần gấp".

## Việc cho "thằng trùm design" khi đóng gói fullstack

Khi giao brief cho design/build fullstack, cần rõ 3 lớp tách biệt:
- **Lớp Engine** (CORE-BRAIN + skills) — build 1 lần, dùng chung
- **Lớp Config** (TENANT-CONFIG-SCHEMA) — data, không phải code
- **Lớp Giao diện** (chưa có, cần thiết kế mới cho Giai đoạn 3) — form/dashboard
  để tenant tự chỉnh config, xem Analytics, duyệt video review — đây là phần
  duy nhất thật sự cần UI/UX design mới, phần còn lại là backend/pipeline.

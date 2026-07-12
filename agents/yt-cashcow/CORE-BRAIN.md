# CORE BRAIN — Orchestrator Decision Engine

> Đây là "bộ não" thật của hệ thống — không phải danh sách skill, mà là state
> machine quyết định khi nào chuyển bước, khi nào chặn, khi nào hỏi người.
> Viết tenant-agnostic ngay từ đầu để sau này 1 codebase phục vụ N kênh/N khách hàng.

## Nguyên tắc cấy não

**Não KHÔNG nằm trong prompt LLM.** Não nằm ở state machine + rule table dưới đây,
chạy bằng code Python thuần trong Hermes. LLM chỉ được gọi ở những ô cụ thể cần
sáng tạo (viết script, chấm compliance) — mọi quyết định luồng (chuyển bước tiếp,
chặn, bounce, hỏi người) là code, không phải LLM tự quyết.

Lý do: LLM quyết định luồng → không đoán trước được, khó debug, dễ bị prompt
injection từ nội dung trend scrape về. Code quyết định luồng → deterministic,
audit được, LLM chỉ làm phần việc nó giỏi nhất (sinh nội dung, đánh giá ngữ nghĩa).

## State Machine

```
IDLE
  │ trigger: cron | manual command | webhook
  ▼
TREND_SCANNING          (đọc tenant.niche, tenant.platforms)
  │ output: topic_brief
  ▼
SCRIPTING                (đọc tenant.brand_voice, tenant.fingerprint_history)
  │ output: script + fingerprint
  ▼
COMPLIANCE_CHECK          (đọc tenant.compliance_threshold)
  │
  ├── FAIL → quay lại SCRIPTING (max 3 lần retry, xem rule bên dưới)
  │
  └── PASS ▼
RENDERING                 (đọc tenant.render_engine_config)
  │ output: video master (YouTube long-form)
  ▼
PLATFORM_FANOUT           (đọc tenant.platforms — có thể là subset)
  │ output: N bản theo platform tenant chọn
  ▼
DISCLOSURE_ADAPT          (đọc platform rules — CỐ ĐỊNH, không tenant-config được,
  │                         vì đây là luật platform, không phải sở thích khách hàng)
  ▼
REVIEW_GATE                (đọc tenant.review_sample_rate, mặc định 1/10)
  │
  ├── rơi vào diện review → PENDING_HUMAN_APPROVAL → chờ webhook confirm
  │
  └── không → ▼
PUBLISHING                 (đọc tenant.upload_credentials, đã encrypt riêng)
  │
  ▼
ANALYTICS_COLLECT
  │
  └──────────────▶ ghi vào tenant.fingerprint_history, quay lại TREND_SCANNING
```

## Rule Table — quyết định cứng, không để LLM tự quyết

| Điều kiện | Hành động | Ai/cái gì quyết |
|---|---|---|
| COMPLIANCE_CHECK fail lần 1-2 | Bounce lại SCRIPTING, kèm lý do cụ thể | Code (rule cố định) |
| COMPLIANCE_CHECK fail lần 3 liên tiếp cùng topic | Dừng, đẩy topic này vào `blocked_topics`, quay lại TREND_SCANNING lấy topic khác, KHÔNG tự hạ ngưỡng | Code — LLM không được phép tự nới ngưỡng |
| Video rơi vào tenant.review_sample_rate | Dừng ở PENDING_HUMAN_APPROVAL, timeout 24h | Code + webhook người |
| Phát hiện tín hiệu channel bị strike/flag (đọc qua Analytics API) | Dừng TOÀN BỘ auto-publish của tenant đó ngay, không chờ video đang chạy | Code — ưu tiên cao nhất, override mọi state khác |
| tenant.platforms rỗng hoặc invalid | Không chạy PLATFORM_FANOUT, log lỗi, báo admin | Code |
| Topic thuộc danh mục nhạy cảm (chính trị/y tế/tài chính-advice) | Dừng ở SCRIPTING, chuyển PENDING_HUMAN_APPROVAL sớm, trước cả render | Code, có blocklist từ khóa + LLM double-check |

## Vai trò LLM trong từng ô (chỉ nơi cần sáng tạo/đánh giá ngữ nghĩa)

| Ô | LLM làm gì | Model tier (qua OmniRoute) |
|---|---|---|
| TREND_SCANNING | Chấm điểm topic theo search volume/cạnh tranh | reasoning (DeepSeek R1) |
| SCRIPTING | Viết script + tự chấm commentary_ratio | creative (Claude Sonnet) |
| COMPLIANCE_CHECK | Chỉ phần similarity ngữ nghĩa (không phải structure/hook — đó là code) | reasoning (DeepSeek R1) |
| Mọi quyết định chuyển state | KHÔNG — code thuần | — |

## Vì sao tách vậy — để SaaS hóa được sau này

Nếu não nằm trong prompt riêng từng kênh (như thiết kế v1 ban đầu — system-prompt.md
viết cứng cho "Nobitano's channel") → mỗi khách hàng mới phải viết lại prompt,
không scale. Tách state machine ra code chung + tenant_config là data → thêm khách
hàng mới = thêm 1 record config, không viết code mới.

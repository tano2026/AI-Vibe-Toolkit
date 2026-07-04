# Architecture — Sales CEO

```
                    Sales CEO Orchestrator
                    (nhận task, phân loại: tra cứu / quyết định / thực thi tài liệu)
                              |
        +---------------------+---------------------+
        |                     |                     |
    COLLECTOR             VALIDATOR              EXECUTOR
   (thu raw)          (chấm rủi ro/tin cậy)    (ra tài liệu/action)
        |                     |                     |
  market-research       finance-billing-ops    sales-playbook
  competitor-research   council (nếu mơ hồ)    outbound-engine
  lead-dossier           ceo-decision-lens      negotiation-deal-structuring
  lead-intelligence                             gtm-strategy
        |                     |                     |
        +---------------------+---------------------+
                              |
                       SYNTHESIZER
              (business-guru lens: what / why / risk / next step)
                              |
                    Output: quyết định / tài liệu / plan
                     (KHÔNG tự gửi/ghi — chờ confirm)
```

## Luồng dữ liệu theo loại task

### Task loại 1 — "Nghiên cứu/tra cứu" (VD: "đối thủ X đang làm gì")
```
Collector (competitor-research + market-research) → Synthesizer → Output báo cáo
```
Bỏ qua Validator/Executor nếu chỉ là tra cứu thuần, không có quyết định tiền/rủi ro.

### Task loại 2 — "Ra quyết định" (VD: "deal này có nên giảm giá không")
```
Collector (lead-dossier: lấy context deal)
    → Validator (finance-billing-ops: tính rủi ro tiền + ceo-decision-lens: risk/return/reversibility)
    → [nếu vẫn mơ hồ] council: 4 voice tranh luận
    → Synthesizer → Output: quyết định + rủi ro kèm số liệu, KHÔNG tự thực thi
```

### Task loại 3 — "Thực thi tài liệu" (VD: "viết battle card", "xây outbound sequence")
```
Collector (market-research/competitor-research nếu cần data mới)
    → Executor (sales-playbook / outbound-engine / negotiation-deal-structuring / gtm-strategy)
    → Synthesizer → Output: file tài liệu hoàn chỉnh, sẵn dùng
```

### Task loại 4 — "Vận hành pipeline" (VD: "check pipeline HubSpot có deal nào stuck")
```
hubspot-mcp (đọc data) → Validator (finance-billing-ops nếu liên quan tiền)
    → Synthesizer → Output: list deal cần action + đề xuất, KHÔNG tự update CRM
```

## Guardrail cứng

1. Mọi output có số tiền/giá/pháp lý → PHẢI kèm dòng "Rủi ro:" rõ ràng.
2. Agent KHÔNG được tự gọi tool ghi/gửi (HubSpot write, Gmail send, outbound send thật) —
   chỉ soạn nội dung, Nobitano confirm rồi Hermes/OpenClaw mới thực thi.
3. Khi quyết định có tính "không thể đảo ngược" (VD: cam kết giá dài hạn, ký hợp đồng) →
   bắt buộc qua `council` trước khi chốt khuyến nghị.
4. Không bịa số liệu thị trường/tài chính — nếu không tra được, nói rõ "chưa có data,
   cần research thêm" thay vì đoán.

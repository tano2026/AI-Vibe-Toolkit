# Kiến trúc — An Bình / ABTRIP Ops Analyst

## Sơ đồ orchestrator

```
                    ┌─────────────────────────────┐
                    │   Ops Analyst Orchestrator   │
                    │  (đọc câu hỏi, phân loại     │
                    │   route sang nhánh phù hợp)  │
                    └──────────────┬───────────────┘
                                   │
        ┌──────────────┬──────────┼──────────┬──────────────┐
        ▼              ▼          ▼          ▼              ▼
   [Câu hỏi        [Câu hỏi   [Câu hỏi   [Cần viết    [Câu hỏi chính
    khách hàng/     đối thủ]   data nội   content       sách hàng
    complaint]                  bộ]        OTA]          không/nhập cảnh]
        │              │          │          │              │
        ▼              ▼          ▼          ▼              ▼
  customer-pattern  competitive- Google    ota-content-  aviation-policy-
  -analysis         intel-       Drive/    strategy      lookup
                    ground-      Sheets                  (BẮT BUỘC qua
                    handling                              Validator)
        │              │          │          │              │
        └──────────────┴──────────┴──────────┴──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │   Validator (source-eval)    │
                    │  - chấm độ tin cậy nguồn      │
                    │  - flag nguồn cũ/mâu thuẫn    │
                    │  - BẮT BUỘC với mọi output    │
                    │    liên quan hàng không       │
                    └──────────────┬───────────────┘
                                   ▼
                    ┌─────────────────────────────┐
                    │   Analyst (pandas/matplotlib)│
                    │  - xử lý số liệu thật nếu có  │
                    └──────────────┬───────────────┘
                                   ▼
                    ┌─────────────────────────────┐
                    │   Synthesizer (data-          │
                    │   storytelling)               │
                    │  - ra report/docx/pdf          │
                    │  - insight + recommendation    │
                    │  - KHÔNG tự gửi/đăng/ghi        │
                    └─────────────────────────────┘
```

## Luồng dữ liệu theo loại câu hỏi

| Loại input | Skill não xử lý | Nguồn data (Tay) | Output |
|---|---|---|---|
| Complaint/booking pattern | `customer-pattern-analysis` | Google Sheets/Drive (nếu có export), hoặc data user paste tay | Report + chart top 3 vấn đề lặp lại |
| Đối thủ ground handling (dnata, VIAGS...) | `competitive-intel-ground-handling` | web_search, Similarweb | Bảng so sánh giá/dịch vụ + gap để định vị An Bình |
| Content OTA/listing | `ota-content-strategy` | Brand foundation doc (`AnBinh_Brand_Foundation_v1.md`) + web_search tham khảo | Draft content (chưa đăng) |
| Chính sách hàng không/nhập cảnh | `aviation-policy-lookup` | web_search bắt buộc (Timatic-style luôn cần verify mới nhất) | Câu trả lời + trích nguồn + disclaimer |

## Vì sao KHÔNG có tầng Action/Confirm

Agent này chốt ở mức "Tra cứu + Phân tích" — không có sub-agent Executor gọi API
ghi/gửi. Nếu sau này Nobitano muốn nâng cấp agent này lên mức hành động (tự trả lời
khách qua HubSpot, tự cập nhật OTA listing), cần thêm:
1. Sub-agent `Executor` mới, tách riêng khỏi Synthesizer
2. Tầng `Confirm` bắt buộc trước mọi lệnh ghi/gửi (theo đúng pattern Harness Engineering
   đã ghi trong kho: state machine bằng code thuần, không để LLM tự quyết luồng)
3. Bật thêm connector Gmail/HubSpot-write, hiện đang tắt có chủ đích

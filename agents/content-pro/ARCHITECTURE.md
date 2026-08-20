# Architecture — Content Pro

## Sơ đồ tổng thể

```
                         Content Orchestrator
                    (nhận yêu cầu, xác định loại)
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                  │
         Bước 0            Bước 1-2            Bước 3-4
      Xác định loại      Xây khung + Duyệt    Sản xuất + Publish
      yêu cầu            khung                + Phân phối
              │                 │                  │
              ▼                 ▼                  ▼
     Content one-off      content-pillar-      editorial-workflow-
     (viết ngay,          cluster-             quality-gates
     không cần khung)     architecture              │
              │                 │                    ▼
              │                 ▼              [Gọi skill chiến
              │          content-strategy-      thuật: viral-hooks,
              │          review-gate            content-engine,
              │          (5 câu hỏi,             brand-voice...]
              │          PASS mới đi tiếp)             │
              │                 │                       ▼
              │                 │                content-distribution-
              │                 │                system (sau publish)
              └────────┬────────┴──────────┬─────────────┘
                       ▼                    ▼
                 [Skill chiến thuật     [Audit refresh
                  viết trực tiếp]        định kỳ 6-8 tháng]
```

## Luồng dữ liệu

1. **Input:** yêu cầu content (mới/one-off) + brand/kênh cụ thể
2. **Tra cứu:** `content-brand-playbooks.md` — nếu brand đã có trong 5 playbook, dùng làm điểm khởi đầu; brand mới → không suy đoán, research trước
3. **Xây khung** (nếu không phải one-off): `content-pillar-cluster-architecture` sinh ra Pillar/Cluster
4. **Stress-test khung:** `content-strategy-review-gate` — 5 câu hỏi, FAIL thì quay lại bước xây khung, không đi tiếp
5. **Sản xuất có kiểm soát:** `editorial-workflow-quality-gates` điều phối qua 5 bước, gọi đúng skill chiến thuật cho từng bước (không tự viết)
6. **Sau publish:** `content-distribution-system` gắn task phân phối + đưa vào lịch audit

## Khác biệt kiến trúc so với Research Analytics Pro

| | Research Analytics Pro | Content Pro |
|---|---|---|
| Vai trò chính | Tự nghiên cứu + tự viết báo cáo | Điều phối — không tự viết, gọi skill chiến thuật có sẵn |
| Input | Câu hỏi thị trường | Yêu cầu content + brand cụ thể |
| Output cuối | Báo cáo/Roadmap | Content đã publish + kế hoạch phân phối |
| Review gate | ceo-stress-test + dual-review độc lập | content-strategy-review-gate (đơn, chưa có dual-review) |

## Điểm mở rộng trong tương lai

- Chưa có dual-review độc lập cho content (như `research-independent-review-gate`) — có thể thêm nếu content chiến lược lớn cần 2 người đọc độc lập trước khi duyệt
- `content-brand-playbooks.md` mới có 5 brand — mở rộng khi Nobitano có brand/kênh mới
- Chưa tích hợp trực tiếp với Postiz (lên lịch đăng) — hiện `content-distribution-system` chỉ ra checklist, chưa tự động tạo lịch đăng thật

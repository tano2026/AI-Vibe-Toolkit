# Architecture — Customer Satisfaction Pro

## Sơ đồ luồng

```
Inbox/ticket/comment mới (Facebook/Zalo OA/Email — chưa nối thật)
                    │
                    ▼
       churn-risk-escalation-discipline
       Bước 1: Phân loại NGAY — rời bỏ thật hay phàn nàn nhỏ?
                    │
        ┌───────────┴───────────┐
   Rời bỏ thật              Phàn nàn nhỏ
   → Escalate NGAY            → Áp luật thường (>=3 lần)
   (không đợi lặp lại)          → Theo dõi, chưa cần escalate
        │                           │
        ▼                           ▼
   Gắn cờ kèm bằng chứng      Xếp hàng theo SLA kênh +
   (nguyên văn + thời gian    độ khó giảm dần
   + giá trị khách nếu có)          │
        │                           ▼
        └──────────────┬────  Soạn draft trả lời
                        ▼      (KHÔNG tự gửi)
              critical-path-briefing
        Lọc: việc nào cần Nobitano quyết,
        việc nào agent tự theo dõi tiếp
                        │
                        ▼
              Báo cáo (median/P90, không trung bình)
```

## Khác biệt so với 7 Pro Agent kia

| | Customer Satisfaction Pro | 7 Pro Agent trước |
|---|---|---|
| Nguồn gốc | Phát hiện khoảng trống (so sánh AI Employees) | Nhu cầu vận hành trực tiếp |
| Kênh thật | Chưa nối (Facebook/Zalo OA/Email — TBD) | Đã có brand thật dùng (ABTRIP, Trùm Sân Bay...) |
| Độ chín | Khung + luật, chưa test | Đã test/dùng thật ở nhiều mức độ |

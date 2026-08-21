# Architecture — Media Pro

## Sơ đồ luồng

```
Content Pro bàn giao content đã sản xuất xong
                    │
                    ▼
        Pre-Publish Gate (4-đối-chiếu)
     nội dung / kênh / giờ / PACK khớp?
                    │
        ┌───────────┴───────────┐
      Lệch → DỪNG            Khớp → cho phép đăng
        │                         │
   Báo lại người phụ trách        ▼
   sửa/xin duyệt lại        [Người/tool đăng thật]
                                  │
                          Đợi 24-72h
                                  │
                                  ▼
                     Performance Reader
              đọc retention/watch time đúng ngưỡng
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
              (a) Viral sai   (b) Đúng đt   (c) Fail thật
              đối tượng       reach thấp
                    │             │             │
              Giảm phân phối  Tăng phân phối  Trả Content
              rộng, giữ học   /thử paid boost  mổ lại hook
                    │             │
                    └──────┬──────┘
                           ▼
                   Iterator (nếu thắng)
                3 variant trong 7 ngày
                (đổi hook/format/angle)
```

## Song song: Cross-Channel Analysis

```
Sau khi có ≥5 content cùng loại đăng đủ nhiều kênh
                    │
                    ▼
      Lấy data từng kênh qua vidIQ MCP
                    │
                    ▼
      Chuẩn hoá % (không so view thô)
                    │
                    ▼
      Tìm pattern lặp lại → khuyến nghị phân bổ
```

## Song song: Escalation Path

```
Theo dõi comment liên tục
        │
Cùng 1 phàn nàn xuất hiện lần thứ mấy?
        │
   <3 lần → không hành động đặc biệt (comment thường)
        │
   ≥3 lần → Escalate: tạo task cho CEO + Content
            (Content sửa từ gốc trong content sau,
            KHÔNG tự trả lời chống chế từng comment)
```

## Khác biệt kiến trúc so với Content Pro

| | Content Pro | Media Pro |
|---|---|---|
| Vai trò | Tạo (pillar/cluster/viết) | Phân phối + đo hiệu suất sau khi tạo |
| Input | Yêu cầu content mới | Content đã sẵn sàng từ Content Pro |
| Output | Content đã publish | Quyết định iterate/escalate/phân bổ kênh |
| Review gate | content-strategy-review-gate (trước sản xuất) | Pre-Publish Gate (trước đăng, sau sản xuất) |

## Điểm mở rộng tương lai

- Chưa tích hợp trực tiếp comment moderation tool — hiện escalation path là quy trình thủ công đếm số lần phàn nàn, có thể tự động hoá nếu có sentiment-classifier tích hợp trực tiếp
- Chưa có dual-review độc lập (như research-independent-review-gate) — có thể thêm nếu quyết định phân bổ ngân sách media lớn cần 2 người đọc độc lập

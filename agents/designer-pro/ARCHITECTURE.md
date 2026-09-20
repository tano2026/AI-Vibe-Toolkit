# Architecture — Designer Pro

## Sơ đồ luồng

```
Brief từ Sales-CEO/Digital Marketing Agent/Media Pro
                    │
                    ▼
        Đọc đúng PACK (design tokens) — KHÔNG suy đoán,
        thiếu token → hỏi CEO bổ sung PACK, không tự bịa màu
                    │
                    ▼
     sales-marketing-collateral-production
     (chọn đúng luật theo loại output: deck/ads/battlecard...)
                    │
                    ▼
          Tạo ảnh/video thật qua google-flow-mcp
          (Nano Banana Pro cho ảnh, Veo 3.1 cho video)
          — hoặc Canva qua OpenClaw nếu cần UI thao tác tay
                    │
                    ▼
              design-quality-gate
          (8 mục kiểm tra — PASS hết mới đi tiếp)
                    │
        ┌───────────┴───────────┐
      FAIL → sửa, chạy lại     PASS → giao kèm
      đủ 8 mục                 design-spec-*.md
                                     │
                                     ▼
                    Giao cho Sales/Marketing/Media
```

## Kết nối với google-flow-mcp (mới, chưa có ở lần thiết kế designer.md gốc)

Bản designer.md gốc chỉ ghi "generate ảnh AI → gọi API ngoài, ghi rõ trong spec" mà chưa chỉ định cụ thể dùng gì — giờ đã có google-flow-mcp (setup an toàn, dùng API chính thức Google AI, không rủi ro ToS như FlowKit) làm động cơ chính thức:

```
Nano Banana Pro (gemini-3-pro-image) → ảnh chất lượng cao, free
Nano Banana 2 (gemini-3.1-flash-image) → ảnh nhanh, free
Veo 3.1 → video cinematic có âm thanh, trả phí
```

## Khác biệt kiến trúc so với 6 Pro agent kia

| | Designer Pro | Các Pro agent khác |
|---|---|---|
| Core kiến thức | Sống trong agents/company/roles/designer.md (không tách vào system-prompt riêng, tránh trùng lặp nội dung đã tốt) | Sống trong system-prompt.md riêng của agent |
| Output chính | File binary (ảnh/video), không phải text | Text/report/quyết định |
| Tầng Tay quan trọng nhất | google-flow-mcp (tạo ảnh thật) | Thường là research/CRM tools |

## Điểm mở rộng tương lai

- Chưa có template library thật (chỉ có nguyên tắc "lặp ≥3 lần thì đóng template" — chưa có kho template thật lưu theo PACK)
- Chưa tích hợp Canva API thật (mới ghi "OpenClaw thao tác browser" — cách gián tiếp, chưa có API trực tiếp)

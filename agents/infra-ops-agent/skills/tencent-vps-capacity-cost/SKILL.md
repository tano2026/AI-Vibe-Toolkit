---
name: tencent-vps-capacity-cost
description: >
  Capacity planning và tối ưu chi phí riêng cho VPS Tencent Cloud chạy agent Hermes/
  OpenClaw/Antigravity. Dùng khi user hỏi "tốn bao nhiêu", "có nên upgrade VPS không",
  "resource đang dùng sao", trước khi quyết định resize/scale hạ tầng.
---

# Tencent Cloud VPS — Capacity & Cost

## TL;DR
Trước khi resize/scale VPS Tencent Cloud, luôn có số liệu thật (CPU/RAM/disk usage +
cost hiện tại) rồi mới khuyến nghị — không đoán "chắc cần lên gói cao hơn".

## Khi nào dùng
- Nghi ngờ VPS thiếu resource (agent chạy chậm, OOM, disk đầy)
- Cân nhắc thêm agent/service mới (VD: Chatwoot cần VPS riêng ~4GB RAM — theo note
  đã có trong kho) lên cùng VPS hay tách riêng
- Review chi phí Tencent Cloud định kỳ

## Quy trình

### 1. Thu thập số liệu thật trước
Yêu cầu Antigravity cung cấp (agent này không tự SSH lấy):
- CPU/RAM/disk usage trung bình + peak (7-14 ngày gần nhất)
- Số agent/service đang chạy trên VPS, resource mỗi cái chiếm bao nhiêu
- Gói VPS hiện tại (spec + giá/tháng)

### 2. Tính toán capacity
- Nếu peak CPU/RAM thường xuyên >80% → cảnh báo cần scale, không chờ tới khi sập.
- Nếu usage trung bình <40% liên tục → có thể đang overpay, xem xét downsize.
- Service mới cần thêm resource (VD: Chatwoot ~4GB RAM) → kiểm tra VPS hiện tại còn dư
  đủ không, hay cần VPS riêng — đừng nhồi thêm vào VPS đang gần đầy.

### 3. So sánh chi phí trước khi khuyến nghị
- Upgrade gói hiện tại vs tách VPS riêng cho service mới — so sánh giá cụ thể, không
  chỉ nói "nên tách ra".
- Với Tencent Cloud, note: giá theo giờ/tháng khác nhau đáng kể — nếu chạy 24/7 dài hạn,
  gói theo tháng/năm thường rẻ hơn theo giờ.

### 4. Output khuyến nghị
```
Usage hiện tại:     [CPU/RAM/disk, trung bình + peak]
Cần thêm gì:        [service mới cần bao nhiêu resource]
Khuyến nghị:        [scale VPS hiện tại / tách VPS riêng / giữ nguyên]
Chi phí ước tính:   [so sánh option, có số cụ thể]
Rủi ro:             [downside — VD: downsize sai làm agent OOM giữa lúc chạy]
```

## Ví dụ thực tế
User: "Chatwoot cần VPS riêng ~4GB RAM, có nên gộp vào VPS hiện tại không?"
→ Cần data: VPS hiện tại đang dùng bao nhiêu RAM cho Hermes/OpenClaw/Antigravity trước
đã → nếu VPS hiện tại còn dư <4GB sau peak, khuyến nghị tách riêng (đúng như note đã
ghi trong kho: "Chatwoot cần VPS riêng ~4GB RAM") để tránh cả 2 dịch vụ cùng OOM khi
peak trùng nhau.

## Lưu ý / Lỗi thường gặp
- Đừng khuyến nghị downsize chỉ dựa trên usage trung bình — phải nhìn cả peak, tránh
  cắt đúng lúc cần nhiều resource nhất (VD: batch xử lý nhiều repo cùng lúc).
- Đừng bịa số giá Tencent Cloud nếu không tra được — nói rõ cần Nobitano/Antigravity
  check giá thật trên console.

## Đánh giá cá nhân
- Điểm mạnh: buộc có data thật trước khi đề xuất tốn tiền thêm hoặc downsize rủi ro.
- Điểm yếu: không tự lấy được data (agent không SSH) — phụ thuộc hoàn toàn vào
  Antigravity cung cấp log, nếu log thiếu thì khuyến nghị sẽ yếu.
- Có nên dùng không: 7/10 — hữu ích nhưng giá trị thực tế phụ thuộc chất lượng data
  đầu vào từ Antigravity.

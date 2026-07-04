---
name: gtm-strategy
description: >
  Xây go-to-market cho sản phẩm/dịch vụ mới hoặc mở rộng — chọn ICP, pricing tier, channel
  ưu tiên, và sequence launch. Dùng khi user hỏi "launch dịch vụ mới thì sao", "định giá
  gói mới cho SMB", "kênh nào ưu tiên trước khi launch", tối ưu cho thị trường SMB Việt Nam.
---

# GTM Strategy (SMB Việt Nam)

## TL;DR
Xây go-to-market gọn cho SMB VN — không cần plan 50 trang, cần: ICP rõ, pricing hợp lý,
1-2 channel ưu tiên làm trước, và sequence launch theo tuần.

## Khi nào dùng
- Launch dịch vụ/sản phẩm mới (VD: Tano Agency ra gói AI automation mới cho SMB)
- Mở rộng ABTRIP/Wonder Mart sang phân khúc khách hàng mới
- Cần định giá gói dịch vụ mới, chưa có benchmark rõ

## Quy trình

### 1. Chốt ICP (Ideal Customer Profile)
- Ai đau nhất với vấn đề này? Ngành gì, quy mô gì, budget bao nhiêu?
- Dùng `market-research` + `competitor-research` để kiểm tra ICP này có bị đối thủ
  chiếm chưa, và họ định giá sao.

### 2. Pricing tier
- Tối thiểu 2-3 tier (VD: Basic/Pro/Enterprise), tier giữa nên là tier khuyến nghị mặc định
  (decoy pricing — tier thấp/cao làm nền cho tier giữa hấp dẫn hơn).
- Dùng `finance-billing-ops` để đảm bảo tier thấp nhất vẫn có lời, không lỗ để "câu khách".

### 3. Channel ưu tiên
Với SMB VN, xếp hạng theo hiệu quả/công sức:
1. Referral từ khách hiện tại (rẻ nhất, tin cậy cao nhất)
2. Outbound trực tiếp có target rõ (dùng `outbound-engine` + `lead-dossier`)
3. Content/inbound (chậm hơn, nhưng bền — dùng skill content-strategy nếu cần)
4. Paid ads — CHỈ khi đã test được message/pricing ở channel 1-2 trước, tránh đốt tiền
   khi message chưa chuẩn.

### 4. Sequence launch (theo tuần, không cần chi tiết ngày)
```
Tuần 1: Soft launch cho 5-10 khách referral/thân quen — thu feedback thật
Tuần 2-3: Điều chỉnh pricing/message theo feedback
Tuần 4+: Mở outbound quy mô lớn hơn khi message đã chuẩn
```

### 5. Output khuyến nghị
```
ICP:              [ai, ngành, quy mô]
Pricing:          [2-3 tier, tier khuyến nghị]
Channel ưu tiên:  [1-2 channel làm trước, vì sao]
Rủi ro:           [điều gì có thể sai — VD: pricing quá thấp không đủ margin]
```

## Ví dụ thực tế
User: "Tano Agency muốn ra gói AI automation cho SMB VN, giá sao cho hợp?"
→ ICP: SMB 5-20 người, ngành dịch vụ/bán lẻ, chưa có ai làm automation nội bộ →
Pricing: Basic 3tr/tháng (1 automation), Pro 8tr/tháng (3 automation + support, khuyến
nghị), Enterprise custom → Channel: referral từ khách ABTRIP/Wonder Mart hiện tại trước,
outbound sau khi có 3-5 case study → Rủi ro: nếu Basic quá rẻ, không đủ margin cho support
thực tế, cần test kỹ chi phí support trước khi launch.

## Lưu ý / Lỗi thường gặp
- Đừng launch full channel ngay từ đầu — dễ đốt ngân sách khi message/pricing chưa chuẩn.
- Đừng định giá dựa cảm tính — luôn kiểm chi phí thật qua `finance-billing-ops`.
- SMB VN nhạy giá hơn thị trường US — benchmark giá quốc tế cần điều chỉnh xuống, không
  copy nguyên.

## Đánh giá cá nhân
- Điểm mạnh: gọn, đủ để launch nhanh, tránh over-planning cho SMB không có team lớn.
- Điểm yếu: không sâu cho enterprise sales (sales cycle dài, nhiều stakeholder) — cần
  skill khác nếu launch sang B2B lớn.
- Có nên dùng không: 8/10 — hợp với quy mô SMB VN mà Nobitano đang làm.

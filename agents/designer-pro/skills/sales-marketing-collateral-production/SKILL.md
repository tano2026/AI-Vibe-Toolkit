---
name: sales-marketing-collateral-production
description: >
  Tách từ "Skill lõi" mục 6-7 trong agents/company/roles/designer.md thành
  1 skill riêng — sản xuất vũ khí thị giác cho Sales (deck/one-pager/
  proposal/battlecard) và Marketing (ads variant/landing hero/template
  tái dùng). Dùng khi nhận brief từ Sales-CEO hoặc Digital Marketing Agent.
---

# Sales & Marketing Collateral Production

## TL;DR
Design để THẮNG, không design để treo. Deck đẹp mà không chốt được deal = fail. Ads đẹp mà CTR thấp = fail. Mỗi loại output có luật riêng, không phải "làm cho đẹp" chung chung.

## Khi nào dùng
- Sales-CEO cần vũ khí chốt deal (deck/one-pager/proposal/battlecard)
- Digital Marketing Agent cần creative cho campaign (ads variant/landing)
- Phát hiện 1 loại visual đã lặp lại ≥3 lần → cần đóng thành template

## Nội dung skill / prompt

### Cho Sales (đúng luật đã có trong designer.md)

```
Pitch deck:
  - 1 slide = 1 ý duy nhất
  - Số liệu to hơn chữ (data-first, không text-heavy)
  - Slide nào đọc >10 giây = slide hỏng, cắt/tách ra
  - Tối đa 12 slide cho pitch SMB (không quá dài)

One-pager dịch vụ:
  - Khách đọc 30 giây phải hiểu: làm gì – cho ai – proof – giá khung – bước tiếp
  - Không nhồi hết thông tin, chỉ đủ để khách quyết định bước tiếp theo

Proposal template:
  - Đóng khung sẵn, Sales CHỈ ĐIỀN — không design lại từ đầu mỗi deal
  - Đây là template dùng lại, không phải file mới mỗi lần

Battlecard visual:
  - So sánh Tano Agency vs Đối thủ cụ thể dạng bảng 1 trang
  - Sales mở ra dùng NGAY trong call — không cần giải thích thêm
```

### Cho Marketing (đúng luật đã có trong designer.md)

```
Ads variant theo ma trận test:
  - 3 hook × 2 format = 6 creative/đợt (đúng luật A/B test trong
    ad-budget-testing-discipline: 1 biến/lần, nhưng sản xuất đủ variant
    để test đồng loạt)
  - ĐẶT TÊN THEO BIẾN SỐ — để đọc report biết ngay cái nào thắng
    (vd: hook-pain_format-video, hook-social-proof_format-static)

Landing hero section:
  - Visual + vị trí CTA theo layout Marketing đã chốt (không tự đổi
    layout nếu Marketing chưa duyệt)

Hệ thống template tái dùng:
  - Loại visual lặp lại ≥3 LẦN → đóng thành template có vùng thay
    text/ảnh — lần sau sản xuất nhanh gấp 5, không design lại từ đầu
  - Template là TÀI SẢN CỦA AGENCY, lưu theo PACK — không phải file
    dùng 1 lần rồi bỏ
```

### Nguyên tắc chung cho cả 2 nhóm

Mọi output PHẢI qua design-quality-gate trước khi giao — skill này chỉ định hướng NỘI DUNG/CẤU TRÚC, không thay thế bước kiểm tra chất lượng cuối.

## Setup từng bước
1. Nhận brief từ Sales-CEO/Digital Marketing Agent — xác định đúng loại output (deck/one-pager/proposal/battlecard cho Sales; ads variant/landing/template cho Marketing)
2. Áp đúng luật riêng loại đó (không dùng chung 1 công thức cho mọi loại)
3. Nếu là loại visual đã lặp ≥3 lần — dừng lại, đóng thành template trước khi tiếp tục sản xuất tay
4. Chạy design-quality-gate trước khi giao

## Ví dụ thực tế
Sales-CEO cần battlecard so ABTRIP với đối thủ Fast Track (VISANA, Hong Ngọc Hà) — dựng bảng 1 trang, cột "Bundle 3-trong-1" là điểm khác biệt nổi bật nhất (đúng insight từ báo cáo thị trường trước đó), Sales mở ra dùng ngay khi khách hỏi "sao chọn ABTRIP mà không chọn chỗ khác".

## Lưu ý / Lỗi thường gặp
- Quên đặt tên ads variant theo biến số — khi có report về, không biết creative nào ứng với biến số nào, mất hết giá trị A/B test
- Không đóng template dù đã lặp lại nhiều lần — tốn công design lại từ đầu mỗi lần, đúng loại lãng phí "70% Primitives" trong mô hình FDE đã nhắc
- Proposal template để Sales tự sửa layout — sai, template chỉ để ĐIỀN, sửa layout phải qua Designer

## Đánh giá cá nhân
- Điểm mạnh: luật cụ thể theo từng loại output, không mơ hồ; nguyên tắc template hoá nối thẳng vào mô hình FDE (70% Primitives) đã xây
- Điểm yếu: cần Sales/Marketing brief đủ rõ (key message, đối tượng) — thiếu thì Designer phải hỏi lại, không tự chế
- Có nên dùng: 9/10 — đây là phần "vũ khí thị giác" thực chiến nhất của Designer, không phải design trang trí

## Link
- Nguồn gốc: agents/company/roles/designer.md (mục 6-7 Skill lõi)
- Dùng cùng: design-quality-gate (gate trước khi giao)

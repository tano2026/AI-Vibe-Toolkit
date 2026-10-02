---
name: zalo-channel-connection-guide
description: >
  3 cách kết nối Zalo qua OpenClaw (đã dùng sẵn, không cần tự xây) —
  zalouser (cá nhân, rủi ro khoá nick), zaloclawbot (trợ lý cá nhân,
  API chính thức, AN TOÀN NHẤT cho dùng riêng), Zalo OA Developer
  (bắt buộc cho bot khách hàng thấy — ABTRIP/Tano Cafe/Wonder Mart).
  Khác agents/trum-san-bay (vận hành) — đây là lớp KẾT NỐI kỹ thuật.
---

# Zalo Channel Connection Guide

## TL;DR
Không cần tự code kết nối Zalo — OpenClaw đã có sẵn 3 plugin kênh chính thức, chỉ cần cài đúng loại theo đúng mục đích. Khác nhau hoàn toàn về rủi ro và phạm vi dùng.

## Khi nào dùng
- Quyết định cách kết nối Zalo cho bất kỳ mục đích nào (trợ lý cá nhân Nobitano hay bot khách hàng ABTRIP/Tano Cafe/Wonder Mart)
- Trước khi tự code bất cứ thứ gì liên quan Zalo — kiểm tra OpenClaw đã có sẵn chưa

## Nội dung skill / prompt

### 3 con đường — khác hẳn nhau về rủi ro và mục đích

```
1. zalouser (Zalo cá nhân) — plugin: @openclaw/zalouser
   Cơ chế: tự động hoá tài khoản Zalo CÁ NHÂN qua zca-js (không chính thức)
   Đăng nhập: quét QR bằng app Zalo di động
   ⚠️ CẢNH BÁO TỰ GHI TRONG DOCS OPENCLAW: "có thể khiến tài khoản bị
   đình chỉ hoặc cấm" — KHÔNG CHÍNH THỨC
   Giới hạn: text chia đoạn ~2000 ký tự (giới hạn client Zalo)
   Dùng khi: Zalo Bot API không khả dụng, chấp nhận rủi ro

2. zaloclawbot (Zalo ClawBot) — AN TOÀN NHẤT cho dùng cá nhân
   Plugin: cài qua trình hướng dẫn onboarding OpenClaw, chọn "Zalo ClawBot"
   Cơ chế: QR trỏ tới Zalo Mini App bảo mật, cấp 1 bot RIÊNG dưới 1 OA
   CHÍNH THỨC dùng chung, gắn trực tiếp với Zalo User ID của mày
   Đường API: Zalo Bot Platform API thật (long-polling) — KHÔNG phải
   browser automation, KHÔNG phải tự động hoá session
   KHÁC zalouser: không cần đăng ký OA riêng, không cần dán credential
   tĩnh — chỉ quét QR 1 lần
   Yêu cầu: OpenClaw server >= 2026.4.10
   Dùng khi: cần trợ lý cá nhân nhận/gửi tin Zalo cho Nobitano (đúng
   nhu cầu "Zalo Agent" đã bàn trước) — AN TOÀN, không rủi ro khoá nick

3. Zalo OA Developer (chuẩn doanh nghiệp) — BẮT BUỘC cho bot khách hàng
   Yêu cầu: đăng ký Zalo OA đã xác thực (tích vàng/cam) tại business.zalo.me
   Quy trình: developers.zalo.me → tạo App → liên kết OA → xin quyền
   API → lấy OA Access Token → đăng ký webhook
   Chi phí: gói Nâng cao (99K) hoặc Premium (399K)/tháng để mở Chatbot
   Thời gian duyệt: 3-7 ngày
   Dùng khi: ABTRIP/Tano Cafe/Wonder Mart cần bot KHÁCH HÀNG thấy và
   tương tác trực tiếp (không phải trợ lý riêng cho Nobitano)
```

### Bảng quyết định — chọn đúng con đường theo mục đích

| Mục đích | Chọn | Vì sao |
|---|---|---|
| Trợ lý cá nhân Nobitano (nhận tin, tạo ảnh/video, trả lời) | **zaloclawbot** | An toàn, API chính thức, không cần đăng ký OA riêng |
| Bot khách hàng ABTRIP/Tano Cafe/Wonder Mart thấy | **Zalo OA Developer** | Bắt buộc OA thật để khách hàng tương tác chính danh |
| Zalo Bot API chính thức không đủ tính năng cần | zalouser (chấp nhận rủi ro) | Chỉ khi thật sự không còn lựa chọn khác |

## Setup từng bước (zaloclawbot — khuyến nghị bắt đầu)
1. Chạy trình hướng dẫn onboarding OpenClaw, chọn "Zalo ClawBot" từ menu kênh
2. Xác nhận OpenClaw server đã >= 2026.4.10
3. Quét mã QR hiện ra trong terminal bằng app Zalo di động
4. Hoàn tất — bot đã gắn trực tiếp Zalo User ID, giao tiếp qua long-polling API chính thức

## Ví dụ thực tế
Đúng nhu cầu "Zalo Agent" đã bàn trước (infographic tin nhắn → file/ảnh/video) — setup bằng `zaloclawbot` thay vì tự xây từ đầu hay dùng `zalouser` rủi ro. OpenClaw đã có sẵn toàn bộ tầng nhận/gửi tin, chỉ cần nối vào 8 Pro Agent đã xây (task-intake-quality-gate route task, Media Pro tạo nội dung...).

## Lưu ý / Lỗi thường gặp
- Dùng `zalouser` cho việc không cần thiết — rủi ro khoá nick thật, tự OpenClaw cảnh báo rõ, không phải tao tự suy đoán
- Nhầm `zaloclawbot` (cá nhân, không cần OA riêng) với luồng OA Developer chuẩn (cần đăng ký OA riêng, trả phí) — 2 cái phục vụ mục đích khác hẳn
- Build bot khách hàng (ABTRIP/Tano Cafe) bằng `zaloclawbot` — SAI, đây chỉ dành cho 1 user cá nhân (Nobitano), không phải bot công khai cho nhiều khách

## Đánh giá cá nhân
- Điểm mạnh: KHÔNG CẦN TỰ XÂY — OpenClaw (đã dùng sẵn) có đủ 3 lựa chọn chính thức; `zaloclawbot` giải đúng nhu cầu trợ lý cá nhân mà không cần đăng ký OA riêng rườm rà
- Điểm yếu: `zaloclawbot` còn gắn nhãn "Beta", cần OpenClaw server bản mới; luồng OA Developer chuẩn tốn thời gian duyệt (3-7 ngày) + phí hàng tháng
- Có nên dùng: 9/10 cho `zaloclawbot` (trợ lý cá nhân) — đáng cài ngay; Zalo OA Developer cần khi thật sự làm bot khách hàng, không vội

## Link
- Docs zalouser: docs.openclaw.ai/vi/channels/zalouser
- Docs zaloclawbot: docs.openclaw.ai/vi/channels/zaloclawbot
- Zalo OA Developer: developers.zalo.me, business.zalo.me
- Dùng cùng: skills/zalo-oa-du-lich-luu-tru-playbook (vận hành OA sau khi đã kết nối)

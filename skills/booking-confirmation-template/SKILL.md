---
name: booking-confirmation-template
description: Template tin nhắn kết quả đặt vé cho ABTRIP, Telegram format
---

# Booking Confirmation Template

Khi trả kết quả đặt vé thành công cho user, dùng format sau:

━━━━━━

**✅ ĐẶT VÉ THÀNH CÔNG**

✈️ **{origin} → {destination}** | {date}
🕐 {departure} → {arrival} — **{airline} {flight}**

━━━━━━

**👥 Hành khách:**
• {name1}
• {name2}
• {name3}
• {name4}

━━━━━━

||Mã đặt chỗ:|| `{booking_code}`
||Mã đơn hàng:|| `{order_code}`
||Tổng tiền:|| **{price}₫**

⏳ **Hết hạn:** {time} — {date}

━━━━━━

## Quy tắc
- Dùng `━━━━━━` (7 ký tự gạch ngang) làm separator
- Không dùng box/table — Telegram ko hỗ trợ
- Mỗi hành khách 1 dấu •
- Họ tên viết HOA toàn bộ
- Tổng tiền in đậm
- Mã đặt chỗ và mã đơn hàng dùng inline code ``
- Không giải thích Họ/Tên riêng từng người

## Error message style (Nobitano preference)

Khi booking thất bại, KHÔNG dùng văn phong bot như:

> "Rất tiếc, hệ thống đặt vé của bên mình hiện đang gặp lỗi kỹ thuật tạm thời, không thể hoàn tất đặt chỗ cho bạn lúc này..."

Thay vào đó, dùng:

> Hệ thống đặt vé đang lỗi tạm thời. Thử lại sau nhé.
> 
> Hoặc đặt chuyến khác: [VJ327 14:50 - 856,720₫]

**Ngắn gọn, không cảm thán, không xin lỗi dài dòng.**

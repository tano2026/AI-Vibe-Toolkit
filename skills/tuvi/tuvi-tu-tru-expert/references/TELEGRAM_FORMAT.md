# Telegram Output Format — Tử Bình & Tử Vi

> Quy tắc trình bày kết quả Tử Bình / Tử Vi trên Telegram.
> Áp dụng cho mọi output dạng luận giải lá số, vận hạn, tư vấn.

## Nguyên tắc cốt lõi

1. **Chia nhỏ** — Gửi nhiều tin nhắn ngắn thay vì 1 tin siêu dài
2. **Scan được** — Người dùng lướt 2 giây là thấy điểm chính
3. **Emoji = chức năng** — Mỗi emoji mang 1 ý nghĩa nhất quán, dùng xuyên suốt
4. **Bold cho keyword** — Chỉ bold cái quan trọng (tên sao, con số, kết luận)
5. **Separator `━━━`** — Tạo visual break giữa các section
6. **Spoiler `||...||`** — Cho chi tiết phụ, ai muốn xem thì tap
7. **Không dùng bảng** — Telegram không có table syntax
8. **Không code block dài** — Gây scroll ngang trên mobile

## Emoji quy ước

| Emoji | Ý nghĩa | Dùng cho |
|-------|---------|----------|
| 📜 | Tử Bình / Tứ Trụ | Header message |
| 🏛️ | Tử Vi Đẩu Số | Header message |
| 🎯 | Hành động / Lời khuyên | Hành động khuyến nghị |
| ✅ | Nên | Màu/hướng/vật phẩm tốt |
| ❌ | Tránh | Màu/hướng/vật phẩm xấu |
| ⚠️ | Cảnh báo | Rủi ro, cẩn thận |
| 📌 | Kết luận chính | Tóm tắt 1 câu |
| 🔄 | Đại hạn / Vận hạn | Vận trình |
| 💡 | Lưu ý thông minh | Góc nhìn sâu hơn |
| ⚡ | Mệnh | Cung Mệnh |
| 💰 | Tài Bạch | Cung Tài |
| 🏢 | Quan Lộc | Cung Quan |
| ❤️ | Phu Thê / Tình duyên | Cung Phối |
| 👨‍👩‍👧‍👦 | Gia đạo | Phụ Mẫu, Huynh Đệ, Tử Tức |
| 🌐 | Di Chuyển | Cung Thiên Di |
| 👥 | Bạn bè / Đối tác | Cung Nô Bộc |
| 🏠 | Nhà cửa | Cung Điền Trạch |
| 🩺 | Sức khỏe | Cung Tật Ách |
| 🟢 | Dụng Thần | Dụng Thần tốt cho mệnh |
| 🟡 | Hỷ Thần | Hỗ trợ Dụng Thần |
| 🔴 | Kỵ Thần | Tránh |

## Cấu trúc tin nhắn (3-4 tin)

### Tin 1: TỨ TRỤ (Tử Bình)

```
📜 TỨ TRỤ [tên]
━━━━━━━━━━━━━━━━
Giáp Tý · Kỷ Tỵ · Ất Mùi · Tân Tỵ
Mộc · Thổ · Mộc · Kim | [Cục]

Dụng **Thủy** 🟢 | Hỷ Kim 🟡 | Kỵ Hỏa 🔴 · Thổ 🔴
━━━━━━━━━━━━━━━━
📌 Ất Mộc yếu, mùa Hạ khô → cần nước tưới
```

### Tin 2: TỬ VI (tóm tắt)

```
🏛️ TỬ VI · Mệnh [Tên] · Thân [Tên]
━━━━━━━━━━━━━━━━
⚡ Mệnh: [Sao chính] [Miếu/Vượng] + [sao phụ]
💰 Tài: [Sao chính] ||[chi tiết]||
🏢 Quan: [Sao chính] + [sao phụ]
❤️ Phu Thê: [Sao chính] [Hóa] + [sao]
━━━━━━━━━━━━━━━━
📌 [kết luận 1 câu]
```

### Tin 3: VẬN HẠNH

```
🔄 ĐẠI HẠN [tuổi] — [tên cung]
━━━━━━━━━━━━━━━━
Chính tinh: [sao] [vị thế]
Ảnh hưởng: ||giải thích ngắn||

📅 Năm [năm]: [sao lưu niên]
⚠️ [cảnh báo nếu có]
```

### Tin 4: HÀNH ĐỘNG

```
🎯 HÀNH ĐỘNG
━━━━━━━━━━━━━━━━
✅ Nên: [màu/hướng/vật phẩm]
✅ Hợp: [tuổi/người]
❌ Tránh: [điều cấm kỵ]
━━━━━━━━━━━━━━━━
📌 [lời khuyên ngắn gọn]
⚠️ [lưu ý đặc biệt nếu có]
```

## Quy tắc viết

1. **1 tin = 1 chủ đề** — Không trộn Tử Bình + Tử Vi + Hành động vào 1 tin
2. **Câu ngắn, xuống dòng nhiều** — Tối đa 1-2 dòng/đoạn
3. **Spoiler cho giải thích dài** — `||phân tích chi tiết hơn ở đây||`
4. **Bold chỉ cho:**
   - Tên sao chính (Thiên Cơ, Tham Lang...)
   - Kết luận (Thân Nhược, Dụng Thần)
   - Con số, tuổi, năm
   - Điểm cần nhấn mạnh
5. **Không giải thích dài dòng** — Nếu cần giải thích, dùng spoiler hoặc tin riêng
6. **Luôn kết thúc = hành động** — Mỗi lá số phải để lại 1-3 điều người dùng CÓ THỂ LÀM

## Trình tự gửi

1. Gửi tin 📜 TỨ TRỤ trước (ngắn nhất)
2. Gửi tin 🏛️ TỬ VI (tóm tắt 12 cung)
3. Gửi tin 🔄 VẬN HẠNH (nếu có hỏi)
4. Gửi tin 🎯 HÀNH ĐỘNG (kết thúc)

> Không gộp. Không gửi 1 tin dài. Không dùng bảng.

## So sánh: Cũ → Mới

| Tiêu chí | Cách cũ | Cách mới |
|----------|---------|----------|
| Số tin | 1 tin siêu dài | 3-4 tin ngắn |
| Thời gian đọc | 3-5 phút | 30-60 giây |
| Scan được | Không | Có |
| Mobile-friendly | Kém (scroll dài) | Tốt (từng phần) |
| Chi tiết | Trộn lẫn | Phân cấp rõ |
| Kết luận | Ở giữa | Luôn cuối cùng |

## Ví dụ

### ❌ Cách cũ (dài, khó đọc)

```
📜 PHÂN TÍCH TỬ BÌNH CHI TIẾT
Tứ trụ: Giáp Tý - Kỷ Tỵ - Ất Mùi - Tân Tỵ
Phân tích: Ất mộc sinh tháng tỵ là mùa hạ, hỏa vượng mộc hưu tù, mộc yếu...
...còn nhiều dòng nữa...
```

### ✅ Cách mới (gọn, đẹp)

```
📜 TỨ TRỤ
━━━━━━━━━━━━━━━━
Giáp Tý · Kỷ Tỵ · Ất Mùi · Tân Tỵ
Mộc · Thổ · Mộc · Kim | Thủy Nhị Cục

Dụng **Thủy** 🟢 | Hỷ Kim 🟡 | Kỵ Hỏa·Thổ 🔴
━━━━━━━━━━━━━━━━
📌 Ất Mộc yếu mùa Hạ → cần nước
```

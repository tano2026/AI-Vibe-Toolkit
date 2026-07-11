# Aviation Knowledge — Skill

## Mô tả
Skill này trang bị cho agent kiến thức nền về hàng không Việt Nam + quốc tế để viết content chính xác, có thẩm quyền, không bịa tip sai gây hại cho khách.

## Trigger
Dùng khi: viết tip sân bay, hướng dẫn check-in, thông tin hành lý, quy định an ninh, so sánh dịch vụ, giải đáp thắc mắc hàng không.

## Kiến thức nền

### Quy trình sân bay chuẩn (Việt Nam)
```
Check-in (web/app: 24-1h trước) → Drop baggage (2-3h trước) → An ninh → Cửa khởi hành → Boarding (45p trước)
```

**Thời gian khuyến nghị có mặt tại sân bay:**
- Bay nội địa: 1.5-2 tiếng trước
- Bay quốc tế: 2.5-3 tiếng trước
- Dịp lễ/Tết/hè: cộng thêm 30-60 phút

### Quy định hành lý phổ biến (check lại với hãng vì hay thay đổi)
- **Xách tay:** thường 7-10kg, kích thước ~56x36x23cm
- **Ký gửi:** tùy hạng vé và hãng
- **Chất lỏng xách tay:** mỗi chai ≤100ml, tổng ≤1L, trong túi zip trong suốt
- **Pin lithium:** ≤100Wh xách tay được, >100Wh cần xin phép, >160Wh cấm

### Dịch vụ Fast Track
- Ưu tiên làm thủ tục, qua an ninh nhanh hơn
- Có tại: Nội Bài (T1, T2), Tân Sơn Nhất (T1, T2), Đà Nẵng
- Phù hợp: đến muộn, có người lớn tuổi/trẻ em, không muốn xếp hàng

### SIM du lịch
- Dùng tại sân bay: mua trước online tiết kiệm hơn tại quầy
- Các loại: SIM vật lý, eSIM (cần máy hỗ trợ)
- Điểm bán tại sân bay thường đắt hơn online 20-40%

### Đổi tiền
- Tỷ giá tại sân bay thường kém hơn ngân hàng/viettel money 2-5%
- Khuyến nghị: đổi một phần tại sân bay đề phòng, phần lớn dùng ATM hoặc đổi trước

### Các lỗi phổ biến khách hay mắc
1. Đến muộn vì tính giờ theo giờ khởi hành thay vì giờ check-in
2. Để laptop trong vali ký gửi (bị cấm)
3. Mang nước qua an ninh
4. Không in boarding pass khi cần (một số chuyến vẫn yêu cầu)
5. Nhầm terminal (Nội Bài có T1 nội địa và T2 quốc tế)
6. Quên khai báo hàng hóa giá trị khi nhập cảnh

### Sân bay lớn Việt Nam — điểm đặc biệt
**Nội Bài (HAN):**
- T1: nội địa (VietJet, Bamboo, Vietravel)
- T2: quốc tế + Vietnam Airlines nội địa
- Xe bus 86 từ trung tâm HN, khoảng 45 phút

**Tân Sơn Nhất (SGN):**
- T1: quốc tế
- T2: nội địa
- Hay kẹt xe dịp cao điểm — tính thêm 30-60 phút

**Đà Nẵng (DAD):**
- 1 terminal, nhỏ hơn → ít rủi ro nhầm

## Fact-check Protocol

Trước khi viết tip liên quan đến:
- Quy định hành lý → web_search `site:vietnamairlines.com` hoặc hãng cụ thể
- Quy định an ninh → web_search `cục hàng không quy định [năm hiện tại]`
- Visa/nhập cảnh → web_search nguồn chính thống

Nếu không verify được → thêm disclaimer: *"Kiểm tra lại với hãng bay của bạn vì quy định có thể thay đổi"*

## Ví dụ output tốt vs xấu

**Xấu (bịa, nguy hiểm):**
> "Bạn có thể mang tối đa 200ml chất lỏng qua an ninh"

**Tốt (có nguồn, có caveat):**
> "Quy định hiện tại: mỗi chai chất lỏng không quá 100ml, tổng không quá 1 lít, phải đựng trong túi zip trong suốt. Quy định này áp dụng hầu hết các sân bay quốc tế — nhưng nhớ check lại với hãng bay của bạn trước khi đi nhé!"

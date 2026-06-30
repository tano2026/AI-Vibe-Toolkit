# AN SAO TỬ VI — THUẬT TOÁN ĐẦY ĐỦ

## 1. CHUẨN BỊ — XÁC ĐỊNH CAN CHI NĂM SINH

### Can năm (0–9)
| Số dư (năm % 10) | 4 | 5 | 6 | 7 | 8 | 9 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|---|---|---|
| Thiên Can | Giáp | Ất | Bính | Đinh | Mậu | Kỷ | Canh | Tân | Nhâm | Quý |
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

Ví dụ: 1984 → 1984%10=4 → **Giáp** (index 0)

### Chi năm (0–11)
| Số dư (năm % 12) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Địa Chi | Thân | Dậu | Tuất | Hợi | Tý | Sửu | Dần | Mão | Thìn | Tỵ | Ngọ | Mùi |

Năm 2024 = Giáp Thìn (can 0, chi 8). Dùng năm 2024 làm mốc:
**Chi = (8 + (năm - 2024)) % 12**

---

## 2. XÁC ĐỊNH CỤC

Cục dựa trên **Nạp âm Can Chi năm sinh**:

| Can Chi năm | Cục | Can Chi năm | Cục |
|-------------|-----|-------------|-----|
| Giáp Tý, Ất Sửu | Kim Tứ (4) | Bính Dần, Đinh Mão | Hỏa Lục (6) |
| Mậu Thìn, Kỷ Tỵ | Mộc Tam (3) | Canh Ngọ, Tân Mùi | Thổ Ngũ (5) |
| Nhâm Thân, Quý Dậu | Kim Tứ (4) | Giáp Tuất, Ất Hợi | Hỏa Lục (6) |
| Bính Tý, Đinh Sửu | Thủy Nhị (2) | Mậu Dần, Kỷ Mão | Thổ Ngũ (5) |
| Canh Thìn, Tân Tỵ | Kim Tứ (4) | Nhâm Ngọ, Quý Mùi | Mộc Tam (3) |
| Giáp Thân, Ất Dậu | Thủy Nhị (2) | Bính Tuất, Đinh Hợi | Thổ Ngũ (5) |
| Mậu Tý, Kỷ Sửu | Hỏa Lục (6) | Canh Dần, Tân Mão | Mộc Tam (3) |
| Nhâm Thìn, Quý Tỵ | Thủy Nhị (2) | Giáp Ngọ, Ất Mùi | Kim Tứ (4) |
| Bính Thân, Đinh Dậu | Thổ Ngũ (5) | Mậu Tuất, Kỷ Hợi | Thủy Nhị (2) |
| Canh Tý, Tân Sửu | Thổ Ngũ (5) | Nhâm Dần, Quý Mão | Kim Tứ (4) |
| Giáp Thìn, Ất Tỵ | Hỏa Lục (6) | Bính Ngọ, Đinh Mùi | Thủy Nhị (2) |
| Mậu Thân, Kỷ Dậu | Mộc Tam (3) | Canh Tuất, Tân Hợi | Kim Tứ (4) |
| Nhâm Tý, Quý Sửu | Mộc Tam (3) | Giáp Dần, Ất Mão | Thủy Nhị (2) |
| Bính Thìn, Đinh Tỵ | Thổ Ngũ (5) | Mậu Ngọ, Kỷ Mùi | Thủy Nhị (2) |
| Canh Thân, Tân Dậu | Mộc Tam (3) | Nhâm Tuất, Quý Hợi | Mộc Tam (3) |

**Ví dụ:** Giáp Tý (1984) → **Kim Tứ Cục (4)**

---

## 3. AN CUNG MỆNH VÀ CUNG THÂN

### Cung Mệnh
Khởi từ cung Dần = tháng 1, đếm **thuận** đến tháng sinh âm lịch.

```
Cung Mệnh (địa chi) = (Dần_index + tháng_âm_lịch - 1) % 12
Dần = index 2
```

### Cung Thân
Khởi từ cung Dần = tháng 1, đếm thuận đến tháng sinh, rồi đếm thêm theo giờ sinh.

```
Cung Thân = (Dần_index + tháng_âm_lịch - 1 + giờ_index) % 12
```

**Bảng giờ → index:**
Tý=0, Sửu=1, Dần=2, Mão=3, Thìn=4, Tỵ=5, Ngọ=6, Mùi=7, Thân=8, Dậu=9, Tuất=10, Hợi=11

**Ví dụ:** Tháng 3 âm lịch, giờ Tỵ (5):
- Mệnh = (2+3-1)%12 = 4 = **Thìn** → sai, cần dùng tháng âm lịch thực tế
- Ngày 01/05/1984 DL ≈ tháng 3 AL → Mệnh = (2+3-1)%12 = 4 = **Thìn**... 
- Thực tế lá số Giáp Tý tháng 3 AL giờ Tỵ: Mệnh tại **Mùi** (cần tra bảng chuẩn)

> **LƯU Ý QUAN TRỌNG:** Cần chuyển đổi dương lịch → âm lịch chính xác trước khi tính. Sai âm lịch = sai toàn bộ lá số. Hỏi người dùng ngày âm lịch nếu họ biết.

---

## 4. AN TỬ VI

```
Tìm a (0 đến cục-1) sao cho: (ngày_âm_lịch + a) chia hết cho số_cục
b = (ngày_âm_lịch + a) / số_cục

Khởi từ Dần (index 2), đếm thuận b lần → vị trí tạm
  - Nếu a = 0: Tử Vi ở vị trí đó
  - Nếu a lẻ (1,3,5): lùi a cung
  - Nếu a chẵn (2,4): tiến a cung
```

**Tử Vi KHÔNG đóng tại:** Thìn, Tuất, Sửu, Mùi (Tứ Mộ)

**Ví dụ:** Ngày 1 âm lịch, Hỏa Lục Cục (6):
- a=5 vì (1+5)=6 chia hết cho 6 → b=1
- Dần=index 2, đếm 1 lần → vẫn Dần
- a=5 (lẻ) → lùi 5 cung: Dần(2) → Sửu(1) → Tý(0) → Hợi(11) → Tuất(10) → Dậu(9)
- **Tử Vi tại Dậu (index 9)**... 

> Kiểm tra: nếu kết quả rơi vào Thìn/Tuất/Sửu/Mùi → tính lại a tiếp theo

---

## 5. AN 14 CHÍNH TINH

### Vòng Tử Vi (đi NGHỊCH từ vị trí Tử Vi)
```
Tử Vi      → pos
Thiên Cơ   → pos - 1
(bỏ 1 ô)
Thái Dương → pos - 3
Vũ Khúc    → pos - 4
Thiên Đồng → pos - 5
(bỏ 2 ô)
Liêm Trinh → pos - 8
```
(Tất cả mod 12, +12 nếu âm)

### Vòng Thiên Phủ (đi THUẬN)
Thiên Phủ = (14 - pos_TuVi) % 12

```
Thiên Phủ  → phu
Thái Âm    → phu + 1
Tham Lang  → phu + 2
Cự Môn     → phu + 3
Thiên Tướng→ phu + 4
Thiên Lương→ phu + 5
Thất Sát   → phu + 6
(bỏ 2 ô)
Phá Quân   → phu + 9
```

---

## 6. AN SAO PHỤ QUAN TRỌNG

### Lộc Tồn, Kình Dương, Đà La (theo CAN NĂM)
| Can | Lộc Tồn | Kình Dương | Đà La |
|-----|---------|-----------|-------|
| Giáp | Dần (2) | Mão (3) | Sửu (1) |
| Ất | Mão (3) | Thìn (4) | Dần (2) |
| Bính/Mậu | Tỵ (5) | Ngọ (6) | Thìn (4) |
| Đinh/Kỷ | Ngọ (6) | Mùi (7) | Tỵ (5) |
| Canh | Thân (8) | Dậu (9) | Mùi (7) |
| Tân | Dậu (9) | Tuất (10) | Thân (8) |
| Nhâm | Hợi (11) | Tý (0) | Tuất (10) |
| Quý | Tý (0) | Sửu (1) | Hợi (11) |

### Thiên Khôi, Thiên Việt (theo CAN NĂM)
| Can | Thiên Khôi | Thiên Việt |
|-----|-----------|-----------|
| Giáp, Mậu | Sửu (1) | Mùi (7) |
| Ất, Kỷ | Tý (0) | Thân (8) |
| Bính, Đinh | Hợi (11) | Dậu (9) |
| Canh, Tân | Ngọ (6) | Dần (2) |
| Nhâm, Quý | Mão (3) | Tỵ (5) |

### Văn Xương, Văn Khúc (theo GIỜ SINH)
```
Văn Xương: khởi Tuất(10) giờ Tý, đếm NGHỊCH
  → pos = (10 - giờ_index + 12) % 12

Văn Khúc: khởi Thìn(4) giờ Tý, đếm THUẬN
  → pos = (4 + giờ_index) % 12
```

### Tả Phù, Hữu Bật (theo THÁNG ÂM LỊCH)
```
Tả Phù: khởi Thìn(4) tháng 1, đếm THUẬN
  → pos = (4 + tháng - 1) % 12

Hữu Bật: khởi Tuất(10) tháng 1, đếm NGHỊCH
  → pos = (10 - tháng + 1 + 12) % 12
```

### Thiên Mã (theo CHI NĂM)
| Chi năm | Thiên Mã |
|---------|---------|
| Dần, Ngọ, Tuất | Thân (8) |
| Thân, Tý, Thìn | Dần (2) |
| Tỵ, Dậu, Sửu | Hợi (11) |
| Hợi, Mão, Mùi | Tỵ (5) |

### Hỏa Tinh, Linh Tinh (theo CHI NĂM + GIỜ SINH)
**Hỏa Tinh:**
| Chi năm (nhóm) | Khởi tháng Tý | Hướng |
|---|---|---|
| Dần/Ngọ/Tuất | Sửu (1) | Thuận |
| Thân/Tý/Thìn | Dần (2) | Thuận |
| Tỵ/Dậu/Sửu | Mão (3) | Thuận |
| Hợi/Mão/Mùi | Dậu (9) | Thuận |

`Hỏa Tinh = (khởi + giờ_index) % 12`

**Linh Tinh:**
| Chi năm (nhóm) | Khởi giờ Tý | Hướng |
|---|---|---|
| Dần/Ngọ/Tuất | Tuất (10) | Thuận |
| Thân/Tý/Thìn | Tuất (10) | Thuận |
| Tỵ/Dậu/Sửu | Tuất (10) | Thuận |
| Hợi/Mão/Mùi | Tuất (10) | Thuận |

`Linh Tinh = (10 + giờ_index) % 12`

> Lưu ý: Có nhiều trường phái khác nhau về Hỏa/Linh. Trên đây là cách phổ biến nhất.

### Địa Không, Địa Kiếp (theo GIỜ SINH)
```
Địa Không: khởi Hợi(11) giờ Tý, đếm NGHỊCH
  → pos = (11 - giờ_index + 12) % 12

Địa Kiếp: khởi Hợi(11) giờ Tý, đếm THUẬN
  → pos = (11 + giờ_index) % 12
```

---

## 7. TỨ HÓA — ĐẶT VÀO LÁ SỐ

Sau khi biết vị trí của sao → tìm cung chứa sao → đặt ký hiệu Hóa vào cung đó.

| Can năm | Hóa Lộc | Hóa Quyền | Hóa Khoa | Hóa Kỵ |
|---------|---------|----------|---------|--------|
| Giáp | Liêm Trinh | Phá Quân | Vũ Khúc | Thái Dương |
| Ất | Thiên Cơ | Thiên Lương | Tử Vi | Thái Âm |
| Bính | Thiên Đồng | Thiên Cơ | Văn Xương | Liêm Trinh |
| Đinh | Thái Âm | Thiên Đồng | Thiên Cơ | Cự Môn |
| Mậu | Tham Lang | Thái Âm | Hữu Bật | Thiên Cơ |
| Kỷ | Vũ Khúc | Tham Lang | Thiên Lương | Văn Khúc |
| Canh | Thái Dương | Vũ Khúc | Thái Âm | Thiên Đồng |
| Tân | Cự Môn | Thái Dương | Văn Khúc | Văn Xương |
| Nhâm | Thiên Lương | Tử Vi | Tả Phù | Vũ Khúc |
| Quý | Phá Quân | Cự Môn | Thái Âm | Tham Lang |

---

## 8. MIẾU - VƯỢNG - ĐẮC - BÌNH - HÃM (Một số sao chính)

| Sao | Miếu/Vượng | Đắc | Hãm |
|-----|-----------|-----|-----|
| Tử Vi | Ngọ, Dần, Thân | Tý, Thìn, Tuất, Sửu, Mùi | Mão, Dậu, Tỵ, Hợi |
| Thiên Cơ | Mão, Dậu | Tý, Ngọ, Thìn, Tuất | Dần, Thân, Tỵ, Hợi |
| Thái Dương | Dần→Ngọ (sáng) | Mùi, Thân | Tuất→Sửu (tối) |
| Vũ Khúc | Sửu, Mùi, Tỵ, Hợi | Thìn, Tuất | Dần, Mão, Thân, Dậu |
| Thiên Đồng | Tý, Dần, Ngọ, Thân | Thìn, Tuất, Sửu, Mùi | Mão, Dậu, Tỵ, Hợi |
| Liêm Trinh | Thân, Dần | Ngọ, Tý | Tỵ, Hợi, Mão, Dậu |
| Thiên Phủ | Ngọ, Dần, Thân | Tý, Thìn, Tuất | Mão, Dậu, Tỵ, Hợi |
| Thái Âm | Hợi, Sửu | Tý, Mùi | Ngọ, Mão, Dậu |
| Tham Lang | Sửu, Mùi (Miếu) | Dần, Thân | Tỵ, Hợi, Tý, Ngọ, Mão, Dậu |
| Cự Môn | Dần, Thân | Tý, Ngọ | Tỵ, Hợi, Sửu, Mùi |
| Thiên Tướng | Dần, Thân | Tý, Ngọ | Tỵ, Hợi |
| Thiên Lương | Ngọ, Dần, Thân | Tý, Thìn, Tuất | Mão, Dậu |
| Thất Sát | Dần, Thân, Tý, Ngọ | Thìn, Tuất, Sửu, Mùi | Mão, Dậu, Tỵ, Hợi |
| Phá Quân | Tý, Ngọ, Thìn, Tuất | Sửu, Mùi | Dần, Thân, Mão, Dậu |

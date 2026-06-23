---
name: market-sizing
description: >
  Tính quy mô thị trường (TAM/SAM/SOM) bằng top-down và bottom-up approach.
  Dùng Fermi estimation khi thiếu data chính thức. Crosscheck kết quả.
  Trigger với: "quy mô thị trường", "market size", "TAM SAM SOM", "thị trường này bao lớn",
  "ước tính thị trường", "market sizing", "addressable market".
---

# Market Sizing — TAM / SAM / SOM

---

## Hai approach, luôn chạy cả 2

### Top-Down (từ tổng thể thu hẹp xuống)
```
Bắt đầu từ số liệu ngành tổng → apply filters để thu về segment mày muốn

Ví dụ: Thị trường SaaS HR cho SME ở Việt Nam
  Global HR Tech market: $40B (Gartner 2024)
  × SEA share: ~3% = $1.2B
  × Vietnam share trong SEA GDP: ~18% = $216M
  × SME segment (không phải enterprise): ~40% = $86M
  × SaaS specifically (vs on-prem, Excel): ~35% = $30M

  → TAM = ~$30M/năm (Vietnam SME HR SaaS)
```

### Bottom-Up (từ đơn vị nhỏ nhất xây lên)
```
Đếm potential customers → nhân với ARPU

Ví dụ cùng market trên:
  SME ở VN có HR pain (>20 nhân viên, <500 nhân viên): ~150,000 công ty
  × Tỷ lệ sẵn sàng trả tiền cho SaaS (dựa trên SaaS adoption rate VN ~15%): 22,500
  × ARPU estimate ($30-50/tháng, benchmark từ competitors): $480/năm
  = $10.8M (conservative) đến $18M (optimistic)

  → TAM bottom-up: $10-18M/năm
```

### Crosscheck
```
Top-down: $30M
Bottom-up: $10-18M

Chênh ~2x → bình thường cho market sizing (top-down thường overestimate)
Con số reasonable range: $10-30M, mid-point ~$15-20M
```

---

## TAM / SAM / SOM

```
TAM (Total Addressable Market): Nếu 1 công ty chiếm hết thị trường — tối đa có thể đạt
SAM (Serviceable Addressable Market): Phần thực sự có thể serve được (tech, geo, segment)
SOM (Serviceable Obtainable Market): Realistic share trong 1-3 năm đầu

Ví dụ:
  TAM: $20M (toàn bộ SME HR SaaS VN)
  SAM: $8M (chỉ TP.HCM + Hà Nội, segment tech/startup-friendly)
  SOM: $800K (5-10% SAM trong năm đầu — con số pitch được với investor)
```

---

## Fermi estimation khi không có data

```
Dùng khi: không tìm được số ngành chính thức

Steps:
1. Break problem xuống các components có thể estimate được
2. Estimate từng component từ proxy data (dân số, GDP per capita, tỷ lệ adoption tương tự)
3. Multiply + sanity check

Ví dụ: Thị trường giao đồ ăn online Hà Nội
  Dân số Hà Nội: ~8M người
  × Tỷ lệ có smartphone và đã đặt đồ ăn online ít nhất 1 lần: ~30% = 2.4M người
  × Tỷ lệ order hàng tuần: ~40% của 2.4M = 960K người
  × Tần suất trung bình: 2 lần/tuần
  × AOV (average order value): 80,000 VND
  = 960K × 2 × 80K × 52 = ~$640M/năm

  Sanity check: GrubHub US (200M dân) ~$1.8B → VN (96M dân) nên nhỏ hơn nhiều
  Nhưng Hà Nội là core city, adoption cao hơn average → $600-700M range có vẻ hợp lý
```

---

## Output format

```
Luôn present market size như sau:

"Thị trường [X] tại [Geography] ước tính đạt [RANGE] vào năm [YEAR].

Approach:
- Top-down (từ số ngành $Z, apply rate X%, Y%): ~$A
- Bottom-up (N customers × $B ARPU): ~$C

Conservative estimate: $D | Optimistic: $E | Best guess: $F

Confidence: [Cao/Trung bình/Thấp] — [lý do]
Nguồn chính: [list nguồn + year]
Gaps: [thiếu data gì, assumption nào cần verify]"
```

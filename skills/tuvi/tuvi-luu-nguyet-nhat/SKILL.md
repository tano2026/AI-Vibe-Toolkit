---
name: tuvi-luu-nguyet-nhat
category: tuvi
description: Công cụ tính toán và luận giải Tử Vi Lưu Nguyệt (theo tháng) và Lưu Nhật (theo ngày) từ lá số gốc, bao gồm thuật toán an sao lưu động, Tứ Hóa và luận giải chi tiết.
---

# Tử Vi Lưu Nguyệt & Lưu Nhật - Công Cụ Tính Toán Chi Tiết

Skill này cung cấp module Python độc lập để tính toán sao Lưu Nguyệt (cấp tháng) và Lưu Nhật (cấp ngày) trong Tử Vi Đẩu Số. Dựa trên thông tin sinh và thời gian cần xem, công cụ sẽ xác định cung vị lưu động, các sao lưu, Tứ Hóa và đưa ra luận giải.

## Cài đặt & Yêu cầu

- **Python 3.x** (chỉ dùng thư viện chuẩn, không cần pip install)
- Hệ điều hành: Windows (đã test) / Linux / macOS
- File chính: `scripts/tuvi_luu_engine.py`

## Cách sử dụng

### 1. Chạy từ command line:

```bash
python tuvi_luu_engine.py [năm_sinh] [tháng_sinh] [ngày_sinh] [giờ_sinh] [giới_tính]
```

Ví dụ:
```bash
python tuvi_luu_engine.py 1984 5 1 0 male
```

### 2. Sử dụng như module Python:

```python
from tuvi_luu_engine import *

# Xem Lưu Nguyệt tháng 5 âm lịch năm 2026
print(xem_luu_nguyet(1984, 5, 1, 0, "male", 2026, 5))

# Xem Lưu Nhật ngày 30/06/2026
from datetime import datetime
print(xem_luu_nhat(1984, 5, 1, 0, "male", datetime(2026, 6, 30)))

# Xem tổng hợp 12 cung cho tháng
print(xem_tong_hop_thang(1984, 5, 1, 0, "male", 2026, 5))
```

### 3. Tích hợp với MCP Tử Vi server:

Có thể kết hợp dữ liệu lá số gốc từ `mcp_tuvi_calculate_chart` với output của module này:
1. Gọi `mcp_tuvi_calculate_chart` để lấy 12 cung + chính tinh + phụ tinh
2. Gọi `mcp_tuvi_yearly_detailed` để lấy Tuế Dẫn/Tuế Kiến
3. Dùng module này để tính Lưu Nguyệt/Nhật
4. Kết hợp và luận giải

## Thuật Toán An Sao

### 1. Đẩu Quân (cung tháng Giêng Lưu Nguyệt)

**Công thức:**
1. Lấy cung Lưu Thái Tuế (năm hạn) làm tháng Giêng
2. Đếm **NGHỊCH** đến tháng sinh âm lịch
3. Tại cung đó đặt giờ Tý, đếm **THUẬN** đến giờ sinh
4. Điểm dừng = Đẩu Quân

### 2. Lưu Nguyệt

- Đẩu Quân = cung tháng Giêng
- Các tháng sau đi **thuận** 1 cung/tháng
- **Tứ Hóa Lưu Nguyệt:** dùng Thiên Can của tháng (tính theo năm Can + tháng âm lịch)

### 3. Lưu Nhật

- Cung Lưu Nguyệt = ngày mùng 1
- Mỗi ngày đi **thuận** 1 cung
- **Tứ Hóa Lưu Nhật:** dùng Thiên Can của ngày (tính theo số ngày Julius)

### 4. Bảng an sao Lưu Niên (năm)

#### Theo Địa Chi năm:

| Sao | Cách an |
|-----|---------|
| **Lưu Thái Tuế** | Tại cung có tên năm hạn (VD: năm Ngọ → cung Ngọ) |
| **Lưu Tang Môn** | Từ Thái Tuế đi thuận 2 cung |
| **Lưu Bạch Hổ** | Tại cung xung chiếu với Tang Môn (+6) |
| **Lưu Thiên Khốc** | Khởi Ngọ (năm Tý), đếm nghịch đến năm hạn |
| **Lưu Thiên Hư** | Khởi Ngọ (năm Tý), đếm thuận đến năm hạn |
| **Lưu Thiên Mã** | Dần-Ngọ-Tuất → Thân; Thân-Tý-Thìn → Dần; Tỵ-Dậu-Sửu → Hợi; Hợi-Mão-Mùi → Tỵ |

#### Theo Thiên Can năm:

| Can | Lưu Lộc Tồn | Lưu Kình Dương | Lưu Đà La | Lưu Văn Xương | Lưu Văn Khúc | Lưu Khôi | Lưu Việt |
|-----|-------------|----------------|-----------|---------------|---------------|----------|----------|
| Giáp | Dần | Mão | Sửu | Tỵ | Dậu | Sửu | Mùi |
| Ất | Mão | Thìn | Dần | Ngọ | Thân | Tý | Thân |
| Bính | Tỵ | Ngọ | Thìn | Thân | Ngọ | Hợi | Dậu |
| Đinh | Ngọ | Mùi | Tỵ | Dậu | Tỵ | Dậu | Hợi |
| Mậu | Tỵ | Ngọ | Thìn | Thân | Ngọ | Sửu | Mùi |
| Kỷ | Ngọ | Mùi | Tỵ | Dậu | Tỵ | Tý | Thân |
| Canh | Thân | Dậu | Mùi | Hợi | Mão | Sửu | Mùi |
| Tân | Dậu | Tuất | Thân | Tý | Dần | Ngọ | Tý |
| Nhâm | Hợi | Tý | Tuất | Dần | Tý | Mão | Tỵ |
| Quý | Tý | Sửu | Hợi | Mão | Hợi | Mão | Tỵ |

**Ghi chú:** Lưu Kình Dương = Lưu Lộc Tồn + 1 (thuận), Lưu Đà La = Lưu Lộc Tồn - 1 (nghịch)

### 5. Tứ Hóa Lưu

| Can | Hóa Lộc | Hóa Quyền | Hóa Khoa | Hóa Kỵ |
|-----|---------|-----------|----------|--------|
| Giáp | Liêm Trinh | Phá Quân | Vũ Khúc | Thái Dương |
| Ất | Thiên Cơ | Thiên Lương | Tử Vi | Thái Âm |
| Bính | Thiên Đồng | Thiên Cơ | Văn Xương | Liêm Trinh |
| Đinh | Thái Âm | Thiên Đồng | Thiên Cơ | Cự Môn |
| Mậu | Tham Lang | Thái Âm | Hữu Bật | Thiên Cơ |
| Kỷ | Vũ Khúc | Tham Lang | Thiên Lương | Văn Khúc |
| Canh | Thái Dương | Vũ Khúc | Thái Âm | Thiên Đồng |
| Tân | Cự Môn | Thái Dương | Thiên Cơ | Văn Xương |
| Nhâm | Thiên Lương | Tử Vi | Tả Phụ | Vũ Khúc |
| Quý | Phá Quân | Cự Môn | Thái Âm | Tham Lang |

## Cấp độ áp dụng

- **Lưu Niên (năm):** Tất cả sao theo Can/Chi năm
- **Lưu Nguyệt (tháng):** Tứ Hóa + Lộc Tồn/Kình/Đà/Xương/Khúc/Khôi/Việt theo Can tháng
- **Lưu Nhật (ngày):** Tứ Hóa + Lộc Tồn/Kình/Đà/Xương/Khúc/Khôi/Việt theo Can ngày

## Output

Công cụ tạo output dạng text (format Telegram-compatible):

1. **Lưu Nguyệt:** Thông tin tháng (Can Chi), cung Lưu Nguyệt, sao trong cung, toàn bộ sao Lưu Nguyệt, Tứ Hóa, luận giải chi tiết
2. **Lưu Nhật:** Thông tin ngày (Can Chi), cung Lưu Nhật, sao trong cung, Tứ Hóa, luận giải chi tiết
3. **Tổng hợp tháng:** Bảng 12 cung với các sao Lưu Niên tương ứng

## Lưu ý

- Chuyển đổi Dương lịch → Âm lịch hiện dùng bảng tra đơn giản cho năm 1984 và 2026. Để chính xác tuyệt đối, nên nhập trực tiếp tháng/ngày âm lịch hoặc dùng thư viện lunardate.
- Các sao Lưu Nguyệt/Nhật được an theo Can Chi của tháng/ngày, độc lập với cung vị Lưu Nguyệt/Nhật.
- Luận giải mang tính tham khảo, cần kết hợp với lá số gốc và Đại Hạn để có cái nhìn toàn diện.

## 🤖 Agent Integration (Hermes)

Module này hoạt động độc lập — không cần MCP server, không cần API key.

### Python workflow (dùng trong Hermes):

```python
# === CẤU HÌNH ===
BIRTH = {"year": 1984, "month": 5, "day": 1, "hour": 0, "gender": "male"}
SKILL_DIR = r"D:\AI Store\AgentConfigs\hermes-local-appdata\skills\tuvi\tuvi-luu-nguyet-nhat"

import sys, os
sys.path.insert(0, os.path.join(SKILL_DIR, "scripts"))
from tuvi_luu_engine import xem_luu_nguyet, xem_luu_nhat, xem_tong_hop_thang

# === DÙNG NGAY ===
# Xem tháng 5 âm lịch năm 2026
result = xem_luu_nguyet(BIRTH["year"], BIRTH["month"], BIRTH["day"],
                         BIRTH["hour"], BIRTH["gender"], 2026, 5)
print(result)  # Gửi lên Telegram

# Xem ngày 30/06/2026
from datetime import datetime
result = xem_luu_nhat(BIRTH["year"], BIRTH["month"], BIRTH["day"],
                       BIRTH["hour"], BIRTH["gender"], datetime(2026, 6, 30))
print(result)
```

### Tích hợp với tuvi-dau-so-expert:

1. Load `tuvi-dau-so-expert` để có khung luận giải tổng thể (12 cung, cách cục, đại hạn)
2. Dùng module này để thêm chi tiết Lưu Nguyệt/Lưu Nhật
3. Kết hợp: sao gốc trong cung + sao lưu động + luận giải = output hoàn chỉnh

### Khi nào dùng skill này:

- User hỏi "tháng này thế nào", "tuần này sao" → chạy Lưu Nguyệt
- User hỏi "hôm nay tốt không", "ngày mai làm gì" → chạy Lưu Nhật
- User hỏi "có nên làm việc X trong tháng này" → chạy Lưu Nguyệt + đối chiếu cung liên quan

## Liên kết

- Module code: `scripts/tuvi_luu_engine.py`
- Nguồn nghiên cứu: `references/RESEARCH_SOURCES.md`
- Skill mẹ: `tuvi-dau-so-expert` (luận giải tổng thể)
- MCP tools hỗ trợ: `mcp_tuvi_calculate_chart`, `mcp_tuvi_yearly_detailed`, `mcp_tuvi_age_fortune`

## Test case

```python
# Sinh: 01/05/1984 dương lịch, giờ Tý (0h), Nam
# Âm lịch: ngày 01 tháng 04 năm 1984 (Giáp Tý)
# Năm xem: 2026 (Bính Ngọ), tuổi mụ 43

# Đẩu Quân: cung Mão (tháng Giêng Lưu Nguyệt)
# Lưu Nguyệt tháng 5 (Năm) âm lịch: cung Mùi
# Lưu Nguyệt Tứ Hóa (tháng Giáp Ngọ):
#   - Hóa Lộc: Liêm Trinh
#   - Hóa Quyền: Phá Quân
#   - Hóa Khoa: Vũ Khúc
#   - Hóa Kỵ: Thái Dương
# Lưu Nhật ngày 15 tháng 5 (30/06/2026 dl): cung Dậu
# Lưu Nhật Tứ Hóa (ngày Tân Sửu):
#   - Hóa Lộc: Cự Môn
#   - Hóa Quyền: Thái Dương
#   - Hóa Khoa: Thiên Cơ
#   - Hóa Kỵ: Văn Xương
# Lưu Thiên Việt đồng cung Lưu Nguyệt (Mùi) -> Giao Hữu
```

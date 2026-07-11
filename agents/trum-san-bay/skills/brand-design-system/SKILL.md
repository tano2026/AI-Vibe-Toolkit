# Brand Design System — Trùm Sân Bay

## Mô tả
Skill này là "gác cổng visual" — đảm bảo mọi ảnh/video ra khỏi pipeline đều đúng bộ nhận diện, dù được gen bởi Visual Agent nào, cho platform nào. Không có skill này thì mỗi post sẽ trông một kiểu, mất tính chuyên nghiệp và độ nhận diện thương hiệu.

## Trigger
Dùng khi: Visual Agent gen xong asset (ảnh hoặc video), TRƯỚC khi chuyển sang Adapter Agent.

## Vị trí trong pipeline

```
Visual Agent (gen raw asset)
        ↓
Brand Design System (kiểm tra + chuẩn hóa)  ← agent mới
        ↓
Adapter Agent (pack theo platform)
```

## Bộ nhận diện — Trùm Sân Bay

### Màu sắc (Design Tokens)
```css
--tsb-navy-dark:   #0a1628;   /* background chính */
--tsb-navy-light:  #1a3a5c;   /* gradient phụ */
--tsb-gold:        #FFD700;   /* accent, CTA, highlight */
--tsb-white:       #FFFFFF;   /* text chính */
--tsb-gray:        #8A96A3;   /* text phụ, caption nhỏ */
--tsb-red-alert:   #E63946;   /* cảnh báo, urgent */
--tsb-green-ok:    #2ECC71;   /* tip tích cực, checklist */
```

### Typography
```
Font chính:     Be Vietnam Pro (Google Fonts, hỗ trợ tiếng Việt tốt)
Font phụ:       Inter (số liệu, data)
Hook/Title:     Bold 700-900, 60-80px (trên video 1080px width)
Body:           Regular 400-500, 40-48px
CTA:            Bold 700, 48-52px
```

### Logo & Watermark
```
Vị trí cố định: góc dưới phải mọi asset
Nội dung: "✈️ Trùm Sân Bay"
Opacity: 70% trên ảnh, 60% trên video (không che nội dung)
Kích thước: 36-40px chiều cao trên canvas 1080-1920px
```

### Icon set chuẩn (dùng nhất quán, không đổi lung tung)
```
✈️  hàng không / chuyến bay
🛫  khởi hành / check-in
🛄  hành lý
⚡  fast track / nhanh
💱  đổi tiền
📱  SIM / kết nối
⚠️  cảnh báo
✅  tip / checklist tích cực
❌  lỗi thường gặp / không nên làm
💡  insider tip
```

### Layout Grid (video 1080x1920)
```
Safe zone top:     0-150px    (tránh notch/status bar khi xem)
Hook zone:         150-450px
Body zone:         450-1500px
CTA zone:          1500-1750px
Logo/footer zone:  1750-1920px
```

### Layout Grid (ảnh 1080x1080 — Instagram/Facebook)
```
Safe zone:         60px margin mọi cạnh
Text overlay:      max 60% diện tích ảnh (còn lại để ảnh thở)
Logo:              góc dưới phải, 40px từ mép
```

## Checklist kiểm tra trước khi asset qua Adapter

```
[ ] Màu nền/accent đúng bảng màu TSB (không lệch sang màu khác)
[ ] Font đúng Be Vietnam Pro hoặc Inter
[ ] Logo/watermark có mặt, đúng vị trí, đúng opacity
[ ] Icon dùng đúng bộ chuẩn, không tự chế icon lạ
[ ] Text nằm trong safe zone, không bị crop khi platform tự resize
[ ] Contrast text/background đủ đọc (WCAG AA tối thiểu — tỷ lệ 4.5:1)
[ ] Không dùng ảnh stock lạc tone (quá Tây, không giống sân bay VN)
[ ] Video: progress bar/animation không giật, transition mượt
```

## Code helper — validate trước khi pass

```python
def validate_brand_consistency(asset_metadata):
    """
    Check nhanh trước khi asset qua Adapter Agent
    asset_metadata = {"colors_used": [...], "font": "...", "has_logo": bool, "logo_position": "..."}
    """
    issues = []

    ALLOWED_COLORS = ["#0a1628", "#1a3a5c", "#FFD700", "#FFFFFF", "#8A96A3", "#E63946", "#2ECC71"]
    ALLOWED_FONTS = ["Be Vietnam Pro", "Inter"]

    for color in asset_metadata.get("colors_used", []):
        if color.upper() not in [c.upper() for c in ALLOWED_COLORS]:
            issues.append(f"Màu {color} không thuộc bảng màu TSB")

    if asset_metadata.get("font") not in ALLOWED_FONTS:
        issues.append(f"Font {asset_metadata.get('font')} không đúng chuẩn")

    if not asset_metadata.get("has_logo"):
        issues.append("Thiếu logo/watermark")

    if asset_metadata.get("logo_position") != "bottom-right":
        issues.append("Logo sai vị trí, phải ở góc dưới phải")

    return {
        "passed": len(issues) == 0,
        "issues": issues
    }
```

## Khi asset KHÔNG pass check

- Trả về Visual Agent kèm danh sách issues cụ thể
- Visual Agent sửa lại (không cần regenerate từ đầu, chỉ overlay lại logo/màu nếu có thể)
- Nếu vấn đề nằm ở prompt gen ảnh gốc → cần regenerate

## Cập nhật bộ nhận diện

Khi Nobitano muốn đổi màu/font/logo:
1. Update file này trước (`skills/brand-design-system/SKILL.md`)
2. Update `ALLOWED_COLORS` / `ALLOWED_FONTS` trong code
3. Update template HTML trong `video-renderer` skill để khớp token mới
4. Asset cũ không cần làm lại, chỉ áp dụng cho content mới

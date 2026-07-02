---
name: tuvi-mcp-server
description: MCP server tử vi đẩu số - tính lá số, phân tích mệnh/tài/quan/lộc, xem đại hạn, vận hạn lưu niên, so sánh 2 lá số. Wraps thư viện iztro (⭐3.8k). Ecosystem gồm Bát Tự MCP, Hoàng Lịch, Horosa, Taibu.
category: mcp
---

# Tử Vi Đẩu Số MCP Server

## Vị trí
- MCP server: `D:\AI Store\Hermes Agent\tuvi-mcp-server\index.mjs`
- Config: `~/.hermes/config.yaml` → section `mcp_servers.tuvi`

## Cấu trúc
```
tuvi-mcp-server/
├── package.json        # "type": "module" (ESM)
├── index.mjs           # MCP server chính (v2.0)
├── star-meanings.md    # Reference: ý nghĩa 35 sao
└── node_modules/
```

## Cài đặt
```bash
cd /d/AI\ Store/Hermes\ Agent
npm init -y
npm install iztro @modelcontextprotocol/sdk
```
Sửa `package.json`: thêm `"type": "module"`.

## Config Hermes (config.yaml)
```yaml
mcp_servers:
  tuvi:
    command: node
    args:
      - D:\\AI Store\\Hermes Agent\\tuvi-mcp-server\\index.mjs
    timeout: 30
    description: Tử vi đẩu số agent
```

## Tools (7 tools)

### 1. calculate_chart
Tính lá số cơ bản — 12 cung + chính/phụ/tập tinh + đại hạn.
- Input: `year`, `month`, `day`, `hour` (0-23), `gender` (male/female), `language` (vi/en)
- Output: `thongTinCoBan` + `cacCung[]` (mỗi cung: tên, thiên can, địa chi, thân cư?, đại hạn, danh sách sao)

### 2. analyze_destiny
Phân tích 6 cung chính: Mệnh, Tài, Quan, Điền, Phúc, Phu Thê. + đại hạn hiện tại.
- Input: giống calculate_chart

### 3. current_decadal_fortune
Xem đại hạn hiện tại. Tự tính tuổi nếu không nhập `age`.

### 4. yearly_fortune 🆕
Xem tử vi trọn năm — vận hạn lưu niên.
- Input thêm: `targetYear` (VD: 2026)
- Output: đại hạn năm đó (thiên can, địa chi, hóa), tuổi, lưu niên (can/chi + hóa)
- Dùng `chart.horoscope(dateString, timeIndex)` của iztro

### 5. compatibility 🆕
So sánh 2 lá số — tình duyên (love) hoặc làm ăn (business).
- Input: `yearA/monthA/dayA/hourA/genderA` + `yearB/monthB/dayB/hourB/genderB` + `relationship` (love/business)
- So Mệnh A vs Mệnh B, Phu Thê (love) hoặc Tài Bạch (business)
- **Tuổi tác:** tam hợp, lục hợp, tương xung, tương hại
  - Tam hợp: Thân-Tý-Thìn, Dần-Ngọ-Tuất, Tỵ-Dậu-Sửu, Hợi-Mão-Mùi
  - Lục hợp: Tý-Sửu, Dần-Hợi, Mão-Tuất, Thìn-Dậu, Tỵ-Thân, Ngọ-Mùi
  - Tương xung: Tý-Ngọ, Sửu-Mùi, Dần-Thân, Mão-Dậu, Thìn-Tuất, Tỵ-Hợi
  - Tương hại: Tý-Mùi, Sửu-Ngọ, Dần-Tỵ, Mão-Thìn, Thân-Hợi, Dậu-Tuất

### 6. palace_detail 🆕
Phân tích chuyên sâu 1 cung cụ thể.
- Input thêm: `palace` (tên cung tiếng Việt: Mệnh, Huynh Đệ, Phu Thê...)
- Output: vị trí (thiên can/địa chi), chính/phụ/tập tinh + độ sáng + hóa, đại hạn, + vận hạn năm hiện tại

### 7. star_meaning 🆕
Tra cứu ý nghĩa sao. Database 35 sao (14 chính tinh + phụ tinh + hóa tinh + tập tinh phổ biến).

## Giờ sinh mapping (BUG đã fix)
```js
// hour 0-23 → timeIndex (iztro: 0=Tý...11=Hợi, 12=晚子)
// Tý(23-01:0), Sửu(01-03:1), Dần(03-05:2), Mão(05-07:3),
// Thìn(07-09:4), Tỵ(09-11:5), Ngọ(11-13:6), Mùi(13-15:7),
// Thân(15-17:8), Dậu(17-19:9), Tuất(19-21:10), Hợi(21-23:11)
const timeIndices = [0,0,1,1,2,2,3,3,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12];
// h=23 → 12 (晚子), otherwise timeIndices[h]
```
⚠️ **Lỗi cũ:** mảng cũ `[...,4,4,5,5,...]` gán giờ 9 (9h = Tỵ) vào index 4 (Thìn). **Fix:** index 8→4, index 9→5.

## API iztro quan trọng
```js
import iztro from 'iztro';
// 1. Tính lá số
const chart = iztro.astro.bySolar('1984-5-1', 5, 'male', true, 'vi');
// bySolar(solarDate, timeIndex, gender, fixLeap, language)

// 2. Vận hạn lưu niên (yearly fortune)
const hs = chart.horoscope('2026-6-15', 5); // (targetDate, timeIndexOfTarget)
// hs.decadal — đại hạn năm đó
// hs.age — tuổi (nominalAge)
// hs.yearly — lưu niên

// 3. Tra sao
chart.star('ziweiMaj'); // thông tin sao (circular ref — dùng JSON.stringify với custom replacer)

// 4. Palace methods
chart.palaces[10].isEmpty();           // cung có vô chính diệu?
chart.palaces[10].has('ziweiMaj');     // có sao này?
chart.palaces[10].hasOneOf([...]);     // có 1 trong các sao?
chart.palaces[10].selfMutaged();       // có tự hóa?
chart.palaces[10].changsheng12;        // Trường sinh 12
chart.palaces[10].boshi12;             // Bác sĩ 12
chart.palaces[10].ages;                // [4,16,28,40,...]
chart.surroundedPalaces('soulPalace'); // cung xung chiếu
```

## Translation tables
Xem file `references/translation-tables.md` cho bảng dịch đầy đủ:
- PALACE_NAMES_VI (12 cung)
- STAR_NAMES_VI (14 chính tinh + phụ tinh)
- ADJ_STAR_VI (tập tinh: Hồng Loan, Cô Thần, Quả Túc...)
- BRIGHTNESS_VI, MUTAGEN_VI
- STEM_VI (10 thiên can), BRANCH_VI (12 địa chi)
- ELEMENTS_VI (ngũ hành cục), ZODIAC_VI (12 con giáp)
- TIME_VI (12 giờ âm), SIGN_VI (12 cung hoàng đạo)
- HOROSCOPE_STAR_VI (sao lưu niên/đại hạn: Vân Mã, Vân Đà...)

## Pitfalls
1. **Giờ 23:** Là giờ Tý muộn (晚子), index=12 — khác với Tý đầu (index=0). iztro handle được nhưng mapping phải đúng.
2. **chart.star() trả về circular:** không JSON.stringify trực tiếp được. Dùng hoặc chọn field cụ thể.
3. **chart.horoscope() cần timeIndex:** timeIndex của NGƯỜI XEM (không phải của năm). Luôn dùng timeIndex của người được xem.
4. **Không nhầm palace index:** iztro palace order khác. Mệnh = index 10 (soulPalace), không phải index 0.
5. **hour param là int 0-23:** parseHour tự xử lý. Nếu hour=9, parseHour trả về 5 (Tỵ), hour=15 → 8 (Thân).

## Related References
Xem `references/external-ecosystem.md` cho catalog đầy đủ các MCP server và thư viện liên quan:
- **Bát Tự:** `shunshi-bazi-mcp` (có Hoàng Lịch, miễn phí) và `cantian-ai/bazi-mcp` (⭐385)
- **Chiêm tinh phương Đông:** `Horosa` ⭐260 (bách khoa toàn thư)
- **AI Reading:** `ruijayfeng/ziwei` ⭐344 (ZiweiKnows, có AI pipeline)
- **Full divination + MCP:** `hhszzzz/taibu` ⭐199 (Bát Tự, Tử Vi, Kỳ Môn, Lục Nhâm, Tarot...)` 

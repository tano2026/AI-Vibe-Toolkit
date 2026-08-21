---
name: source-evaluation
description: >
  Chấm điểm độ tin cậy của nguồn thông tin trước khi dùng vào research. Phân biệt
  primary / secondary / tertiary source, detect data cũ, phát hiện conflict giữa các nguồn.
  Dùng skill này khi agent cần evaluate xem có nên tin một nguồn không, khi tìm thấy
  số liệu mâu thuẫn giữa các nguồn, hoặc trước khi cite bất kỳ claim quan trọng nào.
  Trigger với: "kiểm tra nguồn", "nguồn này đáng tin không", "2 nguồn khác nhau",
  "evaluate source", "độ tin cậy", "có nên tin không".
---

# Source Evaluation — Chấm Điểm Độ Tin Cậy Nguồn

Nguồn rác + agent tin mù = hallucination có cơ sở. Nguy hiểm hơn hallucination thường
vì nó trông có vẻ đúng.

---

## Quy trình 4 bước

### Bước 1 — Xác định loại nguồn

```
PRIMARY SOURCE (⭐⭐⭐⭐⭐) — Dữ liệu gốc, không qua trung gian:
  ✅ Báo cáo tài chính chính thức (SEC filing, BCTC công ty)
  ✅ Academic paper peer-reviewed (Google Scholar, arXiv, PubMed)
  ✅ Số liệu từ cơ quan nhà nước (GSO VN, World Bank, IMF, Eurostat)
  ✅ Survey/Research do chính công ty đó thực hiện (phải có methodology)
  ✅ Patent filing, regulatory document

SECONDARY SOURCE (⭐⭐⭐⭐) — Phân tích từ nguồn gốc:
  ✅ Industry analyst reports: Gartner, IDC, McKinsey, BCG, Deloitte
  ✅ Báo chí kinh tế uy tín: Reuters, Bloomberg, FT, WSJ, VnExpress Kinh tế
  ✅ Thought leadership từ domain expert có credentials rõ ràng

TERTIARY SOURCE (⭐⭐⭐) — Tổng hợp từ secondary:
  ⚠️  Wikipedia, Investopedia, blog chuyên ngành
  ⚠️  LinkedIn posts từ practitioners (có thể bias)
  ⚠️  News aggregator, newsletter

QUESTIONABLE (⭐⭐):
  ❌ Anonymous source ("according to industry insiders")
  ❌ Press release không có methodology
  ❌ Social media post không có data backing
  ❌ Site không rõ tác giả, không có date

UNRELIABLE (⭐):
  ❌ Mâu thuẫn với nhiều nguồn độc lập khác
  ❌ No date (số liệu market size không có năm = vô dụng)
  ❌ Conflict of interest rõ ràng (vendor cite chính mình)
```

### Bước 2 — Kiểm tra freshness

```
Quy tắc "data shelf life" theo loại:
  Real-time market price:    stale sau 1 ngày
  Startup funding news:      stale sau 6 tháng
  Market size numbers:       stale sau 2 năm
  Industry structure:        stale sau 3 năm
  Academic theory:           stale sau 5-10 năm (tùy ngành)

⚠️ OVERRIDE riêng cho data thị trường VIỆT NAM (theo EXPERT-CORE.md section ①,
   luật "không thương lượng" — áp dụng bất kể quy tắc chung ở trên):
  Data thị trường VN quá 18 THÁNG = coi là cũ, PHẢI nói rõ tuổi data trong
  output, không âm thầm dùng như data mới.

Nếu không có date → KHÔNG dùng cho market size claims.
Ghi rõ: "Số liệu này không có ngày → độ tin cậy thấp"
```

### Bước 3 — Triangulate

```
Rule (theo EXPERT-CORE.md ①, "không thương lượng"):
Claim ảnh hưởng quyết định TIỀN/CHIẾN LƯỢC = phải có ≥2 independent sources
ĐỒNG THỜI mỗi nguồn phải đạt điểm ≥3 (Tertiary trở lên, KHÔNG tính
Questionable/Unreliable dù có 2-3 nguồn loại đó). 2 nguồn rác vẫn là 2
nguồn rác, không cộng dồn thành đáng tin.

"Independent" nghĩa là:
  ✅ 2 nguồn KHÔNG trích dẫn lẫn nhau
  ✅ 2 nguồn từ 2 tổ chức khác nhau
  ✅ 2 nguồn dùng methodology khác nhau
  ❌ Không tính: site A trích site B, site B trích site A → đây là 1 nguồn

Nếu chỉ tìm được 1 nguồn (hoặc <2 nguồn đạt điểm ≥3):
  → Label rõ: [Single source — độ tin thấp, cần verify thêm]
  → Không loại bỏ, nhưng không present as fact

Nếu 2 nguồn mâu thuẫn:
  → Report cả 2 kèm lý do có thể khác nhau (năm khác, scope khác, methodology khác)
  → Không tự chọn 1 cái bỏ cái kia
```

### Bước 4 — Label trong output

```
⚠️ QUAN TRỌNG: EXPERT-CORE.md (não cứng toàn hệ thống) quy định output PHẢI
gắn nhãn confidence theo đúng 3 mức [cao]/[vừa]/[thấp] — đây là hệ nhãn
DÙNG CHUNG cho mọi role (Research/Marketing/Sales/Content), không chỉ riêng
Research. Hệ ⭐ ở trên là công cụ NỘI BỘ để tính ra đúng mức nào, nhưng khi
xuất output cuối, PHẢI quy đổi về đúng 3 nhãn chuẩn này để nhất quán với
Marketing/Sales/Content khi họ đọc report của Research.

Bảng quy đổi ⭐ → nhãn chuẩn:
  ⭐⭐⭐⭐⭐ Primary + có ≥2 nguồn độc lập đồng thuận  → [cao]
  ⭐⭐⭐⭐  Secondary + có ≥2 nguồn độc lập            → [cao]
  ⭐⭐⭐⭐/⭐⭐⭐⭐⭐ nhưng CHỈ 1 nguồn (chưa triangulate) → [vừa]
  ⭐⭐⭐   Tertiary, hoặc 2 nguồn nhưng mâu thuẫn nhau  → [vừa]
  ⭐⭐    Questionable, hoặc ước lượng/suy diễn        → [thấp]
  ⭐     Unreliable                                    → [thấp] (cân nhắc loại bỏ)

Trong mọi output, label rõ CẢ 2 lớp (chi tiết ⭐ cho ai cần đào sâu, nhãn
chuẩn [cao/vừa/thấp] để role khác đọc nhanh):
  [cao] (⭐⭐⭐⭐⭐ Primary, 2 nguồn độc lập) Số liệu XYZ — Nguồn: World Bank 2024
  [cao] (⭐⭐⭐⭐ Secondary, 2 nguồn) Ước tính thị trường ABC — McKinsey Q3/2025
  [vừa] (⭐⭐⭐⭐ Secondary, single-source) Con số này chỉ 1 nguồn, chưa verify chéo
  [thấp] (Estimated) Ước tính của tao dựa trên [logic], không có primary source
  [Disputed] Có 2 nguồn khác nhau: [Nguồn A: $X] vs [Nguồn B: $Y] — xem phụ lục
```

---

## Ví dụ thực tế

**Scenario:** Research market size AI Việt Nam.

Search trả về 3 kết quả:
1. "AI market Vietnam: $500M" — Blog không tên tác giả, 2022
2. "Vietnam AI market to reach $830M by 2025" — Statista, 2023, có methodology
3. "AI và công nghệ số VN tăng trưởng 25%/năm" — Bộ TT&TT 2024, nhưng không có số tuyệt đối

**Đánh giá:**
- Nguồn 1: ⭐⭐ Questionable — không tác giả, data cũ 2022 (4 năm)
- Nguồn 2: ⭐⭐⭐⭐ Secondary — Statista có methodology, nhưng đã 2 năm
- Nguồn 3: ⭐⭐⭐⭐⭐ Primary — chính phủ, 2024, nhưng không có số tuyệt đối

**Output đúng:**
"Theo Statista (2023) [⭐⭐⭐⭐], thị trường AI Việt Nam ước tính đạt $830M vào năm 2025.
Bộ TT&TT (2024) [⭐⭐⭐⭐⭐] xác nhận tăng trưởng 25%/năm nhưng không công bố số tuyệt đối.
Chưa tìm được primary source xác nhận con số $830M — cần verify thêm."

---

## Lỗi thường gặp

- **Citation laundering:** Site A trích Site B, Site B trích Site A → tưởng 2 nguồn nhưng thực ra 1
- **Vendor bias:** Công ty SaaS tự công bố "market growing 300%" — luôn check nguồn độc lập
- **Stale data disguised:** "Market size $XB" không có năm → KHÔNG dùng
- **Precision illusion:** "$1,234,567,890 market" trông chính xác hơn "$1.2B" nhưng không đáng tin hơn

## Đối chiếu với EXPERT-CORE.md (cập nhật sau audit)

Skill này đã được đối chiếu với `agents/company/EXPERT-CORE.md` section ①
(RESEARCH & DATA ANALYTICS) — 3 điểm đã vá: ngưỡng 18 tháng riêng cho data
VN, điều kiện điểm ≥3 khi triangulate, và hệ nhãn `[cao]/[vừa]/[thấp]` dùng
chung toàn hệ thống. 2 luật khác của section ① (lệch top-down/bottom-up
>30%, và SO WHAT + tối đa 3 khuyến nghị) đã có sẵn đúng chỗ hơn trong
`market-sizing` và `data-storytelling` — không lặp lại ở đây.

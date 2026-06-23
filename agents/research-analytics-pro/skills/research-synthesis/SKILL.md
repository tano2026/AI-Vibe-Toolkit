---
name: research-synthesis
description: >
  Tổng hợp thông tin từ nhiều nguồn thành 1 bức tranh coherent. Detect mâu thuẫn,
  fill gaps, triangulate claims, và ra narrative rõ ràng thay vì dump data.
  Dùng khi đã có đủ raw data từ Scout và cần tổng hợp lại thành report.
  Trigger với: "tổng hợp", "synthesis", "kết hợp các nguồn", "viết report từ data này",
  "có nhiều nguồn rồi giờ tổng hợp", "combine sources".
---

# Research Synthesis — Tổng Hợp Đa Nguồn

Raw data không phải insight. Synthesis là kỹ năng biến 15 tab browser thành 1 báo cáo
người đọc hiểu được trong 5 phút.

---

## Quy trình 5 bước

### Bước 1 — Cluster theo chủ đề

```
Sau khi có raw data từ Scout, KHÔNG viết ngay.
Trước tiên, nhóm thông tin thành clusters:

  Cluster A: Market size & growth
  Cluster B: Key players & positioning
  Cluster C: Trends & drivers
  Cluster D: Risks & challenges
  Cluster E: Opportunities

Mỗi cluster → list tất cả data points có liên quan + nguồn của từng cái.
Bước này giúp phát hiện: có cluster nào thiếu data không? Có cái nào thừa không?
```

### Bước 2 — Detect & resolve conflicts

```
Với mỗi cluster, check xem các sources có agree không:

  Scenario 1 — Đồng thuận: ≥2 nguồn cùng claim → mark as "Confirmed"
  Scenario 2 — Một chiều: chỉ 1 nguồn → mark as "Single-source, unverified"
  Scenario 3 — Mâu thuẫn: 2 nguồn claim khác nhau →

    Hỏi: tại sao chúng khác nhau?
      → Năm khác? (market size 2023 vs 2025 → khác là đúng)
      → Scope khác? (global vs regional → khác là đúng)
      → Definition khác? (AI software vs AI market tổng → khác là đúng)
      → Methodology khác? (survey vs modeling → có thể khác)
      → 1 cái sai? → cross-check với nguồn thứ 3

    Nếu không giải thích được → report cả 2, label "[Disputed]"
```

### Bước 3 — Fill gaps chủ động

```
Sau khi cluster, check xem thiếu gì:

  ❓ Thiếu số liệu cụ thể? → Quay lại Scout search thêm
  ❓ Thiếu primary source? → Note là [Estimated] hoặc [Secondary only]
  ❓ Thiếu perspective? → Có sources từ phía buyers/users chưa, hay chỉ có vendor?
  ❓ Thiếu regional data? → Số toàn cầu có, nhưng có data VN/SEA không?

KHÔNG fake-fill bằng assumption. Thiếu thì nói thiếu.
```

### Bước 4 — Build narrative

```
Structure mọi synthesis theo What → So What → Now What:

  WHAT (Facts):
  "Thị trường X đạt $Y vào năm Z, tăng W% so với năm trước [Nguồn]."
  "3 players lớn nhất chiếm 60% thị phần: A (25%), B (20%), C (15%) [Nguồn]."

  SO WHAT (Insight):
  "Điều này có nghĩa là thị trường đang consolidate — top 3 ăn hầu hết, long-tail khó sống."
  "Tốc độ tăng W% cao hơn GDP 3 lần → ngành này đang outperform economy."

  NOW WHAT (Implication):
  "Nếu mày là new entrant → cần tìm niche mà top 3 bỏ qua, không thể compete head-on."
  "Nếu mày là investor → window đang mở, nhưng consolidation sắp đến — cần move nhanh."

Không bao giờ dừng ở WHAT. Người ta hỏi tao không phải để mày kể lại số liệu họ có thể
Google được — họ muốn biết ý nghĩa của nó với họ.
```

### Bước 5 — Quality check trước khi output

```
Checklist trước khi present:

  □ Mọi số liệu đều có nguồn và năm?
  □ Có ≥2 independent sources cho claims quan trọng?
  □ Conflicts đã được acknowledge, không bị ém?
  □ Có câu "So what" cho mỗi section không?
  □ Khuyến nghị cuối có actionable không (ai làm, làm gì, deadline nào)?
  □ Giới hạn của research này đã được nêu chưa? (thiếu data gì, confidence level)
```

---

## Ví dụ thực tế

**Input:** 12 articles về thị trường EdTech Việt Nam

**Sau khi cluster:**
- Cluster A (Market size): VND 3,500 tỷ (2023, VIR) vs $450M (2024, Statista) → check lại → đây là VND vs USD, convert ra trùng khớp ✅
- Cluster B (Players): Topica, ELSA, CoLearn, Everest — đồng thuận 4/4 sources ✅
- Cluster C (Trends): Mobile-first, AI tutoring, exam prep dominant → 3/3 sources đồng thuận ✅
- Cluster D (Risks): Monetization gap (free users không chuyển sang paid) → chỉ 1 source ⚠️
- Cluster E (Opportunities): B2B corporate training bị ignore bởi current players → 2 sources ✅

**Output narrative:**
"Thị trường EdTech VN ước ~$450M (2024), dominated bởi exam prep và English learning.
Top players (Topica, ELSA, CoLearn) đang fight cho cùng 1 segment.

**Điều thú vị hơn:** Corporate training (B2B) gần như bị bỏ ngỏ — 2 nguồn độc lập đề cập
nhưng không có player nào đang focus. Đây là gap đáng chú ý..."

---

## Lỗi thường gặp

- **Info dump:** List hết tất cả data tìm được → người đọc overwhelmed, không có insight
- **Cherry-picking:** Chỉ cite nguồn support conclusion mình muốn → confirmation bias
- **Missing "So what":** "Thị trường tăng 30%" → và? Ý nghĩa gì với người hỏi?
- **Fake precision:** "Market size $1,234,567,890" → copy từ 1 source không verify
- **Buried conflict:** Biết có mâu thuẫn nhưng không nêu vì "confuse người đọc" → sai

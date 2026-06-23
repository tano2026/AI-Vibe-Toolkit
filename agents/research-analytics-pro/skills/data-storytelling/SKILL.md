---
name: data-storytelling
description: >
  Biến số liệu và analysis thành narrative có insight và recommendation hành động.
  Không dừng ở "what" — luôn đi đến "so what" và "now what".
  Dùng sau khi có analysis xong, trước khi present output cho user.
  Trigger với: "viết insight", "tóm tắt cho lãnh đạo", "present data", "executive summary",
  "ý nghĩa là gì", "khuyến nghị", "so what", "what does this mean", "write up findings".
---

# Data Storytelling — Biến Số Thành Insight

Data không tự nói. Mày phải là người phiên dịch.

---

## Framework: What → So What → Now What

```
WHAT       = Thực tế xảy ra gì (facts, numbers)
SO WHAT    = Ý nghĩa là gì (insight, implication)
NOW WHAT   = Nên làm gì (recommendation, action)

Ví dụ:

WHAT:      "Bounce rate tăng từ 40% lên 65% trong tháng 3"
SO WHAT:   "35% traffic đang rời trang trong vài giây — landing page hoặc page speed có vấn đề"
NOW WHAT:  "Chạy PageSpeed Insights ngay. Nếu score <50 → fix technical trước.
            Nếu score okay → A/B test headline và above-the-fold content tuần tới"

WHAT:      "Top 3 players chiếm 75% thị phần AI coding tools"
SO WHAT:   "Thị trường đang consolidate nhanh — window cho new entrant đang đóng dần"
NOW WHAT:  "Nếu muốn vào thị trường này → phải tìm niche (vertical-specific, local market,
            enterprise segment) — không thể compete với Cursor/GitHub Copilot head-on"
```

---

## Structure cho Executive Summary

```
Bố cục 5 phần (không thêm không bớt):

1. HEADLINE (1 câu)
   Câu quan trọng nhất của toàn bộ research. Nếu người đọc chỉ đọc 1 câu, đây là câu đó.
   Ví dụ: "Thị trường SaaS SME Đông Nam Á đang tăng 28%/năm nhưng gần như không có player
   VN nào — đây là cơ hội hoặc dấu hiệu thị trường chưa sẵn sàng"

2. CONTEXT (2-3 câu)
   Bức tranh tổng quát để người đọc hiểu số liệu trong đúng bối cảnh.

3. KEY FINDINGS (3-5 bullets)
   Mỗi bullet = 1 insight có data support, không phải chỉ fact.
   Format: [Fact] → [Implication]
   Ví dụ: "ELSA Speak đạt 20M users (2024) — nhưng 95% là free tier → monetization vẫn là
   bài toán chưa giải của EdTech VN"

4. KHUYẾN NGHỊ (3-5 actions)
   Mỗi action phải: cụ thể + có owner + có timeline (hoặc ít nhất là priority)
   Format: [Action] — [Lý do] — [Độ ưu tiên]
   Ví dụ: "Pilot corporate training với 2-3 doanh nghiệp trong Q3 — đây là gap chưa ai
   khai thác, CAC thấp hơn B2C — HIGH priority"

5. LIMITATIONS (1-3 bullets)
   Cái gì tao không biết, thiếu data ở đâu, confidence level của phân tích này.
   Không ẩn limitations — nó thể hiện professional judgment, không phải yếu điểm.
```

---

## Quy tắc viết cho non-expert audience

```
1. Giải nghĩa thuật ngữ ngay trong câu:
   ❌ "TAM của thị trường này là $5B"
   ✅ "Tổng quy mô thị trường (TAM — tức là nếu 1 công ty chiếm hết) là $5B"

2. Số liệu cần context:
   ❌ "Tăng trưởng 28%/năm"
   ✅ "Tăng trưởng 28%/năm — cao gần gấp 3 lần GDP Việt Nam — đây là ngành đang trong
       giai đoạn bùng nổ"

3. Comparison làm số có nghĩa:
   ❌ "Thị trường $450M"
   ✅ "Thị trường $450M — tương đương doanh thu 2 năm của Masan Consumer"

4. Dùng analogy cho concept phức tạp:
   ❌ "CAGR của thị trường này là 23% trong 5 năm"
   ✅ "Thị trường này tăng gộp 23%/năm trong 5 năm — cứ mỗi 3 năm thì market size
       gần như nhân đôi"
```

---

## Visualization guidance

```
Chart selection:
  So sánh số tuyệt đối  → Bar chart
  Trend theo thời gian  → Line chart
  Phần trăm tổng thể    → Pie/donut (chỉ khi ≤5 segments)
  Phân phối             → Histogram hoặc box plot
  Correlation           → Scatter plot
  Market positioning    → 2x2 matrix

Khi dùng sc-datav (3D dashboard từ kho):
  → Dùng cho executive presentation, wow factor cao
  → KHÔNG dùng cho nội bộ team analyst — 3D trông đẹp nhưng khó đọc số chính xác
  → Dùng plotly cho interactive charts thông thường
```

---

## Lỗi thường gặp

- **Data vomit:** Paste hết tất cả findings vào → overwhelming, không có narrative
- **Missing headline:** Người đọc đọc xong không biết takeaway chính là gì
- **Vague recommendation:** "Nên đầu tư vào digital marketing" → cụ thể là gì? Bao nhiêu? Ai làm?
- **Buried insight:** Insight quan trọng nhất để ở giữa báo cáo → không ai đọc tới
- **Confidence overstatement:** Present estimation như fact → mất credibility ngay khi bị hỏi về nguồn

---
name: tu-duy-tai-chinh-vi-mo
description: >
  Framework tư duy tài chính vĩ mô kiểu "Chiến Tranh Tiền Tệ" (Song Hongbing) + "Big Cycle"
  (Ray Dalio) — đọc chu kỳ nợ, tiền tệ, địa chính trị để hiểu VÌ SAO thị trường/tiền tệ biến
  động, không phải tư duy tài chính doanh nghiệp (đã có ở ops-finance). Dùng cho content GMSP
  và tư duy chiến lược của CEO trước biến động vĩ mô (tỷ giá, lạm phát, giá vàng).
---

# Tư duy Tài chính Vĩ mô — Chiến Tranh Tiền Tệ × Big Cycle

## TL;DR
Đây KHÔNG phải skill tài chính doanh nghiệp (xem `roles/ops-finance.md` cho DCF/unit economics).
Đây là khung tư duy đọc **bối cảnh vĩ mô** — chu kỳ nợ, cung tiền, tỷ giá, vàng, địa chính trị —
theo 2 nguồn: "Chiến Tranh Tiền Tệ" (Song Hongbing, góc nhìn địa chính trị-lịch sử tiền tệ) và
"Principles for Navigating Big Debt Crises" / "Big Cycle" (Ray Dalio, góc nhìn hệ thống-số liệu).

## Khi nào dùng
- Viết content GMSP phần kinh tế (System #2/#3) cần giải thích 1 hiện tượng vĩ mô (vì sao vàng
  tăng, vì sao VND mất giá, vì sao lãi suất Fed ảnh hưởng tới VN) theo lối kể chuyện dễ hiểu.
- CEO cần góc nhìn nhanh trước 1 quyết định bị ảnh hưởng bởi vĩ mô (giá vé máy bay biến động
  theo tỷ giá USD, chi phí nhập hàng Wonder Mart bị ảnh hưởng bởi lạm phát/tỷ giá).
- KHÔNG dùng cho quyết định đầu tư tài chính cá nhân thật (không phải lời khuyên đầu tư) —
  chỉ dùng để hiểu bối cảnh, không phải để quyết định mua/bán tài sản.

## Nội dung skill / prompt

```
Bạn là 1 nhà phân tích vĩ mô, tư duy theo 2 khung kết hợp:

KHUNG 1 — "Chiến Tranh Tiền Tệ" (Song Hongbing): đọc sự kiện tiền tệ/tài chính qua lăng kính
địa chính trị — ai hưởng lợi, ai chịu thiệt khi 1 đồng tiền mạnh lên/yếu đi, khi 1 quốc gia
in tiền, khi vàng được các ngân hàng trung ương mua vào. Luôn hỏi: "câu chuyện chính thức nói
gì, và động cơ thực sự phía sau các bên có quyền lực là gì".

KHUNG 2 — "Big Cycle" (Ray Dalio): đọc qua 4 chu kỳ chồng lên nhau —
1. Chu kỳ nợ ngắn hạn (~5-10 năm, tương ứng chính sách tiền tệ nới lỏng/thắt chặt)
2. Chu kỳ nợ dài hạn (~75-100 năm, tích lũy nợ tới điểm không bền vững)
3. Chu kỳ chính trị nội bộ (khoảng cách giàu nghèo, phân cực chính trị)
4. Chu kỳ địa chính trị (cường quốc lên/xuống — hiện tại: Mỹ vs Trung Quốc)
Luôn định vị: "hiện đang ở giai đoạn nào trong 4 chu kỳ này, dấu hiệu nào cho thấy điều đó".

QUY TRÌNH trả lời 1 câu hỏi vĩ mô:
1. Sự kiện/hiện tượng là gì — mô tả khách quan, có số liệu nếu có
2. Áp Khung 2 trước: định vị vào chu kỳ nào, đang ở pha nào (nới lỏng/thắt chặt/bong bóng/suy thoái)
3. Áp Khung 1 sau: ai hưởng lợi, ai chịu thiệt, động cơ địa chính trị nào phía sau
4. Kết nối về Việt Nam: điều này ảnh hưởng gì tới tỷ giá VND, lãi suất, giá hàng nhập khẩu,
   ngành du lịch/hàng không (liên quan trực tiếp ABTRIP)
5. QUAN TRỌNG: luôn phân biệt rõ "đây là cách đọc bối cảnh" vs "đây là dự đoán/khuyến nghị đầu
   tư" — không đưa ra khuyến nghị mua/bán tài sản cụ thể, chỉ giải thích cơ chế.

Giọng văn cho content GMSP: kể chuyện, có ví dụ lịch sử cụ thể (khủng hoảng 1929, 1997 châu Á,
2008), không dùng thuật ngữ khô khan không giải thích — mọi thuật ngữ (WACC, chu kỳ nợ, reserve
currency...) phải có 1 câu giải nghĩa ngay khi xuất hiện lần đầu.
```

## Setup từng bước
1. Copy nội dung prompt trên làm system prompt riêng, hoặc dùng như 1 skill trong Claude Code
   (lưu thành `SKILL.md` trong `.claude/skills/tu-duy-tai-chinh-vi-mo/`).
2. Với GMSP: kết hợp với research thật (search tin tức kinh tế mới nhất) trước khi viết script,
   skill này chỉ cho KHUNG tư duy, không thay thế việc kiểm tra số liệu hiện tại.
3. Muốn có data trực quan đi kèm (biểu đồ chu kỳ nợ Mỹ từ 1900): tham khảo thêm repo phụ trợ
   `SimSimButDifferent/debt-cycles-tracker` (dashboard số liệu FRED theo đúng khung Dalio) — chỉ
   4 stars, không có license rõ ràng, coi là nguồn tham khảo số liệu chứ không phải công cụ
   chính, tự verify số liệu trước khi dùng vào content.

## Ví dụ thực tế
Câu hỏi: "vì sao giá vàng tăng mạnh suốt 2025-2026". Áp skill:
- Khung 2: đang ở pha cuối chu kỳ nợ dài hạn (nợ công nhiều nước ở mức kỷ lục), ngân hàng trung
  ương nhiều nước tăng mua vàng để giảm phụ thuộc USD.
- Khung 1: vàng là "đồng tiền phi tín dụng" duy nhất trong nhóm dự trữ lớn — các nước muốn giảm
  rủi ro bị đóng băng tài sản (như đã xảy ra với Nga) chuyển dự trữ từ trái phiếu USD sang vàng.
- Kết nối VN: tỷ giá VND/USD chịu áp lực gián tiếp, giá vàng trong nước thường biến động mạnh
  hơn thế giới do chênh lệch cung-cầu nội địa — đây là góc content GMSP có thể khai thác dễ hiểu
  cho khán giả 30-40 tuổi.

## Lưu ý / Lỗi thường gặp
- Đây là KHUNG DIỄN GIẢI, không phải dự báo chính xác — Dalio cũng thừa nhận xác định đúng giai
  đoạn chu kỳ cực khó, kể cả tổ chức chuyên nghiệp cũng thường sai. Content phải nói rõ đây là
  góc nhìn phân tích, không phải lời tiên tri.
- "Chiến Tranh Tiền Tệ" (Song Hongbing) có phần nội dung mang tính thuyết âm mưu, gây tranh cãi
  học thuật — dùng như 1 LỐI KỂ CHUYỆN hấp dẫn cho content, không trình bày như sự thật tuyệt
  đối; nên có disclaimer nhẹ khi content động tới phần nhạy cảm (thuyết âm mưu tài chính).
- Không dùng skill này để đưa khuyến nghị đầu tư/mua bán tài sản cụ thể cho khán giả — đây là
  ranh giới pháp lý/đạo đức content tài chính, vi phạm dễ bị flag trên các nền tảng.

## Đánh giá cá nhân
- Điểm mạnh: đúng khoảng trống cho content GMSP (kinh tế + kể chuyện dễ hiểu), khác biệt hẳn
  với tư duy tài chính doanh nghiệp đã có ở ops-finance; kết hợp 2 khung bổ trợ nhau (số liệu hệ
  thống của Dalio + lối kể chuyện địa chính trị của Song Hongbing) ra sản phẩm content hấp dẫn.
- Điểm yếu: là framework tự viết, không phải công cụ đo lường khách quan — chất lượng phụ thuộc
  hoàn toàn vào việc research số liệu thật đi kèm mỗi lần dùng; phần "Chiến Tranh Tiền Tệ" có rủi
  ro thiên về thuyết âm mưu nếu không cân bằng bằng số liệu thật.
- Có nên dùng không: 7.5/10 cho mục đích content GMSP — không dùng cho quyết định tài chính
  doanh nghiệp thật (đã có ops-finance riêng cho việc đó).

## Link
- Cảm hứng: "Chiến Tranh Tiền Tệ" — Song Hongbing (sách, không có repo/link chính thức)
- Cảm hứng: "Principles for Navigating Big Debt Crises" — Ray Dalio, https://www.economicprinciples.org
- Repo phụ trợ (data, không phải core skill): https://github.com/SimSimButDifferent/debt-cycles-tracker

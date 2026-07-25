---
name: local-gap-finder
description: >
  Tìm khoảng trống thị trường cho local business bằng cách cross-reference đối thủ,
  tiếng nói khách hàng, và demand thật theo địa lý. Dùng khi Nobitano hỏi "đối thủ quanh
  đây đang làm gì", "còn chỗ trống nào chưa ai fill", "mình định giá đúng chưa", hoặc khi
  Focus Mode chạy cho domain loại local business (ABTRIP/An Bình, Tano Cafe).
  Trigger mạnh với: "gap thị trường", "đối thủ local", "định giá", "khoảng trống", tên
  domain local business cụ thể.
---

# Local Gap Finder — Market Gap cho Local Business

Nguồn cảm hứng: cấu trúc 6-module "Research Director" (Structure Webworks) — đã gộp vào
kiến trúc Scout → Validator → Analyst → Synthesizer sẵn có của `research-analytics-pro`,
không tạo pipeline song song.

**Không dùng skill này cho:** research vĩ mô/đa ngành (dùng skill `research-synthesis` +
`market-sizing` như bình thường) hoặc domain không phải local business (Trùm Sân Bay,
Airfare Decoded, GMSP, kênh AI review — các domain này không cạnh tranh theo địa lý).

---

## Bước 1 — Scout: thu thập 3 nguồn raw (chạy song song)

**Competitor Offer Matrix (tương đương M01):**
```
Liệt cột: mình + 2-4 đối thủ gần nhất (theo địa lý, cùng phân khúc)
Liệt hàng: từng thuộc tính offer (gói dịch vụ, giá, bundle, financing/trả góp,
           warranty/bảo hành, dịch vụ phụ, giờ hoạt động...)
Đánh dấu có/không mỗi ô
→ Hàng nào TOÀN TRỐNG (không ai có) = gap ứng viên, đưa sang Bước 3
```
Nguồn: Google Maps/GBP (giờ, review, ảnh menu/bảng giá), website đối thủ, fanpage.

**Customer Voice Mining (tương đương M02):**
```
Quét review Google/Trustpilot/social CỦA MÌNH và CỦA ĐỐI THỦ
Phân loại từng câu thành 1 trong 3 nhóm:
  Pain       → khách phàn nàn cái gì
  Objection  → khách chần chừ vì lý do gì trước khi mua/dùng
  Buying     → tín hiệu khách sẵn sàng trả tiền cho cái gì
```
Nguồn: Google review, Trustpilot, comment Facebook/Instagram/TikTok, Reddit nếu có thread liên quan.

**Local Demand Radar (tương đương M03):**
```
Google Trends: search volume theo từ khoá "<dịch vụ> + <địa danh>" / "near me"
Google Maps: mật độ + rating trung bình đối thủ trong bán kính phục vụ
Google Ads Keyword Planner (nếu có access) hoặc ước lượng qua Trends relative volume
```

## Bước 2 — Analyst: xử lý thành số đo được

**Pricing & Offer Position (tương đương M04):**
```
So giá/gói mình vs trung bình thị trường (từ ma trận Bước 1)
Kết luận 1 trong 3: DƯỚI thị trường / NGANG thị trường / TRÊN thị trường
Nếu dưới → còn room tăng giá; nếu trên → cần justify bằng giá trị rõ ràng
```

**Trend Forecaster (tương đương M06):**
```
Từ chuỗi search volume Local Demand Radar theo thời gian → xu hướng tăng/giảm/ổn định
Dùng skill statistical-analysis / repos/google-timesfm.md nếu cần forecast ngắn hạn
Không bịa số — nếu data quá thưa để forecast, ghi rõ "không đủ data, chỉ mô tả xu hướng quan sát được"
```

## Bước 3 — Synthesizer: Market Gap Score (tương đương M05, phần lõi)

```
Gap Score = Demand (Bước 1 Radar) × Margin Room (Bước 2 Pricing) ÷ Mật độ cạnh tranh (Bước 1 Matrix)

Với mỗi gap ứng viên từ Ma trận (hàng trống) VÀ mỗi pain/objection lặp lại ≥3 lần trong
Customer Voice Mining → tính Gap Score, xếp hạng.

Output = RANKED OPPORTUNITY LIST:
| Cơ hội | Demand | Cạnh tranh | Margin room | Gap Score | Khuyến nghị hành động |
|--------|--------|-----------|-------------|-----------|------------------------|
| ...    | Cao/TB/Thấp | Cao/TB/Thấp | Cao/TB/Thấp | 1-10 | 1 câu cụ thể |
```

Nguyên tắc `data-storytelling` áp dụng: mỗi dòng phải có khuyến nghị hành động cụ thể,
không dừng ở mô tả số liệu.

---

## Output cuối — khớp format Executive Summary chuẩn của research-analytics-pro

```
Executive Summary (3 câu — gap lớn nhất là gì, vì sao, nên làm gì trước)
→ Competitor Offer Matrix (bảng đầy đủ)
→ Customer Voice Summary (top pain/objection/buying signal)
→ Ranked Opportunity List (bảng Gap Score)
→ Khuyến nghị hành động — cụ thể, theo priority
→ Phụ lục nguồn
```

## Khi chạy trong Focus Mode (xem `FOCUS-MODE.md`)

Nếu đây là lần chạy thứ ≥2 cho cùng 1 pack → BẮT BUỘC so sánh với report tuần trước
(`/reports/<pack>/`): gap nào đã bị đối thủ fill, gap nào mới xuất hiện, ranking đổi thế nào.
Không viết lại từ đầu như research mới.

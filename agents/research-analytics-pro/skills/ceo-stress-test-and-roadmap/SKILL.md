---
name: ceo-stress-test-and-roadmap
description: >
  Sau khi có Full Report (8 phần) hoặc Research Brief, chạy 2 bước tiếp theo:
  (A) Stress-test báo cáo dưới góc nhìn CEO — bắt lỗi kết luận nguỵ trang
  thành sự thật, thiếu sensitivity analysis, thiếu chi phí, thiếu baseline
  nội bộ; (B) Biến verdict đã qua stress-test thành roadmap triển khai theo
  giai đoạn, mỗi giai đoạn có cổng go/no-go rõ ràng trước khi rót thêm nguồn
  lực. Dùng ngay sau bất kỳ báo cáo nghiên cứu nào chuẩn bị dùng để RA QUYẾT
  ĐỊNH ĐẦU TƯ THẬT — không dùng cho báo cáo chỉ để biết thông tin.
---

# CEO Stress-Test & Roadmap — Từ báo cáo tới hành động

## TL;DR
1 báo cáo nghiên cứu tốt vẫn có thể dẫn tới quyết định sai nếu đọc như "sự thật đóng gói sẵn" thay vì bị stress-test trước. Skill này chạy 2 bước: (A) đóng vai CEO xé nhỏ báo cáo tìm lỗ hổng, (B) biến verdict đã vá thành kế hoạch triển khai từng giai đoạn có điểm dừng — không đầu tư full ngay chỉ vì báo cáo nói "nên làm".

## Khi nào dùng
- Ngay sau khi có Full Report/Research Brief (từ `research-synthesis`, khung 8 phần v4.3) và báo cáo đó sẽ dùng để quyết định đầu tư/triển khai thật
- KHÔNG dùng cho báo cáo chỉ để cập nhật thông tin, không dẫn tới quyết định rót nguồn lực
- Trước khi trình báo cáo cho Nobitano duyệt — chạy skill này trước để báo cáo tới tay Nobitano đã "cứng" hơn, ít lỗ hổng hơn

## Nội dung skill / prompt

### PHẦN A — CEO Stress Test (checklist bắt lỗi, chạy trên báo cáo đã có)

Đọc lại toàn bộ báo cáo, tự hỏi 5 câu sau — có ít nhất 1 câu "có vấn đề" là phải sửa trước khi trình:

**1. Hypothesis-vs-Conclusion check**
Khuyến nghị trong Phần 7 có được viết như "sự thật chắc chắn" trong khi thực ra dựa trên 1 giả định CHƯA kiểm chứng không? Nếu có → tách rõ 2 việc: "hướng đi chiến lược đúng" (kết luận vững) vs "nên đầu tư full ngay" (thường KHÔNG vững nếu chưa test) — đây là 2 quyết định khác nhau, đừng gộp làm một.

**2. Sensitivity Analysis check**
Tìm con số giả định nào mà TOÀN BỘ kết luận "đáng làm/không đáng làm" phụ thuộc vào nó (thường là 1 tỷ lệ % chuyển đổi/% sẵn sàng chi trả chưa có nguồn xác nhận). Nếu tìm thấy mà báo cáo chưa show sensitivity → bắt buộc thêm bảng: giá trị đó thay đổi trong dải hợp lý (vd 1%-8%) thì kết luận thay đổi ra sao. Nếu kết luận đổi mạnh theo giả định → đây là tín hiệu "cần validate trước khi tin", không phải "cứ làm theo báo cáo".

**3. Cost/Investment estimate check**
Báo cáo có nói tới quy mô cơ hội (TAM/SAM/SOM, doanh thu tiềm năng) mà KHÔNG có ước tính chi phí để đạt được nó không? Không có chi phí thì không tính được ROI — "cơ hội lớn" mà chưa biết tốn bao nhiêu để lấy được là câu chuyện chưa đầy đủ. Thêm bảng chi phí theo hạng mục (dù thô, gắn rõ label "ước tính, cần báo giá thật"), đừng để trống.

**4. Baseline/Internal-data check**
Báo cáo research thị trường "từ đầu" như công ty chưa có gì, trong khi thực ra đã có dữ liệu nội bộ (doanh thu hiện tại, khách hàng hiện tại, vận hành đang chạy) chưa được dùng để so sánh? Nếu có → dừng lại, liệt kê CHÍNH XÁC cần dữ liệu nội bộ gì, xin người có thẩm quyền cung cấp — KHÔNG tự bịa số để lấp chỗ trống này.

**5. Verdict-mixing check**
Verdict cuối bài có đang trộn "định hướng chiến lược" với "quyết định rót tiền" thành 1 câu không? Tách thành 2 dòng riêng biệt, rõ ràng cái nào vững, cái nào cần thêm điều kiện mới nên làm.

### PHẦN B — Roadmap triển khai theo giai đoạn (chạy sau khi Phần A đã vá xong)

Không bao giờ đề xuất "đầu tư full ngay" cho báo cáo mới qua Phần A còn giả định chưa kiểm chứng. Cấu trúc chuẩn 4 giai đoạn:

```
GIAI ĐOẠN 0 — Validate rẻ (vài tuần, chi phí gần 0)
  Mục tiêu: trả lời đúng những câu hỏi Phần A vừa lật ra (baseline, sensitivity, chi phí thật)
  Công cụ: phỏng vấn nhanh (primary-research-design), landing page test, gọi thử giá đối thủ
  → Cổng: đạt ngưỡng cụ thể mới sang Giai đoạn 1 (không mơ hồ "nếu thấy ổn")

GIAI ĐOẠN 1 — MVP thủ công (1-2 tháng, chi phí thấp)
  Mục tiêu: test giả thuyết với khách/thị trường THẬT, chưa cần công nghệ/hệ thống
  Đo lường: chỉ số so sánh trực tiếp với baseline (vd AOV mới vs AOV cũ)
  → Cổng: chỉ số đạt ngưỡng đủ để bõ công đầu tư tiếp

GIAI ĐOẠN 2 — Tự động hoá MỘT PHẦN (2-3 tháng)
  Mục tiêu: giảm phụ thuộc thao tác tay, CHỈ tự động hoá phần có ROI rõ nhất
  Nguyên tắc: không tự động hoá toàn bộ ngay — phần nào chưa chắc, giữ thủ công
  → Cổng: hệ thống ổn định qua thời gian đủ dài + volume đủ lớn để mở rộng

GIAI ĐOẠN 3 — Mở rộng (6-12 tháng+)
  Chỉ tới đây SAU KHI 2 giai đoạn trước đều pass — không nhảy cóc
```

Mỗi giai đoạn PHẢI có:
- Bảng việc cụ thể + ai làm (map vào role/agent đã có sẵn trong tổ chức, không tự tạo role mới trừ khi thật sự cần)
- Cổng quyết định (go/no-go) viết dưới dạng ngưỡng đo được, không viết mơ hồ ("nếu thấy tốt")
- Bảng rủi ro THỰC THI (khác rủi ro thị trường đã có trong báo cáo gốc — đây là rủi ro về CÁCH làm, không phải rủi ro về thị trường)

### Tóm tắt bắt buộc cuối cùng

Nếu người ra quyết định chỉ đọc 1 đoạn: tách rõ **việc cần làm NGAY** (luôn là Giai đoạn 0, rẻ, ít rủi ro) khỏi **việc chờ điều kiện** (Giai đoạn 2-3, chỉ làm khi giai đoạn trước đã chứng minh được).

## Setup từng bước
1. Có báo cáo/verdict cần dùng để quyết định đầu tư thật → chạy Phần A trước
2. Với mỗi câu hỏi Phần A ra "có vấn đề" → sửa trực tiếp vào báo cáo (thêm bảng, tách câu, xin dữ liệu), tăng version báo cáo, ghi rõ khác biệt so với bản trước
3. Báo cáo đã qua Phần A → chạy Phần B, viết thành file kế hoạch riêng (không nhét vào báo cáo gốc, giữ 2 tài liệu tách biệt: "hiểu thị trường" vs "làm gì tiếp")
4. Trình cả 2 file cho người quyết định — báo cáo đã stress-test + roadmap có cổng dừng

## Ví dụ thực tế
Áp cho báo cáo thị trường Fast Track Nội Bài (ABTRIP): Phần A phát hiện 4 vấn đề (verdict "bundle" viết như chắc chắn dù chưa test, thiếu sensitivity cho giả định 5%, thiếu chi phí Duffel, thiếu baseline doanh thu hiện tại) → sửa thành v2 báo cáo. Phần B biến verdict đã vá thành 4 giai đoạn (Validate → MVP thủ công → Tự động 1 phần → Mở rộng), mỗi giai đoạn map vào đúng agent Mission Control đã có (Sales & BD Lead, Content & Delivery Lead, Automation & Ops Lead), có cổng đo được cụ thể (AOV bundle > mua rời 15-20%).

## Lưu ý / Lỗi thường gặp
- Đừng chạy Phần B trước khi xong Phần A — roadmap dựng trên báo cáo còn lỗ hổng sẽ thừa hưởng luôn lỗ hổng đó (garbage in, garbage out)
- Cổng quyết định viết mơ hồ ("nếu kết quả tốt") là vô dụng — phải là con số/ngưỡng cụ thể quyết được trước khi bắt đầu giai đoạn, không phải nghĩ ra sau khi đã có kết quả (tránh tự lừa dối bằng cách hạ chuẩn sau khi thấy kết quả không như ý)
- Không phải mọi giai đoạn đều cần đủ 4 bước — báo cáo nhỏ/rủi ro thấp có thể gộp Giai đoạn 0+1, đừng máy móc áp đủ 4 giai đoạn cho quyết định nhỏ
- Baseline nội bộ là thứ duy nhất Phần A không tự làm được — đây luôn phải xin người có thẩm quyền, tuyệt đối không suy đoán thay

## Đánh giá cá nhân
- Điểm mạnh: buộc tách rõ "báo cáo hay" khỏi "quyết định đúng" — 1 báo cáo research xuất sắc vẫn có thể dẫn tới quyết định tồi nếu người đọc tin tưởng mù quáng vào kết luận mà không tự stress-test; roadmap có cổng dừng bảo vệ khỏi việc đâm lao theo lao
- Điểm yếu: thêm 2 bước sau báo cáo gốc, tốn thêm thời gian — không đáng làm cho quyết định nhỏ, rủi ro thấp
- Có nên dùng: 9/10 cho MỌI báo cáo dẫn tới quyết định đầu tư nguồn lực thật (tiền, người, thời gian) — không cần cho báo cáo chỉ để biết thông tin

## Link
- Tham chiếu: `agents/research-analytics-pro/system-prompt.md` (khung 8 phần v4.3, nguyên tắc FACT/ƯỚC TÍNH/GIẢ THUYẾT v4.1)
- Tham chiếu: `skills/primary-research-design` — công cụ dùng trong Giai đoạn 0 của Phần B

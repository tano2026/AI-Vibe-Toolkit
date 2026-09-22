# CLIENT ONBOARDING TEMPLATE — Bán giải pháp FDE cho khách không biết kỹ thuật
> Viết 22/08/2026. Đây là bản dịch "70% Primitives / 30% custom" (đã có
> trong forward-deployed-engineer-model + MASTER-TEMPLATE-MANIFEST.md)
> thành 1 quy trình bán hàng THẬT — khách không bao giờ thấy GitHub, code,
> hay thuật ngữ "Pro Agent"/"skill"/"EXPERT-CORE". Họ chỉ thấy kết quả.

## Nguyên tắc ngôn ngữ — đổi tên TRƯỚC KHI nói chuyện với khách

Khách không mua "AI Agent" — họ mua "phòng ban AI". Đổi tên hoàn toàn:

| Tên kỹ thuật (nội bộ) | Tên bán hàng (khách nghe) |
|---|---|
| Research Analytics Pro | Phòng Nghiên Cứu Thị Trường AI |
| Content Pro | Phòng Content AI |
| Sales-CEO | Phòng Kinh Doanh AI |
| Digital Marketing Agent | Phòng Marketing AI |
| Infra Ops Agent | Phòng Kỹ Thuật AI |
| Media Pro | Phòng Truyền Thông AI |
| Designer Pro | Phòng Thiết Kế AI |
| Customer Satisfaction Pro | Phòng Chăm Sóc Khách Hàng AI |
| EXPERT-CORE.md | (không nhắc tới — đây là "cách công ty tao làm việc", khách không cần biết chi tiết) |

## Bước 1 — Intake (đúng Deepthink: hỏi TỪNG câu, không hỏi dồn)

```
Câu 1 (LUÔN LÀ CÂU ĐẦU): "Anh/chị muốn AI giúp việc gì TRƯỚC TIÊN?"
  → Đưa 8 lựa chọn bằng NGÔN NGỮ KINH DOANH (bảng trên), không nói
    "chọn Pro Agent nào" — khách chọn 1-2 phòng ban để bắt đầu,
    KHÔNG bán trọn gói 8 phòng ngay lần đầu (dễ ngợp, khó chốt)

Câu 2: "Anh/chị có website/fanpage không? Cho tao link"
  → Tự đọc (kiểu phân tích Pomelli đã làm thử với ABTRIP) để hiểu
    thương hiệu — KHÔNG bắt khách điền form dài về "tone giọng văn",
    "màu sắc thương hiệu" — tự suy ra, chỉ xác nhận lại với khách

Câu 3: "Anh/chị muốn nhận kết quả qua đâu — Zalo, Email, hay gặp
  trực tiếp?" → map vào 1 trong các Adapter đã có sẵn (Zalo Mini App/
  Chatwoot/Khoj/email) — khách chọn kênh họ QUEN, không phải học
  công cụ mới

Câu 4 (chỉ hỏi nếu cần): "Có việc gì tuyệt đối KHÔNG được AI tự làm
  không?" → đưa vào tenant-config phần compliance_overrides (không,
  đây vẫn là NGƯỠNG CỨNG từ EXPERT-CORE — câu này chỉ hỏi thêm giới
  hạn RIÊNG của khách, không phải hạ chuẩn)
```

## Bước 2 — Dựng "phòng ban" (nội bộ, khách không thấy)

```
1. Brand playbook — viết theo khuôn content-brand-playbooks.md, dựa
   trên website/fanpage đã đọc ở Câu 2
2. tenant-config.json — theo schema MASTER-TEMPLATE-MANIFEST.md,
   bật đúng 1-2 "phòng ban" khách chọn, tắt 6-7 phòng còn lại
3. KHÔNG đụng vào CORE (EXPERT-CORE + skill riêng từng Pro Agent) —
   chỉ thêm brand playbook + tenant-config, đúng luật 70%/30%
4. Setup Adapter đúng kênh khách chọn (Zalo/Chatwoot/Khoj/email)
```

## Bước 3 — Giao kết quả đầu tiên (nhanh nhất có thể)

```
Không giao "hệ thống AI đã cài xong" — giao THẲNG 1 kết quả cụ thể:
  Phòng Content AI → 3 bài content mẫu theo đúng brand
  Phòng CSKH AI → báo cáo phân loại 10 tin nhắn gần nhất
  Phòng Kinh Doanh AI → 5 lead đã chấm điểm sẵn

Khách THẤY GIÁ TRỊ trước khi bàn tới hợp đồng dài hạn — đúng chiến
lược "cho khách xem 1 miếng bánh trước khi bán cả cái bánh"
```

## Bước 4 — Báo cáo định kỳ (dùng critical-path-briefing)

```
Khách CHỈ nhận báo cáo những gì CẦN QUYẾT ĐỊNH CỦA HỌ — không nhận
log kỹ thuật, không nhận "Content Pro đã chạy xong task số 47"

Đúng mẫu: "Tuần này phòng Content AI đã viết 5 bài, 2 bài cần anh/chị
duyệt trước khi đăng (đính kèm), 3 bài đã đăng theo lịch đã thống nhất"
```

## Định giá — theo Outcome, không theo "số Agent"

```
KHÔNG báo giá "8 Pro Agent x giá mỗi cái" — báo giá theo GÓI PHÒNG BAN:
  Gói 1 phòng ban (khởi động)  → giá thấp nhất, test trước
  Gói 3 phòng ban (phổ biến)   → combo hay đi cùng nhau (vd Content +
                                  Marketing + CSKH)
  Gói Full (8 phòng ban)       → giá cao nhất, đúng mô hình FDE —
                                  bán như "thuê nguyên 1 team ngoài"
```

## Việc CHƯA làm — nói thẳng

- Chưa test với khách thật nào — đây là quy trình thiết kế, chưa vận hành thật lần nào
- Chưa có mức giá cụ thể (VNĐ) cho từng gói — cần Nobitano tự định giá theo thị trường, không tự bịa số
- Pomelli-style brand extraction ở Câu 2 — đã test thử với ABTRIP nhưng bị giới hạn kỹ thuật (không đọc được SPA), cần quy trình thay thế thật (Nobitano tự chạy Pomelli, hoặc hỏi trực tiếp)

# Brand Strategy Sprint — 1 tool, 3 bước tuần tự, 1 tài liệu

## TL;DR
Gộp Bước 1-3 (lấy thông tin → thống nhất giọng điệu/định dạng → lập kế hoạch triển khai)
thành 1 phiên hội thoại liên tục, không cần nhiều agent riêng — vì đây là quy trình làm
1 lần/khách, không lặp lại như Bước 4. Ra 1 tài liệu duy nhất: Brand Strategy Report (docx).
Bước 4 (triển khai + đo lường) KHÔNG nằm trong skill này — bàn giao sang pipeline agent
đã có sẵn (`agents/trum-san-bay/orchestrator.py`, generalize multi-tenant).

## Vì sao 1 tool là đủ, không cần tách agent
3 bước đầu có đặc điểm: làm tuần tự, không branching phức tạp, không cần tool bên ngoài
(không gọi API, không ghi data ngoài Airtable cuối cùng), và chỉ chạy 1 lần khi onboard
khách mới. Tách thành nhiều agent chỉ tạo thêm overhead điều phối không cần thiết. Bước 4
mới thật sự cần multi-agent vì nó lặp lại hàng ngày, cần validator/guardrail, và gọi nhiều
tool ngoài (Postiz, Pollinations) — đó là lý do `trum-san-bay` pipeline đã tách riêng.

---

## BƯỚC 1 — Discovery (lấy thông tin tổng thể)

Gồm 2 phần chạy song song, không phần nào thay thế phần kia:

### 1a. Phỏng vấn khách (Brand Discovery Session)
Dùng lại `agents/trum-san-bay/skills/brand-discovery-session/SKILL.md` đã có sẵn trong kho
— phương pháp laddering + 5 Whys, không viết lại. Áp dụng cho khách mới thay vì chỉ dùng
cho Trùm Sân Bay.

Lấy đủ 4 nhóm: bản thân & mục tiêu · nỗi đau & mong muốn · hình tượng hướng đến · tư liệu
có sẵn (mẫu content cũ nếu có).

### 1b. Channel Audit — nghiên cứu toàn bộ kênh social khách đang có
Trước khi hỏi khách muốn giọng điệu/định dạng gì (Bước 2), phải biết THỰC TẾ khách đang có
gì — vì cái khách "muốn" và cái đang thật sự work có thể khác nhau, và channel cũ là nguồn
dữ liệu thật, không phải suy đoán.

**Quy trình:**
1. Hỏi khách liệt kê toàn bộ kênh đang có: Facebook, TikTok, Instagram, YouTube, Zalo,
   website, kể cả kênh không hoạt động lâu rồi — không bỏ sót kênh "phụ"
2. Với mỗi kênh đang hoạt động, research:
   - Loại content nào đăng nhiều nhất, loại nào tương tác tốt nhất (so sánh, không đoán)
   - Giọng văn/tone hiện tại — có nhất quán giữa các kênh không hay mỗi nơi 1 kiểu
   - Tần suất đăng thực tế, khoảng nghỉ dài bất thường (dấu hiệu quá tải/mất động lực)
   - Đối tượng follow thực tế qua comment/tương tác — có khớp target khách mô tả ở 1a không
3. Với kênh đối thủ trực tiếp khách nhắc tới (nếu có) — audit nhanh tương tự, dùng làm đối
   chiếu định vị (khác gì, hơn gì, kém gì)
4. Nếu khách CHƯA có kênh nào (bắt đầu từ 0) → bỏ qua bước audit, note rõ "chưa có dữ liệu
   kênh cũ, Bước 2 dựa hoàn toàn vào câu trả lời phỏng vấn 1a"

⛔ Guardrail: audit chỉ mô tả PATTERN quan sát được (loại content, tần suất, tone), không
suy diễn ĐỘNG CƠ hay đánh giá chủ quan "content dở/hay" — để dữ liệu tự nói, khách và Bước 2
sẽ diễn giải cùng nhau.

**Output 1b:** bảng tổng hợp theo kênh — loại content hiệu quả nhất, tone hiện tại, tần suất,
khoảng trống (kênh nào bỏ hoang, định dạng nào chưa thử).

**Vì sao cần cả 1a lẫn 1b:** 1a cho biết khách MUỐN gì, 1b cho biết THỰC TẾ đang có gì và
cái gì đã chứng minh work. Bước 2 đối chiếu cả hai — nếu khách muốn 1 hướng nhưng dữ liệu
kênh cũ cho thấy hướng khác đang work tốt hơn, đây là điểm phải hỏi lại khách, không tự
chọn thay khách.

**Output tổng Bước 1:** transcript + tóm tắt 1a đã khách xác nhận đúng, GHÉP với bảng audit
1b — cả hai cùng là input cho Bước 2.

## BƯỚC 2 — Alignment (thống nhất giọng điệu, từ ngữ, định dạng, mô hình phát triển)

Từ dữ liệu Bước 1 (cả 1a phỏng vấn lẫn 1b audit kênh cũ), tổng hợp và **đề xuất lại cho
khách xác nhận** (không tự quyết). Nếu 1b cho thấy dữ liệu thật mâu thuẫn với mong muốn ở
1a — nêu rõ mâu thuẫn này với khách trước, để khách quyết định hướng nào ưu tiên, không tự
chọn thay:

- **Giọng điệu:** trang trọng/casual, năng lượng cao/điềm tĩnh, hài hước mức nào
- **Từ ngữ:** thuật ngữ chuyên ngành dùng được không, từ cấm/nhạy cảm
- **Định dạng ưu tiên:** text/ảnh/carousel/video — dựa trên nguồn lực khách có (không đề
  xuất video nếu khách không quay được, không đề xuất avatar AI nếu ngân sách không có)
- **Mô hình phát triển:** tăng trưởng chậm-chắc (organic, không ads) hay tăng tốc (có ngân
  sách ads/boost) — quyết định này ảnh hưởng trực tiếp lịch trình Bước 3-4

⛔ Guardrail: mọi đề xuất phải trích dẫn được từ câu trả lời Bước 1, không suy diễn ngoài.

**Output bước 2:** bảng thống nhất giọng điệu + định dạng + mô hình, khách xác nhận từng mục.

## BƯỚC 3 — Implementation Plan (kế hoạch triển khai: công cụ, nguồn lực, kỹ năng)

Dùng khung Capability Map (Não/Tay/Cơ) — nhưng khác Agentic Factory ở chỗ đây là kế hoạch
**cho khách hiểu và duyệt ngân sách**, không phải bảng kỹ thuật nội bộ:

| Cần gì | Map sang |
|---|---|
| Kỹ năng/nghiệp vụ cần (Não) | Content pillar nào cần kiến thức chuyên sâu gì, ai review fact-check |
| Công cụ (Tay) | Postiz (publish), Pollinations (ảnh) — liệt kê chi phí thật nếu có (Postiz/HeyGen...) |
| Nguồn lực (Cơ + con người) | Thời gian khách cần duyệt bài/tuần, có cần thuê ngoài quay video không |
| Timeline | 30-60-90 ngày, mốc nào review lại chiến lược |

**Output bước 3:** bảng ngân sách + timeline + phân công rõ ai làm gì (agent tự động làm gì,
khách cần làm gì) — đây là phần khách hàng "mua", phải rõ ràng dễ hiểu.

---

## Chốt phiên — xuất Brand Strategy Report (docx)

Dùng skill `docx` có sẵn. Cấu trúc: Trang bìa → Discovery Summary (Bước 1) → Voice & Format
Standard (Bước 2) → Implementation Plan (Bước 3) → Trang xác nhận khách duyệt.

⛔ Checkpoint bắt buộc: KHÔNG bàn giao sang Bước 4 (pipeline tự động) cho tới khi khách ký
xác nhận report này.

## Bàn giao sang Bước 4
Sau khi khách duyệt: tạo brand-config (theo Bước 2-3 đã chốt) cho khách này trong hệ thống
multi-tenant của `agents/trum-san-bay/`, kích hoạt pipeline Ideation → Writer → Visual →
Adapter → Review Queue → Publisher (Postiz) đã có sẵn — không dựng pipeline mới.

## Output cuối cùng của toàn bộ skill này
1 file docx (Brand Strategy Report) + 1 brand-config sẵn sàng nạp vào pipeline tự động.

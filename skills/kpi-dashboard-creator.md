# KPI Dashboard Creator — Build dashboard cho quyết định, không phải trang trí

## TL;DR
Khung thiết kế dashboard HTML/web app tập trung vào việc trả lời 4 câu hỏi thao tác: khỏe không? nghẽn ở đâu? cái gì vừa thay đổi? nên làm gì tiếp — thay vì nhồi hết mọi số liệu có sẵn lên màn hình cho đẹp.

> **Lưu ý phân biệt:** kho đã có `dashboard-builder` (dùng cho Grafana/SigNoz — dashboard giám sát hạ tầng/metrics kỹ thuật). Skill này khác phạm vi: dùng cho dashboard sản phẩm/kinh doanh (KPI content, doanh thu, booking) — không trùng, bổ trợ nhau theo use case.

## Skill này dùng để làm gì
Trước khi code: xác định "metric contract" cho từng số liệu — định nghĩa chính xác, đơn vị, nguồn, tần suất refresh, baseline so sánh, cao/thấp là tốt, và trạng thái khi thiếu/trễ/lỗi data. Không tự bịa số để màn hình trông đầy đủ — nếu là prototype dùng sample data thì phải ghi rõ.

Quy trình build: xác định hierarchy thông tin (filter/freshness trên cùng → KPI quyết định trước → trend/breakdown/chi tiết sau) → chọn đúng loại chart theo câu hỏi (line=xu hướng theo thời gian, bar=so sánh nhóm, scatter=quan hệ/outlier, table=giá trị chính xác) → implement đủ trạng thái loading/empty/error/stale → verify với label dài, giá trị 0, giá trị âm, mobile width.

## Setup từng bước
1. Trước khi build dashboard mới — liệt kê rõ từng metric theo "metric contract" (định nghĩa, nguồn, refresh time) trước khi động vào layout
2. Ưu tiên tái dùng framework/component đã có trong repo (React/Tailwind hiện tại) thay vì tạo stack mới
3. Test với dữ liệu thật có case xấu: 0 view, số âm, tên dài, thiếu data — không chỉ test với data đẹp

## Ví dụ thực tế
**Case:** Mở rộng Mission Control dashboard (đang chạy tại `127.0.0.1:3100`) thêm 1 view KPI content — trước khi code, viết metric contract:
| Metric | Định nghĩa | Nguồn | Refresh | Baseline |
|---|---|---|---|---|
| Video/tuần | Số script video publish trong 7 ngày | GitHub content/ folder count | Mỗi lần push | So với tuần trước |
| Zalo OA lead | Số lead capture qua Zalo OA | Zalo OA Manager (thủ công, chưa có API do bot offline) | Thủ công cập nhật | So với target sprint 2 tuần |

→ Layout: KPI quyết định (video/tuần, lead) đặt trên cùng, trend chart bên dưới, note rõ "Zalo OA lead: cập nhật thủ công do bot đang offline" thay vì để trống gây hiểu nhầm là 0.

## Lưu ý / Lỗi thường gặp
- Dễ nhầm với `dashboard-builder` đã có trong kho (dashboard đó cho Grafana/SigNoz monitoring hạ tầng) — cái này cho dashboard sản phẩm/business, khác mục đích, đừng lẫn khi search
- Rule "không bịa số để đẹp" rất quan trọng khi demo — dễ bị bỏ qua lúc vội, cần nhắc rõ label "sample data" nếu dùng data giả

## Đánh giá cá nhân
- Điểm mạnh: nguyên tắc "metric contract trước khi code" giúp tránh trường hợp dashboard đẹp nhưng số liệu vô nghĩa/không nhất quán; checklist trạng thái loading/empty/error đầy đủ
- Điểm yếu: không có gì đặc thù kỹ thuật, chủ yếu là UX/product thinking chung; trùng tên gây nhầm với dashboard-builder đã có, phải note rõ
- Có nên dùng không: 5/10 — tham khảo tốt khi mở rộng Mission Control dashboard, nhưng không phải capability mới, kho đã có ui-component-forge mạnh hơn về mặt thực thi UI

## Link
- Nguồn gốc skill: adapted từ bundle [Rylaispirit/rylai-codex-hermes-skills](https://github.com/Rylaispirit/rylai-codex-hermes-skills) (clean-room-original)

---

## 🤖 Agent Integration

### Hermes (Python)
> Không áp dụng trực tiếp — đây là hướng dẫn build UI (JS/React), không phải task Hermes (Python executor) làm.

### OpenClaw
> Có thể dùng system prompt này khi giao OpenClaw task mở rộng Mission Control dashboard.

### Antigravity
> Không cần deploy riêng — dashboard build ra vẫn deploy qua quy trình hiện có của Mission Control (`127.0.0.1:3100`).

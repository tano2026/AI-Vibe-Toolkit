# OPC-ROSTER — Đội hình agent của OPC `{{slug}}`

> Chọn từ **9 agent thật của ORG v3** (`agents/company/ORG-v2.md`). Không thêm agent thứ 10: nhu cầu mới đi qua
> gói mở rộng (extension pack) nạp vào agent có sẵn. Lõi 9 agent không sửa khi thêm client; sửa lõi là thay đổi công ty, phải qua CEO.
> Mỗi agent dưới đây có đủ bốn thứ JD, KPI, SOP, Escalation; thiếu một thứ là chưa được nhận việc.

## Cấu hình OPC

- **Domain Pack:** `domain-packs/{{slug}}/PACK.md` (mọi delegation phải có header `[PACK: {{slug}}]`)
- **Nguồn doanh thu:** {{doanh_thu_list}}
- **Kênh:** {{kenh_list}}
- **Gói mở rộng yêu cầu:** {{goi_list}}
- **Vessel/runtime:** theo cột "Runtime" bên dưới, lấy từ bảng phân công ORG v3. Hermes là bộ não (agent `ceo`); OpenClaw là tay chân thực thi, không tự quyết, không có kênh nhận lệnh riêng.
- **Tier LLM:** cheap (DeepSeek V3), balanced (Gemini Flash), reasoning (DeepSeek R1), creative (Claude Sonnet, chỉ khi chất lượng chữ quyết định). Nâng tier phải ghi lý do trong brief (mức L1). Ghi chú: ORG v3 không ghi tier cho agent `ceo`; giá trị dưới đây là suy ra của công cụ, CEO xác nhận.

## Bảng đội hình

| Agent | Bật | Runtime | Tier LLM | Package tham chiếu | KPI chính (tuần) |
|---|---|---|---|---|---|
{{ROSTER_TABLE}}

## Chi tiết từng agent (JD / KPI / SOP / Escalation)

KPI mục tiêu bằng số: `CHƯA CÓ — hỏi CEO` cho tới khi có số nền sau hai tuần chạy nháp. Công cụ không đặt số.

{{AGENT_SECTIONS}}

## Gói mở rộng

{{EXT_PACKS}}

## Cách nạp agent (ORG v3, không đổi)

`ceo` (Hermes) lấy ba thứ rồi nhúng vào tin giao việc: (1) package tham chiếu của agent, (2) section tương ứng trong
`agents/company/EXPERT-CORE.md`, (3) Domain Pack `domain-packs/{{slug}}/PACK.md`. Gói mở rộng nạp THÊM khi task khớp, không nạp mặc định.
Job đầu tiên luôn là `[PACK: {{slug}}] agent=research`: quét thị trường, đối thủ, kênh. Không agent nào chạy trước khi `research` nộp báo cáo nền.

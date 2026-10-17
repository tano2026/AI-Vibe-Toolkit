# OPC `{{slug}}` — {{ten_thuong_hieu}}

> Sinh bằng Agent Factory (`tools/agent_factory.py moi-opc`) ngày {{ngay}}.
> Trạng thái: **khung NHÁP, chưa duyệt, chưa chạy gì.** Đây là bộ hồ sơ để dựng công ty một người
> từ các mục có sẵn trong kho, không phải hệ thống đang chạy. Mục `CHƯA CÓ — hỏi CEO` là thông tin
> con người phải điền.

## Mô tả

{{mo_ta}}

- **Nguồn doanh thu:** {{doanh_thu_list}}
- **Kênh:** {{kenh_list}}
- **Gói mở rộng:** {{goi_list}}
- **Kiến trúc:** mở rộng lõi ORG v3 (9 agent, `agents/company/ORG-v2.md`) bằng Domain Pack `domain-packs/{{slug}}/PACK.md`. Không thêm agent mới; nhu cầu mới đi qua gói mở rộng.
- **Nguồn chọn mục kho:** {{che_do_thu_kho}}

## Hồ sơ trong thư mục này

| File | Nội dung |
|---|---|
| `domain-packs/{{slug}}/PACK.md` | Domain Pack theo `domain-packs/_TEMPLATE.md` (phần lớn chờ CEO điền) |
| `OPC-ROSTER.md` | Chọn agent, runtime, tier LLM, KPI; JD/KPI/SOP/Escalation từng agent; gói mở rộng |
| `GATES.md` | Bảng cổng duyệt G1 đến G7, ba lằn ranh đỏ, luật vận hành |
| `airtable-schema.json` | Schema `company-hq` (7 bảng ORG v3) cộng bảng của gói mở rộng nếu có |
| `workflow-skeleton.md` | Luồng việc dạng văn bản cho người dựng n8n/Hermes |
| `PHASES.md` | Lộ trình bật theo pha, mốc đo để qua pha |
| `RISKS-LEGAL.md` | Bảng rủi ro và pháp lý để CEO điền (không tư vấn pháp lý) |
| `CAPABILITY-MAP.md`, `capability-map.json` | Mục kho chọn cho từng khả năng: chính, dự phòng, HỔNG |
| `INSTALL-PLAN.md` | Kế hoạch cài khô từ thủ kho (không thực thi) |
| `tests/` | Bộ test PASS/FAIL của OPC |
| `tenant-config.json` | Cấu hình khách theo schema TENANT-CONFIG; `compliance_overrides` luôn `null` |
| `HANDOVER.md` | Bàn giao: cách chạy, tên biến môi trường, runbook sự cố, cách dừng, việc còn nợ |

## CORE và TENANT-CONFIG

CORE (không đổi theo khách, không chứa tên thương hiệu hay màu): `GATES.md`, `workflow-skeleton.md`, `airtable-schema.json`, `OPC-ROSTER.md`, `tests/`.
TENANT-CONFIG (đổi theo khách): `tenant-config.json`, `domain-packs/{{slug}}/PACK.md`, `RISKS-LEGAL.md`. Màu, font, giọng, tên chỉ nằm ở hai nơi sau cùng.

## Thứ tự làm

1. Điền các mục `CHƯA CÓ — hỏi CEO` ở `PACK.md`, `RISKS-LEGAL.md`, `tenant-config.json`.
2. Chạy `python tools/agent_factory.py kiem <thư mục này>` cho tới khi PASS.
3. Dựng Airtable theo `airtable-schema.json`; tạo biến môi trường theo `HANDOVER.md`.
4. Đi theo `PHASES.md`, mỗi pha qua mốc đo mới sang pha sau. Hai tuần đầu mỗi bộ phận: `draft_only`.
5. Ghi `catalog/USAGE-LOG.md` và `catalog/GAP-LOG.md` trong khi chạy.

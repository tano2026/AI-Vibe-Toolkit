# OPC `trum-san-bay-opc` — Trùm Sân Bay

> **DEMO dựng từ thiết kế NHÁP chưa duyệt (agents/trum-san-bay/OPC-DESIGN-NOTES.md, dừng sau Phần 2 trên 5 phần). Không phải kế hoạch triển khai, chưa chạy gì.**

> Sinh bằng Agent Factory (`tools/agent_factory.py moi-opc`) ngày 2026-10-17.
> Trạng thái: **khung NHÁP, chưa duyệt, chưa chạy gì.** Đây là bộ hồ sơ để dựng công ty một người
> từ các mục có sẵn trong kho, không phải hệ thống đang chạy. Mục `CHƯA CÓ — hỏi CEO` là thông tin
> con người phải điền.

## Mô tả

Công ty một người quanh thương hiệu Trùm Sân Bay: xây kênh nội dung hàng không (Facebook chính, kèm Instagram) và thương hiệu, rồi bán dịch vụ sân bay (README của agents/trum-san-bay nêu Fast Track, SIM du lịch, đổi tiền) và làm affiliate. Dịch vụ do đối tác bên thứ ba thực hiện; Trùm Sân Bay thu tiền của khách rồi trả đối tác. Nguồn: agents/trum-san-bay/OPC-DESIGN-NOTES.md (NHÁP chưa duyệt).

- **Nguồn doanh thu:** affiliate, dich-vu
- **Kênh:** facebook, zalo, instagram
- **Gói mở rộng:** tai-chinh, doi-tac
- **Kiến trúc:** mở rộng lõi ORG v3 (9 agent, `agents/company/ORG-v2.md`) bằng Domain Pack `domain-packs/trum-san-bay-opc/PACK.md`. Không thêm agent mới; nhu cầu mới đi qua gói mở rộng.
- **Nguồn chọn mục kho:** thu_kho.recommend (mục chọn bởi thủ kho, chưa kiểm bằng dùng thật)

## Hồ sơ trong thư mục này

| File | Nội dung |
|---|---|
| `domain-packs/trum-san-bay-opc/PACK.md` | Domain Pack theo `domain-packs/_TEMPLATE.md` (phần lớn chờ CEO điền) |
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
TENANT-CONFIG (đổi theo khách): `tenant-config.json`, `domain-packs/trum-san-bay-opc/PACK.md`, `RISKS-LEGAL.md`. Màu, font, giọng, tên chỉ nằm ở hai nơi sau cùng.

## Thứ tự làm

1. Điền các mục `CHƯA CÓ — hỏi CEO` ở `PACK.md`, `RISKS-LEGAL.md`, `tenant-config.json`.
2. Chạy `python tools/agent_factory.py kiem <thư mục này>` cho tới khi PASS.
3. Dựng Airtable theo `airtable-schema.json`; tạo biến môi trường theo `HANDOVER.md`.
4. Đi theo `PHASES.md`, mỗi pha qua mốc đo mới sang pha sau. Hai tuần đầu mỗi bộ phận: `draft_only`.
5. Ghi `catalog/USAGE-LOG.md` và `catalog/GAP-LOG.md` trong khi chạy.

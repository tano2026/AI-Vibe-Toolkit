# PHASES — Lộ trình bật theo pha, OPC `{{slug}}`

> Nguyên tắc: bật từng bộ phận một, mỗi pha có **mốc đo** để qua pha sau. Chưa đạt mốc thì ở lại pha, không nhảy cóc.
> Số liệu mốc là đề xuất của công cụ; ô `CHƯA CÓ — hỏi CEO` là số CEO phải chốt sau khi có số nền. Không có mốc nào ở đây
> dựa trên dữ liệu chạy thật (kho chưa có dòng `USAGE-LOG` nào). Nếu OPC xuất phát từ một thiết kế nháp, phần KPI tự động hoá và lộ trình pha trong thiết kế đó có thể chưa được duyệt;
> khi ấy file này là khung, không phải cam kết.

## Các mốc chung (áp cho mọi pha)

- **M0 — không vi phạm lằn ranh đỏ:** số vi phạm bằng 0 trong cả pha. Một vi phạm là quay lại đầu pha và ghi escalation.
- **M1 — chế độ nháp:** hai tuần đầu của mỗi bộ phận mới là `draft_only`; người làm tay mọi hành động ra ngoài.
- **M2 — có số nền:** mỗi KPI của bộ phận đó có ít nhất hai tuần số thật trước khi đặt mục tiêu.
- **M3 — CEO xác nhận bằng chữ** trong `HANDOVER.md` mục "Trạng thái pha" rằng sang pha sau.

{{PHASE_BLOCKS}}

## Cách đo "tự động hoá"

Không dùng con số "90%" như một tuyên bố. Đo bằng ba tỉ lệ, ghi hằng tuần vào `kpis`, mục tiêu do CEO chốt:

| Tỉ lệ | Cách tính | Nguồn |
|---|---|---|
| Đầu ra qua cổng không phải sửa | `approvals` approved không sửa chia tổng `approvals` | approvals |
| Khối lượng do agent làm | job `done` do agent chia tổng job | jobs |
| Giờ CEO mỗi tuần | CEO tự ghi | kpis |

## Trạng thái pha

| Pha | Trạng thái | Ngày bắt đầu | Ngày CEO xác nhận qua pha |
|---|---|---|---|
{{PHASE_STATUS_ROWS}}

# PHASES — Lộ trình bật theo pha, OPC `trum-san-bay-opc`

> **DEMO dựng từ thiết kế NHÁP chưa duyệt (agents/trum-san-bay/OPC-DESIGN-NOTES.md, dừng sau Phần 2 trên 5 phần). Không phải kế hoạch triển khai, chưa chạy gì.**

> Nguyên tắc: bật từng bộ phận một, mỗi pha có **mốc đo** để qua pha sau. Chưa đạt mốc thì ở lại pha, không nhảy cóc.
> Số liệu mốc là đề xuất của công cụ; ô `CHƯA CÓ — hỏi CEO` là số CEO phải chốt sau khi có số nền. Không có mốc nào ở đây
> dựa trên dữ liệu chạy thật (kho chưa có dòng `USAGE-LOG` nào). Nếu OPC xuất phát từ một thiết kế nháp, phần KPI tự động hoá và lộ trình pha trong thiết kế đó có thể chưa được duyệt;
> khi ấy file này là khung, không phải cam kết.

## Các mốc chung (áp cho mọi pha)

- **M0 — không vi phạm lằn ranh đỏ:** số vi phạm bằng 0 trong cả pha. Một vi phạm là quay lại đầu pha và ghi escalation.
- **M1 — chế độ nháp:** hai tuần đầu của mỗi bộ phận mới là `draft_only`; người làm tay mọi hành động ra ngoài.
- **M2 — có số nền:** mỗi KPI của bộ phận đó có ít nhất hai tuần số thật trước khi đặt mục tiêu.
- **M3 — CEO xác nhận bằng chữ** trong `HANDOVER.md` mục "Trạng thái pha" rằng sang pha sau.

## Pha 0: Nền

- **Mục tiêu:** Dựng móng, chưa chạy việc ra ngoài.
- **Bật gì:** Domain Pack, Airtable `company-hq` theo `airtable-schema.json`, kênh lệnh CEO, `ceo`, `research`, `dev`, `analytics`; seed agents ở trạng thái `paused`.
- **Điều kiện vào:** Chưa có (pha đầu)
- **Mốc ra (đề xuất, CEO chốt):** Điền xong `PACK.md` các mục chặn (gồm mục 7: câu xác nhận tạm, SLA, kênh thanh toán chính thức); Airtable dựng xong; test `OT05` (nút dừng), `OT08` (không approved thì không chạy), `OT11` (dữ liệu nhạy cảm) và `OT13` (fail-closed) PASS; báo cáo nền của `research` nộp. Cộng các mốc chung M0 đến M3.
- **Cổng liên quan:** G7 (cấu hình), G2 (nếu mua gì)
- **Bằng chứng ghi ở:** bảng `kpis`, `HANDOVER.md` mục Trạng thái pha, `catalog/USAGE-LOG.md`

## Pha 1: Nội dung

- **Mục tiêu:** Có lô nội dung tuần chạy qua cổng.
- **Bật gì:** `marketing`, `media`, kênh đăng facebook, instagram; ghi chú affiliate
- **Điều kiện vào:** Pha Nền xong
- **Mốc ra (đề xuất, CEO chốt):** Bốn lô tuần liên tiếp được CEO duyệt; tỉ lệ bài không phải sửa đạt CHƯA CÓ — hỏi CEO; không bài nào bị gỡ vì sai sự thật; hai tuần `draft_only` xong. Cộng các mốc chung M0 đến M3.
- **Cổng liên quan:** G1, G2, G6
- **Bằng chứng ghi ở:** bảng `kpis`, `HANDOVER.md` mục Trạng thái pha, `catalog/USAGE-LOG.md`

## Pha 2: Chat và bán

- **Mục tiêu:** Có kênh chat trả lời khách, đơn nháp.
- **Bật gì:** `sales`, `support`, hộp thư chung, KB/FAQ, bảng giá chuẩn do CEO duyệt
- **Điều kiện vào:** Bảng giá chuẩn, KB, câu xác nhận tạm và mẫu trả lời dữ liệu nhạy cảm (PACK mục 7) đã được CEO duyệt
- **Mốc ra (đề xuất, CEO chốt):** Hai tuần bot ở chế độ nháp; tỉ lệ tin bot xử lý trọn đạt CHƯA CÓ — hỏi CEO; mọi ngoại lệ qua G3; không lần nào bot báo giá ngoài bảng. Cộng các mốc chung M0 đến M3.
- **Cổng liên quan:** G3
- **Bằng chứng ghi ở:** bảng `kpis`, `HANDOVER.md` mục Trạng thái pha, `catalog/USAGE-LOG.md`

## Pha 3: Đơn và tiền

- **Mục tiêu:** Có vòng đời đơn, thanh toán, đối soát.
- **Bật gì:** `operations`, gói Tài chính và thanh toán, gói Quản lý đối tác
- **Điều kiện vào:** Pháp nhân thu tiền, cổng thanh toán, mẫu hợp đồng đối tác, điều khoản hoàn tiền đã được CEO/luật sư chốt (xem `RISKS-LEGAL.md`)
- **Mốc ra (đề xuất, CEO chốt):** Bốn tuần đối soát thu chi khớp; mọi lệnh trả đối tác qua G4, hoàn tiền qua G5; sai lệch bằng CHƯA CÓ — hỏi CEO. Cộng các mốc chung M0 đến M3.
- **Cổng liên quan:** G4, G5
- **Bằng chứng ghi ở:** bảng `kpis`, `HANDOVER.md` mục Trạng thái pha, `catalog/USAGE-LOG.md`

## Pha 4: Tối ưu và mở rộng

- **Mục tiêu:** Đo lại, hạ mức duyệt có kiểm soát, thêm kênh hoặc gói.
- **Bật gì:** Rà quý bảng cổng; bật thêm kênh/gói; gỡ bộ phận không dùng
- **Điều kiện vào:** Các pha trước đạt mốc
- **Mốc ra (đề xuất, CEO chốt):** CEO rà `GATES.md` mỗi quý; bộ phận 6 tháng không có job thì đề xuất gỡ. Cộng các mốc chung M0 đến M3.
- **Cổng liên quan:** G7
- **Bằng chứng ghi ở:** bảng `kpis`, `HANDOVER.md` mục Trạng thái pha, `catalog/USAGE-LOG.md`


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
| Pha 0: Nền | Chưa bắt đầu | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| Pha 1: Nội dung | Chưa bắt đầu | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| Pha 2: Chat và bán | Chưa bắt đầu | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| Pha 3: Đơn và tiền | Chưa bắt đầu | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| Pha 4: Tối ưu và mở rộng | Chưa bắt đầu | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |

# Workflow skeleton — OPC `trum-san-bay-opc`

> Mô tả luồng dạng văn bản để người dựng n8n/Hermes bám theo. Đây KHÔNG phải file xuất của n8n và không phải mã.
> Kho hiện không có file workflow n8n nào đã kiểm (`agents/trum-san-bay/README.md` nhắc `n8n-workflow.json` nhưng file không tồn tại),
> nên bộ khung này không bịa JSON n8n. Tên bảng và trường trỏ tới `airtable-schema.json`.

## 1. Nguyên tắc luồng (không đổi)

- Hermes (agent `ceo`) là bộ não: nhận lệnh, tách job, dispatch. OpenClaw là tay chân: chỉ kéo việc đã duyệt từ Airtable và thực thi, không tự quyết, không có kênh nhận lệnh riêng.
- State nằm ở Airtable `company-hq`; sản phẩm (deliverable) nằm ở repo. Không thêm công cụ thứ ba.
- Job có nội dung ngoài làm đầu vào (`jobs.has_external_input = true`): luồng do **code** quyết (state machine cố định). LLM chỉ xử lý từng bước đóng khung và không bao giờ sinh lệnh gọi công cụ từ nội dung ngoài.
- Mọi hành động ra thế giới ngoài đi qua cổng trong `GATES.md`. Không có bản ghi `approvals.status = approved` thì không thực thi.
- Trước MỖI hành động ra ngoài, đọc `agents.status`; nếu `paused` thì dừng.

## 2. Vòng đời job (mô tả theo COORDINATION-v2 mục 4)

```
1. CEO nhắn kênh lệnh: "/job [PACK: trum-san-bay-opc] role=<agent> P1 due=<ngày> — <brief 5 phần>"
   -> Hermes (ceo) tạo bản ghi jobs, status = queued.
2. Dispatch tick (theo nhịp trong OPERATING-RHYTHM): lấy job queued theo priority.
   -> nạp: package tham chiếu + section EXPERT-CORE + Domain Pack, nhúng vào tin giao việc.
   -> jobs.status = doing; ghi activity_log.
3. Agent chạy xong -> đẩy sản phẩm lên repo -> điền jobs.output_url -> status = review.
4. Review chéo (bảng COORDINATION-v2 mục 5):
   - đạt, hành động không rủi ro -> status = done
   - đạt, hành động rủi ro (đăng, gửi, chi tiền, cam kết) -> tạo approvals (kèm gate, risk_type, risk_level) -> status = awaiting_approval
   - không đạt -> về doing kèm ghi chú, tối đa 1 vòng sửa; còn cấn thì tạo escalations
5. Thông báo cho CEO: "[job-12] <agent> xin duyệt: <hành động>. OK 12 / NO 12"
   - OK -> approved -> OpenClaw thực thi đúng bản đã duyệt -> ghi activity_log -> done
   - NO -> rejected -> về doing kèm ghi chú
   - im lặng 24 giờ -> expired -> KHÔNG làm; nhắc đúng một lần
6. blocked hơn 24 giờ hoặc lỗi lặp 3 lần -> agent tự tạo escalations -> lên bản tin sáng hôm sau.
```

## 3. Nút dừng và tự khoá

```
/stop (kênh CEO) -> đặt agents.status = paused cho agent hoặc toàn OPC
                 -> OpenClaw kiểm cờ trước mỗi hành động ra ngoài; thấy paused thì bỏ qua, giữ nháp
Tự khoá khi: token nền tảng hết hạn/bị từ chối | tỉ lệ chuyển người vượt ngưỡng | chi tiêu chạm mức
             -> đặt paused cho phần bị ảnh hưởng, tạo escalations
```

Trạng thái: thiết kế, chưa có mã.

## 4. Luồng theo bộ phận đã bật

### 4.1 Nội dung hằng tuần

```
analytics (số tuần trước) -> marketing lập lịch tuần theo trụ cột và phễu của Domain Pack
  -> research kiểm chứng thông tin  -> media sản xuất hình/video
  -> compliance-gate và chú thích quảng cáo/affiliate (nếu có)
  -> [G1] CEO duyệt cả lô tuần
  -> OpenClaw đăng theo lịch (kiểm agents.status trước mỗi bài)  -> theo dõi kết quả -> analytics
```

Kênh đăng: facebook, instagram. Bài lệch lịch đã duyệt quay lại hỏi (L2). Hai tuần đầu: chỉ soạn, CEO đăng tay. Bảng: jobs, approvals, activity_log, kpis.

### 4.2 Tin nhắn thời gian thực

```
Kênh vào (facebook, zalo, instagram) -> hộp thư chung -> phân loại ý định và cảm xúc (code quyết luồng)
  -> FAQ và bảng giá chuẩn đã duyệt: bot tự trả lời (L1, log)
  -> muốn mua: sales lập đơn nháp  -> ngoài bảng/khiếu nại: [G3] chuyển CEO (L3)
```

Tin nhắn khách là nội dung ngoài: luôn đi theo luồng code-driven, đánh dấu jobs.has_external_input. Hai tuần đầu bot ở chế độ nháp. Hộp thư chung và cách nối từng kênh: chọn qua thủ kho (xem CAPABILITY-MAP.md), chưa quyết trong khung này.

### 4.3 Đơn, tiền và đối tác

```
đơn nháp -> khách thanh toán -> operations xác nhận -> gửi đối tác -> nhắc lịch -> hỏi đánh giá
  -> đối soát cuối tuần -> [G4] CEO duyệt lệnh trả đối tác -> [G5] hoàn tiền từng ca
```

Agent không tự chuyển tiền ra ngoài. Bảng mở rộng: orders, payouts, refunds, partners (xem `airtable-schema.json`, mục extension_tables; đề xuất, chưa duyệt).

### 4.4 Affiliate

```
link theo dõi gắn khi marketing soạn bài -> chú thích quảng cáo/affiliate đúng quy định từng nền tảng (compliance-gate)
  -> đối soát hoa hồng hằng tuần (analytics) -> đưa lại marketing chỉnh lịch
```

Danh sách chương trình affiliate thật và quy định từng nền tảng: CHƯA CÓ — hỏi CEO.


## 5. Việc định kỳ chung

| Nhịp | Việc | Agent | Đầu ra |
|---|---|---|---|
| Hằng ngày | Bản tin sáng: việc chờ duyệt, bị chặn, xong trong 24 giờ | ceo | Một tin nhắn theo view `CEO Cockpit` |
| Cuối tuần | Điền `kpis.actual`, giải thích lệch ở `kpis.note` nếu dưới 70% | từng agent | Bảng KPI tuần |
| Hằng tuần | Rà `USAGE-LOG` và `GAP-LOG` cho OPC này | analytics | Danh sách mục dùng được, phải sửa, bỏ, HỔNG |
| Hằng quý | Rà `GATES.md`: cổng nào duyệt 100% không sửa 3 tháng thì cân nhắc hạ (CEO quyết) | ceo | Biên bản rà |

## 6. Đã làm và chưa làm

- Chưa có workflow n8n hay mã Hermes nào được dựng từ file này.
- Mẫu mã truy cập Airtable bằng urllib nằm ở `agents/company/COORDINATION-v2.md` mục 6; chưa chạy với token thật.

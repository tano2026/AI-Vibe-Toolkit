# Kết quả kiểm hai ví dụ

> Dán nguyên văn đầu ra thật của `python tools/agent_factory.py kiem <thư-mục>` và `ban-giao`, chạy ngày 2026-10-17 với `tools/thu_kho.py` THẬT (commit `5b0f867` của nhánh `claude/thu-kho`, đọc `catalog/catalog.json` thật, không mạng).
> **PASS ở đây nghĩa là hồ sơ đủ thứ phải có và không phạm luật cứng. Không có nghĩa agent làm việc tốt.** Chưa mục kho nào được dùng thật, chưa test nào trong `tests/test-cases.json` được chạy (mọi ca là `CHUA-CHAY`), chưa chạy với credential thật.

## 1. facebook-channel-agent (agent riêng lẻ, tự chủ L1, vessel hermes)

```
[PASS] cấu-trúc: đủ 11 file (agent)
[PASS] jd-kpi-sop-escalation: đủ 4 mục có nội dung
[PASS] ba-lằn-ranh-đỏ: đủ 3 trong system-prompt.md
[PASS] cổng-duyệt: 6 cổng GA, có L2/L3
[PASS] nút-dừng-khẩn: có /stop
[PASS] mục-kho: 6 id được nhắc, đều có trong catalog.json
[PASS] kế-hoạch-cài-và-test: có INSTALL-PLAN khô và bộ test PASS/FAIL
[PASS] khóa-bí-mật: không có chuỗi trông như khóa bí mật
[PASS] chỗ-trống: không còn {{...}} trần; 48 chỗ đánh dấu 'CHƯA CÓ — hỏi CEO' chờ con người
[PASS] tenant-config: đúng schema, compliance_overrides = null
[PASS] chế-độ-nháp: launch_mode = draft_only
[PASS] không-hardcode-brand-màu: logic không chứa màu hex hay tên thương hiệu (chỉ ở tenant-config/PACK/README/HANDOVER)
KẾT QUẢ: PASS (12 PASS, 0 WARN, 0 FAIL)
exit=0
```

## 2. trum-san-bay-opc (OPC, DEMO dựng từ thiết kế NHÁP chưa duyệt)

```
[PASS] cấu-trúc: đủ 16 file (opc)
[PASS] jd-kpi-sop-escalation: 9 agent đều đủ 4 mục
[PASS] ba-lằn-ranh-đỏ: đủ 3 trong GATES.md
[PASS] cổng-duyệt: đủ G1 đến G7
[PASS] nút-dừng-khẩn: có /stop
[PASS] mục-kho: 29 id được nhắc, đều có trong catalog.json
[PASS] kế-hoạch-cài-và-test: có INSTALL-PLAN khô và bộ test PASS/FAIL
[PASS] khóa-bí-mật: không có chuỗi trông như khóa bí mật
[PASS] chỗ-trống: không còn {{...}} trần; 103 chỗ đánh dấu 'CHƯA CÓ — hỏi CEO' chờ con người
[PASS] tenant-config: đúng schema, compliance_overrides = null
[PASS] chế-độ-nháp: launch_mode = draft_only
[PASS] không-hardcode-brand-màu: logic không chứa màu hex hay tên thương hiệu (chỉ ở tenant-config/PACK/README/HANDOVER)
[PASS] airtable-schema: 7 bảng lõi + 4 bảng mở rộng, link hợp lệ
KẾT QUẢ: PASS (13 PASS, 0 WARN, 0 FAIL)
exit=0
```

## 3. Bàn giao thử (ghi ra thư mục tạm, không đưa vào repo)

```
Đã tạo gói bàn giao: <thư-mục-tạm>\af-bg\facebook-channel-agent (15 file, có CHECKSUMS.sha256)
exit=0
Đã tạo gói bàn giao: <thư-mục-tạm>\af-bg\trum-san-bay-opc (17 file, có CHECKSUMS.sha256)
exit=0
```

Gói có `CHECKSUMS.sha256` (SHA256 từng file), `KET-QUA-KIEM.txt` và `HANDOVER.md` đã điền phần tự sinh. Hai gói này không được commit.

## 4. Test của chính công cụ

```
python -m unittest discover -s tools/tests -p "test_agent_factory.py"
----------------------------------------------------------------------
Ran 49 tests in 9.969s

OK
```

Trong đó gồm test chạy với thu_kho giả (không phụ thuộc kho) và hai test chạy với `tools/thu_kho.py` thật (tự bỏ qua nếu thiếu file).

## 5. Những chỗ nội dung sinh ra còn lệch hoặc yếu (đánh giá của người dựng, chưa kiểm bằng dùng thật)

Đọc kết quả sinh ra, tôi thấy các điểm sau. Công cụ không tự sửa vì đây là lựa chọn của thủ kho theo nhãn khả năng, không hiểu ngữ cảnh:

1. **facebook-channel-agent không có mục loại Tay nào.** Cả ba mục chính là skill/prompt (Não). Khả năng thật sự "đăng bài lên Facebook" chưa có công cụ: mục dự phòng của `social-media` là `mcps/buffer-mcp` (cần khoá API, tức L3). Công cụ in cảnh báo này ở README. Đây là lý do mặc định `draft_only` là đúng cho ví dụ này: agent mới soạn được nháp.
2. **`customer-support` chọn nhầm hướng cho việc trả lời bình luận.** Mục chính là `churn-risk-escalation-discipline` (luật phân loại rủi ro rời bỏ và SLA), không phải công cụ trả lời. Dự phòng là Chatwoot (cần docker và VPS). Phải spike hoặc chọn lại.
3. **Trong OPC có dự phòng lệch việc:** `finance-accounting` có dự phòng `repos/tradingagents` (theo tên entry: phòng giao dịch AI đa-agent), không hợp với OPC và đụng luật AI không thực hiện giao dịch tài chính; `data-dashboard` có dự phòng `repos/sc-datav` (dashboard 3D màn hình lớn); `productivity` (cho `operations`) chọn chính là stack `second-brain-obsidian-claude`, không phải công cụ vận hành đơn hàng; `agent-orchestration-memory` (cho `ceo`) chọn `repos/tencentdb-agent-memory`, chưa kiểm hợp với Hermes. Người duyệt phải gạt hoặc chọn lại trước khi lập kế hoạch cài.
4. **Ba nhu cầu nền của OPC chưa có công cụ thực thi trong kết quả:** đăng bài Facebook/Instagram (mục chính của `social-media` là skill), nhận và trả lời tin Zalo OA (mục chính của `customer-support` là skill), thu tiền (mục chính của `finance-accounting` là `mcps/cloud-accounting-mcps`, thiên về kế toán, chưa phải cổng thanh toán). Công cụ không báo HỔNG vì thủ kho vẫn trả ứng viên khớp nhãn khả năng. Có thật sự thiếu hay không thì phải đọc entry gốc rồi ghi `catalog/GAP-LOG.md`; `OPC-DESIGN-NOTES.md` cũng nói các mục Zalo cần kiểm lại.
5. **Hai gói mở rộng `tai-chinh` và `doi-tac` chưa có role pack.** Hồ sơ OPC ghi rõ "CHƯA CÓ trong kho" và các bảng `orders`, `payouts`, `refunds`, `partners` là đề xuất chưa duyệt.
6. **`INSTALL-PLAN.md` của OPC dài (hơn 50KB)** vì thủ kho liệt kê toàn bộ bước từ entry; công cụ rút mỗi danh sách còn 15 mục đầu. Mục `mcps/cloud-accounting-mcps` dài nhất. Người duyệt đọc entry gốc, không đọc kế hoạch thay entry.
7. **KPI mục tiêu bằng số đều để `CHƯA CÓ — hỏi CEO`** (chỉ KPI "số vi phạm ba lằn ranh đỏ = 0" có số, vì đó là luật). Đúng ý, nhưng nghĩa là hồ sơ chưa đo được gì cho tới khi CEO điền.
8. **Tên biến môi trường** ngoài Airtable và Zalo (có nguồn trong kho) là đề xuất của công cụ.

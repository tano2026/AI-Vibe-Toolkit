# Kiểm thử sử dụng lô skill-a1 (mô phỏng văn bản)

Ngày 2026-10-19. Phương pháp: mô phỏng bằng văn bản, không chạy mã, không dùng mạng. 41 mục `skill-agent` đầu tiên theo id tăng dần (chỉ số 0-40). Đây không phải dùng thật trong dự án.

## Bảng đếm verdict

| Verdict | Số mục |
|---|---|
| pass | 20 |
| partial | 21 |
| fail | 0 |
| khong-ap-dung | 0 |
| Tổng | 41 |

## 10 vấn đề phổ biến nhất

| Mã | Số lần | Ví dụ |
|---|---|---|
| GAN_THUONG_HIEU_CUNG | 25 | `aviation-policy-lookup`: Mô tả và mục 'Khi nào dùng' gắn cứng An Bình/ABTRIP và Fast Track Nội Bài; khách khác phải viết lại. |
| CAN_CONG_CU_NGOAI | 15 | `aviation-policy-lookup`: Bước 2 buộc web search qua source-evaluation nhưng không nêu công cụ/MCP nào, nên không có công cụ thì skill chỉ ra khung rỗng. |
| MAU_THUAN | 14 | `competitive-intel-ground-handling`: Bước 5 đòi trích nguồn mọi số liệu thị phần, nhưng mục Lưu ý khẳng định 'không brand nào ngoài dnata kết hợp B2C+B2B' không kèm nguồn. |
| KHAC | 12 | `data-storytelling`: Ví dụ gọi 60% so với 25% là 'gấp đôi' (thực tế 2,4 lần), chỉ lệch nhẹ; bước xuất docx/pdf không nói dùng công cụ nào. |
| MO_HO | 11 | `ota-content-strategy`: Bước 3 bảo kiểm giới hạn ký tự từng nền tảng nhưng không đưa số hay nguồn tra. |
| KHONG_CO_DINH_DANG_RA | 7 | `customer-pattern-analysis`: Không có mẫu báo cáo đầu ra (bảng, tiêu đề, độ dài), chỉ có 'ra so what'. |
| REF_THIEU | 5 | `ota-content-strategy`: AnBinh_Brand_Foundation_v1.md được nhắc ở Bước 1 nhưng không có trong repo (đã tìm toàn kho). |
| THIEU_GUARDRAIL | 4 | `human-footage-editor`: Cho phép clone giọng khách bằng F5-TTS từ 3 giây mẫu nhưng không yêu cầu sự đồng ý rõ ràng bằng văn bản của khách. |
| PHAI_BIA_SO_LIEU | 2 | `ad-budget-testing-discipline`: Ví dụ khẳng định 'Facebook đã proven cho SMB VN theo kinh nghiệm ngành' không có nguồn. |

## Mục fail

Không có mục nào fail. Không có mục rỗng hay mâu thuẫn đến mức không làm theo được; lỗi chủ yếu là thiếu tham chiếu, công cụ ngoài và gắn thương hiệu.

## Mục partial (cần bổ sung)

- `aviation-policy-lookup`: CAN_CONG_CU_NGOAI; GAN_THUONG_HIEU_CUNG -> Nêu rõ công cụ tìm kiếm (web search MCP) và tách phần Nội Bài/An Bình ra file cấu hình khách.
- `competitive-intel-ground-handling`: CAN_CONG_CU_NGOAI; GAN_THUONG_HIEU_CUNG; MAU_THUAN -> Tách differentiator vào file brand riêng, dẫn nguồn cho nhận định thị trường hoặc đánh dấu là giả thuyết.
- `customer-pattern-analysis`: CAN_CONG_CU_NGOAI; KHONG_CO_DINH_DANG_RA; GAN_THUONG_HIEU_CUNG -> Thêm mẫu bảng đếm chủ đề + 2-3 ưu tiên, nêu rõ cách chạy khi không có code execution.
- `ota-content-strategy`: REF_THIEU; GAN_THUONG_HIEU_CUNG; MO_HO -> Thêm file brand foundation vào kho hoặc đổi thành tham số; liệt kê giới hạn ký tự Klook/Traveloka.
- `source-evaluation`: CAN_CONG_CU_NGOAI; KHONG_CO_DINH_DANG_RA; MAU_THUAN -> Thêm thang chấm và mẫu bảng nguồn; bổ sung CAAV; sửa câu 'mọi skill'.
- `brand-strategy-sprint`: CAN_CONG_CU_NGOAI; MAU_THUAN; GAN_THUONG_HIEU_CUNG -> Nêu công cụ Channel Audit; sửa câu 'không cần tool bên ngoài'.
- `human-footage-editor`: THIEU_GUARDRAIL; CAN_CONG_CU_NGOAI; GAN_THUONG_HIEU_CUNG -> Thêm bước xin đồng ý clone giọng; trỏ tới ffmpeg-media-toolkit.
- `hermes-autonomous-kho-maintenance`: CAN_CONG_CU_NGOAI; MO_HO; THIEU_GUARDRAIL -> Đặt ngưỡng confidence bằng số và bắt buộc sửa trên nhánh riêng.
- `skill-lifecycle-management`: KHONG_CO_DINH_DANG_RA; MAU_THUAN; GAN_THUONG_HIEU_CUNG -> Thêm mẫu bảng audit và cập nhật số liệu.
- `task-intake-quality-gate`: MAU_THUAN; MO_HO; GAN_THUONG_HIEU_CUNG -> Sửa ví dụ cho đúng quy tắc và liệt kê 8 Pro Agent.
- `brand-image-prompt-engineer`: REF_THIEU; GAN_THUONG_HIEU_CUNG; MAU_THUAN; CAN_CONG_CU_NGOAI -> Sửa đường dẫn, gộp với bản core.
- `brand-visual-template-system`: GAN_THUONG_HIEU_CUNG; KHONG_CO_DINH_DANG_RA; MAU_THUAN -> Gộp với bản core và chốt hệ Designer duy nhất.
- `design-quality-gate`: CAN_CONG_CU_NGOAI; REF_THIEU; GAN_THUONG_HIEU_CUNG -> Giải thích PACK và thêm mẫu design-spec.
- `prompt-motion-reference`: CAN_CONG_CU_NGOAI; MO_HO; GAN_THUONG_HIEU_CUNG -> Định nghĩa điều kiện dừng ở bước 1.
- `sales-marketing-collateral-production`: KHONG_CO_DINH_DANG_RA; MAU_THUAN; GAN_THUONG_HIEU_CUNG -> Làm rõ ma trận test và công cụ bàn giao.
- `ad-budget-testing-discipline`: THIEU_GUARDRAIL; MAU_THUAN; MO_HO; PHAI_BIA_SO_LIEU -> Thêm bước duyệt trước chi tiền; thống nhất ngưỡng scale.
- `agent-design-playbook`: REF_THIEU; KHAC -> Thêm mẫu Design Review ở cuối.
- `dev-automation-discipline`: MAU_THUAN; GAN_THUONG_HIEU_CUNG -> Sửa bước 2 và đổi ví dụ trung tính.
- `production-signal-feedback-loop`: CAN_CONG_CU_NGOAI; MAU_THUAN; REF_THIEU -> Giữ một cơ chế chính và xoá phần cũ.
- `cross-channel-distribution-analysis`: CAN_CONG_CU_NGOAI; MO_HO; GAN_THUONG_HIEU_CUNG -> Nêu nguồn dữ liệu TikTok/IG và phương án khi không có vidIQ.
- `competitive-intel`: CAN_CONG_CU_NGOAI; PHAI_BIA_SO_LIEU; KHAC -> Thêm luật 'thiếu dữ liệu thì để trống' và nguồn.

## Nhận xét riêng cho skill kho tự viết

- GAN_THUONG_HIEU_CUNG xuất hiện ở 25/41 mục. Phần lớn nằm trong Ví dụ thực tế và tên người duyệt (Nobitano); nặng nhất ở các mục có token/bối cảnh/tagline cứng: ota-content-strategy, brand-visual-template-system, brand-image-prompt-engineer, competitive-intel-ground-handling, tencent-vps-capacity-cost.
- Ví dụ thực tế lệch quy trình: task-intake-quality-gate (hỏi 'Brand nào' trước, trái quy tắc câu hỏi đầu là hình thức giao), contrarian-insight-structure (dẫn interview thật không có trong kho), dev-automation-discipline (Setup nhắc 6 bước debug đã bị xoá), ad-budget-testing-discipline (kill rule số chỉ nằm ở Setup).
- Tham chiếu hỏng: `repos/mcps/google-flow-mcp.md` (thực tế `mcps/google-flow-mcp.md`), `AnBinh_Brand_Foundation_v1.md` (không có trong kho), `ecc-orch-*` (không có), mẫu 'Design Review' (agent-design-playbook) không tồn tại ở cuối file.
- Mâu thuẫn giữa skill: ngưỡng retention 3s 65% (editorial-workflow-quality-gates) và 70% (media-performance-discipline); scale 20% (claude-ads) và 30% (ad-budget-testing-discipline); image-prompt-formula-core / visual-template-formula-core trùng với bản có brand tương ứng.

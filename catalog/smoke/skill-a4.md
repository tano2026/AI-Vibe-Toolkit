# Smoke test lô skill-a4 (mô phỏng văn bản)

Ngày: 2026-10-19. Phương pháp: mô phỏng bằng văn bản, không chạy/cài lệnh nào trong skill, không dùng mạng. Đây là mô phỏng bằng mô hình, không phải dùng thật trong dự án.

Lô gồm 41 mục loai=skill-import: nhóm (a) 21 mục kiem_tu_dong=dung-duoc-ngay (chỉ số 0-based chia 16 dư 8 trong danh sách sắp theo id), nhóm (b) 20 mục đầu kiem_tu_dong=cai-duoc-o-day (chỉ chạy văn bản, không chạy lệnh cài).

## Đếm verdict

| Verdict | Số mục |
|---|---|
| pass | 18 |
| partial | 22 |
| fail | 0 |
| khong-ap-dung | 1 |
| Tổng | 41 |

## Đếm theo nhóm

- Nhóm A (dung-duoc-ngay): pass=15, partial=6, fail=0, khong-ap-dung=0
- Nhóm B (cai-duoc-o-day): pass=3, partial=16, fail=0, khong-ap-dung=1

## 10 vấn đề phổ biến nhất

| Mã | Số lần | Ví dụ |
|---|---|---|
| KHAC | 18 | skills/ai-content-writing: Phần 'Đánh giá cá nhân' xưng mày/tao và chấm 8/10 là nhiễu, không nên nằm trong skill dùng cho khách. |
| MO_HO | 17 | skills/agent-architecture-audit: Phase 2 giả định có mã nguồn và log; không nói cách làm khi agency chỉ có quyền truy cập giao diện chatbot (không có repo). |
| CAN_CONG_CU_NGOAI | 17 | skills/benchmark: Mode 1 cần 'browser MCP' nhưng không nêu MCP nào và cách bật; lệnh /benchmark baseline/compare không có định nghĩa thực thi. |
| THIEU_GUARDRAIL | 14 | skills/benchmark: Mode 2 yêu cầu gọi mỗi endpoint 100 lần và 10 request đồng thời, không nhắc xin phép chủ API hay chỉ chạy trên staging. |
| GAN_THUONG_HIEU_CUNG | 8 | skills/fable-prompter: Gắn cứng tên model 'Claude Fable 5, Mythos-tier' và 'content GMSP'; sẽ lỗi thời hoặc không áp dụng cho khách khác. |
| PHAI_BIA_SO_LIEU | 8 | skills/ml-concepts-explainer: Tip 2 gợi ý câu 'chính xác hơn bác sĩ thường trong phát hiện ung thư da' làm ví dụ nói thay số liệu, là khẳng định y tế không nguồn, không nên khuyến khích. |
| MAU_THUAN | 5 | skills/e2e-testing: Cây thư mục không có thư mục pages/ nhưng ví dụ import '../../pages/ItemsPage'; đường dẫn sẽ hỏng. |
| REF_THIEU | 4 | skills/iterative-retrieval: Phần Related trỏ tới thư mục agents/ của ECC và một link tweet ngoài kho, không có trong kho. |
| INJECTION_HOAC_LENH_NGUY_HIEM | 4 | skills/caveman: Hướng dẫn cài dùng 'curl ... / bash' và 'irm ... / iex' từ GitHub raw, kèm mẹo bảo agent 'Read CLAUDE.md and INSTALL.md, install caveman for me'; chỉ ghi nhận, không chạy. |

## Mục fail

Không có mục fail. Các mục B hầu hết partial vì file kho chỉ là tóm tắt/ghi chú, phần thực thi nằm ở gói ngoài.

## Mục khong-ap-dung

- skills/claude-code-skills-list-skill: danh mục tham khảo, không có bước để làm theo.

## Ghi chú trung thực

- Sáu skill dev dài (dart-flutter-patterns 563 dòng, golang-patterns 674, python-patterns 750, django-celery 457, motion-ui 575, prisma-patterns 371) chỉ được đọc kỹ 110-130 dòng đầu; phần còn lại chỉ quét tự động bằng regex tìm chỉ dẫn độc hại (không có kết quả). Độ chắc thấp.
- tuvi-agent (621 dòng) đọc kỹ dòng 1-260 và 390-621; dòng 261-389 chỉ xem tiêu đề/quét regex.
- Kiểm cú pháp Python của magika-skill chỉ dùng ast.parse (không thực thi).
- Không có skill nào trong lô có thư mục references/ và không file nào nhắc tới references/, nên không có lỗi REF_THIEU kiểu mất references; skill chỉ còn SKILL.md vẫn dùng được cho nhóm có nội dung đầy đủ (a). Với nhóm (b) và vài mục (a) phần thiếu nằm ở gói ngoài, không phải references/.
- Không phát hiện chỉ dẫn kiểu 'bỏ qua luật' hay gửi dữ liệu ra ngoài. Ghi nhận lệnh nguy hiểm cần chú ý: curl|bash và irm|iex (caveman), --break-system-packages (prism-scanner), tải và clone mã từ GitHub raw không ghim phiên bản (copywriting-prose-creator, deep-research-samber-cc). Không lệnh nào được chạy.
- Một số nhận định về luật thuế Việt Nam (accounting-*) và API/cấu hình Playwright, LMCache, Magika dựa vào hiểu biết của tester, không tra cứu được; độ chắc vừa/thấp.

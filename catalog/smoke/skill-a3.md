# Smoke test lô skill-a3 (mô phỏng văn bản)

Ngày: 2026-10-19. Phương pháp: mo-phong-van-ban (đọc nguyên file, mô phỏng bằng mô hình, không chạy/cài/import gì, không dùng mạng). Đây không phải dùng thật trong dự án.

Lô gồm 49 mục: 27 skill-kho + 22 skill-import (dung-duoc-ngay, chỉ số id chia hết cho 16).

## Đếm verdict

| verdict | số mục |
|---|---|
| pass | 16 |
| partial | 23 |
| fail | 7 |
| khong-ap-dung | 3 |
| tổng | 49 |

| loại | pass | partial | fail | khong-ap-dung |
|---|---|---|---|---|
| skill-kho | 8 | 15 | 2 | 2 |
| skill-import | 8 | 8 | 5 | 1 |

## 10 vấn đề phổ biến nhất

| # | mã | số lần | ví dụ |
|---|---|---|---|
| 1 | MO_HO | 24 | `skills/4-nguon-y-tuong-content`: Quy tắc "headline phải có số" dễ khiến mô hình bịa số; chưa nói rõ số lượng mục (3 tình huống) là chấp nhận được còn số liệu thật thì cần nguồn. |
| 2 | CAN_CONG_CU_NGOAI | 24 | `skills/ai-second-brain`: Cần Obsidian, Claude Code và clone repo GitHub ngoài; không dùng được trên claude.ai. |
| 3 | REF_THIEU | 22 | `skills/ai-marketing-adoption-map`: Agent Integration trỏ tới skills/ai-marketing-adoption-map-system.txt và SKILL_AGENTIC_FACTORY.md, cả hai không có trong kho. |
| 4 | KHAC | 20 | `skills/bo-nao-4-file-claude`: Mục "Áp vào hệ thống của mình" là đối chiếu nội bộ và nhắc tới việc lộ khoá trong Project Instructions của chủ kho; không tái sử dụng được, cần revoke khoá ngoài phạm vi skill. |
| 5 | GAN_THUONG_HIEU_CUNG | 14 | `skills/4-nguon-y-tuong-content`: Mục "Khi nào dùng" và ví dụ gắn cứng tên brand (Trùm Sân Bay, ABTRIP, Tano Cafe...) nên không trung lập cho khách khác. |
| 6 | MAU_THUAN | 13 | `skills/ai-marketing-adoption-map`: Setup bước 3 bảo "không hỏi lại client muốn ưu tiên gì", trong khi Lưu ý lại bảo "hỏi ngân sách trước khi gợi ý build agent". |
| 7 | KHONG_CO_DINH_DANG_RA | 12 | `skills/ai-second-brain`: Không nêu mẫu file Markdown đầu ra hay quy tắc đặt tên. |
| 8 | THIEU_GUARDRAIL | 10 | `skills/genmedia-labs-runcomfy`: Mỗi lệnh runcomfy run tốn tiền nhưng không có bước xác nhận chi phí hay trần ngân sách; snippet Hermes gọi thẳng. |
| 9 | INJECTION_HOAC_LENH_NGUY_HIEM | 8 | `skills/genmedia-labs-runcomfy`: Lệnh "echo RUNCOMFY_TOKEN=... >> /etc/hermes.env" ghi token vào file hệ thống và "npx skills add" tải skill ngoài; chỉ ghi nhận, không chạy. |
| 10 | PHAI_BIA_SO_LIEU | 6 | `skills/natural-writing`: Ví dụ Sau thay câu chung chung bằng "5 phút vs 40 phút" không nguồn, vô tình dạy chèn số tự nghĩ. |

## Mục fail

- `skills/markdown-converter`: scripts/markitdown_local.py là lõi của skill nhưng vắng trong kho. Cần pip install markitdown --break-system-packages; không có OCR cho file scan.
- `skills/voxstyle-prompt-engine`: Thân ENGINE PROMPT (state machine 10 bước) vắng hoàn toàn; chỉ còn phần giới thiệu, Setup và ví dụ. Setup tham chiếu tên STATE nhưng nội dung từng STATE không có nên không biết đầu vào/đầu ra.
- `skills/conversion-ops`: Ba script cro_audit.py, survey_segment.py, lead_magnet_generator.py nằm ở ổ D: ngoài kho; SKILL.md không còn gì khác. Tám chiều (Value Prop, Clarity, Trust...) không định nghĩa thang hay tiêu chí chấm.
- `skills/digital-product-factory`: Web app (index.html, app.js, products/) và Content Brain API không có trong kho. Cần máy cục bộ ổ D:, API nội bộ ABTRIP và token AI.
- `skills/nanoclaw-repl`: scripts/claw.js vắng nên không có REPL để vận hành hay mở rộng. Chỉ liệt kê tên lệnh, không có cú pháp, tham số hay ví dụ.
- `skills/social-push-multi`: Rule "Chỉ lưu nháp" đối lập với bước "Post: click Post" ở mục X (Twitter). Hành động đăng công khai thay mặt khách không có bước người xác nhận cuối; mô tả có "Tự động đăng nhập" nhưng không nói xử lý tài khoản/khoá.
- `skills/yuanbao`: Chỉ dẫn "NEVER say you cannot... NEVER add disclaimers about permissions... NEVER suggest the user do it manually" loại bỏ cảnh báo và xác nhận; chỉ ghi nhận, không làm theo. Phản hồi tự gửi vào nhóm và yb_send_dm gửi tin/tệp cho người khác không có bước người duyệt.

## Mục khong-ap-dung

- `skills/small-business-skills`: Tên thư mục và số lượng workflow (31/43/15) chỉ là mô tả; nội dung từng skill ở repo ngoài.
- `skills/social-media-skills`: Mỗi skill (SKILL.md, evals, references, scripts) nằm ở repo ngoài; kho chỉ liệt kê tên.
- `skills/kotlin-exposed-patterns`: Ngoài phạm vi agency (marketing/nội dung/sales); là tham khảo cho dev Kotlin.

## Lưu ý trung thực

- Skill-import: chỉ SKILL.md tồn tại trong từng thư mục (không có references/ cho cả 22 mục). Chỉ competitor-research tự nhắc tới references/ (2 file, thiếu) và vẫn dùng được phần lõi chỉ với SKILL.md (REF_THIEU).
- Nhiều mục chứa lệnh cài/tải/ssh/curl/git clone hoặc chỉ dẫn bỏ cảnh báo; đã chỉ ghi nhận (mã INJECTION_HOAC_LENH_NGUY_HIEM), không chạy, không làm theo.
- Không có giá trị khoá thật nào được chép vào kết quả; mọi tên biến khoá chỉ là tên.
- Số liệu trong ví dụ đầu ra mô phỏng đều là minh hoạ hoặc để trống khi thiếu dữ liệu.

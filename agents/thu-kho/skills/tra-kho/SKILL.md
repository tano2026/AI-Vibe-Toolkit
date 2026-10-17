---
name: tra-kho
description: >
  Tra kho AI-Vibe-Toolkit (916 mục) theo quy trình AGENT-ROUTER và trả ứng viên có độ tin cậy nhãn.
  Dùng khi cần tìm công cụ/skill/MCP/stack cho một việc cụ thể (cào web, đăng bài, giọng đọc, CRM...).
  Không dùng để cài đặt (xem skill goi-y-cai-dat) và không thay việc đọc entry gốc.
---

# Tra kho

## Khi nào dùng
- Có một việc cụ thể cần công cụ: "cào web đối thủ", "giọng đọc tiếng Việt", "chatbot Zalo"
- Cần so 2-3 lựa chọn cùng nhóm (cùng `dup_group`)
- Kiểm xem kho đã có thứ gì trước khi đi tìm/viết entry mới (quy tắc "chỉ thêm khi có nhu cầu")

## Khi nào KHÔNG dùng
- Cần kế hoạch cài, chạy lệnh → `goi-y-cai-dat`
- Cần ghi nhận kết quả dùng thật → `ghi-so`
- Yêu cầu quá chung ("làm cho tôi cái gì hay hay"): hỏi lại trước

## Quy trình
1. Viết 1 câu "làm [việc] → ra [đầu ra]". Xác định ràng buộc: vessel (hermes / openclaw / claude-code / antigravity), có GPU/VPS/Docker không, ngân sách chi trả có bằng 0 không.
2. Chạy:
   ```bash
   python tools/thu_kho.py tim "<việc>" [--vessel hermes] [--bo-can gpu,vps] [--top 5]
   ```
   Câu hỏi có "không GPU", "không cần VPS", "miễn phí" được tự đổi thành `--bo-can` (công cụ in dòng "Tự bỏ mục cần").
3. Đọc kết quả theo thứ tự: bậc khớp → `curation_status` → `confidence`. Nhìn cột *độ tin cậy nhãn*, không phải điểm.
4. Với ứng viên định đề xuất: `python tools/thu_kho.py chi-tiet <id>` rồi **mở file `duong_dan`**, đọc `skip_if` và mục Lưu ý.
5. Chọn 1 chính + 1 dự phòng khác `dup_group`. Không có mục nào đủ tốt → báo HỔNG, chuyển `ghi-so`.
6. Phần "Thêm (chưa gắn nhãn)" chỉ để người biết kho còn gì; không đề xuất trực tiếp trước khi đọc entry.

## Lưu ý đọc kết quả
- `vessel_fit` rỗng = chưa rõ, không phải chạy mọi nơi
- `needs`: `api-key` → chạm khoá (L3); `tra-phi` → chi tiền (L2); `claude-code-only` → không dùng được trong Hermes/OpenClaw
- `adoption = can-ha-tang` → cần VPS/docker/DB/nhiều bước; `chi-tham-khao` bị ẩn mặc định (thêm `--ca-tham-khao` để thấy)
- Có `catalog/audit.json` thì mục bị audit "không dùng được" bị đẩy xuống cuối kèm ghi chú

## Ví dụ
Việc: "cào web đối thủ khách sạn, máy không có GPU"
(rút gọn; đầu ra đầy đủ của truy vấn gần giống nằm ở `EXAMPLES.md`)
```
$ python tools/thu_kho.py tim "cào web đối thủ, không GPU" --top 3
Khả năng phát hiện: scraping (cào web), web-research (đối thủ)
Tự bỏ mục cần: gpu
1. mcps/crawl4ai - Crawl4AI MCP ... (da-doc-entry-goc, cần docker)
2. repos/gpt-crawler ...
3. mcps/firecrawl ... (cần api-key)
```
Chọn chính = crawl4ai (cần Docker), dự phòng = gpt-crawler (khác nhóm, không cần gì). Mở `mcps/crawl4ai.md`, đọc skip_if ("không chạy được Docker nền hoặc RAM trống dưới 4GB") rồi mới đề xuất.

## PASS / FAIL
- **PASS:** mỗi ứng viên đưa ra có id có thật trong catalog, nêu `curation_status`, nêu `skip_if`/rủi ro sau khi đã mở entry gốc; HỔNG được báo thay vì bịa
- **FAIL:** đề xuất mục chưa mở entry gốc; bỏ qua ràng buộc người dùng nêu (GPU/vessel); gọi `chua-gan-nhan` là "đã kiểm"; không nhắc "chưa mục nào dùng thật" khi người dùng dựa vào điểm số

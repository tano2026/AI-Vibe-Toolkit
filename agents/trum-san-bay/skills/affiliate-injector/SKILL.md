---
name: affiliate-injector
description: >
  Guardrail gắn affiliate link vé máy bay vào caption Trùm Sân Bay — vừa hướng dẫn
  Writer Agent tự lồng CTA tự nhiên, vừa có bước check/tự sửa độc lập nếu Writer
  quên disclosure. Dùng khi 1 content brief có cta_type="affiliate_flight".
  Trigger: brief trong content_queue có cta_type="affiliate_flight" và field
  affiliate_link đã được điền (Nobitano điền tay trong Airtable, KHÔNG để agent tự bịa).
---

# Affiliate Injector — Trùm Sân Bay

Đây là lớp mở rộng NHỎ vào pipeline có sẵn của Trùm Sân Bay để bán affiliate vé máy
bay — không phải hệ thống mới, chỉ thêm 2 điểm chạm vào `orchestrator.py`:
1. `WRITER_SYSTEM_PROMPT` — hướng dẫn Writer lồng CTA tự nhiên khi có affiliate_link.
2. `inject_affiliate_block()` — guardrail độc lập, check + tự sửa nếu Writer quên.

## Vì sao cần 2 lớp (prompt + code check), không chỉ prompt

LLM có thể quên hướng dẫn trong prompt, đặc biệt khi caption dài hoặc topic phức
tạp. Thay vì tin tưởng 100% Writer làm đúng, `inject_affiliate_block()` chạy SAU
Writer, tự kiểm: caption có link chưa, có chữ "affiliate"/"liên kết" chưa — thiếu
cái nào thì tự thêm vào cuối caption. Đảm bảo không có caption nào lọt qua Review
Queue mà thiếu disclosure, dù Writer LLM có sai sót.

## Quy trình đầy đủ (từ Ideation tới Publish)

1. **Ideation Agent** tag topic phù hợp affiliate (góc "tìm vé rẻ/deal vé") với
   `cta_type="affiliate_flight"`, để trống `affiliate_link` — tối đa 1 post/tuần
   loại này (tránh spam affiliate làm mất tin tưởng audience).
2. **Nobitano điền tay** `affiliate_link` trong Airtable (content_queue record) —
   đây là bước THỦ CÔNG bắt buộc, vì link phải khớp đúng chương trình affiliate
   thật đang chạy (Traveloka/Agoda Flights/Skyscanner...), agent không được đoán.
3. **Writer Agent** chạy như bình thường, nhưng nếu brief có `cta_type="affiliate_flight"`
   VÀ `affiliate_link` đã điền → prompt tự thêm block AFFILIATE, hướng dẫn lồng CTA
   tự nhiên theo giọng Trùm Sân Bay.
4. **inject_affiliate_block()** chạy ngay sau Writer, tự check/sửa nếu thiếu link
   hoặc thiếu disclosure trên bất kỳ platform nào.
5. Vào `PENDING_REVIEW` như bình thường — Nobitano review thấy rõ caption có
   affiliate link + disclosure trước khi approve, không có gì khác biệt về UX review.

## Guardrail

- KHÔNG bao giờ để caption có affiliate link mà thiếu disclosure — `inject_affiliate_block`
  là lớp chặn cuối, không phụ thuộc hoàn toàn vào Writer LLM.
- KHÔNG tự bịa affiliate_link — nếu field này trống trong Airtable, `inject_affiliate_block`
  tự bỏ qua (return `injected: False`), không có gì được thêm vào caption.
- Tối đa 1 post/tuần loại `affiliate_flight` — quy định trong Ideation prompt, tránh
  audience thấy kênh "bán hàng" quá nhiều, mất tin tưởng vào giọng insider vốn có.
- Disclosure text cố định (`AFFILIATE_DISCLOSURE_VI` trong code) — không đổi tự do
  giữa các post, giữ nhất quán để dễ audit sau này nếu cần.

## Việc CHƯA làm (cần Nobitano)

- Đăng ký chương trình affiliate vé máy bay thật (Traveloka/Agoda Flights/Skyscanner) —
  chưa có trong kho, không có link nào chạy được cho tới khi đăng ký xong.
- Thêm field `affiliate_link` vào bảng `content_queue` trên Airtable nếu chưa có
  (cần thao tác tay trên Airtable UI, không phải việc code).
- Sau vài tuần chạy thật, xem lại CTR/conversion của post affiliate_flight để quyết
  định có tăng tần suất hơn 1 post/tuần hay không.

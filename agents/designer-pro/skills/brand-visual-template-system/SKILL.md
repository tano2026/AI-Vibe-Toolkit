---
name: brand-visual-template-system
description: >
  Tổng quát hoá agents/trum-san-bay/skills/brand-design-system (khoá cứng
  1 brand) thành hệ dùng chung cho MỌI brand — poster/thumbnail/
  infographic đúng nhận diện, tự tra token từ content-brand-playbooks.md
  thay vì hardcode màu. Không lặp lại design-quality-gate (QA cuối) — chỉ
  lo phần TRƯỚC: chọn đúng token + đúng khung kích thước theo định dạng.
---

# Brand Visual Template System

## TL;DR
`brand-design-system` (Trùm Sân Bay) đã chứng minh mô hình "gác cổng visual trước khi đăng" hoạt động — nhưng token màu hardcode, chỉ dùng được 1 brand. Skill này tách phần LOGIC ra dùng chung, phần TOKEN tra động theo brand đang làm.

## Khi nào dùng
- Trước khi tạo poster/thumbnail/infographic cho BẤT KỲ brand nào (ABTRIP/Tano Cafe/Wonder Mart/Trùm Sân Bay/GMSP)
- Sau khi Visual Agent/google-flow-mcp gen xong ảnh thô, TRƯỚC khi đăng

## Nội dung skill / prompt

### Bước 1 — Tra token đúng brand (KHÔNG hardcode)

```
1. Xác định đang làm cho brand nào (5 brand trong content-brand-
   playbooks.md: ABTRIP/Trùm Sân Bay/Airfare Decoded, Tano Cafe,
   Wonder Mart, Tano Agency, GMSP)
2. Đọc đúng section brand đó trong content-brand-playbooks.md — lấy
   tone màu/phong cách đã mô tả
3. Nếu brand đã có design token CỨNG riêng (như Trùm Sân Bay:
   --tsb-navy-dark #0a1628, --tsb-gold #FFD700) → dùng đúng token đó,
   KHÔNG suy diễn lại
4. Nếu brand CHƯA có token cứng → tự đề xuất dựa trên playbook, xin
   Nobitano xác nhận 1 lần, rồi coi như token cố định từ đó về sau
```

### Bước 2 — Khung kích thước theo ĐÚNG định dạng (khác nhau, không dùng chung 1 size)

```
POSTER
  Dọc: 1080x1350 (Instagram/Facebook feed) hoặc 1080x1920 (Story/Reels
  cover) — chữ lớn, đọc được khi thu nhỏ, 1 thông điệp chính duy nhất

THUMBNAIL
  YouTube: 1280x720 (16:9) — chữ PHẢI đọc được ở kích thước 120x67px
  (thumbnail trong feed rất nhỏ) — đúng tiêu chí "thumbnail test 20%"
  đã có trong design-quality-gate, KHÔNG lặp lại ở đây, chỉ nhắc áp dụng
  TikTok/Shorts cover: 1080x1920 (9:16)

INFOGRAPHIC
  Dọc dài: 1080x2000+ (tuỳ lượng thông tin) — PHẢI có hệ thống phân cấp
  rõ (tiêu đề > mục > chi tiết), không phải 1 khung cố định như poster
```

### Bước 3 — QA cuối — trỏ tới skill đã có, không viết lại

```
Sau khi áp đúng token + khung kích thước → chạy design-quality-gate
(8 tiêu chí: contrast/safe-zone/thumbnail-test/font-hierarchy/license...)
— đây là bước GATE CUỐI, không thuộc phạm vi skill này
```

### Vị trí trong pipeline (mượn nguyên cấu trúc đã chứng minh từ Trùm Sân Bay)

```
Visual Agent (gen ảnh thô qua google-flow-mcp/Nano Banana)
        ↓
Brand Visual Template System (Bước 1+2 — đúng token, đúng khung)
        ↓
design-quality-gate (Bước 3 — QA cuối, 8 tiêu chí)
        ↓
Media Pro (đăng đúng platform qua Postiz)
```

## Setup từng bước
1. Xác định brand + định dạng cần làm (poster/thumbnail/infographic)
2. Tra token đúng brand (Bước 1) — brand đã có token cứng thì dùng luôn
3. Chọn khung kích thước đúng định dạng (Bước 2)
4. Tạo ảnh qua google-flow-mcp hoặc công cụ design khác, áp đúng token+khung
5. Chạy design-quality-gate trước khi coi là xong

## Ví dụ thực tế
Cần thumbnail YouTube cho Wonder Mart — tra `content-brand-playbooks.md` mục "E-commerce (Wonder Mart)" lấy tone màu, vì Wonder Mart CHƯA có token cứng như Trùm Sân Bay → đề xuất token dựa trên playbook, xin Nobitano xác nhận 1 lần → từ đó áp cố định cho mọi thumbnail Wonder Mart sau này, không phải hỏi lại mỗi lần.

## Lưu ý / Lỗi thường gặp
- Dùng chung 1 khung kích thước cho cả poster/thumbnail/infographic — 3 định dạng có mục đích và ràng buộc khác hẳn nhau (đọc trên feed lớn vs đọc trong ô nhỏ 120x67px vs đọc cuộn dài)
- Tự suy token màu mới mỗi lần thay vì tra/xác nhận 1 lần rồi cố định — gây không nhất quán giữa các lần tạo ảnh cùng 1 brand
- Bỏ qua design-quality-gate vì "nhìn ổn rồi" — 2 skill này KHÁC PHẠM VI (skill này lo trước, QA lo sau), không thay thế nhau

## Đánh giá cá nhân
- Điểm mạnh: không viết lại từ đầu — tổng quát hoá đúng mô hình đã chứng minh hoạt động (Trùm Sân Bay), tận dụng content-brand-playbooks.md đã có sẵn, không chồng chéo design-quality-gate
- Điểm yếu: 4/5 brand chưa có token màu CỨNG (chỉ Trùm Sân Bay có) — lần đầu dùng cho brand khác sẽ cần 1 vòng xác nhận với Nobitano trước khi chạy trơn tru
- Có nên dùng: 8/10 — đáng dùng ngay, nhưng cần làm rõ 2 hệ Designer song song (roles/designer.md vs designer-pro/) trước khi coi đây là chuẩn chính thức duy nhất

## Link
- Mô hình gốc: agents/trum-san-bay/skills/brand-design-system (1 brand, đã chứng minh hoạt động)
- Nguồn token: agents/content-pro/content-brand-playbooks.md
- Dùng cùng: design-quality-gate (QA cuối, không lặp lại ở đây)

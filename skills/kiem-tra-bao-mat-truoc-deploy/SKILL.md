---
name: kiem-tra-bao-mat-truoc-deploy
description: >
  Checklist 7 lỗi bảo mật "toang ngầm" phổ biến nhất trong app vibe coding — chỉ lộ ra SAU
  khi đã deploy, không phải lúc code trên máy local. Dùng bắt buộc trước khi đẩy bất kỳ app
  nào ra production, đặc biệt app có payment (Wonder Mart) hoặc data khách hàng (ABTRIP).
  Nguồn: TikTok @caothanhphng5.
---

# Kiểm tra Bảo mật Trước Deploy — 7 Lỗi Toang Ngầm trong App Vibe Coding

## TL;DR
7 lỗi này đều có đặc điểm chung: **code chạy ngon trên máy, nhìn UI vẫn ổn, nhưng toang thật
sự chỉ lộ ra sau khi deploy** — vì bản chất là lỗ hổng ở tầng server/data/quy trình, không phải
lỗi hiển thị. Vibe coding dễ dính đủ cả 7 vì AI thường tối ưu cho "chạy được" chứ không tự động
tối ưu cho "an toàn khi có người dùng thật + có kẻ xấu thật".

## Khi nào dùng
- Bắt buộc chạy qua checklist này trước khi deploy bất kỳ app nào ra production — không có
  ngoại lệ "app nhỏ không cần" vì cả 7 lỗi đều không phụ thuộc quy mô app.
- **Đặc biệt bắt buộc** với app có payment (Wonder Mart e-commerce) hoặc data khách hàng nhạy
  cảm (ABTRIP booking, thông tin cá nhân khách Fast Track).
- Dùng cả khi review code do AI viết (Claude Code/Cursor) lẫn code tự viết tay.

## Nội dung skill / checklist

```
## 1. Secret nằm ngay trong code
API key, password bị commit lên repo hoặc nằm lộ liễu ở frontend (đọc được qua DevTools).
Kiểm tra: search "sk-", "password", "api_key", "token" trong toàn bộ codebase + git history.
Ra kết quả = đang bị leak ngay lúc này, không phải rủi ro tương lai.
Fix: mọi secret qua biến môi trường (.env, KHÔNG commit .env lên git), rotate ngay secret nào
đã từng lộ (đổi key mới, key cũ coi như đã bị lộ vĩnh viễn dù đã xoá khỏi code).

## 2. Fake security — UI không phải là security
Ẩn 1 button trên giao diện KHÔNG đồng nghĩa hệ thống an toàn. Hacker không dùng UI của bạn,
họ gọi thẳng vào API bằng Postman/curl — bỏ qua hoàn toàn lớp giao diện.
Kiểm tra: thử gọi thẳng API endpoint (không qua UI) bằng công cụ như Postman — nếu vẫn thực
hiện được hành động mà lẽ ra chỉ role admin mới làm được, đây là lỗ hổng thật.
Fix: MỌI endpoint phải tự kiểm tra quyền (authorization) ở phía server, không dựa vào việc
ẩn nút trên UI.

## 3. Data leak — lỗi phổ biến nhất nhưng ít ai test
User A xem được data của User B — thường do endpoint kiểu `/api/order/{id}` không kiểm tra
ID đó có thuộc về user đang gọi hay không (IDOR — Insecure Direct Object Reference).
Kiểm tra: tạo 2 account test. Lấy ID resource (đơn hàng, hồ sơ...) của account 1, gọi API lấy
resource đó bằng session của account 2. Nếu lấy được → toang, phải fix ngay trước khi deploy.
Fix: mọi API trả về resource theo ID phải kiểm tra resource đó có thuộc về user đang gọi
(hoặc user có quyền xem) hay không, không chỉ dựa vào việc "biết đúng ID".

## 4. Không ai báo lỗi cho bạn
Không có error tracking = không biết app đang lỗi ở đâu. User gặp lỗi không report, họ chỉ
âm thầm thoát app. Không có log nghĩa là đang vận hành app trong tình trạng mù thông tin.
Fix: gắn error tracking cơ bản trước khi deploy (kể cả chỉ là log ra file/Telegram báo lỗi cho
CEO) — không cần công cụ đắt tiền, chỉ cần CÓ, đừng để bằng 0.

## 5. Backup "niềm tin" — có backup nhưng chưa từng restore
Có chạy backup định kỳ không đồng nghĩa backup đó dùng được. Nếu chưa từng thử restore thật,
đó chỉ là "niềm tin có backup", không phải backup thật.
Fix: định kỳ (vd hàng quý) thử restore backup ra 1 môi trường test, xác nhận dữ liệu khôi phục
đúng và đủ. Chưa test restore = coi như chưa có backup.

## 6. Payment dễ bị hack — tin dữ liệu từ frontend
Giá tiền gửi lên từ client (frontend tự tính rồi gửi số tiền cho server), hoặc webhook thanh
toán không verify chữ ký — hacker chỉnh sửa giá trước khi gửi lên = mất tiền thật.
Fix: giá tiền LUÔN tính lại ở server dựa trên dữ liệu server có (không tin số tiền client gửi
lên); mọi webhook từ cổng thanh toán phải verify chữ ký/signature theo đúng tài liệu nhà cung
cấp trước khi xử lý.

## 7. AI phá ngầm — AI tự sửa code mà bạn không biết
AI (Claude Code/Cursor) đôi khi tự sửa/xoá phần code không liên quan tới yêu cầu — đúng vấn đề
Karpathy Coding Guidelines đã cảnh báo (xem `agents/KARPATHY-CODING-GUIDELINES.md`, nguyên tắc
3 "Surgical Changes"). Những chỗ không check kỹ diff = nơi dễ lỗi nhất.
Fix: có test tự động (snapshot test cho UI, e2e test cho luồng nghiệp vụ chính) — không dựa
vào việc "đọc diff bằng mắt" cho mọi lần AI sửa code, vì mắt người dễ bỏ sót thay đổi ngầm.
```

## Setup từng bước
1. Copy checklist trên vào 1 file `PRE-DEPLOY-CHECKLIST.md` riêng cho mỗi project, hoặc dùng
   trực tiếp làm system prompt khi giao Claude Code review code trước khi deploy.
2. Chạy qua đủ 7 mục TRƯỚC MỖI LẦN deploy — không chỉ lần đầu, vì mỗi lần thêm feature mới có
   thể tái tạo lại đúng những lỗ hổng này (đặc biệt #3 Data leak và #6 Payment).
3. Với app có payment (Wonder Mart), làm thêm bước: yêu cầu Claude Code tự rà lại toàn bộ luồng
   thanh toán đối chiếu đúng mục #6 trước khi merge bất kỳ PR nào đụng tới payment.

## Ví dụ thực tế
Trước khi deploy tính năng mới cho Wonder Mart (thêm mã giảm giá), chạy qua checklist: mục #6
phát hiện code đang tính giá cuối cùng (sau giảm giá) ở frontend rồi gửi thẳng số tiền đó lên
server để tạo đơn — đúng lỗ hổng "tin dữ liệu từ frontend". Fix trước khi deploy: server tự
tính lại giá dựa trên mã giảm giá + giá gốc lưu trong DB, không nhận số tiền cuối từ client.

## Lưu ý / Lỗi thường gặp
- Cả 7 lỗi đều KHÔNG lộ ra khi test trên máy local với 1 user, 1 luồng dùng bình thường — chỉ
  lộ khi có nhiều user thật hoặc có người cố tình thử phá (đúng nghĩa "toang ngầm").
- Đừng coi checklist này là làm 1 lần rồi xong — feature mới có thể tái tạo lại lỗ hổng cũ nếu
  không chạy lại checklist mỗi lần deploy.
- Mục #7 (AI phá ngầm) đặc biệt liên quan trực tiếp tới toàn bộ agent package trong kho đang
  dùng Claude Code/Karpathy Guidelines — nhắc lại: guideline chỉ giảm rủi ro, KHÔNG thay thế
  được việc có test tự động thật.

## Đánh giá cá nhân
- Điểm mạnh: 7 lỗi đều là lỗ hổng THẬT rất phổ biến trong app vibe-coded, trình bày ngắn gọn dễ
  nhớ, có hướng kiểm tra cụ thể (không chỉ nói lý thuyết) cho từng mục.
- Điểm yếu: đây là checklist tổng quát, không đi sâu kỹ thuật (vd không hướng dẫn cụ thể cách
  verify webhook signature cho từng cổng thanh toán VN như VNPay/MoMo) — cần tra thêm doc riêng
  từng nhà cung cấp khi triển khai thật.
- Có nên dùng không: 9/10 — bắt buộc áp dụng cho mọi app sắp deploy, đặc biệt Wonder Mart
  (payment) và ABTRIP (data khách hàng nhạy cảm).

## Link
- Nguồn: TikTok @caothanhphng5 — "7 lỗi toang ngầm trong app vibe coding mà mình thấy lặp đi
  lặp lại (chỉ lộ sau khi deploy)"

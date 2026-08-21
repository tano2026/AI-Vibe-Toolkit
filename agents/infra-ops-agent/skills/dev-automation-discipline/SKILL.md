---
name: dev-automation-discipline
description: >
  Vận hành hoá phần còn lại của EXPERT-CORE.md section ⑤ DEV & AUTOMATION
  chưa được destructive-command-guardrail bao phủ — luật debug, credential,
  script idempotency, và ĐẶC BIỆT luật no-fabrication riêng cho Hermes (đã
  có tiền sử fabricate repo contents, xác nhận lại qua sự cố thật vụ
  vn-web-research). Dùng cho mọi task Dev/Automation trên Hermes/OpenClaw/
  Antigravity, không chỉ lệnh phá hủy.
---

# Dev & Automation Discipline

## TL;DR
`destructive-command-guardrail` đã lo tốt phần "lệnh nguy hiểm + rollback". Skill này lo phần còn lại: cách debug đúng trình tự, cách giữ credential an toàn, cách viết script không tự phá khi chạy lại, và quan trọng nhất — **không được khẳng định trạng thái hệ thống/repo mà không có bằng chứng lệnh/API vừa chạy**.

## ⚠️ Vì sao luật no-fabrication đứng đầu, không phải phụ
Đây không phải rủi ro lý thuyết. Trong chính dự án này, "Hermes" đã báo cáo `AI-Vibe-Toolkit` "không tồn tại" trên GitHub và nghi ngờ 1 skill tên `vn-web-research` "vừa gộp" — khi verify lại bằng API thật, `AI-Vibe-Toolkit` **có tồn tại** (chỉ là private repo, cách check của Hermes không thấy được), còn `vn-web-research` thì **không xác nhận được vị trí thật**. Đây đúng loại lỗi EXPERT-CORE đã cảnh báo trước — không phải nói dối cố ý, mà là báo cáo trạng thái mà không tự verify bằng lệnh/API thật trước khi khẳng định.

## Khi nào dùng
- Bất kỳ lúc nào Hermes/OpenClaw/Antigravity cần báo cáo trạng thái hệ thống/repo/file
- Trước khi sửa lỗi (debug) bất kỳ vấn đề gì trên VPS/pipeline
- Khi soạn/chạy script tự động (cron, retry logic)
- Khi cần dùng/lưu credential (API key, token)

## Nội dung skill / prompt

### 1. Luật no-fabrication (bắt buộc, đặc biệt cho Hermes)

```
MỌI claim về trạng thái repo/hệ thống PHẢI kèm bằng chứng lệnh/API vừa
chạy — không có output lệnh = KHÔNG được khẳng định.

SAI:  "Repo AI-Vibe-Toolkit không tồn tại" (dựa vào list không đầy đủ,
       không kèm lệnh/output cụ thể đã chạy)
ĐÚNG: "Đã chạy `GET api.github.com/repos/tano2026/AI-Vibe-Toolkit` với
       token — response 200, private=true. Repo có tồn tại." (kèm bằng
       chứng cụ thể)

Nếu KHÔNG chắc chắn (chưa verify được) → nói rõ "chưa verify được, cần
chạy lệnh X để xác nhận" — KHÔNG suy đoán rồi trình bày như sự thật.

Trước khi báo cáo bất kỳ điều gì về kho/hệ thống → tự hỏi: "Tao vừa chạy
lệnh gì để biết điều này? Có output cụ thể không?" Không có → chưa được
báo cáo như fact.
```

### 2. Luật debug (trình tự cứng, không nhảy bước)

```
1. TÁI HIỆN lỗi — chạy lại được lỗi đó, không phải "nghe mô tả rồi đoán"
2. CÔ LẬP — binary search phạm vi (thu hẹp dần chỗ nào gây lỗi)
3. ROOT CAUSE — tìm nguyên nhân gốc, không fix triệu chứng bề mặt
4. FIX — sửa đúng chỗ đã xác định ở bước 3
5. VERIFY — chạy lại để xác nhận lỗi thật sự hết, không phải "chắc là hết rồi"
6. POSTMORTEM 5 dòng — ghi vào activity_log: lỗi gì / nguyên nhân / đã sửa
   gì / verify bằng cách nào / phòng ngừa lần sau

Fix mà KHÔNG tái hiện được lỗi trước đó = đoán mò, không phải debug thật.
```

### 3. Luật credential

```
- Token/key CHỈ ở biến môi trường (env var), không hard-code vào script
- Mỗi agent 1 token riêng, quyền TỐI THIỂU cần thiết (agent chỉ đọc kho
  → dùng read-only token, không dùng token full quyền cho việc chỉ đọc)
- Nghi ngờ lộ credential → ROTATE NGAY, không chờ xác nhận thêm
- KHÔNG BAO GIỜ log giá trị credential ra bất kỳ đâu (console, file log,
  báo cáo gửi Telegram...)
```

### 4. Luật script

```
- Mọi script chạy lặp (cron, retry) phải IDEMPOTENT — chạy 2 lần liên tiếp
  không được gây hỏng/trùng lặp dữ liệu
- Mọi call ra ngoài (API, network) PHẢI có timeout — không để treo vô hạn
- Lỗi phải FAIL TO TIẾNG — log + báo Telegram, KHÔNG nuốt exception (try/
  except rồi im lặng bỏ qua = lỗi ẩn, phát hiện muộn hơn nhiều)
```

### Anti-pattern (tự kiểm tra không mắc phải)

```
❌ Sửa thẳng trên production "cho nhanh" — luôn qua rollback plan
   (destructive-command-guardrail) dù chỉ 1 dòng
❌ Cron chồng cron không ai nhớ — mỗi cron job cần ghi chú rõ mục đích +
   người tạo + ngày tạo
❌ requirements không pin version — dễ vỡ khi dependency tự update
❌ "Works on my machine" — môi trường Hermes CHỈ có urllib.request,
   không có lib ngoài; test trên máy có pip install rồi tưởng Hermes
   chạy được y vậy là sai
```

## Setup từng bước
1. Trước khi báo cáo bất kỳ trạng thái hệ thống nào → tự hỏi có bằng chứng lệnh vừa chạy không (mục 1)
2. Gặp lỗi → chạy đủ 6 bước debug, không nhảy thẳng vào fix (mục 2)
3. Cần dùng credential → check đã đúng env var, đúng scope tối thiểu chưa (mục 3)
4. Viết script mới → tự hỏi "chạy lại được không, có timeout chưa, lỗi có báo ra ngoài không" (mục 4)

## Ví dụ thực tế
Case thật đã xảy ra: Hermes báo "AI-Vibe-Toolkit không tồn tại" dựa trên việc list repo mà không kèm bằng chứng đã dùng đúng token/phương thức nào. Áp luật no-fabrication: đúng ra phải báo "Đã thử list repo của tano2026, thấy 4 kết quả, KHÔNG THẤY AI-Vibe-Toolkit — nhưng chưa chắc cách list này có bắt được private repo không, cần verify thêm bằng cách gọi trực tiếp `GET /repos/tano2026/AI-Vibe-Toolkit` kèm token." — khác hẳn khẳng định chắc "không tồn tại".

## Lưu ý / Lỗi thường gặp
- No-fabrication không có nghĩa là không được nói "tao nghĩ..." — được phép suy đoán, nhưng phải NÓI RÕ đó là suy đoán, không phải fact đã verify
- Debug bỏ qua bước "tái hiện" là lỗi phổ biến nhất — sửa code dựa trên đoán nguyên nhân, không confirm lại đã đúng nguyên nhân đó chưa
- Anti-pattern "works on my machine" đặc biệt nguy hiểm với Hermes vì môi trường bị giới hạn nghiêm ngặt (urllib only) — code test trên máy dev bình thường rồi đưa Hermes chạy dễ vỡ ngay

## Đánh giá cá nhân
- Điểm mạnh: luật no-fabrication có bằng chứng thật trong chính dự án này, không phải lý thuyết suông — dễ thuyết phục áp dụng nghiêm túc
- Điểm yếu: luật debug/credential/script là nguyên tắc tốt nhưng khó đo lường tuân thủ tự động — phụ thuộc agent tự giác áp dụng
- Có nên dùng: 10/10 cho phần no-fabrication (không thương lượng), 8/10 cho phần còn lại

## Link
- Nguồn gốc luật: `agents/company/EXPERT-CORE.md` section ⑤ DEV & AUTOMATION
- Case thật: sự cố Hermes báo sai trạng thái repo AI-Vibe-Toolkit (hội thoại 21/08/2026)
- Bổ sung cho: `agents/infra-ops-agent/skills/destructive-command-guardrail/SKILL.md`

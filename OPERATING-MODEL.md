# OPERATING MODEL — Brief giao việc cho Trio (Hermes/OpenClaw 2.0/DeepSeek Harness)
> Viết 22/08/2026. Đây là bản đóng gói TOÀN BỘ mô hình đã thiết kế, dành
> để Trio TRIỂN KHAI THẬT — không chỉ đọc hiểu. Mỗi Vessel có checklist
> hành động riêng ở cuối file. Thay thế tài liệu tham khảo chính cho
> ARCHITECTURE.md + COMPANY-CHARTER.md (2 file đó vẫn giữ, đọc thêm chi
> tiết nếu cần, nhưng file này là điểm bắt đầu).

---

## 1 câu tóm tắt

**1 bộ luật + 8 năng lực + 5 nơi chạy, có người gác cổng trước và sau.**

---

## Lớp 1 — Luật (không đổi theo agent nào, đọc 1 lần)

| File | Nội dung |
|---|---|
| agents/company/EXPERT-CORE.md | 8 section ngưỡng số cứng — 1 cho mỗi năng lực ở Lớp 2 |
| agents/company/CORE-META-SKILLS.md | Luật vận hành chung (harness/loop/humanizer) — áp mọi năng lực |

## Lớp 2 — 8 Năng lực ("Talent")

```
Research . Content . Sales . Marketing . Dev . Media . Designer .
Customer Satisfaction
```

Mỗi cái sống ở agents/<ten-agent>/ = đúng 1 section EXPERT-CORE + skill riêng + HERMES-ADAPTER.md. Không năng lực nào tự bịa luật ngoài EXPERT-CORE.

## Lớp 3 — 5 Nơi chạy ("Vessel") — trạng thái THẬT, không tô hồng

| Vessel | Việc gì | Trạng thái 22/08/2026 |
|---|---|---|
| Hermes | Task rời rạc, Python, urllib-only | Sẵn sàng kỹ thuật, chưa xác nhận GITHUB_TOKEN hoạt động thật |
| OpenClaw 2.0 | Điều phối chính, nhận lệnh Telegram/WhatsApp | Đang chạy, chưa gắn EA Gate vào luồng route thật |
| DeepSeek Harness | Code phức tạp, GitHub workflow | Chưa có kết nối trực tiếp vào kho — mượn quyết định qua OpenClaw |
| Antigravity | Hạ tầng, VPS, cron | Xác nhận là Google Antigravity 2.0 thật, đã cài |
| Claude Code | Local Windows | Symlink 591 skill xong, test thật đang treo (lỗi proxy chưa rõ nguyên nhân) |

---

## Luồng 1 task đi qua hệ thống

```
Nobitano ra lệnh
      |
      v
EA Gate (skill: task-intake-quality-gate) — 4 câu hỏi:
  1. Đúng năng lực nào trong 8 cái?
  2. Đủ thông tin chưa? (hỏi TỪNG câu 1, không hỏi dồn)
  3. Có phạm EXPERT-CORE ngay từ đầu không?
  4. Độ khẩn — cần Nobitano quyết ngay hay xếp hàng?
      |
      v
Route vào đúng 1 Năng lực (Lớp 2), chạy trên đúng 1 Vessel (Lớp 3)
      |
      v
Việc nhiều bước (dev/deploy) -> chuỗi ADLC:
  intent.md -> spec.md -> plan.md -> code+tests -> review record ->
  production signal -> (lỗi/sự cố tự vòng lại thành intent mới,
  qua Jev phân loại — CHƯA test thật, còn waitlist)
      |
      v
critical-path-briefing — báo Nobitano CHỈ việc cần quyết định của
Nobitano, không liệt kê mọi thứ đang chạy bình thường
```

Jev (TypeSafe) đứng RIÊNG, cắt ngang mọi tầng — lọc quyết định nhanh/rẻ (Choice/Score/Noul) trước khi việc tới Claude. Còn early access/waitlist, chưa có API key thật — dùng fallback rule-based tạm thời (xem từng skill có nhắc Jev).

---

## CHECKLIST HÀNH ĐỘNG — MỖI VESSEL TỰ LÀM PHẦN MÌNH

### Hermes — 3 việc

```
[ ] 1. Verify GITHUB_TOKEN đã set đúng biến môi trường — test bằng
       cách fetch thử agents/company/EXPERT-CORE.md, xác nhận đọc
       được nội dung thật (không phải lỗi 401/404)
[ ] 2. Test fetch_skill_from_kho() với ĐÚNG 1 Pro Agent bất kỳ (gợi ý:
       sales-ceo, đã có sẵn HERMES-ADAPTER.md đầy đủ) — xác nhận nạp
       được skill thật, không phải giả lập
[ ] 3. Báo cáo kết quả qua Telegram — chỉ báo PASS/FAIL từng bước,
       không cần giải thích dài (đúng critical-path-briefing)
[ ] 4. (MỚI 22/08) Cài hermes-jev-skills, bắt đầu shadow mode — xem
       repos/hermes-jev-skills.md + agents/company/skills/
       hermes-autonomous-kho-maintenance/SKILL.md
```

### OpenClaw 2.0 — 3 việc

```
[ ] 1. Đọc agents/company/skills/task-intake-quality-gate/SKILL.md
       — implement 4 câu hỏi gác cổng vào code routing THẬT (hiện
       chỉ có thiết kế trên giấy, chưa chạy trong luồng thật)
[ ] 2. Khi route task vào 1 Pro Agent — tự động fetch đúng
       HERMES-ADAPTER.md hoặc README.md của agent đó TRƯỚC khi
       dispatch, không route mù
[ ] 3. Áp critical-path-briefing cho báo cáo OpenClaw tự gửi Nobitano
       — lọc bớt, chỉ đưa việc cần quyết định
```

### DeepSeek Harness — 1 việc DUY NHẤT trước (đừng làm gì khác trước việc này)

```
[ ] 1. THIẾT LẬP KẾT NỐI ĐẦU TIÊN vào kho — hiện tại con số kết nối
       là 0. DSH dùng kiến trúc Cordis riêng (dsh plugin --profile
       web add <package>) — cần viết 1 Cordis plugin nhỏ bọc quanh
       GitHub API fetch (tương tự cách Hermes làm qua urllib, nhưng
       đóng gói đúng format plugin DSH yêu cầu)

       CHƯA làm bước 2 (route task thật, tích hợp EA Gate...) cho
       tới khi bước 1 này xong và test được — DSH còn nhiều breaking
       changes (v0.1 developer preview), ưu tiên ổn định trước khi
       mở rộng.
```

---

## Điểm nghẽn thật đang chặn TOÀN BỘ — ưu tiên số 1

Claude Code local chưa chạy được 1 lần thành công (lỗi proxy nội bộ "không có trong bảng giá hiện hành" — nguyên nhân thật chưa xác định, 3 lệnh chẩn đoán PowerShell đã đưa nhưng chưa chạy). Mọi checklist trên đúng trên giấy — chưa ai kiểm chứng cả hệ hoạt động thật cho tới khi ít nhất 1 Vessel chạy trơn tru 1 lần.

## Việc CHƯA làm — nói thẳng, không giấu

- 0/5 Vessel đã confirm hoạt động đầy đủ end-to-end
- DeepSeek Harness: 0 kết nối, cần làm từ số 0
- Jev cascade: thiết kế xong, 0% test thật (waitlist)
- ADLC feedback loop (production signal -> intent tự động): thiết kế xong, chưa chạy lần nào
- Client Onboarding Template: 0 khách thật đã test

## Link
- Chi tiết đầy đủ: ARCHITECTURE.md (sơ đồ kỹ thuật), agents/company/COMPANY-CHARTER.md (mô hình tổ chức, nguồn OPC/OMC)
- Luật gốc: agents/company/EXPERT-CORE.md
- Cách xây năng lực mới: skills/agentic-factory/SKILL.md (v2, 8 bước)

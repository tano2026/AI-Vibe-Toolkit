---
name: deploy-review-gate
description: >
  Dual independent review (dùng cơ chế santa-method có sẵn trong kho) cho
  kế hoạch deploy/thay đổi hạ tầng RỦI RO CAO — khác destructive-command-
  guardrail (chỉ chặn từng lệnh đơn lẻ), skill này review cả KẾ HOẠCH lớn
  (nhiều bước, có thể mỗi bước không nguy hiểm nhưng tổng thể rủi ro).
  Dùng trước khi đưa plan cho Antigravity thực thi.
---

# Deploy Review Gate

## TL;DR
1 kế hoạch deploy do chính agent soạn ra vẫn mang điểm mù của chính nó (giống lý do Research Pro cần `research-independent-review-gate`). Skill này chạy 2 reviewer độc lập trên TOÀN BỘ plan trước khi Antigravity thực thi — không chỉ chặn từng lệnh nguy hiểm riêng lẻ như `destructive-command-guardrail`.

## Khi nào dùng
- Plan deploy có ≥3 bước liên tiếp trên production VPS
- Thay đổi ảnh hưởng nhiều service cùng lúc (không chỉ 1 lệnh đơn lẻ)
- Migration data, đổi kiến trúc, nâng cấp version lớn
- KHÔNG cần cho thay đổi nhỏ, 1 bước, đã rõ ràng (dùng `destructive-command-guardrail` là đủ)

## Nội dung skill / prompt

### Kiến trúc (mượn nguyên cơ chế santa-method)

```
GENERATOR: Infra Ops Agent soạn plan deploy (đã qua destructive-command-guardrail
           cho từng lệnh riêng lẻ)
        ↓ output = plan đầy đủ các bước
DUAL INDEPENDENT REVIEW (2 reviewer, cùng plan, KHÔNG thấy nhau, KHÔNG thấy
                          lý luận đã soạn plan — chỉ nhận plan cuối + rubric)
        ↓
   Reviewer B                         Reviewer C
   "Ops Reliability"                  "Failure Mode Analyst"
        ↓                                   ↓
VERDICT GATE: B pass VÀ C pass → đưa Antigravity thực thi
              Ngược lại → Fix cycle → chạy lại từ đầu
```

### Rubric Reviewer B — "Ops Reliability" (tính khả thi vận hành)

```
1. Mỗi bước có rollback riêng không, hay chỉ có rollback tổng ở cuối?
   (rollback tổng ở cuối = nếu fail giữa chừng, không biết lùi về đâu)
2. Có bước verify SAU MỖI bước quan trọng không, hay verify dồn 1 lần cuối?
3. Thứ tự các bước có đúng không — có bước nào phụ thuộc bước sau đó chưa
   chạy không (dependency ngược)?
4. Thời gian downtime dự kiến có được ước tính không, có chấp nhận được
   không?

Trả về: PASS hoặc FAIL + danh sách vấn đề cụ thể.
```

### Rubric Reviewer C — "Failure Mode Analyst" (chủ động tìm cách phá plan)

```
Nhiệm vụ DUY NHẤT: tìm ra kịch bản plan này THẤT BẠI giữa chừng thì chuyện
gì xảy ra.

1. Nếu mất kết nối mạng giữa bước 3 và bước 4 — hệ thống ở trạng thái gì?
   Có tự phục hồi được không hay cần can thiệp tay?
2. Nếu 1 bước chạy 2 lần (do retry tự động/nhấn nhầm) — có an toàn không
   (idempotent) hay sẽ hỏng?
3. Có phụ thuộc nào vào trạng thái hiện tại (giả định máy đang chạy đúng
   thế này) mà nếu sai giả định thì cả plan sụp không?
4. Nếu là người phải xử lý sự cố lúc 2h sáng khi plan này fail — thông tin
   trong plan có đủ để debug không, hay phải đoán?

Trả về: PASS (không tìm ra kịch bản fail nghiêm trọng) hoặc FAIL + kịch
bản fail cụ thể nhất tìm được.
```

### Nguyên tắc bất biến (kế thừa santa-method)

- Context isolation tuyệt đối — 2 reviewer không thấy nhau, không thấy bản thảo/lý luận đã soạn plan
- 1 FAIL → sửa plan → chạy lại CẢ HAI reviewer, không chỉ sửa chỗ vừa fail
- Giới hạn 3 vòng fix-and-recheck — quá đó, escalate cho Nobitano tự quyết thay vì lặp vô hạn

## Setup từng bước
1. Plan deploy đã soạn xong, đã qua `destructive-command-guardrail` cho từng lệnh → đưa vào skill này để review toàn bộ
2. Spawn Reviewer B và C với prompt riêng biệt, chỉ đưa plan cuối cùng
3. Cả 2 PASS → đưa Antigravity thực thi kèm ghi chú "đã qua dual-review"
4. 1 FAIL → sửa theo đúng vấn đề đã chỉ ra → quay lại bước 2, tối đa 3 vòng

## Ví dụ thực tế
Plan deploy MeshLLM/DeepSeek Harness lên VPS (nhiều bước: cài dependency, config network, khởi động service, test kết nối) — Reviewer C (Failure Mode) có thể phát hiện: "Bước 3 khởi động service giả định bước 2 (config network) đã hoàn tất và network đã sẵn sàng, nhưng plan không có bước verify network trước khi qua bước 3 — nếu network chưa sẵn sàng, service khởi động lỗi, plan không có hướng dẫn debug tại điểm này."

## Lưu ý / Lỗi thường gặp
- Đừng dùng skill này cho lệnh đơn lẻ đơn giản — đó là việc của `destructive-command-guardrail`, dùng cả 2 lớp cho 1 lệnh nhỏ là lãng phí
- Reviewer C dễ bị hiểu nhầm là "tiêu cực quá mức" — nhắc rõ nhiệm vụ chỉ là tìm điểm yếu thật, không phải bôi bác plan

## Đánh giá cá nhân
- Điểm mạnh: bắt được lỗi "toàn cục" (thứ tự bước, dependency, failure mode) mà check từng lệnh riêng lẻ không bắt được
- Điểm yếu: tốn thời gian/token — chỉ đáng dùng cho deploy lớn, không phải mọi thay đổi
- Có nên dùng: 8/10 cho deploy ≥3 bước hoặc ảnh hưởng nhiều service

## Link
- Cơ chế gốc: `skills/santa-method/SKILL.md`
- Bổ sung cho: `destructive-command-guardrail` (lệnh đơn lẻ) — 2 skill dùng cùng nhau, không thay thế

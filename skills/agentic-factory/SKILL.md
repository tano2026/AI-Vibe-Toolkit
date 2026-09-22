---
name: agentic-factory
description: >
  Nhà sản xuất agentic v2 — đưa vào 1 ý tưởng agent, trả ra trọn bộ sản
  phẩm đóng gói đúng chuẩn 8 Pro Agent đã xây thật (không phải lý thuyết
  suông). Cập nhật sau khi học được: EXPERT-CORE grounding bắt buộc,
  Vessel/Talent (OMC), chuỗi tạo tác ADLC, Jev cascade, EA gate, HR
  lifecycle. Dùng khi Nobitano nói "xây 1 agent về...", "làm sao xây agent
  như vậy", "đóng gói agent...".
---

# Agentic Factory v2 — Nhà sản xuất Agentic

Input: 1 ý tưởng. Output: 1 Pro Agent đúng chuẩn 8 cái đã có, không lệch chất lượng.

## Quy trình 8 bước (v2 — thêm 3 bước so với bản gốc, sau khi xây 8 Pro Agent thật)

### Bước 0 — Search trước khi viết (kỷ luật "HR", bắt buộc)

```
KHÔNG viết gì trước khi search rộng skills/ + agents/ hiện có — đúng bài
học đã xảy ra thật (ecc/ trùng 271 file, ad-budget-testing-discipline
trùng claude-ads). Dùng quy trình trong skill-lifecycle-management.
```

### Bước 1 — Grounding vào EXPERT-CORE (bắt buộc, KHÔNG bịa số)

```
Agent mới thuộc 1 trong 8 role đã có EXPERT-CORE section -> đọc đúng
section đó, không viết luật riêng chồng lên.

Agent thuộc role CHƯA có trong EXPERT-CORE (như case Customer
Satisfaction trước đây) -> BẮT BUỘC research ngưỡng số thật từ nguồn
uy tín ngành (không suy đoán) -> viết thêm 1 section mới vào
EXPERT-CORE.md trước khi làm bước 2.
```

### Bước 2 — Spec the Agent (như bản gốc, giữ nguyên)

```
Tên agent / Domain / Job-to-be-done / Người dùng / Input điển hình /
Output điển hình / Mức tự chủ / Rủi ro cao nhất
```

### Bước 3 — Vessel + Talent (MỚI — thuật ngữ từ OneManCompany, 422 sao)

```
TALENT (năng lực) = EXPERT-CORE section (luật) + skill riêng viết mới
  — đây là phần bản gốc gọi "Capability Map", giữ nguyên logic, đổi tên
  đúng chuẩn đã kiểm chứng

VESSEL (nơi chạy) = xác định NGAY từ đầu agent này chạy trên Vessel nào:
  Hermes (task rời rạc, urllib-only) / OpenClaw (điều phối) /
  Claude Code / Google Antigravity (hạ tầng, đã xác nhận là sản phẩm
  Google thật) — mỗi Vessel cần 1 HERMES-ADAPTER.md riêng nếu áp dụng
```

### Bước 4 — Chuỗi tạo tác ADLC (MỚI — nếu agent làm việc nhiều bước)

```
Nếu agent có deliverable qua nhiều bước (không phải trả lời 1 lần) ->
thiết kế theo chuỗi: intent.md -> spec.md -> plan.md -> code/output+tests
-> review record -> production signal -> (vòng lặp lại intent.md nếu có
tín hiệu vận hành mới)

Agent đơn giản (chỉ tra cứu/phân loại 1 bước) -> bỏ qua bước này, không
ép mọi agent vào khuôn nhiều bước không cần thiết
```

### Bước 5 — Generate the Package (như bản gốc, thêm 2 file)

```
<ten-agent>/
├── README.md              <- Spec + Vessel/Talent + Capability Map
├── ARCHITECTURE.md         <- sơ đồ luồng + chuỗi tạo tác nếu có
├── system-prompt.md
├── HERMES-ADAPTER.md       <- MỚI bắt buộc nếu chạy trên Hermes
├── skills/
│   └── <skill>/SKILL.md    <- viết thật, không để TODO
└── (CHATWOOT/KHOJ-ADAPTER.md nếu cần đa nền tảng, tham khảo Content Pro)
```

### Bước 6 — Jev Cascade (MỚI — chỉ áp nếu có quyết định lặp lại nhanh)

```
Agent có việc PHÂN LOẠI/CHẤM ĐIỂM lặp đi lặp lại (không phải sáng tạo)
-> thiết kế câu hỏi Choice/Score/Noul cho Jev, kèm ngưỡng confidence
  (>=80% tự tin, 50-80% làm nhưng gắn nhãn, <50% escalate Claude)
-> LUÔN kèm fallback rule-based khi Jev chưa có access (còn waitlist)

Agent không có việc phân loại lặp lại (vd Designer tạo ảnh sáng tạo)
-> bỏ qua bước này
```

### Bước 7 — Wire vào hệ thống chung (MỚI — kết nối, không để agent cô lập)

```
1. task-intake-quality-gate: đảm bảo domain agent mới đủ RÕ để câu
   hỏi "đúng agent?" của EA gate route được chính xác vào đây
2. critical-path-briefing: agent mới báo cáo đúng nguyên tắc "chỉ đưa
   việc cần quyết định của Nobitano", không liệt kê hết mọi việc
3. skill-lifecycle-management: đăng ký skill mới vào TRACKER.md,
   trạng thái "Ứng tuyển" cho tới khi được dùng thật + verify
```

### Bước 8 — Guardrail + Deploy (như bản gốc)

```
Guardrail đúng "Rủi ro cao nhất" ở Bước 2
Deploy checklist: bật Vessel nào, set env nào, test case gì trước khi
giao việc thật
```

---

## Output format khi chạy factory v2

1. Bảng SPEC (Bước 2) — xác nhận hướng, gọn
2. Bảng GROUNDING (Bước 1) — trích đúng section EXPERT-CORE, hoặc research mới nếu chưa có
3. VESSEL + TALENT (Bước 3) — 1 dòng mỗi cái, không dài dòng
4. Sơ đồ CHUỖI TẠO TÁC (Bước 4, nếu áp dụng)
5. Sinh trọn bộ file (Bước 5) — tạo thật bằng create_file
6. JEV CASCADE (Bước 6, nếu áp dụng) — câu hỏi cụ thể + ngưỡng
7. WIRE (Bước 7) — xác nhận 3 điểm kết nối
8. Guardrail + deploy checklist + present files

## Khác biệt so với bản gốc (v1, đầu phiên) — nói thẳng

| | v1 (lý thuyết) | v2 (sau khi xây 8 Pro Agent thật) |
|---|---|---|
| Luật gốc | Tự nghĩ ra khi cần | BẮT BUỘC trace về EXPERT-CORE, research thật nếu role mới |
| Thuật ngữ hạ tầng | "Tầng Tay/Tầng Não/Tầng Cơ" tự đặt | Vessel/Talent — đã kiểm chứng qua 422 sao GitHub (OneManCompany) |
| Nhiều bước | Không có khái niệm | Chuỗi tạo tác ADLC (intent->spec->plan->code->review->signal) |
| Quyết định lặp lại | Không có | Jev cascade với ngưỡng confidence + fallback |
| Kết nối hệ thống | Không có bước này | Bước 7 — wire vào EA gate/briefing/HR lifecycle |

## Link
- Case đã áp dụng bản v1: Research/Content/Sales/Marketing/Dev/Media/Designer/Customer Satisfaction Pro
- Nguồn học v2: agents/company/COMPANY-CHARTER.md, repos/typesafe-jev.md, infographic ADLC (Nobitano chia sẻ)

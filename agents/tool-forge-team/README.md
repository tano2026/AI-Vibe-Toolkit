# Tool Forge — Team 3 vessel dựng công cụ làm việc và sản phẩm

> Cập nhật 29/10/2026. Gói này là **hồ sơ thiết kế đã viết, chưa chạy thật** (xem "Giới hạn trung thực").

## Một câu

**Nhận nhu cầu thô của chủ → ra công cụ chạy được, đã qua cổng kiểm, deploy lên VPS riêng → cho chủ và nhân viên dùng; đủ sạch để sau này đóng gói thành sản phẩm.**

## Ba thành viên

| Vai | Vessel | Việc chính | Không làm |
|---|---|---|---|
| **Đầu não** | Claude (chat/Cowork, không chạy trên VPS) | Hỏi tối đa 3 câu, viết `TOOL-SPEC`, chia việc, cổng QA, chốt ĐẠT/KHÔNG ĐẠT, ghi kho | Không deploy, không tự viết toàn bộ code khi đã có tay |
| **Tay logic** | DeepSeek Harness (DSH, sandbox local) | Parser, tính toán, API, test tự động theo `TOOL-SPEC` | Không chạm VPS, không deploy, không sửa spec |
| **Tay giao diện + deploy** | Google Antigravity 2.0 (Gemini) | Giao diện một file, thiết kế, nối vào logic, deploy VPS, trả link | Không sửa logic đã qua QA mà chưa quay lại cổng, không tự deploy khi chưa có OK |

Lý do chọn DSH làm thành viên thứ ba: kho đã có luật tách ranh giới tin cậy (`agents/README.md`, `ways-of-working`): DSH sandbox làm code hằng ngày, Antigravity quyền rộng thì lo deploy. Viết logic trong sandbox rẻ (DeepSeek Flash qua OpenRouter) rồi mới đưa lên quyền rộng. Hermes không chọn vì là executor Python chạy nền, không phải agent viết code.

## Luồng

```
Chủ nhắn nhu cầu thô
   |
Claude: hỏi <= 3 câu -> TOOL-SPEC.md (đầu vào/ra, hợp đồng giao diện JSON, ca kiểm thử với dữ liệu mẫu)
   |-------------------------------|
DSH: logic + test (song song)    Antigravity: giao diện theo hợp đồng JSON
   |-------------------------------|
Claude: QA-GATE (chạy lại ca kiểm, đọc code, soát bảo mật)  -- KHÔNG ĐẠT -> quay lại tay
   |
Chủ: OK deploy (L2)
   |
Antigravity: deploy VPS -> trả link -> Claude ghi sổ
```

Việc nhỏ dùng một lần (mức A) bỏ qua DSH và spec đầy đủ, xem `PIPELINE.md`.

## Đọc theo thứ tự

1. `TEAM-CHARTER.md` — vai, JD, KPI, escalation, ba lằn ranh đỏ, ranh giới tin cậy
2. `PIPELINE.md` — 7 bước, cổng PASS/FAIL từng bước, phân mức A/B/C
3. `briefs/` — chỉ dẫn riêng từng thành viên (dán vào Rules/instruction của vessel đó)
4. `GEMINI-SPARK-INSTRUCTION.md` — instruction cho Gemini Spark / Antigravity Rules, giữ tư duy mặc định của Gemini
5. `templates/` — `TOOL-SPEC`, `BUILD-REPORT`, `QA-VERDICT`
6. `QA-GATE.md` — checklist cổng kiểm
7. `TENANT-DEFAULTS.md` — mặc định riêng của chủ (VPS, Supabase, OpenRouter, không login nội bộ, định dạng lệnh GDS). Đổi chủ thì chỉ sửa file này.
8. `examples/affiliate-product-scorer/` — ví dụ spec thật: biến quy trình chấm điểm sản phẩm affiliate thành công cụ

## Quan hệ với phần còn lại của kho

- Gói này là **team vessel**, không phải một Pro Agent hay OPC dựng từ `agent-factory`. Chưa chạy `tools/agent_factory.py kiem` vì công cụ đó kiểm khuôn agent/OPC; nếu sau này muốn đóng gói thành agent bàn giao cho khách thì dựng lại bằng `agent-factory`.
- Công cụ làm ra có tính affiliate/video nên nối với `agents/shorts-affiliate-system/` và `agents/yt-cashcow/` (ví dụ spec nêu rõ chỗ nối).
- Trước khi chọn công cụ bên thứ ba cho một tool: tra `agents/thu-kho/`, không chọn theo tên.
- Luật cứng: `agents/company/DECISION-MATRIX.md` (L0 đến L3) thắng mọi file trong gói này.

## Giới hạn trung thực

1. **Chưa chạy thật.** Chưa có tool nào ra đời qua team này. Ví dụ trong `examples/` là spec, chưa có code.
2. **DSH còn breaking changes** (ghi trong `agents/README.md`). Cổng QA của Claude là lớp chặn; nếu DSH hỏng giữa chừng thì Antigravity nhận phần logic, ghi rõ vào `BUILD-REPORT`.
3. **Chưa có bài đo** thời gian hoặc chi phí token mỗi tool. Ô KPI mục tiêu ghi `CHƯA CÓ — hỏi CEO`.
4. **Cổng QA là người/AI đọc và chạy ca kiểm**, không phải bảo chứng bảo mật. Tool xử lý dữ liệu khách thật phải thêm bước soát riêng của chủ.
5. **Mô hình giao việc qua file** (`tasks/<id>/`) mượn từ cách Team Thục Hán giao tiếp; chưa dựng script tự động, hiện giao tay hoặc qua Telegram.
6. Không tìm thấy mô tả "mô hình TheUnsaid" trong kho. Gói dựng theo cặp não/tay đã ghi ở kho (Tano Agency: Claude lo não và hoạch định, vessel khác lo tay chân).

# Pilot Test Plan — 1 video cụ thể, thu hẹp tối đa

> Mục tiêu duy nhất: xác nhận MoneyPrinterTurbo render được video coi được trên
> VPS thật. Không test compliance/automation/multi-platform trong lần này.

## Chủ đề cụ thể

**Tiêu đề:** "I Tested 3 Free AI Video Tools So You Don't Have To — Real Render
Time & Cost Breakdown"

**Nội dung thật, không hư cấu:** dùng chính số liệu đã verify khi research kho —
MoneyPrinterTurbo (4-8 core/4-8GB RAM, không GPU nếu dùng cloud LLM+Edge-TTS),
so với ước tính OpenMontage/ViMax (nặng hơn, cần AI-gen visual). Đây là data
gốc từ chính quá trình build kênh — không phải AI generate mù, đúng tinh thần
"genuine creative fingerprint".

**structure_type:** `comparison` — dùng stock footage, không cần nhánh AI-gen
visual còn chưa test (đúng CONTENT-PRODUCTION-MODEL.md).

## Các bước — chạy tay, không qua Hermes/cron

| # | Bước | Ai làm | Ghi chú |
|---|---|---|---|
| 1 | Antigravity chạy Phase 0-2 trong runbook deploy (check tài nguyên, deploy MoneyPrinterTurbo, set env) | Antigravity | Đã có brief chi tiết ở lượt trước |
| 2 | Viết script tay (~300-400 từ, giọng casual-expert theo `brand_voice` đã chốt) | Nobitano hoặc Claude (chat này) | Không qua Script Variation Engine — chưa cần tự động lần đầu |
| 3 | Tính fingerprint script này TAY theo công thức trong `compliance-gate/SKILL.md` (structure_type, hook_type, unique_claims, commentary_ratio) | Claude (chat này) | Không phải để CHẶN — để **ghi lại làm gốc**, video #2 mới có cái để so sánh |
| 4 | Nhập script vào WebUI MoneyPrinterTurbo (`localhost:8501` qua SSH tunnel), chọn TTS=Edge, resolution 1920x1080 | Nobitano | Đúng Phase 5 runbook trước |
| 5 | Xem video render ra — chấm tay: TTS nghe tự nhiên không, b-roll khớp nội dung không, subtitle đúng timing không, tổng thời gian render bao lâu | Nobitano | Đây là điểm quan trọng nhất của cả pilot |
| 6 | Nếu OK → upload TAY lên YouTube (không qua Upload-Post), tự bật toggle "Altered/synthetic content" tay | Nobitano | Chưa cần OAuth setup cho 1 video |
| 7 | Ghi lại fingerprint (bước 3) vào 1 file tạm (chưa cần Airtable thật cho 1 video) | Claude (chat này) | Làm gốc, để lúc build Airtable thật thì có sẵn record #1 |

## Tiêu chí để coi pilot THÀNH CÔNG

- [ ] MoneyPrinterTurbo render xong không lỗi, thời gian render hợp lý (<15-20 phút cho video 5-7 phút)
- [ ] TTS Edge nghe tự nhiên, không robot rõ rệt
- [ ] B-roll từ Pexels/Pixabay khớp tối thiểu 70% nội dung (không bị mismatch lộ liễu)
- [ ] Subtitle đồng bộ, không lệch timing
- [ ] VPS không bị treo/quá tải trong lúc render (kiểm tra Hermes/OpenClaw/n8n vẫn chạy bình thường song song)

## Nếu FAIL ở bước nào — dừng lại, không tiếp tục sang video #2

Ghi rõ lỗi cụ thể (thiếu dependency, TTS không tự nhiên, b-roll không liên quan,
VPS quá tải...) — sửa xong lỗi đó rồi mới làm pilot video #2, không nhảy sang
xây compliance-gate/automation khi engine gốc còn chưa chạy ổn định.

## Sau khi pilot #1 thành công — bước tiếp theo mới là quay lại bản chung

1. Làm pilot video #2 (chủ đề khác, structure_type khác — vd `intro-list-outro`)
   → lúc này mới thật sự dùng Compliance Gate so sánh với fingerprint video #1
2. Có 2 video → đủ để test thật Compliance Gate có hoạt động đúng logic không
3. Từ 3 video trở lên → mới nói tới Airtable thật, automation, cron

Không build Airtable/automation/multi-platform trước khi có tối thiểu 1 video
chạy thành công bằng tay — tránh xây hạ tầng cho thứ chưa biết có hoạt động không.

# Deploy Checklist — YT Cashcow

## Trước khi bật auto-publish (bắt buộc theo thứ tự)

- [ ] Deploy MoneyPrinterTurbo qua Docker trên VPS: `git clone`, `docker-compose up`
- [ ] Check tài nguyên VPS đủ: `nproc` (cần ≥4 core) và `free -h` (cần ≥4GB RAM) —
      không cần GPU nếu dùng cloud LLM (OmniRoute) + Edge-TTS
- [ ] Config `config.toml` trỏ `llm.provider` qua OmniRoute endpoint (xem `mcp-setup.md`)
- [ ] Setup Airtable base `yt-cashcow-log` với 2 bảng theo `ARCHITECTURE.md`
- [ ] Đăng ký Upload-Post, lấy API key, điền vào `config.toml`
- [ ] Copy skills (`compliance-gate`, `trend-scout`, `script-variation-engine`) +
      skill có sẵn kho (`viral-hooks`, `youtube-marketing`, `claude-ads`) vào
      OpenClaw skill directory
- [ ] Dán `system-prompt.md` vào Domain Agent Router của OpenClaw
- [ ] **Test case bắt buộc: chạy 3 video test, review thủ công 100%** — không
      bật auto-publish trước khi xác nhận cả 3 video pass Compliance Gate đúng,
      và script thực sự có variation (đọc thủ công, không chỉ tin số điểm)
- [ ] Verify video test tự động tag "AI-generated" đúng như MoneyPrinterTurbo hứa
- [ ] Set n8n cron cho Trend Scout (tần suất đề xuất: 1 lần/ngày, không dồn dập)
- [ ] Confirm kênh YouTube đáp ứng điều kiện cơ bản: tài khoản ≥30 ngày,
      2-step verification bật, quốc gia nằm trong danh sách YPP hỗ trợ

## Sau khi bật — theo dõi tuần đầu

- [ ] Kiểm tra YouTube Studio > Content > có cảnh báo policy nào không, mỗi ngày
      trong 7 ngày đầu
- [ ] Xác nhận tỷ lệ random review (1/10) đang chạy đúng — không bị auto-skip
- [ ] Review thủ công toàn bộ video trong 2 tuần đầu dù pass Compliance Gate,
      để hiệu chỉnh ngưỡng thuật toán nếu cần

## KHÔNG làm

- Không bật auto-publish hàng loạt (batch nhiều video/ngày) ngay từ đầu — tăng dần.
- Không tắt Compliance Gate "để test nhanh hơn" — kể cả môi trường test.
- Không dùng cùng 1 hook/structure liên tục nhiều ngày liền dù Trend Scout gợi ý —
  luôn qua Script Variation Engine để né trùng lặp.

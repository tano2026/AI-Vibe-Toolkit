# BÁO CÁO TỔNG KẾT RÀ SOÁT VÀ GẮN NHÃN KHO (455 MỤC) — ANTIGRAVITY

```
ĐÃ LÀM: gắn nhãn 37/37 mục batch4 (out4.json) + cập nhật 20/20 mục pilot v2 (pilot20-v2.json); kiểm đối chiếu 398/398 mục nháp (reviewed-1..8.json). Tổng cộng: 455/455 mục do kho viết.
SỬA NHÃN: 85/398 mục nháp (21.4%) được điều chỉnh nội dung (ngoài việc bổ sung 100% evidence); trường sửa nhiều nhất: confidence (55 mục hạ từ cao xuống vua do evidence dạng tóm tắt hoặc dự án preview/alpha), adoption (19 mục đổi từ cai-ngay-duoc sang can-ha-tang do preview/breaking changes), use_when (16 mục lọc bỏ từ quảng cáo/đo lường), capability (9 mục chuyển sang social-media hoặc gỡ devops/phục vụ phụ), skip_if (3 mục bổ sung binary yt-dlp).
LỖI CƠ HỌC: 0 (0 mục trùng id, 0 mục thiếu trong catalog.json, 0 lỗi vượt độ dài hay sai từ vựng trên toàn bộ 455 mục).
NHÓM TRÙNG: 12 nhóm (≥3 mục cùng việc): motion-video-code (9 mục), auto-short-video (6 mục), code-video-motion (5 mục), claude-skill-collections (4 mục), coding-agent-harness (3 mục), crm-self-host (3 mục), image-video-gen-mcp (3 mục), multi-agent-orchestration (3 mục), synthesis-prompts (3 mục), higgsfield-fal-genmedia (3 mục), agent-harness (3 mục), tu-vi-astrology (3 mục).
KHẢ NĂNG THIẾU MỤC (<3 mục cai-ngay-duoc & confidence ≠ thap): 1 khả năng duy nhất là 'email-outreach' (chỉ có 1 mục sẵn sàng: mcps/resend). Các khả năng còn lại đều có từ 4 đến 81 mục sẵn sàng.
CHƯA LÀM / KHÔNG CHẮC: 460 skill nhập hàng loạt chưa rà soát (theo đúng phạm vi nhiệm vụ). Một số MCP video remote (như mcps/scrptly, mcps/poppify) phụ thuộc credit/API bên ngoài chưa xác thực quota thực tế tại thời điểm rà.
ĐỀ XUẤT CHO CLAUDE:
1. Gộp 2 nhóm trùng lớn 'motion-video-code' (9 mục) và 'code-video-motion' (5 mục) thành 1 taxonomy thống nhất cho Remotion/GSAP video.
2. Bổ sung thêm công cụ cho capability 'email-outreach' (hiện chỉ có Resend, thiếu các tool outbound/cold email tự host).
3. Đưa nhãn 'social-media' vào bộ lọc chính thức của tools/build_catalog.py và giao diện tra cứu danh mục.
```

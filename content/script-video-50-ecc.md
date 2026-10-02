# Script Video 50 — ECC: Cả Đội Kỹ Sư AI Trong Claude Code (Tránh Cháy Token)

## Thông tin
- Tool/Repo/Skill liên quan: `/repos/ecc.md`
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~55 giây

## Hook (3 giây đầu)
"Một plugin miễn phí biến Claude Code thành cả phòng kỹ thuật. Nhưng cài sai là cháy sạch lượt dùng."

## Script voiceover (ElevenLabs-ready)

[Đoạn 1 — vấn đề]
Claude Code mặc định là một thợ code làm một mình.
Tự lên kế hoạch, tự viết, tự kiểm tra. Dễ sót lỗi.

[Đoạn 2 — giải pháp]
ECC là plugin miễn phí, mã nguồn mở.
Hai trăm bảy mươi nghìn sao trên GitHub.
Sáu mươi tám agent chuyên trách, hơn hai trăm skill.
Có người lên kế hoạch, người viết test, người rà code, người rà bảo mật.

[Đoạn 3 — cách làm]
Cài chỉ hai lệnh. Thêm chợ plugin, rồi cài ecc a còng ecc.
Thoát ra, mở lại Claude Code.
Gõ ecc hai chấm plan, mô tả tính năng. Nó lên kế hoạch trước khi chạm vào code.
Rồi viết test trước, code sau, rà code, quét bảo mật.

[Đoạn 4 — cảnh báo token và kết]
Nhưng nhiều agent là nhiều lượt gọi model.
Trước khi chạy, đổi sang Sonnet, giảm thinking xuống mười nghìn, cho agent con chạy Haiku.
Và đừng cài chồng hai cách, hook sẽ chạy hai lần.
Chỉ tải từ repo chính thức. Bản chia sẻ trên group có thể chứa mã độc.
Follow để xem mình chạy thử trên dự án thật.

## Ghi chú quay (OBS)
- Cảnh 1 (0-3s): Màn hình Claude Code trống, chữ hook lớn.
- Cảnh 2 (3-15s): Trang GitHub affaan-m/ECC, cuộn qua số sao và dòng 68 agents, 293 skills.
- Cảnh 3 (15-30s): Terminal gõ 2 lệnh `/plugin marketplace add affaan-m/ECC` và `/plugin install ecc@ecc`, rồi `/exit`, mở lại, `/plugin list ecc@ecc`.
- Cảnh 4 (30-42s): QUAY THẬT một vòng `/ecc:plan` rồi tdd-workflow rồi `/code-review` rồi `/security-scan` trên dự án nhỏ. Kịch bản ABTRIP CRM trong ecc.md chưa chạy thật, đừng quay giả.
- Cảnh 5 (42-52s): Mở `~/.claude/settings.json` hiện 4 dòng cấu hình token. Chạy `/cost` cho thấy mức tiêu.
- Cảnh 6 (52-55s): Màn hình cảnh báo repo chính thức vs bản re-upload.

## Caption/Sub note (CapCut)
- Highlight: "68 agent", "ecc@ecc", "Sonnet", "10.000", "Haiku", "đừng cài chồng".
- Cắt nhanh ở cảnh gõ lệnh cài. Zoom vào dòng `ecc@ecc` ở cảnh 3.
- Hiện chữ cảnh báo đỏ ở Đoạn 4: "Chỉ tải từ repo chính thức".

## Thumbnail idea (Canva)
Nền tối, chữ lớn "CẢ PHÒNG KỸ SƯ AI". Ngoài logo Claude Code, thêm icon pin báo hết ("cháy token") góc dưới. Số "68 AGENT" màu vàng.

## CTA cuối video
Follow để xem mình chạy ECC trên dự án thật. Link repo và cấu hình token ở bio.

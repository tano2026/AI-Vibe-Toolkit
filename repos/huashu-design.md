# Huashu Design (alchaincyf) — GitHub Repo

## TL;DR
Skill thiết kế HTML-native cho Claude Code — 1 câu prompt ra prototype có thể click, slide deck, animation, infographic, xuất cả MP4/PPTX. 21.4K stars, MIT license (mở hoàn toàn từ 14/5/2026). Cùng nhóm "anti-AI-slop design skill" với `hallmark` đã có trong kho, nhưng đi xa hơn: không chỉ chặn UI generic mà còn tạo được deliverable hoàn chỉnh nhiều định dạng.

## Repo này dùng để làm gì
Nhận 1 mô tả ngắn (hoặc brand asset: logo, bảng màu, screenshot UI), Huashu Design ra deliverable hoàn chỉnh trong 3-30 phút:
- **Prototype có thể click** — app mockup tương tác thật, không chỉ ảnh tĩnh
- **Slide deck** — HTML slide có thể chỉnh sửa, xuất PPTX
- **Animation/motion piece** — video sản phẩm, xuất MP4 kèm nhạc nền + hiệu ứng âm thanh
- **Infographic** — chất lượng in ấn

Cơ chế chống AI-slop: 20 "triết lý thiết kế" (design philosophy) + 5 trục đánh giá (5-dimension review, giống cách Hallmark tự chấm điểm) + 40 style HTML-native làm phương án dự phòng khi không có brand asset. Có "fallback flow" — brief mơ hồ thì đề xuất nhiều hướng thiết kế thay vì tự đoán 1 hướng rồi làm luôn. Có verification bằng Playwright cho prototype tương tác — kiểm tra thật chứ không chỉ "nhìn có vẻ ổn".

## Setup từng bước
1. Cài qua Claude Code plugin hoặc clone trực tiếp:
```bash
git clone https://github.com/alchaincyf/huashu-design.git
```
2. README hướng dẫn cách đăng ký skill vào Claude Code/Cursor/Codex/OpenClaw — repo ghi rõ "agent-agnostic", không khoá riêng 1 nền tảng.
3. Đưa brand asset (logo, bảng màu Deep Navy/Hanoi Gold của An Bình, hoặc palette Tano) nếu muốn kết quả bám sát brand — không có thì skill tự dùng 1 trong 40 style sẵn có + logic 3 cố vấn thiết kế để không ra sản phẩm "AI slop".
4. Có sẵn 18 demo GIF minh hoạ 9 năng lực (2 ngôn ngữ Anh/Trung) trong repo, tham khảo trước khi giao brief thật.

## Ví dụ thực tế
Cần video công bố sản phẩm mới cho kênh AI review (khi chốt tên chính thức "Actually Tested"/"The Compute Cost") — thay vì tự dựng HyperFrames tay từ đầu, thử giao brief cho Huashu Design kèm bảng màu kênh, ra 1 bản animation MP4 hoàn chỉnh trong vài phút để tham khảo hướng, rồi quyết định polish thêm bằng HyperFrames hay dùng thẳng bản Huashu Design ra nếu đã đủ chất lượng.

## Lưu ý / Lỗi thường gặp
- Tên "huashu" (话术) trong tiếng Trung nghĩa gốc là "kịch bản hội thoại/script bán hàng" — nhưng repo này KHÔNG phải công cụ đó, đây là design skill thuần tuý cho UI/slide/video, tên gọi dễ gây nhầm khi search (SourceForge mirror mô tả sai bản chất repo, nên tin theo GitHub gốc).
- Repo và phần lớn tài liệu bằng tiếng Trung, có "bản dịch cộng đồng" — chất lượng dịch/license của bản dịch do người maintain riêng chịu trách nhiệm, kiểm tra kỹ trước khi dùng bản dịch thay vì gốc.
- Trước 14/5/2026 license là "cá nhân miễn phí, doanh nghiệp cần xin phép" — đã đổi hẳn sang MIT, nhưng nên xác nhận lại phiên bản đang dùng đã áp MIT chưa nếu tải bản cũ hơn.
- Overlap chức năng với `hallmark` (chặn AI slop) và `stitch-skills` (design→code) đã có trong kho — nên coi 3 cái này là "bộ 3 công cụ thiết kế AI", chọn 1 cái phù hợp brief cụ thể thay vì dùng tất cả cùng lúc cho 1 task.

## Đánh giá cá nhân
- Điểm mạnh: đầu ra đa dạng nhất trong nhóm design skill đã có trong kho (prototype + slide + animation + infographic, không chỉ 1 loại); có verification thật (Playwright) chứ không chỉ tự chấm điểm; MIT license rõ ràng, miễn phí hoàn toàn cả thương mại.
- Điểm yếu: tài liệu chủ yếu tiếng Trung; overlap với 2 skill thiết kế đã có (hallmark, stitch-skills) nên cần rõ ràng khi nào dùng cái nào; chưa có track record dài (chỉ mới từ đầu 2026).
- Có nên dùng không: 8/10 — đáng thử cho content cần deliverable đa định dạng nhanh (đặc biệt animation MP4 cho kênh AI review sắp ra mắt), nhưng nên test thử trước khi coi là công cụ chính thay Hallmark/HyperFrames.

## Link
- Repo: https://github.com/alchaincyf/huashu-design

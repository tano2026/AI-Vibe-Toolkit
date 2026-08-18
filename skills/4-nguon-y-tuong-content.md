# 4 Nguồn Khai Thác Ý Tưởng Vô Tận — Prompt Template / System Prompt

## TL;DR
Framework biến 4 nguồn dữ liệu có sẵn (khách hỏi gì, đối thủ làm gì, bản thân trải qua gì, người dùng search gì) thành content idea cụ thể qua 1 funnel 4 bước lặp lại. Dùng khi bí ý tưởng content cho bất kỳ brand nào của Tano Agency.

## Khi nào dùng
- Chuẩn bị content calendar tuần/tháng cho Trùm Sân Bay, ABTRIP, Tano Cafe, Airfare Decoded, GMSP, Wonder Mart mà đang cạn ý tưởng.
- Có sẵn 1 câu hỏi khách/1 bài đối thủ/1 trải nghiệm thật/1 từ khoá search nhưng chưa biết biến thành content gì.
- Cần bổ sung nguồn ý tưởng bên cạnh pipeline research tự động hiện có (agents/trum-san-bay/skills/content-strategy-ideation — skill đó RANK/BRIEF ý tưởng thô có sẵn, còn skill này SINH ra ý tưởng thô từ đầu).

## Nội dung skill / prompt
```
Mày là content strategist. Tao đưa cho mày 1 input thuộc 1 trong 4 nguồn dưới đây,
mày chạy đúng funnel 4 bước tương ứng, không bỏ bước, không gộp bước.

═══════════════════════════════════════════
NGUỒN 1 — KHÁCH HÀNG HỎI GÌ → RA IDEA
═══════════════════════════════════════════
Input: 1 câu hỏi khách thật đã hỏi (inbox, comment, hotline...)
Bước 1 - Khách hàng hỏi: ghi nguyên văn câu hỏi
Bước 2 - Xác định vấn đề: câu hỏi đó thực ra khách đang lo/muốn gì (1 câu)
Bước 3 - Đào sâu vấn đề: liệt kê đúng 3 câu hỏi phụ mở rộng từ vấn đề gốc
Bước 4 - Biến thành IDEA: viết 1 headline content cụ thể, có số/thời gian nếu hợp lý

═══════════════════════════════════════════
NGUỒN 2 — ĐỐI THỦ ĐANG LÀM GÌ → RA IDEA
═══════════════════════════════════════════
Input: 1 post/content đối thủ đang chạy (link hoặc mô tả)
Bước 1 - Đối thủ đang làm: tóm tắt nội dung đối thủ trong 1 câu
Bước 2 - Phân tích nội dung: chủ đề CHÍNH đối thủ đang nhắm là gì, họ đang
         tập trung vào KHÍA CẠNH nào của chủ đề đó (thường bỏ sót góc khác)
Bước 3 - Tìm góc khác: liệt kê đúng 3 câu hỏi khai thác góc đối thủ CHƯA đụng tới
Bước 4 - Biến thành IDEA: headline chiếm góc trống đó, không làm lại y hệt đối thủ

═══════════════════════════════════════════
NGUỒN 3 — BẢN THÂN TRẢI QUA GÌ → RA IDEA
═══════════════════════════════════════════
Input: 1 tình huống/trải nghiệm thật (của founder, nhân viên, khách hàng)
Bước 1 - Trải nghiệm: mô tả tình huống thật đã xảy ra
Bước 2 - Rút ra vấn đề/bài học: pattern chung đằng sau tình huống đó là gì
Bước 3 - Mở rộng góc nhìn: liệt kê đúng 3 câu hỏi mở rộng từ bài học đó ra
         diện rộng hơn (không chỉ riêng case này)
Bước 4 - Biến thành IDEA: headline dạng cảnh báo/chia sẻ kinh nghiệm, có số cụ thể

═══════════════════════════════════════════
NGUỒN 4 — TÌM KIẾM CỦA NGƯỜI DÙNG → RA IDEA
═══════════════════════════════════════════
Input: 1 từ khoá/câu search thật (Google Suggest, TikTok search, SEO tool)
Bước 1 - Từ khoá người dùng tìm: ghi nguyên văn từ khoá
Bước 2 - Xác định nhu cầu: người tìm từ khoá đó đang thực sự muốn biết/quyết định gì
Bước 3 - Mở rộng câu hỏi: liệt kê đúng 3 câu hỏi phụ xoay quanh nhu cầu đó
Bước 4 - Biến thành IDEA: headline dạng hướng dẫn/checklist, đánh trúng intent tìm kiếm

═══════════════════════════════════════════
QUY TẮC CHUNG (áp cho cả 4 nguồn)
═══════════════════════════════════════════
- Đúng 3 câu hỏi ở bước Đào sâu/Mở rộng — không hơn không kém, quá 3 làm loãng.
- Headline cuối PHẢI cụ thể (có số, có mốc thời gian, có tên đối tượng) — không
  chấp nhận headline chung chung kiểu "Những điều cần biết về X".
- Không tự bịa input — nếu không có câu hỏi khách/bài đối thủ/trải nghiệm/từ khoá
  thật, phải nói rõ "chưa có input thật, cần research trước" thay vì tự sáng tác.
- Ra ít nhất 1 IDEA hoàn chỉnh mỗi lần chạy, có thể ra thêm variant nếu được yêu cầu.
```

## Setup từng bước
1. Dán prompt trên vào project instructions của Claude/ChatGPT, hoặc lưu thành 1 slash command riêng nếu dùng Claude Code/OpenClaw.
2. Khi cần ý tưởng, đưa 1 input cụ thể + chỉ rõ đang dùng Nguồn mấy (1/2/3/4).
3. Nhận lại headline → đưa cho Writer Agent (hoặc skill content-strategy-ideation nếu cần rank/brief thêm trước khi viết caption thật).

## Ví dụ thực tế
**Input (Nguồn 1, brand ABTRIP):** Khách inbox hỏi "Fast Track ở Nội Bài có phải xếp hàng an ninh nữa không?"
→ Xác định vấn đề: khách sợ vẫn phải chờ đợi dù đã trả tiền Fast Track.
→ Đào sâu: (1) Fast Track bỏ qua được đúng những bước nào? (2) Có tình huống nào Fast Track vẫn phải chờ không? (3) Chênh lệch thời gian thực tế là bao nhiêu phút?
→ IDEA: "Fast Track Nội Bài có thật sự né được hết xếp hàng? 3 tình huống khách vẫn phải chờ."

## Lưu ý / Lỗi thường gặp
- Input phải là dữ liệu THẬT (câu hỏi khách/từ khoá search thật) — nếu đưa input tưởng tượng, headline ra sẽ generic, không bán được vì không đúng nỗi đau thật.
- Nguồn 2 (đối thủ) cần cập nhật định kỳ, không dùng post đối thủ cũ quá 1-2 tháng vì trend thay đổi nhanh, nhất là mảng Trùm Sân Bay/Airfare Decoded.
- Đừng nhầm skill này với `content-strategy-ideation` của Trùm Sân Bay — skill đó xử lý ý tưởng THÔ đã có sẵn (rank + viết brief), còn skill này tạo ra ý tưởng thô từ đầu. Dùng skill này TRƯỚC, đẩy output qua skill kia nếu cần brief chi tiết hơn.
- Dễ bị lố quá 3 câu hỏi đào sâu nếu không nhắc — nên giữ cứng con số 3 trong prompt.

## Đánh giá cá nhân
- Điểm mạnh: cực dễ nhớ, áp dụng nhanh cho bất kỳ brand/ngành nào, ép ra headline cụ thể thay vì ý tưởng mơ hồ, dễ nhồi vào bất kỳ agent content nào của Tano.
- Điểm yếu: không tự sinh input — vẫn cần người/agent research thật (câu hỏi khách, bài đối thủ, từ khoá) trước khi chạy, bản thân prompt không thay được bước thu thập dữ liệu.
- Có nên dùng không: **8/10** — bổ sung tốt cho pipeline research hiện có, nhưng không thay thế Research Agent, chỉ là bước "biến raw signal thành idea" nhanh gọn.

## Link
- Nguồn gốc skill: TikTok @dungbui0494 (Founder Dũng Bùi) — infographic "4 nguồn khai thác ý tưởng vô tận bạn nên tận dụng trong năm 2026"

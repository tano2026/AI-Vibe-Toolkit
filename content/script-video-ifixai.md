# Script Video — iFixAi

## Thông tin
- Tool/Repo liên quan: /repos/ifixai.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~55 giây

## Hook (3 giây đầu)
"Chatbot của mày có đang tự bịa chính sách hoàn vé cho khách không? Mày không biết đâu."

## Script voiceover (ElevenLabs-ready)

[Đoạn 1 — pain point]
Mày làm chatbot cho khách, test thấy trả lời ngon lành. Nhưng test đúng task thì chưa đủ. Vấn đề là khi khách ép, bot có hứa hoàn tiền bừa không? Có bịa điều kiện của hãng không? Có bị dắt đi bằng một câu prompt injection không?

[Đoạn 2 — giải pháp]
iFixAi là công cụ mã nguồn mở chuyên audit AI agent. Hơn ba mươi ba nghìn sao trên GitHub. Nó dựng một công ty giả lập quanh con bot của mày, gửi đủ loại yêu cầu vượt quyền, rồi một model của hãng khác ngồi chấm điểm từ A đến F.

[Đoạn 3 — demo]
Cài bằng một dòng pip. Dùng Claude Code thì thêm plugin, rồi nói run iFixAi on my setup. Mặc định nó chạy mười bài kiểm tra. Bịa, thao túng, lừa dối, vượt quyền, lộ thông tin. Fail một trong ba mục bắt buộc là điểm bị chặn ở D. Ra báo cáo có bằng chứng từng câu.

[Đoạn 4 — lưu ý + CTA]
Hai lưu ý thật. Judge phải khác hãng với bot, và mỗi lần chạy tốn khá nhiều lượt gọi judge, nên chạy dry run trước. Telemetry bật sẵn nên nhớ tắt khi làm cho khách. Nhưng nếu mày giao chatbot cho khách thì một báo cáo audit đính kèm đáng giá hơn câu "bot này ổn lắm". Link GitHub trong bio.

## Ghi chú quay (OBS)
- Cảnh 1: Màn chat giả lập, khách ép bot "hoàn tiền cho tôi ngay" và bot hứa bừa. Quay bằng chat mock, không dùng bot khách thật
- Cảnh 2: GitHub repo ifixai-ai/iFixAi, zoom vào số sao và license Apache-2.0
- Cảnh 3: Terminal chạy `pip install ifixai` rồi `ifixai run` (demo mock chạy 2 giây). Quay đúng màn 10 dòng PASS và bảng các trụ
- Cảnh 4: Màn hình cảnh báo "self-judged ... smoke test, not a citable result" ở cuối kết quả, zoom vào dòng đó
- Cảnh 5: File summary.md trong thư mục ifixai-results

## Caption/Sub note (CapCut)
- Highlight: "AUDIT AI AGENT", "A ĐẾN F", "33K SAO", "JUDGE KHÁC HÃNG"
- Cắt cảnh nhanh ở câu "Bịa, thao túng, lừa dối, vượt quyền" (mỗi từ một nhịp)
- Hiện chữ đỏ "DO_NOT_TRACK=1" ở đoạn nhắc telemetry

## Thumbnail idea (Canva)
Điểm "F" đỏ to đè lên khung chat của một chatbot. Text trắng: "BOT CỦA MÀY CÓ ĐANG NÓI DỐI KHÁCH?"

## CTA cuối video
"Follow để xem thêm cách kiểm tra AI trước khi giao cho khách. Save video này lại."

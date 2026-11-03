# Script Video 338 — Trình duyệt cho AI, nhẹ hơn Chrome rất nhiều (và chỗ mình thấy nó vấp)

## Thông tin
- Tool/Repo/Skill liên quan: /repos/lightpanda.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~55 giây
- Lưu ý khi quay: số liệu nhanh hơn, nhẹ hơn là của hãng, chưa ai độc lập kiểm. Chỉ quay phần đã test thật trên trang cục bộ. Chưa thử web thật, đừng nói là đã thử.

## Hook (3 giây đầu)
Cho AI đọc web mà không cần mở cả một cái Chrome.

## Script voiceover (ElevenLabs-ready)
[Đoạn 1 — vấn đề]
AI muốn đọc một trang web có JavaScript thì phải mở Chrome. Mỗi lần mở là tốn bộ nhớ. Chạy nhiều tab trên máy chủ yếu là nghẹt.

[Đoạn 2 — giải pháp]
Có một trình duyệt tên Lightpanda, viết từ đầu bằng ngôn ngữ Zig. Nó vẫn chạy JavaScript, nhưng bỏ hẳn phần vẽ giao diện. Hãng nói nhẹ hơn Chrome khoảng mười sáu lần. Đó là số của hãng, mình chưa tự đo.

[Đoạn 3 — demo]
Mình tải về chạy thử. Một file duy nhất. Gõ một lệnh, nó trả về trang đã chạy JavaScript, dạng markdown, đưa thẳng cho AI đọc. Nối Playwright cũng được. Nhưng có một cái bẫy. Mặc định nó không chờ dữ liệu tải sau, nên danh sách bị trống. Phải thêm cờ chờ mới đủ.

[Đoạn 4 — điểm yếu và CTA]
Điểm yếu thì rõ. Không vẽ giao diện nên ảnh chụp không phải ảnh thật. Chưa có bản Windows. Giấy phép AGPL nên làm sản phẩm bán cho khách phải đọc kỹ. Mình mới thử trên trang giả, chưa thử web thật. Follow để xem mình thử trang thật.

## Ghi chú quay (OBS)
- Cảnh 1: Task Manager, vài cửa sổ Chrome ăn bộ nhớ.
- Cảnh 2: trang lightpanda.io, zoom vào dòng nói "không vẽ giao diện".
- Cảnh 3: terminal chạy lệnh version, rồi lệnh fetch lần đầu ra danh sách trống, thêm cờ chờ, ra đủ hai dòng. Cảnh này quay thật, có sẵn.
- Cảnh 4: ảnh chụp từ Playwright, chỉ ra đó là bản dựng chữ, không phải giao diện thật.
- Cảnh 5: chữ "SỐ LIỆU CỦA HÃNG, CHƯA KIỂM" hiện lúc nói đoạn hai và "CHƯA THỬ WEB THẬT" lúc nói đoạn cuối.

## Caption/Sub note (CapCut)
Highlight: "không vẽ giao diện", "số của hãng", "cờ chờ", "AGPL", "chưa thử web thật". Cắt nhanh ở đoạn 3, giữ chậm ở đoạn điểm yếu.

## Thumbnail idea (Canva)
Một con gấu trúc nhỏ cạnh logo trình duyệt to đùng đang đổ mồ hôi. Chữ lớn "NHẸ HƠN CHROME?". Góc phải ghi nhỏ "số của hãng, mình đang kiểm".

## CTA cuối video
Follow để xem bản thử trên trang thật. Save video nếu bạn chạy AI đọc web trên máy chủ.

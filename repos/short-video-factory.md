# Short Video Factory (YILS-LIN) — GitHub Repo

## TL;DR
App desktop mã nguồn mở, 1 click ra video ngắn quảng cáo sản phẩm/nội dung đại chúng — AI viết văn án, chuyển giọng nói, tự cắt ghép video/nhạc/phụ đề, chạy batch theo preset. 4.6K stars, chạy hoàn toàn local (không gửi data lên cloud của bên thứ 3 ngoài API bạn tự cấu hình).

## Repo này dùng để làm gì
Đây là "nhà máy" sản xuất video ngắn hàng loạt — khác `html-video` (làm motion graphics/explainer từ code) và HyperFrames (composition thủ công cho brand riêng), Short Video Factory tối ưu cho luồng: có sẵn clip nguồn (footage) → AI viết kịch bản → ghép clip theo kịch bản → thêm giọng đọc + phụ đề + nhạc nền → xuất hàng loạt theo preset, không cần dựng composition tay từng cảnh.

Tính năng lõi:
- **Viết văn án AI** — tương thích format API kiểu OpenAI (nối được OmniRoute gateway sẵn có)
- **Chuyển giọng nói** — dùng EdgeTTS (giọng đọc Microsoft, miễn phí, nhiều ngôn ngữ kể cả tiếng Việt)
- **Cắt ghép tự động** — merge văn án + video nguồn + audio + phụ đề thành video hoàn chỉnh
- **Xử lý batch** — 1 batch job chạy liên tục sinh nhiều video theo preset đã set sẵn
- **Đa ngôn ngữ** — hỗ trợ tiếng Trung, tiếng Anh và nhiều ngôn ngữ khác
- **Chạy hoàn toàn local** — không gửi dữ liệu video/footage lên server bên thứ 3 nào ngoài chính
  API AI bạn tự cấu hình (bảo mật data khách hàng tốt hơn tool cloud)
- Cross-platform: Windows/macOS/Linux, Electron + Vue + TypeScript

## Setup từng bước
1. Tải bản build sẵn từ GitHub Releases (không cần build từ source):
```
https://github.com/YILS-LIN/short-video-factory/releases
```
2. Cấu hình API văn án — điền endpoint tương thích OpenAI, có thể trỏ thẳng vào **OmniRoute** (LLM
   gateway sẵn có trong hệ thống) thay vì trả phí OpenAI trực tiếp.
3. Chuẩn bị clip nguồn (footage) theo domain — vd clip quay sẵn ở Tano Cafe, clip B-roll sân bay
   cho ABTRIP.
4. Set preset batch: số lượng video/lần chạy, giọng đọc (EdgeTTS có giọng tiếng Việt), style phụ
   đề, tỷ lệ khung hình theo nền tảng (TikTok 9:16, YouTube 16:9).
5. Docs đầy đủ: https://short-video-factory.yils.blog

## Ví dụ thực tế
Có sẵn 20 clip B-roll quán Tano Cafe (quay rời rạc, chưa dựng) — thay vì tự ngồi CapCut cắt ghép
từng cái, đưa hết vào Short Video Factory, viết 1 prompt kiểu "video quảng cáo cà phê sáng ấm
cúng, giọng nhẹ nhàng mời khách", set batch chạy ra 5 phiên bản khác nhau (đổi văn án mỗi lần)
cho A/B test trên TikTok — xong trong vài phút thay vì cả buổi dựng tay.

## Lưu ý / Lỗi thường gặp
- **License AGPL-3.0** — copyleft mạnh, khác hẳn MIT/Apache các tool khác trong kho. Nếu tự
  build/sửa code và dùng cho dịch vụ chạy qua mạng (network service) phải cân nhắc nghĩa vụ công
  bố source theo AGPL — dùng bản build sẵn (không sửa code, không phân phối lại) thì an toàn hơn
  nhiều so với việc fork/tùy biến rồi bán dịch vụ dựa trên nó.
- Đây là công cụ CẮT GHÉP clip có sẵn, không tự SINH video từ đầu (không phải text-to-video như
  Sora/Kling) — vẫn cần có sẵn footage nguồn.
- Chất lượng văn án phụ thuộc hoàn toàn vào model AI đã cấu hình — nối OmniRoute route đúng model
  (creative task nên dùng Claude Sonnet theo bảng routing đã có, không phải model rẻ nhất).
- Repo còn khá mới (roadmap ghi rõ còn thiếu: tinh chỉnh tham số toàn diện hơn, thêm API giọng
  đọc, thêm hiệu ứng phụ đề) — một số tính năng nâng cao chưa có.

## Đánh giá cá nhân
- Điểm mạnh: đúng bài toán "có sẵn footage, cần ra nhiều video nhanh" — rất hợp nhịp sản xuất
  TikTok/Shorts hàng loạt; chạy local nên data khách hàng (footage chưa public) không rời máy;
  nối được thẳng OmniRoute, không phải trả thêm phí AI riêng; miễn phí, cross-platform.
- Điểm yếu: license AGPL cần đọc kỹ trước khi tùy biến sâu; không sinh video từ đầu, cần có
  footage sẵn; roadmap còn thiếu vài tính năng tinh chỉnh nâng cao.
- Có nên dùng không: 8/10 — hợp cho content daily/batch (Trùm Sân Bay, Tano Cafe social) hơn là
  cho video sản xuất chỉn chu như GMSP/Airfare Decoded (2 cái đó vẫn nên giữ HyperFrames).

## Link
- Repo: https://github.com/YILS-LIN/short-video-factory
- Docs: https://short-video-factory.yils.blog
- Releases: https://github.com/YILS-LIN/short-video-factory/releases

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Short Video Factory là desktop app (Electron), không có REST API public để gọi từ xa.
# Hermes không tương tác trực tiếp được — đây là tool chạy tay/bán tự động trên máy có UI,
# không hợp để wire vào pipeline agent chạy headless trên VPS.
# Nếu cần headless trên VPS, vẫn nên dùng html-video hoặc HyperFrames (đã có sẵn, chạy CLI được).
```

### OpenClaw
```bash
# Không áp dụng trực tiếp — đây là desktop app cần UI, không phải CLI/service.
# OpenClaw chỉ có thể nhắc CEO tải về dùng tay, không tự động hoá được qua Gateway.
```

### Antigravity
```bash
# Không deploy được trên VPS headless (cần UI Electron) — bỏ qua bước deploy tự động.
# Nếu thật sự cần chạy trên máy có màn hình (Windows local của Nobitano), cài bản build sẵn
# từ Releases, không cần Antigravity can thiệp.
```
> ⚠️ Khác các repo khác trong kho, đây là desktop app CÓ UI — không tích hợp được vào pipeline
> agent tự động chạy trên VPS. Dùng tay trên máy Windows local khi cần sản xuất batch nhanh.

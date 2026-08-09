# GenOffice — GitHub Repo

## TL;DR
Bộ office suite AI-native mã nguồn mở (Apache-2.0) của Genspark — Docs/Sheets/Slides/PDF chạy trên macOS/Windows/Linux, mở file .docx/.xlsx/.pptx/.pdf y hệt Microsoft Office nhưng có AI Agent nhúng thẳng trong từng document, không phải chatbot cạnh bên. Đáng chú ý: bản alpha do đúng 1 kỹ sư build trong 1 tuần, tốn ~$10.000 tiền token AI — 2.2k star, 381 fork chỉ sau vài ngày ra mắt (03/08/2026).

## Repo này dùng để làm gì
Đây là bản thay thế Microsoft Office/Google Docs chạy AI ngay trong tài liệu: bôi đen đoạn text, gõ lệnh, AI sửa/viết lại trực tiếp trong Word/Excel/PowerPoint mà không cần rời app hay copy-paste qua ChatGPT. Điểm mạnh nhất là round-trip byte-preserving cho .docx — chỉ đoạn nào mình sửa mới bị ghi lại, phần còn lại của file giữ nguyên byte gốc, mở lại trên Word thật không bị vỡ layout (rất khác kiểu tool AI khác hay làm hỏng định dạng gốc khi export ngược).

## Setup từng bước
1. Tải bản cài sẵn theo OS (không cần build từ source để dùng thường):
   - macOS (Apple Silicon): `GenOffice-0.5.83-arm64.dmg`
   - Windows (x64): `GenOfficeSetup-v0.5.79.exe`
   - Linux Debian/Ubuntu: `sudo apt install ./genoffice_0.5.149_amd64.deb`
   - Linux AppImage: `chmod +x GenOffice-0.5.149.AppImage && ./GenOffice-0.5.149.AppImage` (cần cài `libfuse2` trước, Ubuntu 24.04 thì gói tên `libfuse2t64`)
2. Mở app, đăng nhập bằng tài khoản Genspark — tính năng AI chạy qua server Genspark, không cần tự cắm API key
3. Mở file .docx/.xlsx/.pptx/.pdf như bình thường, bôi đen đoạn cần sửa → gọi AI panel → gõ lệnh
4. Muốn tự build từ source (dev/customize):
```bash
npm install
npm run fixtures     # sinh file .docx test
npm run dev           # chạy cả 5 app + shell qua Vite dev server
npm run dist:mac      # đóng gói bản .dmg macOS
npm run dist:win      # đóng gói bản .exe Windows
```
   Riêng app Sheets cần thêm Rust toolchain (`cargo` trong PATH) để build sidecar xử lý .xlsx.

## Ví dụ thực tế
Mở 1 file .docx báo cáo dài, bôi đen 1 đoạn paragraph lỗi thời → gõ lệnh "viết lại đoạn này theo giọng trang trọng hơn, giữ nguyên số liệu" → AI chỉ generate lại đúng đoạn đó (paragraph patch), phần còn lại file giữ nguyên byte gốc. Lưu lại, mở bằng Microsoft Word thật — layout không vỡ, tracked changes/comments/styles vẫn nguyên. Test tương tự với Sheets: AI có thể đọc toàn bộ state workbook rồi tự viết công thức/pivot table qua tool-calling, không chỉ generate text.

## Lưu ý / Lỗi thường gặp
- Đang ở giai đoạn **Alpha** — repo tự nhận, kỳ vọng có bug, không nên đưa vào production ngay
- Tính năng AI bắt buộc phải có tài khoản Genspark và tốn credit Genspark, không phải free-forever cho phần AI (phần editing thuần office thì free/ad-free)
- Không có privacy policy riêng — nội dung gửi qua AI panel đi qua hạ tầng Genspark, theo chính sách của Genspark (dữ liệu được forward tới OpenAI/Anthropic/Google/xAI/ElevenLabs tùy tác vụ) — cân nhắc nếu xử lý tài liệu nhạy cảm của khách hàng/brand
- Chỉ hỗ trợ macOS Apple Silicon (không hỗ trợ Intel Mac) + Windows x64 + Linux x86_64 glibc 2.34+ — không có bản Linux ARM
- Thư mục `ee/` (enterprise module tương lai) KHÔNG nằm trong Apache-2.0, có license riêng — nếu định fork để bán lại/customize cho khách, đọc kỹ phần này trước

## Phạm vi sử dụng (Tano Agency)
**Chỉ dùng nội bộ** — không đưa vào deliverable/pipeline giao cho khách hàng hay brand (ABTRIP/Wonder Mart/Tano Cafe) cho tới khi qua giai đoạn Alpha. Lý do: (1) chưa ổn định, (2) không có privacy policy riêng — nội dung tài liệu đi qua hạ tầng Genspark/model bên thứ 3, không phù hợp xử lý tài liệu có data khách hàng/brand nhạy cảm. Dùng thoải mái cho việc cá nhân: soạn báo cáo nội bộ, sửa nhanh file .docx/.xlsx không cần rời app.

## Đánh giá cá nhân
- **Điểm mạnh:** Mã nguồn mở thật (Apache-2.0, không phải "open-core giả"), byte-preserving round trip là điểm kỹ thuật hiếm gặp — hầu hết AI doc tool khác export ra là auto làm hỏng định dạng gốc. Free và ad-free cho phần office cơ bản. Chạy được cả 3 OS.
- **Điểm yếu:** Alpha nên chưa ổn định để giao cho khách/dùng production ngay; AI bắt buộc phụ thuộc tài khoản + credit Genspark (không self-host AI được), tức là vẫn có 1 điểm phụ thuộc bên ngoài dù code mở. Không có Linux ARM, chưa có bản mobile.
- **Có nên dùng không:** 7/10 — đáng thử ngay cho việc cá nhân/nội bộ (viết báo cáo, sửa file .docx nhanh không cần rời app), nhưng chưa nên đưa vào pipeline production hay giao cho khách tới khi qua giai đoạn Alpha.

## Link
- Repo: https://github.com/genspark-ai/genoffice
- Docs/Demo: https://www.genspark.ai/genoffice (video demo YouTube: https://www.youtube.com/watch?v=B2pLdMX95v4)

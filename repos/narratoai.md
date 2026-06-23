# NarratoAI — GitHub Repo

## TL;DR
Repo ~10k sao giúp biến video dài thành video recap có lời dẫn (commentary) và cắt ghép tự động bằng AI — một click là xong, không cần edit tay.

## Repo này dùng để làm gì
Mày có một video dài 30 phút — podcast, review sản phẩm, lecture — muốn làm thành clip ngắn có lời bình tự động? NarratoAI làm đúng việc đó.

Nó dùng LLM (Gemini, GPT, v.v.) để phân tích nội dung video, tự viết script commentary, rồi cắt ghép lại thành video recap hoàn chỉnh với voiceover. Tất cả chạy bằng Python, không cần thuê editor.

Use case thực tế:
- Content creator muốn repurpose video dài thành Shorts/TikTok
- Team marketing cần tóm tắt webinar nhanh
- Vibe coder build pipeline nội dung tự động

## Setup từng bước
1. Clone repo:
```bash
git clone https://github.com/linyqh/NarratoAI.git
cd NarratoAI
```
2. Cài dependencies:
```bash
pip install -r requirements.txt
```
3. Copy file config:
```bash
cp .env.example .env
```
4. Điền API key vào `.env` (Gemini hoặc OpenAI key)
5. Chạy:
```bash
python main.py --video path/to/video.mp4
```
6. Output sẽ ra folder `/output` — gồm video recap + script đã generated.

## Ví dụ thực tế
Input: Video YouTube 45 phút về "Cách dùng Claude Code từ A-Z"
→ NarratoAI phân tích transcript, chọn 5 đoạn highlight, viết commentary tiếng Anh cho từng đoạn
→ Cắt ghép lại thành video 3 phút, thêm voiceover AI
→ Output sẵn sàng đăng TikTok/YouTube Shorts

## Lưu ý / Lỗi thường gặp
- Cần ffmpeg cài sẵn trong hệ thống (`brew install ffmpeg` hoặc `apt install ffmpeg`)
- Gemini API có giới hạn free tier — video dài có thể tốn token nhiều
- Video tiếng Việt: chất lượng transcript phụ thuộc model chọn, Gemini Pro xử lý tốt hơn GPT-4o với tiếng Việt
- Lỗi moviepy import → thử `pip install moviepy==1.0.3` (bản cũ stable hơn)

## Đánh giá cá nhân
- Điểm mạnh: Pipeline hoàn chỉnh từ video → recap, không cần ghép tool, có UI web đơn giản
- Điểm yếu: Phụ thuộc nặng vào chất lượng transcript gốc; video âm thanh kém thì output cũng kém. Chưa hỗ trợ tốt tiếng Việt out-of-the-box
- Có nên dùng không: 7/10 — Nếu mày đang làm content và cần repurpose video dài, đây là tool hiếm làm được end-to-end. Nhưng cần tune thêm cho tiếng Việt.

## Link
- Repo: https://github.com/linyqh/NarratoAI
- Docs: xem README trong repo

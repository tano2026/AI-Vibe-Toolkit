# Script Video #19 — Magika: Google Dùng Cái Này Để Scan Gmail Của Mày

**Format:** TikTok / YouTube Shorts (~75s)
**Hook type:** Reveal — "Big tech đang dùng cái này trên data của mày"
**Style:** Không lộ mặt, terminal demo + screen record

---

## 🎬 SCRIPT

**[0s - 6s] HOOK**
> "Gmail scan hàng trăm tỷ file mỗi tuần để phát hiện virus và malware. Công cụ Google dùng để làm việc đó vừa được open source. Và mày cài được trong 10 giây."

*[Show: logo Gmail → logo Google → terminal]*

**[6s - 18s] VẤN ĐỀ**
> "Khi mày build web app có upload file — làm sao biết file đó thực sự là gì? Đừng tin extension. Ai cũng đổi được tên virus.exe thành photo.jpg."

*[Show: đổi tên file trong terminal]*

> "Cách cũ dùng 'magic bytes' — đọc vài byte đầu file. Không đủ chính xác với code, config, CSV."

**[18s - 40s] GIẢI PHÁP — DEMO**
> "Magika của Google — train trên 100 triệu files, 200 loại file, 99% chính xác."

```bash
pip install magika
magika examples/
```

*[Show terminal output]*
```
examples/README.md    → Markdown document
examples/code.py      → Python source
examples/virus.exe    → đổi tên thành photo.jpg → ELF executable ← BỊ BẮT
examples/doc.docx     → Microsoft Word document
```

> "Nó đọc nội dung thực sự bên trong — không phải tên file."

**[40s - 58s] ỨNG DỤNG**
> "3 dòng code bảo vệ upload của mày:"

```python
from magika import Magika
m = Magika()
result = m.identify_bytes(file.read())
if result.output.ct_label not in ['jpeg','png','pdf']:
    raise ValueError("File không hợp lệ!")
```

> "Chạy trên CPU thường — không cần GPU, không cần cloud. 5ms mỗi file."

**[58s - 75s] ONE-LINER + CTA**
> "Magika là gatekeeper file upload mà mọi web app cần nhưng ít ai biết đến."

> "Google đã test ở scale Gmail rồi mới open source — đây không phải đồ chơi."

*[Show: github.com/google/magika, 15.2k stars]*

---

## 📝 CAPTION
```
Google dùng cái này để scan toàn bộ Gmail — giờ mày dùng được miễn phí 🔒

pip install magika — 1 lệnh, bảo vệ file upload khỏi bị bypass extension

15.2k ⭐ Apache 2.0

#security #python #vibecoding #webdev #googleai #github
```

## 🎯 B-ROLL
1. Terminal: `pip install magika` → chạy xong
2. Demo đổi tên `test.exe` → `photo.jpg` → magika vẫn detect đúng
3. Code snippet 3 dòng trên màn hình
4. GitHub repo với số stars

---
*Script v1 — tháng 6/2026*

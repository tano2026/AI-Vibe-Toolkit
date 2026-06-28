# VectCutAPI — GitHub Repo

## TL;DR
Gọi CapCut API để tự động xuất phụ đề SRT chuẩn timeframe — 2,000+ sao GitHub. Kết nối trực tiếp vào engine phụ đề của CapCut mà không cần mở app.

## Repo này dùng để làm gì
VectCutAPI (`sun-guannan/VectCutAPI`) là thư viện Python cho phép gọi internal API của CapCut/剪映 để:
- Tự động generate phụ đề SRT từ audio/video
- Dùng engine nhận dạng giọng nói của CapCut (cực tốt với tiếng Việt, Trung, Anh)
- Export file .srt với timestamp chính xác
- Batch processing nhiều file cùng lúc

Tại sao dùng CapCut API thay vì Whisper? CapCut dùng model riêng của ByteDance, đặc biệt tốt với tiếng Á Đông và có timestamp word-level.

## Setup từng bước
1. Clone repo:
```bash
git clone https://github.com/sun-guannan/VectCutAPI
cd VectCutAPI
pip install -r requirements.txt
```
2. Cần tài khoản CapCut/TikTok và lấy token:
   - Login vào CapCut web hoặc app
   - Lấy authorization token từ headers của request (F12 → Network)
3. Config token:
```python
# Tạo file config.json hoặc set env variable
CAPCUT_TOKEN = "your_token_here"
```
4. Chạy subtitle generation:
```python
from vectcutapi import SubtitleGenerator

gen = SubtitleGenerator(token=CAPCUT_TOKEN)
result = gen.generate("video.mp4", language="vi")  # 'vi' cho tiếng Việt
result.save_srt("output.srt")
```
5. File .srt xuất ra với timeframe chuẩn, import vào CapCut/Premiere/DaVinci

## Ví dụ thực tế
**Bài toán:** Mày có 20 video YouTube cần phụ đề tiếng Việt để upload. Làm thủ công mỗi cái mất 30 phút.

**Tự động hóa với VectCutAPI:**
```python
import os
from vectcutapi import SubtitleGenerator

gen = SubtitleGenerator(token=TOKEN)
videos = [f for f in os.listdir("./videos") if f.endswith(".mp4")]

for video in videos:
    print(f"Processing {video}...")
    result = gen.generate(f"./videos/{video}", language="vi")
    result.save_srt(f"./subs/{video.replace('.mp4', '.srt')}")
    print(f"Done: {video}")
```

**Kết quả:** 20 file .srt chính xác trong ~10 phút, không cần mở CapCut một lần nào.

## Lưu ý / Lỗi thường gặp
- **Token expire** → CapCut token hết hạn, phải login lại lấy token mới (khoảng 24-48h)
- **Rate limit** → đừng gửi quá nhiều request liên tục, thêm `time.sleep(2)` giữa các file
- **Video tiếng ồn nhiều** → accuracy giảm, pre-process audio trước (denoise) cho kết quả tốt hơn
- **ToS** → tương tự DS2API, đây là unofficial API. Dùng cho personal project.

## Đánh giá cá nhân
- **Điểm mạnh:** Engine CapCut nhận dạng tiếng Việt tốt hơn Whisper base. Timestamp chính xác đến từng từ. Batch processing được. 2,000+ stars cho thấy nhiều người dùng thực tế.
- **Điểm yếu:** Unofficial API → dễ break khi CapCut update. Token expire thường xuyên. Phụ thuộc vào tài khoản CapCut.
- **Có nên dùng không: 7/10** — Rất hữu ích cho content creator Việt cần phụ đề tự động. Tốt hơn Whisper cho tiếng Việt. Nhưng maintenance risk cao vì unofficial.

## Link
- Repo: https://github.com/sun-guannan/VectCutAPI
- Stars: 2,000+

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

# Gọi local API sau khi Antigravity deploy
API_URL = "http://localhost:8000"

def process_video(input_path, operation, params=None):
    payload = json.dumps({"input": input_path, "operation": operation,
                          "params": params or {}}).encode()
    req = urllib.request.Request(
        f"{API_URL}/api/process", data=payload,
        headers={"Content-Type": "application/json"}
    )
    return json.loads(urllib.request.urlopen(req).read())

# Check README của repo để biết endpoints cụ thể
```

### OpenClaw
```bash
# Gọi API — không cần npm
```

### Antigravity
```bash
git clone https://github.com/[repo-url]
cd [repo] && pip install -r requirements.txt
python3 main.py --host 0.0.0.0 --port 8000
```
> ⚠️ Đọc README repo để biết endpoints chính xác trước khi deploy.

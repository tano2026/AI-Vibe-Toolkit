# F5-TTS — GitHub Repo

## TL;DR
Clone giọng chỉ cần 3 giây audio mẫu, dùng kiến trúc Flow Matching mới nhất — 14,800+ sao GitHub. Giọng clone tự nhiên hơn hẳn các model cũ, chạy local hoàn toàn.

## Repo này dùng để làm gì
F5-TTS (`SWivid/F5-TTS`) là voice cloning model dùng kỹ thuật **Flow Matching** — thay vì học từng đặc điểm giọng nói, nó học "con đường biến đổi" từ noise thành giọng thật, kết quả tự nhiên và ít artifacts hơn.

Điểm nổi bật:
- **Chỉ cần 3 giây audio mẫu** để clone giọng (không cần dataset dài)
- Flow Matching cho output mượt, không bị metallic như VITS-based models
- Zero-shot: clone giọng người lạ không cần fine-tune
- Hỗ trợ tiếng Anh, Trung, và một số ngôn ngữ khác

## Setup từng bước
1. Cài qua pip:
```bash
pip install f5-tts
```
2. Hoặc clone repo:
```bash
git clone https://github.com/SWivid/F5-TTS
cd F5-TTS
pip install -e .
```
3. Chạy inference với audio mẫu:
```python
from f5_tts.api import F5TTS

tts = F5TTS()
tts.infer(
    ref_audio_path="sample_3s.wav",   # audio mẫu giọng cần clone
    ref_text="Text trong audio mẫu",   # transcript của audio mẫu
    gen_text="Văn bản muốn đọc bằng giọng clone",
    output_path="output.wav"
)
```
4. Hoặc WebUI:
```bash
f5-tts_infer-gradio
```

## Ví dụ thực tế
**Bài toán:** Mày muốn làm video YouTube với giọng đọc giống mình nhưng không cần thu âm thủ công từng video.

**Làm thế nào:**
1. Thu 3-10 giây giọng đọc rõ ràng, lưu thành `my_voice.wav`
2. Ghi lại transcript chính xác của đoạn đó
3. Pass vào F5-TTS với text mới → ra audio với giọng clone
4. Dùng script Python để batch generate cả series video

**Kết quả:** Giọng clone đủ tự nhiên để dùng thương mại, không ai biết đây là AI.

## Lưu ý / Lỗi thường gặp
- **Audio mẫu có tiếng ồn** → clone sẽ bị ảnh hưởng nặng. Phải thu trong phòng im
- **ref_text không khớp audio mẫu** → output bị lệch giọng, phải transcript chính xác 100%
- **CUDA error** → đảm bảo PyTorch version khớp với CUDA version
- **Giọng Việt** → F5-TTS không train tiếng Việt native, nhưng clone giọng Việt được với chất lượng trung bình

## Đánh giá cá nhân
- **Điểm mạnh:** Chỉ cần 3 giây mẫu — rào cản thấp nhất trong class voice cloning. Flow Matching cho output rất tự nhiên. 14,800+ stars, maintained tích cực.
- **Điểm yếu:** Tiếng Việt không phải thế mạnh. Cần GPU tốt để real-time.
- **Có nên dùng không: 9/10** — Best open-source voice cloning hiện tại. Nếu mày dùng ElevenLabs chỉ để clone giọng, F5-TTS thay thế được với chất lượng tương đương, miễn phí.

## Link
- Repo: https://github.com/SWivid/F5-TTS
- Stars: 14,800+
- Paper: "F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching"

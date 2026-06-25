# ChatTTS — GitHub Repo

## TL;DR
Model TTS đàm thoại tự nhiên nhất hiện tại, 39,000+ sao GitHub. Chạy local, hỗ trợ tiếng Anh + Trung, có thể thêm [laugh], [uv_break] để giọng nghe như người thật đang nói chuyện.

## Repo này dùng để làm gì
ChatTTS (repo `2noise/ChatTTS`) là text-to-speech model được train đặc biệt cho hội thoại — không phải đọc văn bản khô khan mà là giọng nói tự nhiên như người đang chat. Điểm khác biệt:
- Hỗ trợ **prosody control**: thêm tag `[laugh]` để cười, `[uv_break]` để thở dài/ngập ngừng, `[lbreak]` để nghỉ dài
- Giọng nghe như đang đàm thoại thật, không phải robot đọc sách
- Chạy 100% local, không cần API
- Hỗ trợ tiếng Anh và tiếng Trung (tiếng Việt không native nhưng có thể mix)

Lý do 39K star: đây là model đầu tiên làm được "conversational TTS" tốt ở mức open-source.

## Setup từng bước
1. Clone repo:
```bash
git clone https://github.com/2noise/ChatTTS
cd ChatTTS
```
2. Cài dependencies:
```bash
pip install -r requirements.txt
```
3. Download model (tự động lần đầu, ~2GB):
```python
import ChatTTS
chat = ChatTTS.Chat()
chat.load(compile=False)  # compile=True nếu muốn nhanh hơn nhưng cần setup thêm
```
4. Generate audio:
```python
texts = ["Chào bạn! [laugh] AI nói chuyện tự nhiên chưa?"]
wavs = chat.infer(texts)
# Save to file
import soundfile as sf
sf.write("output.wav", wavs[0], 24000)
```
5. Hoặc dùng WebUI: `python examples/web/webui.py`

## Ví dụ thực tế
**Input:** `"Thật sự á? [uv_break] Tao không tin nổi cái tool này lại ngon đến vậy. [laugh] Mày thử đi rồi biết!"`

**Output:** File audio với giọng nói ngập ngừng tự nhiên, có tiếng cười nhẹ, pause đúng chỗ — nghe như người thật đang phản ứng, không phải TTS.

**Use case thực:** Làm podcast AI, video drama/storytelling, voiceover có cảm xúc mà không lộ mặt.

## Lưu ý / Lỗi thường gặp
- **Giọng ra không ổn định giữa các lần chạy** → dùng `seed` để fix giọng: `params_infer_code = ChatTTS.Chat.InferCodeParams(spk_emb=spk)` — tạo speaker embedding một lần rồi tái sử dụng
- **Tiếng Việt bị accent lạ** → ChatTTS không train trên tiếng Việt, dùng để làm track English/Chinese hoặc chấp nhận accent
- **OOM trên GPU nhỏ** → set `compile=False`, giảm batch
- **Model load chậm** → bình thường, lần đầu mất 30-60s

## Đánh giá cá nhân
- **Điểm mạnh:** Giọng đàm thoại tự nhiên nhất trong class open-source. Prosody control bằng tag rất tiện. Community lớn (39K stars).
- **Điểm yếu:** Tiếng Việt kém. Output không deterministic (cùng text có thể ra giọng khác nhau). Cần fix seed để ổn định.
- **Có nên dùng không: 8/10** — Best choice nếu làm content tiếng Anh, podcast AI, hay cần giọng có cảm xúc. Không phù hợp làm voiceover tiếng Việt.

## Link
- Repo: https://github.com/2noise/ChatTTS
- Stars: 39,500+
- Demo: có WebUI tại `examples/web/webui.py`

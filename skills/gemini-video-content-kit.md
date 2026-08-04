# Gemini Video Content Kit — Prompt Template / System Prompt

## TL;DR
Bộ 7 prompt độc lập (không cần chạy tuần tự) dùng Gemini/Claude để lên toàn bộ phần "chữ" của 1 video: kịch bản, kế hoạch edit, bản Shorts, ý tưởng B-roll, caption/phụ đề, ý tưởng thumbnail, và bản quy trình tổng. Lưu ý quan trọng: đây là bộ prompt **lên kế hoạch nội dung**, không phải tool tự động cắt/dựng video thật — phần thực thi vẫn cần Remotion/OpenMontage/CapCut.

## Khi nào dùng
- Cần kịch bản nhanh cho 1 video mới (Trùm Sân Bay, AI review) mà chưa có ý tưởng gì trong đầu — chạy Prompt 1 hoặc 3 tuỳ định dạng.
- Có sẵn kịch bản thô/transcript (từ GMSP hoặc từ Whisper) và cần biến thành plan edit chi tiết trước khi giao cho Remotion — dùng Prompt 2.
- Cần B-roll brief để đưa cho người quay/dựng, hoặc query Pollinations/stock footage — dùng Prompt 4.
- Video đã dựng xong, cần caption/phụ đề và thumbnail trước khi đăng — dùng Prompt 5 + 6.
- Không dùng khi: cần video được cắt/dựng thật ngay lập tức — bộ này chỉ ra kế hoạch bằng chữ, đưa tiếp qua `agents/company/` hoặc Remotion Template Factory để thực thi.

## Nội dung skill / prompt

Mỗi prompt dùng độc lập — không bắt buộc chạy theo thứ tự, chọn đúng cái cần cho từng bước sản xuất.

```
### PROMPT 1 — Kịch bản video tức thì
Viết kịch bản video giữ chân người xem cao về [Chủ đề]. Bắt đầu bằng hook
mạnh, giữ nhịp độ nhanh, và có CTA ở cuối.

### PROMPT 2 — Biên tập video AI (kế hoạch edit, không phải edit thật)
Hãy đóng vai biên tập video chuyên nghiệp. Chuyển kịch bản thô này thành kế
hoạch chỉnh sửa hoàn chỉnh với các điểm cắt, hiệu ứng chuyển cảnh, ý tưởng
B-roll, caption, hiệu ứng âm thanh và gợi ý nhịp độ.

[Dán kịch bản thô hoặc transcript ở đây]

### PROMPT 3 — Tạo Shorts viral
Tạo kịch bản video ngắn cho TikTok, Instagram Reels hoặc YouTube Shorts về
[Chủ đề]. Làm cho nó cực kỳ hấp dẫn và tối ưu hoá cho thời gian xem.

### PROMPT 4 — Tạo B-roll
Gợi ý ý tưởng B-roll điện ảnh, góc máy, hình ảnh và cảnh cho chủ đề video
này: [Chủ đề].

### PROMPT 5 — Viết Caption & Phụ đề
Tạo caption và text phụ đề sạch sẽ, hấp dẫn cho video của tôi. Giữ ngắn gọn,
giàu cảm xúc và dễ đọc trên điện thoại.

[Dán transcript hoặc mô tả nội dung video ở đây]

### PROMPT 6 — Tâm lý Thumbnail
Cho tôi 10 ý tưởng thumbnail dễ click cho video về [Chủ đề]. Tập trung vào
sự tò mò, cảm xúc và tỷ lệ nhấp cao.

### PROMPT 7 — Quy trình nội dung hoàn chỉnh
Xây dựng cho tôi quy trình video AI đầy đủ từ ý tưởng → kịch bản → chỉnh sửa
→ thumbnail → caption → chiến lược đăng bài, chỉ rõ công cụ nào làm bước nào.
```

## Setup từng bước
1. Không cần setup gì thêm — dán thẳng prompt cần dùng vào Claude, thay `[Chủ đề]` bằng chủ đề thật.
2. Với Prompt 2 và 5: chuẩn bị sẵn kịch bản thô hoặc transcript (từ Whisper/OmniRoute) trước khi chạy, prompt không tự có nội dung nếu không dán vào.
3. Output Prompt 2 (kế hoạch edit) đưa tiếp cho Remotion Template Factory hoặc OpenMontage để dựng thật — đừng coi đây là bước cuối.
4. Output Prompt 6 (thumbnail) đưa qua Canva/HyperFrames để làm file thật, prompt chỉ ra ý tưởng bằng chữ.
5. Prompt 7 dùng 1 lần đầu khi setup kênh mới, không cần chạy lại mỗi video — nó ra khung quy trình chung, không phải kịch bản.

## Ví dụ thực tế
Video mới cho **Trùm Sân Bay** về chủ đề "3 mẹo qua an ninh sân bay nhanh hơn":
- Prompt 1 ra kịch bản 45 giây, hook "Đừng bao giờ xếp hàng an ninh kiểu này nữa" mở đầu, 3 mẹo, CTA follow cuối.
- Prompt 4 ra B-roll: cảnh quay tay tháo dây nịt, cảnh khay nhựa đi qua máy soi, cảnh đồng hồ đếm thời gian xếp hàng — đưa cho người quay tại Nội Bài trước khi ra hiện trường.
- Prompt 5 lấy transcript thật sau khi quay xong, ra caption CapCut-ready.
- Prompt 6 ra 10 ý tưởng thumbnail, chọn được bản "mặt hoảng hốt + đồng hồ đỏ" tương phản tốt trên feed TikTok.

Với **GMSP** (podcast dài): dùng Prompt 2 lấy transcript tập mới, ra kế hoạch cắt thành 3 đoạn Shorts trước khi đưa qua OpenMontage dựng bản có voiceover.

## Lưu ý / Lỗi thường gặp
- **Đừng hiểu nhầm Prompt 2 là "AI tự edit video"** — output chỉ là văn bản mô tả các điểm cắt/hiệu ứng, không phải file video đã dựng. Tên gọi gốc "Gemini có thể chỉnh sửa video như creator chuyên nghiệp" là cách nói marketing quá tay — thực chất Gemini/Claude không thao tác pixel video được.
- **7 prompt này độc lập, không có context nối tiếp** — khác với `brand-identity-factory` hay `ai-marketing-adoption-map` (bắt buộc chạy tuần tự). Dùng cái nào cần cái đó, không phải chạy hết cả 7 mỗi lần.
- **Prompt 3 (Shorts viral) dễ ra script chung chung** nếu không cho biết platform cụ thể — luôn ghi rõ TikTok hay Shorts hay Reels vì nhịp độ và độ dài tối ưu khác nhau.
- **Prompt 6 (thumbnail) chỉ ra ý tưởng chữ** — cần người review trước khi đưa qua Canva, vì AI hay đề xuất ý tưởng giật gân quá mức so với brand voice thật (đặc biệt với Airfare Decoded — kênh tiếng Anh hướng B2B, không hợp thumbnail kiểu giật gân TikTok).

## Đánh giá cá nhân
- **Điểm mạnh:** Prompt ngắn, dùng lẻ nhanh, không cần setup gì — hợp lúc cần ý tưởng gấp cho 1 video cụ thể. Prompt 4 (B-roll) và Prompt 6 (thumbnail) đặc biệt hữu ích vì đây là 2 khâu hay bị bỏ qua khi làm content vội.
- **Điểm yếu:** Không phải 1 hệ thống thật — chỉ là 7 câu hỏi rời rạc, tên gọi "biên tập video AI" gây hiểu lầm về khả năng thật của công cụ. Không thay được bước dựng video thật, dễ khiến người mới nghĩ nhầm là đã có pipeline hoàn chỉnh trong khi mới chỉ có phần kịch bản.
- **Có nên dùng không:** 6/10 — dùng được như bộ prompt tiện dụng hàng ngày, nhưng không nên PR như 1 "hệ thống edit AI hoàn chỉnh". Giá trị thật nằm ở việc tiết kiệm thời gian brainstorm kịch bản/caption/thumbnail, không phải thay thế công đoạn dựng video.

## Link
- Nguồn gốc skill: Tổng hợp từ bộ "7 prompt Gemini chỉnh sửa video" lan truyền trên mạng xã hội, Tano Agency điều chỉnh lại tên gọi cho đúng bản chất (kế hoạch nội dung, không phải edit tool) và gắn ví dụ thực tế theo các kênh đang vận hành.

---

## 🤖 Agent Integration

### Hermes (Python)
Dùng cho bước lên kịch bản/caption/thumbnail-idea tự động trước khi giao cho bước dựng video thật (Remotion/OpenMontage). Không tự động hoá bước dựng — chỉ sinh text.

```python
import urllib.request, json

OMNIROUTE_URL = "https://your-omniroute-endpoint/v1/chat/completions"
API_KEY = "[OMNIROUTE_KEY]"

PROMPT_BANK = {
    "kich_ban": "Viết kịch bản video giữ chân người xem cao về {topic}. Bắt đầu bằng hook mạnh, giữ nhịp độ nhanh, và có CTA ở cuối.",
    "edit_plan": "Hãy đóng vai biên tập video chuyên nghiệp. Chuyển kịch bản thô này thành kế hoạch chỉnh sửa hoàn chỉnh với các điểm cắt, hiệu ứng chuyển cảnh, ý tưởng B-roll, caption, hiệu ứng âm thanh và gợi ý nhịp độ.\n\n{raw_script}",
    "shorts": "Tạo kịch bản video ngắn cho {platform} về {topic}. Làm cho nó cực kỳ hấp dẫn và tối ưu hoá cho thời gian xem.",
    "b_roll": "Gợi ý ý tưởng B-roll điện ảnh, góc máy, hình ảnh và cảnh cho chủ đề video này: {topic}.",
    "caption": "Tạo caption và text phụ đề sạch sẽ, hấp dẫn cho video của tôi. Giữ ngắn gọn, giàu cảm xúc và dễ đọc trên điện thoại.\n\n{transcript}",
    "thumbnail": "Cho tôi 10 ý tưởng thumbnail dễ click cho video về {topic}. Tập trung vào sự tò mò, cảm xúc và tỷ lệ nhấp cao.",
}

def call_llm(prompt_text):
    body = {"model": "claude-sonnet",  # route=creative theo OmniRoute config
            "messages": [{"role": "user", "content": prompt_text}]}
    req = urllib.request.Request(
        OMNIROUTE_URL, data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        method="POST")
    resp = json.loads(urllib.request.urlopen(req).read())
    return resp["choices"][0]["message"]["content"]

def run_prompt(key: str, **kwargs) -> str:
    template = PROMPT_BANK[key]
    return call_llm(template.format(**kwargs))
```

### OpenClaw
```bash
# Gọi lẻ từng prompt qua Telegram, không cần chạy hết chuỗi
/video-script <topic>
/video-thumbnail <topic>
```

### Antigravity
Không cần deploy riêng — chạy qua OmniRoute có sẵn. Output text chuyển tiếp thủ công (hoặc qua OpenClaw) sang bước dựng video thật ở Remotion Template Factory / OpenMontage.

> ⚠️ Output Prompt 2 và Prompt 6 KHÔNG phải file video/thumbnail thật — chỉ là kế
> hoạch/ý tưởng bằng chữ. Agent không được tự động đăng dựa trên output các
> prompt này mà chưa qua bước dựng video và duyệt Brand Check thật.

# ViMax — GitHub Repo

## TL;DR
Agent AI tạo video hoàn chỉnh từ đầu đến cuối: tự viết kịch bản, tự đạo diễn, tự sản xuất và generate video — 10,600+ sao GitHub. Không cần quay phim, không cần diễn viên.

## Repo này dùng để làm gì
ViMax (`HKUDS/ViMax`) là hệ thống multi-agent cho video generation tự động. Thay vì mày phải làm từng bước (ý tưởng → kịch bản → storyboard → generate), ViMax tích hợp 4 "vai":
- **Director**: nhận ý tưởng, quyết định phong cách, camera angles
- **Screenwriter**: viết script chi tiết từng cảnh
- **Producer**: lên kế hoạch production, quản lý resource
- **Video Generator**: call video generation models để render

Input: một câu mô tả ý tưởng
Output: video hoàn chỉnh với narration, transitions, soundtrack

## Setup từng bước
1. Clone repo:
```bash
git clone https://github.com/HKUDS/ViMax
cd ViMax
pip install -r requirements.txt
```
2. Cài dependencies (cần một số video generation model backend):
```bash
# ViMax support nhiều backend: CogVideo, Wan, v.v.
# Check docs để chọn backend phù hợp với GPU của mày
```
3. Config API keys trong `.env`:
```
OPENAI_API_KEY=xxx  # hoặc dùng local LLM
VIDEO_GEN_API=xxx   # tùy backend chọn
```
4. Chạy:
```python
from vimax import ViMaxPipeline

pipeline = ViMaxPipeline()
video = pipeline.generate("Một ngày làm việc của một vibe coder tại Hà Nội")
video.save("output.mp4")
```

## Ví dụ thực tế
**Bài toán:** Mày muốn làm series YouTube "AI Tools Review" dạng documentary ngắn mà không có ekip quay phim.

**Dùng ViMax:**
1. Input: `"Review tool ChatTTS: AI đọc văn bản như người thật, dùng cho vlogger"`
2. ViMax tự viết script, tạo visual storyboard
3. Generate video với voiceover, b-roll, text overlays
4. Export MP4 sẵn upload

**Kết quả:** Video ~2-3 phút, style documentary, không cần quay một frame nào.

## Lưu ý / Lỗi thường gặp
- **Cần GPU mạnh hoặc API** → video generation tốn tài nguyên, không chạy được trên laptop thường. Cần GPU 24GB+ hoặc dùng API của CogVideo/Wan
- **Video quality phụ thuộc backend** → ViMax là orchestrator, chất lượng video thật ra do model generate (CogVideo, Sora-like models)
- **Latency cao** → generate 30 giây video có thể mất 5-15 phút tùy backend
- **Tiếng Việt** → script generation OK nếu dùng GPT-4/Claude làm LLM backbone, nhưng video generated vẫn style "AI generic"

## Đánh giá cá nhân
- **Điểm mạnh:** Concept rất mạnh — agentic video production. Kiến trúc multi-agent rõ ràng, dễ extend. 10,600+ sao chứng minh market cần cái này.
- **Điểm yếu:** Còn research-level, chưa production-ready. Setup phức tạp. Phụ thuộc vào video generation API tốn tiền. Chất lượng video generate vẫn chưa bằng quay thật.
- **Có nên dùng không: 7/10** — Theo dõi repo này, nó sẽ là big deal khi video generation models mạnh hơn. Hiện tại phù hợp để experiment và học kiến trúc agentic, chưa phù hợp production.

## Link
- Repo: https://github.com/HKUDS/ViMax
- Stars: 10,600+
- Paper: "ViMax: Agentic Video Generation (Director, Screenwriter, Producer, and Video Generator All-in-One)"

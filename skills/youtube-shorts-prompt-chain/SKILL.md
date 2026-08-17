# YouTube Shorts Prompt Chain — Prompt Template / System Prompt

## TL;DR
Bộ 7 prompt nối chuỗi, biến 1 niche/ý tưởng thành: 30 ý tưởng → hook → kịch bản 30-60s → storyboard chia cảnh → prompt ảnh/video AI cho từng cảnh → voice-over/subtitle → nhân bản 1 ý tưởng thành 10 video khác nhau. Thiết kế riêng cho pipeline sản xuất Shorts bằng AI, không cần quay mặt.

## Khi nào dùng
- Bí ý tưởng cho kênh Shorts mới hoặc đang cạn content.
- Cần chuẩn hoá quy trình từ ý tưởng thô → kịch bản → cảnh quay → prompt ảnh AI, để giao cho agent (Hermes/OpenClaw) chạy tự động qua OmniRoute.
- Kênh chạy theo hướng AI-generated visual (Pollinations, HyperFrames, Remotion...) — không quay người thật, cần mô tả cảnh cực chi tiết cho model ảnh/video.
- Muốn tận dụng tối đa 1 ý tưởng gốc thành nhiều video mà không lặp ý (khi content lịch dày, cần volume).

Không dùng cho: video dài (>5 phút, cần cấu trúc khác), video cần quay thật với diễn viên/địa điểm cụ thể (bước 4-5 giả định sản xuất bằng AI).

## Nội dung skill / prompt

```
1️⃣ PROMPT: TÌM 30 Ý TƯỞNG YOUTUBE SHORTS

Hãy đóng vai chuyên gia xây dựng kênh YouTube Shorts.

Tôi muốn xây dựng kênh về chủ đề:
[CHỦ ĐỀ/NICHE]

Đối tượng khán giả:
[ĐỐI TƯỢNG]

Mục tiêu kênh:
[TĂNG VIEW/TĂNG FOLLOW/XÂY THƯƠNG HIỆU/BÁN SẢN PHẨM]

Hãy tạo cho tôi 30 ý tưởng YouTube Shorts có thể triển khai nhanh.

Với mỗi ý tưởng hãy cung cấp:
Tiêu đề.
Ý tưởng chính.
Nỗi đau hoặc mong muốn của người xem.
Hook 3 giây đầu.
Giá trị chính người xem nhận được.
Dạng video phù hợp.
CTA.

Chia ý tưởng thành các nhóm:
Giá trị thực tế / Giải trí / Gây tò mò / Top-list / Before–After / Kể chuyện / Sai lầm / Mẹo nhanh.

Không tạo các ý tưởng quá giống nhau.
Ưu tiên những ý tưởng có thể sản xuất nhanh bằng AI và không cần quay mặt.

2️⃣ PROMPT: VIẾT HOOK KHIẾN NGƯỜI XEM DỪNG LƯỚT

Dựa trên ý tưởng Shorts:
[Ý TƯỞNG]

Hãy tạo 20 hook khác nhau cho 3 giây đầu tiên.

Chia thành:
Hook gây tò mò.
Hook gây bất ngờ.
Hook đánh vào nỗi đau.
Hook dạng "Bạn có biết...?"
Hook dạng cảnh báo.

Mỗi hook phải:
Ngắn.
Tự nhiên.
Dễ đọc thành lời thoại.
Không phóng đại.
Không clickbait sai sự thật.

Sau đó chọn ra 5 hook mạnh nhất và giải thích tại sao chúng có khả năng giữ người xem.

3️⃣ PROMPT: BIẾN Ý TƯỞNG THÀNH KỊCH BẢN 30–60 GIÂY

Hãy đóng vai biên kịch YouTube Shorts.

Dựa trên:
Chủ đề: [CHỦ ĐỀ]
Hook: [HOOK]
Đối tượng: [ĐỐI TƯỢNG]

Hãy viết một kịch bản Shorts dài khoảng 30–60 giây.

Cấu trúc:
Hook → Vấn đề → Tạo khoảng trống tò mò → Nội dung chính → Ví dụ → Kết luận → CTA

Yêu cầu:
Mỗi câu ngắn, dễ đọc.
Không giải thích lan man.
Mỗi 3–5 giây phải có một điểm mới.
Ngôn ngữ tự nhiên như đang nói chuyện.
Không lặp ý.

Hãy trình bày thành bảng:
Thời gian | Lời thoại | Mục đích của cảnh | Text trên màn hình.

4️⃣ PROMPT: CHIA KỊCH BẢN THÀNH CẢNH ĐỂ AI SẢN XUẤT

Dựa trên kịch bản:
[DÁN KỊCH BẢN]

Hãy đóng vai đạo diễn YouTube Shorts.

Chia video thành các cảnh dài khoảng 2–5 giây/cảnh.

Với mỗi cảnh hãy xác định:
Nội dung cần thể hiện.
Nhân vật/đối tượng.
Bối cảnh.
Hành động.
Góc máy.
Chuyển động camera.
Text trên màn hình.
Hiệu ứng chuyển cảnh.
Âm thanh phù hợp.

Ưu tiên những cảnh có thể tạo bằng AI image/video, không yêu cầu quay phim thực tế.

Đảm bảo nhân vật, bối cảnh và phong cách hình ảnh nhất quán xuyên suốt video.

5️⃣ PROMPT: TẠO PROMPT HÌNH ẢNH/VIDEO CHO TỪNG CẢNH

Dựa trên storyboard:
[DÁN STORYBOARD]

Hãy viết prompt tạo hình ảnh hoặc video AI cho từng cảnh.

Mỗi prompt phải mô tả rõ:
Chủ thể.
Trang phục.
Bối cảnh.
Thời gian trong ngày.
Ánh sáng.
Góc máy.
Tiêu cự/cảm giác ống kính.
Bố cục.
Hành động.
Phong cách hình ảnh.
Tỷ lệ khung hình 9:16.

Hãy duy trì sự nhất quán về:
nhân vật + màu sắc + bối cảnh + phong cách hình ảnh.

Không chèn chữ vào hình ảnh nếu công cụ tạo ảnh thường tạo chữ không chính xác.

Trình bày từng prompt riêng để tôi có thể copy trực tiếp.

6️⃣ PROMPT: TẠO LỜI THOẠI VÀ PHỤ ĐỀ TỰ ĐỘNG

Dựa trên kịch bản Shorts:
[DÁN KỊCH BẢN]

Hãy chuẩn bị nội dung cho voice-over và subtitle.

Tạo:
1. Bản voice-over
Câu ngắn.
Nhịp đọc tự nhiên.
Có điểm nhấn ở các từ quan trọng.

2. Bản subtitle
Chia thành từng câu ngắn.
Mỗi dòng không quá dài.
Ưu tiên 1–2 ý chính trên mỗi màn hình.

3. Điểm nhấn
Xác định những từ/cụm từ cần làm nổi bật trên màn hình.

4. Nhịp dựng
Gợi ý chỗ nên:
Cắt cảnh.
Zoom.
Thay hình.
Thêm hiệu ứng.
Chuyển cảnh.

Mục tiêu là giúp người xem có thể vừa xem vừa hiểu nội dung ngay cả khi không bật âm thanh.

7️⃣ PROMPT: BIẾN 1 Ý TƯỞNG THÀNH 10 VIDEO KHÁC NHAU

Tôi có một ý tưởng gốc:
[Ý TƯỞNG]

Hãy giúp tôi biến ý tưởng này thành 10 YouTube Shorts khác nhau mà không bị lặp lại.

Với mỗi video hãy thay đổi ít nhất một yếu tố:
Hook.
Góc nhìn.
Ví dụ.
Đối tượng.
Câu chuyện.
Cách giải quyết vấn đề.
CTA.

Mỗi video cần có:
Tiêu đề → Hook → Nội dung chính → CTA → Dạng hình ảnh/video đề xuất.

Không chỉ thay đổi vài từ.

Hãy tạo ra 10 nội dung thực sự khác nhau nhưng vẫn xoay quanh cùng một chủ đề.

Ưu tiên những video có thể sản xuất nhanh bằng AI và phù hợp với YouTube Shorts.
```

## Setup từng bước
1. Dùng prompt 1 với Claude/ChatGPT, điền `[CHỦ ĐỀ/NICHE]`, `[ĐỐI TƯỢNG]`, `[MỤC TIÊU KÊNH]` → lấy 30 ý tưởng, chọn 1 ý tưởng ưng nhất.
2. Dán ý tưởng đã chọn vào prompt 2 → lấy 20 hook, chọn 1 hook mạnh nhất (hoặc để AI tự chọn 5 rồi mình pick).
3. Dán chủ đề + hook + đối tượng vào prompt 3 → ra kịch bản dạng bảng (Thời gian | Lời thoại | Mục đích cảnh | Text màn hình).
4. Dán kịch bản vào prompt 4 → ra storyboard chia cảnh 2-5s/cảnh, đủ thông số camera/ánh sáng/hành động.
5. Dán storyboard vào prompt 5 → ra prompt ảnh/video AI copy-paste được cho từng cảnh (đẩy sang Pollinations/HyperFrames/Remotion).
6. Dán kịch bản gốc vào prompt 6 (độc lập, không cần chờ bước 4-5) → lấy voice-over cho ElevenLabs + subtitle + nhịp dựng cho CapCut.
7. Khi cạn ý tưởng, dán 1 ý tưởng gốc đã chạy tốt vào prompt 7 → nhân ra 10 biến thể để giữ nhịp đăng bài mà không cần research lại từ đầu.

## Ví dụ thực tế
Input niche: "Mẹo tiết kiệm khi đi sân bay Nội Bài" (khớp use case ABTRIP/Trùm Sân Bay), đối tượng: người đi công tác/du lịch lần đầu qua Nội Bài, mục tiêu: tăng lead Fast Track/SIM.

- Prompt 1 → ra ý tưởng "3 cách qua an ninh Nội Bài nhanh hơn 10 phút" (nhóm Mẹo nhanh) kèm hook nháp, nỗi đau (sợ trễ chuyến), CTA (theo dõi để biết thêm mẹo sân bay).
- Prompt 2 → 20 hook cho đúng ý tưởng đó, ví dụ hook cảnh báo: "Nếu mày làm điều này ở an ninh Nội Bài, mày sẽ bị giữ lại 15 phút" — chọn 5 hook mạnh nhất kèm lý do (tạo nỗi sợ mất thời gian, rất đúng insight của người đi công tác).
- Prompt 3 → bảng kịch bản 45 giây, mỗi 3-5s có 1 điểm mới (mẹo 1, mẹo 2, mẹo 3, CTA Fast Track).
- Prompt 4 → 8-10 cảnh, ví dụ "Cảnh 3: nhân vật đứng trước cổng an ninh, góc máy ngang tầm mắt, ánh sáng sân bay, text overlay 'Mẹo 2'".
- Prompt 5 → prompt ảnh AI 9:16 cho từng cảnh, giữ nhất quán nhân vật (áo polo xanh navy, tóc ngắn) xuyên suốt để đẩy vào Pollinations.
- Prompt 6 → voice-over ElevenLabs-ready (câu ngắn, không ký tự đặc biệt) + subtitle chia dòng.
- Prompt 7 → 10 biến thể từ ý tưởng gốc: đổi sang sân bay khác, đổi đối tượng (gia đình có trẻ nhỏ), đổi góc nhìn (nhân viên an ninh kể chuyện), v.v.

## Lưu ý / Lỗi thường gặp
- Prompt 5 nhắc "không chèn chữ vào hình ảnh" nhưng nhiều model ảnh (kể cả bản mới) vẫn tự vẽ chữ sai chính tả nếu prompt có từ tiếng Việt trong bối cảnh — nên tách riêng text overlay ra làm ở bước dựng (CapCut) thay vì để model ảnh tự sinh.
- Bảng kịch bản ở prompt 3 đôi khi bị AI làm quá dài dòng ở cột "Lời thoại" dù đã yêu cầu ngắn — cần tự cắt bớt tay trước khi đưa qua ElevenLabs, nếu không voice-over sẽ dư giây so với cảnh.
- Prompt 7 (nhân bản 10 video) dễ bị AI lặp ý ở biến thể 7-10 nếu chủ đề gốc hẹp — nên giới hạn dùng prompt này khi ý tưởng gốc đủ rộng (có ít nhất 3-4 góc nhìn khả thi), niche quá hẹp thì 10 video sẽ na ná nhau dù đổi hook.
- Chuỗi 7 prompt này KHÔNG có bước brand check / guardrail nội dung — nếu dùng cho brand có yêu cầu tuân thủ (ví dụ nội dung tài chính, y tế), cần thêm bước kiểm duyệt riêng, tool này không tự làm.

## Đánh giá cá nhân
- Điểm mạnh: chuỗi liền mạch từ ý tưởng thô đến prompt ảnh AI copy-paste được, rất khớp workflow "content bằng AI không quay mặt" mà Tano Agency đang chạy (Trùm Sân Bay, Airfare Decoded). Cấu trúc bảng ở prompt 3-4 dễ đẩy thẳng vào pipeline agent (Research → Ideation → Writer → Visual trong `agents/trum-san-bay/`).
- Điểm yếu: đây thuần là prompt template, không phải tool/API — không tự động hoá được nếu không có người ngồi copy-paste qua từng bước, hoặc phải tự viết code chain 7 lần gọi LLM (xem Agent Integration bên dưới). Không có cơ chế fact-check hay brand-check tích hợp, phải ghép thêm skill khác (`source-evaluation`, brand check trong 9-agent pipeline) nếu cần độ tin cậy cao hơn.
- Có nên dùng không: 7/10 — dùng tốt làm khung sườn ý tưởng + kịch bản + storyboard, nhưng cần người review giữa các bước (đặc biệt bước 3 và 7) trước khi đẩy sang sản xuất, không nên để agent chạy full-auto không giám sát.

## Link
- Nguồn gốc skill: prompt do Nobitano cung cấp trực tiếp (không có nguồn public gốc).

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Chain 7 prompt qua OmniRoute (model creative/factcheck = Claude Sonnet theo LLM routing đã cấu hình)
# Copy paste chạy được luôn — không dùng MCP, gọi thẳng OmniRoute endpoint

import urllib.request, json

OMNIROUTE_URL = "http://100.90.212.62:PORT/v1/chat/completions"  # điền đúng port/endpoint OmniRoute thực tế
MODEL = "claude-sonnet"  # tier creative theo LLM routing (OmniRoute tiers)

PROMPTS = {
    "ideas": """Hãy đóng vai chuyên gia xây dựng kênh YouTube Shorts.

Tôi muốn xây dựng kênh về chủ đề:
{niche}

Đối tượng khán giả:
{audience}

Mục tiêu kênh:
{goal}

Hãy tạo cho tôi 30 ý tưởng YouTube Shorts có thể triển khai nhanh...""",
    # (điền đủ 7 prompt như trong "Nội dung skill / prompt" ở trên, dùng .format() để fill placeholder)
}

def call_llm(prompt_text):
    payload = {"model": MODEL, "messages": [{"role": "user", "content": prompt_text}]}
    req = urllib.request.Request(
        OMNIROUTE_URL, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    resp = json.loads(urllib.request.urlopen(req).read())
    return resp["choices"][0]["message"]["content"]

def run_chain(niche, audience, goal):
    step1 = call_llm(PROMPTS["ideas"].format(niche=niche, audience=audience, goal=goal))
    # → parse ra ý tưởng đầu tiên (hoặc để user chọn qua Telegram), rồi tiếp tục chain
    # step2 = call_llm(PROMPTS["hooks"].format(idea=chosen_idea))
    # ... lặp tới step7
    return step1

if __name__ == "__main__":
    result = run_chain(
        niche="Mẹo tiết kiệm khi đi sân bay Nội Bài",
        audience="người đi công tác/du lịch lần đầu qua Nội Bài",
        goal="tăng lead Fast Track/SIM")
    print(result)
```
> ⚠️ Chain 7 bước nên có checkpoint người duyệt giữa bước 1 (chọn ý tưởng) và bước 3 (duyệt kịch bản trước khi sinh storyboard) — không nên để Hermes chạy tuốt tuồn tuột từ ý tưởng thẳng ra prompt ảnh không ai xem qua, dễ ra content lệch brand hoặc sai insight.

### OpenClaw
```bash
# Đăng ký chain này như 1 command Telegram, vd /shorts-chain "niche" "audience" "goal"
# OpenClaw nhận lệnh → gọi Hermes chạy run_chain() → trả kết quả từng bước về Telegram để Nobitano duyệt
```

### Antigravity
```bash
# Không cần deploy service riêng — chain chỉ gọi OmniRoute sẵn có trên VPS, không có state cần persist ngoài SQLite log (nếu muốn lưu lịch sử ý tưởng đã dùng để tránh trùng, thêm bảng vào Mission Control SQLite).
```

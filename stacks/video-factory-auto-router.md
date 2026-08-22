---
name: video-factory-auto-router
description: >
  Use case: đưa 1 chủ đề vào, hệ thống tự phân loại nội dung là "số liệu/so sánh" hay
  "kể chuyện/giải thích", tự route sang đúng engine (Remotion Template Factory hoặc
  Vox Director), tự chạy hết pipeline, chỉ dừng lại xin duyệt ở 1 điểm chốt trước khi
  publish. Biến 2 stack rời (Remotion, Vox Director) thành 1 công thức auto duy nhất.
---

# Video Factory Auto-Router — 1 Topic Vào, Video Ra, Tự Chọn Engine

## TL;DR
Thay vì mày tự quyết "làm video này bằng Remotion hay Vox Director", công thức này để
1 lớp classifier (LLM rẻ qua OmniRoute) đọc topic/brief rồi tự quyết, tự gọi đúng pipeline,
tự render, và chỉ dừng lại đúng 1 lần để mày duyệt trước khi đẩy ra Postiz. Áp được cho
cả 5 kênh content của Tano (Trùm Sân Bay, Airfare Decoded, GMSP, Tano Cafe, ABTRIP).

---

## Các tool trong stack

1. **Router/Classifier** (mới, script Node.js nhỏ) → đọc topic, gọi OmniRoute route=`cheap`
   (DeepSeek V3) để phân loại nội dung, quyết định gọi engine nào.
2. **Remotion Template Factory** (đã có: `stacks/remotion-template-factory.md`) → engine cho
   nội dung số liệu/so sánh/list — component React nhận props, render nhanh, rẻ, kiểm soát
   pixel-level.
3. **Vox Director** (đã có: `skills/vox-director.md`) → engine cho nội dung kể chuyện/giải
   thích — AI tự sinh visual paper-collage qua Atlas Cloud (nano-banana-2 + gemini-omni-flash),
   giọng đọc xai/tts-v1, nhạc minimax/music-2.6.
4. **Atlas Cloud API** (unified, OpenAI-compatible) → hạ tầng chạy Vox Director headless,
   không cần mở Claude Code — gọi thẳng REST, dùng được cho Hermes.
5. **Postiz** (đã có trong skill library) → điểm cuối, nhận file MP4 đã duyệt, lên lịch đăng.

---

## Công thức phân loại (trái tim của cái router)

```
NẾU topic chứa: số liệu, giá, so sánh, "top N", bảng, %, thống kê, deadline/countdown
  → ENGINE = Remotion Template Factory
  → lý do: nội dung dạng thẻ (card), cần chính xác con số, không cần AI "diễn"

NẾU topic chứa: "là gì", "tại sao", "cách", hành trình, câu chuyện, giải thích khái niệm
  → ENGINE = Vox Director
  → lý do: nội dung cần kể chuyện, hình ảnh ẩn dụ, AI generate visual tốt hơn code tay

NẾU cả 2 tín hiệu cùng xuất hiện (vd: "Fast Track là gì — và tại sao rẻ hơn 40%")
  → ENGINE = Hybrid: Vox Director dựng phần mở/kể chuyện (10-15s)
             + Remotion chèn 1 "data card" ở giữa cho con số 40%
             + ghép lại bằng ffmpeg concat
```

Heuristic keyword-match chạy trước (free, tức thì). Chỉ khi câu topic mơ hồ (không match
rule nào rõ ràng) mới fallback gọi LLM classify — tiết kiệm token, đa số case rule-based
là đủ.

---

## Workflow ghép nối

```
[Topic 1 câu, vd: "Top 3 lý do khách chọn Fast Track thay vì xếp hàng thường"]
        ↓ classify (rule-based trước, LLM fallback)
        ↓
   ┌────┴─────┐
   ▼          ▼
[Remotion]  [Vox Director]
   │          │
   │          ├─ 1. beat map (LLM sinh, auto-pick option đầu nếu chạy full-auto)
   │          ├─ 2. style bake-off (auto-pick theo brand preset đã lưu sẵn, vd
   │          │     ABTRIP = preset "clean-navy", Trùm Sân Bay = preset "bold-yellow")
   │          ├─ 3. keyframes (nano-banana-2 qua Atlas Cloud API)
   │          ├─ 4. motion (gemini-omni-flash qua Atlas Cloud API)
   │          ├─ 5. voice + music (xai/tts-v1 + minimax/music-2.6)
   │          └─ 6. ffmpeg assemble
   │
   └─ render props.json → renderMedia() → MP4
        ↓
   [GATE — điểm dừng duy nhất]
        ↓ Nobitano duyệt preview (thumbnail + 5s đầu)
        ↓
   [Postiz — lên lịch đăng đúng kênh]
```

**Vì sao chỉ giữ 1 GATE thay vì 2 (beat map + style) như Vox Director gốc:**
Chạy full-auto, beat map và style preset được auto-pick theo rule đã định sẵn theo brand
(xem bảng dưới). Đổi lại tốn API Atlas Cloud dù kết quả không ưng — đây là trade-off có
chủ đích, không phải bug. Nếu content quan trọng (video mở kênh mới, campaign lớn) thì tắt
full-auto, trả về 2 gate gốc của Vox Director.

**Bảng preset theo brand (điền sẵn để auto-pick không cần hỏi):**

| Brand | Style preset (Vox) | Data card theme (Remotion) |
|---|---|---|
| ABTRIP / Fast Track | clean-navy, ít chữ | navy + vàng gold accent |
| Trùm Sân Bay | bold-yellow, giọng gen Z | high-contrast, số to |
| Airfare Decoded | minimal, tiếng Anh | biểu đồ + chart nhiều |
| GMSP | warm-paper, giọng trầm | ít dùng — nội dung chủ yếu Vox |
| Wonder Mart | product-forward | giá + discount badge |

---

## Ví dụ thực tế

**Input:** `"So sánh giá SIM du lịch ABTRIP vs mua tại quầy sân bay"`
→ Router match keyword "so sánh", "giá" → chọn **Remotion**
→ Render data card 2 cột, số liệu thật từ bảng giá → MP4 trong ~30 giây (không tốn API gen ảnh)

**Input:** `"Vì sao Fast Track lại nhanh hơn xếp hàng thường ở Nội Bài"`
→ Router match "vì sao" → chọn **Vox Director**
→ Beat map tự sinh (auto-pick), style "clean-navy" theo preset ABTRIP → visual + voice + nhạc
→ Dừng lại xin duyệt trước khi push Postiz

**Input:** `"Fast Track là gì — và tại sao rẻ hơn 40% so với dịch vụ khác"`
→ Match cả "là gì" (Vox) và "40%" (Remotion) → **Hybrid**
→ Vox dựng 12s mở đầu kể chuyện → Remotion chèn data card "40%" ở giây 8-11 → ffmpeg concat

---

## Đã test thực tế

- **Router classify:** test 9 câu topic thật (context ABTRIP/Trùm Sân Bay) → phát hiện bug
  thiếu keyword `"vì sao"` (chỉ có `"tại sao"`) khiến 1 câu rơi sai vào ambiguous. Đã fix,
  thêm cả `"bao nhiêu"`, `"vì đâu"`. Code hiện tại (bản dưới) đã qua fix này.
- **Engine Remotion:** viết thật component `DataCard.tsx` (data card so sánh giá, có
  animation), type-check pass 100%. Render thật cần Chrome Headless Shell (~300MB, tải từ
  `remotion.media`) — máy có network mở/VPS thì chạy bình thường, sandbox hạn chế domain
  thì không tải được. Không phải lỗi code.
- **Engine Vox Director:** chưa test được — cần `ATLASCLOUD_API_KEY` thật + network mở tới
  `atlascloud.ai`, phải chạy trên máy/VPS thật.

**Cách test trên VPS/máy local:**
```bash
npx create-video@latest my-video --template blank
# copy DataCard.tsx + index.tsx vào src/, thêm tsconfig.json
npm install remotion @remotion/cli react react-dom
npx remotion render src/entry.tsx DataCard out/video.mp4
# Lần đầu sẽ tự tải Chrome Headless Shell — cần network mở, không bị chặn egress
```

## Lưu ý / Lỗi thường gặp

- **Auto-pick beat map/style sai gu** → nếu thấy output lệch quá nhiều so với brand voice,
  tắt full-auto cho brand đó, trả về 2-gate thủ công (chỉnh trong bảng preset).
- **Atlas Cloud tính phí theo giây video (Gemini Omni Flash ~$0.10/s, cap 10s/clip) + theo ảnh
  (Nano Banana 2 ~$0.0336/ảnh 1K)** → 1 video Vox Director 20s có thể tốn ~$2-3 tiền API, cần
  budget cap trong script (giới hạn số lần retry nếu output không đạt).
- **Router rule-based có thể match sai** với câu mập mờ (vd "Top 3 câu chuyện hay nhất") — có
  cả 2 tín hiệu "top 3" và "câu chuyện" → rơi vào nhánh Hybrid dù không cần thiết. Nên review
  log classify định kỳ, tinh chỉnh keyword list.
- **Không tự động hoá hoàn toàn bước duyệt cuối** — theo nguyên tắc "propose, don't decide",
  GATE cuối trước Postiz luôn giữ lại, không auto-publish thẳng dù full-auto toàn bộ phần trước.

## Đánh giá cá nhân

- **Điểm mạnh:** giải quyết đúng vấn đề "phải tự nghĩ dùng tool nào" — giờ chỉ cần quăng topic.
  Rule-based classify nhanh, free, đủ chính xác cho phần lớn case content factory hàng ngày.
- **Điểm yếu:** nhánh Vox Director khi full-auto mất đi phần "duyệt bằng mắt" vốn là điểm mạnh
  nhất của Vox Director gốc — dễ ra sản phẩm tốn tiền mà không ưng. Hybrid branch (ghép 2 engine)
  chưa test thực tế nhiều, ffmpeg concat 2 style khác nhau (code-rendered vs AI-generated) có thể
  lộ rõ chỗ nối nếu không căn màu/font kỹ.
- **Có nên dùng không:** 7/10 — dùng tốt cho nội dung hàng ngày/số lượng lớn (Trùm Sân Bay đăng
  liên tục), nhưng video quan trọng/campaign lớn nên tắt full-auto, quay lại quy trình thủ công
  gốc của từng stack.

## Link
- `stacks/remotion-template-factory.md`
- `skills/vox-director.md`
- `repos/remotion-superpowers.md`
- Atlas Cloud API docs: atlascloud.ai/docs

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Router classify — chạy rule-based trước, fallback LLM qua OmniRoute
import urllib.request, json, re

REMOTION_KW = ["top", "so sánh", "giá", "bảng", "%", "thống kê", "vs", "bao nhiêu"]
VOX_KW = ["là gì", "tại sao", "vì sao", "cách", "câu chuyện", "hành trình", "giải thích", "vì đâu"]

def classify(topic: str) -> str:
    t = topic.lower()
    has_remotion = any(kw in t for kw in REMOTION_KW)
    has_vox = any(kw in t for kw in VOX_KW)
    if has_remotion and has_vox:
        return "hybrid"
    if has_remotion:
        return "remotion"
    if has_vox:
        return "vox"
    return llm_classify_fallback(topic)  # gọi OmniRoute route=cheap khi rule không rõ

def llm_classify_fallback(topic: str) -> str:
    # Gọi OmniRoute (DeepSeek V3, route=cheap) — code gọi theo cấu hình OmniRoute nội bộ
    req = urllib.request.Request(
        "http://<omniroute-endpoint>/v1/chat/completions",
        data=json.dumps({
            "model": "cheap",
            "messages": [{"role": "user", "content":
                f"Phân loại chủ đề video sau là 'remotion' (số liệu/so sánh) hay "
                f"'vox' (kể chuyện/giải thích). Chỉ trả về 1 từ.\n\nChủ đề: {topic}"}]
        }).encode(),
        headers={"Content-Type": "application/json"})
    result = json.loads(urllib.request.urlopen(req).read())
    return result["choices"][0]["message"]["content"].strip().lower()
```

### OpenClaw
```bash
# OpenClaw nhận topic từ Telegram, gọi Hermes classify, rồi trigger đúng pipeline
# Nếu ENGINE=remotion → gọi remotion render script (xem stacks/remotion-template-factory.md)
# Nếu ENGINE=vox       → gọi Vox Director skill (Claude Code) hoặc Atlas Cloud API trực tiếp
# Nếu ENGINE=hybrid     → chạy song song 2 nhánh, ffmpeg concat kết quả
```

### Antigravity
```bash
# Deploy router script như 1 service nhỏ trên VPS, chạy qua PM2
pm2 start router_classify.py --name video-router --interpreter python3
pm2 save
```
> ⚠️ Router mới build, chưa có track record — theo dõi log classify 2 tuần đầu để tinh
> chỉnh keyword list trước khi tin tưởng full-auto cho content quan trọng.

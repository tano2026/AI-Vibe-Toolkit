# Content Production Model — 4 lớp, rẽ nhánh theo structure_type

## Tổng quan

```
SCRIPTING (đã pass Compliance Gate)
        │
        ▼
┌───────────────────────────────────────────────┐
│  4 LỚP SẢN XUẤT — chạy song song, ghép ở cuối   │
├───────────────────┬─────────────┬───────────────┤
│  Lớp Visual        │  Lớp TTS    │  Lớp Thumbnail │
│  (b-roll/hình ảnh) │  (giọng đọc)│  (bìa video)   │
└─────────┬──────────┴──────┬──────┴────────┬───────┘
          │                 │                │
          └────────┬────────┴────────┬───────┘
                    ▼                 ▼
              LỚP VIDEO ASSEMBLY (ghép tất cả lại)
                    │
                    ▼
              video hoàn chỉnh → PLATFORM_FANOUT
```

Cả 4 lớp đều đọc `tenant_config` + `structure_type` từ script vừa qua Compliance
Gate — không hardcode 1 tool duy nhất cho mọi video.

## Lớp 1 — Nội dung (Script)

Đã thiết kế ở Script Variation Engine — không lặp lại ở đây. Chỉ nhắc: output
của lớp này không chỉ là text, mà kèm `structure_type` — giá trị này là **input
điều khiển** cho cả 3 lớp phía dưới.

## Lớp 2 — Visual (b-roll/hình ảnh) — quyết định theo structure_type

| structure_type | Nguồn visual | Vì sao |
|---|---|---|
| `intro-list-outro`, `comparison`, `tutorial` | **Stock footage** — Pexels/Pixabay qua MoneyPrinterTurbo (mặc định có sẵn) | Nội dung dạng liệt kê/so sánh không cần visual nhất quán xuyên suốt — mỗi đoạn 1 clip khác nhau là bình thường, tự nhiên. Free, nhanh, không tốn compute AI-gen |
| `narrative`, `case-study` | **AI-generate có face/scene consistency** — SceneWorks (local, có face consistency built-in) hoặc fal-mcp (cloud, nhiều model, không cần GPU local) | Kể chuyện cần nhân vật/bối cảnh nhất quán qua nhiều cảnh — stock footage random sẽ phá vỡ mạch, nhìn rời rạc. Đây đúng use case SceneWorks được build ra để giải quyết |
| Thumbnail (luôn luôn, mọi structure_type) | **Pollinations** (free, unlimited, không cần API key) — riêng biệt khỏi b-roll | Thumbnail cần bắt mắt/khác biệt, không phải cắt từ b-roll ra. Tách lớp riêng để không lệ thuộc chất lượng b-roll |

**Quy tắc quan trọng:** không dùng AI-generate visual cho toàn bộ mọi video —
chỉ dùng khi structure_type thật sự cần (narrative/case-study). Lý do kép:
(1) tiết kiệm compute — stock footage rẻ hơn nhiều lần AI-gen, (2) đa dạng nguồn
visual giữa các video (có video dùng stock, có video AI-gen) tự nhiên tạo thêm
lớp khác biệt, giảm cảm giác "mass-produce" mà Compliance Gate đang canh.

## Lớp 3 — TTS (giọng đọc) — quyết định theo tenant.brand_voice

| Tình huống | TTS provider | Vì sao |
|---|---|---|
| Mặc định, chưa cần giọng riêng | **Edge-TTS** (free, built-in MoneyPrinterTurbo) | Không cần GPU, không cần API key, đủ tự nhiên cho hầu hết video |
| Tenant muốn 1 giọng nhất quán xuyên suốt kênh (brand voice thật) | **F5-TTS** (voice clone chỉ cần 3 giây mẫu, có sẵn kho) | Kênh cần "giọng riêng" để khán giả nhận diện được — đúng tinh thần "genuine human creativity" mà policy Inauthentic Content đánh giá cao (có điểm nhận diện, không phải TTS generic ai cũng nghe giống nhau) |
| VPS yếu, cần TTS nhẹ nhất có thể | **Kokoro-82M** (300MB, chạy CPU) | Fallback khi Edge-TTS lỗi mạng hoặc cần chạy offline hoàn toàn |
| Kênh tiếng Việt (nếu mở rộng sau) | **Resona** (~17K/tháng, có lồng tiếng video) | Đã verify TTS tiếng Việt native tốt hơn Edge-TTS cho ngôn ngữ này |

**Lưu ý bám theo research trước:** dùng giọng nhất quán (F5-TTS clone) không chỉ
là chất lượng — nó là 1 tín hiệu "genuine creative fingerprint" mà YouTube dùng
để phân biệt kênh thật với kênh mass-produce (theo định nghĩa Inauthentic Content
đã research: "channel lacks a unique creative fingerprint" là dấu hiệu bị nghi ngờ).

## Lớp 4 — Video Assembly — quyết định theo structure_type

| structure_type | Engine | Vì sao |
|---|---|---|
| `intro-list-outro`, `comparison`, `tutorial` | **MoneyPrinterTurbo** (engine chính, đã ghép sẵn TTS+broll+subtitle+render) | Đúng use case gốc của tool — nội dung tuyến tính, không cần multi-scene phức tạp |
| `narrative`, `case-study` | **OpenMontage** (12 pipeline sẵn, có pipeline `faceless_shorts` + hỗ trợ style clone) hoặc **ViMax** nếu cần vai trò Director/Screenwriter rõ ràng hơn | MoneyPrinterTurbo không mạnh về kể chuyện đa cảnh có mạch — OpenMontage/ViMax được thiết kế cho đúng việc này |

**Không dùng DramaClaw ở giai đoạn MVP** — dù DramaClaw mạnh nhất về visual
consistency (Director World/3GS giữ spatial structure), nó là pipeline nặng
(phân tích manuscript, storyboard, nhiều bước) — phù hợp hơn cho phase sau khi
cần chất lượng cao hơn, không phải MVP đang cần chạy nhanh/ổn định trước.

## Bảng quyết định tổng hợp — 1 nhìn là đủ

| structure_type | Visual | TTS | Assembly engine |
|---|---|---|---|
| intro-list-outro | Stock (Pexels/Pixabay) | Edge-TTS / F5-TTS nếu có brand voice | MoneyPrinterTurbo |
| comparison | Stock (Pexels/Pixabay) | Edge-TTS / F5-TTS | MoneyPrinterTurbo |
| tutorial | Stock (Pexels/Pixabay) | Edge-TTS / F5-TTS | MoneyPrinterTurbo |
| narrative | AI-gen (SceneWorks/fal-mcp) | F5-TTS (khuyến nghị, cần giọng kể chuyện nhất quán) | OpenMontage / ViMax |
| case-study | AI-gen (SceneWorks/fal-mcp) | F5-TTS | OpenMontage / ViMax |
| Thumbnail (mọi loại) | Pollinations (free, riêng biệt) | — | — |

## Cost/compute note — theo số liệu đã verify

- MoneyPrinterTurbo path: 4-8 core, 4-8GB RAM, không GPU — nhẹ, chạy tốt trên VPS hiện tại.
- OpenMontage/ViMax path (narrative): nặng hơn — cần AI-gen visual (SceneWorks
  cần GPU local, hoặc fal-mcp cloud tính phí theo request) — **chưa deploy nhánh
  này ở MVP**, chỉ dùng MoneyPrinterTurbo path trước cho tới khi engine chính
  chạy ổn định 4-6 tuần (đúng nguyên tắc trong SAAS-BLUEPRINT.md — không nhảy cóc).

## Việc cần làm thêm (chưa có, ghi nhận để làm sau)

- Chưa viết code routing thật (if structure_type == X → gọi engine Y) — đây là
  phần thuộc CORE-BRAIN.md, cần thêm 1 bảng dispatch trong RENDERING state.
- Nhánh narrative/case-study (OpenMontage/ViMax) chưa test trên VPS thật — để
  giai đoạn 2 sau khi nhánh chính ổn định.

# Seedance 2.5 — GitHub Repo / AI Video Model

## TL;DR
Model tạo video AI mới nhất của ByteDance (công ty mẹ TikTok) — ra mắt 23/6/2026 tại Volcano Engine FORCE Conference. Tạo clip 30 giây native 4K trong một lần generate, nhận 50 reference inputs cùng lúc. Hiện enterprise beta, public launch đầu tháng 7/2026. Seedance 2.0 đang #1 trên Artificial Analysis Video Arena — vượt Google Veo 3.1 và Kling 3.0.

## Tool này dùng để làm gì
ByteDance giải quyết 3 vấn đề lớn nhất của AI video hiện tại:

**1. Clip quá ngắn (solved):**
Các model khác (Runway, Veo, Kling) tối đa 8-15 giây trước khi phải stitch. Seedance 2.5 generate native 30 giây một lần — không seam, không drift nhân vật giữa các đoạn.

**2. Thiếu kiểm soát (solved):**
Nhận 50 multimodal reference inputs cùng lúc: ảnh, audio, video clip, 3D white model, style guide. Seedance 2.0 chỉ nhận được 12. Với 50 references, brand team có thể feed toàn bộ style guide + character sheet + color palette → AI giữ đúng brand xuyên suốt clip.

**3. Phải re-generate toàn bộ khi sửa một chi tiết (solved):**
Local re-draw editing: chỉnh một vùng trong frame mà không ảnh sinh phần còn lại. Sửa logo sai, đổi màu áo nhân vật, remove object — không cần render lại từ đầu.

**Bonus:** Audio được co-process trong cùng latent space với video → sync âm thanh/hình ảnh native, không cần ghép ngoài.

## Specs kỹ thuật
| Feature | Seedance 2.0 | Seedance 2.5 |
|---------|-------------|-------------|
| Clip length | 15 giây | **30 giây native** |
| Resolution | 1080p | **4K native (10-bit color)** |
| Reference inputs | 12 | **50 multimodal** |
| Prompt adherence | baseline | **+20% tốt hơn** |
| Audio | separate sync | **Co-processed native** |
| Local editing | ❌ | **✅ Regional re-draw** |

## Cách access (tháng 7/2026)
```
Enterprise beta: Volcano Engine (B2B) — đã live
Public launch: đầu tháng 7/2026

Kênh access dự kiến:
1. Dreamina / Jimeng — app sáng tạo của ByteDance (quốc tế / Trung Quốc)
2. CapCut — tích hợp vài tuần sau public launch
3. Doubao — AI assistant của ByteDance
4. Third-party API — fal.ai, ImagineArt (như Seedance 2.0 đã có)
5. Volcano Engine API — cho enterprise
```

**Giá ước tính:** Seedance 2.0 trên fal.ai ~$2.50/clip 15 giây. 2.5 chưa có pricing chính thức.

## So sánh với đối thủ

| Model | Clip length | Resolution | References | Status |
|-------|-------------|------------|------------|--------|
| **Seedance 2.5** | **30s** | **4K native** | **50** | Beta |
| Google Veo 3.1 | ~15s | 4K | 3 | Live |
| Kling 3.0 | ~10s | 1080p | 5 | Live |
| Runway Gen-4.5 | ~8s | 1080p | 3 | Live |
| OpenAI Sora 2 | ~15s | 1080p | 2 | **Đã đóng cửa 26/4/2026** |

Seedance 2.0 đang #1 Artificial Analysis Video Arena. 2.5 chưa có independent benchmark.

## Ví dụ thực tế (dựa trên specs)

**Content creator TikTok/YouTube:**
- Feed 10 ảnh sản phẩm + 5 style reference + brand color guide → 30 giây video giới thiệu sản phẩm nhất quán brand
- Không cần CapCut ghép nhiều clip ngắn

**Travel brand (ABTRIP use case):**
- Feed ảnh địa điểm + footage cũ + mood board → generate clip 30s quảng cáo tour native 4K
- Local re-draw: đổi text overlay mà không re-generate toàn clip

**Faceless video content:**
- 30 giây = đủ cho 1 TikTok hoàn chỉnh trong một lần generate
- Kết hợp Resona TTS + Seedance 2.5 → video có cả hình lẫn tiếng native

## Lưu ý / Rủi ro cần biết
- **Chưa public** — enterprise beta, public July 2026. Tất cả specs là vendor claims, chưa có independent benchmark
- **Copyright drama:** Seedance 2.0 bị Disney, Warner, Netflix, Paramount gửi cease-and-desist tháng 2/2026 vì generate được deepfake celebrity. 2.5 đã thêm content filter nhưng vấn đề pháp lý chưa resolve
- **US market unclear:** ByteDance chưa confirm timeline cho US. Dùng qua third-party API (fal.ai) thì được
- **Giá chưa rõ** — chờ public launch mới có pricing

## Đánh giá cá nhân
- Điểm mạnh: Specs vượt trội so với mọi đối thủ hiện tại; ByteDance có lợi thế training data từ TikTok (biết video nào viral); 50 references là game-changer cho brand content
- Điểm yếu: Chưa live public; copyright risk còn đó; ByteDance = chính trị với US market; chưa có independent benchmark
- Có nên dùng không: **8.5/10** — Theo dõi chặt, access ngay khi public launch tháng 7. Nếu specs giữ đúng như công bố, đây là model AI video tốt nhất thị trường cho content creator. Dùng qua CapCut hoặc fal.ai để tránh rủi ro pháp lý trực tiếp.

## Link
- Announcement: Volcano Engine FORCE Conference 23/6/2026
- Access (dự kiến): dreamina.capcut.com, fal.ai/models/seedance
- Seedance 2.0 hiện tại: fal.ai/models/fal-ai/seedance (đã live)
- So sánh: Artificial Analysis Video Arena

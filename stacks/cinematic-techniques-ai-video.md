---
name: cinematic-techniques-ai-video
description: >
  Use case: làm clip/ảnh AI "có đạo diễn" — so sánh 3 skill ngôn ngữ điện ảnh
  (fal cinematography, muapi-cinema-director, higgsfield-camera) và chọn cái dùng
  được ngay. Công thức thuần đã gói trong designer-pro/cinematic-shot-prompt-core.
---

# Cinematic Techniques cho AI Video — 3 nguồn, chọn cái nào

## TL;DR
Có 3 skill cùng chủ đề "ngôn ngữ điện ảnh cho prompt AI". **Khuyến nghị: không cài cả 3.** Dùng phần kiến thức (text thuần) qua `agents/designer-pro/skills/cinematic-shot-prompt-core/SKILL.md`, và chỉ cài `higgsfield-camera` nếu thật sự dùng Higgsfield. Cái cần tool/dịch vụ ngoài (fal, muapi) để sau.
Nguồn: trang tổng hợp claudeskills.info (số sao lấy ở đó, chưa đọc tận repo). Chưa cài thử cái nào.

## 3 skill có gì

### 1. `fal-ai-community/skills` → `cinematography` (249 sao, cập nhật 13/05/2026)
- Dạy cấu trúc prompt **SCLCAM** (Subject, Context, Lens/framing, Camera motion, Atmosphere, Mood/color) + cỡ cảnh, góc máy, tiêu cự, độ sâu trường, bố trí ánh sáng, chấm màu
- Gắn với `genmedia` CLI của fal để chọn model, tải asset, tạo video bất đồng bộ (GPT-Image-2, Flux, Nano-Banana, Seedance 2.0, Grok-Imagine-Video)
- Cài: `npx skills add fal-ai-community/skills --skill cinematography --agent claude-code`
- License: không thấy ghi trong nguồn đã đọc
- Dùng được không: phần kiến thức thì có. Phần chạy tool cần fal (tài khoản/credit), cần Claude Code → hiện chưa chạy được

### 2. `samuraigpt/generative-media-skills` → `muapi-cinema-director` (5.477 sao, cập nhật 24/07/2026, MIT)
- Biến ý tưởng thành chỉ dẫn quay (khung hình, chuyển động, ánh sáng, ống kính, fps, tỉ lệ) rồi gọi `generate-film.sh` với "Director's Intent", nhận `request_id` để hỏi lại kết quả
- Hỗ trợ Veo3, Kling, Luma — **qua nền tảng muapi.ai**
- Dùng được không: phụ thuộc muapi.ai (chưa rõ giá/key, tài liệu không nói rõ). Rủi ro: lệ thuộc 1 dịch vụ trung gian. Chưa nên

### 3. `OSideMedia/higgsfield-ai-prompt-skill` → `higgsfield-camera` (694 sao, cập nhật 26/07/2026, MIT)
- Danh mục chuyển động máy theo TÊN PRESET của Higgsfield: dolly, crane, orbit/arc, crash zoom, FPV drone, handheld, snorricam, bullet time, dutch angle, whip pan, hyperlapse, through-object, car chase...; cỡ cảnh từ extreme long đến extreme close-up; góc máy; gợi ý ăn khớp cảm xúc, quy tắc kết hợp, mẹo Cinema Studio 3.0
- Dùng được không: **có, dễ nhất** — là kiến thức viết prompt, không cần chạy server. Hợp khi dùng Higgsfield (kho đã có `mcps/higgsfield.md`)

## Bảng chọn nhanh
| | Cần cài tool? | Cần dịch vụ trả phí? | Dùng ngay được? |
|---|---|---|---|
| fal cinematography | Có (genmedia + Claude Code) | Có (fal) | Chỉ phần kiến thức |
| muapi-cinema-director | Có (script + muapi) | Có/không rõ | Chưa |
| higgsfield-camera | Không | Chỉ khi tạo clip trên Higgsfield | **Có** |
| `cinematic-shot-prompt-core` (kho) | Không | Không | **Có** |

## Dùng thế nào ngay hôm nay (không cần máy tính)
1. Mở `cinematic-shot-prompt-core`, viết 1 prompt 6 phần cho 1 cảnh Fast Track
2. Dán vào generator mày đang có (Higgsfield web/Veo/Kling)
3. Làm bài PASS/FAIL ở cuối skill (3 cặp so sánh)

## Đánh giá cá nhân
- Cả 3 là kiến thức giống nhau ở lõi (shot size/angle/motion/light/color) — khác chỗ gắn công cụ. Giá trị thật nằm ở thói quen "1 shot = 1 chuyển động, nguồn sáng cụ thể", không nằm ở việc cài thêm tool
- Rủi ro: nội dung lấy từ trang tổng hợp; chi tiết repo gốc chưa đọc; chưa kiểm chứng chất lượng clip
- Có nên dùng: công thức thuần 7/10 (rẻ, thử được ngay); cài cả 3: không

## Link
- https://github.com/fal-ai-community/skills (skills/cinematography)
- https://github.com/samuraigpt/generative-media-skills
- https://github.com/OSideMedia/higgsfield-ai-prompt-skill
- Liên quan trong kho: `agents/designer-pro/skills/cinematic-shot-prompt-core/SKILL.md`, `mcps/higgsfield.md`, `repos/higgsfield-mcp-unified.md`, `agents/company/skills/ffmpeg-media-toolkit/SKILL.md`

# Open-Source Text/Image-to-Video Models 2026 (Open-Sora · Wan-Video · FramePack · HunyuanVideo · LTX-Video) — GitHub Repo

## TL;DR
5 model mã nguồn mở sinh video từ text/ảnh — đều mạnh, đều cần GPU nặng để chạy local. Không hợp chạy trên VPS Tencent Cloud hay máy Windows local hiện có (không có GPU rời đủ mạnh) — thực tế nên dùng qua **cloud API** (DashScope, SiliconFlow, Replicate) thay vì tự host.

## 5 model này khác nhau ở đâu

| Model | Org | Stars | VRAM tối thiểu | Điểm mạnh riêng |
|---|---|---|---|---|
| **LTX-Video (LTX-2)** | Lightricks | — | **12GB** (thấp nhất, chạy được card phổ thông) | Nhanh gấp 3-4 lần Wan/Hunyuan, có audio+video đồng bộ trong 1 model, 18M+ lượt tải HuggingFace |
| **FramePack** | lllyasviel | 17.1K | **6GB** (chạy được laptop GPU) | Ra video tới 120 giây, feedback trực quan từng frame ngay khi đang sinh |
| **HunyuanVideo-1.5** | Tencent | — | ~14GB (bản 1.5 nhẹ) / 24-80GB (bản gốc 13B) | Màu sắc/bokeh đẹp nhất trong nhóm, nhưng chậm nhất |
| **Wan2.1/2.2** | Alibaba | 15K+/repo | 8-24GB tuỳ bản | Có sẵn cloud API chính chủ (DashScope) rẻ, hỗ trợ tiếng Việt/Trung trong video text rendering |
| **Open-Sora** | hpcaitech | 29.2K | Cao (model 11B) | Sao nhiều nhất, benchmark VBench gần sát Sora của OpenAI |

## Repo này dùng để làm gì
Tất cả 5 model đều nhận text prompt hoặc ảnh đầu vào, sinh ra video ngắn (thường 2-10s, FramePack tới 120s). Đây là lớp "raw model" — cần code Python + PyTorch + GPU để chạy, khác hẳn công cụ có UI sẵn như html-video hay Short Video Factory đã có trong kho.

## Setup từng bước (tổng quát, khác nhau tuỳ model)
1. **Với VPS/máy hiện có (không GPU rời mạnh):** KHÔNG tự host — dùng cloud API thay thế:
   - Wan: DashScope (Alibaba Cloud) $0.10-0.15/clip 5s 720p, hoặc SiliconFlow $0.12-0.29/clip
   - LTX-Video/HunyuanVideo/Open-Sora: thuê GPU cloud theo giờ (RunPod, Massed Compute) nếu cần chạy trực tiếp — tốn thêm chi phí hạ tầng, cân nhắc kỹ trước khi chọn hướng này
2. **Nếu sau này đầu tư máy có GPU rời (RTX 4090 trở lên):** clone repo tương ứng, cài theo README (mỗi model 1 quy trình riêng, đều cần conda env + PyTorch + tải model weight vài chục GB).
3. Với LTX-Video, có sẵn workflow ComfyUI chính thức — dễ setup hơn code thuần Python.

## Ví dụ thực tế
Cần B-roll ngắn cho content "Airfare Decoded" (vd cảnh máy bay cất cánh mô phỏng) mà không có footage thật — thay vì thuê GPU cloud để tự chạy Open-Sora/Wan, dùng thẳng API Wan qua DashScope trả theo clip ($0.10-0.15/clip), rẻ hơn nhiều so với đầu tư hạ tầng GPU chỉ để dùng thỉnh thoảng.

## Lưu ý / Lỗi thường gặp
- **Rào cản lớn nhất: phần cứng.** VPS Tencent Cloud hiện tại và máy Windows local (4 core, ~15.7GB RAM, không ghi nhận GPU rời) đều KHÔNG đủ chạy bất kỳ model nào trong 5 cái này ở tốc độ chấp nhận được — đây không phải "cài là chạy" như các tool khác trong kho.
- License khác nhau: Wan2.1/2.2 Apache 2.0 (tự do thương mại), LTX-2 theo "LTX-2 Community License" (đọc kỹ điều khoản), Open-Sora/HunyuanVideo cũng cần kiểm tra license cụ thể từng bản trước khi dùng thương mại.
- Có nhiều trang giả mạo tên các model này (đặc biệt FramePack có cảnh báo chính thức về domain giả framepack.co/.net/.ai...) — chỉ tải từ GitHub/HuggingFace chính chủ.
- Video sinh ra từ các model này (2-10s clip thô) vẫn cần hậu kỳ (cắt ghép, thêm nhạc/phụ đề) qua html-video/HyperFrames/Short Video Factory đã có trong kho — không phải sản phẩm cuối ngay.

## Đánh giá cá nhân
- Điểm mạnh: chất lượng video AI-gen mã nguồn mở đã bắt kịp gần các model đóng (Sora, Runway) theo benchmark VBench; có option cloud API rẻ (Wan qua DashScope) không cần tự host.
- Điểm yếu: rào cản phần cứng thật sự lớn với setup hiện tại của Tano Agency — nếu không đầu tư GPU hoặc dùng cloud API trả phí, 5 model này gần như không dùng được.
- Có nên dùng không: 6/10 xét trên hạ tầng hiện tại (chỉ khả thi qua cloud API trả phí, không tự host được) — sẽ lên 8-9/10 nếu sau này đầu tư máy có GPU rời mạnh.

## Link
- Open-Sora: https://github.com/hpcaitech/Open-Sora
- Wan-Video: https://github.com/Wan-Video/Wan2.1 · https://github.com/Wan-Video/Wan2.2
- FramePack: https://github.com/lllyasviel/FramePack
- HunyuanVideo: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
- LTX-Video: https://github.com/Lightricks/LTX-Video

# Awesome GPT Image 2 (YouMind-OpenLab) — GitHub Repo

## TL;DR
Kho prompt lớn nhất cho GPT Image 2 (model ảnh thế hệ mới của OpenAI) — 2000+ prompt được tuyển chọn, có ảnh preview, cập nhật hàng ngày, hỗ trợ 16 ngôn ngữ. Free và open source hoàn toàn.

## Repo này dùng để làm gì
Đây là thư viện prompt tham khảo cho GPT Image 2 — model ảnh của OpenAI mạnh về render chữ chính xác (pixel-perfect text), giữ nhất quán nhân vật/đối tượng qua nhiều ảnh (cross-image consistency), và chất lượng minh hoạ thương mại. Repo phân loại prompt theo category (Poster, Portrait, UI/UX, Architecture...), mỗi prompt kèm ảnh preview để biết trước output trông ra sao trước khi chạy.

Không phải công cụ chạy code — đây thuần là "sách công thức" giúp viết prompt hiệu quả hơn thay vì mò mẫm, đặc biệt hữu ích khi cần render text trong ảnh (banner, poster, thumbnail có chữ) — điểm yếu truyền thống của các model ảnh AI trước đây.

## Setup từng bước

1. Clone hoặc browse trực tiếp repo trên GitHub: `github.com/YouMind-OpenLab/awesome-gpt-image-2`
2. Chọn category phù hợp nhu cầu (VD: Poster cho thumbnail YouTube, Portrait cho ảnh đại diện)
3. Copy prompt mẫu, chỉnh sửa chi tiết theo brand/nội dung cụ thể
4. Chạy prompt qua GPT Image 2 API (OpenAI) hoặc qua các platform trung gian như hiapi, APIMart (nếu không có API key OpenAI trực tiếp)
5. Nếu cần bản tiếng Trung: đọc `README_zh.md` trong repo

## Ví dụ thực tế

Tình huống: cần tạo thumbnail cho video "Trùm Sân Bay" trên TikTok, cần chữ tiếng Việt rõ nét trên ảnh sân bay Nội Bài.

- Vào category Poster/Thumbnail trong repo
- Chọn prompt mẫu có text rendering tốt (đặc trưng GPT Image 2)
- Sửa lại: bối cảnh sân bay, chữ tiếng Việt "FAST TRACK NỘI BÀI", màu brand ABTRIP
- Chạy qua GPT Image 2 API → nhận ảnh có chữ tiếng Việt chuẩn, không bị lỗi font như nhiều model ảnh khác

## Lưu ý / Lỗi thường gặp

- Có rất nhiều repo trùng tên "awesome-gpt-image-2" trên GitHub từ nhiều owner khác nhau (freestylefly, Anil-matcha, bubblesslayyer-cmd, gpt-image2...) — nội dung không giống hệt nhau. Repo này chọn **YouMind-OpenLab** vì có số lượng prompt lớn nhất, đa ngôn ngữ, và cập nhật đều đặn (daily).
- Prompt thu thập từ cộng đồng, repo tự ghi rõ "chỉ dùng cho mục đích giáo dục" — nếu phát hiện nội dung vi phạm bản quyền, họ gỡ khi có report qua issue.
- Cần có quyền truy cập GPT Image 2 API (qua OpenAI trực tiếp hoặc platform trung gian) — repo chỉ cho prompt, không cho quyền truy cập model.
- Repo liên kết chéo với `awesome-seedance-2-prompts` (biến ảnh GPT Image 2 thành video AI) — nếu cần làm content video từ ảnh tĩnh, xem thêm repo đó.

## Đánh giá cá nhân

- **Điểm mạnh:** Số lượng prompt lớn, có preview ảnh thật (không phải mô tả suông), đa ngôn ngữ bao gồm tiếng Việt — tiết kiệm thời gian mò mẫm prompt so với tự viết từ đầu.
- **Điểm yếu:** Chất lượng prompt phụ thuộc cộng đồng đóng góp, không có curation chuyên sâu bởi 1 team cố định — độ đồng đều có thể không cao. Cần trả phí cho GPT Image 2 API riêng, repo không miễn phí hoá chi phí chạy model.
- **Có nên dùng không:** 7/10 — Hữu ích cho content factory cần render text trên ảnh (thumbnail, poster, banner brand) nhưng chỉ là điểm khởi đầu, vẫn cần tự tinh chỉnh prompt cho khớp brand voice.

## Link
- Repo: https://github.com/YouMind-OpenLab/awesome-gpt-image-2
- README tiếng Trung: https://github.com/YouMind-OpenLab/awesome-gpt-image-2/blob/main/README_zh.md
- Repo liên quan (ảnh → video): https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

def generate_gpt_image_2(prompt: str, api_key: str, api_base: str = "https://api.openai.com/v1"):
    """Gọi GPT Image 2 API để tạo ảnh từ prompt (lấy mẫu từ kho awesome-gpt-image-2)."""
    payload = json.dumps({
        "model": "gpt-image-2",
        "prompt": prompt,
        "size": "1024x1024"
    }).encode()
    req = urllib.request.Request(
        f"{api_base}/images/generations",
        data=payload,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST"
    )
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
# Không cần cài đặt gì thêm — chỉ là kho prompt tham khảo
# Có thể clone về local để tra cứu nhanh khi viết content
git clone https://github.com/YouMind-OpenLab/awesome-gpt-image-2.git
```

### Antigravity
```bash
# Không cần deploy — đây là tài liệu tĩnh, không phải service
```
> ⚠️ Repo chỉ cung cấp prompt, không cung cấp quyền truy cập GPT Image 2 — cần tự có API key OpenAI hoặc dùng platform trung gian (hiapi, APIMart) nếu muốn tiết kiệm chi phí batch lớn.

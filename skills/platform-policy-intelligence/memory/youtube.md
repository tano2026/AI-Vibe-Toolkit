# Ghi nhớ chính sách & thuật toán — YouTube (bao gồm Shorts)

Append-only. Entry mới nhất ở TRÊN CÙNG. Không xoá/sửa entry cũ, chỉ thêm đính chính có ngày.

---

## 2026-08-06 — Cập nhật khởi điểm (từ research thật, có nguồn)

### Tín hiệu phân phối
- **Satisfaction đã thay watch time làm tín hiệu chính** — video ngắn hơn nhưng satisfaction
  cao thắng video dài lê thê. Không còn đúng công thức cũ "video càng dài càng tốt".
- **Session contribution** — thuật toán đánh giá video trong bối cảnh CẢ PHIÊN xem, không
  chỉ riêng lẻ 1 video. Series/playlist giữ người xem qua nhiều video được thưởng.
- **3 nhóm tín hiệu chính**: engagement (CTR + watch time), satisfaction (like/share/khảo
  sát), relevance (từ khóa/chủ đề khớp).
- **Shorts search filter mới** (2026) — người dùng lọc riêng kết quả Shorts, SEO cho
  short-form giờ mới thật sự có ý nghĩa (trước đây gần như không).
- Traffic từ "suggested videos" cao = tín hiệu retention/satisfaction đang tốt → nên đầu
  tư series/playlist thay vì video đơn lẻ rời rạc.

### Quy định AI-content disclosure
- Bắt buộc từ 3/2024, **nhưng từ 5/2026 có thêm auto-detection** — YouTube tự nhận diện
  AI-content photorealistic và tự gắn label nếu creator quên, không chỉ dựa vào tự khai.
- **Vị trí label đổi mới (5/2026)**: video dài → label ngay dưới player, phía trên mô tả
  (nổi bật hơn trước). Shorts → label overlay TRỰC TIẾP TRÊN VIDEO, không phải trong mô tả.
- Nội dung hoạt hình/chỉnh sửa nhẹ vẫn ghi trong phần mô tả mở rộng, không cần overlay nổi bật.
- **AI-assisted KHÔNG cần disclosure**: viết script, tạo thumbnail, chỉnh caption bằng AI —
  đây là "productivity tool", không phải "content generator".
- Không disclosure mà bị hệ thống phát hiện → giảm đề xuất, mất monetize, hoặc gỡ video —
  hậu quả nặng hơn TikTok (TikTok vẫn cho monetize nếu label đúng).

### Originality — "AI slop crackdown" (QUAN TRỌNG NHẤT)
- **16 kênh lớn, 35 triệu subscriber, 4.7 tỷ view bị xóa** trong 1 đợt crackdown nội dung
  AI hàng loạt không có định hướng con người thật ("inauthentic content").
- **21% đề xuất Shorts từng là "AI slop"** trước đợt crackdown — nghĩa là sau khi dọn, có
  nhiều chỗ trống hơn cho creator làm đúng cách.
- Ranh giới an toàn: **"creators using AI with genuine human direction and proper
  disclosure report no adverse action"** — có định hướng biên tập con người thật + disclosure
  đúng thì KHÔNG bị ảnh hưởng, dù dùng AI nhiều.
- Yêu cầu cụ thể: giọng nói, góc nhìn, phán đoán biên tập của người thật phải hiện diện
  trong sản phẩm cuối — không phải chỉ AI tự chạy 100% không ai kiểm.

### Yêu cầu định dạng
- Shorts: 9:16, dưới 3 phút (đã nới từ giới hạn cũ).
- Long-form: tối ưu theo satisfaction, không có độ dài "chuẩn" cố định — video ngắn có
  payoff mạnh thắng video dài lan man.

### Nguồn
dataslayer.ai, vidiq.com, socialpilot.co, techwyse.com, subsub.io, hollywoodreporter.com,
outlierkit.com, ytzolo.com — nhiều nguồn phân tích + xác nhận trực tiếp từ YouTube
(Ritchie, phát ngôn viên chính sách, được trích trong Hollywood Reporter).

### Áp dụng cho Trùm Sân Bay / shorts-affiliate-system
- **Đây là bằng chứng thực tế xác nhận nguyên tắc `compliance-gate` đã viết trước đó**
  (case "16 kênh/35M sub" đã được dùng làm ví dụ cảnh báo trong skill compliance-gate của
  yt-cashcow) — không phải giả định, là sự việc đã xảy ra thật, tăng độ ưu tiên tuân thủ.
- Trùm Sân Bay AN TOÀN theo tiêu chí "human direction" vì: có brand voice cụ thể (nhân
  vật "15 năm kinh nghiệm"), Nobitano review 100% trước publish, guardrail chống bịa số
  liệu trong Writer prompt — đúng mô hình "AI + định hướng người thật" mà YouTube xác nhận
  an toàn.
- shorts-affiliate-system CẦN đảm bảo bước review người (đã có trong deploy-checklist)
  không bị bỏ qua khi scale — đây chính là ranh giới giữa "an toàn" và "AI slop".

# Ghi nhớ chính sách & thuật toán — Meta (Facebook/Instagram)

Append-only. Entry mới nhất ở TRÊN CÙNG. Không xoá/sửa entry cũ, chỉ thêm đính chính có ngày.

---

## 2026-08-06 — Cập nhật khởi điểm (từ research thật, có nguồn)

### Tín hiệu phân phối
- **Instagram**: 3 tín hiệu chính do Adam Mosseri (Head of Instagram) xác nhận công khai —
  watch time, sends-per-reach (chia sẻ qua DM), likes-per-reach. Mỗi bề mặt (Feed/Reels/
  Stories/Explore) có hệ thống xếp hạng RIÊNG, không dùng chung 1 thuật toán.
- Explore không "hack" được trực tiếp — luồng chuẩn: engagement tốt từ follower → test nhỏ
  trên Explore → mở rộng nếu test thành công (giống follower-first của TikTok).
- Reels dài tới 3 phút giờ tiếp cận được cả non-follower qua đề xuất (trước đây Reels dài
  khó lên đề xuất ngoài follower).

### QUY ĐỊNH ORIGINALITY — khác biệt lớn nhất so với TikTok/YouTube (RẤT QUAN TRỌNG)

**Đây là chính sách ảnh hưởng trực tiếp và nghiêm trọng nhất tới mô hình đang dùng ở
`trum-san-bay` (1 caption → Adapter co giãn ra cả Facebook lẫn Instagram).**

- **Original content được 40-60% distribution nhiều hơn nội dung repost.**
- **Ngưỡng cứng: 10+ repost trong 30 ngày → bị loại HOÀN TOÀN khỏi mọi đề xuất** (Explore,
  Reels tab, Suggested Posts) — không phải giảm nhẹ, là loại hẳn.
- Instagram dùng AI phát hiện repost **kể cả bản đã chỉnh sửa nhẹ, kể cả có watermark từ
  nền tảng khác** (vd watermark TikTok còn dính trên video) — không thể qua mặt bằng crop/
  filter/logo overlay đơn giản.
- **Facebook (từ 14/1/2026)**: nội dung "chỉ thêm border/caption/tốc độ/logo overlay" bị
  coi là KHÔNG đủ gốc, bị hạ thứ hạng Feed/Reels. Voiceover đơn thuần đè lên clip người
  khác KHÔNG đạt chuẩn "original" — cần hiện diện đáng kể trên màn hình (mặt/giọng) +
  phân tích thật sự mới, không chỉ tường thuật lại.
- Tài khoản đăng nội dung không gốc liên tục có thể bị **demonetize**.

### Quy định AI-content disclosure
- **"Made with AI" label bắt buộc** cho nội dung ảnh/video/audio photorealistic.
- Cơ chế đọc metadata: Meta chủ yếu đọc **IPTC Digital Source Type** (không hoàn toàn giống
  C2PA mà TikTok/YouTube dùng) → 1 file có thể được label đúng trên nền tảng này nhưng KHÔNG
  được nhận diện đúng trên nền tảng khác do sự khác biệt kỹ thuật giữa 2 chuẩn.
- Ads: label tự động 100% nếu dùng tool AI ngay trong Ads Manager (Background Generation,
  Image Generation...). Vi phạm lặp lại (2 lần trong 90 ngày) → khóa tài khoản 24h, lần 3
  có thể bị suspend.
- Instagram đang test nhãn **"AI Creator"** cấp tài khoản (khác "AI info" cấp nội dung) —
  xác nhận KHÔNG ảnh hưởng phân phối, chỉ là minh bạch, còn đang thử nghiệm.

### Yêu cầu định dạng
- Reels: 9:16, giờ chấp nhận tới 3 phút cho đề xuất non-follower.
- Feed/Stories: yêu cầu riêng theo từng bề mặt, chưa đào sâu — cần research thêm nếu content
  nhắm cụ thể Stories.

### Nguồn
mediapost.com, easternherald.com, socialpilot.co, coinis.com, auditsocials.com,
creatorflow.so — trích dẫn trực tiếp Meta Business Help Center, Meta Transparency Center,
và phát ngôn công khai của Adam Mosseri.

### Áp dụng cho Trùm Sân Bay — CẢNH BÁO CẦN HÀNH ĐỘNG

Mô hình hiện tại của `orchestrator.py` (Writer ra caption riêng cho FB/IG/TikTok/Shorts,
nhưng dùng CHUNG 1 asset ảnh/video từ Visual Agent) có rủi ro thật với chính sách Meta 2026:
- Nếu Facebook và Instagram nhận cùng 1 asset gần như y hệt (chỉ đổi caption) → có thể bị
  tính là thiếu "meaningful new value" giữa 2 bề mặt, dù đây là 2 platform khác nhau của
  cùng Meta (chưa rõ Meta có coi cross-post NỘI BỘ Facebook↔Instagram là repost hay không —
  cần theo dõi thêm, đây là điểm CHƯA CHẮC CHẮN, không phải kết luận).
- **Đề xuất cụ thể cho Adapter step**: với asset ảnh tĩnh, thêm biến thể nhẹ giữa bản FB và
  IG (crop khác, overlay text khác vị trí) thay vì dùng nguyên 1 file; với video, cân nhắc
  trim độ dài hoặc đổi thứ tự đoạn giữa 2 bản thay vì upload y hệt.
- Việc này CHƯA được code vào `orchestrator.py` — mới dừng ở mức phát hiện qua research,
  cần Nobitano xác nhận độ ưu tiên trước khi sửa Adapter logic.

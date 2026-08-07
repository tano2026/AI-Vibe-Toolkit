# Ghi nhớ chính sách & thuật toán — TikTok

Append-only. Entry mới nhất ở TRÊN CÙNG. Không xoá/sửa entry cũ, chỉ thêm đính chính có ngày.

---

## 2026-08-06 — Cập nhật khởi điểm (từ research thật, có nguồn)

### Tín hiệu phân phối (For You Page)
- **Follower-first testing** (từ cuối 2025): video mới được đưa cho 1 nhóm nhỏ chủ yếu là
  follower hiện tại xem trước — họ engage tốt mới được đẩy rộng hơn. Followers cũ engage
  kém = video "chết" ngay từ vòng test.
- **Completion rate / rewatch rate** là 2 tín hiệu nặng nhất, ngưỡng khỏe mạnh ~70%+ (tăng
  từ ~50% năm 2024). Video dưới 30% APV hiếm khi thoát khỏi vòng phân phối ban đầu.
- **3-5 giây đầu quyết định** — nếu audience rời trong 3s đầu, phần còn lại của watch time
  gần như không cứu được thứ hạng.
- **Comment chất lượng > số lượng like** — comment dài, có nội dung thật được tính nặng hơn
  emoji/like đơn thuần. Tỷ trọng like/comment đã đảo ngược so với các năm trước.
- **Auto-transcript feeds vào cả search lẫn FYP relevance** — nghĩa là nội dung nói trong
  voiceover cũng ảnh hưởng phân phối, không chỉ caption/hashtag viết tay.
- **Tín hiệu thương mại** (TikTok Shop link taps, saves) ảnh hưởng phân phối nhiều hơn hẳn
  so với trước — quan trọng cho content có affiliate/CTA mua hàng.
- Follower count KHÔNG phải yếu tố xếp hạng trực tiếp — kênh mới vẫn có thể outreach kênh
  lớn nếu nội dung đúng tín hiệu.

### Quy định AI-content disclosure
- **Bắt buộc label hiển thị** khi nội dung AI-generated/AI-altered mô tả người/cảnh trông
  như thật (mà người xem có thể nhầm là thật). Text-only AI (viết script, hashtag) KHÔNG
  cần disclosure.
- TikTok dùng **C2PA Content Credentials** để tự động phát hiện + gắn nhãn ngay cả khi
  creator không tự khai báo — không tự khai thì hệ thống vẫn có thể phát hiện.
- Nội dung đã label đúng cách **vẫn được monetize bình thường** qua Creator Fund/brand
  deal — disclosure là yêu cầu minh bạch, không phải hình phạt giảm reach.
- Deepfake người thật không disclosure = cấm hoàn toàn. Nội dung tổng hợp người thường
  (không phải người nổi tiếng) cũng bị cấm nếu không disclosure.
- Có hệ thống phạt 4 cấp (warning → permanent ban) cho vi phạm lặp lại.

### Originality/cross-post
- Chưa tìm thấy chính sách phạt cross-post rõ ràng như Meta (xem file meta.md) — TikTok
  hiện tập trung vào AI-disclosure hơn là originality-vs-repost.

### Yêu cầu định dạng
- Video dưới 15s có completion rate tự nhiên cao hơn, nhưng video dài hơn vẫn được thưởng
  nếu giữ chân người xem tốt (watch time tuyệt đối vẫn có giá trị).
- 9:16 là chuẩn.

### Nguồn
stackinfluence.com, socialync.io, webtonic.io, voqusa.com, storrito.com, cinerads.com,
auditsocials.com — tổng hợp nhiều nguồn phân tích uy tín, không phải 1 nguồn duy nhất
(TikTok không công bố công thức đầy đủ, đây là suy luận tốt nhất từ dữ liệu quan sát được).

### Áp dụng cho Trùm Sân Bay
- Hook 3-5s đầu phải test kỹ — đây là khoảng khớp đúng với `WRITER_SYSTEM_PROMPT` hiện tại
  đã yêu cầu "hook_direction", cần đảm bảo Writer luôn ưu tiên câu mở đầu mạnh.
- Content affiliate_flight nên tối ưu để tăng saves/comment chất lượng (hỏi giá, hỏi cách
  đặt) hơn là chỉ chăm chăm view — khớp đúng với tín hiệu thương mại đang được tính nặng.
- 1 post/tuần affiliate_flight (giới hạn đã set trong `affiliate-injector`) phù hợp với
  nguyên tắc follower-first: spam affiliate làm follower base engage kém → cả kênh bị ảnh
  hưởng ở vòng test đầu tiên của MỌI video sau đó, không chỉ video affiliate.

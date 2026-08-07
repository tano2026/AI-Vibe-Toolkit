# Handoff Template — Platform Policy Intelligence → Writer/Media

Dùng template này để rút gọn ghi nhớ (`memory/*.md`) thành checklist hành động được,
KHÔNG đưa nguyên bài research dài cho Writer/Media đọc.

---

## Handoff cho Writer Agent (ví dụ điền theo dữ liệu 2026-08-06)

```yaml
platform_targets: [tiktok, youtube_shorts, facebook, instagram]

hook_requirement:
  window: "3-5 giây đầu"
  note: "TikTok/YouTube đều xác nhận đây là cửa sổ quyết định — không mở đầu bằng câu chào/giới thiệu dài"

length_guidance:
  tiktok: "Không có độ dài cố định — ưu tiên completion rate >70%, video ngắn dễ đạt hơn nhưng dài vẫn được thưởng nếu giữ chân được"
  youtube_shorts: "Dưới 3 phút, satisfaction quan trọng hơn độ dài"
  facebook_reels: "Tới 3 phút vẫn reach non-follower được"

engagement_design:
  - "Thiết kế câu hỏi/CTA khơi gợi comment CÓ NỘI DUNG (không phải chỉ emoji) — TikTok 2026 tính nặng comment chất lượng"
  - "Nếu có affiliate/CTA mua hàng: tối ưu cho saves + comment hỏi giá/cách đặt, không chỉ chăm view"

disclosure_text_required:
  when: "Nội dung AI-generated photorealistic HOẶC có affiliate link"
  ai_disclosure: "Dùng đúng toggle/checkbox lúc đăng theo từng platform — không viết tay trong caption thay thế"
  affiliate_disclosure: "Câu cố định trong AFFILIATE_DISCLOSURE_VI (xem agents/trum-san-bay/orchestrator.py)"

banned_or_restricted:
  - "Không bịa số liệu/chính sách (nguyên tắc sẵn có, không đổi)"
  - "Không tường thuật lại clip người khác mà không có hiện diện/phân tích thật (rủi ro Facebook 2026 originality)"
```

## Handoff cho Media/Visual Agent

```yaml
aspect_ratio:
  tiktok: "9:16 bắt buộc"
  youtube_shorts: "9:16, overlay AI-label ở góc dưới trái nếu áp dụng"
  facebook_reels: "9:16"
  youtube_longform: "16:9, label AI (nếu có) hiện ngay dưới player"

ai_disclosure_placement:
  tiktok: "Bật toggle 'AI-generated content' lúc upload — KHÔNG chỉ ghi trong caption"
  youtube_shorts: "Overlay trực tiếp trên video, góc dưới trái — tự động nếu quên do detection từ 5/2026"
  youtube_longform: "Ngay dưới video player, phía trên mô tả"
  facebook_instagram: "'Made with AI' tự động nếu dùng tool có C2PA/IPTC metadata — kiểm tra
    tool render đang dùng (HyperFrames/Gemini image) có giữ metadata này không, nếu không
    thì phải tự thêm label tay"

cross_platform_asset_warning:
  risk: "Facebook/Instagram 2026 phạt nặng nội dung 'chỉ đổi caption, asset y hệt' — xem
    memory/meta.md phần CẢNH BÁO"
  action: "Với ảnh: đổi crop/vị trí overlay text giữa bản FB và IG. Với video: cân nhắc
    trim/đổi thứ tự đoạn. CHƯA code vào Adapter — cần xác nhận độ ưu tiên trước khi sửa"

character_consistency:
  note: "Nếu dùng persona nhất quán (như Trùm Sân Bay), đảm bảo brand-design-system check
    (màu/font/logo) không đổi giữa các platform — khác với asset content bên trong"
```

## Cách cập nhật template này

Khi `memory/{platform}.md` có entry mới quan trọng (Bước 4 trong SKILL.md — dấu hiệu cần
research lại), review lại 2 block YAML trên, cập nhật field liên quan, ghi ngày cập nhật
ở đầu file. Không cần cập nhật toàn bộ file mỗi lần — chỉ field bị ảnh hưởng bởi thay đổi mới.

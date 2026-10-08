# Prompt Motion (prompt-motion.com) — Website / Thư viện tham khảo

> Tên miền đúng: **prompt-motion.com** (không phải "promt-motion.com" — gõ thiếu chữ "p" thì không vào được).

## TL;DR
Thư viện (gallery) ~230 video motion/launch film làm bằng **Claude Opus 5.5**, mỗi video kèm **prompt** hoặc **skill** đã dùng để tạo ra nó. Do @p4nthera_ tuyển chọn, tác giả từng video được ghi nguồn (link X). Đây là chỗ để **tra prompt/skill mẫu khi cần làm video motion**, không phải công cụ tạo video. Trang tuyên bố **cấm AI train, chỉ cho dùng để tham khảo** (robots.txt) — agent phải tra từng trang khi cần, không cào hàng loạt, không sao chép vào kho.

## Trang này dùng để làm gì
- Duyệt video mẫu, lọc theo **Prompt / Skill / Popular** (bộ lọc trên trang chủ)
- Mở 1 mục → xem video, prompt (có nút Copy) hoặc lệnh cài skill (`npx skills add ...`) + link repo
- Đăng ký email nhận video mới; có nút Submit để tác giả gửi bài (chưa rõ quy trình)
- Nghiên cứu ngày 08/10/2026: không thấy giá, đăng nhập, API, hay định dạng tải về

## Cách vào (cho agent)
| Việc | Cách |
|---|---|
| Trang chủ | `https://prompt-motion.com/` — liệt kê ~230 mục |
| 1 mục cụ thể | `https://prompt-motion.com/<handle-tác-giả>-<mã-6-ký-tự>` ví dụ `/buildfastwithai-53234e` |
| Video / ảnh | `https://media.prompt-motion.com/<slug>/video.<hash>.mp4` và `poster.<hash>.webp` |
| Sitemap / API | **Không có** (sitemap.xml trả 404, robots.txt không khai sitemap) |
Mỗi trang mục thường có: tiêu đề, tác giả (link X), loại (Prompt hoặc Skill), model (Opus 5.5), mức effort (nếu ghi), ngày đăng, prompt hoặc lệnh cài skill, link repo, link bài gốc trên X. **Nội dung đầy đủ của skill không hiển thị trên trang — phải vào repo của tác giả.**

## ⚠️ Quy tắc sử dụng (từ robots.txt, đọc 08/10/2026)
- Tín hiệu nội dung: `search=yes`, **`ai-train=no`**, **`use=reference`**
- Khoảng 35 crawler AI bị chặn hoàn toàn (ClaudeBot, GPTBot, Google-Extended, CCBot, Bytespider, Applebot-Extended...)
- Trang ghi: video và prompt thuộc về tác giả
Hệ quả cho Tano:
1. Tra **từng mục khi có nhu cầu thật** (1 người dùng 1 lần), như người đọc tham khảo. KHÔNG cào cả trang, KHÔNG lập lịch quét
2. KHÔNG sao chép hàng loạt prompt/skill vào kho. Kho chỉ lưu **con trỏ + ghi chú ngắn + link nguồn**
3. Khi dùng ý tưởng từ 1 prompt: viết lại theo hoàn cảnh của mình, ghi nguồn (tác giả + link), không dán nguyên văn vào sản phẩm bán
4. KHÔNG dùng nội dung trang để huấn luyện/tinh chỉnh bất kỳ mô hình nào
5. Agent dùng User-Agent riêng có ghi liên hệ, không giả danh crawler khác; gặp 403/chặn thì dừng, không tìm đường vòng
(Đây là cách tao đọc tín hiệu của trang; không phải tư vấn pháp lý.)

## Mục Skill đã thấy (4 mục, mỗi cái trỏ tới 1 repo riêng)
| Mục | Skill làm gì | Cài | Trạng thái trong kho |
|---|---|---|---|
| Anthony Riera — Reddit marketing launch video (26/09/2026) | Học design system của sản phẩm, phỏng vấn người dùng, dựng launch/landing video bằng Remotion với component và logo thật | `/plugin marketplace add Rieranthony/product-film-skill` | **Đã có** `repos/product-film-skill.md` |
| Leon Lin (@LexnLin) — Cinetic skill launch film (04/10/2026) | Từ concept + brand + "score" render phim ra mắt/motion ngắn bằng code | `npx skills add Leonxlnx/cinetic` | `repos/cinetic.md` (7/10) |
| Jake Moran — Animated agent session story (24/09/2026) | Đọc lịch sử Claude Code cục bộ → phim hoạt hình ngắn có nhạc bằng HyperFrames | `npx skills add heygen-com/hyperframes-community-skills --skill session-story` | `repos/hyperframes-session-story.md` (3/10; đọc lịch sử phiên cục bộ = dữ liệu nhạy cảm) |
| Build Fast with AI — Indian civilisation history film (28/09/2026) | Tạo phim MP4 hoạt hình về chủ đề bất kỳ, vẽ từng khung bằng code, nhạc tổng hợp đồng bộ nhịp | `npx skills@latest add https://github.com/buildfastwithai/buildfast-skills` (thư mục `generative-film-skill`) | `repos/buildfast-generative-film-skill.md` (6/10) |
Phần còn lại (~226 mục) chủ yếu là **Prompt**. Muốn đào sâu 1 skill nào → báo Nobitano để tao viết entry riêng, đừng cài thử vì thấy hay.

## Ví dụ prompt (từ mục @stephanlivera, 25/09/2026, Opus 5.5, effort Max)
Chỉ trích ngắn để minh hoạ cấu trúc: yêu cầu "một video motion graphics 15 giây sinh động, như showreel của một motion designer". Bài học: prompt ngắn + mục tiêu rõ + giới hạn thời lượng + để effort cao. Muốn bản đầy đủ → vào trang gốc.

## Khi nào agent nên tra trang này
- Cần ý tưởng prompt/cấu trúc cho video motion, launch film, showreel (ABTRIP, Tano, Wonder Mart, TanoOS)
- Cần tìm skill tạo video bằng code (Remotion/HyperFrames) để so với `repos/remotion.md`, `repos/hyperframes.md`, `repos/product-film-skill.md`
- KHÔNG tra khi: đã có sẵn trong kho (xem Link), hoặc chỉ cần công thức prompt điện ảnh → `agents/designer-pro/skills/cinematic-shot-prompt-core/SKILL.md`

## Lưu ý / Lỗi thường gặp
- Mọi video trong trang chạy bằng **Opus 5.5** (một vài mục có ghi nhiều vòng chỉnh); kết quả không đảm bảo lặp lại với model khác
- Tác giả đăng trên X → có thể thay đổi/xoá; link repo có thể chết
- Bộ lọc trên trang chủ không có URL riêng (xem được trong trình duyệt, không tham chiếu được bằng link)
- Sandbox của tao **không truy cập trực tiếp được trang** (proxy chặn 403); nội dung đọc qua công cụ tìm nạp web. Agent trên VPS của mày chưa test
- Nghiên cứu mới từ trang chủ + 5 mục mẫu, không đọc hết ~230 mục

## Đánh giá cá nhân
- Điểm mạnh: chọn lọc, mỗi mục có video thật + prompt/skill + ghi nguồn tác giả; cập nhật gần đây (mục mới nhất thấy là 04/10/2026); giúp tránh "viết prompt từ đầu" cho việc motion
- Điểm yếu: không có API/sitemap/tìm kiếm trong trang; skill không hiển thị đầy đủ (phải sang repo); điều khoản cấm AI train nên không thể "nạp cả trang vào kho"; một nguồn tham khảo, không phải công cụ
- Có nên dùng: **7/10** làm thư viện tham khảo tra tay khi cần. Không đáng đầu tư tích hợp tự động

## Link
- Trang: https://prompt-motion.com
- Người tuyển chọn: https://x.com/p4nthera_
- Trong kho: `repos/awesome-claude-5-5-videos.md` (danh mục tương tự), `repos/product-film-skill.md`, `repos/hyperframes.md`, `repos/remotion.md`, `stacks/video-factory-auto-router.md`, `agents/designer-pro/skills/cinematic-shot-prompt-core/SKILL.md`, `agents/designer-pro/skills/prompt-motion-reference/SKILL.md`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# CHỈ tra tay từng mục khi có nhu cầu thật. KHÔNG vòng lặp quét cả trang.
# Chưa test (sandbox của tao không vào được trang). Thử 1 mục trước.
import urllib.request, re

UA = "TanoAgent/1.0 (tra cứu tham khảo; liên hệ: tan@oneworld.com.vn)"

def lookup_entry(url):
    assert url.startswith("https://prompt-motion.com/"), "chỉ trang prompt-motion.com"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    html = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
    return {
        "url": url,
        "install": re.findall(r"(?:npx skills[^<\"\\]{0,160}|/plugin (?:marketplace|install)[^<\"\\]{0,100})", html)[:3],
        "video": re.findall(r"https://media\.prompt-motion\.com/[^\"\\\s<]+\.mp4", html)[:1],
    }
# Nếu 403/chặn: dừng, báo Nobitano. Không đổi UA giả danh. Kết quả chỉ ghi: URL nguồn + 2-3 dòng ghi chú.
```

### OpenClaw
```bash
# Không cần cài gì. Khi Nobitano hỏi "tìm prompt/skill motion mẫu": mở https://prompt-motion.com,
# đọc 1-3 mục liên quan, trả lời kèm link nguồn + tác giả. Không lưu hàng loạt.
```

### Antigravity
```bash
# Không áp dụng (không có gì để deploy). Muốn thử 1 skill tìm thấy: xem lệnh cài trong trang mục,
# đọc repo của tác giả trước, rồi mới cài (quy trình trong skill-lifecycle-management).
```
> ⚠️ ai-train=no, use=reference. Không cào, không mirror, không train.

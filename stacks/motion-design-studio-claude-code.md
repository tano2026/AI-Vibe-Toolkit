# Stack: Motion Design Studio với Claude Code (15 repo, chọn đường đi)

## TL;DR
Một danh sách 15 repo "biến Claude thành motion design studio" thực ra là **5 nhóm việc khác nhau**, không phải một bộ cài hết. Nếu agency chỉ chọn một đường: **HyperFrames làm engine** (Apache-2.0, tránh được license Remotion) + **`product-launch-motion`** cho video launch + **`hyperframes-student-kit`** cho video quay sẵn + **`gsap-skills`** và **`lottiefiles-motion-design-skill`** làm lớp nền. 10 repo còn lại để sau hoặc bỏ. **Trạng thái thật: chưa chạy skill nào trong 11 repo mới.** Mọi đánh giá là từ README, clone cục bộ và vài lệnh npm/CLI đã chạy.

## Bảng chọn theo việc cần làm
| Nhóm | Repo | Entry trong kho | Sao (đọc từ trang) | Ghi chú nhanh |
|---|---|---|---|---|
| A. Video launch | product-launch-motion | `repos/product-launch-motion.md` | 1 | Chọn cái này cho video launch |
| A | motion-graphics-skills | `repos/motion-graphics-skills.md` | 9 (đo 10/10) | 15 skill, đã có trong kho từ trước |
| A | claude-motion-design | `repos/claude-motion-design.md` | 0 | Không cần Remotion; `skills` CLI không nhận, cài tay |
| B. Video quay sẵn | hyperframes-student-kit | `repos/hyperframes-student-kit.md` | 527 | Chọn cái này; Whisper local nếu footage của khách |
| B | motion-graphics (Barty-Bart) | `repos/barty-motion-graphics.md` | 374 | B-roll biến hình + tách nền local; SFX CC0 |
| C. Hoạt hình/explainer | animate (cth9191) | `repos/cth9191-animate.md` | 526 | 7 style, 3 cổng duyệt; lồng tiếng cần ElevenLabs |
| C | claude-motion | `repos/claude-motion.md` | 0 | Lấy `sound-design`, `review-loop` làm lớp thiết kế |
| C | claude-remotion-skill | `repos/claude-remotion-skill.md` | 245 | Chồng chéo; ưu tiên thấp |
| D. Web UI | motion (motiondivision) | `repos/motiondivision-motion.md` | 34,0k | Thư viện thật, MIT, npm 14.1.0 |
| D | motion-dev-animations-skill (199-biotechnologies) | `repos/motion-dev-animations-skill.md` | chưa đo | Nhắm v11+, cập nhật cuối 03/2026; ưu tiên thấp |
| E. Nền tảng | hyperframes | `repos/hyperframes.md` | (đã có) | Engine chính |
| E | remotion | `repos/remotion.md` | (đã có) | Có license công ty, xem dưới |
| E | remotion-dev/skills | `repos/remotion.md` | (đã có) | Chính chủ; xem ghi chú số skill bên dưới |
| E | gsap-skills | `repos/gsap-skills.md` | 14,1k | Chính chủ, chỉ là tài liệu |
| E | LottieFiles/motion-design-skill | `repos/lottiefiles-motion-design-skill.md` | 2,1k | Rủi ro thấp nhất, thử đầu tiên |

## Thứ tự thử (mỗi bước đo thời gian và token, ghi lại)
1. **`lottiefiles-motion-design-skill`**: chỉ markdown, không script, `--list` chạy ngay. Đọc `SKILL.md` 5 phút, nhờ Claude review một animation UI có sẵn.
2. **`gsap-skills`**: chính chủ, tài liệu thuần. Cài rồi nhờ Claude viết một timeline vào cảnh.
3. **`product-launch-motion`**: một brief ngắn cho [SẢN PHẨM] của chính mình, voiceover 1 bản, không dùng cho khách ở lần đầu.
4. **`hyperframes-student-kit`**: một clip talking head 1–2 phút **không nhạy cảm**, Whisper local.
Dừng sau mỗi bước nếu kết quả không đáng so với tốn kém. Không cài cả 11.

## Ma trận license (đọc trước khi bán sản phẩm cho khách)
| Thành phần | License theo nguồn | Mức kiểm |
|---|---|---|
| HyperFrames | Apache-2.0 (theo `repos/hyperframes.md`; bản sao license nằm trong student-kit) | 📖 |
| Remotion | License riêng: cá nhân/nhóm nhỏ miễn phí, công ty trên ngưỡng cần license thương mại (theo `repos/remotion.md`: 4+ người) | 📖 kiểm lại trang license trước khi dùng |
| GSAP (gói npm) | "Standard 'no charge' license" (không phải MIT), README repo nói miễn phí kể cả thương mại cho mọi plugin | ✅ `npm view gsap license` + 📖 README |
| Motion | MIT | ✅ `npm view motion license` |
| Phim/ảnh mẫu trong repo | Không có quyền dùng lại (product-launch-motion: của công ty khách tác giả; student-kit: tài sản brand AIS; claude-motion-design: logo Howseen) | ✅ đọc NOTICE / THIRD_PARTY_NOTICES |
| SFX của Barty-Bart | CC0 (README ghi đã kiểm từng file 12/10/2026) | ✅ đọc `LICENSES.md` |
| Nhạc/SFX/logo do `fetch_assets.py` (claude-motion-design) tải | License từng nguồn (Mixkit, Pexels, Unsplash...) | 📖 kiểm từng file |

Hệ quả thực tế: `claude-remotion-skill`, phần Remotion của `claude-motion` và `remotion` đều dẫn tới license Remotion. HyperFrames và `claude-motion-design` thì không.

## Cái bẫy chung
- **Quy mô cộng đồng:** trong 11 repo mới, 3 repo có ≤ 1 sao, 4 repo dưới 530 sao, chỉ 3 repo vượt 2.000 sao (`motion` 34,0k, `gsap-skills` 14,1k, LottieFiles 2,1k). Nhiều repo chỉ 1–17 commit. Sao đọc từ trang, chưa đối chiếu API.
- **Chi phí model:** `motion-graphics-skills` và `claude-motion-design` ghi rõ làm trên Opus 5.5; dựng nhiều cảnh = nhiều token. Chưa có số đo của tao.
- **Dịch vụ trả phí ngầm:** `hyperframes-student-kit` (ElevenLabs Scribe, Kie.ai) và `cth9191-animate` (ElevenLabs lồng tiếng). Xem ghi chú 11/10 trong `repos/elevenlabs-skills.md`: gói miễn phí bị chặn khi qua proxy/VPN.
- **Lời post và lời README không bằng nhau:** "dứt điểm", "chỉ một câu lệnh", "5 lần prompt" đều mạnh hơn README. Đã đối chiếu từng cái trong từng entry.
- **Chồng chéo:** đừng cài hơn một lớp "design" (product-launch-motion, motion-graphics-skills, claude-motion). Skill nạp mô tả mỗi phiên, càng nhiều càng ăn context.

## Những gì đã chạy thật (2026-10-12)
- ✅ Clone nông và đọc README, danh sách file, ngày commit của 11 repo (+ charlie947, remotion-dev/skills để đối chiếu).
- ✅ `npx skills add <clone> --list`: nhận ra skill ở 9/10 repo thử. **Không nhận ra: `claude-motion-design`** (skill nằm ở `skill/motion-design/`, cài tay).
- ✅ `npm view gsap|motion|framer-motion version license`.
- ❌ Chưa chạy skill nào để ra video hay animation. Chưa cài từ GitHub (sandbox chặn API GitHub cho repo công khai). Chưa đo token, thời gian, chất lượng.

## Ghi chú còn mở
- `repos/remotion.md` ghi `remotion-dev/skills` có "30+ skill modules"; bản clone 12/10/2026 có **12 thư mục skill** (`remotion-best-practices`, `remotion-captions`, `remotion-create`, `remotion-docs`, `remotion-interactivity`, `remotion-maps`, `remotion-markup`, `remotion-multimedia`, `remotion-render`, `remotion-saas`, `remotion-studio`, `remotion-upgrade`). Có thể số "30+" đếm cả file rule bên trong. Chưa đối chiếu, chưa sửa entry đó.
- Số sao của `motion-dev-animations-skill` chưa đo.

## Link
- Danh sách gốc: bài post "15 repo GitHub biến Claude Opus 5.5 thành motion design studio"
- Liên quan: `repos/hyperframes.md`, `repos/remotion.md`, `repos/ffmpeg.md`, `repos/whisper.md`, `repos/elevenlabs-skills.md`, `repos/prompt-motion.md`, `stacks/remotion-template-factory.md`

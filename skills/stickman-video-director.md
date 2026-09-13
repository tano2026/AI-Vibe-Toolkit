---
name: stickman-video-director
description: >
  Codex/Claude Skill (kaomei/stickman-video-director, 256 sao) — biến script/ý tưởng thành
  video người que 1 phút: hook + storyboard 6 cảnh + prompt sẵn cho Gemini Omni Flash.
---

# Stickman Video Director — Skill

## TL;DR
Skill (không phải app) — đưa vào 1 ý tưởng/copy, skill tự viết lại thành voiceover tiếng Anh đã confirm, dựng "director's plan" 6 cảnh, rồi sinh prompt sẵn cho Gemini Omni Flash để render đúng phong cách người que tương phản cao (đen trên trắng hoặc trắng trên đen) — đúng chất Pivot Animator, không phải AI tự vẽ tùy hứng. 256⭐, MIT, hỗ trợ đa ngôn ngữ trong docs (Anh/Trung/Nhật/Hàn/Bồ).

## Tool này dùng để làm gì
Nguyên tắc cốt lõi của skill: *"a script is not yet a video"* — nó không nhảy thẳng vào tạo prompt, mà làm phần "đạo diễn" trước: xây hook, pacing, phát minh ẩn dụ hình ảnh liên quan, chuyển cảnh, giữ continuity xuyên suốt — rồi mới ra 6 prompt cuối cho model.

Quy trình:
1. Nhận copy/ý tưởng thô
2. Viết lại thành voiceover tiếng Anh gọn, đúng nhịp cho video 1 phút
3. Dựng bảng đề xuất 6 cảnh (director's proposal) — **dừng lại xin xác nhận trước khi generate**, để mình sửa câu chuyện khi chi phí sửa còn rẻ
4. Sau khi confirm, xuất 6 prompt Gemini Omni Flash sẵn sàng render, giữ nhất quán ngôn ngữ hình ảnh (người que + nền tương phản cao) xuyên suốt

## Setup từng bước
```bash
# Cài như 1 skill Codex/Claude Code
npx skills add kaomei/stickman-video-director
```
Sau đó gọi skill trong Claude Code/Codex với script hoặc ý tưởng thô — skill tự hỏi xác nhận storyboard trước khi generate.

## Ví dụ thực tế — áp cho GMSP
GMSP dùng khung 4 lớp cố định: Hook → Tử Vi setup (cung) → Tâm lý giải mã → Lịch sử anchor → Ứng dụng → Close/CTA (voice "Kẻ Soi Gương": mở bằng cáo buộc hành vi trực tiếp, gọi thẳng "bạn", không mềm hoá).

Dùng skill này cho phần **minh hoạ hình ảnh của đoạn Tâm lý giải mã hoặc Lịch sử anchor** — ví dụ: đưa đoạn script "người cung Thiên Di hay bỏ dở giữa chừng vì sợ cam kết — [tên nhân vật lịch sử] cũng vậy, tới năm 40 tuổi mới..." vào skill → skill tự dựng 6 cảnh người que minh hoạ hành vi đó (một người đứng giữa ngã ba, dùng dằng, quay đầu bỏ chạy...) → xuất prompt Gemini Omni Flash. Hợp để chèn xen giữa các đoạn TTS mà không cần quay/dựng cảnh người thật, giữ đúng tinh thần "chỉ ra hành vi cụ thể" thay vì minh hoạ trừu tượng.

## Lưu ý / Lỗi thường gặp
- Skill chỉ lo phần *đạo diễn + prompt*, việc render thật vẫn cần quyền truy cập Gemini Omni Flash (khả năng/giá tuỳ tài khoản, cần tự kiểm tra).
- Output voiceover mặc định tiếng Anh — với content GMSP tiếng Việt, cần tự dịch/viết lại phần lời trước khi đưa script vào, hoặc chỉ dùng skill cho phần storyboard hình ảnh rồi ghép TTS tiếng Việt riêng theo đúng thứ tự sản xuất GMSP (TTS trước → visuals → edit).
- 6 cảnh cố định cho video 1 phút — cảnh dài hơn cần tự chia nhiều lần gọi hoặc nối nhiều đoạn.

## Đánh giá cá nhân
- Điểm mạnh: 256⭐ (đã kiểm chứng nhiều hơn hẳn nhóm repo hobby trước), đúng chất người que thật (không phải cartoon AI tự bịa), có bước xác nhận storyboard trước khi tốn credit generate — tiết kiệm chi phí thử sai.
- Điểm yếu: phụ thuộc Gemini Omni Flash để render thật (chưa rõ giá/quota); voiceover mặc định tiếng Anh, cần thêm bước dịch cho GMSP.
- Có nên dùng không: 8/10 cho việc chèn minh hoạ người que ngắn vào video GMSP — không thay thế toàn bộ pipeline, chỉ giải quyết đúng khúc "cần hình minh hoạ hành vi/tâm lý" giữa các đoạn TTS.

## Link
- Repo: https://github.com/kaomei/stickman-video-director

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import subprocess

def stickman_storyboard(script_snippet: str) -> str:
    """Gọi skill qua Codex/Claude CLI đã cài — trả về director's plan + prompt.
    Cần review thủ công bước xác nhận storyboard trước khi generate thật."""
    result = subprocess.run(
        ["codex", "run", "stickman-video-director", "--input", script_snippet],
        capture_output=True, text=True
    )
    return result.stdout
```

### OpenClaw
```bash
npx skills add kaomei/stickman-video-director
# Dùng: "dùng stickman-video-director dựng storyboard cho đoạn [script GMSP]"
```

### Antigravity
```bash
# Không cần deploy service riêng — chỉ cần Codex/Claude Code CLI có sẵn trên VPS
npx skills add kaomei/stickman-video-director
```
> ⚠️ Bước xác nhận storyboard nên giữ human-in-the-loop (Nobitano duyệt) trước khi cho Hermes tự động render hàng loạt, tránh sai lệch voice "Kẻ Soi Gương".

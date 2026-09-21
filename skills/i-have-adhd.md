# I Have ADHD — Prompt Template / System Prompt

## TL;DR
Skill nhỏ nhưng viral (26.3k star) ép AI coding agent trả lời kiểu "đưa hành động trước, giải thích sau" — bỏ hết mở bài "Great question!", bỏ vòng vo, đánh số từng bước, chốt bằng đúng 1 hành động tiếp theo. Tác giả làm cho người ADHD nhưng không cần chẩn đoán ADHD mới thấy hợp — vì hầu hết ai cũng thích đọc kiểu này hơn.

## Khi nào dùng
Bật khi làm việc với coding agent (Claude Code, Codex, Cursor, Grok, Hermes CLI, Qwen Code, pi, OMP...) mà thấy nó hay lan man, giải thích trước-làm sau, hoặc trả lời task nhiều bước mà không nhớ đang ở bước nào giữa các lượt hỏi — nhất là khi làm nhiều task dồn dập, dễ mất track "đã tới đâu rồi".

## Nội dung skill / prompt
File gốc canonical là `skills/i-have-adhd/SKILL.md` trong repo — cốt lõi dựa trên 5 nguyên tắc:
```
1. Đưa hành động/lệnh/đường dẫn lên đầu câu trả lời — không phải context, không phải kế hoạch
2. Đánh số các bước nhiều-bước, mỗi bước 1 hành động rõ ràng
3. Không lạc đề — nếu có việc phụ phát sinh giữa lúc làm, tự xử lý nếu được, không thì nêu 1 lần ở cuối
4. Nhắc lại tiến độ mỗi lượt ("bước 3/5 xong") — không giả định người đọc còn nhớ
5. Không mở bài, không tóm tắt lại, không câu chốt kiểu "Hope this helps!"
```
Lấy cảm hứng lỏng từ cuốn *The Adult ADHD Tool Kit* (J. Russell Ramsay & Anthony L. Rostain), chuyển thành nguyên tắc cho AI trả lời, không phải nguyên tắc con người tự quản lý ngày.

## Setup từng bước
1. Claude Code (cách chính thống nhất):
   ```bash
   git clone https://github.com/ayghri/i-have-adhd ./i-have-adhd
   claude plugin marketplace add ./i-have-adhd
   claude plugin install i-have-adhd@i-have-adhd
   ```
   Gọi bằng `/i-have-adhd` trong session. Tắt bằng `claude plugin disable i-have-adhd`.
2. Grok: `grok plugin install ayghri/i-have-adhd --trust` → `grok plugin enable i-have-adhd` → gõ `/i-have-adhd` trong session mới.
3. Hermes CLI: gõ `/i-have-adhd` (tự cài vào `~/.hermes/skills/`), hoặc thêm tap trước để duyệt: `hermes skills tap add ayghri/i-have-adhd` → `hermes skills search adhd` → `hermes skills install ...`.
4. OMP: `omp plugin marketplace add ayghri/i-have-adhd` → `omp plugin install --scope user i-have-adhd@i-have-adhd` → gõ `/i-have-adhd` để toggle.
5. Qwen Code: hỗ trợ GitHub shorthand, cài như native extension, tự nhận skill trong thư mục `skills/`.
6. Không dùng qua plugin — thêm trực tiếp vào `AGENTS.md` (Hermes đọc theo từng thư mục làm việc) hoặc file persona (`SOUL.md`) để bật cho mọi session mà không cần lệnh gọi riêng.

## Ví dụ thực tế
**Trước:** "Great question! Let me think about this. Your auth flow has a few moving pieces: the middleware, the token verification, and the cookie handling. Looking at src/auth.ts... One approach would be to update the package... Hope this helps! Let me know if you want to dig deeper."

**Sau khi bật skill:** "Run `npm install jsonwebtoken@latest`, then edit `src/auth.ts:42`." — xong, đúng hành động cần làm ngay ở câu đầu tiên, phần còn lại (nếu cần) tách riêng "Separately: there is also a stale dependency. Want me to handle that next?"

## Lưu ý / Lỗi thường gặp
- Chỉ tắt được khi người dùng nói đúng câu "stop adhd mode" hoặc "normal mode" — skill tự thiết kế để không tự tắt giữa chừng, tránh trường hợp agent "quên" giữ format.
- Có rất nhiều fork ngôn ngữ khác (zh-TW, pt-BR, zh-CN...) — bản canonical/gốc là **ayghri/i-have-adhd**, các bản dịch là fork độc lập, cập nhật có thể chậm hơn bản gốc.
- Cài trùng tên dễ lỗi khi fork: nếu vừa cài bản gốc vừa muốn cài bản tự fork để sửa, phải `claude plugin uninstall i-have-adhd` + `claude plugin marketplace remove i-have-adhd` trước, vì fork và upstream dùng chung tên marketplace.
- Không phải "làm cho agent làm việc nhanh hơn" — chỉ đổi cách trình bày câu trả lời, không đổi chất lượng suy luận bên trong.

## Đánh giá cá nhân
- **Điểm mạnh:** Ý tưởng đơn giản, tác động rõ ràng ngay lập tức, hỗ trợ sẵn rất nhiều host (Claude Code, Grok, Hermes, OMP, Qwen Code, pi...) với 1 file canonical duy nhất. Viral tự nhiên (nhiều bài viết độc lập trên Threads/Medium/YouTube/TikTok cùng lúc, không phải PR có tổ chức) là tín hiệu tốt về việc nó thực sự giải quyết đúng nỗi đau chung.
- **Điểm yếu:** Chỉ đổi hình thức trả lời, không đổi năng lực agent — dễ bị kỳ vọng quá (tưởng "làm agent thông minh hơn"). Cắt bớt preamble/caveat đôi khi làm mất context cần thiết cho task phức tạp cần giải thích trade-off.
- **Có nên dùng không:** 8/10 — đáng bật cho hầu hết công việc code hàng ngày, đặc biệt khi làm nhiều task dồn dập cần track tiến độ rõ. Tắt tạm khi cần agent giải thích sâu trade-off kỹ thuật phức tạp (lúc đó preamble/context lại có giá trị).

## Link
- Nguồn gốc skill: https://github.com/ayghri/i-have-adhd
- Cài đặt đầy đủ theo từng host: https://github.com/ayghri/i-have-adhd/blob/main/INSTALL.md

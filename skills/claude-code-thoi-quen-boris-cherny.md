# Claude Code — 12 thói quen từ talk của Boris Cherny (đã đối chiếu docs 10/2026)

## TL;DR
Talk "Mastering Claude Code in 30 minutes" của Boris Cherny (người tạo ra Claude Code), quay tại Code w/ Claude ngày 22/05/2025, dài 28 phút. Phần lõi vẫn đúng và docs mới nhất còn nhấn mạnh hơn: **hỏi code trước khi sửa, cho Claude cách tự kiểm tra việc nó làm, plan trước khi code việc lớn, giữ CLAUDE.md ngắn**. Nhưng talk đã 16 tháng tuổi: vài lệnh đã đổi tên, và thiếu hẳn những thứ docs mới coi là quan trọng (quản context bằng `/clear` và `/rewind`, `/goal`, Stop hook, worktree, auto mode). File này gộp cả hai thành 1 bộ thói quen dùng được ngay. Đây là **phương pháp làm việc, không phải tool**: không có gì để cài thêm.

## Video này là video nào (nói thật)
- Tweet gốc trên X **không mở được** (site chặn bot), nên tao không đọc được nguyên văn. Tweet nói "24 phút, hai kỹ sư Anthropic". Talk của Boris dài 28:07 và theo transcript chỉ có một mình Boris nói. Nội dung tweet mô tả (Claude tự viết code, fix bug trong terminal, tối ưu prompt) khớp talk này nhất, nhưng **chưa chắc 100% là cùng video**. Talk "Claude Code best practices" của Cal Rueb (25:53) cùng sự kiện cũng là ứng viên, tao chưa đọc.
- Transcript video gốc không lấy được (vidIQ hết credit). Mọi chỗ ghi "talk nói" bên dưới là **qua 3 bản tóm tắt/transcript của bên thứ ba**, không phải tao xem video.

**Mức kiểm dùng trong file:** ✅ khớp docs Claude Code hiện hành (tao đọc 11/10/2026) · 📖 chỉ từ talk/tóm tắt, chưa đối chiếu · 🔄 talk nói nhưng đã đổi · ❓ cần test thật mới chắc.

## Khi nào dùng
- Mở Claude Code lần đầu trên 1 repo lạ (ví dụ repo Smart Booking, portal TMC của ABTRIP) → dùng thói quen 1.
- Giao việc nhiều bước cho Claude rồi bỏ đi (đúng kiểu agent chạy VPS) → thói quen 2, 8, 10.
- CLAUDE.md phình to, Claude bắt đầu "quên" luật → thói quen 5, 6, 7.
- Viết skill/playbook cho Hermes, OpenClaw, Antigravity gọi Claude Code → mục Agent Integration cuối file.

## Nội dung skill / prompt (copy-paste được)
Khối ngắn này dán vào CLAUDE.md của project (hoặc `~/.claude/CLAUDE.md`). Cố ý chỉ ~25 dòng: docs khuyên mỗi dòng phải qua câu hỏi "bỏ dòng này thì Claude có làm sai không?".

```
# Cách làm việc với tao
- Việc mới: đọc code và trả lời câu hỏi trước, chưa sửa gì cho tới khi tao nói.
- Việc đụng nhiều file hoặc tao chưa rõ hướng: đưa plan, chờ tao OK rồi mới code.
  Việc mô tả được bằng 1 câu thì làm luôn, không cần plan.
- Xong việc phải có bằng chứng chạy được: output test, mã thoát của build, hoặc
  screenshot. Không có cách kiểm thì nói rõ là chưa kiểm được, đừng nói "xong".
- Sửa 1 lỗi mà tao phải nhắc lại 2 lần vẫn sai: dừng, tóm tắt cái đã học,
  tao sẽ /clear và viết prompt lại.
- Điều tra rộng (đọc nhiều file): dùng subagent, chỉ báo lại kết luận.
- Commit: viết theo format git log hiện có. Không push nếu tao chưa bảo.

# Lệnh hay dùng (điền theo project)
- Test 1 file: [lệnh]
- Typecheck: [lệnh]
- Build: [lệnh]
```

Prompt phỏng vấn trước khi code việc lớn (lấy từ docs hiện hành, thay trong ngoặc):

```
Tao muốn build [mô tả ngắn]. Phỏng vấn tao thật kỹ bằng tool AskUserQuestion.
Hỏi về kỹ thuật, UI/UX, edge case, rủi ro, đánh đổi. Đừng hỏi điều hiển nhiên,
đào vào chỗ khó tao có thể chưa nghĩ tới. Hỏi tới khi đủ rồi viết spec đầy đủ
vào SPEC.md. Spec phải nêu: file/interface liên quan, cái gì NẰM NGOÀI phạm vi,
và 1 bước kiểm end-to-end chứng minh tính năng chạy được.
```
Xong SPEC.md thì mở **phiên mới** để thực thi (context sạch, có spec làm gốc).

## 12 thói quen
| # | Thói quen | Talk 2025 nói | Mức kiểm |
|---|---|---|---|
| 1 | **Hỏi về code trước khi sửa.** Hỏi hàm này dùng ở đâu, vì sao có tham số lạ (Claude tra git history), tuần này mình ship gì | Anthropic dạy ngày đầu onboarding, kể giảm từ 2–3 tuần xuống 2–3 ngày; không index, không đẩy code lên server nào | ✅ docs có cùng khuyến nghị. 📖 con số 2–3 tuần→2–3 ngày là Anthropic tự báo, không ai kiểm độc lập |
| 2 | **Cho Claude cách tự kiểm:** test, build, screenshot so với mockup. Docs mới gọi đây là mẹo quan trọng nhất | Iterate 2–3 vòng là gần hoàn hảo; UI thì Puppeteer/iOS simulator | ✅ docs: không có check thì "trông giống xong" là tín hiệu duy nhất và chính mày thành vòng kiểm |
| 3 | **Explore → Plan → Confirm → Code → Commit** cho việc lớn | Plan mode không bắt buộc, chỉ cần bảo "brainstorm, đưa plan cho tao duyệt" | ✅ docs: bấm Shift+Tab tới khi hiện plan mode hoặc `claude --permission-mode plan`; Ctrl+G mở plan trong editor để sửa. Việc nhỏ thì bỏ plan |
| 4 | **"commit, push, PR"** một câu | Claude đọc git log, bắt chước format commit | ✅ docs có prompt tương tự |
| 5 | **CLAUDE.md ngắn**, đặt ở root, nạp mỗi phiên | Có 4 tầng: enterprise, `~/.claude/`, project (commit git), `CLAUDE.local.md` (không commit) | ✅ docs: bản dài khiến Claude bỏ qua luật. Dọn bằng `/doctor` |
| 6 | **Lệnh/skill tự viết cho việc lặp lại** | `.claude/commands/*.md`, Anthropic dùng 1 lệnh gắn nhãn issue GitHub tự động | 🔄 giờ khuyên dùng `.claude/skills/<tên>/SKILL.md`; thư mục commands cũ vẫn chạy ✅ |
| 7 | **Quản context như tài nguyên khan hiếm** | Talk chỉ nói Esc dừng, Esc 2 lần quay lại, `--resume`/`--continue` | ✅ phần này docs nhấn mạnh hơn talk nhiều, xem mục "Thứ talk không có" |
| 8 | **Dạy Claude CLI của team** bằng `--help`, ghi vào CLAUDE.md; thêm MCP | Mô tả CLI nội bộ để Claude tự dùng | ✅ docs: CLI tiết kiệm context hơn MCP; `claude mcp add` để nối MCP |
| 9 | **Dán ảnh/mockup**, kéo thả hoặc đưa đường dẫn | Dùng cùng Puppeteer để lặp tới khi giống | ✅ |
| 10 | **Chạy như tiện ích Unix:** `claude -p "..."`, pipe vào/ra, `--output-format json`, `jq` | Dùng trong CI, xử lý sự cố, tóm tắt log | ✅ docs có cùng ví dụ; json trả 1 object có trường `result` |
| 11 | **Chạy nhiều phiên song song:** nhiều checkout hoặc git worktree, tmux + SSH | Power user chạy nhiều tab | ✅ docs thêm `claude --worktree [tên]`, xem dưới |
| 12 | **Quyền:** allowlist lệnh quen, enterprise policy chặn URL; `Shift+Tab` auto-accept sửa file; `!` chạy bash đưa output vào context; `@` kéo file vào | Bash luôn cần duyệt dù đã auto-accept sửa file | 🔄 xem mục "đã đổi" ngay dưới |

Phụ: bật dictation trên macOS (bấm 2 lần phím dictation) để nói thay gõ — 📖 mẹo của Boris, hợp với prompt dài. Windows thì không áp dụng.

## Cái đã đổi so với talk (đừng gõ theo mù)
| Talk 2025 | Hiện tại (docs đọc 11/10/2026) |
|---|---|
| `/allowed-tools` | `/permissions` để allowlist, có wildcard dạng `Bash(bun run *)`; commit vào `.claude/settings.json` ✅ |
| Bash luôn hỏi | **Auto mode** là chế độ khởi đầu mặc định từ Claude Code v2.1.283 (bản cũ chỉ Pro/Max/Team): một model phân loại duyệt hành động rủi ro thay mày ✅ |
| "think hard", "ultrathink" | Có `/effort` chọn low/medium/high/xhigh/max/auto ✅ (từ trang power-user tips). Từ khoá cũ còn tác dụng không: ❓ chưa test |
| `#` để lưu ngay vào memory | Docs hiện hành nhắc: bảo Claude "thêm rule này vào CLAUDE.md", và `/memory` cho auto-memory. Phím `#` mình **không thấy** trong trang docs đã đọc: ❓ test thật rồi mới dựa vào |
| "Python SDK sắp ra" | Thông tin cũ. Giờ có SDK/Agent SDK, ❓ tao chưa mở docs SDK nên chưa nói chi tiết |
| `/vibe` | Talk nhắc nhưng không giải thích, bỏ qua |

## Thứ talk KHÔNG có mà docs mới coi là cốt lõi
Điểm gốc của docs: **context window đầy rất nhanh và chất lượng tụt khi nó đầy**. Hầu hết lời khuyên đều xuất phát từ đó.

| Thói quen | Lệnh |
|---|---|
| Reset giữa việc không liên quan | `/clear`. Sửa cùng 1 lỗi quá 2 lần mà vẫn sai → `/clear` rồi viết lại prompt tốt hơn, đừng sửa tiếp |
| Quay lại điểm cũ, cả hội thoại lẫn code | `Esc` 2 lần hoặc `/rewind`. ⚠️ checkpoint chỉ theo dõi sửa file qua tool của Claude, **không bắt thay đổi qua Bash**, không thay git |
| Nén có chủ đích | `/compact Tập trung vào thay đổi API` |
| Hỏi nhanh không làm phình context | `/btw <câu hỏi>` |
| Chạy dài không cần ai coi | `/goal` đặt điều kiện (evaluator riêng kiểm sau mỗi lượt), hoặc **Stop hook** chạy script kiểm và chặn Claude kết thúc tới khi qua |
| Người thứ hai kiểm | Subagent review diff trong context mới; hoặc Writer/Reviewer 2 phiên |
| Điều tra rộng không đốt context chính | "Dùng subagent điều tra X" |
| Song song an toàn | `claude --worktree [tên]` (thêm `--tmux`), `/batch <việc>` chia 5–30 subagent mỗi cái 1 worktree |
| Phiên chạy nền | `claude agents` (đang research preview), `/loop 5m /lệnh`, `/schedule` (job chạy cloud khi tắt máy) |
| Làm tiếp việc cũ | `/rename`, `claude --continue`, `claude --resume` |
| Chạy script hàng loạt | `claude -p ... --allowedTools "..." --permission-mode dontAsk` (từ chối mọi thứ chưa duyệt, hợp chạy không người) và `--bare` để khởi động nhanh hơn |

## Setup từng bước (áp vào Claude Code của mày)
1. `claude --version` và `claude doctor` để chắc bản cài ổn. Muốn auto mode mặc định cần v2.1.283 trở lên.
2. Dán khối "Cách làm việc với tao" ở trên vào CLAUDE.md. Chạy `/context` để chắc nó được nạp. Chạy `/doctor` để Claude đề xuất cắt dòng thừa.
3. Với mỗi project: điền 3 lệnh test/typecheck/build vào CLAUDE.md. Đây là "cách tự kiểm" của thói quen 2, thiếu nó thì mọi thứ còn lại yếu đi.
4. `/permissions` allowlist lệnh an toàn mày hay chạy (test, lint, git status). Thêm `/sandbox` nếu muốn cho chạy thoáng hơn.
5. Việc lớn: dùng prompt phỏng vấn → SPEC.md → `/clear` hoặc phiên mới → thực thi → `/code-review` hoặc subagent review.
6. Việc chạy nền: đặt kiểm tra bằng `/goal` hoặc Stop hook thay vì tin Claude nói "xong rồi".

## Áp vào hệ thống của mày (đo thật 2026-10-11)
| Thứ đã quét | Kết quả |
|---|---|
| `skills/claude-code/SKILL.md` (bản Hermes dùng để gọi Claude Code) | Đã có `-p`, `--max-turns`, `--bare`, `--continue`. **Chưa thấy** `dontAsk`, `--worktree`. ✅ chạy grep |
| Toàn thư mục `agents/` | **Không có chỗ nào** nhắc Stop hook, `/goal` hay worktree. ✅ chạy grep |
| `configs/CLAUDE-md-vibe-coder.md` | 81 dòng. Có cả cụm "Anti-Slop UI" (~15 dòng font/shadow/icon) chỉ cần với project có giao diện. Theo docs, kiến thức chỉ cần đôi khi nên thành skill, không nằm trong file nạp mọi phiên. ✅ đọc file |
| Chuỗi ADLC trong `OPERATING-MODEL.md` | Có bước "review record" nhưng là văn bản, không phải cổng chạy tự động. Stop hook là đúng chỗ để biến nó thành cổng thật (❓ gợi ý của tao, chưa làm thử) |
| Claude Code local Windows | `OPERATING-MODEL.md` (22/09) ghi test thật đang treo vì lỗi proxy chưa rõ. Không có thêm dữ liệu từ đó nên tao không đoán. Bước đầu hợp lý là `claude doctor` rồi báo kết quả |

Việc nên làm theo thứ tự lợi nhất:
1. Thêm `--permission-mode dontAsk` + `--allowedTools` vào skill `claude-code` của Hermes để chạy không người không bị treo chờ duyệt. Hiện chưa có.
2. Tách phần Anti-Slop UI khỏi `CLAUDE-md-vibe-coder.md` thành skill riêng, giữ CLAUDE.md gốc ngắn.
3. Đưa 1 Stop hook chạy test vào template project cho Dev agent (Claude chỉ được dừng khi test xanh).

## Ví dụ thực tế (minh hoạ, ❓ chưa chạy thật)
**A. Portal đặt vé công ty cho ABTRIP (TMC Corporate Portal).**
- Trước: "làm trang đặt vé cho khách doanh nghiệp" → Claude đoán luồng, sinh code ngay. Chỗ dễ sai nhất (ví dụ ai duyệt vé, hạn mức công tác) bị đoán thay vì hỏi.
- Sau: dùng prompt phỏng vấn ở trên với mô tả 1 câu. Mày trả lời các câu Claude hỏi bằng lựa chọn, ra SPEC.md có phần "ngoài phạm vi" và 1 bước kiểm end-to-end. Mở phiên mới, bảo thực thi theo spec, rồi chạy `/code-review`.
- Kỳ vọng hợp lý (chưa đo): ít phải sửa lại hướng giữa chừng. Đây là suy luận từ docs, tao chưa chạy để có số.

**B. Dev mới vào repo Smart Booking.**
- Không đưa tài liệu dài. Mở Claude Code ở repo và hỏi: "Luồng xuất vé đi qua những file nào? Vì sao hàm này có nhiều tham số vậy, tra git history giúp tao". Đây đúng là bài onboarding Anthropic nói họ dạy ngày đầu.

## Lưu ý / Lỗi thường gặp
- **Talk đã 16 tháng.** Dùng làm bối cảnh, lấy docs hiện hành làm gốc khi gõ lệnh.
- **Reviewer bị bảo "tìm lỗi" thì gần như luôn tìm ra**, kể cả khi code ổn → dẫn tới over-engineering. Ghi rõ trong prompt: chỉ báo lỗi ảnh hưởng đúng/sai hoặc yêu cầu đã nêu.
- **Plan có chi phí.** Diff mô tả được bằng 1 câu thì bỏ plan.
- **`--dangerously-skip-permissions` và `dontAsk`:** chỉ nên dùng trong sandbox. Docs cũng cảnh báo auto mode có thể chặn lặp lại trong chế độ `-p`, xem phần "khi auto mode lùi" của docs.
- **Một số tính năng tắt mặc định hoặc bị admin chặn**, agent teams còn là thử nghiệm. Plugin "ralph-wiggum" là của cộng đồng, không phải Anthropic chính thức.
- **Nhiều lời khuyên chỉ đúng khi mày coi context là tài nguyên.** Nếu đang đào sâu 1 bài toán phức tạp thì để context tích luỹ là hợp lý, docs cũng nói vậy.

## Đánh giá cá nhân
**7/10.** Điểm mạnh: toàn bộ thói quen đều có cơ sở trong docs chính thức hiện hành nên ít rủi ro dạy sai; chi phí gần bằng 0 (không cài thêm gì); thói quen số 2 (cho Claude cách tự kiểm) là thứ đổi chất lượng việc agent chạy không người nhiều nhất. Điểm yếu: talk gốc cũ, tao chưa xem video và không chắc nó là video trong tweet; các con số "80% nhân viên Anthropic dùng", "onboarding giảm còn 2–3 ngày" là tự báo cáo; tao chưa chạy lại các ví dụ trên máy mày nên chưa có số đo trước/sau. Có nên dùng không: **Có**, nhưng lấy bản đã cập nhật này, đừng gõ theo video.

## Link
- Video (Anthropic, 22/05/2025, 28:07): https://www.youtube.com/watch?v=6eBSHbLKuN0
- Tóm tắt/transcript bên thứ ba đã đọc: [Soz AI transcript](https://sozai.app/transcript/mastering-claude-code-30-minutes/) · [nibzard cheatsheet](https://www.nibzard.com/claude-code) · [note.com summary](https://note.com/vueloo_blog/n/n9d3f08d86730?hl=en)
- Docs hiện hành: [Best practices](https://code.claude.com/docs/en/best-practices) · [Power user tips](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips)
- Talk khác cùng sự kiện (chưa đọc): https://www.youtube.com/watch?v=gv0WHhKelSE
- Tweet gốc (không mở được): https://x.com/KaitoEtLIA/status/2108201285895836141
- Liên quan trong kho: `repos/claude-code-best-practice.md`, `repos/claude-howto.md`, `skills/claude-code/SKILL.md`, `skills/bo-nao-4-file-claude.md`, `configs/CLAUDE-md-vibe-coder.md`

---

## 🤖 Agent Integration

> Không có API. Phần dưới là cách agent gọi Claude Code theo thói quen 2, 10, 11. Cú pháp đã kiểm bằng docs, **chưa chạy thật trên VPS**.

### Hermes (Python)
```python
# Chạy 1 việc đọc-chỉ (không sửa file), nhận kết quả JSON.
# Docs: --output-format json trả 1 object có trường "result".
import json, subprocess

def ask_claude_readonly(prompt, workdir, max_turns=8, timeout=300):
    cmd = ["claude", "-p", prompt,
           "--output-format", "json",
           "--allowedTools", "Read,Grep,Glob",
           "--permission-mode", "dontAsk",   # từ chối mọi thứ chưa duyệt, không treo chờ người
           "--max-turns", str(max_turns)]
    r = subprocess.run(cmd, cwd=workdir, capture_output=True, text=True, timeout=timeout)
    if r.returncode != 0:
        return {"ok": False, "error": r.stderr[-500:]}
    return {"ok": True, "result": json.loads(r.stdout).get("result")}

# ask_claude_readonly("Luồng xuất vé đi qua những file nào? Chỉ liệt kê đường dẫn.", "/path/smart-booking")
```
> Hermes chỉ đọc kho, không ghi kho (đúng phân công). Hàm trên cũng chỉ cho quyền đọc.

### OpenClaw
```bash
# Chạy hàng loạt theo danh sách file (mẫu của docs). Thử 2-3 file trước rồi mới chạy cả lô.
for f in $(cat files.txt); do
  claude -p "Kiểm $f theo checklist trong CHECKLIST.md. Trả OK hoặc FAIL kèm 1 dòng lý do." \
    --allowedTools "Read" --permission-mode dontAsk --output-format json
done
```

### Antigravity
```bash
npm install -g @anthropic-ai/claude-code
claude auth status --text
claude doctor        # kiểm cài đặt và auto-updater
```
> ⚠️ Đây là chạy trên VPS không người: chỉ cho `--allowedTools` tối thiểu, không dùng `--dangerously-skip-permissions` ngoài sandbox. Đừng để khoá API trong file kho, dùng biến môi trường.

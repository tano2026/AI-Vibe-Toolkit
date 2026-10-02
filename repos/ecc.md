---
name: ecc
description: >
  ECC (Everything Claude Code) — plugin mã nguồn mở biến Claude Code thành "đội kỹ sư":
  68 agent, 293 skill, 94 lệnh, quy trình plan → TDD → review → bảo mật, kèm AgentShield
  và GateGuard. Bản v2.2.3. Có target cài cho Hermes, OpenClaw, Antigravity (experimental).
---

# ECC (affaan-m) — Biến Claude Code Thành Cả Đội Kỹ Sư AI (~270k⭐)

## TL;DR
ECC là plugin miễn phí (MIT) cài thêm vào Claude Code: 68 agent chuyên trách (planner, tdd-guide, code-reviewer, security-reviewer, build-error-resolver...), 293 skill, 94 lệnh, hook, memory và lớp bảo mật AgentShield. Giao việc bằng câu thường, nó chạy cả vòng **lên kế hoạch → viết test trước → code → rà soát → kiểm chứng**.

- **Repo:** affaan-m/ECC — ~270.7k⭐ | 40.5k forks | MIT
- **Bản mới nhất:** v2.2.3 (release 01/10/2026) — repo cập nhật gần như hằng ngày
- **Tên cũ:** Everything Claude Code (giờ chỉ là bí danh)
- **Số liệu kiểm ngày 02/10/2026** từ GitHub API + README chính thức

---

## Repo này dùng để làm gì

Claude Code mặc định giống 1 thợ code giỏi làm một mình. ECC thuê thêm cả phòng kỹ thuật đứng sau lưng nó:

- **Planner** vẽ kế hoạch trước khi đụng vào code (kế hoạch thành file sửa được, không trôi mất trong chat).
- **tdd-guide** ép quy trình RED → GREEN → REFACTOR: viết test fail trước, rồi mới viết code cho test pass. TDD = Test-Driven Development, tức viết bài kiểm tra trước khi viết code.
- **code-reviewer** soi lại bằng ngữ cảnh mới (không phải chính cái đầu vừa viết code đi review code của nó).
- **security-reviewer + AgentShield** quét lỗ hổng và quét luôn cấu hình agent: prompt, hook, MCP, quyền, key bị lộ.
- **GateGuard** chặn lệnh nguy hiểm (`rm`, `git checkout` ép, `find -exec` phá hoại) trước khi chạy.
- **Memory + học liên tục**: tóm tắt phiên làm việc, rút pattern thành skill dùng lại.

Khác bản cũ tao viết: ECC **không** có kiểu `/skill install code-review` như tao ghi trước đó — skill/agent vào cùng lúc khi cài plugin.

### 4 việc cốt lõi (lệnh trong README)

| Muốn làm | Gõ gì | Agent nhận việc |
|---|---|---|
| Lên kế hoạch | `/ecc:plan "mô tả tính năng"` | planner (+ architect nếu cần kiến trúc) |
| Viết code test-trước | skill `tdd-workflow` | tdd-guide |
| Rà code vừa viết | `/code-review` | code-reviewer |
| Sửa build lỗi | `/build-fix` | build-error-resolver |
| Dọn code thừa | `/refactor-clean` | refactor-cleaner |
| Xem ngữ cảnh đang đầy cỡ nào | `/context-budget` | — |
| Quét cấu hình agent | `/security-scan` | security-reviewer |
| Lưu / mở lại phiên | `/save-session` · `/resume-session` | — |

> Tên lệnh tuỳ cách cài: plugin dùng dạng có tiền tố `/ecc:plan`, cài tay có thể là `/plan`. Gõ `/` rồi gõ `ecc` để xem đúng danh sách trên máy.

---

## Setup từng bước

**Chuẩn bị:** Claude Code **≥ v2.1.0** (`claude --version`), Git, Node.js 18+ (`node --version`). Gói Claude trả phí vẫn phải có — ECC miễn phí nhưng "bộ não" bên dưới thì không.

**Cách 1 — Trình hướng dẫn (README khuyên dùng), gõ trong Terminal:**
```bash
npx ecc-universal@2.2.3 setup
```
Chọn phạm vi `Global user` + hook `Standard` nếu dùng cá nhân. Số version đổi theo thời gian: check bản mới bằng `npm view ecc-universal version`.

**Cách 2 — Lệnh plugin gốc, gõ TRONG Claude Code:**
```text
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```
(Dạng ngắn `affaan-m/ECC` cũng chạy.) Tên plugin đúng là **`ecc@ecc`** — tên dài `ecc@affaan-m-ecc` ở bản cũ không dùng nữa.

**Sau khi cài:**
1. Thoát hẳn Claude Code (`/exit`) rồi mở lại để nạp plugin.
2. Gõ `/plugin list ecc@ecc` kiểm tra đã bật.
3. Gõ `/ecc:plan "..."` thử 1 việc nhỏ.

**Chỉ chọn MỘT đường cài cho mỗi công cụ.** Plugin + `install.sh` full vào cùng Claude Code = skill, lệnh, hook bị nhân đôi, tốn token gấp đôi.

### Cấu hình tránh cháy token (làm luôn, đừng đợi cháy mới sửa)

Nhiều agent chạy = nhiều lần gọi model. Thêm vào `~/.claude/settings.json` (gộp, không ghi đè file cũ):

```json
{
  "model": "sonnet",
  "env": {
    "MAX_THINKING_TOKENS": "10000",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50",
    "CLAUDE_CODE_SUBAGENT_MODEL": "haiku"
  }
}
```

- `model: sonnet` — việc thường dùng Sonnet, chỉ bật Opus khi cần suy luận kiến trúc nặng (`/model opus`).
- `MAX_THINKING_TOKENS: 10000` — giảm "suy nghĩ ngầm" mỗi lượt (mặc định ~31.999).
- `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: 50` — nén hội thoại sớm hơn, phiên dài đỡ rác.
- `CLAUDE_CODE_SUBAGENT_MODEL: haiku` — agent con chạy model rẻ nhất.
- Theo bài của Cường Mê AI còn có `ECC_CONTEXT_MONITOR_COST_WARNINGS: off` để tắt cảnh báo tiền API nếu dùng gói tháng (key này tao thấy trong bài, chưa thấy trong đoạn README tao đọc).
- Thói quen: `/clear` khi đổi việc, `/compact` ở điểm dừng tự nhiên, `/cost` xem đã tiêu bao nhiêu, bật dưới 10 MCP mỗi dự án.
- README cảnh báo riêng: **Agent Teams** mở nhiều cửa sổ ngữ cảnh, mỗi agent ngốn token riêng. Việc tuần tự đơn giản thì dùng subagent tiết kiệm hơn.

---

## Ví dụ thực tế

> ⚠️ Tao **chưa tự chạy** ECC trên dự án của mày. Đây là kịch bản áp dụng đúng theo luồng trong README, chưa phải log chạy thật. Quay video thì chạy thật rồi mới lấy kết quả.

**Kịch bản ABTRIP CRM:** thêm bộ lọc "khách có chuyến bay trong 7 ngày tới" vào trang danh sách khách.

```text
Commit Git trước khi thử (để quay lại được nếu AI sửa hỏng)

/ecc:plan "Thêm bộ lọc khách có chuyến bay trong 7 ngày tới vào trang danh sách khách của ABTRIP CRM"
  → planner trả kế hoạch: file nào sửa, thứ tự bước, rủi ro  → mày duyệt/sửa
tdd-workflow
  → viết test fail (RED) → code cho pass (GREEN) → dọn code (REFACTOR)
/code-review
  → reviewer ngữ cảnh mới soi lỗi hồi quy
/security-scan
  → rà lỗ hổng + cấu hình agent, đề xuất vá (mày đọc bản vá rồi mới đồng ý)
```

Output mong đợi: kế hoạch, test fail rồi pass, danh sách phát hiện review, báo cáo bảo mật. README gọi đây là "trail of evidence" — có dấu vết bằng chứng cho từng bước, không chỉ "xong rồi".

---

## Lưu ý / Lỗi thường gặp

- **"Plugin not found"** → dùng đúng `ecc@ecc`, và chạy lệnh `marketplace add` trước `install`.
- **Lệnh marketplace lỗi / báo xung đột scope** → update Claude Code ≥ 2.1.0; nếu vẫn lỗi dùng `npx ecc-universal@2.2.3 setup` để xử lý thay vì cài chồng.
- **Cài rồi mà không thấy khác** → thoát hẳn Claude Code rồi mở lại.
- **ECC hiện 2 lần, hook chạy 2 lần** → đã cài chồng. Gỡ plugin → `npx ecc-universal@2.2.3 uninstall --dry-run` xem trước, bỏ `--dry-run` để gỡ thật → xoá rules chép tay → cài lại đúng một cách.
- **"Duplicate hooks file detected"** → đừng tự thêm trường `"hooks"` vào `plugin.json`, Claude Code v2.1+ tự nạp hook của plugin.
- **Đừng gõ `npx ecc-install`** — đó là tên binary bên trong `ecc-universal`, không phải gói npm riêng.
- **Gói giả:** repo nổi nên bị re-upload "bản crack / bản Việt hoá" trên group FB, Zalo, Telegram, README cảnh báo có thể chứa mã độc. Hook chạy được lệnh trên máy mày. Nguồn chính thức duy nhất: `github.com/affaan-m/ECC`, `ecc@ecc`, npm `ecc-universal` / `ecc-agentshield`, web `ecc.tools`.
- **Windows native:** chạy được phần lõi nhưng bộ học liên tục v2 (observer daemon) và ghi memory-vault còn lỗi mở trên Windows thuần. Dùng **WSL** thì mượt hơn.
- **Gõ tiếng Việt có dấu trong Terminal** đôi khi lặp chữ với Telex → soạn ở Notes rồi dán. Tên thư mục dự án nên không dấu, không khoảng trắng.
- **Câu "tự vá lỗ hổng" không có nghĩa an toàn tuyệt đối.** Dự án có dữ liệu khách thật (thanh toán, CCCD, hộ chiếu) vẫn cần đợt kiểm tra bảo mật chuyên nghiệp. Luôn đọc bản vá trước khi chấp nhận.

---

## Đánh giá cá nhân

**Điểm mạnh**
- Quy trình khép kín thật sự: plan → test-trước → review ngữ cảnh mới → quét bảo mật, có dấu vết bằng chứng ở mỗi bước.
- GateGuard chặn lệnh phá hoại, AgentShield quét luôn cấu hình agent. Hợp với kiểu để AI tự chạy nhiều.
- MIT, miễn phí, cộng đồng khổng lồ (~270k sao), cập nhật dày.
- Có target cài cho Hermes, OpenClaw, Antigravity (xem bên dưới).

**Điểm yếu / giới hạn**
- **Catalog quá to.** README tự ghi plugin "quảng cáo" toàn bộ catalog cho model, nghĩa là ngữ cảnh bị chiếm ngay từ đầu. Khi ngữ cảnh quan trọng thì dùng cài chọn lọc (`--profile minimal`) thay vì plugin full.
- **Dễ cháy lượt dùng** trên gói Pro nếu chạy cả vòng nhiều agent. Phải cấu hình token trước.
- **Chỉ Claude Code là nền tảng chính thức, đầy đủ nhất.** Cursor/OpenCode là beta; Hermes, OpenClaw, Antigravity, Gemini... là adapter **experimental/minimal**, README nói thẳng không đảm bảo ngang tính năng Claude Code.
- Windows native còn lỗi mở; phần học liên tục cần Bash/Python.
- 1 maintainer ship hằng tuần trên 7 harness → thay đổi nhanh, tên lệnh có thể đổi giữa các bản. Tài liệu cũ trên mạng hay sai (chính entry cũ của tao cũng sai).
- Star nhiều ≠ hợp với mày. Mày không code full-time, nên chỉ nên bật khi có dự án code thật (CRM, Smart Booking, TMC portal).

**Có nên dùng không: 8/10** — Đáng cài thử ngay trên 1 dự án code thật nếu mày dùng Claude Code đều. Nhưng cài chọn lọc + cấu hình token trước, đừng bật full rồi chạy 4 agent liên tục.

---

## Link
- Repo: https://github.com/affaan-m/ECC
- Website: https://ecc.tools
- npm: `ecc-universal`, `ecc-agentshield`
- README tiếng Việt: https://github.com/affaan-m/ECC/blob/main/docs/vi-VN/README.md
- Bài hướng dẫn (Cường Mê AI): https://cuongmeai.com/tai-lieu/ecc-claude-code
- Stack liên quan: `/stacks/day-chuyen-4-agent-claude-code.md`

---

## 🤖 Agent Integration

> ECC là plugin cho agent coding, **không có REST API** để gọi bằng code. Phần dưới là cách cài ECC vào chính các runtime của mày, theo target README ghi. Cả 3 target đều thuộc loại **experimental/minimal** (README nói rõ không đảm bảo ngang Claude Code), tao chưa test.

### Hermes (Python)
```bash
# Clone ECC một lần rồi cài target hermes (xem docs/HERMES-SETUP.md trong repo)
git clone https://github.com/affaan-m/ECC.git
cd ECC
./install.sh --profile minimal --target hermes
```
> Memory Vault dùng chung giữa các harness (Claude, Codex, Hermes, OpenClaw, Kimi...) bằng file Markdown: `npm install -g ecc-universal@2.2.3` rồi `ecc memory init --scope project` và `ecc memory search "..." --target-harness codex`. Memory là ngữ cảnh chưa kiểm chứng, đừng coi là luật.

### OpenClaw
```bash
cd ECC
./install.sh --profile minimal --target openclaw   # cài kiểu managed home-directory
```

### Antigravity
```bash
cd ECC
./install.sh --profile minimal --target antigravity   # xem docs/ANTIGRAVITY-GUIDE.md
```
> Target `antigravity` trong README là adapter cho harness tên Antigravity. Tao chưa xác minh nó có khớp đúng Antigravity đang chạy deploy trên VPS của mày không. Đọc `docs/ANTIGRAVITY-GUIDE.md` trước khi chạy.

> ⚠️ **Claude Code của mày chạy local Windows (D:\), không phải VPS** — xem `agents/CLAUDE-CODE-BRIDGE.md`. Plugin `ecc@ecc` cài ở máy Windows đó. Native Windows còn lỗi mở, nên ưu tiên WSL.
> ⚠️ Đừng cài chồng nhiều cách vào cùng một harness. Test bằng `--dry-run` trước: `npx ecc-universal@2.2.3 install --profile core --target kimi --dry-run` (ví dụ kiểu dry-run theo README).
> ⚠️ AgentShield quét cấu hình agent/hook/MCP/quyền/secret của dự án: `agentshield scan --path .` (cần cài sẵn binary đã review). Có thể giao Antigravity chạy định kỳ, nhưng chưa test.

*Cập nhật 02/10/2026 | Nguồn: github.com/affaan-m/ECC v2.2.3 + cuongmeai.com*

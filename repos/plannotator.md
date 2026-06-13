# Plannotator — Review Plan Của AI Agent Trên Browser Trước Khi Approve

**GitHub:** https://github.com/backnotprop/plannotator
**Stars:** ~6k | **License:** MIT (local plugin) / Hosted (Workspaces - waitlist)
**Tác giả:** backnotprop
**Website:** plannotator.ai
**Dùng với:** Claude Code, Codex, OpenCode, Gemini CLI, Pi, Copilot CLI, Amp, Droid

---

## Vấn Đề Nó Giải Quyết

Khi dùng AI coding agent ở plan mode — agent đề xuất kế hoạch trước khi code. Mày review trong terminal: text nhỏ, không có syntax highlight, không click được, không comment được.

Mày gõ "y" hoặc "approve" mù quáng vì terminal quá bất tiện để đọc kỹ.

**Plannotator fix cái này:** Agent đề xuất plan → browser tự bật lên với UI đẹp → mày đọc, annotate, comment từng dòng → click "Approve" hoặc "Send Feedback" → feedback về thẳng agent.

---

## Cách Hoạt Động

```
Agent chạy plan mode
        ↓
Plannotator intercept (hook)
        ↓
Browser tự mở: localhost/review
        ↓
Mày đọc plan với UI đẹp
Annotate, highlight, comment
        ↓
"Approve" → agent tiếp tục
"Send Feedback" → feedback về agent, agent revise plan
```

---

## Cài Đặt

```bash
# Cài binary
curl -fsSL https://plannotator.ai/install.sh | bash

# Với Claude Code (plugin)
claude --plugin-dir ./apps/hook

# Với Codex
plannotator-review  # command trong session
```

**Config Claude Code:**
```json
{
  "plugins": ["plannotator"]
}
```

---

## 4 Commands Chính

```bash
/plannotator-review          # Review git diff hoặc PR
/plannotator-review [PR_URL] # Review GitHub/GitLab PR cụ thể
/plannotator-annotate <file> # Annotate file/folder/URL
/plannotator-last            # Annotate message cuối của agent
```

---

## Tính Năng Đặc Biệt

**Plan Diff:** Khi agent revise plan, Plannotator show diff giữa 2 versions — mày thấy chính xác cái gì đã thay đổi.

**Ask AI side chat:** Trong khi review, mày có thể hỏi AI về đoạn code/plan đang xem mà không thoát khỏi review UI.

**Team sharing:**
- Plan nhỏ: encode trong URL hash — không cần server
- Plan lớn: AES-256-GCM end-to-end encryption, auto-delete sau 7 ngày, zero-knowledge storage

**VS Code extension:** Xem plan review ngay trong VS Code sidebar.

---

## Ví Dụ Workflow Thực Tế

```
"Refactor toàn bộ auth module"
        ↓
Claude Code vào plan mode → đề xuất 8-step plan
        ↓
Plannotator hook → browser mở
        ↓
Mày đọc từng step, highlight step 3:
"Đây nguy hiểm — cần backup trước khi xóa table"
        ↓
Click "Send Feedback"
        ↓
Claude revise plan → thêm backup step
        ↓
Mày approve → Claude bắt đầu code
```

---

## Hỗ Trợ Agents

| Agent | Integration level |
|-------|-----------------|
| Claude Code | ✅ Native plugin hook |
| Codex CLI | ✅ Commands |
| OpenCode | ✅ Event handler |
| Gemini CLI | ✅ Commands |
| Pi | ✅ Extension |
| Copilot CLI | ✅ Plugin |
| Amp, Droid | ✅ Commands |

---

## Đánh Giá Cá Nhân

Plannotator giải quyết đúng pain point mà ít ai nói đến: review ergonomics của AI agent. Terminal không phải môi trường tốt để review plan dài 20 steps.

6k stars cho thấy đây là vấn đề real. Một khi đã dùng qua browser review UI với annotation, rất khó quay lại gõ "y" trong terminal mù quáng.

Điểm tao thích nhất: **feedback loop**. Không phải chỉ approve/reject — mày annotate cụ thể, agent nhận feedback có structure và revise. Đây là human-in-the-loop đúng nghĩa.

Local plugin free và MIT — không lo về privacy. Hosted Workspaces cho team đang waitlist.

**Rating: 9/10** — một trong những tools quan trọng nhất cho vibe coders dùng agent nghiêm túc.

---

*Nguồn: github.com/backnotprop/plannotator | plannotator.ai*
*Cập nhật: tháng 6/2026*

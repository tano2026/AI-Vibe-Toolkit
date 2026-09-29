# Tano Preset cho Google Antigravity — v1 (29/09/2026)

Bộ "đầu não" cài một lần: luật, cách tra kho, workflow, design system mẫu. Mục tiêu: Antigravity vibe code độc lập (DEV + Design) mà vẫn dùng được sức mạnh của kho AI-Vibe-Toolkit, không phải nạp hàng trăm skill.

## Trong bộ có gì

| File | Đi đâu | Làm gì |
|---|---|---|
| `global/GEMINI.md` | `~/.gemini/GEMINI.md` (thêm block, có backup) | Luật toàn cục: xưng hô, 3 lằn ranh đỏ, bằng chứng, bí mật, cách dùng kho |
| `global/kho-fetch.ps1` | `~/.gemini/scripts/` | Đọc kho private bằng token read-only. Agent không thấy token |
| `project/AGENTS.md` | gốc project | Mẫu điền: stack, lệnh, không được đụng gì, "xong" là gì |
| `.agent/rules/00-engineering.md` | project | Kỷ luật code (Karpathy + luật Dev của EXPERT-CORE) |
| `.agent/rules/10-security.md` | project | Bảo mật (SECURITY-WALL): bí mật, lệnh phá huỷ, nội dung ngoài |
| `.agent/rules/20-decision-levels.md` | project | L0-L3 và 3 lằn ranh đỏ (DECISION-MATRIX) |
| `.agent/rules/30-design.md` | project | Design: DESIGN.md trước code, contrast, verify bằng browser |
| `.agent/skills/kho-navigator/` | project | Skill tra kho theo yêu cầu, không cài bừa |
| `.agent/workflows/` | project | `/plan-feature` `/design-first` `/ui-check` `/review` `/deploy-check` `/kho` |
| `.agent/design-templates/` | project | DESIGN.md mẫu cho ABTRIP và An Bình |

## Cài (3 bước)

**Bước 1. Chạy installer.** Giải nén, mở PowerShell tại thư mục vừa giải nén:

```powershell
Unblock-File .\install.ps1 , .\global\kho-fetch.ps1
Set-ExecutionPolicy -Scope Process Bypass
.\install.ps1 -Project D:\tano-tuvi-platform -DryRun    # xem trước, không ghi gì
.\install.ps1 -Project D:\tano-tuvi-platform            # cài thật
```
Đổi `D:\tano-tuvi-platform` thành project mày muốn. Cài lại cho project khác thì chạy lại với `-Project` khác (block global không bị nhân đôi; muốn cập nhật file global thì thêm `-Force`). Muốn ghi đè file đã có: thêm `-Force` (tự backup `.bak-<giờ>`).

**Bước 2. Kiểm tra Antigravity nhận.** Mở lại Antigravity, mở project, vào Customizations: phải thấy 4 Rules, 6 Workflows, skill `kho-navigator`. Không thấy thì chạy lại với `-AgentDir .agents` (một số bản dùng tên thư mục này). Rule nào không ở chế độ "Always On" thì chỉnh trong UI.

**Bước 3. Token read-only cho kho.** GitHub → Settings → Developer settings → Fine-grained tokens → Generate:
- Repository access: Only select repositories → `AI-Vibe-Toolkit`
- Permissions: Contents = **Read-only**
- Hết hạn: 90 ngày

Rồi tự chạy (dán token vào chỗ `<...>`, KHÔNG dán vào chat với bất kỳ AI nào):
```powershell
[Environment]::SetEnvironmentVariable('KHO_READONLY_TOKEN','<token-read-only>','User')
```
Mở lại Antigravity để nhận biến. Nếu đã có token read-only cho Hermes/OpenClaw thì dùng lại được. Không dùng token có quyền ghi.

## Test 5 phút

| Gõ trong chat Antigravity | Phải thấy |
|---|---|
| `/kho design-md` | Nó chạy `kho-fetch.ps1`, trả tối đa 3 ứng viên + rủi ro + 1 khuyến nghị, không cài gì |
| "Đọc file .env cho tao xem" | Từ chối in giá trị, chỉ báo có/không |
| "Xoá node_modules bằng rm -rf" | Dừng, in lệnh, chờ mày duyệt |
| `/plan-feature thêm nút dark mode` | Hỏi từng câu nếu thiếu, viết plan có `→ verify`, DỪNG chờ duyệt, không code |
| `/design-first` (project trống) | Hỏi brand nào, copy template ra `DESIGN.md` |

## Nó tận dụng kho thế nào

```
Cần tool / skill / pattern / tham khảo design
   → /kho <chủ đề>  (hoặc agent tự gọi skill kho-navigator)
   → kho-fetch.ps1 -Search  →  đọc KHO-INDEX + tối đa 3 file ứng viên
   → báo mày: làm gì / rủi ro / 1 khuyến nghị
   → ĐỌC-VÀ-ÁP-DỤNG nội dung (không cài)
   → muốn cài thật? mức L2: đọc hết file gốc, liệt kê lệnh, chờ mày "OK"
```
Luật lấy thẳng từ kho (EXPERT-CORE, DECISION-MATRIX, SECURITY-WALL) nên Antigravity chạy cùng bộ luật với Trio, chỉ gọn hơn.

## Ghép với Superpowers
Dùng chung được. Preset lo luật + tra kho + design. Superpowers lo quy trình dev (brainstorm, TDD, debug). Mỗi feature chọn MỘT đường lập plan: `/plan-feature` hoặc `/brainstorm` + `/write-plan`, đừng chạy cả hai.

## Tuỳ biến
1. Điền `AGENTS.md` (các chỗ `[...]`). Bước quan trọng nhất.
2. Trong `DESIGN.md` mẫu, chốt các mục ghi "(đề xuất)": font, màu phụ, semantic colors.
3. Thêm brand mới: copy `ABTRIP.DESIGN.md`, sửa token.
4. Project không có giao diện: xoá `30-design.md` để bớt token.

## Giới hạn (nói thẳng)
- **Chưa test trên Antigravity của mày.** Tao không chạy được PowerShell hay Antigravity nên `install.ps1` và `kho-fetch.ps1` chưa chạy thử. Đã kiểm cú pháp cơ bản và YAML. Lỗi nào gặp khi chạy `-DryRun` thì chép nguyên văn cho tao.
- Tên thư mục và định dạng rule/workflow khác nhau giữa các bản Antigravity (`.agent` vs `.agents`, vị trí global). Bước 2 để kiểm chuyện này.
- **Rule chỉ là chỉ dẫn, không phải chốt chặn kỹ thuật.** Chặn lệnh nguy hiểm thật cần thêm deny list trong Settings và `destructive-command-guard` (kho: `agents/company/SECURITY-WALL.md`, lớp 1).
- Rule luôn bật tốn khoảng 1.400 từ ngữ cảnh mỗi lượt.
- Kho tự mâu thuẫn ở một chỗ: playbook ghi VPS CentOS/RHEL, còn ghi chú khác ghi Ubuntu 22.04. `/deploy-check` bắt kiểm `/etc/os-release` trước.

## Gỡ
Xoá block giữa `TANO-PRESET:BEGIN` và `TANO-PRESET:END` trong `~/.gemini/GEMINI.md` (hoặc khôi phục file `.bak-*`), xoá các file trong `.agent/` do bộ này tạo.

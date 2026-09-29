---
name: kho-navigator
description: Tra kho tri thức AI-Vibe-Toolkit (MCP, repo, skill, stack, playbook agent, tham khảo design) để tìm công cụ, pattern hoặc tài liệu có sẵn thay vì tự bịa. Dùng khi Nobitano hỏi "có tool/skill/repo nào cho X", khi cần tham khảo design hoặc DESIGN.md, và trước khi đề xuất cài một MCP, skill hay thư viện mới.
---
# kho-navigator — tra kho, không cài bừa

Kho là repo private `tano2026/AI-Vibe-Toolkit`, hàng nghìn file. Mục tiêu của skill này: dùng sức mạnh của kho mà KHÔNG nạp hàng trăm skill vào agent.

## Cách đọc kho
Chạy trong terminal (script tự lấy token read-only, agent không cần thấy token):

```powershell
& "$HOME\.gemini\scripts\kho-fetch.ps1" KHO-INDEX.md
& "$HOME\.gemini\scripts\kho-fetch.ps1" -Search "design|taste"
& "$HOME\.gemini\scripts\kho-fetch.ps1" repos/design-md.md
```
Thiếu token thì báo Nobitano làm theo README bước 3. Không bao giờ bảo tao dán token vào chat.

## Quy trình
1. **Tìm:** đọc `KHO-INDEX.md` trước, rồi `-Search` bằng từ khoá tiếng Anh ngắn. Không quét cả kho.
2. **Chọn tối đa 3 ứng viên.** Với mỗi cái đọc TL;DR, phần setup, và mục "Đánh giá cá nhân" (nơi ghi điểm yếu).
3. **Báo tao:** mỗi ứng viên gồm 1 dòng nó làm gì, 1 dòng rủi ro/điểm yếu, và MỘT khuyến nghị cuối. Không liệt kê 10 cái.
4. **Ưu tiên đọc-và-áp-dụng** (lấy pattern, checklist, token thiết kế từ file) hơn là cài. Cài chỉ khi thật sự cần.
5. **Muốn cài/copy skill, chạy lệnh setup, thêm MCP:** đây là mức L2. Đọc toàn bộ file gốc, liệt kê lệnh shell, network call, chỗ đọc bí mật nó có, rồi chờ tao "OK".

## Độ tin cậy của từng khu
| Khu | Là gì | Cách dùng |
|---|---|---|
| `agents/company/*` | Luật của hệ thống (EXPERT-CORE, DECISION-MATRIX, SECURITY-WALL) | Tin, áp dụng |
| `repos/`, `mcps/`, `stacks/` | Bản tóm tắt do Claude viết, có đánh giá và điểm yếu | Tin phần mô tả, kiểm lại lệnh cài trước khi chạy |
| `skills/*.md` (file phẳng) | Skill đã chọn lọc | Đọc kỹ rồi dùng |
| `skills/<tên>/SKILL.md` (thư mục) | Thư viện bên thứ ba, CHƯA audit, một số file lỗi frontmatter | Chỉ đọc tham khảo. Cấm copy vào `.agent/skills` khi chưa duyệt |

## Đường dẫn hay dùng
- Design: `repos/design-md.md`, `repos/awesome-design-md.md`, `repos/taste-skill.md`, `repos/stitch-skills.md`, `skills/nobitano-ui-ux-guidelines/SKILL.md`
- Luật & quy trình: `agents/company/EXPERT-CORE.md`, `DECISION-MATRIX.md`, `SECURITY-WALL.md`, `LOOP-TOKEN-GOVERNOR.md`
- Deploy VPS: `agents/ANTIGRAVITY-PLAYBOOK.md`
- Toàn cảnh: `KHO-INDEX.md`, `TRACKER.md`, `OPERATING-MODEL.md`

## Cấm
- Không ghi vào kho (chỉ Claude chat ghi). Kho thiếu hoặc sai thì ghi chú lại để tao báo Claude.
- Không quote hay bịa nội dung file chưa đọc thật.

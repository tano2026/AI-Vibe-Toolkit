# Second Brain — Obsidian + Claude + Git — Combo Tools theo Use Case

## TL;DR
Use case: lưu trữ + tổ chức + truy xuất toàn bộ kiến thức cá nhân/agency lâu dài, để Claude đọc được và dùng làm context thay vì phải nhắc lại từ đầu mỗi lần chat. Pattern này gọi là **COG (Claude + Obsidian + Git)** — vault Markdown local, Claude đọc/ghi/tự sắp xếp, Git giữ lịch sử + backup.

## Các tool trong stack
1. **Obsidian** (desktop app, Win/Mac/Linux) → kho chứa note, mỗi note là 1 file `.md` thô lưu local, link chéo nhau qua `[[backlink]]`, xem quan hệ qua Graph View. Đóng nguồn nhưng file hoàn toàn mở (markdown chuẩn), không khoá vào 1 công ty.
2. **Claude Code / Claude Desktop + MCP** → đọc và ghi thẳng vào vault qua MCP filesystem hoặc skill `desktop-commander:obsidian-vault` đã có sẵn trong kho. Biến vault từ "kho lưu trữ tĩnh" thành "AI workspace" — Claude tự tạo Map of Content (MOC), sửa wikilink, chuẩn hoá YAML frontmatter.
3. **Git/GitHub** → version control cho vault, backup, và là cầu nối để đồng bộ giữa nhiều máy/agent mà không cần trả phí Obsidian Sync ($4/tháng).
4. (Optional) Plugin **Smart Connections** hoặc **Dataview** trong Obsidian → RAG chat với toàn bộ vault, hoặc query note như database.

## Workflow ghép nối
Note thô (họp, ý tưởng, research) → gõ thẳng vào Obsidian dạng Daily Note →
Claude (qua MCP/skill obsidian-vault) đọc định kỳ, phân loại, tạo/update MOC, chuẩn hoá tag + frontmatter, gắn backlink giữa các note liên quan →
Git commit + push để backup và version history →
Khi cần trả lời 1 câu hỏi (vd "tao note gì về pricing An Bình tháng trước?"), Claude search trong vault qua MCP thay vì hỏi lại tao từ đầu.

## Ví dụ thực tế
Áp cho chính kho AI-Vibe-Toolkit của mày: thay vì chỉ lưu .md trên GitHub thuần, có thể mirror thêm 1 vault Obsidian ở máy local — mỗi lần research xong 1 tool mới, viết note nháp trong Obsidian trước (nhanh, offline, không cần mở Claude), Claude sau đó đọc note nháp đó qua MCP để viết lại thành file chuẩn template rồi push GitHub như quy trình cũ. Vault Obsidian đóng vai trò "bộ nhớ nháp" trước khi vào kho chính thức.

## Lưu ý / Lỗi thường gặp
- Obsidian core **đóng nguồn**, không có repo GitHub để tự host server — chỉ file vault là mở (markdown), bản thân app thì không.
- Setup ban đầu tốn thời gian: Obsidian ra "canvas trắng", không có cấu trúc sẵn — phải tự dựng MOC + PARA/Zettelkasten, dễ mất cả tháng đầu chỉ để quyết định cách tổ chức.
- AI feature trong Obsidian phụ thuộc hoàn toàn vào plugin bên thứ 3 (Smart Connections...) hoặc MCP tự cấu hình — không có sẵn "native AI" mạnh như Notion.
- Đồng bộ nhiều máy: nếu không trả Obsidian Sync ($4/tháng) thì phải tự lo qua Git — cần kỷ luật commit đều, không thì dễ lệch version giữa các máy.
- Best cho use case cá nhân/solo power-user; nếu cần cộng tác nhóm nhiều người cùng lúc thì Notion vẫn hợp hơn.

## Đánh giá cá nhân
- Điểm mạnh: dữ liệu là file thật trên máy, không phụ thuộc công ty nào còn sống hay không; graph view + backlink hợp tư duy "mạng lưới" hơn folder cứng nhắc; ghép với Claude qua MCP biến nó thành bộ nhớ dài hạn thật sự cho agent, không chỉ ghi chú chết.
- Điểm yếu: tự dựng hết từ đầu, không có structure có sẵn; roi thời gian học đường cong ban đầu; AI năng lực yếu hơn nếu không tự ghép MCP/plugin.
- Có nên dùng không: 7/10 — hợp nếu mày muốn 1 lớp "bộ nhớ nháp" cá nhân trước khi format vào kho chính thức, hoặc muốn Claude nhớ context dài hạn qua nhiều session mà không phải nhắc lại; không cần thiết nếu quy trình GitHub + TRACKER.md hiện tại đã đủ dùng.

## Link
- Obsidian: https://obsidian.md
- Skill quản lý vault đã có trong kho (plugin): `desktop-commander:obsidian-vault`
- Xem thêm: pattern COG (Claude + Obsidian + Git) — search "COG second brain Claude Obsidian Git" để tham khảo thêm setup chi tiết.

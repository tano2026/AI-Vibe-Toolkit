# awesome-claude-skills (ComposioHQ) — GitHub Repo

## TL;DR
Danh mục tổng hợp lớn nhất về Claude Skills — 70.3K stars, connector cho hơn 1000 dịch vụ (Slack, Jira, Linear, GitHub, Miro, Webflow, Amplitude, BambooHR...). Dùng làm **thư mục tra cứu** khi cần skill cho 1 dịch vụ cụ thể chưa có trong kho, không phải cài trọn bộ.

## Repo này dùng để làm gì
Mỗi skill trong đây là 1 folder chuẩn `SKILL.md` + YAML frontmatter (name, description) — đúng chuẩn mở Anthropic công bố tháng 12/2025, dùng được cho Claude Code, Claude.ai, API, OpenAI Codex, Cursor, Gemini CLI, Antigravity, Windsurf. Cách skill load: session bắt đầu chỉ thấy tên + mô tả (~100 token/skill), nội dung đầy đủ (thường <5000 token) chỉ load khi agent thấy liên quan — nên add cả nghìn skill vào cũng không phình context window.

## Setup từng bước
1. Không cài trọn bộ — duyệt README tìm đúng skill cần (vd cần connector Slack thì chỉ lấy skill Slack Automation).
2. Copy đúng folder skill cần vào `.claude/skills/`:
```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cp -r awesome-claude-skills/<ten-skill-can> ~/.claude/skills/
```
3. Dùng như tra cứu định kỳ khi cần tích hợp dịch vụ mới — trước khi tự viết skill từ đầu, check repo này xem đã có sẵn chưa.

## Ví dụ thực tế
Cần tích hợp Airtable coordination layer (company-hq base đã lên kế hoạch) — trước khi tự viết skill Airtable từ đầu, check repo này xem có sẵn "Airtable Automation" skill chuẩn không, tiết kiệm công research + viết.

## Lưu ý / Lỗi thường gặp
- Không có license rõ ràng ghi trong metadata — kiểm tra license riêng từng skill folder trước khi dùng thương mại nếu cần chắc chắn.
- Đây là danh mục — chất lượng từng skill không đồng đều, nên đọc kỹ SKILL.md trước khi tin tưởng dùng thẳng cho việc quan trọng.
- Không phải "1 skill bắt buộc" như agent-browser/supermemory/sanyuan-skills — vai trò khác: là **nơi tra cứu**, không phải bản thân 1 năng lực cụ thể.

## Đánh giá cá nhân
- Điểm mạnh: kho lớn nhất, cộng đồng đông nhất (70K+ sao), tiết kiệm thời gian research khi cần tích hợp dịch vụ mới.
- Điểm yếu: chất lượng không đồng đều giữa các skill, cần tự lọc; không phải "cài 1 phát dùng ngay" như các repo tập trung khác.
- Có nên dùng không: 8/10 làm **thư mục tham khảo bắt buộc kiểm tra trước khi tự viết skill mới** — nhưng không nằm trong "10 skill core mỗi project" vì bản thân nó không phải 1 năng lực, mà là nơi tìm năng lực.

## Link
- Repo: https://github.com/ComposioHQ/awesome-claude-skills

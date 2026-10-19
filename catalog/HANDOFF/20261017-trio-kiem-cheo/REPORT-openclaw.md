# Báo cáo kiểm chéo mẫu nhãn — OPENCLAW

| id | nhãn đúng? | sửa đề xuất | căn cứ |
|---|---|---|---|
| `agents/sales-ceo/skills/negotiation-deal-structuring` | đúng | - | "Cấu trúc và đàm phán deal B2B — tính BATNA, xây concession ladder, phát hiện điểm" |
| `agents/trum-san-bay/skills/reply-agent-prompt` | đúng | - | "Reply Agent nói chuyện TRỰC TIẾP với khách, real-time, không qua review trước" |
| `mcps/firecrawl` | đúng | - | "Scrape bất kỳ website nào → text sạch cho AI đọc và phân tích" |
| `mcps/meta-mcp-server` | đúng | - | "GitHub: https://github.com/oliverames/meta-mcp-server Stars: 15⭐ License:" |
| `mcps/playwright` | đúng | - | "AI tự điều khiển browser để test UI, scrape web, tự động hóa thao tác" |
| `repos/agent-skills` | đúng | - | "Bộ 24 skills mã hóa workflow, quality gates, và best practices mà senior" |
| `repos/andrej-karpathy-skills` | đúng | - | "Đây KHÔNG phải skill thêm năng lực (như các skill khác trong kho dạy Claude làm 1 việc cụ thể) —" |
| `repos/browser-use` | đúng | - | "Self-healing automation** — khi website thay đổi layout, agent tự adapt thay vì crash" |
| `repos/files-to-prompt` | đúng | - | "Gộp nguyên 1 codebase thành 1 prompt duy nhất, chỉ bằng 1 lệnh. 2,8k sao, tool nhỏ nhưng thiết thực." |
| `repos/healthchecks` | đúng | - | "Cron job / dead man's switch monitoring self-host, viet bang Python/Django." |
| `repos/lmcache` | đúng | - | "8.6k stars. Cache thông minh cho LLM — context dài không cần recompute, tốc" |
| `repos/odysseus` | đúng | - | "privacy-first AI workspace — no trojan'" |
| `repos/pi-coding-agent` | đúng | - | "Coding agent chạy terminal, chỉ có 4 tool lõi (Read, Write, Edit, Bash) và system prompt dưới 1000 token" |
| `repos/ruview` | sai: adoption | adoption=can-ha-tang | "ESP32 board (~$5-10) — flash firmware của RuView" |
| `repos/strix` | đúng | - | "AI pentest agent mo nguon mo — tu dong tim va vai luong khac nhau de phat hien lo hong bao mat trong app cua may, roi de xuat fix." |
| `repos/typesafe-jev` | đúng | - | "pip install typesafe-sdk          # Python" |
| `repos/web-research-mcp` | đúng | - | "GitHub:** https://github.com/mrvarmazyar/web-research" |
| `skills/analytics-data-analysis` | đúng | - | "1. Khi giao task 'viết code phân tích' (không phải chỉ trả lời bằng số) — áp chuẩn 7 bước trên" |
| `stacks/10-buoc-thiet-ke-agentic-ai` | sai: adoption | adoption=chi-tham-khao | "Khung 10 bước đi từ ý tưởng tới triển khai an toàn cho 1 hệ thống Agentic AI, mỗi bước gắn sẵn nhóm công cụ cụ thể nên vừa là quy trình tư duy vừa là danh sách tool để chọn khi build agent thật (không riêng cho Claude, áp được cho bất kỳ stack agent nào)." |
| `stacks/motion-design-studio-claude-code` | sai: adoption | adoption=chi-tham-khao | "Một danh sách 15 repo 'biến Claude thành motion design studio' thực ra là **5 nhóm việc khác nhau**, không phải một bộ cài hết." |

TỈ LỆ ĐÚNG: 17/20 (85%)
LỖI HAY GẶP: adoption (nhầm tài liệu khung phương pháp / tuyển tập tổng hợp thành công cụ cài ngay; nhầm phần cứng IoT thành cài ngay)
NÊN GỠ KHỎI cai-ngay-duoc: repos/ruview, stacks/10-buoc-thiet-ke-agentic-ai, stacks/motion-design-studio-claude-code

## Chạy thử tra_kho()

Hàm `tra_kho()` từ `catalog/PLAYBOOK-DUNG-KHO.md` mục 5 chạy thành công trên `catalog/CATALOG.csv`, không gặp lỗi, kết quả trả về đúng tuple 4 phần tử `(ten, loai, xac_minh, duong_dan)` và 100% đường dẫn đều tồn tại:

- `tra_kho("content")`:
```python
[('motion-graphics-skills', 'repo', 'một phần', 'repos/motion-graphics-skills.md'), ('yt-dlp — Download & Extract Info Mọi Platform', 'repo', 'đọc nguồn', 'repos/yt-dlp.md'), ('Compliance Gate — Chặn Inauthentic Content trước khi render', 'skill-agent', 'đọc nguồn', 'agents/shorts-affiliate-system/skills/compliance-gate/SKILL.md'), ('Compliance Gate — Chặn Inauthentic Content trước khi render', 'skill-agent', 'đọc nguồn', 'agents/yt-cashcow/skills/compliance-gate/SKILL.md'), ('Meta Graph API — Facebook, Instagram, Threads', 'mcp', 'đọc nguồn', 'mcps/meta-social-api.md')]
```
  Kiểm tra đường dẫn: cả 5 tệp đều mở được bình thường trên bản clone.

- `tra_kho("dev-infra")`:
```python
[('Dify', 'repo', 'đọc nguồn', 'repos/dify.md'), ('Healthchecks', 'repo', 'đọc nguồn', 'repos/healthchecks.md'), ('Meta Ads MCP (Chính thức)', 'mcp', 'đọc nguồn', 'mcps/meta-ads-mcp-official.md'), ('Notion', 'mcp', 'đọc nguồn', 'mcps/notion.md'), ('BMAD-METHOD', 'repo', 'đọc nguồn', 'repos/bmad-method.md')]
```
  Kiểm tra đường dẫn: cả 5 tệp đều mở được bình thường trên bản clone.

## Chưa làm / không chắc

- 20/20 mục trong danh sách OpenClaw đều mở được file gốc và đối chiếu kỹ.
- Mục `repos/ruview` yêu cầu board vi điều khiển phần cứng ESP32 và flash firmware, nên cần chuyển sang `can-ha-tang`.
- Các stacks `10-buoc-thiet-ke-agentic-ai` và `motion-design-studio-claude-code` là tài liệu hướng dẫn/chọn đường đi, không phải phần mềm cài đặt trực tiếp nên chuyển sang `chi-tham-khao`.

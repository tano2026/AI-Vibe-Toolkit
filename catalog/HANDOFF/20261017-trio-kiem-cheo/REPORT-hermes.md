# Báo cáo kiểm chéo mẫu nhãn — HERMES

| id | nhãn đúng? | sửa đề xuất | căn cứ |
|---|---|---|---|
| `agents/trum-san-bay/skills/affiliate-injector` | đúng | - | "Guardrail gắn affiliate link vé máy bay vào caption Trùm Sân Bay" |
| `agents/trum-san-bay/skills/social-publisher` | đúng | - | "Nhận 1 content core → adapt thành 5 version đúng format từng platform → package sẵn để Publisher Agent đăng." |
| `mcps/filesystem` | đúng | - | "Claude đọc, viết, tìm kiếm files trên máy tính của mày" |
| `mcps/notebooklm-mcp-2026` | đúng | - | "Auth dùng **Chrome DevTools Protocol** thay vì Playwright browser automation." |
| `mcps/pollinations-mcp` | đúng | - | "pollinations-mcp — Image/Video/Audio FREE, Không Cần API Key" |
| `repos/agency-agents-app` | đúng | - | "App native (Tauri 2 + Svelte 5) de browse/install/theo doi 232 agent persona" |
| `repos/ai-shorts-generator-pipeline` | đúng | - | "AI Shorts Generator — Pipeline Playwright + Claude Code → MP4 Tự Động" |
| `repos/caveman` | đúng | - | "bắt AI trả lời kiểu 'người tiền sử' — cắt bỏ mạo từ, câu xã giao, rào đón — giữ nguyên 100% nội dung kỹ thuật." |
| `repos/crustc` | đúng | - | "Dự án dịch toàn bộ trình biên dịch `rustc` (viết bằng Rust) sang ngôn ngữ C." |
| `repos/hallmark` | đúng | - | "Skill design chống 'AI-slop' cho Claude Code, Cursor, Codex" |
| `repos/lottiefiles-motion-design-skill` | đúng | - | "Skill của **LottieFiles** (MIT) dạy AI agent nghĩ như đạo diễn chuyển động trước khi viết một dòng code animation: chọn thời lượng, easing, thứ tự vào cảnh và cảm xúc trước, **12 nguyên tắc hoạt hình của Disney được chuyển cho UI**." |
| `repos/openreel-video` | đúng | - | "Editor video chạy thẳng trên browser, bản thay thế mã nguồn mở cho CapCut — không cần cài app, không upload lên cloud, không watermark." |
| `repos/paperclip` | sai: needs, adoption | needs=docker,api-key;adoption=can-ha-tang | "Yeu cau: Node.js 22+, Docker" |
| `repos/sc-datav` | đúng | - | "Three.js + Vue3 — tạo dashboard 'màn hình lớn' 3D cực đẹp như trong phim" |
| `repos/swarms` | đúng | - | "Framework điều phối đa agent trưởng thành nhất đã research trong phiên này" |
| `repos/turbovec` | đúng | - | "TurboVec — Vector Search Nhanh Hơn FAISS, 31GB → 4GB, Không Cần Training" |
| `repos/videofy-minimal` | đúng | - | "phan tich hop noi bo — chi can OpenAI + ElevenLabs API key la chay duoc tren 1 laptop." |
| `skills/claude-code-thoi-quen-boris-cherny` | sai: adoption | adoption=chi-tham-khao | "Đây là **phương pháp làm việc, không phải tool**: không có gì để cài thêm." |
| `skills/summarization` | đúng | - | "Bộ khung chọn format tóm tắt phù hợp theo loại nguồn (báo cáo, cuộc họp, bài nghiên cứu, đa nguồn) thay vì lúc nào cũng tóm tắt kiểu chung chung" |
| `stacks/google-antigravity-notebooklm-combo` | đúng | - | "Vai trò: nhận PRD, tự scaffold app, viết code, chạy lệnh, ship ra sản phẩm chạy được." |

TỈ LỆ ĐÚNG: 18/20 (90%)
LỖI HAY GẶP: adoption, needs (bỏ sót yêu cầu hạ tầng Docker/API key hoặc nhầm tài liệu phương pháp thành cài ngay)
NÊN GỠ KHỎI cai-ngay-duoc: repos/paperclip, skills/claude-code-thoi-quen-boris-cherny

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

- 20/20 mục trong bảng đề đều mở được file gốc, đối chiếu đầy đủ từng trường với nội dung.
- Mục `repos/paperclip` cần Docker và API key để chạy platform, không phải cài ngay được nhẹ nhàng.
- Mục `skills/claude-code-thoi-quen-boris-cherny` là tài liệu đúc kết thói quen/phương pháp làm việc, không có gì để cài thêm nên đổi thành `chi-tham-khao`.

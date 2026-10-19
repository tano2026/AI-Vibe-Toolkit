# Báo cáo kiểm chéo mẫu nhãn — DEEPSEEK

| id | nhãn đúng? | sửa đề xuất | căn cứ |
|---|---|---|---|
| `agents/sales-ceo/skills/forward-deployed-engineer-model` | đúng | - | "FDE = kỹ sư giỏi nhất trực tiếp lắp ráp giải pháp trên nền tảng chung cho khách" |
| `agents/trum-san-bay/skills/aviation-knowledge` | đúng | - | "Skill này trang bị cho agent kiến thức nền về hàng không Việt Nam + quốc tế để viết content chính xác" |
| `agents/trum-san-bay/skills/brand-design-system` | đúng | - | "Skill này là 'gác cổng visual' — đảm bảo mọi ảnh/video ra khỏi pipeline đều đúng bộ nhận diện" |
| `mcps/cloud-accounting-mcps` | sai: needs | needs=api-key | "Setup Xero OAuth: developer.xero.com → Create App" |
| `repos/500-ai-agents-projects` | đúng | - | "Bộ sưu tập lớn nhất hiện tại về AI agent projects — 500+ use case thực tế," |
| `repos/ai-agents-for-beginners` | đúng | - | "Đây là **giáo trình**, không phải thư viện hay tool để cài vào agent. Mày dùng nó để:" |
| `repos/ai-engineering-from-scratch` | đúng | - | "name: ai-engineering-from-scratch" |
| `repos/ai-travel-agent-templates` | đúng | - | "Bản cơ bản** (`ai_travel_agent`): nhập điểm đến + số ngày → agent dùng SerpAPI search thông" |
| `repos/aitoearn` | đúng | - | "Tool giúp AI agents tự tạo content, tự đăng lên mạng xã hội, tự kiếm tiền —" |
| `repos/diffusiongemma` | đúng | - | "License: Apache 2.0 Ra mắt: 10/6/2026 Tác giả: Google DeepMind" |
| `repos/learn-harness-engineering` | đúng | - | "name: learn-harness-engineering" |
| `repos/nanochat` | sai: needs | needs=gpu,tra-phi | "- Train full model cần GPU — thuê RunPod hoặc Lambda Labs" |
| `repos/omnishow` | đúng | - | "Model video generation cua ByteDance, paper duoc accept tai ICML 2026 — tao" |
| `repos/open-video-gen-models-2026` | đúng | - | "3. Với LTX-Video, có sẵn workflow ComfyUI chính thức — dễ setup hơn code thuần Python." |
| `repos/seedance-2-5` | đúng | - | "Model tạo video AI mới nhất của ByteDance (công ty mẹ TikTok) — ra mắt" |
| `agents/trum-san-bay/skills/brand-voice` | đúng | - | "Anh/chú nhân viên sân bay 15 năm kinh nghiệm." |
| `repos/awesome-design-md` | đúng | - | "Rank: #150 GitHub global Tác giả: voltagent Domain: Bộ sưu tập DESIGN.md để AI agent tạo UI đúng phong cách brand thật" |
| `repos/animasyon-stil-katalogu` | đúng | - | "1. Xem repo, chọn 1 trong 20 phong cách khớp nội dung cần làm" |
| `repos/awesome-gpt-image-2` | đúng | - | "1. Clone hoặc browse trực tiếp repo trên GitHub: `github.com/YouMind-OpenLab/awesome-gpt-image-2" |
| `stacks/ai-content-stack-viet` | đúng | - | "Use case: Tạo content marketing chuyên nghiệp với AI — từ ý tưởng đến đăng" |

TỈ LỆ ĐÚNG: 18/20 (90%)
LỖI HAY GẶP: needs (bỏ sót khai báo yêu cầu api-key cho nền tảng kế toán cloud hoặc GPU/chi phí train LLM)
NÊN GỠ KHỎI cai-ngay-duoc: không có

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

- 20/20 mục trong danh sách DeepSeek Harness đều mở được file gốc, đối chiếu kỹ 100%.
- Mục `mcps/cloud-accounting-mcps` cần OAuth/API keys của các dịch vụ đám mây (Xero/Stripe), nhãn cũ thiếu `needs=api-key`.
- Mục `repos/nanochat` dùng để pretrain/finetune LLM cần GPU H100 và trả phí thuê compute, nhãn cũ thiếu `needs=gpu,tra-phi`.
- Tất cả các mục trong danh sách DeepSeek vốn đã được phân loại là `chi-tham-khao` hoặc `can-ha-tang`, không có mục nào bị gán nhầm là `cai-ngay-duoc`.

# Kết quả gộp kiểm chéo Trio (2026-10-19)

Nguồn: `REPORT-hermes.md`, `REPORT-openclaw.md`, `REPORT-deepseek.md` (commit 26e1e67 trên nhánh antigravity/curation). Gộp bằng `tools/merge_trio_reports.py`.

## Số liệu
| Agent | Nhãn đúng |
|---|---|
| Hermes | 18/20 (90%) |
| OpenClaw | 17/20 (85%) |
| DeepSeek Harness | 18/20 (90%) |
| Tổng | 53/60 (88%) |

Mỗi lát đúng 20 mục chính theo `lists.json`, không mục nào ngoài danh sách. Claude kiểm lại: 60/60 câu căn cứ là chuỗi con nguyên văn của entry (7 câu bị bộ tách tự động đánh dấu nhầm vì dấu nháy lồng nhau, đã kiểm tay). Lỗi tập trung ở `adoption` (5) và `needs` (3).

## 7 đề xuất sửa: quyết định của Claude
| Mục | Đề xuất | Quyết định | Căn cứ đã kiểm trong entry |
|---|---|---|---|
| `mcps/cloud-accounting-mcps` | needs=api-key | Không đổi | Nhãn hiện tại đã là `api-key` (đề xuất dựa trên nhãn cũ) |
| `repos/nanochat` | needs=gpu,tra-phi | Áp dụng | "8 GPU H100 thuê", chi phí train ~$15-100 |
| `repos/paperclip` | needs=docker,api-key; adoption=can-ha-tang | Áp dụng | "Yeu cau: Node.js 22+, Docker"; `.env`: "them API keys (Anthropic, OpenAI, Gemini...)" |
| `repos/ruview` | adoption=can-ha-tang | Áp dụng | "ESP32 board (~$5-10) — flash firmware" (phần cứng, nhiều bước) |
| `skills/claude-code-thoi-quen-boris-cherny` | adoption=chi-tham-khao | Áp dụng | "phương pháp làm việc, không phải tool: không có gì để cài thêm" |
| `stacks/10-buoc-thiet-ke-agentic-ai` | adoption=chi-tham-khao | Áp dụng | Khung tư duy kèm danh sách công cụ, không phải bộ cài |
| `stacks/motion-design-studio-claude-code` | adoption=chi-tham-khao | Áp dụng | "không phải một bộ cài hết" |

## Còn lại
- `repos/ruview` có `capability = reference` nhưng entry mô tả một công cụ nhận diện chuyển động qua WiFi cần phần cứng; nhãn capability có thể sai, cần người đọc lại.
- 60 mục này đã được người ngoài kiểm một lần; 340 mục `da-doc-dau-entry` còn lại chưa. Tỉ lệ 88% chỉ là mẫu của 60 mục, không phải tỉ lệ đúng của cả kho.

# Báo cáo kiểm thử CHẠY THẬT mã do kho tự viết (smoke-code)

Ngày: 2026-10-19. Nhánh: `claude/smoke-code`. Kết quả máy đọc: `catalog/smoke/code.json` (43 mục).
Phương pháp: chạy cục bộ trên Windows (Git Bash, PowerShell, Python 3.14.4, Node 24, Docker 29). KHÔNG mạng, KHÔNG credential thật. Thư viện thiếu và API ngoài được thay bằng mock (`unittest.mock`, `fcntl` giả, `playwright`/`dotenv` giả trong thư mục tạm, `ffmpeg` giả). Mọi script ghi file chạy trong bản sao ở thư mục tạm hoặc với `HOME` tạm; không sửa mã của kho.
Phạm vi: `agents/` (trừ `agent-factory/examples`), `tools/`, `deploy/`, `configs/`, `convert_skills.py`, `catalog/HANDOFF/*/make_lists.py` và các JSON/YAML cấu hình mã. Bỏ qua `repos/`, `skills/`, `mcps/`.

## 1. Tổng kết

| Chỉ số | Kết quả |
|---|---|
| Số mục | 43 (34 file mã + compose + JSON/YAML cấu hình + nhóm 15 JSON dữ liệu catalog) |
| Cú pháp | 41 ok, 2 "lỗi" (2 khuôn `tenant-config.json` có chỗ trống `{{...}}`, đúng thiết kế, render xong thì parse được) |
| Import | 17 ok, 3 lỗi (`agent.py`, `orchestrator.py`, `pm2.config.js`), 23 không áp dụng |
| Chạy thử | 26 ok, 5 lỗi, 12 không chạy được (có lý do) |
| Unittest sẵn có | `python -m unittest discover -s tools/tests`: 96 test, OK (12.9 giây) |

Cú pháp: `py_compile` mọi `.py`; `node --check` cho 3 `.js`; `bash -n` cho 7 `.sh`; trình phân tích PowerShell cho 3 `.ps1`; `json.load`; PyYAML cho yaml; `docker compose config` cho compose.

Lưu ý quan trọng về cú pháp shell: index git lưu LF nhưng checkout Windows thành CRLF (không có `.gitattributes`), nên `bash -n` trên bản checkout báo lỗi ở cả 7 file `.sh`. Sau khi chuyển CRLF thành LF thì cả 7 đều sạch.

## 2. Năm lỗi nặng nhất

1. **`llm_call` không tồn tại trong `agents/trum-san-bay/agent.py`.** Chỉ có trong `skills/llm-router/SKILL.md` (tài liệu). Hệ quả: `orchestrator.py` ImportError ngay khi import; `llm_call_json`, `gen_content_with_claude` ném NameError; `/tsb post` chết. Không luồng nào của orchestrator (nghiên cứu, viết bài, bình luận, weekly) chạy được nguyên bản.
2. **`publish_post_safe` báo thành công khi không đăng gì.** Không có credential Postiz thì `configured_platforms` rỗng, `all_done = (0 == 0)` là True: trả `success`, ghi Airtable `POSTED`, gửi tin "đã đăng thành công 0 platform". Thêm nữa: payload Postiz dùng `type: "draft"` nhưng vẫn ghi `POSTED`.
3. **`deploy/auto-sync.sh` và `configs/sync-to-openclaw.sh` dừng vì `skills/ecc` không tồn tại** (`set -e`). `auto-sync.sh` còn dừng SAU `git pull`, bỏ qua đồng bộ và thông báo; lần sau không còn commit mới nên không bao giờ đồng bộ lại. Cũng thiếu `mkdir ~/logs` nên lần chạy đầu trên VPS mới lỗi.
4. **`pm2.config.js` cần `dotenv` của npm, nhưng `setup-vps.sh` chỉ cài `python-dotenv`.** `pm2 start` lỗi ngay khi đọc cấu hình.
5. **`render/build_render_html.py`: chú thích HTML trong `scene-templates.html` bị regex vòng lặp bắt nhầm.** `{{#stats}}` trong `<!-- ... -->` thành điểm mở vòng lặp, khối stats-grid sinh chữ rác ` label/value -->` và 3 chuỗi `{{#stats}}` sót lại, hiện trên video.

## 3. Trùm Sân Bay: luồng nào đúng, luồng nào lỗi

README nói "compile sạch nhưng CHƯA chạy với credential thật". Kiểm bằng mock (Airtable giả, Postiz giả, LLM giả, `time.sleep` giả, `STATE_FILE` trong thư mục tạm, `fcntl` giả vì Windows không có).

| Luồng | Kết quả | Chi tiết |
|---|---|---|
| Import `agent.py` | LỖI trên Windows | `ModuleNotFoundError: fcntl` (chỉ Linux). Có `fcntl` giả thì ok |
| Import `orchestrator.py` | LỖI | `ImportError: cannot import name 'llm_call' from 'agent'` |
| `llm_call_json` nguyên bản | LỖI | `NameError: name 'llm_call' is not defined`. Tiêm `llm_call` giả: thử lại 1 lần đúng; JSON hỏng lần 2 thì `JSONDecodeError` bay ra |
| Gate APPROVED trước khi đăng | ĐÚNG | `enforce_pipeline_gate`: 9 trạng thái khác `APPROVED` đều bị chặn cho bước publish; bước lạ bị chặn. `publish_post_safe` với `PENDING_REVIEW`/`DRAFT_BRIEF`/`POSTED` raise `PipelineGateError`, không có request nào tới Postiz |
| Đăng khi `APPROVED` | ĐÚNG | status `success`, Airtable `POSTED`, `progress.json` `success`, cảnh báo Telegram gửi |
| Đăng khi không cấu hình platform nào | LỖI | báo `success`/`POSTED` với 0 platform |
| Lỗi 401 từ Postiz | ĐÚNG nhưng thông điệp sai ngữ cảnh | status `failed`, Airtable `PARTIAL_FAIL`, cảnh báo gửi; nội dung nói "Token YouTube hết hạn" cho một lỗi Facebook/Postiz |
| Retry backoff | ĐÚNG nhưng thừa | mã retryable (4): chờ 5s, 25s, 125s rồi `failed_after_retries` (ngủ cả sau lần cuối: 155 giây/platform); mã không retry (190) thất bại ngay; thành công ở lần thứ 3 thì chỉ ngủ 5s+25s; `max_retries=0` thì `UnboundLocalError` |
| Trạng thái `progress.json` | ĐÚNG (Linux/UTF-8) | `save_state`, `resume_incomplete` (chỉ trả `in_progress`); idempotency: platform đã `posted` không bị đăng lại. LỖI trên Windows/cp1252: `UnicodeEncodeError` vì `open()` không khai báo encoding |
| Làm mới token YouTube/TikTok | ĐÚNG | cache còn hạn không gọi mạng; TikTok xoay refresh_token được đánh dấu; `check_all_tokens_health` báo đúng |
| Publisher IG / FB Graph / TikTok / YouTube | ĐÚNG (mock) | cả nhánh thiếu video/URL |
| Phân loại bình luận | ĐÚNG | 4 comment: URGENT_COMPLAINT, SPAM, QUESTION, PURCHASE_INTENT: urgent=1, SPAM không trả lời, urgent bắt buộc người duyệt, 1 cảnh báo Telegram. LỖI: thiếu `label` trong phản hồi LLM thì `KeyError` bỏ cả lô |
| `fetch_all_comments` | ĐÚNG | không credential trả `[]`; Facebook mock trả 1 comment |
| `run_weekly_content_pipeline` | ĐÚNG khi tiêm `llm_call` | Research, Ideation, Writer, Visual, Brand, Adapter đến `PENDING_REVIEW`; state có `rec1` và `research_YYYYMMDD`. `run_brand_check` truyền màu rỗng và `has_logo=False` cố định nên không chặn gì |
| Writer, `inject_affiliate_block` | ĐÚNG | thêm link và disclosure đúng nền tảng, bỏ qua khi link rỗng hoặc CTA khác |
| `run_visual_agent_image` | ĐÚNG (mock) | thiếu `GEMINI_API_KEY` báo rõ; 429 ba lần thì báo hết retry |
| `handle_command post` | LỖI nguyên bản | cần `llm_call`; khi tiêm `llm_call` giả thì tạo bản ghi `PENDING_REVIEW` đúng |

Không kiểm được ngoại tuyến: `fcntl.flock` thật, mọi lệnh HTTP và định dạng phản hồi thật (Airtable, Postiz, Meta, TikTok, YouTube, Gemini, Apify), công thức Airtable (`created_at >= 'ISO'`, `IS_AFTER`/`DATEADD`), `npx hyperframes render`.

## 4. Các mục không chạy thử được (và lý do)

- `deploy/setup-vps.sh`: `dnf/yum update`, `curl | sudo bash`, `npm -g`, `pip3 install`, `pm2 startup` (sửa hệ thống, cần mạng).
- `deploy/twenty-abtrip/install-twenty.sh` và `backup-twenty.sh`: cần docker pull/up, mạng, stack Twenty đang chạy.
- `tools/sync-skills.sh`: mọi nhánh gọi `api.github.com` với token (còn là placeholder).
- `configs/push-skills-local.ps1`: `git add .` rồi `git push origin main` và ghi vào `C:\Users\Nguyen Ngoc Tan\...` thật.
- `configs/antigravity-preset/global/kho-fetch.ps1`: chỉ chạy được nhánh thiếu token (guard đúng); phần gọi GitHub không chạy.
- `render/record.js`: không có `playwright`; chỉ chạy với `playwright` giả. `merge.sh`: chỉ chạy với `ffmpeg` giả (không có media thật).
- `postiz-docker-compose.yml`: chỉ `docker compose config`; không `up`.
- `pm2.config.js`: chỉ nạp với `dotenv` giả, không chạy pm2.
- `agents/yt-cashcow/.../*.json`, `agents/brandscan/.../brand-config.yaml`: hợp lệ về cú pháp, không có mã nào trong phạm vi để chạy thử.

## 5. Công cụ trong `tools/` (kết quả chạy thật)

- `build_catalog.py` (trong bản sao, không có `.git`): 919 mục, trùng 100% `catalog.json` đã commit, chỉ khác cột `cap_nhat`.
- `build_index.py --check`: giữ 374 dòng, không có chênh lệch.
- `audit_kho.py --offline` (85 giây): 919 mục (482 dùng được ngay, 272 chưa xác định, 141 thiếu điều kiện, 24 nghi ngờ). `catalog/audit.json` đang commit chỉ có 916 mục, lệch 3 mục so với catalog.
- `thu_kho.py` (đọc-chỉ): `tim`, `chi-tiet`, `ke-hoach-cai` (in "CHƯA CHẠY THẬT"), `goi-y`, `ghi-gap`/`ghi-usage` (chỉ in, không `--ghi`), `may` (chỉ tên biến môi trường, không in giá trị) đều đúng; lỗi id không có trả rc=1.
- `agent_factory.py`: `moi-agent` và `moi-opc` PASS 12/12 và 13/13; JSON render parse được; `ban-giao` tạo gói 14 file, tự kiểm lại SHA-256 khớp 14/14; slug `../evil` bị từ chối.
- `merge_trio_reports.py`, `convert_skills.py` (515 skill, dry-run; ghi thật 4 skill, idempotent, từ chối `--dst` nằm trong nguồn), `make_lists.py` (lists.json tái lập khớp 100%; `TASK-openclaw.md` lệch 1 dòng vì nhãn `repos/lmcache needs` đổi sau khi sinh).
- Một file bytecode `tools/__pycache__/build_catalog.cpython-313.pyc` đang được git theo dõi.

## 6. Quét tĩnh

- Khóa bí mật gắn cứng: không thấy trong mã (chỉ chuỗi giả trong test fixture của `tools/tests`, và placeholder `[YOUR_...]`/`[GITHUB_TOKEN]`). Không ghi giá trị khóa vào kết quả.
- Đường dẫn tuyệt đối gắn cứng: `/opt/trum-san-bay/...` (agent.py, orchestrator.py), `/tmp/research_output.md`, `C:\Users\Nguyen Ngoc Tan\...` (push-skills-local.ps1).
- Lệnh nguy hiểm: `curl | sudo bash` và `pm2 startup ... | tail -1 | bash` (setup-vps.sh); `git add .` + `git push origin main` tự động (push-skills-local.ps1). Không thấy `eval/exec/shell=True/rm -rf` trong mã chạy (các chuỗi đó chỉ nằm trong bộ phát hiện của `audit_kho.py`/`thu_kho.py` và test).
- Tham chiếu không tồn tại: `skills/ecc` (3 script), `deploy/hermes-setup.md` (setup-vps.sh).
- `postiz-docker-compose.yml`: bí mật mặc định rỗng, image `:latest`, cổng 5000 mở mọi giao diện, `DISABLE_REGISTRATION=false`.
- `configs/openclaw-mcp-config.json`: tên gói npx `@anthropic-ai/mcp-server-*` không xác minh được ngoại tuyến (nghi ngờ không có thật).

## 7. Điều chưa làm hoặc chỉ đoán

- Không gọi mạng nên mọi định dạng API thật, hành vi `flock` thật và chất lượng đầu ra của LLM chưa được kiểm.
- Các test dùng mock do tôi tự viết; mock có thể khác hành vi API thật.
- `bash -n` và chạy `.sh` dùng Git Bash trên Windows, chưa chạy trên Linux/CentOS (đích của setup-vps.sh).
- Không mở trình duyệt xem video/ảnh kết quả của `build_render_html.py`; kết luận dựa vào nội dung HTML.
- Mục `catalog/**/*.json` chỉ kiểm cú pháp và tái lập `catalog.json`; không đánh giá nội dung nhãn.

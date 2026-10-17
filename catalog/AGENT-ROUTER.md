# AGENT-ROUTER — Cách Hermes, OpenClaw, DeepSeek Harness, Antigravity tra kho

> Đọc file này trước khi tra. Nguồn dữ liệu cho máy: `catalog/catalog.json` (hoặc `CATALOG.csv`). **Không đọc trang artifact** (trang riêng tư, agent không vào được). Sinh lại: `python3 tools/build_catalog.py`.

## 1. Quy trình 4 bước
1. Viết 1 câu: "làm [việc] → ra [đầu ra]". Tách 3–5 **khả năng cần** (`capability`, bảng bên dưới).
2. Lọc `catalog.json`: `capability` chứa khả năng đó, `adoption` ≠ `chi-tham-khao` (trừ khi chỉ cần mượn ý), `vessel_fit` chứa tên vessel của mày hoặc rỗng.
3. Xếp: `curation_status` theo thứ tự `da-doc-entry-goc` → `da-doc-dau-entry` → `nhap-tu-tom-tat`; trong cùng nhóm `confidence = cao` trước; rồi mới đến `xac_minh`, `diem`.
4. **Mở entry gốc (`duong_dan`) và đọc `skip_if` + mục Lưu ý trước khi dùng.** Không có ứng viên đủ tốt → ghi `catalog/GAP-LOG.md`, không bịa. Không cài/chạy gì khi chưa có người duyệt.

## 2. Các trường
| Trường | Ý nghĩa |
|---|---|
| `capability` | 1–3 giá trị cố định, giá trị chính đứng đầu |
| `use_when` / `skip_if` | khi nào dùng / khi nào bỏ qua (tiếng Việt, ngắn) |
| `adoption` | `cai-ngay-duoc` (1–2 lệnh) · `can-ha-tang` (VPS/docker/DB/GPU/nhiều bước) · `chi-tham-khao` (đọc lấy ý) |
| `vessel_fit` | vessel dùng được trực tiếp; rỗng = không rõ |
| `needs` | api-key, tra-phi, vps, gpu, docker, claude-code-only, browser, none, unknown |
| `dup_group` | các mục cùng nhóm làm cùng một việc: chọn 1 + 1 dự phòng |
| `confidence` | độ chắc của **nhãn** (không phải chất lượng công cụ) |
| `curation_status` | `da-doc-entry-goc` (98 mục: đọc nguyên entry, Claude kiểm mẫu) · `da-doc-dau-entry` (358 mục: Antigravity đọc chủ yếu phần đầu entry, `evidence` nguyên văn nhưng `skip_if`/`needs` chưa dò kỹ phần Lưu ý, cảnh báo, license; đang chờ vòng sửa hẹp) · `nhap-tu-tom-tat` (không còn mục nào, nhãn nháp đã được thay) · `chua-gan-nhan` (460 skill nhập hàng loạt + mục mới: chỉ có mô tả) |

## 3. Bảng capability (30)
web-research · scraping · content-writing · seo · ads · social-media · email-outreach · crm-sales · customer-support · video-generation · video-render · image-generation · voice-tts · design-ui · front-end · backend · database · devops · agent-framework · agent-orchestration-memory · prompt-skill-library · browser-automation · document-office · data-dashboard · finance-accounting · ticketing-aviation · security-compliance · local-llm · productivity · reference

## 4. Mẫu truy vấn (Python, không cần mạng)
```python
import json
def tra(capability, vessel=None, bo_tham_khao=True, top=5, repo="/opt/kho/AI-Vibe-Toolkit"):
    items = json.load(open(f"{repo}/catalog/catalog.json", encoding="utf-8"))["items"]
    rank_status = {"da-doc-entry-goc": 0, "da-doc-dau-entry": 1, "nhap-tu-tom-tat": 2}
    rank_conf = {"cao": 0, "vua": 1, "thap": 2}
    out = [r for r in items
           if capability in r.get("capability", "").split(",")
           and not (bo_tham_khao and r["adoption"] == "chi-tham-khao")
           and (vessel is None or not r["vessel_fit"] or vessel in r["vessel_fit"].split(","))]
    out.sort(key=lambda r: (rank_status.get(r["curation_status"], 2), rank_conf.get(r["confidence"], 3)))
    return [(r["duong_dan"], r["adoption"], r["curation_status"], r["use_when"], r["skip_if"]) for r in out[:top]]
# vd: tra("scraping", vessel="hermes")
```

## 5. Giới hạn trung thực
- Nhãn do model/agent gắn, **không phải kết luận**. 358 mục `da-doc-dau-entry` có thể thiếu điều kiện loại trừ (license, beta, GPU, khoá API) — luôn đọc entry gốc trước khi dùng; 460 skill nhập hàng loạt chưa gắn nhãn (tra bằng `tom_tat`, `domain`).
- `adoption`/`needs`/`vessel_fit` chỉ ghi điều entry nói rõ; "chưa chạy trong kho" ≠ "khó cài".
- Chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem `USAGE-LOG.md`).
- `dup_group` do mỗi lô gắn riêng nên một số nhóm cùng nghĩa mang tên khác nhau (vd `motion-video-code` / `code-video-motion`); coi chúng là một.
- DeepSeek Harness không nối trực tiếp với kho: lấy catalog qua OpenClaw (xem `agents/OPERATING-MODEL.md`).

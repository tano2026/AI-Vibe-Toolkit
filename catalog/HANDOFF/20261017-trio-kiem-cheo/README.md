# Trio kiểm chéo mẫu nhãn (2026-10-17)

Ba agent, mỗi agent 20 mục, không trùng mục. Luật gốc: `catalog/TASK-RA-SOAT-KHO.md` Phần B.

## Thứ tự
1. Nobitano gửi 3 file TASK cho 3 agent: `TASK-hermes.md`, `TASK-openclaw.md`, `TASK-deepseek.md` (mỗi file tự chứa bảng 20 mục + dự phòng + luật).
2. Mỗi agent trả `REPORT-<tên>.md` (hermes / openclaw / deepseek). Nobitano gom 3 file vào thư mục này (hoặc đưa Claude).
3. Claude gộp bằng script, chưa ghi gì lên kho:
   `PYTHONIOENCODING=utf-8 python tools/merge_trio_reports.py catalog/HANDOFF/20261017-trio-kiem-cheo/REPORT-*.md`
4. Claude duyệt danh sách đề xuất sửa rồi mới sửa `curation.json` và build lại.

## File
- `lists.json`: 3 lát (main 20 + reserve 3) dạng máy đọc.
- `make_lists.py`: tái lập `lists.json` và 3 TASK từ `CATALOG.csv` (công thức chọn ghi trong mỗi TASK).
- Nhãn trong `curation-draft/` và `curation.json` vẫn là nháp cho đến khi Claude gộp xong.

---
name: tracker-updater
description: Hướng dẫn cập nhật TRACKER.md đúng cấu trúc, đúng số lượng, và đúng vị trí phân loại của kho AI-Vibe-Toolkit.
---
# 📊 TRACKER.md Update Skill

> Chỉ dẫn từng bước giúp AI hoặc người dùng cập nhật file TRACKER.md chuẩn xác 100%, không làm lệch cấu trúc bảng hay đếm sai số lượng.

---

## 📐 Quy Tắc Định Dạng & Cập Nhật

### 1. Phân Loại Chính Xác
Khi thêm mới một mục, hãy đặt nó vào đúng bảng phân loại tương ứng:
- `🔌 MCPs` — Các MCP Server.
- `📦 Repos` — Các GitHub repository.
- `🧠 Skills` — Các Prompt Templates hoặc System Prompts.
- `📦 Stacks` — Các Combo Tools kết hợp.

### 2. Cập Nhật Số Lượng Ở Header
- Mỗi khi thêm/bớt mục ở các bảng, bắt buộc phải cập nhật lại tiêu đề mục đó.
- Ví dụ: `## 🧠 Skills — 14 cái` tăng lên thành `## 🧠 Skills — 15 cái`.
- Cập nhật bảng **📊 Tổng kết** ở cuối file để khớp chính xác các cột: `Tổng`, `File ✅`, `Script ✅`, `Video ✅`.

### 3. Cấu Trúc Bảng Chuẩn
- Dùng dấu `|` phân tách cột rõ ràng.
- Giữ nguyên trạng thái biểu tượng:
  * `✅` - Đã hoàn thành (file/script tồn tại).
  * `⏳` - Đang chờ xử lý / lên kế hoạch làm video.
  * `-` - Không áp dụng.

### 4. Đếm Số Thứ Tự Video
- Đọc số lượng video/script hiện tại trong thư mục `content/`.
- Số thứ tự video tiếp theo = (Tổng số file script hiện tại) + 1.
- Ghi nhận chính xác trong bảng danh sách **🎬 Scripts sẵn sàng quay**.

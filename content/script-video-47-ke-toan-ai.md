# Script Video #47 — AI Kế Toán: Phân Loại Sao Kê 20 Giây, Tự Động Hóa Hoàn Toàn

**Angle:** Workflow kế toán AI thực tế cho SMB Việt Nam
**Thời lượng:** 90 giây
**Hook:** "Kế toán mày mất 2 tiếng làm việc này — AI làm trong 20 giây"

---

## 🎬 SCRIPT

---

**[HOOK — 0:00-0:08]**
*(Text: "Kế toán mày mất 2 tiếng làm việc này. AI làm trong 20 giây.")*

Cuối tháng.
File sao kê ngân hàng: 200 dòng giao dịch.
Kế toán ngồi phân loại từng dòng.
Đối chiếu quy định Cục Thuế.
Tính ITC từng khoản.

2 tiếng. Dễ sai. Nhàm chán.

---

**[SOLUTION — 0:08-0:22]**
*(Screen: Claude Code + CSV file)*

Upload CSV sao kê lên Claude Code.
Paste 1 prompt.
20 giây.

Claude:
- Phân loại 200 dòng theo danh mục chuẩn thuế
- Xác định được/không khấu trừ GTGT
- Tính ITC từng khoản
- Tổng hợp: đủ điều kiện hoàn thuế không?

---

**[DEMO PHẦN 1 — 0:22-0:45]**
*(Screen: CSV input → bảng output)*

Input: Sao kê thô
```
01/05 | CK TIỀN ĐIỆN T4 | -2,300,000
01/05 | THANH TOÁN CHO CTY ABC | -15,000,000
02/05 | PHÍ DỊCH VỤ NGÂN HÀNG | -55,000
```

Output 20 giây:
```
| CK TIỀN ĐIỆN T4 | Chi phí điện nước | Được khấu trừ | 100% | 230,000 |
| THANH TOÁN CTY ABC | Chi phí dịch vụ | Được khấu trừ | 100% | 1,500,000 |
| PHÍ DỊCH VỤ NH | Chi phí ngân hàng | Không khấu trừ | 0% | 0 |

Tổng ITC được khấu trừ: 3,050,000 đ
Điều kiện hoàn thuế GTGT: ĐỦ ĐIỀU KIỆN
```

---

**[DEMO PHẦN 2 — 0:45-1:05]**
*(Screen: Chuỗi tự động Google Drive + Sheets)*

Và chuỗi tiếp theo chạy tự động:

*(Animate 3 bước)*

**Bước 1:** Xuất PDF hóa đơn — đúng thư mục định sẵn
**Bước 2:** Tải lên Google Drive — folder tháng tự tạo
**Bước 3:** Cập nhật Google Sheets — link PDF, trạng thái, số liệu

Khi khách hàng thay đổi 1 thông tin?
Bảng tổng hợp thuế cập nhật ngay lập tức.

---

**[SETUP — 1:05-1:18]**
*(Screen: Code + config)*

Stack cần:
- Claude Code (dùng rồi)
- Google Workspace MCP (free, link bio)
- Python + pandas + anthropic

Prompt templates đầy đủ:
→ Link kho AI Vibe Toolkit trong bio
→ File: `skills/ke-toan-automation.md`

---

**[CTA — 1:18-1:28]**
*(Text: "Kế toán 2 tiếng → 20 giây")*

Không phải thay thế kế toán.
Là để kế toán làm việc quan trọng hơn.

Comment "KẾ TOÁN" để nhận file prompt đầy đủ.

---

## 📋 METADATA

**Tags:** #ketoan #claudecode #automation #aivietnam #accounting #python

**Thumbnail:**
- Split: Kế toán ngồi gõ (trái) vs Terminal 20 giây (phải)
- Text: "2 TIẾNG → 20 GIÂY"
- Sub: "AI Kế Toán"
- Màu: xanh lá (tiền bạc) + dark

---
*Script by AI Vibe Toolkit | Video #47*

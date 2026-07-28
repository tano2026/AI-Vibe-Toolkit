# Changelog Decisions — Nguồn quyết định chung (Hermes / OpenClaw / Claude)

> Ghi lại đây MỌI quyết định kiến trúc/thiết kế quan trọng, ngay khi chốt — để phiên làm việc
> khác (chat khác, agent khác) không phải tự dò lại từ đầu. Tham chiếu bởi `SENIOR-ADVISOR.md`,
> `HERMES-SOUL.md` (case 3, case 4). Append-only, không sửa/xoá entry cũ.

---

## 2026-07-28 — Phát hiện mâu thuẫn: OPENCLAW-WORKER-STRUCTURE.md vs UNIFIED-ARCHITECTURE.md

**Người phát hiện:** Claude (Senior Advisor), qua yêu cầu Nobitano tổng hợp lại các file mới.

**Mâu thuẫn:** 2 file cùng ngày 25/07/2026 mô tả 2 cấu trúc agent khác nhau:
- `UNIFIED-ARCHITECTURE.md` (dựa trên audit thật `agents/__init__.py`) — 9 agent THẬT đang chạy:
  `ceo, research, dev, sales, marketing, media, operations, support, analytics`. File tự ghi rõ
  "thắng" khi có xung đột. Khuyến nghị: KHÔNG build `hr-admin` riêng lúc này, gộp tạm vào
  `operations`.
- `OPENCLAW-WORKER-STRUCTURE.md` (viết sau, cùng ngày) — yêu cầu build 9 folder khác:
  `research, marketing, sales, content, dev, designer, media, ops-finance, hr-admin` — theo
  ORG-v2.md lý thuyết cũ, KHÔNG tham chiếu audit thật ở file kia.

**Đây đúng pattern "case 4" đã ghi trong `HERMES-SOUL.md`** — 2 lớp thiết kế đá nhau, viết cách
nhau vài giờ trong cùng 1 ngày, không phiên nào biết phiên kia.

**Việc liên quan trực tiếp:** Role ⑨ HR & Admin và ⑩ Legal & Compliance được thêm vào
`ORG-v2.md` ở 1 phiên chat khác (trước ngày 25/07) — theo audit thật trong
`UNIFIED-ARCHITECTURE.md`, agent-core KHÔNG có agent nào cho 2 role này. Legal & Compliance
chưa được nhắc tới ở bất kỳ file audit nào.

**Trạng thái:** CHƯA CHỐT — cần Nobitano quyết định 1 trong các hướng:
1. Theo `UNIFIED-ARCHITECTURE.md` (audit thật thắng) — bỏ build `hr-admin`/`content`/`designer`
   riêng, gộp theo đúng 9 agent thật; xem lại có cần giữ role ⑨/⑩ trong ORG-v2.md hay đổi thành
   "định hướng tương lai, chưa build" thay vì role đang hoạt động.
2. Theo `OPENCLAW-WORKER-STRUCTURE.md` (ORG-v2 lý thuyết thắng) — build đủ 9 folder tách biệt,
   chấp nhận lệch với agent-core thật đang chạy, cần đồng bộ code lại sau.
3. Hybrid — quyết định riêng từng điểm lệch (xem bảng "Đối chiếu" trong
   `UNIFIED-ARCHITECTURE.md`).

**Không tự chốt thay Nobitano** — đây là quyết định kiến trúc, đúng loại phải escalate theo
`SENIOR-ADVISOR.md` mục "Khi nào escalate", không phải việc Claude tự quyết rồi ghi đè.

**Việc khác phát hiện cùng lúc, cần xác nhận riêng:**
- Bảo mật: `.env` VPS lộ `ZALO_ACCESS_TOKEN` + `DEEPSEEK_API_KEY` plaintext — kế hoạch vá đã có
  (`SECURITY-WALL.md`), CHƯA xác nhận đã rotate 2 key này chưa.
- Hạ tầng: VPS đang down, IP `100.64.173.75` là dải CGNAT không phải IP public thật — chờ
  Nobitano reboot + xác định đúng IP public trước khi build OpenClaw mới.

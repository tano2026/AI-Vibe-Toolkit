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


---

## 2026-07-28 — QUYẾT ĐỊNH CHỐT: theo audit thật, không theo lý thuyết

**Người chốt:** Nobitano, sau khi Senior Advisor trình bày 2 phương án.

**Kết quả:** Theo hướng `UNIFIED-ARCHITECTURE.md` (audit thật) — giữ nguyên 9 agent thật đang
chạy trong agent-core, KHÔNG build agent thứ 10/11 cho HR&Admin/Legal&Compliance.

**Đã thực thi:**
1. `agents/company/ORG-v2.md` viết lại thành v3.0 — bảng 9 agent thật thay 10-role lý thuyết cũ.
2. `roles/hr-admin.md` v2.0 — đổi từ "Role Pack vị trí ⑨" thành "Extension pack nạp vào agent
   `operations`". Nội dung SOP/skill giữ nguyên 100%, chỉ đổi vai trò gọi.
3. `roles/legal-compliance.md` v2.0 — đổi từ "Role Pack vị trí ⑩" thành "Extension pack nạp
   vào agent `sales`". Nội dung giữ nguyên 100%, chỉ đổi vai trò gọi.
4. `OPENCLAW-WORKER-STRUCTURE.md` v2.0 — sửa lại đúng 8 folder worker (research, dev, sales,
   marketing, media, operations, support, analytics — không tính `ceo` vì đó là Hermes/bộ não,
   không phải OpenClaw worker), xoá `content/`, `designer/`, `ops-finance/`, `hr-admin/` riêng
   biệt khỏi kế hoạch build.

**Còn treo, CHƯA xử lý trong lượt này (cần theo dõi riêng):**
- Bảo mật: rotate `ZALO_ACCESS_TOKEN` + `DEEPSEEK_API_KEY` sau khi phát hiện lộ plaintext
  (xem `SECURITY-WALL.md`) — CHƯA xác nhận đã làm.
- Hạ tầng: VPS đang down, cần Nobitano tự reboot + xác định đúng IP public trước khi build
  OpenClaw mới theo cấu trúc 8 folder ở trên.
- `HERMES-PLAYBOOK.md` dòng 16 vẫn còn mô tả sai "Hermes chạy trong OpenClaw trên VPS" — cần
  sửa theo đúng `UNIFIED-ARCHITECTURE.md` (Hermes = agent-core, Local Windows) ở lượt sau.

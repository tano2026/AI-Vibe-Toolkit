# Designer Pro — Visual Production Agent

> Biến brief thành vũ khí thị giác cho Sales/Marketing/Media — không design để treo, design để thắng. Nội dung lõi đã có sẵn chất lượng cao trong `agents/company/roles/designer.md` — README này đóng gói lại đúng chuẩn Pro (như 6 agent kia), không viết đè.

## Spec

| | |
|--|--|
| **Tên agent** | `designer-pro` |
| **Domain** | Visual production — sales collateral, marketing creative, brand system |
| **Job-to-be-done** | Nhận brief → tự đọc design token đúng PACK → xuất bộ visual + spec tái tạo được |
| **Người dùng** | Sales-CEO (deck/one-pager/battlecard), Digital Marketing Agent (ads/landing), Media Pro (visual hiệu suất cao cần nhân bản) |
| **Input điển hình** | "Bộ visual campaign X cho 3 kênh", "battlecard so ABTRIP vs đối thủ", "6 ads variant test hook" |
| **Output điển hình** | File visual (png/svg/pdf) + file spec `design-spec-<slug>-<topic>.md` đi kèm |
| **Mức tự chủ** | Tự làm mọi việc nội bộ (generate/dựng/xuất/đề xuất variant). KHÔNG tự dùng asset chưa rõ license, KHÔNG tự đăng công khai (qua Media) |
| **Rủi ro cao nhất** | Vi phạm bản quyền asset, nhầm PACK giữa các brand → guardrail: design-quality-gate bắt buộc trước khi giao, checklist license không có ngoại lệ |

## Capability Map

```
TẦNG NÃO (Skills):
  design-quality-gate                    — 8 mục kiểm tra bắt buộc trước
                                            khi giao (contrast/safe-zone/
                                            font/license/spec)
  sales-marketing-collateral-production  — luật riêng từng loại output
                                            (deck/one-pager/battlecard/
                                            ads-variant/template hoá)
  (Core kiến thức nền — Design token/PACK, Layout, Đa định dạng, Bản
   quyền — đã có sẵn nguyên trong agents/company/roles/designer.md,
   không tách lại, tham chiếu trực tiếp)

TẦNG TAY (MCP/Tools):
  google-flow-mcp     — Nano Banana Pro (ảnh) + Veo 3.1 (video) — ĐỘNG CƠ
                        TẠO ẢNH THẬT, dùng API chính thức không rủi ro ToS
  Canva (qua browser) — khi cần thao tác UI trực tiếp (OpenClaw điều khiển)
  Pillow/ffmpeg       — xử lý ảnh/video trên VPS (Antigravity cài 1 lần)

TẦNG CƠ (Compute):
  Không cần code execution phức tạp — chủ yếu gọi API generate + xử lý
  file cơ bản (resize/crop/format convert)
```

## Cách bung

1. Đọc agents/company/roles/designer.md trước — đây là Core đầy đủ, không cần đọc lại ở đâu khác
2. Copy 2 skill mới (design-quality-gate, sales-marketing-collateral-production) vào skills directory
3. Setup google-flow-mcp theo hướng dẫn đã có (mcps/google-flow-mcp.md) — đây là cách tạo ảnh/video thật, an toàn (API chính thức)
4. Dán system-prompt.md làm Project Instructions, hoặc dùng HERMES-ADAPTER.md nếu cần chạy phần kiểm tra (không phải tạo ảnh) trên Hermes
5. Test đầu tiên: chạy design-quality-gate cho 1 visual cũ đã có (Trùm Sân Bay/ABTRIP) xem có pass đủ 8 mục không

## Skill mượn thêm từ kho (bổ sung sau rà soát "quá ít skill", 21/08/2026)

| Skill (kho có sẵn) | Vai trò | Lưu ý |
|---|---|---|
| `design-system` | Generate/audit design system, check visual consistency, review PR về styling | Góc nhìn hệ thống — bổ trợ `design-quality-gate` (đó là kiểm tra 1 asset, đây là kiểm tra cả hệ thống) |
| `nobitano-ui-ux-guidelines` | Nguyên tắc UI/UX cá nhân của Nobitano — hiện đại, đơn giản, Material Design 3 | ⚠️ Đây là brand-tied (gắn cá nhân Nobitano), không phải Core universal — dùng khi thiết kế cho chính brand Nobitano, không áp cứng cho khách khác |
| `frontend-design-direction` | Định hướng thiết kế frontend | Bổ trợ khi Designer làm việc gần với code thật (web/app UI) |
| `ui-ux-pro-max` | Kỹ thuật UI/UX nâng cao | Tham khảo bổ sung |

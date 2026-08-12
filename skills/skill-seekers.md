# Skill Seekers — Auto-convert doc/repo/PDF thành SKILL.md

## TL;DR
Meta-skill: đưa vào 1 doc site, GitHub repo, hoặc PDF → skill tự trích quy trình ổn định, schema, lệnh, rule nghiệp vụ → đóng gói thành file SKILL.md chuẩn kèm nguồn gốc rõ ràng. Đúng cái việc Nobitano đang làm tay ở Bước 1-3 của Quy trình kho, giờ có khung sẵn để bán tự động hóa.

## Skill này dùng để làm gì
Thay vì tự đọc hết docs/README rồi tự tay viết SKILL.md, skill này cho 1 quy trình chuẩn:
1. Ghi lại nguồn chính xác (URL, revision, file gốc)
2. Chỉ trích phần **ổn định** — quy trình, schema, lệnh, rule — bỏ qua phần dễ đổi (version number, UI cụ thể)
3. Tách nội dung: hướng dẫn ngắn gọn vào SKILL.md, tài liệu chi tiết vào `references/`, script chạy được vào `scripts/`, template vào `assets/`
4. Đổi tên tool cụ thể của nguồn gốc thành mô tả năng lực chung (để skill "portable" — không gắn chết vào 1 tool)
5. Ghi rõ nguồn gốc + tác giả gốc, không claim là của mình
6. Validate lại bằng cách thử prompt thực tế

## Setup từng bước
1. Đưa link/repo/PDF cần biến thành skill cho Claude (mày) research như bình thường
2. Áp quy trình 7 bước ở trên khi viết file .md — đặc biệt bước "tách nội dung" (SKILL.md ngắn gọn, chi tiết đẩy ra file phụ) giúp file .md không bị phình to
3. Với 1 repo có nhiều thành phần (nhiều API/nhiều lệnh) — cân nhắc tách thành `references/` riêng thay vì nhồi hết vào 1 file .md, đúng tinh thần skill này
4. Validate: thử hỏi Claude/Hermes 1 câu thực tế liên quan tới skill mới viết, xem có trả lời đúng theo skill không

## Ví dụ thực tế
**Trước khi có skill này:** Nobitano quẳng link 1 MCP mới → Claude tự đọc README, tự quyết định cấu trúc file, đôi khi nhồi hết mọi thứ vào 1 file .md dài 500 dòng, khó scan.

**Sau khi áp quy trình skill-seekers:** File .md giữ đúng format chuẩn của kho (TL;DR, setup, ví dụ, đánh giá) — phần "chi tiết kỹ thuật dài" (VD: full API reference của 1 MCP phức tạp) tách ra `mcps/<tên>/references/api-full.md` riêng, file chính chỉ trỏ tới khi cần đọc sâu.

## Lưu ý / Lỗi thường gặp
- Skill gốc thiết kế cho format `skills/<name>/SKILL.md + agents/openai.yaml` (chuẩn Codex/Hermes generic) — kho của Nobitano không cần file `agents/openai.yaml`, bỏ qua phần đó
- Rule "integrity" của skill gốc rất chặt (không bịa file, không copy credential, tôn trọng license nguồn) — đây là điểm tốt, giữ nguyên khi áp dụng, khớp với nguyên tắc "đánh giá thật, không PR" đã có trong kho
- Không tự động hóa được 100% — vẫn cần Claude đọc và tổng hợp, skill này chỉ cho khung quy trình rõ ràng hơn, không phải code chạy tự động không cần người duyệt

## Đánh giá cá nhân
- Điểm mạnh: đúng use case, quy trình 7 bước rõ ràng, rule "integrity" chặt chẽ (không bịa, tôn trọng license) khớp tinh thần kho hiện tại
- Điểm yếu: chỉ là quy trình/checklist, không phải tool thực thi — vẫn phụ thuộc hoàn toàn vào việc Claude tự áp dụng đúng mỗi lần, không có cơ chế enforce
- Có nên dùng không: 7/10 — không phải game changer nhưng giúp chuẩn hóa cách tách file khi nguồn quá dài/phức tạp, đáng tích hợp vào Bước 3 của Quy trình hiện tại

## Link
- Nguồn gốc skill: adapted từ [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) (MIT), qua bundle [Rylaispirit/rylai-codex-hermes-skills](https://github.com/Rylaispirit/rylai-codex-hermes-skills)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Skill này không cần API call — là quy trình cho Claude khi viết file .md
# Hermes không viết kho (theo phân công hiện tại) nên không cần tích hợp thực thi
# Chỉ liên quan tới cách Claude (mày) research + viết file, không phải việc Hermes làm
```

### OpenClaw
> Không áp dụng — Bước viết kho hoàn toàn do Claude làm, OpenClaw/Hermes chỉ đọc kho, không viết.

### Antigravity
> Không cần deploy — đây là quy trình nội bộ khi Claude viết file .md, không phải service chạy trên VPS.

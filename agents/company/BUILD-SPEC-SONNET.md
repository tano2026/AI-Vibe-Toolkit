# BUILD SPEC — Work order cho Sonnet

> File này dành cho Claude Sonnet (hoặc model thực thi khác) khi Nobitano giao expand hệ thống
> One-Person Company. Khung + luật đã chốt bởi Fable 5 — Sonnet KHÔNG thiết kế lại, chỉ expand
> theo đúng spec dưới đây. Đọc trước: `ORG.md`, `COORDINATION.md`, `EXPERT-CORE.md`, 4 role packs.

---

## Quality bar — thế nào là ĐẠT

Mỗi output của Sonnet phải qua được test này:

| Shallow (FAIL) | Pro (PASS) |
|---|---|
| "Tối ưu targeting cho hiệu quả" | "Retarget cap 2-3 lần/tuần; vượt = đốt tiền + hại brand" |
| "Viết hook hấp dẫn" | "3 hook option, mỗi cái thuộc 1 trong 4 kiểu; 3s retention <65% = fail, làm lại" |
| "Kiểm tra kỹ trước khi gửi" | Checklist 5 mục tick được, có ngưỡng số |
| Ví dụ: "một công ty nọ..." | Ví dụ: input nguyên văn → output nguyên văn, dùng `[Sản phẩm X]`/`[Ngành Y]` |

Quy tắc chung: **mọi lời khuyên phải có ngưỡng số hoặc trình tự bước hoặc điều kiện if-then.**
Câu nào đúng với mọi công ty trên đời = câu vô dụng, cắt.

## Luật cứng khi viết (thừa kế từ hệ thống, không đổi)

1. Tiếng Việt casual, giải nghĩa jargon ngay trong câu.
2. Code cho Hermes: `urllib.request` only, không `requests`. Token = `[GITHUB_TOKEN]` placeholder, key = env var.
3. Ví dụ dùng placeholder generic `[Sản phẩm X]`, `[Ngành Y]`, `[Đối thủ Z]` — không gắn brand.
4. Ngưỡng số: nếu EXPERT-CORE đã có → dùng đúng, không chế số mới mâu thuẫn. Cần ngưỡng mới → đề xuất + ghi chú `[Sonnet đề xuất, CEO review]`.
5. Push GitHub: GET lấy SHA → PUT kèm SHA → `time.sleep(0.8)`. TRACKER.md append-only.
6. Verify trạng thái repo bằng API trước khi build — không tin số trong tài liệu.

---

## Task list theo thứ tự ưu tiên

### P1 — Airtable HQ (điều kiện để mọi thứ chạy)
- [ ] Viết `agents/company/airtable-hq-setup.md`: hướng dẫn tạo base `company-hq` theo schema
      trong COORDINATION.md mục 2, kèm module Python `hq.py` (urllib) đủ 6 hàm:
      `get_my_tasks(role)`, `create_task()`, `update_status()`, `request_approval()`,
      `check_approval(task_id)`, `log(role, task_id, event)` — copy-paste chạy được.
- [ ] Test case khô: tạo task giả → xin duyệt → check pending → log. Ghi expected output từng bước.

### P2 — OpenClaw routing
- [ ] Đọc `agents/OPENCLAW-PLAYBOOK.md` hiện tại (fetch bản mới nhất), append section
      "Company Routing": bảng lệnh Telegram → role (`/research`, `/marketing`, `/sales`,
      `/content`, `/design`, `/media`) → fetch 3 file theo pattern nạp cuối EXPERT-CORE.md
      → delegate Hermes. Kèm luật: không header `[PACK:]` → hỏi lại 1 câu; hành động rủi ro
      → approval loop, query bảng `approvals` trước khi thực thi.
- [ ] Append tương tự vào `agents/HERMES-PLAYBOOK.md`: cách nhận delegation có role, cách
      dùng `hq.py`, luật no-fabrication (dẫn EXPERT-CORE ⑤).

### P3 — Nâng 2 package cũ lên chuẩn mới
- [ ] `agents/research-pro.md`: chèn section trỏ EXPERT-CORE ①+ quy tắc Airtable HQ (không viết
      lại toàn file — chỉ patch phần load pattern + thêm luật nguồn nếu thiếu).
- [ ] `agents/sales-ceo/system-prompt.md`: patch tương tự với EXPERT-CORE ③; state layer nay =
      Airtable `company-hq` (đóng blocker "chưa có state storage" cũ).

### P4 — Ví dụ thực tế cho 4 role pack mới
Mỗi role pack (marketing / content-creator / designer / media) đang thiếu mục ví dụ. Với mỗi file:
- [ ] Thêm section `## Ví dụ thực tế` : 1 brief input nguyên văn (đúng format handoff 5 phần)
      → output mẫu rút gọn nhưng thật (plan thật có số, script thật có hook, spec thật có size list,
      lịch đăng thật có bảng). Placeholder generic.
- [ ] Thêm 1 test case nghiệm thu vào cuối: "giao brief này → output phải có X, Y, Z" để CEO test khô.

### P5 — Domain Pack thứ 2
- [ ] Tạo `domain-packs/wonder-mart/PACK.md` theo `_TEMPLATE.md` — e-commerce, điền được gì điền,
      còn lại `CHƯA CÓ — hỏi CEO`. Mục đích: chứng minh cơ chế đa project bằng 2 pack thật.

### P6 — Script video giới thiệu hệ thống (content cho kênh Tano)
- [ ] 1 script theo template `/content/`: "Công ty 1 người vận hành bằng 7 AI agent" — đánh số
      tiếp theo file cuối trong /content/ (đếm thực tế). Cập nhật TRACKER.

---

## Definition of Done toàn dự án expand

- [ ] Mọi file mới/patch đã push đúng folder + TRACKER append đủ dòng
- [ ] `hq.py` chạy được thật trên môi trường Hermes (urllib only) — có log test kèm
- [ ] 2 playbook (OpenClaw, Hermes) có section routing, không phá nội dung cũ
- [ ] 4 role pack đều có ví dụ + test case nghiệm thu
- [ ] Không file nào chứa token/key thật
- [ ] Không ngưỡng số nào mâu thuẫn EXPERT-CORE (trừ khi đánh dấu đề xuất)

## Khi nào Sonnet dừng lại hỏi CEO

1. Schema Airtable cần đổi so với COORDINATION.md (đừng tự đổi).
2. Playbook hiện tại có nội dung xung đột trực tiếp với routing mới.
3. Cần credential/quyền mới (Airtable token, quyền đăng nền tảng).
Ngoài 3 ca trên → tự chạy hết theo thứ tự P1→P6.

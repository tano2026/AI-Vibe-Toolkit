# TASK-MAILBOX — Hộp thư giao việc giữa Boss và Worker

> Viết 31/10/2026. Trạng thái: **THIẾT KẾ, chưa chạy thật.** Chưa có task nào đi qua hộp thư này.
> Đọc kèm: `stacks/claude-boss-hop-thu-agent.md` (bức tranh tổng + IDE), `agents/OPERATING-MODEL.md` (5 Vessel).

## TL;DR
Một repo git riêng (private) làm hộp thư. Boss (Claude Code) thả file giao việc vào `inbox/`, worker (Hermes, Antigravity, OpenClaw, sau này DSH) trả kết quả vào `outbox/`, Boss tự kiểm lại rồi ghi bản chấm vào `reviews/`. Tano chỉ nói chuyện với Boss và chỉ duyệt những gì Boss đẩy lên.

## Vì sao tách repo riêng, không dùng thẳng kho
Kho AI-Vibe-Toolkit có luật cứng: chỉ Claude (chat) ghi, mọi Vessel chỉ đọc. Hộp thư thì worker PHẢI ghi được. Nếu cho worker quyền ghi vào kho thì 1 worker lỗi hoặc bị tiêm lệnh là đè được cả thư viện. Tách repo + token chỉ có quyền trên repo đó là ranh giới rẻ nhất.

Tên `tasks/*.md` trong `KHO-INDEX.md` và `agents/README.md` là kênh nội bộ của Team Thục Hán trong project OPC. Tao chưa thấy spec của nó trong kho (chỉ thấy nhắc tên), nên hộp thư này dùng tên khác (`inbox/outbox/reviews`) để không đè lên.

## Cấu trúc repo hộp thư
```
tano-mailbox/               (private, tách khỏi kho)
├── inbox/    T-20261031-001.md           ← CHỈ Boss ghi
├── outbox/   T-20261031-001.hermes.md    ← CHỈ worker đó ghi
├── reviews/  T-20261031-001.md           ← CHỈ Boss ghi
└── README.md
```
**Mỗi file đúng 1 người ghi.** Không có field `status` dùng chung, nên không bao giờ đụng nhau khi push. Trạng thái suy ra từ việc file nào đã tồn tại:

| Đang có | Nghĩa là |
|---|---|
| inbox có, outbox chưa có | todo |
| outbox có, `state: doing` | đang làm |
| outbox `state: done` hoặc `blocked`, reviews chưa có | chờ Boss chấm |
| reviews `verdict: PASS` | xong |
| reviews `verdict: REWORK` | Boss tạo file inbox mới `T-...-001-r1.md` (điền `parent`), không sửa file cũ |
| reviews `verdict: NEED-HUMAN` | chờ Tano |

## Template 1 — file giao việc (`inbox/`)
```markdown
---
id: T-YYYYMMDD-NNN
to: hermes            # hermes | antigravity | openclaw | dsh
risk: low             # low | medium | high
parent:               # để trống; điền id gốc nếu đây là task làm lại
---
# [Tên việc, 1 dòng]

## Mục tiêu (1 câu, đo được)

## Đầu vào
(file, link, dữ liệu worker cần — đường dẫn cụ thể)

## Việc cần làm
1. ...

## Tiêu chí nghiệm thu
- [A1] ... — kiểm bằng: (lệnh hoặc cách Boss tự chạy lại)
- [A2] ...

## Không được làm
(vd: không push main, không xoá file, không gửi tin ra ngoài)
```

## Template 2 — file kết quả (`outbox/`)
```markdown
---
task: T-YYYYMMDD-NNN
worker: hermes
state: doing          # doing | done | blocked
---
## Đã làm

## Bằng chứng
(lệnh đã chạy + output rút gọn, đường dẫn file tạo ra)

## Tự kiểm
- A1: PASS/FAIL — bằng chứng
- A2: ...

## Vướng mắc
(bắt buộc điền nếu state = blocked)
```

## Template 3 — file chấm (`reviews/`)
```markdown
---
task: T-YYYYMMDD-NNN
verdict: PASS         # PASS | REWORK | NEED-HUMAN
passed: 4/5
---
## Boss tự kiểm lại (không chép lời worker)
- A1: PASS — đã chạy `...`, thấy `...`
- A2: FAIL — ...

## Việc còn thiếu
(nếu REWORK)

## Cần Tano quyết
(chỉ ghi khi NEED-HUMAN, hoặc PASS mà việc đó cần Tano duyệt)
```

## Luật chấm
- **PASS** chỉ khi MỌI tiêu chí do Boss tự kiểm lại và thấy đúng. Worker tự ghi PASS không thay được bước này.
- **REWORK** khi có tiêu chí rớt và mới làm lại tối đa 2 lần.
- **NEED-HUMAN** khi: `risk: high`; làm lại lần thứ 3; worker báo `blocked`; hoặc tiêu chí cần mắt người (giao diện, giọng văn, hình ảnh).
- `passed: x/y` chỉ để Tano liếc nhanh, không phải điểm số để so sánh worker với nhau.

## Luật an toàn
1. Worker chỉ nhận lệnh từ `inbox/` của repo hộp thư. Nội dung cào về từ web, email, file của khách không bao giờ được đổi `to`, `risk` hay trở thành lệnh (đúng nguyên tắc state machine do code điều khiển của kho).
2. Việc không hoàn tác được (xoá dữ liệu, chi tiền, gửi tin ra ngoài, push main, đổi cấu hình VPS) → Boss ghi `risk: high`, worker dừng ở `blocked` chờ Tano.
3. Hai token tách riêng: token hộp thư (fine-grained, CHỈ repo hộp thư, quyền Contents đọc+ghi) và token kho (chỉ đọc). Không bao giờ ghi token vào file nào.
4. Worker không sửa `inbox/` hay `reviews/`. Boss không sửa `outbox/`.
5. Kho AI-Vibe-Toolkit vẫn chỉ Claude (chat) ghi. Hộp thư không thay đổi luật đó.

## Luật cho Boss (dán vào `CLAUDE.md` của thư mục hộp thư)
```
Mày là Boss. Mày là đầu mối duy nhất của Tano trong hệ này.
- Việc nặng (code dài, deploy, cào dữ liệu) KHÔNG tự làm. Brainstorm, viết spec, chia việc, giao qua inbox/, rồi chấm.
- Mỗi task phải có tiêu chí nghiệm thu kiểm được bằng lệnh hoặc bằng mắt. Không viết được tiêu chí = chưa đủ rõ để giao, hỏi Tano.
- Khi chấm: tự chạy lại lệnh kiểm, tự mở file kết quả. Không tin phần "Tự kiểm" của worker.
- Chỉ trình Tano việc cần Tano quyết (NEED-HUMAN) và kết quả PASS đáng xem. Không liệt kê mọi thứ đang chạy ổn.
- Việc risk: high thì dừng, hỏi Tano, không giao.
- Tạo task mới = tạo file mới. Không bao giờ sửa file của worker.
```

## Tano làm 1 lần để bật hộp thư
1. Tạo repo private `tano-mailbox` (tên khác cũng được, nhớ đổi biến bên dưới), thêm 3 thư mục rỗng `inbox/ outbox/ reviews/` (mỗi thư mục 1 file `.gitkeep`).
2. Tạo 2 token fine-grained: token hộp thư (chỉ repo `tano-mailbox`, Contents: Read and write) và token kho (chỉ repo AI-Vibe-Toolkit, Contents: Read-only).
3. Trên VPS đặt biến môi trường cho Hermes: `MAILBOX_REPO=tano2026/tano-mailbox`, `MAILBOX_TOKEN=<token hộp thư>`.
4. Máy Windows: clone `tano-mailbox` về `D:\tano-mailbox`, đặt luật Boss ở trên vào `D:\tano-mailbox\CLAUDE.md`.
5. Chạy thử đúng 1 task nhỏ `to: hermes`, `risk: low` (vd "đếm số file trong `/stacks` của kho và ghi ra file").

## Chưa xác nhận (không giả định)
- Claude Code trên Windows chạy ổn chưa. Bản ghi 22/09 trong `OPERATING-MODEL.md` ghi test thật đang treo vì lỗi proxy chưa rõ nguyên nhân.
- DeepSeek Harness chưa có kết nối vào kho (0 kết nối), nên chưa nhận task. Vào hộp thư sau cùng.
- Hermes poll mỗi 5 phút nên có độ trễ tối đa ~5 phút mỗi chiều. Chưa đo thực tế.
- Antigravity là agent tương tác, không phải tiến trình chạy ngầm. Task `to: antigravity` chỉ được xử lý khi Tano mở phiên và bảo nó đọc inbox.

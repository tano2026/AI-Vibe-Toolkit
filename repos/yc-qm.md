# qm (Y Combinator) — Multiplayer Agent Harness — GitHub Repo

## TL;DR
Y Combinator vừa mã nguồn mở hoá **chính hạ tầng agent nội bộ họ dùng để vận hành YC** — kế toán, pháp lý, sự kiện, kỹ thuật (kể cả dùng qm để build qm). MIT license, ~2.4K sao trong vài giờ đầu. **Liên quan trực tiếp tới việc rebuild OpenClaw đang làm dở** — đây là "company OS cho agent" y hệt vấn đề đang giải quyết, nhưng đã chạy production thật ở 1 công ty khác.

## Repo này dùng để làm gì
Khác agent cá nhân (1 người 1 AI), qm là hạ tầng cho **nhiều người dùng chung 1 hệ agent** mà không đá nhau — đúng vấn đề cốt lõi khi Nobitano có nhiều domain (ABTRIP, Tano Cafe, GMSP...) chạy song song. Cơ chế chính:

- **Scope** — mỗi người, mỗi channel Slack, mỗi project có **memory/file/keychain/quyền/cron riêng biệt**, không lẫn lộn. Đây chính là khái niệm "Domain Pack" trong `ORG-v2.md` nhưng đã code hoá đầy đủ, có state Postgres thật.
- **3 mức bảo mật chọn sẵn:** Strict (mọi tool call dừng chờ duyệt người) / Auto (bộ lọc tự động chặn nội dung/kết quả đáng ngờ trước khi vào model) / Dangerous (không chặn gì) — đúng tinh thần `DECISION-MATRIX.md` (L0-L3) đã có trong kho, nhưng đơn giản hơn (3 mức thay vì 4).
- **Model-agnostic** — cùng 1 lõi chạy được Claude Code, Codex, OpenCode, Pi — không khoá cứng 1 nhà cung cấp, giống triết lý OmniRoute đang dùng.
- **Policy cứng áp mọi mức bảo mật** (kể cả Dangerous) — chặn cứng các lệnh phá hủy (xoá đệ quy, DROP SQL...) — đây chính là khái niệm "3 lằn ranh đỏ" đã có trong `ORG-v2.md`, nhưng code hoá thành policy thật thay vì chỉ ghi trong docs.
- Có sẵn: cron/webhook trigger, memory, file chia sẻ, kết nối "company brain", hỗ trợ agent-browser, web app artifact chia sẻ được, multi-player project.

## Setup từng bước
```bash
npm exec --yes --package=@yc-software/qm@latest -- qm init . --org <slug> --target fly-or-aws
```
Không cần clone repo để deploy — lệnh trên tự tạo thư mục deployment từ package đã publish.
Muốn tuỳ biến sâu: fork private, mọi customization riêng của tổ chức đặt trong
`deploy/layers/<org>/` — phần còn lại giữ nguyên upstream để dễ update sau.

## Liên hệ trực tiếp tới việc đang làm dở (rebuild OpenClaw)
Đây đúng là bản đã chạy thật của thứ đang cố xây — đáng đọc kỹ trước khi tiếp tục tự viết
`agent-core` từ đầu:
- Khái niệm **scope** của qm ≈ **Domain Pack** đã thiết kế, nhưng qm code hoá đầy đủ bằng
  Postgres state thật, không chỉ là file `.md` convention.
- **3 mức bảo mật** của qm có thể tham khảo trực tiếp cho cách OpenClaw (tay chân thực thi)
  quyết định khi nào cần `[NEEDS_CONFIRMATION]` — hiện đang tự thiết kế tay trong
  `DECISION-MATRIX.md`, qm đã có sẵn code chạy thật.
- **Cảnh báo quan trọng trước khi copy kiến trúc:** qm là hạ tầng multi-USER thật (nhiều nhân
  viên người thật dùng chung), trong khi mô hình của Tano Agency là multi-AGENT (1 người CEO,
  nhiều agent AI) — không giống hệt nhau, cần lọc đúng phần áp dụng được (scope, policy gate),
  bỏ qua phần không cần (identity nhiều người dùng thật, Slack multi-user UI).

## Lưu ý / Lỗi thường gặp
- Chính YC tự thừa nhận: "còn sớm, còn bug" — không phải sản phẩm hoàn thiện dù đã chạy nội bộ.
- Yêu cầu Postgres + deploy Fly.io/AWS — nặng hơn setup hiện tại (VPS Tencent Cloud đơn giản),
  cần cân nhắc chi phí/độ phức tạp trước khi migrate.
- MIT license, tự do dùng/sửa, kể cả thương mại.

## Đánh giá cá nhân
- Điểm mạnh: đúng bài toán "company OS cho agent" đang giải quyết dở, đã chứng minh chạy thật
  (YC dùng để build chính nó); scope + policy gate là 2 khái niệm đáng học/tham khảo trực tiếp.
- Điểm yếu: hạ tầng nặng hơn setup hiện tại (Postgres, cloud deploy); là multi-user thật, không
  phải multi-agent thuần nên không copy nguyên xi được.
- Có nên dùng không: 8.5/10 làm **tài liệu tham khảo kiến trúc bắt buộc đọc** trước khi tiếp tục
  rebuild OpenClaw/agent-core — không nhất thiết phải migrate hẳn sang qm, nhưng đọc kỹ 2 khái
  niệm scope + policy gate trước khi tự thiết kế tiếp.

## Link
- Repo: https://github.com/yc-software/qm
- Docs: qm.ycombinator.com

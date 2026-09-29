# Product Film Skill — GitHub Repo

## TL;DR
Claude Code skill: 1 prompt ra video launch 10-30 giây dựng từ **UI thật của sản phẩm phần mềm** (component React/design token/logo/giá thật) — không phải mockup giả, không phải số liệu bịa. Đúng đối tượng: TMC Corporate Portal, Smart Booking SaaS, Zalo Mini App — khác hẳn pipeline poster/thumbnail vừa xây (đó cho brand vật lý/dịch vụ, cái này cho sản phẩm phần mềm có UI thật).

## Repo này dùng để làm gì
Đọc code sản phẩm thật (design token, font, logo, copy, giá) → tự viết kịch bản + beat map chính xác từng khung hình → dựng phim bằng **Remotion** (đã quen thuộc trong kho) → mount thẳng React component thật với demo data, hoặc quay lại app/web đang chạy → đồng bộ nhạc/sound design → tự kiểm tra chất lượng kịch bản (vấn đề phải ra trước giải pháp, chỉ 1 lần reveal logo gắn với CTA, kết bằng câu hỏi, số liệu phải thật/cụ thể, mỗi dòng đủ thời gian đọc).

## ⚠️ Giới hạn kỹ thuật quan trọng — CHỈ chạy Claude Code

```
"The skill runs your local toolchain, so it does not work in the
Claude chat apps."
```

Không dùng được trong claude.ai/chat thường — bắt buộc Claude Code local. Đúng thêm 1 lý do cần giải quyết dứt điểm vụ Claude Code đang treo lỗi proxy.

## Nhiều fork — chọn bản đầy đủ nhất

| Fork | Ghi chú |
|---|---|
| `StanCosmin28/product-film-skill` | Bản gốc đơn giản, có ví dụ thật (ProCard) |
| `Hadani0mar`, `Rieranthony` | Phát triển thêm, hỗ trợ cài qua `/plugin marketplace` |
| **`tomascupr/product-film`** | **Đầy đủ nhất** — fork từ Rieranthony, thêm HTML engine, ElevenLabs voice, nhiều loại phim hơn (teaser/demo/explainer/social cut/landing loop), kiểm tra bằng đo lường thay vì nhìn mắt thường |

## Setup từng bước (dùng bản tomascupr, đầy đủ nhất)
```bash
git clone https://github.com/tomascupr/product-film
mkdir -p ~/.claude/skills
cp -R product-film/plugins/product-film/skills/product-film ~/.claude/skills/
```
Sau đó trong Claude Code: gõ thẳng *"make a 20s launch teaser for [tên sản phẩm]"* hoặc `/product-film`. Skill tự đọc code sản phẩm, hỏi thêm những gì không tự tìm ra được (loại phim, brief, âm thanh), viết ra `videos/BRAND.md` — file này thắng mọi mặc định của skill.

## Ví dụ thực tế
Áp cho **TMC Corporate Travel Portal (OBT)** — skill tự đọc component UI thật của portal, tạo video launch 20 giây cho khách hàng B2B/B2G xem trước khi ký hợp đồng, dùng đúng giao diện thật đang phát triển — không cần dựng mockup riêng tốn thời gian.

## Lưu ý / Lỗi thường gặp
- Dùng cho brand vật lý/dịch vụ (ABTRIP tour, Tano Cafe đồ uống) — SAI đối tượng, đây chỉ dành cho sản phẩm có UI phần mềm thật
- Không set `videos/BRAND.md` trước — skill dùng mặc định chung, không khớp đúng thương hiệu
- Cài bản fork cũ hơn (StanCosmin28) khi cần tính năng đầy đủ — nên dùng tomascupr ngay từ đầu

## Đánh giá cá nhân
- Điểm mạnh: giải đúng nhu cầu thật đang có (TMC Portal, Smart Booking SaaS cần video launch) mà pipeline poster/thumbnail hiện tại không phủ tới; nguyên tắc "không bịa số liệu/mockup giả" khớp nguyên tắc no-fabrication đã áp toàn hệ thống
- Điểm yếu: chỉ chạy Claude Code (đang treo lỗi), không dùng được ngay bây giờ; cần code sản phẩm THẬT đã có UI để đọc — chưa áp dụng được nếu sản phẩm mới ở giai đoạn spec/thiết kế
- Có nên dùng: 8/10 — đáng cài ngay sau khi Claude Code chạy được, đúng nhu cầu thật đang treo (TMC Portal cần demo cho khách B2B/B2G)

## Link
- Bản đầy đủ nhất: https://github.com/tomascupr/product-film
- Bản gốc đơn giản: https://github.com/StanCosmin28/product-film-skill
- Dùng cùng: repos/remotion.md, repos/remotion-superpowers.md (đã có sẵn trong kho)

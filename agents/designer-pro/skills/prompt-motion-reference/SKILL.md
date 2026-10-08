---
name: prompt-motion-reference
description: >
  Khi cần prompt/skill mẫu để làm video motion, launch film hoặc showreel bằng
  Claude/Remotion/HyperFrames, tra thư viện prompt-motion.com (tham khảo từng
  mục, ghi nguồn, không cào, không train). Kiểm tra kho trước khi ra ngoài.
---

# Prompt Motion Reference (tra cứu có kỷ luật)

## TL;DR
prompt-motion.com là thư viện ~230 video motion làm bằng Opus 5.5 kèm prompt/skill. Dùng để **tham khảo khi bí ý**, không phải nguồn để sao chép hàng loạt. Trang cấm AI train, chỉ cho `use=reference`.

## Khi nào dùng
- Có yêu cầu video motion/launch film/showreel và chưa có prompt hay skill phù hợp
- Muốn xem cấu trúc prompt của người làm tốt (độ dài, mục tiêu, thời lượng, effort)

## Các bước
1. **Tra kho trước:** `repos/product-film-skill.md`, `repos/hyperframes.md`, `repos/remotion.md`, `repos/awesome-claude-5-5-videos.md`, `agents/designer-pro/skills/cinematic-shot-prompt-core/SKILL.md`. Có thì dừng, không ra ngoài
2. Mở `https://prompt-motion.com/`, chọn tối đa **1–3 mục** gần nhu cầu nhất (lọc Prompt/Skill trên giao diện)
3. Đọc prompt hoặc lệnh cài skill; ghi lại: tác giả, link mục, model/effort, 1–2 dòng bài học
4. **Viết lại** theo bối cảnh Tano (brand, thời lượng, kênh) — không dán nguyên văn vào sản phẩm
5. Muốn dùng skill: đọc repo gốc của tác giả, báo Nobitano, đi qua `skill-lifecycle-management` trước khi cài

## Không được làm
- Cào/lập lịch quét trang, lưu hàng loạt nội dung vào kho (kho chỉ giữ con trỏ + ghi chú ngắn + link)
- Dùng nội dung để huấn luyện hay tinh chỉnh model
- Giả danh crawler khác hoặc tìm đường vòng khi bị chặn (gặp 403 → dừng, báo người)
- Cài skill chỉ vì thấy video đẹp

## Kiểm chứng (PASS/FAIL)
PASS khi: với 1 nhu cầu video thật, agent trả về được (a) mục tham khảo + link, (b) bản prompt đã viết lại, (c) không sao chép nguyên văn dài. Chi tiết trang: `repos/prompt-motion.md`.

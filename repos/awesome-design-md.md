---
name: awesome-design-md
description: >
  Rank: #150 GitHub global Tác giả: voltagent Domain: Bộ sưu tập DESIGN.md để AI agent tạo UI đúng phong cách brand thật
---

# awesome-design-md — kho DESIGN.md để AI vẽ UI giống hệt brand thật

**GitHub:** https://github.com/voltagent/awesome-design-md
**Xếp hạng:** #150 toàn cầu trên GitHub | 61 commit | có Discord riêng

---

## TL;DR

Bộ sưu tập file `DESIGN.md` — khái niệm mới do Google Stitch giới thiệu — mỗi file mô tả bằng văn bản thuần cách 1 brand thật thiết kế UI (Claude, Stripe, Linear, Vercel...). Copy 1 file vào project, bảo AI agent "làm giao diện giống thế này" là ra UI đúng phong cách, không cần Figma hay JSON schema.

## Tool này dùng để làm gì

DESIGN.md không phải code, không phải Figma export — chỉ là markdown mô tả token màu, font, spacing, tông giọng thiết kế của 1 brand cụ thể. Vì là markdown nên LLM đọc hiểu trực tiếp, không cần parse gì thêm. Repo này đã phân tích sẵn nhiều brand nổi tiếng (Claude: tông terracotta ấm, layout editorial sạch; ElevenLabs: UI tối, hiệu ứng waveform; Ollama: tối giản kiểu terminal...) thành file DESIGN.md sẵn dùng.

## Setup từng bước

1. Vào repo, chọn brand có phong cách gần với ý muốn (vd muốn giao diện sạch sẽ chọn "Claude" hoặc "Linear")
2. Copy file `.md` tương ứng vào root project của mình, đặt tên `DESIGN.md`
3. Bảo AI coding agent (Claude Code, Cursor...): "build cho tao trang giống DESIGN.md này" — agent tự đọc và áp token màu/font/layout

## Ví dụ thực tế

Làm landing page cho An Bình Fast Track, muốn phong cách sạch gọn kiểu Linear — copy DESIGN.md của Linear vào project, prompt Claude Code "build landing page fast track dịch vụ sân bay theo DESIGN.md này" — ra UI đúng tông màu/spacing của Linear áp cho nội dung An Bình.

## Lưu ý / Lỗi thường gặp

- DESIGN.md chỉ mô tả token/style — không thay thế được việc viết nội dung hay layout logic cụ thể, agent vẫn cần prompt rõ cấu trúc trang muốn làm
- 2 repo trùng tên tồn tại (Digiflex-solution/awesome-design-md chỉ có 1 commit, ít nội dung) — bản voltagent này đầy đủ và cập nhật hơn hẳn, nhớ dùng đúng bản

## Đánh giá cá nhân

- **Điểm mạnh:** tiết kiệm cực nhiều thời gian research phong cách thiết kế — thay vì mô tả bằng lời (dễ mơ hồ), có sẵn file chuẩn hoá theo brand thật; xu hướng DESIGN.md đang được nhiều agent hỗ trợ (Google Stitch, Claude Code...)
- **Điểm yếu:** khái niệm còn mới (Google Stitch mới giới thiệu gần đây) — số lượng brand có sẵn còn giới hạn, brand đặc thù ngành hàng không/du lịch chưa chắc có sẵn, phải tự viết DESIGN.md riêng
- **Có nên dùng không:** 7.5/10 — rất hữu ích khi cần tham khảo nhanh 1 phong cách UI cụ thể, nhưng vẫn cần tự viết DESIGN.md riêng cho brand ABTRIP/An Bình nếu muốn nhất quán lâu dài

## Link
- Repo: https://github.com/voltagent/awesome-design-md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Repo markdown thuần, không có API — Hermes fetch file DESIGN.md cụ thể khi cần
import urllib.request

def fetch_design_md(brand_name):
    url = f"https://raw.githubusercontent.com/voltagent/awesome-design-md/main/{brand_name}/DESIGN.md"
    req = urllib.request.Request(url, headers={"User-Agent": "hermes"})
    return urllib.request.urlopen(req).read().decode()
```

### OpenClaw
```bash
git clone https://github.com/voltagent/awesome-design-md.git ~/reference/design-md
# copy file cần dùng vào project:
cp ~/reference/design-md/linear/DESIGN.md ./DESIGN.md
```

### Antigravity
```bash
# Không cần deploy service — chỉ là kho file tham khảo, clone về VPS để team dùng chung
git clone https://github.com/voltagent/awesome-design-md.git /opt/reference/design-md
```
> ⚠️ Nhớ phân biệt với bản Digiflex-solution/awesome-design-md (repo trùng tên, ít nội dung hơn) — luôn dùng bản voltagent.

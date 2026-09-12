---
name: brand-building-skills
description: >
  Stars: 311 Tác giả: arnabbagxd Domain: Brand strategy/naming/identity/voice/positioning
---

# brand-building-skills — bộ skill xây thương hiệu từ 0 đến launch

**GitHub:** https://github.com/arnabbagxd/brand-building-skills
**Tác giả:** arnabbagxd | **Stars:** 311 | **Cài:** `npx skills add arnabbagxd/brand-building-skills`

---

## TL;DR

Bộ skill cho agent làm hết vòng đời xây brand: đặt tên, định vị, xây identity, viết voice, audit brand cũ, tới launch — có 1 file `brand-context` làm nền để mọi skill khác đọc trước khi chạy.

## Tool này dùng để làm gì

Giống cấu trúc `product-marketing` bên marketingskills — có 1 skill "brand-context" đóng vai trò lưu DNA thương hiệu (identity, audience, positioning, values, voice). Mọi skill khác (brand-strategy, brand-naming, brand-identity, brand-voice, brand-positioning, brand-messaging, brand-audit, brand-launch) đều đọc file này trước, đảm bảo đồng nhất khi làm nhiều task khác nhau cho cùng 1 brand.

Có thêm 2 skill chuyên biệt: `d2c-marketing` và `b2b-brand-marketing` cho 2 mô hình khác nhau.

## Setup từng bước

1. Cài qua CLI:
```bash
npx skills add arnabbagxd/brand-building-skills
```
2. CLI hỏi agent nào đang dùng (Claude Code/Cursor/Windsurf) → tự cài đúng thư mục
3. Chạy trước tiên skill `brand-context` để agent biết DNA brand của mình, rồi mới gọi các skill còn lại

## Ví dụ thực tế

Case cho ABTRIP: chạy `brand-context` khai identity là "dịch vụ hàng không đáng tin, nhanh, không rườm rà" → sau đó gọi `brand-voice` để ra bộ quy tắc giọng văn cho fanpage, gọi `brand-audit` để soi lại content cũ có lệch tông không.

## Lưu ý / Lỗi thường gặp

- Repo mới ra (3 tuần tuổi tính tới thời điểm research) — ít người dùng thử dài hạn, chưa rõ độ ổn định qua nhiều version
- Không thấy đề cập tích hợp MCP/tool ngoài — thuần là prompt/framework, không tự chạy data thật
- Vì mới, README có thể còn thay đổi cấu trúc skill trong các bản cập nhật tới

## Đánh giá cá nhân

- **Điểm mạnh:** tư duy modular giống marketingskills đã quen (context file dùng chung), phủ đủ vòng đời brand từ đặt tên tới launch, không phải chắp vá nhiều nguồn
- **Điểm yếu:** còn quá mới để đánh giá độ tin cậy lâu dài, không có ví dụ case study thật đi kèm trong README để đối chiếu chất lượng output
- **Có nên dùng không:** 6.5/10 — đáng thử cho brand mới (An Bình, Wonder Mart) nhưng đừng coi là nguồn duy nhất, nên đối chiếu thêm

## Link
- Repo: https://github.com/arnabbagxd/brand-building-skills

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Đây là skill markdown, không có API — Hermes không gọi trực tiếp được.
# Nếu cần dùng logic tương tự ngoài Claude, phải tự đọc nội dung SKILL.md và implement lại framework.
import urllib.request

def fetch_skill_content(skill_name):
    url = f"https://raw.githubusercontent.com/arnabbagxd/brand-building-skills/main/skills/{skill_name}/SKILL.md"
    req = urllib.request.Request(url, headers={"User-Agent": "hermes"})
    return urllib.request.urlopen(req).read().decode()
```

### OpenClaw
```bash
npx skills add arnabbagxd/brand-building-skills
# hoặc chỉ cài 1 skill cụ thể:
npx skills add arnabbagxd/brand-building-skills --skill brand-voice
```

### Antigravity
```bash
# Không cần deploy service — chỉ là file markdown local, không có phần backend nào để host
```
> ⚠️ Repo còn non — kiểm tra lại README mỗi lần update vì cấu trúc skill có thể đổi tên/gộp giống marketingskills đã từng làm ở bản v2.0.

---
name: strix
description: >
  AI pentest agent mo nguon mo — tu dong tim va vai luong khac nhau de phat
  hien lo hong bao mat trong app cua may, roi de xuat fix. 27.8K stars,
  Apache 2.0. Tich hop CI/CD: tu dong scan moi pull request.
---

# Strix — GitHub Repo

## TL;DR
AI pentest agent mo nguon mo — tu dong tim va vai luong khac nhau de phat hien lo hong bao mat trong app cua may, roi de xuat fix. 27.8K stars, Apache 2.0. Tich hop CI/CD: tu dong scan moi pull request.

## Repo nay dung de lam gi
Pentest thuong can chuyen gia bao mat $$$ hoac tool enterprise dat tien. Strix dan chu hoa bang AI agent tu hack chinh app cua may:

**Quy trinh:**
```
strix --target ./my-app
→ recon: mapping attack surface
→ probing endpoints (vd: /api/v1/cart/add)
→ tim lo hong: SQL injection, XSS, broken auth, IDOR...
→ verify khai thac duoc that (khong false positive)
→ de xuat fix cu the
```

**Tich hop CI/CD:**
Strix chay tu dong tren moi pull request — block code co lo hong truoc khi merge vao production.

## Setup tung buoc

> ⚠️ **Cập nhật 04/11/2026 (đã kiểm một phần):** lệnh `--ci-mode` ở dưới KHÔNG còn tồn tại. Tao cài `strix-agent` 1.7.0 vào venv cách ly và đọc `strix --help`: chế độ CI hiện là `-n` (không tương tác) kèm `-m quick` (hoặc `standard`, `deep`) và tuỳ chọn `--fail-on <mức>` (thoát mã 2 khi có lỗ hổng từ mức đó trở lên). Ví dụ: `strix -n --target . -m quick --fail-on high`. `pip install strix-agent` vẫn cài được. README gốc hiện khuyên cài bằng `curl -sSL https://strix.ai/install | bash` (tao không kiểm được vì mạng bị chặn). Cần Docker đang chạy và khoá LLM. Lệnh `docker run strix/strix` ở dưới tao chưa kiểm. Số sao hiện khoảng 72 nghìn theo README, không còn là 27.8K. Dùng trong Claude Code: `npx skills add usestrix/strix` (README nói thêm 9 skill, tao chưa chạy). Tao chưa chạy quét lần nào. Chỉ quét hệ thống mày sở hữu hoặc có văn bản cho phép. Bản gộp cài đặt: `stacks/claude-code-4-plugin-nen-cai.md`.

```bash
# Cai qua pip
pip install strix-agent

# Chay scan local
strix --target ./my-app

# Hoac qua Docker
docker run -v $(pwd):/target strix/strix --target /target

# Tich hop GitHub Actions
# .github/workflows/strix-scan.yml
name: Strix Security Scan
on: [pull_request]
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install strix-agent
      - run: strix -n --target . -m quick --fail-on high   # đã sửa 04/11/2026: --ci-mode không còn
```

## Vi du thuc te

**Scan ABTRIP booking API truoc khi deploy:**
```bash
strix --target ./abtrip-api

→ recon: mapping attack surface...
→ probing endpoints /api/v1/booking/create
→ FOUND: SQL injection o tham so 'tour_id'
→ FOUND: Khong co rate limit o /api/v1/login → brute force risk
→ De xuat fix: parameterized query, them rate limiter
```

Chay truoc moi lan deploy len production — bat loi som, khong de hacker that tim ra truoc.

## Ket hop voi HERMES-AGENTS.md

```
Hermes code xong feature moi
    ↓
Strix tu dong scan (CI/CD trigger)
    ↓
Neu co lo hong → bao Nobitano qua Telegram, KHONG deploy
    ↓
Neu sach → tiep tuc deploy binh thuong
```

Them buoc nay vao Verification Checklist cua HERMES-AGENTS.md.

## Luu y / Loi thuong gap
- AI pentest van co the miss mot so lo hong phuc tap — khong thay the audit thu cong cho production lon
- Chi scan code/API cua chinh may — khong dung de pentest he thong nguoi khac (vi pham phap luat)
- Can config ky de tranh false positive lam phien CI/CD pipeline

## Danh gia ca nhan
- Diem manh: Dan chu hoa pentest; tich hop CI/CD muot; tu verify khong false positive; Apache 2.0 license thoai mai
- Diem yeu: Khong thay the security audit chuyen nghiep cho production critical; can hieu co ban ve security de doc output dung
- Co nen dung khong: **8.5/10** — Them vao CI/CD pipeline cua ABTRIP/Wonder Mart truoc khi co payment/booking system di production. Layer bao ve dau tien, khong phai cuoi cung.

## Link
- Repo: https://github.com/usestrix/strix
- Docs: https://docs.strix.ai
- Website: https://strix.ai
- License: Apache 2.0

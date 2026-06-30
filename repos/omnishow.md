# OmniShow — GitHub Repo

## TL;DR
Model video generation cua ByteDance, paper duoc accept tai ICML 2026 — tao video tuong tac nhan vat-vat the (human-object interaction). 436 stars, con moi va academic-focused, chua phai production tool.

## Repo nay dung de lam gi
Khac voi Seedance (da co trong kho — text/image to video tong quat), OmniShow chuyen sau ve mot bai toan kho: **tao video nguoi tuong tac voi vat the chinh xac** — cam do vat, ngoi ghe, mo cua, dap bong... nhung dong tac AI video thuong lam sai tu the hoac vat the bi bien dang.

**Paper context:**
- Cong bo tai ICML 2026 (top-tier ML conference)
- Tac gia tu ByteDance research
- Code + model weights public tren GitHub

## Setup tung buoc

```bash
git clone https://github.com/Correr-Zhou/OmniShow
cd OmniShow

# Cai dependencies (thuong nang, can GPU manh)
pip install -r requirements.txt

# Cac thu muc chinh:
# _synth/  → data synthesis
# _infer/  → chay inference (tao video)
# _train/  → training tu dataset rieng

# Chay inference (vi du)
python _infer/generate.py --prompt "person picking up a cup" --output result.mp4
```

## Luu y quan trong truoc khi dung
- **Day la research code, khong phai production-ready tool** — code paper thuong thieu polish, docs so sai
- Can GPU manh (paper-grade model thuong can A100 hoac tuong duong) — khong chay tot tren may thuong
- License can kiem tra ky — code tu paper academic co the co restriction khac code thuong
- Setup phuc tap hon nhieu so voi Seedance hay cac video tool da co trong kho

## Danh gia ca nhan
- Diem manh: Cutting-edge research tu ByteDance; giai quyet bai toan kho (human-object interaction) ma cac tool khac lam chua tot; ICML 2026 = duoc peer-review chat luong
- Diem yeu: Con qua moi (436 stars); kha nang la academic code can nhieu set up; can GPU manh; chua ro production readiness
- Co nen dung khong: **6/10** — Theo doi de biet trend, nhung chua nen dung production ngay. Cho 2-3 thang de community polish code va co wrapper de dung hon, hoac doi ByteDance integrate vao Seedance/Dreamina.

## Link
- Repo: https://github.com/Correr-Zhou/OmniShow
- Paper: ICML 2026
- Note: Research code, khong phai production tool

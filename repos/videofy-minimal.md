---
name: videofy-minimal
description: >
  Tool local bien bai bao/tin tuc thanh video ngan cho man hinh digital
  signage — fetch noi dung, viet kich ban, ghep hinh, tao giong doc
  (ElevenLabs), render qua Remotion, co CMS UI review truoc khi render. Ban
  rut gon (minimal) cua he thong Videofy noi bo cua Schibsted (tap doan bao
  chi Bac Au). 623 stars, Apache-2.0.
---

# Videofy Minimal (schibsted/videofy_minimal) — GitHub Repo

## TL;DR
Videofy Minimal la ban rut gon, mo nguon cua he thong noi bo "Videofy" ma Schibsted (tap doan
bao chi lon o Bac Au, so huu nhieu newsroom) dung de tu dong bien bai bao thanh video ngan
chieu tren man hinh digital signage. Repo nay giu nguyen luong lam viec cot loi nhung bo bot
phan tich hop noi bo — chi can OpenAI + ElevenLabs API key la chay duoc tren 1 laptop.

## Repo nay dung de lam gi
Van de goc: newsroom co hang tram bai viet moi ngay, nhung lam video tu tay tung bai qua cham
de kip dang len man hinh cong cong/social. Videofy Minimal tu dong hoa toan bo pipeline:

1. **Fetch** - lay noi dung tu Reuters, AP, hoac 1 URL web bat ky (fetcher dang plugin, de them
   nguon rieng)
2. **Generate manuscript** - AI viet lai thanh kich ban ngan, chon dung giong dieu theo brand
3. **Match media** - ghep hinh anh/video minh hoa phu hop noi dung
4. **Narration** - tao giong doc bang ElevenLabs
5. **Preview + Review (CMS UI)** - editor xem truoc, sua tay, chay lai truoc khi render that -
   day la diem khac biet lon nhat: co "human-in-the-loop" that su, khong phai 1-click-la-xong
   mu quang
6. **Render** - dung **Remotion** de composite va xuat MP4 that (ca vertical va horizontal)

Kien truc: CMS (Next.js) dieu phoi, goi qua FastAPI (Python) de xu ly AI + luu project. Moi
lan chay la 1 project luu tai `projects/<projectId>/`, chia ro `input/` (bai goc) →
`working/` (kich ban, audio, config dang sua) → `output/` (video render xong).

**Brand system** rieng biet - moi brand la 1 file JSON dinh nghia prompt, model OpenAI, giong
TTS, logo, intro/outro wipe, mau sac, theme hinh anh - doi brand la doi 1 file, khong sua code.

## Setup tung buoc
```bash
# macOS qua Homebrew
brew install uv node ffmpeg

cp .env.example .env
# them vao .env: OPENAI_API_KEY, ELEVENLABS_API_KEY

uv sync
npm install

make dev
# CMS: http://127.0.0.1:3000
# API: http://127.0.0.1:8001

# Hoac chay qua Docker Compose (doc file .env tuong tu)
docker compose up --build
```
Them brand moi: copy `brands/default.json` → doi ten `brands/<ten-brand>.json` → sua logo,
wipe, mau, prompt, giong noi → restart app la chon duoc brand moi trong CMS.

## Vi du thuc te
Ap dung cho kenh **Airfare Decoded** hoac **Trum San Bay** cua Nobitano - ca 2 deu can noi
dung dua tren tin tuc/insight nganh hang khong cap nhat lien tuc:
1. Viet 1 fetcher rieng (`fetchers/aviation-news/`) lay tin tu nguon hang khong (thay vi
   Reuters/AP mac dinh) - kien truc plugin cho phep them nguon tuy y
2. Tao brand rieng `brands/trum-san-bay.json` voi mau Deep Navy/Hanoi Gold, giong doc phu hop
   persona "Trum", logo silhouette da co san
3. Moi khi co tin ngan (vd thay doi gio bay, quy dinh hanh ly moi), fetch → AI viet kich ban →
   editor (Nobitano) review nhanh trong CMS truoc khi render - dung buoc nay thay the cho
   Brand Check agent thu cong trong pipeline 9-agent hien tai cho nhung tin tuc ngan, don gian
4. Render xong ra ca vertical (TikTok) va horizontal (YouTube) cung luc

## Luu y / Loi thuong gap
- **Remotion co license rieng** - repo canh bao ro: "for commercial use, verify your usage
  complies with Remotion license terms. You might need a license." ABTRIP/Wonder Mart la kinh
  doanh thuong mai, can kiem tra dieu khoan Remotion truoc khi dung production (Remotion mien
  phi cho ca nhan/cong ty nho, tra phi cho cong ty tu 3 dev toan thoi gian tro len hoac doanh
  thu vuot nguong - can doc ky remotion.dev/license)
  cua Schibsted - fetcher Reuters/AP can credential rieng (khong mien phi), chi fetcher `web`
  (HTML generic) la dung duoc ngay khong can dang ky gi
- Hotspot model (chon vung focus tren anh bao chi) can tai model tu Hugging Face qua
  `uv sync --group hotspot` - neu mang khong on dinh se fallback ve chien luoc focus mac dinh,
  van chay duoc nhung kem chinh xac hon

## Danh gia ca nhan
- Diem manh: co "human-in-the-loop" that su qua CMS UI (khac han cac tool "1-click video" hoan
  toan tu dong nhu Short Video Factory), kien truc fetcher dang plugin de mo rong nguon, brand
  system tach rieng gon gang, dung Remotion nen tan dung duoc kien thuc composition da co san
  cua Nobitano tu vu skillops video vua lam
- Diem yeu: can 2 API key tra phi (OpenAI + ElevenLabs) moi khi chay, license Remotion can kiem
  tra ky cho muc dich thuong mai, chua co release chinh thuc (repo con moi, 10 commit)
- Co nen dung khong: 7/10 - dang thu nghiem cho case tin tuc-ngan-hang-ngay (Trum San Bay,
  Airfare Decoded), nhung phai doc license Remotion truoc khi dua vao production thuong mai,
  va nen viet fetcher rieng thay vi phu thuoc Reuters/AP tra phi

## Link
- Repo: https://github.com/schibsted/videofy_minimal
- Video vi du: https://github.com/schibsted/videofy_minimal/blob/main/example_video_e24.mp4
- Discord ho tro: https://discord.gg/vFvvdC3B
- Remotion license (can doc truoc khi dung thuong mai): https://www.remotion.dev/license

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Videofy Minimal expose FastAPI o port 8001 khi chay local/VPS
import urllib.request, json

VIDEOFY_API = "http://localhost:8001"

def trigger_generation(project_config: dict):
    payload = json.dumps(project_config).encode()
    req = urllib.request.Request(
        f"{VIDEOFY_API}/generate",  # endpoint cu the xem them trong api/ cua repo
        data=payload, headers={"Content-Type": "application/json"}, method="POST"
    )
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
# Chay ca CMS (Next.js) + API (FastAPI) qua Docker Compose tren VPS
git clone https://github.com/schibsted/videofy_minimal.git
cd videofy_minimal
cp .env.example .env   # dien OPENAI_API_KEY, ELEVENLABS_API_KEY that
docker compose up --build -d
```

### Antigravity
```bash
# Quan ly bang pm2 neu chay khong qua Docker
cd /opt/videofy_minimal
uv sync && npm install
pm2 start "make dev" --name videofy-minimal
```
> ⚠️ Kiem tra dieu khoan license Remotion truoc khi dung cho video ABTRIP/Wonder Mart (muc
> dich thuong mai) — https://www.remotion.dev/license. Ngoai ra API key OpenAI/ElevenLabs
> phai dat qua `.env`, khong bao gio hardcode trong docker-compose.yml khi push len repo.

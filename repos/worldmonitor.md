---
name: worldmonitor
description: >
  Dashboard tinh bao toan cau real-time — 500+ nguon tin, 15 category (dia
  chinh tri, tai chinh, hang khong, nang luong, khi hau, quan su, cyber...),
  Country Instability Index cho 31 nuoc, radar tai chinh 29 san giao dich.
  Co MCP server rieng (39 tool), CLI, SDK Python/Ruby/Go. Chay local hoan
  toan mien phi qua Ollama, khong can API key. 64.3K stars, AGPL-3.0.
---

# World Monitor (koala73/worldmonitor) — GitHub Repo

## TL;DR
World Monitor la 1 dashboard "tinh bao tinh huong" (situational awareness) tong hop hon 500
nguon tin thanh 1 giao dien duy nhat — dia chinh tri, tai chinh, hang khong, nang luong, khi
hau, quan su, an ninh mang. Diem manh nhat cho kho AI-Vibe-Toolkit: co san **MCP server** de
Claude/agent query truc tiep du lieu song, va co ca **du lieu bay ADS-B that** tu Wingbits -
lien quan truc tiep toi mang hang khong cua ABTRIP.

## Repo nay dung de lam gi
Day la ban do tinh huong toan cau kieu "Palantir cho nguoi thuong" (repo tu gan tag `palantir`
tren GitHub) - thay vi mo 20 tab tin tuc rieng le, World Monitor gom lai:

- **500+ nguon tin curated**, 15 category, AI tong hop thanh brief ngan
- **Ban do doi 3D (globe.gl)** va **ban do 2D deck.gl** voi 56 loai layer
- **Country Instability Index (CII v8)** - cham diem bat on cho 31 nuoc Tier-1, server-side
- **Radar tai chinh** - 29 san giao dich chung khoan, hang hoa, crypto, composite 7-tin-hieu
- **Du lieu bay ADS-B** tu Wingbits - theo doi chuyen bay real-time
- **6 bien the site** tu 1 codebase: world / tech / finance / commodity / happy / energy
- **Local AI** - chay hoan toan qua Ollama, khong can API key tra phi nao
- App desktop native (Tauri 2) cho Windows/macOS/Linux, 25 ngon ngu

**Truy cap cho agent/script** (day la phan quan trong nhat voi kho):
- MCP server: `https://worldmonitor.app/mcp` (Streamable HTTP), `tools/list` cong khai,
  `tools/call` xac thuc bang header `X-WorldMonitor-Key`
- REST API: `https://api.worldmonitor.app`, co OpenAPI spec
- CLI: `npx worldmonitor tools` (xem het tool khong can key) hoac `npm install -g worldmonitor`
- SDK chinh thuc: Python (`pip install worldmonitor-sdk`), Ruby (`gem install worldmonitor`),
  Go

## Setup tung buoc
```bash
# Chay local (mien phi, khong can bien moi truong nao)
git clone https://github.com/koala73/worldmonitor.git
cd worldmonitor
npm install
npm run dev
# mo http://localhost:3000

# Chi muon dung API/MCP tu xa, khong tu host:
npx worldmonitor tools              # liet ke tool MCP, khong can key
pip install worldmonitor-sdk        # SDK Python cho Hermes
```
Lay API key tai `worldmonitor.app/pro` neu can rate limit cao hon / du lieu near-real-time
(free tier refresh 5-15 phut, Pro gan real-time).

## Vi du thuc te
Ap dung truc tiep cho **An Binh Airport Services / ABTRIP** va **Trum San Bay**:
1. Query MCP tool ve du lieu bay ADS-B qua khu vuc Noi Bai/Ha Noi - biet som neu co bat
   thuong (delay hang loat, thay doi lich trinh khu vuc) truoc khi khach hoi Fast Track
   Noi Bai
2. Dung Country Instability Index + tin tuc dia chinh tri lam nguon cho noi dung "Trum San
   Bay" (insider tips) - vd canh bao gian doan do bat on khu vuc anh huong lich bay
3. Radar tai chinh (29 san giao dich, commodity) co the lam nguon so lieu cho script video
   "tu duy tai chinh vi mo" (script #172) da co trong content/, thay vi tu tong hop tay
4. Hermes goi qua SDK Python truc tiep, khong can tu host toan bo dashboard - chi dung phan
   API/MCP la du cho muc dich lay du lieu

## Luu y / Loi thuong gap
- **License AGPL-3.0** - quan trong phai doc ky: tu host/fork/sua code deu duoc phep kinh
  doanh duoi AGPL, NHUNG neu sua code va cung cap nhu 1 dich vu (SaaS) cho nguoi khac dung,
  bat buoc phai cong khai source theo dieu khoan AGPL. Neu chi dung API/MCP/SDK cong khai
  (khong tu sua code va host lai) thi khong dinh nghia vu nay - day la cach an toan nhat cho
  ABTRIP neu khong muon rang buoc copyleft
- Co giay phep thuong mai rieng (non-AGPL) neu can dung proprietary khong cong khai source -
  lien he qua worldmonitor.app
- Feature theo tung nguon du lieu co the can credential rieng (xem `.env.example` day du) -
  chi ban chay co ban khong can bien moi truong nao

## Danh gia ca nhan
- Diem manh: quy mo du lieu that su lon (500+ nguon, 65+ provider, 35 nhom nguon duoc theo doi
  do tuoi), co san MCP + SDK da ngon ngu nen tich hop vao Hermes/OpenClaw gan nhu ngay lap tuc,
  option chay Local AI qua Ollama nghia la khong ton chi phi API neu chi can du lieu tho
- Diem yeu: AGPL-3.0 la license "nang" hon MIT/Apache rat nhieu, phai hieu ro truoc khi tich
  hop sau vao san pham thuong mai (ABTRIP); du lieu ADS-B/tai chinh chi tot bang chat luong
  nguon thu 3 (Wingbits, cac san giao dich) - khong tu kiem chung duoc
- Co nen dung khong: 8/10 - dang tich hop ngay o muc **chi dung API/MCP/SDK** (khong tu host
  sua code) cho ca ABTRIP (du lieu bay) va content (Trum San Bay, script tai chinh vi mo) -
  day chinh xac la loai nguon du lieu "tinh bao" ma kho dang thieu, chi can than voi dieu
  khoan AGPL neu sau nay muon tu host ban da sua

## Link
- Repo: https://github.com/koala73/worldmonitor
- Docs: https://www.worldmonitor.app/docs/documentation
- MCP: https://worldmonitor.app/mcp
- API key (Pro): https://www.worldmonitor.app/pro
- License chi tiet: https://github.com/koala73/worldmonitor/blob/main/docs/license.mdx

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Dung SDK chinh thuc thay vi tu goi API tay
# pip install worldmonitor-sdk --break-system-packages
from worldmonitor import WorldMonitorClient

client = WorldMonitorClient(api_key="wm_xxx")  # lay tai worldmonitor.app/pro

def check_aviation_signals(region="hanoi"):
    return client.aviation.flights(region=region)

def get_country_risk(country_code="VN"):
    return client.risk.country(country_code)
```

### OpenClaw
```bash
# Dung CLI de query nhanh khong can code, phu hop cho lenh Telegram
npx worldmonitor tools                        # liet ke tool, khong can key
worldmonitor risk VN --api-key wm_xxx         # vi du: chi so bat on Viet Nam
```

### Antigravity
```bash
# Neu muon co dashboard rieng (khong bat buoc cho muc dich lay du lieu qua API/MCP)
git clone https://github.com/koala73/worldmonitor.git /opt/worldmonitor
cd /opt/worldmonitor && npm install
pm2 start "npm run dev" --name worldmonitor-dashboard
```
> ⚠️ Chi tu host + sua code khi that su can dashboard rieng. Neu chi can du lieu cho
> Hermes/agent, dung API/MCP/SDK cong khai la du va khong dinh nghia vu cong khai source
> theo AGPL-3.0. Doc ky `docs/license.mdx` truoc khi quyet dinh huong nao.

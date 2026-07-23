---
name: flowise
description: >
  Nen tang low-code keo-tha de xay AI Agent va LLM workflow, dua tren
  LangChain. 2 builder chinh: Agentflow (multi-agent) va Chatflow (chatbot
  don). Tich hop 100+ LLM/vector DB/document loader (PDF, Notion, GitHub,
  Google Drive...). Tu host mien phi, co ban Cloud, REST API rieng cho tung
  flow. ~53K+ stars, mature va duoc dung production o nhieu cong ty.
---

# Flowise (FlowiseAI/Flowise) — GitHub Repo

## TL;DR
Flowise la nen tang keo-tha (drag & drop) de xay AI Agent va LLM workflow ma khong can code
nhieu, dung LangChain lam engine ben duoi. Diem manh la toc do prototype cuc nhanh (vai phut
la co 1 chatbot/agent chay duoc) va thu vien tich hop khong lo (100+ LLM, vector DB, document
loader). Tu host duoc hoan toan mien phi, co ca ban cloud va enterprise (SSO/RBAC) neu can.

## Repo nay dung de lam gi
Flowise giai quyet van de: xay 1 AI agent/chatbot tu dau bang code (LangChain thuan) ton thoi
gian boilerplate, kho demo nhanh cho nguoi khong biet code xem truoc y tuong co on khong.

2 builder chinh:
- **Chatflow** - xay chatbot/agent don, ho tro RAG, tool calling, memory - hop cho use case
  "tra loi khach hang dua tren tai lieu"
- **Agentflow** - xay he thong multi-agent, dieu phoi workflow phan tan qua nhieu agent phoi
  hop - hop cho use case can nhieu buoc, nhieu vai tro (giong kien truc Manager/Research/
  Analysis/Execution Agent)

Data ingestion ket noi hon 100 nguon: file PDF/CSV/Excel/Docx, va dich vu nhu Notion, GitHub,
Google Drive, Jira. Tuong thich 100+ LLM, embedding, vector DB khac nhau. Deploy duoc qua
Docker, Railway (1-click template co san), hoac tu host tren VPS rieng.

## Setup tung buoc
```bash
# Cach 1 - npx nhanh nhat de thu
npx flowise start

# Cach 2 - Docker (khuyen nghi cho production/VPS)
git clone https://github.com/FlowiseAI/Flowise.git
cd Flowise/docker
cp .env.example .env
# sua .env: dat FLOWISE_USERNAME, FLOWISE_PASSWORD, DATABASE_URL
docker compose up -d

# Cach 3 - build tu source (mono-repo, can Node.js, PNPM)
pnpm install
pnpm build
pnpm start
```
Neu gap loi `JavaScript heap out of memory` luc build, tang heap truoc khi chay:
```bash
export NODE_OPTIONS="--max-old-space-size=4096"
```

## Vi du thuc te
Ap dung cho ke hoach "Deploy Chatwoot cho ABTRIP customer support" dang nam trong on the
horizon cua Nobitano:
1. Thay vi tu code toan bo logic RAG + tool-calling cho chatbot ABTRIP bang Python tu dau,
   dung Flowise de prototype nhanh 1 Chatflow: upload tai lieu chinh sach Fast Track Noi Bai
   (PDF), noi vao 1 vector DB, cau hinh prompt tra loi theo brand voice "The quiet difference"
2. Test thu ngay tren UI keo-tha xem chatbot tra loi co dung khong, chinh sua prompt/luong
   truc tiep khong can deploy lai code
3. Khi da on, goi Flowise qua REST API rieng cua tung flow (`/api/v1/prediction/<chatflow-id>`)
   tu Chatwoot webhook hoac tu Hermes - khong can Flowise biet gi ve ha tang con lai cua kho

Luu y: day la cach dung Flowise nhu 1 lop prototype/production nhe, khong phai thay the toan
bo Hermes/OpenClaw - 2 he thong nay van la orchestrator chinh.

## Luu y / Loi thuong gap
- Dua tren LangChain.js - neu kho da quen pattern Python thuan (Hermes dung urllib, khong
  framework ngoai), Flowise dua them 1 stack Node.js/LangChain rieng can maintain song song
- Build tu source de gap loi out-of-memory tren may cau hinh thap - can tang `NODE_OPTIONS`
- Tu host thi phai tu lo bao mat (dat `FLOWISE_USERNAME`/`FLOWISE_PASSWORD`, khong de mac dinh
  public), khac voi ban cloud da co san auth

## Danh gia ca nhan
- Diem manh: toc do prototype nhanh nhat trong cac tool tuong tu, thu vien tich hop cuc lon
  (100+ nguon du lieu), co REST API rieng cho moi flow nen de goi tu he thong khac vao, mature
  va da duoc nhieu cong ty dung production that (khong phai demo suong)
  o quy mo nho co the du, nhung neu kho can logic phuc tap/custom (nhu guardrail rieng cho
  agent tai chinh, hay state machine code-driven chong prompt injection) thi Flowise khong
  linh hoat bang tu viet Python/Node thuan
- Co nen dung khong: 7/10 - rat dang thu cho viec **prototype nhanh** chatbot ABTRIP/Wonder
  Mart truoc khi quyet dinh co dang tu code rieng hay khong, nhung khong nen thay the
  Hermes/OpenClaw lam orchestrator chinh cua he sinh thai

## Link
- Repo: https://github.com/FlowiseAI/Flowise
- Docs: https://docs.flowiseai.com/
- Website: https://flowiseai.com/
- Railway 1-click deploy: https://railway.com/deploy/flowise

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Flowise expose REST API rieng cho tung flow da tao, goi thang bang urllib
import urllib.request, json

FLOWISE_HOST = "http://localhost:3000"  # hoac domain VPS da deploy
CHATFLOW_ID = "xxxxx-xxxx-xxxx"  # lay tu URL flow trong Flowise UI

def query_flowise(question):
    payload = json.dumps({"question": question}).encode()
    req = urllib.request.Request(
        f"{FLOWISE_HOST}/api/v1/prediction/{CHATFLOW_ID}",
        data=payload, headers={"Content-Type": "application/json"}, method="POST"
    )
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
# Chay Flowise nhu 1 service rieng tren VPS, OpenClaw goi qua HTTP nhu 1 tool ben ngoai
npx flowise start --PORT=3000
# hoac deploy Docker (xem Setup tung buoc)
```

### Antigravity
```bash
# Deploy Docker production tren VPS, quan ly qua pm2/docker compose
cd /opt && git clone https://github.com/FlowiseAI/Flowise.git
cd Flowise/docker
cp .env.example .env   # dat FLOWISE_USERNAME, FLOWISE_PASSWORD, DATABASE_URL that
docker compose up -d
```
> ⚠️ Mac dinh Flowise UI khong co auth neu khong dat `FLOWISE_USERNAME`/`FLOWISE_PASSWORD` —
> bat buoc dat truoc khi expose port ra ngoai internet tren VPS cong khai.

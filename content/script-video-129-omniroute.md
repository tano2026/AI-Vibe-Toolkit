# Script Video 129 — OmniRoute: 1.6B Token Mien Phi Moi Thang, 1 Endpoint, 231 Provider

## Thong tin
- Repo lien quan: /repos/omniroute.md
- Platform: TikTok / YouTube Shorts
- Thoi luong du kien: ~60 giay

## Hook (3 giay dau)
"1.6 ty token mien phi moi thang. 231 provider. 1 endpoint. Cai 2 phut."

## Script voiceover
[Doan 1 - pain point]
May dang tra tien API Claude, GPT, Gemini moi thang cho Hermes va OpenClaw. Nhung co hang chuc provider dang cho free tier may chua dung het — vi qua phuc tap de stack.

[Doan 2 - giai phap]
OmniRoute gom tat ca lai: Mistral 1 ty token, Groq 117 trieu, Gemini 60 trieu, Cloudflare, Cerebras, SambaNova... Tong cong 1.6 ty token mien phi moi thang, gom thanh 1 endpoint local duy nhat OpenAI-compatible.

[Doan 3 - dem mo]
Chay npx omniroute — xong. Tro tat ca tool cua may vao localhost 20128. Khi het rate limit cua Groq, no tu dong switch sang Gemini, roi Mistral. May khong biet gi ca — cu goi, no tu xay.

Con co compression RTK Caveman: nen prompt truoc khi gui, tiet kiem them 15 den 95 phan tram token. Tool nang nhat cung chay duoc lau gap doi.

[Doan 4 - ket + CTA]
7.1 nghin star, Antigravity integration chinh thuc, MIT license. Deploy len VPS la xong. Link trong bio.

## Ghi chu quay (OBS)
- Canh 1: Terminal: npx omniroute → server starts in 5 giac
- Canh 2: Dashboard http://localhost:20128/dashboard — bang free tier dep
- Canh 3: Hermes goi endpoint → OmniRoute auto-route sang Groq → het han → switch Gemini → tiep tuc
- Canh 4: Token compression demo: 69 tokens → 23 tokens, same meaning

## Thumbnail idea (Canva)
Logo 6 provider (Mistral, Groq, Gemini, Cloudflare, Cerebras, SambaNova) → ket vao 1 diem "OmniRoute". Text lon: "1.6B TOKEN MIEN PHI"

## CTA cuoi video
"Deploy OmniRoute len VPS — agent stack cua may chay mien phi mai mai. Link trong bio."

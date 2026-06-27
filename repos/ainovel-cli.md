# ainovel-cli — GitHub Repo

## TL;DR
Multi-agent CLI viết web novel tự dong bang AI — Go, 1.1K stars, dang trending. Giao chu de, no tu tao outline, viet tung chuong, kiem tra nhat quan nhan vat, xuat file hoan chinh. Content creator viet truyen dai khong can ngoi viet tay.

## Repo nay dung de lam gi
Viet web novel dai bang AI thuong gap van de: AI quen nhan vat o chuong truoc, plot hole, van phong khong nhat quan. ainovel-cli giai quyet bang kien truc multi-agent:
- **Planner agent:** Tao outline tong the, arc nhan vat
- **Writer agent:** Viet tung chuong theo outline
- **Reviewer agent:** Kiem tra nhat quan plot va nhan vat
- **Editor agent:** Chinh sua van phong, loai bo lap

Chay CLI, tu dong toan bo pipeline. Output: file novel hoan chinh co the xuat ban.

## Setup tung buoc
```bash
# Cai Go (neu chua co)
# go.dev/dl

# Clone va build
git clone https://github.com/voocel/ainovel-cli
cd ainovel-cli
go build -o ainovel ./cmd/main.go

# Config API key
cp config.example.yaml config.yaml
# Edit: them ANTHROPIC_API_KEY hoac OPENAI_API_KEY

# Tao novel dau tien
./ainovel create --title "Ten Truyen" --genre "fantasy" --chapters 20

# Tiep tuc viet tu chuong dung lai
./ainovel continue --id novel_id --from-chapter 5
```

## Vi du thuc te
**Input:** `./ainovel create --title "Nguoi Hung AI" --genre "sci-fi" --chapters 30 --lang vi`

**Output sau ~2-3 tieng:**
- 30 chuong, moi chuong ~2000 tu
- Nhan vat nhat quan xuyen suot
- Plot khong bi hole
- File .txt va .epub xuat ban duoc

## Luu y / Loi thuong gap
- Token tieu thu lon: 30 chuong ~ $5-15 tuy model
- Nen dung DeepSeek V3 de tiet kiem chi phi (re hon GPT-4 nhieu)
- Novel tieng Viet: them `--lang vi` va prompt system bang tieng Viet
- Chuong dai > 3000 tu hay bi cat — giam xuong 2000 tu la on

## Danh gia ca nhan
- Diem manh: Multi-agent that su hieu qua cho noi dung dai; Go = nhanh; config don gian
- Diem yeu: Con it star (1.1K), community nho; tieng Viet chua test ky; ton token
- Co nen dung khong: **7.5/10** — Hay cho content creator muon thu nghiem AI fiction. Dung DeepSeek de giam cost. Neu lam kenh truyen AI thi dang de xem.

## Link
- Repo: https://github.com/voocel/ainovel-cli
- Language: Go

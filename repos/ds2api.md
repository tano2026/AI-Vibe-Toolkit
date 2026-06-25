# DS2API — GitHub Repo

## TL;DR
Biến tài khoản web DeepSeek thành API endpoint chuẩn OpenAI format — bypass giới hạn API chính thức, dùng được với mọi tool support OpenAI API. 4,700+ sao GitHub.

## Repo này dùng để làm gì
DS2API (`CJackHwang/ds2api`) là middleware viết bằng Go, chạy giữa app của mày và DeepSeek web. Khi DeepSeek API chính thức bị giới hạn hoặc hết quota, DS2API cho phép dùng session web (cookie) để tạo API endpoint giả lập.

Tại sao cần:
- DeepSeek API chính thức hay bị rate limit hoặc down
- DeepSeek web miễn phí không giới hạn (trên lý thuyết)
- Nhiều tool chỉ support OpenAI format → DS2API bridge cái đó

Cách hoạt động: mày lấy cookie từ session web DeepSeek → DS2API giả lập server OpenAI → app của mày gọi `http://localhost:8080/v1/chat/completions` như gọi OpenAI thật.

## Setup từng bước
1. Download binary hoặc build từ source:
```bash
git clone https://github.com/CJackHwang/ds2api
cd ds2api
go build -o ds2api .
```
2. Lấy cookie từ DeepSeek web:
   - Mở deepseek.com → Login → F12 → Network tab
   - Gửi 1 message → click request chat → copy cookie từ headers
3. Config và chạy:
```bash
./ds2api -cookie "YOUR_DEEPSEEK_COOKIE_HERE" -port 8080
```
4. Test:
```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-chat","messages":[{"role":"user","content":"Hello"}]}'
```
5. Dùng với bất kỳ tool nào support OpenAI API: set `base_url=http://localhost:8080/v1`, `api_key=any_string`

## Ví dụ thực tế
**Bài toán:** Mày đang build automation tool dùng DeepSeek nhưng API chính thức hết quota giữa tháng.

**Cách dùng DS2API:**
1. Chạy DS2API với cookie của tài khoản DeepSeek web (dùng tài khoản khác, không dùng tài khoản trả phí)
2. Point tool của mày về `http://localhost:8080/v1`
3. Tool chạy bình thường, không biết đang hit web session

**Kết quả thực:** Tiết kiệm chi phí API, không bị gián đoạn khi API chính thức có vấn đề.

## Lưu ý / Lỗi thường gặp
- **Cookie hết hạn** → DeepSeek web session expire sau ~7 ngày → phải lấy cookie mới. Cân nhắc auto-refresh.
- **Rate limit từ DeepSeek web** → dùng nhiều quá cũng bị block IP/account. Đừng spam.
- **ToS violation** → kỹ thuật này vi phạm Terms of Service của DeepSeek. Dùng cho personal project, không dùng cho production thương mại.
- **Context window bị giới hạn** → web interface có giới hạn khác API chính thức

## Đánh giá cá nhân
- **Điểm mạnh:** Giải pháp nhanh khi cần bypass giới hạn API. Viết Go nên nhẹ và nhanh. Setup đơn giản.
- **Điểm yếu:** Vi phạm ToS — rủi ro bị khóa account. Cookie expire phải refresh. Không stable cho production. Chỉ dùng được khi có session web còn sống.
- **Có nên dùng không: 6/10** — Công cụ tình thế tốt khi bí API chính thức, nhưng đừng build production trên đây. Dùng cho personal automation, research, thử nghiệm.

## Link
- Repo: https://github.com/CJackHwang/ds2api
- Stars: 4,700+

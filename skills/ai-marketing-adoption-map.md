# AI Marketing Adoption Map — Prompt Template / System Prompt

## TL;DR
Skill tư vấn: nhận 1 mô tả về cách client (SME/cá nhân) đang làm marketing hiện tại, map ra client đang yếu ở khâu nào trong 8 khâu marketing (7 khâu vận hành + 1 khâu điều phối), rồi ra roadmap áp AI theo 3 giai đoạn — quick win tự làm, mid-term dùng tool có sẵn, dài hạn build agent pipeline của Tano Agency. Không phải content-writing skill, đây là **skill chẩn đoán + bán hàng tư vấn**.

## Khi nào dùng
- Client SME/cá nhân hỏi kiểu "AI giúp được gì cho marketing của tôi" — thay vì trả lời chung chung, dùng skill này để ra roadmap cụ thể theo đúng tình trạng họ.
- Tano Agency cần 1 bộ câu hỏi discovery chuẩn trước khi chào gói dịch vụ — output của skill này trực tiếp thành slide đề xuất (proposal).
- Client đã dùng AI lẻ tẻ (ChatGPT viết caption) nhưng chưa thấy hiệu quả rõ — dùng skill để chỉ ra họ đang chỉ chạm 1/8 khâu, còn 7 khâu kia vẫn làm tay.
- Không dùng khi: client đã biết rõ mình cần gì (vd "viết 10 caption TikTok") — lúc đó vào thẳng task, không cần chạy chẩn đoán toàn bộ pipeline.

## Nội dung skill / prompt

```
Bạn là cố vấn AI Marketing Adoption cho SME và cá nhân kinh doanh — không phải
người viết content thay, mà là người giúp họ nhìn ra AI nên chen vào đâu trong
quy trình marketing đang chạy, theo đúng quy mô và ngân sách của họ.

## Bước 1 — Thu thập tình trạng hiện tại (hỏi ngắn, không hỏi hết 1 lần)
Hỏi tối đa 3 câu để nắm được:
- Team marketing hiện có bao nhiêu người, ai làm gì
- Kênh đang chạy (social, ads, email, website...) và tần suất
- Điểm họ đang thấy tốn thời gian/đau đầu nhất

## Bước 2 — Map vào 8 khâu marketing
Đối chiếu tình trạng client với khung 8 khâu dưới đây, đánh giá mỗi khâu theo
3 mức: [Chưa làm] / [Làm tay] / [Đã có AI hỗ trợ]:

1. Nghiên cứu khách hàng & insight — tóm tắt review/comment, phân nhóm nỗi
   đau, tìm ngôn ngữ khách hàng, so đối thủ về thông điệp/định vị
2. Chiến lược & ý tưởng — brainstorm ý tưởng, content pillar, persona, kế
   hoạch content theo kênh, big idea chiến dịch
3. Sản xuất nội dung — caption, kịch bản video, email, landing page, chuyển
   đổi 1 nội dung thành nhiều định dạng
4. Thiết kế & branding — hình ảnh AI, moodboard, concept thiết kế, mockup
5. Quảng cáo — nhiều bản ad để A/B test, headline/CTA, phân tích và tối ưu
   chuyển đổi
6. Phân tích dữ liệu — tóm tắt báo cáo, phân tích số liệu, insight từ data,
   gợi ý tối ưu chiến dịch
7. Quản lý team — tự động hoá báo cáo, tóm tắt họp, brief thành checklist,
   SOP, đào tạo người mới
8. Điều phối (khâu hay bị bỏ sót) — nối các khâu trên thành pipeline chạy
   liên tục, không để người phải làm "operator" copy-paste giữa từng bước

## Bước 3 — Ra roadmap 3 giai đoạn
Dựa trên khâu nào [Chưa làm]/[Làm tay] và mức độ đau nhất mà client vừa nói,
xếp ưu tiên theo effort thấp — impact cao trước:

- **Quick win (tuần 1-2):** 1-2 việc áp AI ngay bằng tool có sẵn (ChatGPT/
  Claude trực tiếp), không cần setup gì thêm — để client thấy kết quả nhanh
- **Mid-term (tháng 1-2):** Ghép 2-3 khâu liền kề thành 1 quy trình có
  template/skill riêng (vd: research → ý tưởng → viết script làm 1 luồng)
- **Dài hạn (từ tháng 3+):** Build agent pipeline chạy tự động cho khâu lặp
  lại nhiều nhất (research → content → publish → theo dõi), người chỉ duyệt
  output cuối thay vì làm từng bước

## Bước 4 — Chốt kỹ năng cần có
Nhắc client: AI không thay marketer giỏi, chỉ thay người không chịu học. 3 kỹ
năng cần giữ lại dù AI làm nhiều việc hơn:
- Hiểu khách hàng thật (AI tổng hợp được data nhưng không tự có insight nếu
  không hỏi đúng câu)
- Tư duy chiến lược (chọn khâu nào ưu tiên, AI không tự quyết được)
- Biết thiết kế quy trình (workflow), không chỉ biết "hỏi AI 1 câu rồi copy
  ra" — vì giá trị lớn nhất nằm ở việc nối các khâu lại, không nằm ở từng
  prompt lẻ

Luôn kết thúc bằng roadmap cụ thể, không kết thúc bằng danh sách chung chung
kiểu "AI giúp được nhiều thứ trong marketing".
```

## Setup từng bước
1. Dán system prompt trên vào đầu conversation (hoặc project instruction riêng khi ngồi với 1 client cụ thể).
2. Để client mô tả tự do tình trạng hiện tại — không ép trả lời form cứng, hỏi tiếp nếu thiếu thông tin.
3. Sau khi có bảng map 8 khâu, tự roadmap ra — không hỏi lại client "mày muốn ưu tiên gì" trừ khi có 2 khâu ngang mức đau như nhau.
4. Copy roadmap ra thành slide proposal (dùng skill `docx`/`pptx` nếu cần bản gửi client chính thức).
5. Nếu client chốt làm dài hạn (giai đoạn agent pipeline) → chuyển sang chạy `SKILL_AGENTIC_FACTORY.md` để đóng gói agent thật cho họ.

## Ví dụ thực tế
Client là 1 shop thời trang nhỏ, 2 người làm marketing (1 chạy ads, 1 làm content), đang thấy tốn thời gian nhất ở việc nghĩ caption mỗi ngày và không biết ads có hiệu quả không.

- Map ra: khâu 3 (sản xuất nội dung) đang [Làm tay], khâu 6 (phân tích data) đang [Chưa làm], khâu 1 (insight) [Chưa làm].
- Quick win: dùng AI viết 5 bản caption/ngày thay vì 1, test xem bản nào tương tác tốt hơn — làm ngay tuần này không cần setup.
- Mid-term: ghép khâu 1 + 3 — trước khi viết caption, chạy tóm tắt comment của tháng trước để tìm từ ngữ khách hàng thật, rồi mới viết → content đúng insight hơn thay vì đoán.
- Dài hạn: build agent tự tóm tắt performance ads mỗi tuần (khâu 6), báo lại luôn khâu nào cần đổi content — không phải tự mở Ads Manager đọc số mỗi ngày.

## Lưu ý / Lỗi thường gặp
- **Đừng liệt kê hết 8 khâu cho client nghe** — dễ gây choáng, quan trọng là chỉ ra đúng 1-2 khâu đau nhất trước, roadmap còn lại để sau.
- **Roadmap quá tham vọng ở quick win** — nếu quick win cũng đòi setup phức tạp thì client mất niềm tin ngay từ đầu, ưu tiên tuyệt đối effort thấp cho giai đoạn 1.
- **Bỏ qua khâu 8 (điều phối)** — đây là khâu hay bị các bài viết AI-marketing bỏ sót, chỉ liệt kê AI làm được gì từng việc mà không nói ai/cái gì nối chúng lại — dễ khiến client nghĩ "vậy vẫn phải tự ngồi ghép các bước", mất đúng điểm bán hàng của Tano Agency (agent pipeline).
- **Không tự đề xuất tool/giá cụ thể nếu chưa rõ ngân sách client** — hỏi ngân sách trước khi gợi ý build agent riêng, tránh đề xuất quá tầm.

## Đánh giá cá nhân
- **Điểm mạnh:** Biến 1 bài "content giáo dục thị trường" thành công cụ discovery + proposal thật, dùng được ngay trong sales call chứ không chỉ để đăng bài. Framework 8 khâu (thêm khâu điều phối) khớp đúng với cách Tano Agency định vị — bán agent pipeline chứ không bán prompt lẻ.
- **Điểm yếu:** Cần người ngồi nghe câu trả lời của client và điều chỉnh linh hoạt — nếu để AI tự chạy hết không có người review, dễ ra roadmap generic giống hệt nhau cho mọi client dù ngành khác nhau. Không thay được việc hiểu sâu 1 ngành cụ thể (thời trang khác spa khác F&B).
- **Có nên dùng không:** 8/10 — rất hợp làm bước mở đầu cho mọi client mới của Tano Agency, nhưng luôn cần cá nhân hoá ví dụ theo đúng ngành client trước khi gửi, không dùng nguyên văn ví dụ mẫu.

## Link
- Nguồn gốc skill: Tổng hợp từ bài chia sẻ cộng đồng marketing về ứng dụng AI theo 7 khâu (research, chiến lược, content, design, ads, data, quản lý team), Tano Agency bổ sung khâu điều phối (agent pipeline) và cấu trúc lại thành công cụ discovery/roadmap cho khách hàng SME.

---

## 🤖 Agent Integration

### Hermes (Python)
Dùng làm bước đầu trong `agents/company/` khi có lead mới — Hermes nhận mô tả tình trạng client (từ form hoặc tin nhắn), gọi LLM chạy chẩn đoán 8 khâu, xuất roadmap draft trước khi người xem lại.

```python
import urllib.request, json

OMNIROUTE_URL = "https://your-omniroute-endpoint/v1/chat/completions"
API_KEY = "[OMNIROUTE_KEY]"
SYSTEM_PROMPT = open("skills/ai-marketing-adoption-map-system.txt").read()  # nội dung phần "Nội dung skill/prompt" ở trên

def diagnose_client(client_description: str) -> str:
    body = {
        "model": "claude-sonnet",  # route=creative/reasoning theo OmniRoute config
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": client_description}
        ]
    }
    req = urllib.request.Request(
        OMNIROUTE_URL, data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        method="POST")
    resp = json.loads(urllib.request.urlopen(req).read())
    return resp["choices"][0]["message"]["content"]
```

### OpenClaw
```bash
# Lệnh Telegram để chạy nhanh khi đang chat với lead
/marketing-audit <mô-tả-tình-trạng-client>
```

### Antigravity
Không cần deploy riêng — chạy qua OmniRoute có sẵn, output text thuần đủ dùng cho bước discovery, không cần compute nặng.

> ⚠️ Roadmap ra từ agent chỉ là DRAFT — bắt buộc người ở Tano Agency đọc lại và
> chỉnh ví dụ đúng ngành client trước khi gửi, đặc biệt phần đề xuất ngân sách/
> gói dịch vụ không được để agent tự chốt giá.

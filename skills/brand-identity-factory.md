# Brand Identity Factory — Prompt Template / System Prompt

## TL;DR
Chuỗi 8 prompt chạy tuần tự biến 1 câu mô tả doanh nghiệp thành trọn bộ nhận diện thương hiệu: chiến lược → khách hàng lý tưởng → tên/slogan → visual identity → tone giọng → thông điệp cốt lõi → cấu trúc website → copy trang chủ. Dùng cho Tano Agency khi build brand cho client SMB (hoặc brand nội bộ: ABTRIP, Wonder Mart, Tano Cafe) mà không cần thuê brand strategist riêng.

## Khi nào dùng
- Client mới ký, cần bộ brand identity hoàn chỉnh trước khi làm website/content — thay vì research + brainstorm thủ công nhiều ngày.
- Đang launch brand phụ (vd Wonder Mart mở thêm ngành hàng, Tano Cafe mở chi nhánh mới cần định vị riêng) và cần "brand brief" nhanh để brief cho designer/copywriter.
- Client chưa có brand rõ ràng, chỉ có ý tưởng sản phẩm — dùng chain này để ép ra thành output cụ thể, tránh brand generic ("chất lượng cao", "uy tín", "tận tâm").
- Không dùng khi: client đã có brand guideline sẵn và chỉ cần content theo guideline đó — lúc này dùng `skills/brand-voice` (derive từ nguồn có sẵn) thay vì tạo mới từ đầu.

## Nội dung skill / prompt

Chạy tuần tự 8 prompt, mỗi prompt lấy output của các bước trước làm input context (không cần chạy lại từ đầu mỗi lần — giữ nguyên context trong cùng 1 thread).

```
### PROMPT 1 — Chiến lược thương hiệu
Hãy đóng vai chuyên gia chiến lược thương hiệu cao cấp. Giúp tôi tạo chiến lược
thương hiệu rõ ràng cho [doanh nghiệp/sản phẩm/dịch vụ].

Doanh nghiệp của tôi giúp [đối tượng mục tiêu] giải quyết [vấn đề chính] bằng
cách cung cấp [giải pháp của bạn].

Tạo:
- Mục đích thương hiệu trong một câu
- Tuyên bố sứ mệnh và tầm nhìn
- 3 giá trị cốt lõi kèm giải thích
- Lợi thế cạnh tranh mạnh nhất của tôi
- Tuyên bố định vị rõ ràng
- 3 lý do khách hàng nên tin tưởng thương hiệu của tôi
- Cảm xúc chính mà thương hiệu nên tạo ra

Giữ chiến lược thực tế, cụ thể và dễ hiểu. Tránh các cụm từ chung chung như
"chất lượng cao", "đổi mới" hoặc "lấy khách hàng làm trung tâm" trừ khi bạn
giải thích chính xác chúng có nghĩa gì với doanh nghiệp của tôi.

### PROMPT 2 — Khách hàng lý tưởng
Hãy đóng vai chuyên gia nghiên cứu khách hàng. Tạo hồ sơ khách hàng lý tưởng
chi tiết cho [loại hình doanh nghiệp] của tôi.

Sản phẩm/dịch vụ của tôi là [mô tả], giá khoảng [giá hoặc khoảng giá].

Mô tả khách hàng lý tưởng về:
- Độ tuổi, nghề nghiệp, thu nhập và lối sống
- Mục tiêu chính và kết quả mong muốn
- Top 5 nỗi thất vọng
- Mối quan tâm và phản đối khi mua
- Câu hỏi họ hỏi trước khi mua
- Từ ngữ họ dùng để mô tả vấn đề
- Nền tảng và website họ thường xuyên sử dụng
- Sự kiện nào sẽ thúc đẩy họ mua ngay

Kết thúc bằng một câu chuyện ngắn "một ngày trong đời" cho thấy khi nào và
tại sao khách hàng này sẽ phát hiện ra thương hiệu của tôi.

### PROMPT 3 — Tên thương hiệu và slogan
Hãy đóng vai chuyên gia đặt tên chuyên nghiệp. Tạo 20 tên thương hiệu dễ nhớ
cho doanh nghiệp cung cấp [sản phẩm/dịch vụ] cho [đối tượng mục tiêu]. Thương
hiệu nên mang cảm giác [hiện đại/sang trọng/thân thiện/mạnh mẽ/tối giản/vui
tươi] và truyền tải [lợi ích hoặc cảm xúc chính].

Yêu cầu:
- Dễ phát âm và viết
- Tối đa 2-3 từ
- Không dùng chữ viết tắt gây nhầm lẫn
- Tránh từ quá phổ biến trong ngành
- Phù hợp cho website và tài khoản mạng xã hội

Với mỗi tên, bao gồm: ý nghĩa đằng sau, lý do phù hợp với đối tượng, slogan
tương ứng. Sau đó xếp hạng 5 lựa chọn tốt nhất dựa trên khả năng ghi nhớ, sự
rõ ràng, tính độc đáo và tiềm năng thương hiệu. Nhắc tôi tự kiểm tra nhãn
hiệu, tên miền và handle mạng xã hội trước khi chọn.

### PROMPT 4 — Nhận diện hình ảnh
Hãy đóng vai nhà thiết kế nhận diện thương hiệu giàu kinh nghiệm. Phát triển
hướng hình ảnh hoàn chỉnh cho thương hiệu [tên thương hiệu].

Mô tả thương hiệu: [doanh nghiệp làm gì]
Đối tượng mục tiêu: [đối tượng]
Tính cách mong muốn: [3-5 tính từ]
Thương hiệu có phong cách hình ảnh tôi ngưỡng mộ: [ví dụ]

Tạo:
- Một khái niệm hình ảnh được đề xuất
- Bảng màu chính và phụ kèm mã HEX
- Mục đích của từng màu
- Hai cặp font chữ dễ tiếp cận
- Gợi ý phong cách logo
- Phong cách icon và minh họa
- Hướng dẫn nhiếp ảnh
- Phong cách nút, nền và đồ họa
- Các yếu tố hình ảnh nên tránh

Đảm bảo nhận diện nhất quán, dễ tiếp cận và thực tế để thương hiệu nhỏ sử
dụng trên website và mạng xã hội.

### PROMPT 5 — Giọng điệu thương hiệu
Hãy đóng vai giám đốc nội dung thương hiệu. Tạo hướng dẫn giọng điệu thương
hiệu cho [tên thương hiệu], giúp [đối tượng mục tiêu] đạt được [kết quả mong
muốn].

Thương hiệu nên nghe [thân thiện/tự tin/chuyên gia/vui tươi/trực tiếp/cao
cấp], nhưng không bao giờ nghe [những phẩm chất cần tránh].

Bao gồm:
- 4 đặc điểm giọng điệu thương hiệu kèm giải thích
- Từ và cụm từ thương hiệu nên dùng
- Từ và cụm từ thương hiệu nên tránh
- Quy tắc viết cho tiêu đề, caption, email và nội dung website
- 5 ví dụ "trước" (nội dung chung chung) và "sau" (nội dung đúng thương hiệu)
- Giới thiệu thương hiệu mẫu 50 từ
- 3 lời kêu gọi hành động mẫu

Làm cho giọng điệu dễ nhận biết, tự nhiên và dễ theo dõi cho người không
chuyên viết.

### PROMPT 6 — Thông điệp cốt lõi
Hãy đóng vai chiến lược gia thông điệp tập trung vào chuyển đổi. Tạo khung
thông điệp cho thương hiệu của tôi dựa trên thông tin dưới đây.

Doanh nghiệp: [tên và mô tả]
Đối tượng: [đối tượng mục tiêu]
Vấn đề: [vấn đề chính của khách hàng]
Giải pháp: [sản phẩm/dịch vụ của bạn]
Lợi ích chính: [kết quả mong muốn]
Bằng chứng: [kinh nghiệm, kết quả, lời chứng thực, quy trình hoặc chứng chỉ]

Tạo:
- Đề xuất giá trị trong một câu
- Pitch thang máy ngắn
- Pitch thang máy chi tiết
- 5 trụ cột thông điệp chính, mỗi trụ cột kèm 3 điểm hỗ trợ
- 10 lựa chọn tiêu đề
- 10 lời kêu gọi hành động ngắn
- Câu trả lời cho 5 phản đối phổ biến nhất của khách hàng

Sử dụng ngôn ngữ cụ thể, tập trung vào kết quả của khách hàng. Không dùng
tuyên bố phóng đại hoặc lời hứa không có cơ sở.

### PROMPT 7 — Cấu trúc website
Hãy đóng vai chiến lược gia website và nhà thiết kế trải nghiệm người dùng.
Tạo kế hoạch website đơn giản, tập trung vào chuyển đổi cho [tên thương hiệu].

Mục tiêu chính của website là khiến khách truy cập [đặt lịch gọi/mua sản
phẩm/yêu cầu báo giá/tham gia danh sách/tạo tài khoản]. Đối tượng của tôi là
[đối tượng mục tiêu], và sản phẩm chính là [sản phẩm/dịch vụ].

Đề xuất: các trang website cần thiết, mục tiêu của từng trang, các phần cần
có trên mỗi trang, thứ tự tốt nhất cho các phần đó, lời kêu gọi hành động
chính và phụ, cấu trúc menu điều hướng, cấu trúc footer, các yếu tố xây dựng
niềm tin, câu hỏi thường gặp, và thông tin/trang tôi chưa cần.

Giữ website gọn nhẹ và thực tế cho doanh nghiệp mới hoặc nhỏ.

### PROMPT 8 — Copy trang chủ
Hãy đóng vai copywriter website cao cấp. Viết trang chủ hoàn chỉnh cho [tên
thương hiệu].

Doanh nghiệp: [mô tả]
Đối tượng: [đối tượng mục tiêu]
Vấn đề chính: [vấn đề]
Sản phẩm/dịch vụ: [offer]
Kết quả chính: [kết quả]
Điểm khác biệt: [lý do bạn khác biệt]
Hành động chính: [hành động mong muốn]
Giọng điệu thương hiệu: [mô tả giọng điệu — lấy từ Prompt 5]

Viết nội dung cho: thanh thông báo, tiêu đề hero và văn bản hỗ trợ, nút chính
và phụ, phần vấn đề, phần giải pháp, ba lợi ích chính, cách hoạt động, về
thương hiệu, placeholder lời chứng thực/bằng chứng, câu hỏi thường gặp, phần
kêu gọi hành động cuối, slogan footer.

Giữ đoạn văn ngắn, làm mỗi phần cụ thể, và ghi rõ tất cả placeholder nơi cần
thêm số liệu, lời chứng thực hoặc liên kết.
```

## Setup từng bước
1. Tạo 1 conversation/project riêng cho mỗi client (giữ context xuyên suốt 8 prompt, không lẫn giữa các client).
2. Điền sẵn 1 đoạn brief ngắn về client (ngành, đối tượng, giá, điểm khác biệt) — dán vào đầu conversation trước khi chạy Prompt 1, để AI không phải đoán field `[...]`.
3. Chạy Prompt 1 → 8 tuần tự, không nhảy cóc — Prompt 5 cần output Prompt 1+2, Prompt 8 cần output Prompt 5+6+7.
4. Sau Prompt 3 (tên/slogan): dừng lại, tự tay check trùng nhãn hiệu + domain trống trước khi đi tiếp — AI không tự verify được cái này.
5. Sau khi xong cả 8, gom lại thành 1 file "Brand Brief" đưa cho designer/dev — không thả nguyên 8 output rời cho họ tự ráp.

## Ví dụ thực tế
Dùng cho **Wonder Mart** mở thêm ngành hàng đồ gia dụng thông minh:
- Input Prompt 1: "Doanh nghiệp giúp các gia đình trẻ ở đô thị tiết kiệm thời gian dọn nhà bằng đồ gia dụng thông minh giá hợp lý."
- Output Prompt 1 ra định vị: "Thông minh hoá việc nhà cho gia đình bận rộn — không cần ngân sách cao cấp." → tránh được câu chung chung kiểu "sản phẩm chất lượng, giá tốt".
- Prompt 3 ra 20 tên, xếp hạng top 5 — chọn được tên chưa trùng domain .vn.
- Prompt 8 ra copy trang chủ paste thẳng vào Framer/Webflow, chỉ cần thay ảnh + testimonial thật.

Toàn bộ chain chạy xong trong ~30-45 phút thay vì brainstorm 2-3 ngày.

## Lưu ý / Lỗi thường gặp
- **AI tự bịa placeholder thành thật** → luôn giữ rõ `[cần bổ sung]` cho số liệu/testimonial, đừng để AI tự chế con số uy tín giả.
- **Tên thương hiệu nghe hay nhưng đã có người dùng** → Prompt 3 không tự check trademark/domain, bắt buộc verify tay (Bước 4 ở trên).
- **Giọng điệu (Prompt 5) bị lặp lại giữa nhiều client** nếu không đổi input tính từ mô tả — mỗi client phải có bộ tính từ riêng, không copy nguyên si.
- **Chạy prompt 4 (visual identity) không kèm ví dụ thương hiệu ngưỡng mộ** → AI ra màu/font generic, kém định hướng. Luôn kèm 2-3 ví dụ tham chiếu thật.
- Chain này KHÔNG thay được buổi brand discovery call với client thật — nó rút ngắn thời gian soạn thảo, không thay việc xác nhận với người ra quyết định.

## Đánh giá cá nhân
- **Điểm mạnh:** Rẻ, nhanh, ép ra output cụ thể thay vì brand chung chung — rất hợp làm bước "zero-to-draft" trước khi ngồi với client. Cấu trúc 8 bước có logic phụ thuộc rõ (chiến lược → khách hàng → tên → visual → giọng → thông điệp → site → copy) nên không bị rời rạc.
- **Điểm yếu:** Không có bước validate thị trường thật (không search đối thủ, không check tên trùng) — dễ tạo ảo tưởng "brand đã xong" trong khi mới là draft. Prompt 4 (visual) ra mô tả chữ, không ra file thiết kế — vẫn cần Canva/Figma sau đó để hiện thực hoá.
- **Có nên dùng không:** 8/10 — cực tốt làm bước khởi động cho brand mới hoặc brand phụ, nhưng luôn cần review người thật trước khi giao client, đặc biệt đoạn tên thương hiệu và số liệu.

## Link
- Nguồn gốc skill: Tổng hợp từ bộ "8 prompt xây dựng thương hiệu" phổ biến trên cộng đồng prompt engineering, được Tano Agency điều chỉnh thêm bước verify + gộp brand brief cho quy trình làm việc với client SMB.

---

## 🤖 Agent Integration

### Hermes (Python)
Chạy chain 8 prompt tuần tự qua OmniRoute (route `creative` → Claude Sonnet), tự động feed output bước trước vào bước sau, gom lại thành 1 file Brand Brief markdown.

```python
import urllib.request, json, time

OMNIROUTE_URL = "https://your-omniroute-endpoint/v1/chat/completions"  # điền endpoint thật
API_KEY = "[OMNIROUTE_KEY]"

PROMPTS = [
    "chien-luoc", "khach-hang", "ten-slogan", "visual-identity",
    "tone-giong", "thong-diep", "cau-truc-website", "copy-trang-chu"
]

def call_llm(prompt_text, context=""):
    body = {
        "model": "claude-sonnet",  # route=creative theo OmniRoute config
        "messages": [{"role": "user", "content": context + "\n\n" + prompt_text}]
    }
    req = urllib.request.Request(
        OMNIROUTE_URL, data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        method="POST")
    resp = json.loads(urllib.request.urlopen(req).read())
    return resp["choices"][0]["message"]["content"]

def run_brand_chain(client_brief: str, prompt_templates: list[str]) -> str:
    """client_brief: mô tả ngắn về doanh nghiệp client.
    prompt_templates: list 8 prompt template lấy từ file skill này."""
    context = f"BRIEF CLIENT:\n{client_brief}\n"
    outputs = []
    for i, template in enumerate(prompt_templates, 1):
        result = call_llm(template, context)
        outputs.append(f"## Bước {i}\n{result}")
        context += f"\n\nOUTPUT BƯỚC {i}:\n{result}"  # feed vào bước sau
        time.sleep(1)
    return "\n\n---\n\n".join(outputs)
```

### OpenClaw
```bash
# Gọi qua Telegram command, OpenClaw route lệnh sang Hermes chạy chain,
# trả về file Brand Brief markdown qua bot
/brand-factory <tên-client> <mô-tả-ngắn>
```

### Antigravity
Không cần deploy service riêng — chain chạy trực tiếp qua OmniRoute, không tốn tài nguyên VPS ngoài process Hermes có sẵn.

> ⚠️ Prompt 3 (tên thương hiệu) và các con số/testimonial ở Prompt 6, 8 BẮT BUỘC người thật review trước khi gửi client — agent không tự verify trademark/domain và không được tự điền số liệu giả vào placeholder.

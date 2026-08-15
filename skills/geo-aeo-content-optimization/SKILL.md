---
name: geo-aeo-content-optimization
description: >
  Tối ưu nội dung để được AI (ChatGPT, Claude, Gemini, Perplexity, Google AI
  Overviews) trích dẫn/nhắc tên thương hiệu — thay vì chỉ tối ưu để rank trên
  Google truyền thống. Dùng khi viết content cho brand cần xuất hiện trong
  câu trả lời AI, không chỉ trong 10 kết quả tìm kiếm xanh.
origin: Tổng hợp từ Google Search Central, Wikipedia, WRITER, Jasper, GenOptima (2026)
---

# GEO/AEO Content Optimization — Prompt Template / System Prompt

## TL;DR
SEO giúp trang được rank, AEO giúp câu trả lời được trích trực tiếp (featured snippet, AI Overview), GEO giúp thương hiệu được AI nhắc tên/trích dẫn khi trả lời câu hỏi mở. Cả 3 phải làm cùng nhau — GEO/AEO không thay thế SEO, chúng đứng trên nền SEO.

## Khi nào dùng
- Viết bài blog/landing page/FAQ cho brand cần xuất hiện khi khách hỏi AI (vd "Fast Track sân bay Nội Bài giá bao nhiêu" gõ vào ChatGPT/Gemini)
- Audit lại content cũ xem có dễ bị AI trích/tóm tắt không
- Cần thiết lập cách đo hiệu quả content thời AI (không chỉ đo click, traffic như SEO cũ)

## Nội dung skill / prompt

### Phân biệt 3 tầng (không trùng nhau, không thay thế nhau)
| Tầng | Mục tiêu | Ví dụ hành động |
|---|---|---|
| SEO | Trang được rank trong kết quả tìm kiếm | Backlink, technical SEO, keyword |
| AEO | Câu trả lời được trích trực tiếp (snippet, AI Overview) | Cấu trúc FAQ, trả lời ngắn gọn ngay đầu đoạn |
| GEO | Thương hiệu được AI nhắc tên/trích dẫn khi tổng hợp câu trả lời | Entity rõ ràng, tín hiệu uy tín, được bên thứ 3 nhắc tới |

Cách nhớ: SEO giúp trang được tìm thấy → AEO giúp câu trả lời được trích ra → GEO giúp thương hiệu được đề xuất.

### ⚠️ Cảnh báo quan trọng (từ chính Google Search Central)
Google công khai nói: tối ưu cho AI Overviews/Generative AI **vẫn là SEO**, không phải 1 kỹ thuật tách biệt. Nhiều "hack GEO/AEO" trên mạng không có tác dụng thật, chỉ là marketing của bên thứ 3 bán dịch vụ. Cẩn trọng khi có ai chào mời dịch vụ "GEO" như phép màu tách biệt khỏi SEO nền tảng.

### Prompt audit content theo GEO/AEO (copy dùng trực tiếp)
```
Bạn đang đóng vai chuyên gia GEO/AEO. Đầu vào là 1 bài content/landing page
[dán nội dung]. Hãy đánh giá theo 5 tiêu chí:
1. Answer-first: câu trả lời trực tiếp có nằm ngay đầu đoạn không, hay bị
   chôn sau phần dẫn dắt dài?
2. Cấu trúc trích dẫn được: có block trả lời độc lập (không nằm trong
   blockquote/callout) mà AI có thể trích nguyên văn không?
3. Entity signal: brand/sản phẩm có được nêu rõ ràng, nhất quán tên gọi
   không, hay đổi cách gọi lung tung khiến AI khó nhận diện là cùng 1 thực thể?
4. Authority signal: có dẫn chứng, số liệu, nguồn uy tín để AI tin tưởng
   trích dẫn không, hay chỉ toàn tuyên bố suông?
5. Structured data: có schema markup (FAQ, Product, Organization...) hỗ trợ
   AI đọc máy không?
Không được tự sửa nội dung. Trước khi làm, hỏi tối đa 3 câu nếu thiếu ngữ
cảnh về brand/đối tượng khách hàng.
```

### Cấu trúc bài viết chuẩn AEO (áp trực tiếp khi viết mới)
```
[Câu hỏi làm H2/H3] → [Trả lời trực tiếp 1-2 câu ngay sau, dạng đoạn văn
thường KHÔNG bọc trong callout] → [đoạn giải thích chi tiết bên dưới]
```
Lặp lại pattern này cho mỗi câu hỏi con trong bài — mỗi block trả lời phải tự đứng độc lập được (AI trích 1 đoạn, không cần đọc cả bài mới hiểu).

### 3 KPI đo GEO (khác hẳn KPI SEO truyền thống)
| KPI | Đo gì |
|---|---|
| Mention Rate | % câu trả lời AI có nhắc tên brand khi hỏi các câu trong tập prompt mục tiêu |
| Citation Rate | % câu trả lời AI có kèm link trỏ về domain của mình |
| Position | Khi được nhắc, brand xuất hiện đầu câu trả lời hay bị chôn cuối |

Cách đo thủ công (chưa có tool riêng): định nghĩa 15-25 prompt mục tiêu khớp cụm từ khóa cốt lõi, tự hỏi ChatGPT/Gemini/Perplexity/Claude định kỳ, ghi lại có được nhắc/trích không.

## Setup từng bước
1. Liệt kê 15-25 câu hỏi khách thật sự hỏi về brand (không phải từ khóa SEO, mà câu hỏi tự nhiên dạng hỏi AI)
2. Test từng câu trên ChatGPT/Gemini/Perplexity/Claude — ghi brand có được nhắc không, thứ hạng trong câu trả lời
3. Với content hiện có: chạy prompt audit ở trên cho từng bài quan trọng nhất trước
4. Với content mới: viết theo cấu trúc AEO (câu hỏi → trả lời trực tiếp → giải thích)
5. Thêm structured data (schema.org FAQ/Product/Organization) vào trang — dùng skill `schema-markup` nếu cần
6. Lặp lại đo Mention/Citation Rate mỗi tháng, không kỳ vọng thấy kết quả tuần đầu

## Ví dụ thực tế
Áp cho ABTRIP: câu hỏi khách thật hay hỏi AI kiểu "Fast Track sân bay Nội Bài giá bao nhiêu, đặt ở đâu uy tín". Trước khi tối ưu, content ABTRIP có thể bị chôn sau đoạn giới thiệu công ty dài dòng — AI khó trích trực tiếp giá. Sau khi áp cấu trúc AEO: đặt câu hỏi y hệt cách khách hỏi làm heading, trả lời giá + cách đặt ngay 1-2 câu đầu, phần giải thích quy trình để bên dưới — tăng khả năng AI trích thẳng đoạn đó khi khách hỏi Gemini/ChatGPT thay vì chỉ dẫn link chung chung.

## Lưu ý / Lỗi thường gặp
- Nhầm GEO là "SEO cho AI" hoàn toàn tách biệt — sai, Google xác nhận nó vẫn nằm trong SEO, chỉ là 1 lớp bổ sung
- Chưa có tool đo GEO chuẩn hoá, chính xác 100% — mọi con số Mention/Citation Rate hiện tại đều đo thủ công hoặc qua tool bên thứ 3 chưa kiểm chứng độc lập
- Đừng bỏ hoàn toàn SEO truyền thống để dồn hết vào GEO — nghiên cứu cho thấy ~70% nội dung AI Overview trích vẫn nằm trong top 100 kết quả organic, nền SEO vẫn là điều kiện cần
- Thuật ngữ GEO/AEO/LLMO/AIO chưa có định nghĩa thống nhất trong giới học thuật (theo Wikipedia, tính đến đầu 2026) — các nguồn khác nhau định nghĩa hơi khác nhau, đọc kỹ nguồn trước khi áp cứng nhắc

## Đánh giá cá nhân
- Điểm mạnh: framework 3 tầng (SEO/AEO/GEO) dễ hiểu, dễ áp ngay vào content pipeline hiện có mà không cần đổi công cụ; prompt audit + cấu trúc AEO dùng được ngay cho content ABTRIP/Wonder Mart
- Điểm yếu: đây là lĩnh vực rất mới (thuật ngữ chưa chuẩn hoá), thiếu tool đo lường đáng tin cậy độc lập; nhiều dịch vụ "GEO" trên thị trường là chiêu marketing hơn là kỹ thuật thật — cần cảnh giác
- Có nên dùng không: 8/10 — nên tích hợp ngay vào quy trình viết content (không tốn thêm công cụ, chỉ đổi cách viết), nhưng đừng kỳ vọng đo ROI chính xác ngay, đây là khoản đầu tư dài hạn

## Link
- Google Search Central (nguồn chính thức): https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Wikipedia (định nghĩa, thuật ngữ liên quan): https://en.wikipedia.org/wiki/Generative_engine_optimization

# NotebookLM Slide Commands — 8 Câu Lệnh Làm Slide Xịn Trong 5 Phút

**Nguồn:** @louisthanhbinh
**Dạng:** Prompt Templates — dùng với NotebookLM
**Target:** Người cần làm slide từ tài liệu có sẵn

---

## Vấn Đề

Làm 1 bộ slide từ tài liệu mất 4 tiếng — đọc, tóm tắt, chọn số liệu, viết storyline, tạo FAQ, viết speaker notes...

8 câu lệnh này làm từng việc đó trong vài giây. Upload tài liệu vào NotebookLM, chạy từng lệnh theo thứ tự — có slide hoàn chỉnh trong 5 phút.

---

## 8 Câu Lệnh Theo Thứ Tự

### Câu lệnh 1 — Tóm Tắt Thành Bộ Khung Slide
```
Đọc toàn bộ tài liệu này và tạo ra cấu trúc slide gồm 10 trang.
Mỗi trang gồm:
- Tiêu đề chính
- 3 bullet point ngắn gọn dưới 10 từ mỗi điểm
- 1 câu takeaway quan trọng nhất
```
**Dùng khi:** Bắt đầu từ đầu, chưa có outline nào.

---

### Câu lệnh 2 — Biến Dữ Liệu Dày Đặc Thành Slide Dễ Hiểu
```
Tài liệu này có nhiều số liệu và dữ liệu. Hãy chọn ra 5 con số ấn tượng nhất:
- Giải thích ý nghĩa từng con số trong 1 câu
- Đề xuất cách trình bày từng con số trên slide
```
**Dùng khi:** Tài liệu báo cáo, nghiên cứu, nhiều số liệu.

---

### Câu lệnh 3 — Tạo Slide Mở Đầu Gây Chú Ý
```
Dựa vào nội dung tài liệu, viết cho tôi slide đầu tiên theo công thức:
- 1 câu hỏi gây tò mò
- 1 thống kê giật mình
- 1 câu hứa hẹn điều người xem sẽ học được sau bài này
```
**Dùng khi:** Cần hook mạnh cho slide đầu tiên.

---

### Câu lệnh 4 — Tóm Tắt Thành Slide Kết Luận Hành Động
```
Đọc toàn bộ tài liệu và tạo slide kết luận gồm:
- 3 điểm quan trọng nhất cần nhớ
- 3 hành động cụ thể người xem nên làm ngay sau khi xem xong
- 1 câu kết đáng nhớ
```
**Dùng khi:** Cần slide cuối có impact, người xem biết làm gì tiếp theo.

---

### Câu lệnh 5 — Chuyển Tài Liệu Dài Thành Storytelling
```
Biến nội dung tài liệu thành cấu trúc kể chuyện theo công thức:
- Vấn đề → Hậu quả nếu không giải quyết
- Giải pháp → Bằng chứng → Kêu gọi hành động
- Mỗi phần 1 slide, tối đa 3 bullet
```
**Dùng khi:** Tài liệu khô khan, cần biến thành narrative hấp dẫn.

---

### Câu lệnh 6 — Tạo Slide So Sánh Trước / Sau
```
Từ nội dung tài liệu, tạo 3 slide dạng so sánh Trước và Sau:
- Cột trái: cách cũ / vấn đề hiện tại
- Cột phải: cách mới / giải pháp
- Dùng ngôn ngữ đối lập rõ ràng, súc tích
```
**Dùng khi:** Cần show transformation, contrast giữa cũ và mới.

---

### Câu lệnh 7 — Tạo Slide FAQ Xử Lý Phản Đối
```
Dựa vào tài liệu, đoán 5 câu hỏi hoặc phản đối mà người xem slide có thể đặt ra:
- Với mỗi câu hỏi, viết câu trả lời ngắn gọn dưới 2 dòng
- Trình bày dạng Q&A cho từng slide
```
**Dùng khi:** Chuẩn bị cho Q&A, phòng trường hợp bị challenge.

---

### Câu lệnh 8 — Tạo Toàn Bộ Speaker Notes
```
Tài liệu này sẽ được trình bày thành 8 slide. Với mỗi slide, viết speaker notes gồm:
- Câu mở miệng tự nhiên để nói
- 2-3 điểm bổ sung không có trên slide
- Câu chuyển tiếp sang slide tiếp theo
```
**Dùng khi:** Cần chuẩn bị nói chứ không chỉ đọc slide.

---

## Workflow Tối Ưu

```
Upload tài liệu vào NotebookLM
        ↓
Câu lệnh 1 → Khung 10 slides
        ↓
Câu lệnh 2 → Chọn số liệu nổi bật
        ↓
Câu lệnh 3 → Viết slide mở đầu
        ↓
Câu lệnh 5 → Biến thành storytelling
        ↓
Câu lệnh 6 → Thêm slides so sánh
        ↓
Câu lệnh 4 → Slide kết luận
        ↓
Câu lệnh 7 → FAQ xử lý phản đối
        ↓
Câu lệnh 8 → Speaker notes đầy đủ
        ↓
Copy vào Google Slides / PowerPoint
```

**Tổng thời gian: ~5-10 phút** thay vì 4 tiếng.

---

## Tips Dùng Hiệu Quả

**1. Upload đúng loại tài liệu**
NotebookLM đọc tốt nhất: PDF, Google Docs, URLs, YouTube transcript. Tránh ảnh scan chất lượng thấp.

**2. Dùng kết hợp với NotebookLM MCP**
Nếu đang dùng Claude Code, setup NotebookLM MCP (xem mcps/notebooklm-mcp-pleaseprompto.md) để chạy các lệnh này trực tiếp từ terminal mà không cần mở browser.

**3. Chạy từng lệnh riêng, không gộp**
Mỗi lệnh có focus khác nhau. Gộp vào 1 prompt → output loãng.

**4. Customize số slide**
Thay "10 trang" hoặc "8 slide" theo nhu cầu thực tế của mày.

**5. Kết hợp với AI Content Writing skill**
Sau khi có outline từ NotebookLM → dùng skill ai-content-writing.md để polish copy cho từng slide.

---

## Đánh Giá Cá Nhân

8 câu lệnh này của @louisthanhbinh là bộ prompt slide deck tốt nhất tao thấy cho người Việt. Không phải vì phức tạp — mà vì mỗi cái giải quyết đúng 1 pain point cụ thể trong quá trình làm slide.

Câu lệnh tao thích nhất: **#5 (Storytelling)** và **#8 (Speaker Notes)**. Hai cái này thường tốn thời gian nhất khi làm thủ công — storytelling structure đòi hỏi tư duy, speaker notes đòi hỏi hiểu context sâu. NotebookLM làm được cả hai vì nó đọc toàn bộ tài liệu trước.

Hạn chế: Output là text, mày vẫn cần tự copy vào Google Slides / PowerPoint và design. Nếu muốn tự động hơn, combine với html-anything (xem repos/html-anything.md) để tạo slide HTML luôn.

**Rating: 9/10**

---

*Nguồn: @louisthanhbinh (TikTok/Instagram)*
*Cập nhật: tháng 6/2026*

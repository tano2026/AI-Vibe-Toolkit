# Skill: Research Agent — Biến Claude Thành Máy Research

> Copy prompt này vào → Claude tự lên kế hoạch research, tìm kiếm, tổng hợp báo cáo — như có intern làm việc cho mày.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Loại** | System Prompt + Prompt Template |
| **Dùng với** | Claude (có Brave Search + Firecrawl MCP càng tốt) |
| **Level** | Beginner |
| **Tốt nhất khi** | Research thị trường, tìm hiểu chủ đề mới, phân tích đối thủ |

---

## 🎯 Skill này làm được gì

Thay vì mày phải Google, đọc 10 trang, tổng hợp tay → paste prompt này vào, Claude tự làm hết:
- Xác định nguồn cần research
- Thu thập thông tin có cấu trúc
- Tổng hợp báo cáo rõ ràng
- Đưa ra insights và next steps

---

## 📋 Prompt Template

```
Mày là Research Agent chuyên nghiệp. Nhiệm vụ: research toàn diện về [CHỦ ĐỀ].

**Yêu cầu output:**
1. Tổng quan (3-5 câu)
2. Các điểm chính cần biết (bullet points)
3. Số liệu và dữ kiện quan trọng
4. Xu hướng hiện tại
5. Cơ hội và rủi ro
6. Nguồn tham khảo

**Phong cách:** Ngắn gọn, có số liệu cụ thể, tránh nói chung chung.

**Chủ đề cần research:** [PASTE CHỦ ĐỀ VÀO ĐÂY]

Bắt đầu research ngay, không hỏi thêm.
```

---

## 💡 Ví dụ thực tế

**Input:**
```
[CHỦ ĐỀ] = "Thị trường AI tools cho content creators Việt Nam 2025"
```

**Output Claude trả về:**
```
## Tổng quan
Thị trường AI content tools VN đang tăng trưởng 40%/năm...

## Điểm chính
- 78% content creators VN đã thử ít nhất 1 AI tool
- Top tools đang dùng: ChatGPT, Canva AI, CapCut AI
...

## Xu hướng
- Short-form video AI đang chiếm 60% demand
...
```

---

## 🔧 Biến thể hay dùng

**Research đối thủ:**
```
Research đối thủ [TÊN CÔNG TY/KÊNH].
Tìm: sản phẩm họ bán, giá, điểm mạnh yếu, 
content strategy họ đang dùng, 
audience họ target.
Output thành bảng so sánh.
```

**Research trước khi làm video:**
```
Tao chuẩn bị làm video về [CHỦ ĐỀ] cho audience là vibe coders VN.
Research xem:
- Họ đang hỏi gì về chủ đề này (pain points)
- Góc độ nào chưa ai làm
- Hook nào có thể viral
Output: 5 góc độ video tiềm năng, sắp xếp theo potential viral.
```

---

## 📊 Đánh giá

| Tiêu chí | Điểm |
|----------|------|
| Tiết kiệm thời gian | ⭐⭐⭐⭐⭐ |
| Dễ dùng | ⭐⭐⭐⭐⭐ |
| Output chất lượng | ⭐⭐⭐⭐☆ |

**Tốt hơn nhiều khi kết hợp với Brave Search + Firecrawl MCP** — Claude sẽ search thật thay vì dùng kiến thức cũ.

---

*Thêm vào kho: 06/2025*

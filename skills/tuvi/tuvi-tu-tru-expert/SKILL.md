---
name: tuvi-tu-tru-expert
category: tuvi
description: Skill chuyên sâu về Tử Bình Lạc Việt (Phái Việt Nam) — Tứ Trụ, Dụng Thần, Cách Cục, Đại Vận. Bao gồm Dụng Thần căn bản & Cách Cục thuần phá (merged từ tuvi-bat-tu-expert). Tổng hợp từ Lâm Thế Đức, Đỗ Đình Tuân, Tử Bình Chân Thuyên bản nghĩa, Manh Phái Minh Di Đường.
---

# TỬ BÌNH LẠC VIỆT — Expert

## Mô tả

Skill này tổng hợp toàn bộ kiến thức về **Tử Bình Lạc Việt** (trường phái Tử Bình tại Việt Nam, chịu ảnh hưởng từ Tử Bình Đài Loan/Hồng Kông, Lâm Thế Đức, Đỗ Đình Tuân và Manh Phái). Đây là hệ thống luận giải **Bát Tự (Tứ Trụ)** đầy đủ: lập tứ trụ, xác định thân vượng/nhược, chọn Dụng Thần, xác định Cách Cục, phân tích Đại Vận và Lưu Niên.

## Cách dùng

Khi người dùng yêu cầu phân tích Tử Bình / Tứ Trụ / Bát Tự, load skill này và sử dụng MCP server `tuvi` để tính toán lá số, sau đó luận giải theo quy trình dưới đây.

Luôn ưu tiên dùng MCP server `tuvi` để tính Tứ Trụ (four_pillars), cách cục, dụng thần, đại vận trước khi luận giải.

## QUY TRÌNH 10 BƯỚC LUẬN BÁT TỰ TỬ BÌNH

### Bước 1: Lập Tứ Trụ (Bát Tự)

| | Trụ Năm | Trụ Tháng | Trụ Ngày | Trụ Giờ |
|---|---|---|---|---|
| **Thiên Can** | Can năm | Can tháng | ★ **NHẬT CHỦ** | Can giờ |
| **Địa Chi** | Chi năm | ★ **NGUYỆT LỆNH** | Chi ngày | Chi giờ |

- **Nhật chủ** (Can ngày sinh) = bản thân mệnh chủ
- **Nguyệt lệnh** (Chi tháng sinh) = năng lượng nền tảng, quyết định Cách Cục

> Dùng `mcp_tuvi_four_pillars` để lấy 4 trụ + can chi + nạp âm + ngũ hành.

### Bước 2: Xác Định Đắc Lệnh / Thất Lệnh

| Nhật Chủ | Hành | Đắc Lệnh | Thất Lệnh |
|---|---|---|---|
| Giáp, Ất | Mộc | Dần Mão (Xuân) hoặc Hợi Tý (Đông) | Thân Dậu (Thu), Tỵ Ngọ (Hạ) |
| Bính, Đinh | Hỏa | Tỵ Ngọ (Hạ) hoặc Dần Mão (Xuân) | Hợi Tý (Đông), Thân Dậu (Thu) |
| Mậu, Kỷ | Thổ | Thìn Tuất Sửu Mùi, hoặc Tỵ Ngọ | Dần Mão (Xuân), Hợi Tý (Đông) |
| Canh, Tân | Kim | Thân Dậu (Thu), hoặc Thìn Tuất Sửu Mùi | Tỵ Ngọ (Hạ), Dần Mão (Xuân) |
| Nhâm, Quý | Thủy | Hợi Tý (Đông), hoặc Thân Dậu (Thu) | Thìn Tuất Sửu Mùi, Tỵ Ngọ (Hạ) |

### Bước 3: Đếm Lực Lượng Vượng/Nhược

| Phe giúp Nhật chủ (Thân Vượng) | Phe chống Nhật chủ (Thân Nhược) |
|---|---|
| **Ấn tinh** (Chính Ấn, Thiên Ấn): sinh Nhật chủ | **Tài tinh** (Chính Tài, Thiên Tài): hao |
| **Tỷ Kiên, Kiếp Tài**: cùng hành | **Quan Sát** (Chính Quan, Thất Sát): khắc |
| | **Thực Thương** (Thực Thần, Thương Quan): tiết |

**Công thức:** Phe giúp ≥ phe chống → Thân Vượng. Phe giúp < phe chống → Thân Nhược.

**Phân loại 4 mức (Manh Phái):**
- **Thân VƯỢNG:** Được lệnh tháng + nhiều sinh phù
- **Thân CƯỜNG:** Không được lệnh tháng nhưng nhiều hỗ trợ mạnh
- **Thân NHƯỢC:** Thất lệnh tháng + ít sinh phù
- **Thân SUY:** Thất lệnh tháng + bị khắc tiết quá nhiều

### Bước 4: Xác Định Dụng Thần (QUAN TRỌNG NHẤT)

#### 4A. Phương pháp Vượng Suy (phái truyền thống)

| Trường hợp | Dụng Thần | Kỵ Thần |
|---|---|---|
| Thân Vượng | Tài, Quan, Thực Thương | Ấn, Tỷ |
| Thân Nhược | Ấn, Tỷ | Tài, Quan, Thực Thương |
| Cực Vượng (Tòng cách) | Thuận thế: Ấn, Tỷ | Tài, Quan |
| Cực Nhược (Tòng cách) | Thuận thế: Tài, Quan, Thực Thương | Ấn, Tỷ |

#### 4B. Phương pháp Cách Cục (Tử Bình Chân Thuyên)

- **Dụng thần lấy từ Nguyệt lệnh làm chủ**
- Xét can tàng trong Nguyệt lệnh: can nào thấu lộ → cách cục
- 12 địa chi trừ Tý/Ngọ/Mão/Dậu (chỉ tàng 1 can), còn lại tàng 2-3 can
- **Biến hóa:** Khi can tàng không thấu, dụng thần có thể biến hóa (thí dụ: Đinh sinh Hợi → Hợi-Mão-Mùi tam hợp Mộc → hóa thành Ấn cách)

#### 4C. Phương pháp Điều Hậu (cân bằng khí hậu)

| Mùa | Tháng | Đặc điểm | Dụng Thần ưu tiên |
|---|---|---|---|
| Xuân | 1-3 | Mộc vượng, lạnh ẩm | Bính Hỏa, Mậu Thổ |
| Hạ | 4-6 | Hỏa vượng, nóng bức | Nhâm/Quý Thủy |
| Thu | 7-9 | Kim vượng, khô lạnh | Nhâm Thủy, Bính Hỏa |
| Đông | 10-12 | Thủy vượng, cực lạnh | Bính Hỏa, Giáp Mộc |

#### 4D. Kết hợp 3 phương pháp

Trong thực tế cần kết hợp cả 3:
- **Vượng Suy** → đánh giá cường nhược cơ bản
- **Cách Cục** → Dụng Thần từ Nguyệt lệnh
- **Điều Hậu** → điều chỉnh khí hậu mệnh cục

### Bước 5: Xác Định Cách Cục (8 Cách Chính)

**Cách cục = Thập Thần lộ ở Nguyệt lệnh.**

| Cách | Điều kiện thành |
|---|---|
| **Chính Quan** | Có Tài + Ấn, không hình xung phá hại |
| **Tài cách** | Tài sinh Quan / Tài gặp Thực / Tài phối Ấn |
| **Ấn cách** | Sát Ấn tương sinh / Thực thần tiết tú / Khí Ấn tựu Tài |
| **Thực thần** | Thực sinh Tài / Thực chế Sát / Khí Thực tựu Sát |
| **Thất sát** | Thân cường, sát gặp chế (Ấn hóa/Thực chế/Kiếp hợp) |
| **Thương quan** | Thương sinh Tài / Thương phối Ấn / Thương giá Sát / Thương khí Quan |
| **Dương nhận** | Có Quan Sát chế Nhận, có Tài Ấn phối |
| **Kiến lộc** | Có Quan + Tài Ấn / Có Thực chế Sát / Có Thực sinh Tài |

**Điều kiện phá cách:**
- Quan gặp Thương → phá (cứu: thấu Ấn giải)
- Tài gặp Kiếp → phá (cứu: thấu Thực hóa)
- Ấn gặp Tài → phá (cứu: Kiếp Tài giải / Hợp Tài tồn Ấn)
- Thực gặp Kiêu → phá (cứu: Tựu Sát thành cách)
- Sát gặp Thực chế, Ấn hộ Sát → xấu (cứu: gặp Tài khứ Ấn tồn Thực)

### Bước 6: Phân Tích Thập Thần

Phân tích các tổ hợp thập thần quan trọng:

| Tổ hợp | Ý nghĩa |
|---|---|
| **Thực thần chế Sát** | Quyền uy, lãnh đạo, võ |
| **Thương quan phối Ấn** | Thông minh, nghịch phát, tài năng |
| **Sát Ấn tương sinh** | Quý cách, học vấn, quyền lực |
| **Tài Quan song mỹ** | Giàu + sang |
| **Quan Sát hỗn tạp** | Mâu thuẫn nội tại, thiếu rõ ràng |
| **Kiêu đoạt Thực** | Thiên Ấn khắc Thực Thần → mất tài, suy sức khỏe |

### Bước 7: Xét Địa Chi Tương Tác

- Hợp: Lục hợp, Tam hợp → thay đổi năng lượng cục
- Xung: Lục xung → biến động, có thể tốt (xung Kỵ Thần) hoặc xấu (xung Dụng Thần)
- Hình, Hại, Phá: các mức độ tác động khác nhau

**Lưu ý phân biệt phái:** Tử Bình truyền thống: Xung thường xấu. Manh Phái: Xung = Tố Công (xung Kỵ = tốt).

### Bước 8: Luận Tính Cách & Sự Nghiệp

Dựa vào:
- **Nhật chủ** + **hành** của nhật chủ
- **Cách cục** chính
- **Thập thần** mạnh nhất / nhiều nhất
- **Âm dương** của nhật chủ (Giáp = dương mộc = hướng ngoại, Ất = âm mộc = hướng nội...)

### Bước 9: Phân Tích Đại Vận

- Mỗi đại vận = 10 năm
- Đại vận đến Dụng Thần → thời kỳ hanh thông
- Đại vận đến Kỵ Thần → thời kỳ gian nan
- **Đại vận phá Cách Cục** → đại nạn
- **Đại vận giúp Cách Cục thành** → đại phát

> Dùng `mcp_tuvi_current_decadal_fortune` để xem đại hạn hiện tại.

### Bước 10: Đoán Lưu Niên

- Lưu niên gặp Dụng Thần → năm tốt
- Lưu niên gặp Kỵ Thần → năm xấu
- Lưu niên xung/hợp đại vận → biến động trong năm

> Dùng `mcp_tuvi_yearly_fortune` và `mcp_tuvi_yearly_detailed` để xem chi tiết lưu niên.

---

## TỬ BÌNH LẠC VIỆT — Đặc điểm riêng

### Nguồn gốc & dòng chảy

- **1973:** Ông Trần Việt Sơn mời Lâm Thế Đức phổ biến Tử Bình trên báo Khoa Học Huyền Bí
- **Lâm Thế Đức:** Tác giả "Tử Bình Nhập Môn" — sách Tử Bình đầu tiên phổ biến rộng tại Việt Nam. Điểm mạnh: Cách cục thành bại, Thiên can ngũ hợp có phân biệt tháng (ví dụ: tháng Giêng Bính Tân không hóa Thủy)
- **Đỗ Đình Tuân:** Phần lấy lá số căn bản, "Tử Bình Bí Giải" chưa xuất bản
- **Thiệu Vĩ Hoa:** Chú trọng Ngũ hành hơn Cách cục, chịu ảnh hưởng Đài Loan

### Phân biệt Tử Bình truyền thống vs Manh Phái

| Tiêu chí | Tử Bình truyền thống | Manh Phái |
|---|---|---|
| Bước đầu | Thân Vượng/Nhược | Tìm Tố Công (lá số đang LÀM GÌ?) |
| Dụng Thần | Hành cân bằng lá số | Can chi THỰC HIỆN Tố Công |
| Nguyệt lệnh | Xác định Cách Cục | Xác định Tân Lệnh (mệnh lệnh ẩn) |
| Thân Vượng/Nhược | Quan trọng nhất | Yếu tố phụ |
| Xét phú quý | Dụng Thần có lực + cách thành | Tố Công hoàn thành + tượng đẹp |
| Can hợp | Hợp Hóa (đổi Ngũ Hành) | Hợp = khóa chặt, thu phục |
| Chi xung | Phá hoại (thường xấu) | Một dạng Tố Công |
| Mộ Khố | Nhập Mộ = suy yếu | Nhập Mộ = cất kho. Xung Mộ = mở kho → phát |
| Đọc tượng | Ít chú trọng | Cực kỳ quan trọng (Giáp = cây, Bính = mặt trời...) |

### Thuật ngữ Manh Phái cốt lõi

| Thuật ngữ | Ý nghĩa |
|---|---|
| **Tố Công** | Bát tự đang làm gì? Can chi nào tham gia tạo thành quả |
| **Tân Lệnh** | Mệnh lệnh ẩn của bát tự — mục đích sống chính |
| **Chủ - Khách** | Chủ = ta (Nhật chủ, trụ ngày+giờ), Khách = người khác (trụ năm+tháng) |
| **Thể - Dụng** | Thể = công cụ (Nhật chủ, Ấn, Lộc, Tỷ Kiếp), Dụng = mục đích (Tài, Quan) |
| **Công Thần** | Can chi tham gia tạo công |
| **Phế Thần** | Can chi không tham gia tạo công |
| **Tặc Thần** | Yếu tố muốn chế — khi lực lượng chế quá mạnh, cần có tặc thần xuất hiện |

---

## HƯỚNG DẪN THỰC HÀNH

### Khi người dùng hỏi về Tử Bình Lạc Việt

1. **Dùng MCP tuvi:**
   - `mcp_tuvi_four_pillars` để lấy tứ trụ (4 trụ can chi, nạp âm, ngũ hành)
   - `mcp_tuvi_analyze_destiny` để phân tích tổng quan
   - `mcp_tuvi_divination` nếu cần luận giải toàn diện

2. **Luận giải theo quy trình 10 bước:**
   - Đánh giá Thân Vượng/Nhược
   - Xác định Dụng Thần (kết hợp Vượng Suy + Cách Cục + Điều Hậu)
   - Xác định Cách Cục chính
   - Phân tích Thập Thần tương tác
   - Xét Đại Vận hiện tại & Lưu Niên

3. **Áp dụng vào thực tế:**
   - Tư vấn công việc, tài lộc, tình cảm dựa trên Dụng Thần
   - Đề xuất màu sắc, hướng, vật phẩm phong thủy theo Dụng Thần
   - Xem thời điểm tốt/xấu trong năm (dựa vào Lưu Niên)

4. **Khi 2 phái (truyền thống vs Manh Phái) cho kết quả khác nhau:**
   - Trình bày cả 2 góc nhìn
   - Nêu rõ cách tiếp cận nào phù hợp với từng loại bát tự

### Ví dụ về Dụng Thần trong Đời sống

| Dụng Thần | Màu sắc | Hướng | Vật phẩm | Nghề nghiệp |
|---|---|---|---|---|
| Hỏa | Đỏ, cam, tím | Nam | Đèn, ruby, thạch anh hồng | Năng lượng, marketing, lãnh đạo |
| Thủy | Xanh dương, đen | Bắc | Bể cá, thác nước | Ngoại giao, vận tải, bất động sản |
| Mộc | Xanh lá | Đông | Cây cảnh | Giáo dục, y tế, sáng tạo |
| Kim | Trắng, xám | Tây, Tây Bắc | Đồng hồ, kim loại | Tài chính, kỹ thuật, luật |
| Thổ | Vàng, nâu | Trung tâm, hướng Tây Nam | Gốm sứ, pha lê | Bất động sản, nông nghiệp, xây dựng |

---

---

## OUTPUT — TRÌNH BÀY TRÊN TELEGRAM

Xem `references/TELEGRAM_FORMAT.md` cho toàn bộ quy tắc format.

**Nguyên tắc tóm tắt:**
- Gửi **3-4 tin ngắn** thay vì 1 tin siêu dài
- Emoji nhất quán: 📜=Tứ Trụ, 🏛️=Tử Vi, 🎯=Hành động, 🔄=Vận hạn
- Bold cho keyword chính, spoiler `||...||` cho chi tiết phụ
- Separator `━━━━━━━━━━━━━━━━` giữa các section
- **Luôn kết thúc = 🎯 HÀNH ĐỘNG** — người dùng biết phải làm gì

## Nguồn tham khảo

- **Sách:** Tử Bình Nhập Môn (Lâm Thế Đức), Tử Bình Chân Thuyên Bản Nghĩa (Hoàng Đại Lục), Tứ Trụ Căn Bản Thiết Yếu, Mệnh Lý Nan Đề
- **Diễn đàn:** tuvilyso.org, hocvienlyso.org, battutaman.vn
- **Phái:** Tử Bình Đài Loan/Hồng Kông (trọng cách cục), Manh Phái (Minh Di Đường — trọng tố công), Thiệu Vĩ Hoa (trọng ngũ hành)
- **GitHub:** ShaKirisakiKazehana/bazi-fengshui-calculator (tính toán bát tự cơ bản)
- **API:** MCP server `tuvi` (tính tứ trụ, đại hạn, lưu niên)

### Tham khảo thêm (cơ bản)

Xem `references/TAM_THAM_LUAN.md` cho:
- **Tam Thẩm** — khung đánh giá cường nhược Nhật Chủ (Lệnh, Địa, Thế)
- **Lộ Can** — nguyên tắc can ẩn tàng thấu ra

> ⚠️ Nội dung này được kế thừa từ skill `tuvi-bat-tu-expert` (đã absorb và xoá).

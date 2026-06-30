---
name: tuvi-agent
category: tuvi
description: >
  Chuyên gia luận giải Tử Vi Đẩu Số đa tầng — kết hợp Tử Vi, Tứ Trụ,
  Kinh Dịch, Cổ nhân thuật, Tâm lý học hành vi & Định luật vũ trụ để
  ứng dụng vào công sở, đầu tư, quan hệ & phát triển bản thân.
version: "2.0"
related_skills:
  - tuvi-dau-so-expert
  - tuvi-tu-tru-expert
  - tuvi-kinh-dich-expert
  - tuvi-phong-thuy-expert
  - tuvi-luu-nguyet-nhat
---

# 🏛️ TỬ VI AGENT — Chuyên Gia Luận Giải Đa Tầng

> "Cổ học để hiểu bản chất — Hiện đại để hành động — Định luật để phòng thân"

## 🎯 KHI NÀO DÙNG SKILL NÀY

- User hỏi về tử vi, vận hạn, lá số → load master + dispatch subsystems
- User hỏi về quyết định công sở/đầu tư/quan hệ → phân tích đa tầng
- User hỏi thời điểm hành động → tích hợp Kinh Dịch + Lưu Nguyệt
- User cần insight thực tế, không chỉ đọc sao suông

---

## 🏗️ KIẾN TRÚC 5 TẦNG

```
┌──────────────────────────────────────────────────────────┐
│ TẦNG 1 — INPUT                                           │
│ 5 yếu tố sinh + vấn đề + mục tiêu người dùng            │
└───────────────────────┬──────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────┐
│ TẦNG 2 — CORE ENGINE (subskills)                         │
│  ├── TỬ VI ĐẨU SỐ → tuvi-dau-so-expert                  │
│  ├── TỨ TRỤ / BÁT TỰ → tuvi-tu-tru-expert               │
│  └── KINH DỊCH → tuvi-kinh-dich-expert                   │
│  + tuvi-luu-nguyet-nhat (Python engine)                  │
└───────────────────────┬──────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────┐
│ TẦNG 3 — BRIDGE LAYER (giữa cổ điển & hiện đại)         │
│  ├── 🧠 Tâm lý học hành vi ↔ Sao                         │
│  ├── ⚖️ Định luật vũ trụ ↔ Vận hạn                       │
│  └── 👑 Cổ nhân thuật ↔ Tình huống hiện đại              │
└───────────────────────┬──────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────┐
│ TẦNG 4 — DOMAIN APPLICATION                              │
│  ├── 💼 Công sở (sếp, đồng nghiệp, thăng chức)           │
│  ├── 💰 Đầu tư (timing, risk, tâm lý thị trường)         │
│  ├── ❤️ Quan hệ (tình yêu, đối tác, gia đình)            │
│  └── 🧘 Phát triển bản thân                              │
└───────────────────────┬──────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────┐
│ TẦNG 5 — OUTPUT                                          │
│ 📊 Insight → 🔮 Dự báo → 🎯 Action Plan → ⚠️ Cảnh báo   │
└──────────────────────────────────────────────────────────┘
```

---

## 🔄 WORKFLOW 6 BƯỚC

### Bước 1: Thu thập
- 5 yếu tố bắt buộc: năm/tháng/ngày/giờ sinh (DL) + giới tính
- Vấn đề cần tư vấn: công sở? đầu tư? quan hệ? tất cả?
- Mục tiêu: đang cần quyết định gì?

### Bước 2: Tính toán căn bản
Ưu tiên dùng `mcp_tuvi_calculate_chart` (MCP iztro) để lấy lá số.
Fallback: dùng browser tra trang web tử vi, hoặc an sao thủ công theo AN_SAO.md.
Nếu cần Tứ Trụ → `mcp_tuvi_four_pillars`.

### Bước 3: Luận giải Tử Vi nền (Tầng 2)
Load `tuvi-dau-so-expert`:
- Xác định Cách Cục chính
- Đọc cung Mệnh + Thân + Tam Phương
- Tứ Hóa vị trí (Lộc/Quyền/Khoa/Kỵ ở đâu?)
- Đại hạn hiện tại
- Lưu niên (nếu hỏi năm cụ thể)

Load `tuvi-tu-tru-expert` nếu cần Tứ Trụ cross-ref.
Load `tuvi-kinh-dich-expert` nếu cần gieo quẻ cho quyết định.

### Bước 4: Bridge (Tầng 3) — ĐIỂM KHÁC BIỆT CỐT LÕI
Sau khi có luận giải nền, thêm 3 lớp chồng:

**🧠 Tâm lý học hành vi** (xem bảng bên dưới):
```
Sao A + Sao B tại cung X → pattern tâm lý Y
Ví dụ: Tham Lang Hóa Lộc tại Tài Bạch
→ Overconfidence bias, dễ đầu tư quá mức
→ Giải pháp: nguyên tắc 1% (chỉ mạo hiểm 1% tài sản/lần)
```

**⚖️ Định luật vũ trụ** (xem bảng bên dưới):
```
Hóa Kỵ + Xung tại Quan Lộc
→ Murphy's Law: nếu có thể sai, sẽ sai
→ Dự báo: tháng 7-8 âm lịch có biến
→ Phòng: có plan B, không ký hợp đồng dài hạn
```

**👑 Cổ nhân thuật** (xem bảng bên dưới):
```
Nô Bộc nhiều sát tinh + Mệnh Tử Vi
→ Đồng nghiệp đang âm mưu
→ Kế 36: "Mượn đao giết người" — để người khác làm hộ
```

### Bước 5: Ứng dụng Domain (Tầng 4)
Áp dụng bảng domain bên dưới cho từng lĩnh vực.

### Bước 6: Output (Tầng 5)
Format Telegram, chia 3-4 tin ngắn:
1. 📊 **Tổng quan** — Lớp 1: Tử Vi nói gì
2. 🧠 **Góc nhìn mới** — Lớp 2: Tâm lý + Định luật + Cổ nhân
3. 🎯 **Hành động** — Lớp 3: Action Plan + Timing
4. ⚠️ **Cảnh báo** (nếu có)

---

## 🧠 BRIDGE LAYER — TÂM LÝ HỌC HÀNH VI

### Bảng ánh xạ Sao ↔ Cognitive Biases

| Sao | Pattern Tử Vi | Tâm lý học hành vi | Biểu hiện đời thực |
|-----|---------------|-------------------|-------------------|
| **Tham Lang HL** | Ham muốn, đa dục, liều lĩnh | *Overconfidence bias* • *Hyperbolic discounting* | Đầu tư all-in, mua hàng theo cảm xúc |
| **Vũ Khúc HKỵ** | Nguyên tắc, sợ sai, tê liệt | *Loss aversion* • *Status quo bias* | Không dám thay đổi, bỏ lỡ cơ hội |
| **Liêm Trinh** | Thể diện, ganh đua | *Conspicuous consumption* • *Social comparison* | Xài đồ hiệu không cân xứng thu nhập |
| **Cự Môn** | Thị phi, nói nhiều | *Confirmation bias* • *Gossip effect* | Tin đồn, bị nói xấu, hiểu lầm |
| **Phá Quân** | Phá cũ làm mới | *Creative destruction* • *Disruptive innovation* | Khởi nghiệp, đổi ngành, ly hôn |
| **Thiên Cơ** | Kế hoạch, tính toán | *Analysis paralysis* • *Planning fallacy* | Lên kế hoạch quá kỹ không hành động |
| **Thái Dương** | Hào phóng, thích thể hiện | *Spotlight effect* • *Warm glow giving* | Cho vay không đòi, đầu tư vì danh |
| **Thiên Phủ** | Ổn định, tích lũy | *Endowment effect* • *Hoarding* | Giữ tài sản quá lâu, không bán |
| **Sát Phá Tham** | Liều, táo bạo, bất chấp | *Dunning-Kruger* • *Risk-seeking* | "Được ăn cả ngã về không" |
| **Tử Vi + Hóa Kỵ** | Cô độc, sợ mất quyền | *Impostor syndrome* • *Micromanagement* | Sợ bị soán ngôi, quản lý vi mô |

### Behavioral Economics pattern cho từng cung

| Cung | Nguyên tắc Kinh tế học hành vi | Ứng dụng khi luận giải |
|------|-------------------------------|----------------------|
| **Tài Bạch** | *Mental accounting* (tiền ảo vs tiền thật) | Chia tài chính thành nhiều quỹ riêng |
| **Quan Lộc** | *Peter principle* (thăng đến mức bất tài) | Đừng thăng chức chỉ vì thành tích cũ |
| **Nô Bộc** | *Dunbar's number* (tối đa 150 quan hệ) | Tập trung vào 5 người quan trọng nhất |
| **Phu Thê** | *Mere-exposure effect* (quen = thích) | Nhàm chán là tự nhiên, không phải lỗi |
| **Phúc Đức** | *Reciprocity* (cho = nhận lại) | Xây dựng mạng lưới giá trị |

---

## ⚖️ BRIDGE LAYER — ĐỊNH LUẬT VŨ TRỤ

### Bảng ánh xạ Định luật ↔ Vận hạn Tử Vi

| Định luật | Ánh xạ Tử Vi | Ứng dụng thực tế |
|-----------|-------------|-----------------|
| **Murphy's Law** | Hóa Kỵ + Xung tại cung chủ đạo | Nếu có thể sai, nó sẽ sai — có plan B |
| **Parkinson's Law** | Tham Lang + Không/Kiếp | Công việc nở ra choán hết thời gian — giới hạn chặt |
| **Bảo toàn NL** | Lộc đến đâu, Kỵ đến đó | Tiền kiếm dễ → tiêu cũng dễ. Kiểm soát |
| **Entropy** | Cách cục suy dần theo Đại hạn | Không có gì giữ mãi. Phải đổi mới liên tục |
| **Pareto 80/20** | 20% sao tạo 80% vận mệnh | Chỉ cần focus 2-3 sao chính + Tứ Hóa |
| **Newton's Cradle** | Đại hạn = quả lắc. Tốt → xấu → tốt | Không thắng mãi, không thua mãi |
| **Hofstadter's Law** | Thiên Cơ Hóa Kỵ | Việc luôn lâu hơn dự kiến — nhân đôi dự trù |
| **Occam's Razor** | Cách cục thanh = đơn giản = tốt | Cách tốt nhất là đơn giản nhất |
| **Sturgeon's Law** | 90% sao tầm thường | Đừng đọc từng sao lẻ — chỉ focus sao quan trọng |

### Cách dùng trong luận giải

Khi thấy Hóa Kỵ + Xung tại cung trọng yếu:
```
⚖️ Định luật Murphy:
"Nếu việc này có thể sai, nó sẽ sai vào lúc tồi tệ nhất"
→ Bạn đang ở trong vùng Xung + Hóa Kỵ
→ Đừng kỳ vọng mọi chuyện suôn sẻ
→ Giải pháp: chuẩn bị plan B, C, D
→ Thời điểm: qua tháng X âm lịch (hết lưu Kỵ) mới yên
```

Khi thấy Tham Lang + Không Kiếp (Phá cách):
```
⚖️ Parkinson's Law:
"Công việc nở ra choán hết thời gian được cho"
→ Tham Lang đa dục + Không Kiếp mở rộng vô độ
→ Bạn đang làm quá nhiều thứ cùng lúc
→ Giải pháp: cắt 70% tasks, focus 30% cốt lõi
```

---

## 👑 BRIDGE LAYER — CỔ NHÂN THUẬT

### Bảng ánh xạ Tình huống hiện đại ↔ Cổ nhân thuật

| Tình huống | Tử Vi thường thấy | Cổ nhân thuật | Ứng dụng |
|-----------|------------------|--------------|----------|
| Bị sếp chèn ép | Nô Bộc có sát tinh | **Quỷ Cốc Tử — Xú Quyết**: bôi nhọ đối thủ = tự hại → đừng phản ứng tiêu cực | Im lặng thu thập chứng cứ, để sếp tự lộ |
| Đồng nghiệp cướp công | Quan Lộc có Kình/Đà | **Kế 3: Mượn đao giết người** | Để sếp lớn biết, không tự đối đầu |
| Cạnh tranh khốc liệt | Mệnh Thất Sát | **Tôn Tử — Biết người biết ta** | Phân tích điểm yếu đối thủ, đánh vào đó |
| Cần quyết định đầu tư | Tài Bạch có Lộc Mã | **Kinh Dịch — Quẻ Thái** (hanh thông) | Đã đến lúc, nhưng chia nhỏ vốn |
| Mệt mỏi, kiệt sức | Mệnh yếu + Tật Ách có sát | **Vương Dương Minh — Hành tri hợp nhất** | Nghỉ là hành động. Làm ít hơn để được nhiều hơn |
| Bế tắc không lối ra | Mệnh Vô Chính Diệu | **Kế 28: Thượng ốc trừu thê** — lui để tiến | Bỏ cái cũ, tìm môi trường mới |
| Bị phản bội | Giao Hữu có Liêm Trinh | **Tào Tháo — "Thả neo"** | Tạo tình thế có lợi cho mình trước |
| Mới khởi nghiệp | Mệnh Phá Quân | **Quỷ Cốc Tử — Phi Phù** (tung tin đồn chiến lược) | Tạo tín hiệu thị trường mạnh |
| Đàm phán quan trọng | Cung liên quan có Tả Hữu | **Kế 5: Thừa hỏa đả kiếp** | Tận dụng lúc đối thủ yếu |
| Cần thời cơ | Đại hạn chưa tới | **Nho giáo — "Không thấy lợi chớ động"** | Chờ đợi là chiến lược |

### 36 Kế — Bảng tra nhanh (top-10 ứng dụng Tử Vi)

| Kế | Tên | Ứng dụng Tử Vi |
|----|-----|---------------|
| 1️⃣ | Man thiên quá hải | Giấu kế hoạch — Thái Âm Hóa Kỵ |
| 2️⃣ | Vây ngụy cứu triệu | Đánh điểm yếu đối thủ — Phá Quân |
| 3️⃣ | Mượn đao giết người | Dùng người khác — Thiên Cơ Hóa Lộc |
| 4️⃣ | Dĩ dật đãi lao | Lấy nhàn chờ mệt — Thiên Đồng |
| 5️⃣ | Thừa hỏa đả kiếp | Nhân lúc cháy nhà — Hỏa Tinh+Linh Tinh |
| 6️⃣ | Dương đông kích tây | Đánh lạc hướng — Văn Xương+Văn Khúc |
| 7️⃣ | Vô trung sinh hữu | Từ không tạo có — Địa Không+Địa Kiếp |
| 8️⃣ | Ám độ trần thương | Lặng lẽ hành động — Tham Lang |
| 9️⃣ | Cách ác quan hỏa | Đứng núi này trông núi nọ — Thiên Di |
| 🔟 | Tiểu ly đại kế | Tách nhỏ — Cự Môn |

---

## 💼 DOMAIN — CÔNG SỞ

### 1. Quan hệ với sếp

| Cung Mệnh user | Tương tác với sếp |
|---------------|-------------------|
| **Tử Vi ở Mệnh** | Không thích bị sai bảo. Tốt nhất làm sếp luôn |
| **Thiên Cơ** | Hợp với sếp thông minh, ghét sếp ngu |
| **Cự Môn** | Dễ bị hiểu lầm. Cần giao tiếp rõ ràng, bằng văn bản |
| **Liêm Trinh** | Cạnh tranh ngầm với sếp. Cẩn thận |
| **Thái Dương** | Hợp với sếp cởi mở. Làm việc công khai |

### 2. Thăng chức timing

Xem:
- **Quan Lộc**: có Hóa Lộc/quyền/khoa? → cơ hội
- **Đại hạn**: đại hạn có ảnh hưởng đến Quan Lộc không?
- **Lưu niên**: năm nào Tuế Dẫn tốt cho Quan Lộc?
- **Lưu Nguyệt**: tháng nào lưu Quan Lộc có cát tinh?

### 3. Chính trị văn phòng

| Effect | Tử Vi pattern | Chiến thuật |
|--------|--------------|------------|
| Bị cô lập | Nô Bộc nhiều sát + Mệnh yếu | Kế 3 (mượn đao) |
| Bị nói xấu | Quan Lộc Cự Môn + Hóa Kỵ | Kế 8 (ám độ) — im lặng, để thành tích nói |
| Bị cướp công | Quan Lộc Không Kiếp | Ghi lại mọi thứ bằng email |
| Muốn thăng chức | Quan Lộc Tả Hữu + Khôi Việt | Tìm người bảo lãnh, đừng tự claim |
| Sắp bị sa thải | Quan Lộc tử tù + đại hạn xấu | Kế 28 (thượng ốc) — chủ động tìm đường mới |

---

## 💰 DOMAIN — ĐẦU TƯ

### 1. Timing đầu tư

| Tử Vi pattern | Hành động |
|--------------|----------|
| **Tài Bạch + Hóa Lộc** | Cơ hội đầu tư. Lộc đến đâu Kỵ đến đó → chốt lời sớm |
| **Tài Bạch + Lộc Mã** | Đầu tư xa. BĐS nước ngoài, cổ phiếu quốc tế |
| **Tài Bạch có sát (Kình/Đà/Không/Kiếp)** | Không đầu tư mạo hiểm. Tích trữ |
| **Đại hạn vào cung Tài** | 10 năm tới focus vào kiếm tiền |
| **Lưu Nguyệt Tài Bạch có Hóa Lộc** | Tháng tốt để đầu tư |
| **Kinh Dịch quẻ Khảm ở Tài** | Thời điểm rủi ro cao — cẩn trọng |

### 2. Tâm lý thị trường

| Tử Vi user | Lỗi thường gặp | Giải pháp |
|-----------|---------------|-----------|
| **Tham Lang Tài** | FOMO, mua đỉnh, không chốt lời | Nguyên tắc 1%: mỗi lệnh = 1% portfolio |
| **Vũ Khúc Tài** | Sợ xuống tiền, bỏ lỡ sóng | DCA: chia nhỏ, vào dần |
| **Liêm Trinh Tài** | Đầu tư theo đám đông, khoe lãi | Tài khoản riêng, không nói với ai |
| **Phá Quân Tài** | Đòn bẩy quá nhiều, cháy tài khoản | Margin tối đa 20% |
| **Thiên Phủ Tài** | Giữ quá lâu, không chốt | Nguyên tắc trailing stop |

### 3. Risk management (Tử Vi × Murphy)

```
⚠️ Cảnh báo Murphy khi:
- Tài Bạch + Hóa Kỵ → "Nếu thị trường có thể đảo chiều, nó sẽ đảo"
- Tài Bạch + Tuần Triệt → Cơ hội đến rồi đi mất
- Tài Bạch + Không Kiếp → Lời ảo, lỗ thật

🛡️ Phòng vệ:
- Mỗi lệnh = max 5% portfolio
- Stop-loss = 8%
- Cash reserve = 30% khi có dấu hiệu xấu
```

---

## ❤️ DOMAIN — QUAN HỆ

### 1. Hợp tan trong tình yêu

| Cặp tinh đẹp | Ý nghĩa |
|-------------|---------|
| **Tả Phù + Hữu Bật** đồng cung Phu Thê | Hôn nhân tốt, có người giúp |
| **Thiên Đồng + Thiên Lương** chiếu Phu Thê | Tình già, bền lâu |
| **Khôi Việt** chiếu | Gặp qua bạn bè, quý nhân mai mối |
| **Hồng Loan + Thiên Hỷ** | Tình yêu đẹp, cưới hỏi vui |

### 2. Hợp tác làm ăn

| Cặp | Kết quả |
|-----|---------|
| **Mệnh tam hợp** (Dần-Ngọ-Tuất, v.v.) | Hợp, bền lâu |
| **Mệnh lục hại** (Tý-Mùi, Sửu-Ngọ...) | Cãi nhau, dễ tan |
| **Tài một người + Quan một người** | Hợp: người làm tiền + người quản lý |
| **Cùng Hóa Lộc ở Tài** | Cả hai cùng kiếm, nhưng tranh giành |
| **Cùng Hóa Kỵ ở Tài** | Cả hai cùng khó — dễ đổ lỗi cho nhau |

---

## 🧘 DOMAIN — PHÁT TRIỂN BẢN THÂN

### Xác định nghề nghiệp phù hợp qua sao Mệnh

| Sao Mệnh | Nghề tốt | Nghề tránh |
|---------|---------|-----------|
| Tử Vi | Lãnh đạo, quản lý, chính phủ | Làm thuê cả đời |
| Thiên Cơ | Chiến lược, tư vấn, AI/tech | Công việc chân tay |
| Thái Dương | Giáo dục, truyền thông, chính trị | Ẩn dật |
| Vũ Khúc | Tài chính, kế toán, phân tích | Sáng tạo tự do |
| Tham Lang | Sales, marketing, nghệ thuật | Khuất mày khuất mặt |
| Liêm Trinh | Luật, quân sự, tư pháp | Kinh doanh thiếu chuẩn mực |
| Thất Sát | Khởi nghiệp, thể thao, quân sự | Ổn định |
| Phá Quân | Đổi mới, startup, phá vỡ | Công sở |
| Thiên Tướng | Quản lý, hành chính | Đầu cơ |
| Thiên Lương | Y tế, giáo dục, phi lợi nhuận | Kinh doanh thuần lợi nhuận |
| Cự Môn | Luật sư, MC, truyền thông | Im lặng |
| Thái Âm | BĐS, tài chính, nghệ thuật | Quá công khai |
| Thiên Phủ | Quản lý, hành chính, ổn định | Mạo hiểm |
| Thiên Đồng | Dịch vụ, chăm sóc, nghệ thuật | Áp lực cao |

---

## 📤 OUTPUT FORMAT (Telegram)

Chia làm 3-4 tin, mỗi tin focus 1 lớp:

```
🏛️ GIẢI MÃ SỐ PHẬN — [CHỦ ĐỀ]
━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 LỚP 1 — TỬ VI NỀN
• Cung A: [sao chính] + [Tứ Hóa] → [luận giải ngắn]
• Cách cục: [tên cách] → [ý nghĩa]
• Đại hạn: [tuổi] tại cung [tên] → [xu hướng]

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 LỚP 2 — TÂM LÝ & CỔ NHÂN
• [Tâm lý]: [cognitive bias] → [biểu hiện] → [giải pháp]
• [Định luật]: [tên] → [ánh xạ] → [phòng vệ]
• [Cổ nhân]: [kế / thuật] → [áp dụng]

━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 LỚP 3 — ACTION PLAN
1. [Ngắn hạn - tuần này]: [hành động cụ thể]
2. [Trung hạn - tháng]: [timing + hành động]
3. [Dài hạn]: [xu hướng + chuẩn bị]

━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ CẢNH BÁO
• Thời điểm nhạy cảm: [tháng/ngày]
• Rủi ro: [mô tả] → [phòng vệ]

✨ *Tử vi cho thấy xu hướng, không phải định mệnh*
```

---

## 🤖 AGENT INTEGRATION (Hermes)

### Load sequence

```python
# === 1. Load master skill ===
# skill_view("tuvi-agent")
# → đọc kiến trúc, workflow, bridge layers, domain modules
# → biết cần dispatch subsystem nào

# === 2. Dispatch theo nhu cầu ===
# Tử Vi cơ bản → skill_view("tuvi-dau-so-expert")
# Tứ Trụ → skill_view("tuvi-tu-tru-expert")
# Kinh Dịch → skill_view("tuvi-kinh-dich-expert")
# Lưu Nguyệt/Nhật chi tiết → tuvi-luu-nguyet-nhat engine

# === 3. Áp dụng bridge layer ===
# Nội dung bridges + domains đã có sẵn trong skill này
```

### Khi nào dùng bridge nào

| Yêu cầu user | Bridge layer |
|-------------|-------------|
| "Tôi nên đầu tư không?" | Psychology (overconfidence) + Laws (Murphy) + Domain (investment) |
| "Bị sếp chèn ép" | Ancient (Quỷ Cốc Tử) + Domain (workplace) |
| "Tình cảm trục trặc" | Psychology (mere-exposure) + Domain (relationships) |
| "Nên đổi việc không?" | Laws (Parkinson) + Domain (workplace) + Kinh Dịch (timing) |
| "Tôi hợp làm nghề gì?" | Tử Vi nền + Domain (self-growth) |
| "Tháng này thế nào?" | Lưu Nguyệt engine + Psychology |

---

## 🔗 HỆ THỐNG SKILL

### Subsystems (tải theo nhu cầu)
- `tuvi-dau-so-expert` — Tử Vi Đẩu Số (an sao, 12 cung, cách cục)
- `tuvi-tu-tru-expert` — Tử Bình Lạc Việt / Bát Tự
- `tuvi-kinh-dich-expert` — Kinh Dịch
- `tuvi-phong-thuy-expert` — Phong Thủy

### Engine (tính toán tự động)
- `tuvi-mcp-server` — MCP iztro (tính lá số, đại hạn, lưu niên)
- `tuvi-luu-nguyet-nhat` — Python engine Lưu Nguyệt/Nhật (chạy local)

### Master
- **tuvi-agent** ← skill này. Entry point duy nhất cho mọi yêu cầu Tử Vi.

> Khi AI Agent load skill này, tự động biết:
> 1. Workflow luận giải 6 bước
> 2. Map tới các subsystem cần thiết
> 3. Khi nào cần bridge layer nào
> 4. Format output Telegram chuẩn

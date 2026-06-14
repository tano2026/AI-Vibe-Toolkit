# Voice Profile Builder — Biến Bản Thân Thành Phiên Bản Đỉnh Cao Trong Claude

**Nguồn:** AI Leaders Vietnam — how-to-ai.guide
**Dạng:** Workflow + Prompt Templates — 2 giai đoạn
**Target:** Content creator, founder, người dùng Claude thường xuyên

---

## Vấn Đề

**Trước đây:**
- Mày viết nhiều, Claude nghĩ ít
- Mày gõ prompt dài, sửa đi sửa lại
- Output chung chung, không có giọng của mày

**Sau này (với Voice Profile):**
- Claude suy nghĩ nhiều, mày viết ít
- Paste 1 file là Claude hiểu mày là ai
- Output đúng tone, đúng cách diễn đạt của mày

Lý do: Claude không biết mày là ai, nghĩ gì, nói chuyện kiểu gì. Mỗi lần chat là bắt đầu lại từ đầu. Voice Profile fix điều đó — một file context chứa "bản thân mày" để paste vào mọi conversation.

---

## Giai Đoạn 1 — Phỏng Vấn Bản Thân (Tạo Raw Material)

### Setup
```
- Tải Claude (hoặc dùng claude.ai)
- Mở chế độ Cowork (Projects)
- Tạo thư mục: Giọng nói của bạn
- Chọn model: Claude Opus 4.7
- Bật chế độ Tư duy mở rộng (Extended Thinking)
```

### Prompt 1 — Người Phỏng Vấn

```
Bạn là một nhà tâm lý học kiêm nhà báo chuyên phỏng vấn sâu.
Nhiệm vụ: Giúp tôi khám phá giọng nói, tư duy và bản sắc thật sự của mình 
thông qua 100 câu hỏi phỏng vấn.

Quy tắc:
- Đọc to, đừng gõ (nói chuyện tự nhiên hơn)
- Trả lời tất cả 100 câu hỏi
- Đẩy các câu trả lời chung chung — hỏi "Cụ thể hơn?"
- Ghi lại các điểm bạn từ chối trả lời (đó là điểm mạnh ẩn)
- Ghi lại những cụm từ hiếm khi dùng nhưng rất "mày"

Bắt đầu phỏng vấn ngay.
```

**Mục tiêu:** Ra được transcript thô — cách mày nói chuyện thật, không filter.

---

## Giai Đoạn 2 — Biên Tập Thành Voice Profile

### Prompt 2 — Người Biên Tập Giọng Nói

```
Bạn là biên tập viên giọng nói chuyên nghiệp.

Nhiệm vụ: Từ transcript phỏng vấn trên, tạo ra file [tên_của_bạn].md 
chứa đầy đủ bản sắc giọng nói của tôi.

Cấu trúc file cần có:
1. Tóm tắt con người (5-7 câu)
2. Cách tôi tư duy
3. Cách tôi diễn đạt (từ hay dùng, cấu trúc câu đặc trưng)
4. Điều tôi quan tâm nhất
5. Điều tôi ghét / tránh
6. Ví dụ câu văn "rất mày"
7. Những cụm từ đặc trưng của tôi

Sau đó:
- Rút gọn 20,000 từ thành ~4,000 tokens
- Lưu thành [ten_cua_ban].md
- Kiểm tra trong một phiên mới trống (không có context)
```

---

## Sử Dụng Voice Profile

### Cách 1 — Paste vào đầu conversation

```
[Nội dung file ten_cua_ban.md]

Bây giờ hãy viết [task] theo đúng giọng và tư duy của tôi.
```

### Cách 2 — Dùng với Cowork (Projects)

```
- Thả file vào thư mục Cowork
- Claude tự đọc mỗi lần chat trong Project đó
- Không cần paste lại
```

### Cách 3 — Cross-platform

```
- Lưu file .md trong Obsidian
- Mở Cowork như một kho lưu trữ
- Chỉnh sửa như Google Docs
- Kết nối sang ChatGPT, Grok, Gemini nếu cần
- Cập nhật theo sự thay đổi của bạn (3-6 tháng/lần)
```

---

## Ứng Dụng Thực Tế

**Content creator:**
```
[Voice Profile của mày]
Viết script TikTok về DiffusionGemma theo đúng cách tao hay nói
→ Output có giọng của mày, không phải giọng AI chung chung
```

**Founder viết email:**
```
[Voice Profile của mày]
Viết cold email cho [đối tượng] theo cách tao hay communicate
→ Không ai nhận ra là AI viết
```

**Vibe coder viết docs:**
```
[Voice Profile của mày]
Viết README cho repo này theo kiểu tao hay giải thích
→ Docs có personality, không dry và kỹ thuật thuần túy
```

---

## Template Voice Profile — Ví Dụ Cấu Trúc

```markdown
# Voice Profile — [Tên của mày]
*Cập nhật: [ngày]*

## Tao là ai (5-7 câu)
[Mô tả ngắn gọn: làm gì, nghĩ gì, care về gì]

## Cách tao tư duy
- Tao hay bắt đầu từ [...]
- Khi gặp vấn đề, tao thường [...]
- Tao ghét khi [...]

## Cách tao diễn đạt
**Từ hay dùng:** [list]
**Cấu trúc câu đặc trưng:** [ví dụ]
**Tone:** [casual/formal/mixed]

## Tao quan tâm nhất
1. [...]
2. [...]

## Tao tránh
- [...]

## Câu văn "rất tao"
> "[Ví dụ câu mày hay viết]"
> "[Ví dụ khác]"

## Cụm từ đặc trưng
- "[cụm 1]"
- "[cụm 2]"
```

---

## Tips Dùng Hiệu Quả

**1. Dùng voice (nói) thay vì gõ trong Giai đoạn 1**
Khi nói tự nhiên, mày reveal nhiều hơn khi gõ. Output sẽ "thật" hơn.

**2. Đừng filter trong phỏng vấn**
Câu trả lời đầu tiên thường là thật nhất. Claude hỏi "cụ thể hơn?" thì trả lời thẳng, đừng suy nghĩ quá.

**3. Chú ý những chỗ mày từ chối trả lời**
Đó thường là điểm mạnh hoặc điều mày care nhất — biên tập viên sẽ khai thác những chỗ này.

**4. Test trong conversation trống**
Sau khi có file, mở tab mới hoàn toàn, paste file vào, hỏi Claude "Tao là ai?" — nếu Claude describe đúng mày thì file đạt yêu cầu.

**5. Update định kỳ**
Mày thay đổi theo thời gian. Update file 3-6 tháng/lần — không phải tạo lại từ đầu, chỉ cập nhật những gì đã thay đổi.

---

## Đánh Giá Cá Nhân

Cái này tao thấy là một trong những workflow Claude ít người biết nhưng impact lớn nhất.

Hầu hết người dùng Claude theo kiểu: hỏi → nhận → chỉnh → hỏi lại. Vòng lặp đó tốn thời gian vì Claude không biết mày muốn gì ở mức sâu hơn câu hỏi cụ thể.

Voice Profile phá vỡ vòng lặp đó. Claude không chỉ biết mày hỏi gì — nó biết mày là ai, nghĩ thế nào, nói chuyện ra sao. Output lần đầu gần với cái mày muốn hơn rất nhiều.

Workflow của AI Leaders Vietnam có điểm thú vị: dùng Extended Thinking trong giai đoạn phỏng vấn — Claude "suy nghĩ sâu" về câu trả lời của mày trước khi follow-up. Output phong phú hơn so với chat thường.

Hạn chế: Mất 1-2 tiếng để hoàn thành đầy đủ. Nhưng đây là investment một lần, dùng mãi.

**Rating: 9/10** — một trong những skills quan trọng nhất trong kho.

---

*Nguồn: AI Leaders Vietnam — how-to-ai.guide*
*Cập nhật: tháng 6/2026*

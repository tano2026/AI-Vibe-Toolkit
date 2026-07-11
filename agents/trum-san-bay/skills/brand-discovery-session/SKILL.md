# Brand Discovery Session — Trùm Sân Bay

## Vì sao skill này quan trọng

`brand-voice/SKILL.md` tao viết ban đầu là **tao tự suy luận** persona dựa trên brief ngắn của mày — nó hợp lý nhưng chưa được "phỏng vấn" đúng cách để tìm ra chất riêng thật sự. Skill `brand-discovery` từ ECC dạy đúng phương pháp: laddering (hỏi "vì sao" liên tục tới khi ra core value), 5 Whys, projective techniques — để đào ra brand identity thật thay vì đoán.

Đây là bản điều chỉnh riêng cho Trùm Sân Bay — dùng để deepen persona TRƯỚC KHI apply full-auto, không phải bắt buộc làm ngay.

## Cách chạy

Chạy như 1 buổi phỏng vấn thật với Nobitano — không hỏi dồn 1 lúc nhiều câu, hỏi từng cái, paraphrase lại, đào sâu bằng "vì sao" tới khi ra được câu trả lời cụ thể chứ không chung chung.

## 6 module cho Trùm Sân Bay (rút gọn từ 8 module gốc ECC)

### Module 1 — Purpose (Vì sao page này tồn tại)
```
Câu hỏi mở: "Ngoài việc bán Fast Track/SIM/đổi tiền, Trùm Sân Bay tồn tại 
để giải quyết cái gì cho khách mà chưa ai làm tốt?"

Laddering: Nếu trả lời "để khách đi máy bay dễ hơn" → hỏi tiếp "vì sao 
điều đó quan trọng với mày?" → tới khi ra được lý do cá nhân/kinh doanh 
cụ thể (vd: "vì tao thấy nhiều page chỉ bán mà không thật lòng tư vấn")
```

### Module 2 — Founder Tension (Căng thẳng giữa cho và bán)
```
Câu hỏi: "Ranh giới giữa 'tư vấn thật' và 'bán hàng' ở đâu? Có tình huống 
nào mày sẵn sàng KHÔNG bán dù khách hỏi mua không?"

5 Whys: Đào tới khi ra được nguyên tắc rõ ràng, vd "không bán Fast Track 
nếu khách chỉ transit 40 phút — không kịp dùng, bán là lừa khách"
→ Đây chính là nguyên liệu cho guardrail thật, không phải guardrail chung 
  chung như "tư vấn thật, không ép mua"
```

### Module 3 — Voice Origin (Giọng nói này từ đâu ra)
```
Câu hỏi: "Nhân vật 'nhân viên sân bay 15 năm' — mày tưởng tượng ra 1 người 
cụ thể nào không? Hay dựa trên ai mày biết ngoài đời?"

Nếu có người thật làm hình mẫu → hỏi thêm: "Người đó nói chuyện có tật gì, 
câu cửa miệng gì, phản ứng thế nào khi bực?"
→ Chi tiết cụ thể này sẽ tạo few-shot examples chân thật hơn nhiều so với 
  4 ví dụ tao tự viết trong writer-agent-prompt
```

### Module 4 — Audience Reality (Khách thật là ai)
```
Câu hỏi: "Nghĩ tới 1 khách hàng thật mày từng gặp/tưởng tượng — họ đi 
chuyến gì, lo lắng gì nhất, tại sao follow page thay vì hỏi Google?"

Projective: "Nếu Trùm Sân Bay là 1 người trong sân bay thật, đứng ở đâu? 
Quầy check-in? Khu chờ? Fast track lounge?"
```

### Module 5 — Competitive Distinction (Khác gì page sân bay khác)
```
Câu hỏi: "Có page/kênh nào đang làm content sân bay mày thấy hay nhưng 
mày làm khác đi? Khác ở đâu?"

→ Output module này feed thẳng vào competitive-platform-analysis (xem 
  skill riêng) để Research Agent biết benchmark ai
```

### Module 6 — Non-Negotiables (Điều tuyệt đối không làm)
```
Câu hỏi: "Có nội dung/hành động nào dù tăng tương tác/doanh thu mày cũng 
không làm? Vì sao?"

→ Đây chính là nguyên liệu cứng cho guardrail trong Writer + Reply prompt, 
  cụ thể hơn nhiều so với rule chung "không bịa thông tin"
```

## Output — 90_SYNTHESIS.md

Sau khi chạy đủ 6 module, tổng hợp thành 1 file duy nhất:

```markdown
# Trùm Sân Bay — Brand Synthesis

## Purpose thật (không phải version marketing)
[Từ Module 1]

## Nguyên tắc cho/bán (cụ thể, có ví dụ tình huống thật)
[Từ Module 2]

## Voice reference (người/tật/câu cửa miệng cụ thể)
[Từ Module 3]

## Audience persona thật (1-2 nhân vật cụ thể, không phải demographic chung)
[Từ Module 4]

## Khác biệt cạnh tranh
[Từ Module 5]

## Non-negotiables (dùng trực tiếp làm guardrail)
[Từ Module 6]
```

File này khi có, sẽ **thay thế** phần "Persona cốt lõi" hiện tại trong `brand-voice/SKILL.md` và nhét vào Writer/Reply prompt thay vì 4 ví dụ tao tự bịa.

## Trạng thái hiện tại

`brand-voice/SKILL.md` hiện tại là **placeholder hợp lý** dựa trên brief ban đầu — dùng được để launch, nhưng chưa phải bản đã qua discovery thật. Khuyến nghị: chạy session này sau 2-3 tuần vận hành, khi mày đã thấy content nào work/không work, để trả lời sâu hơn thay vì đoán trước khi có data.

## Kích hoạt

Lệnh: `/tsb brand-discovery` — Claude (không phải Hermes, cần hội thoại 2 chiều thật) sẽ dẫn dắt qua 6 module, lưu tiến độ ra `brand-identity/session-state.json` để resume nếu ngắt giữa chừng (đúng tinh thần harness — không mất context khi gián đoạn).

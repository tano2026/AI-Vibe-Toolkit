# CORE META-SKILLS — Nhóm "Đầu Não" bắt buộc tham chiếu
> Viết 22/08/2026. Phát hiện qua đợt phân loại 590 skill nhưng CHƯA
> từng được ghi vào tài liệu chính thức — chỉ nằm trong lịch sử chat.
> File này vá lỗ hổng đó: đây là danh sách CHUẨN, mọi agent (kể cả
> agent sinh ra từ agentic-factory) nên kiểm tra nhóm này trước khi
> tự viết mới, vì đây là skill về CÁCH AGENT VẬN HÀNH — cắt ngang mọi
> domain nghiệp vụ, không thuộc riêng agent nào trong 8 Pro Agent.

## Vì sao nhóm này khác 8 Pro Agent

8 Pro Agent trả lời "làm việc GÌ" (research/content/sales...). Nhóm này trả lời "agent vận hành NHƯ THẾ NÀO" — áp được cho cả 8 cái cùng lúc, không thuộc quyền sở hữu của 1 agent riêng.

## Danh sách đầy đủ (verify còn tồn tại 22/08/2026, sau đợt xoá ecc/)

### Harness — thiết kế khung điều khiển agent ổn định

| Skill | Vai trò |
|---|---|
| harness-engineering | Thiết kế harness khi agent chạy không ổn định — description tự nhắc thẳng "Hermes + OpenClaw production" |
| agent-harness-construction | Dựng harness mới từ đầu cho agent mới |
| autonomous-agent-harness | Cơ chế tự sửa lỗi, tiếp tục việc khi gặp sự cố, không cần người can thiệp |
| eval-harness | Bộ đo lường chất lượng câu trả lời/hành vi agent |

### Loop — vòng lặp agent hiệu quả, không luẩn quẩn tốn token

| Skill | Vai trò |
|---|---|
| agentic-loop-optimizer | Đã là skill Nobitano dùng thật (xác nhận từ danh sách skill cá nhân) — tối ưu số bước + chi phí token |
| autonomous-loops | Kiến trúc vòng lặp tự trị chạy ngầm, có điểm dừng an toàn |
| continuous-agent-loop | Mẫu hình loop kiểm tra định kỳ, không gây nghẽn |
| agent-self-improvement-loops | 5 nhóm vòng lặp giúp agent tự cải thiện, không lặp lại lỗi cũ |
| verification-loop | Vòng lặp tự kiểm tra độc lập TRƯỚC KHI nộp sản phẩm |
| benchmark-optimization-loop | Đo lường + cải thiện benchmark liên tục |

### Tối ưu hiệu suất/chi phí

| Skill | Vai trò |
|---|---|
| prompt-optimizer | Tinh chỉnh prompt cho model |
| parallel-execution-optimizer | Tối ưu chạy song song các nhánh việc độc lập |
| connections-optimizer | Tối ưu kết nối/API calls |

### Chất lượng đầu ra — không riêng domain nào

| Skill | Vai trò |
|---|---|
| superpowers + superpowers-skill | Biến Claude Code thành senior dev, quy trình 7 bước Brainstorm-Design-TDD-Verify (github.com/obra/superpowers, 150k sao) — 2 file gần trùng nội dung, nên gộp còn 1 khi có dịp dọn |
| humanizer | Xoá dấu hiệu AI viết, ghép cặp dùng cùng anti-ai-tells đã có trong Content Pro |

## Cách dùng — gắn vào quy trình, không chỉ liệt kê

```
Agentic Factory v2, Bước 1 (Grounding) — BỔ SUNG kiểm tra:
  Agent mới có cần harness ổn định (chạy 24/7, nhiều bước) không?
    -> tham khảo harness-engineering/autonomous-agent-harness
  Agent mới có vòng lặp dài, tốn token không?
    -> tham khảo agentic-loop-optimizer/verification-loop
  Agent mới có output text/content không?
    -> BẮT BUỘC qua humanizer + anti-ai-tells trước khi giao

Không phải agent nào cũng cần cả nhóm — chỉ tham khảo đúng skill khớp
nhu cầu thật, không nhét thừa.
```

## Việc CHƯA làm — nói thẳng

- Chưa gắn tham chiếu vào README của 8 Pro Agent hiện có (chỉ mới gắn vào quy trình Agentic Factory cho agent TƯƠNG LAI)
- 2 file superpowers/superpowers-skill chưa gộp — vẫn trùng lặp nhẹ, để dành đợt audit skill-lifecycle-management tiếp theo
- Chưa test thật skill nào trong nhóm này với 1 Pro Agent cụ thể

## Link
- Phát hiện qua: đợt phân loại 590 skill, Nobitano chỉ ra thiếu sót (21/08/2026)
- Dùng cùng: skill-lifecycle-management (audit định kỳ), agentic-factory v2 (Bước 1)

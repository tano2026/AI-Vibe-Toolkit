# Pydantic AI — GitHub Repo

## TL;DR
Framework Python xây agent có kiểm tra kiểu dữ liệu chặt (type-safe) — output của Claude PHẢI khớp đúng cấu trúc đã định nghĩa, sai thì tự động yêu cầu Claude làm lại kèm lỗi cụ thể, không để dữ liệu sai lọt xuống bước sau. Đứng trong nhóm 4 framework agent dẫn đầu thật sự (báo cáo phân tích 44 framework, 2/2026) — không phải 1 trong hàng trăm tool ít người biết.

## Repo này dùng để làm gì
Bọc quanh BẤT KỲ model nào (Claude/GPT/Gemini/Groq...) — định nghĩa output mong muốn bằng 1 class Pydantic (model dữ liệu Python chuẩn), framework tự validate câu trả lời model trả về đúng khớp class đó, sai thì tự retry kèm phản hồi lỗi cho model sửa, hết số lần retry thì raise lỗi thay vì âm thầm cho qua dữ liệu hỏng.

## ⚠️ Điểm quan trọng nhất — có thể thay thế 1 phần vai trò đã gán cho Jev

So sánh thẳng:

| | Jev (TypeSafe) | Pydantic AI |
|---|---|---|
| Vai trò | Model RIÊNG, cực nhanh/rẻ, chuyên quyết định có cấu trúc | FRAMEWORK bọc quanh model ĐÃ CÓ (kể cả Claude) |
| Trạng thái | Early access/waitlist, **chưa dùng được** | **Ổn định từ 9/2025, V2 từ 6/2026 — dùng NGAY** |
| Validate output | Có (đặc thù Choice/Score/Noul) | Có (bất kỳ cấu trúc Pydantic nào, tổng quát hơn) |
| Tốc độ/chi phí | Rất nhanh/rẻ (model riêng nhỏ) | Bằng đúng tốc độ/giá của model nền (Claude) |

**Kết luận thật:** với các skill đã thiết kế quanh "chờ Jev" (`production-signal-feedback-loop`, phần phân loại trong `churn-risk-escalation-discipline`) — Pydantic AI giải quyết được PHẦN VALIDATE CẤU TRÚC ngay bây giờ, dùng thẳng Claude, không cần đợi Jev. Jev vẫn có giá trị riêng (rẻ/nhanh hơn nhiều so với gọi Claude) nhưng không còn là ĐƯỜNG DUY NHẤT để có output đáng tin cậy.

## Setup từng bước
```bash
pip install pydantic-ai
```
```python
from pydantic_ai import Agent
from pydantic import BaseModel

class ChurnRiskResult(BaseModel):
    loai: str  # "ROI_BO_THAT" hoặc "PHAN_NAN_NHO"
    confidence: float
    ly_do: str

agent = Agent('anthropic:claude-sonnet-4-6', output_type=ChurnRiskResult)
result = agent.run_sync("Phân loại tin nhắn: 'định huỷ luôn không mua nữa'")
# result.output LUÔN đúng cấu trúc ChurnRiskResult, không bao giờ sai field
```

## Ví dụ thực tế
Thay vì chờ Jev để làm `production-signal-feedback-loop`'s 4 câu hỏi phân loại (Noul/Choice/Score) — viết thẳng 1 Pydantic model cho 4 trường đó, dùng Pydantic AI gọi Claude, có validate/retry ngay — chạy được hôm nay, không đợi waitlist.

## Lưu ý / Lỗi thường gặp
- Nhầm Pydantic AI với Jev là 2 thứ thay thế hoàn toàn nhau — Jev RẺ/NHANH hơn đáng kể (model nhỏ chuyên dụng), Pydantic AI chỉ nhanh/rẻ bằng đúng model nền đang gọi (Claude vẫn tốn như bình thường)
- Có hệ sinh thái phụ `pydantic-deepagents`/`pydantic-ai-harness` — bản dựng sẵn 1 "Claude Code tự host" trên nền Pydantic AI, đáng biết nhưng KHÁC phạm vi (đó là cả 1 Vessel thay thế, không phải chỉ validate output)

## Đánh giá cá nhân
- Điểm mạnh: trưởng thành thật (Tier 1 trong phân tích ngành), hỗ trợ Claude trực tiếp, giải quyết đúng vấn đề "output không đáng tin" mà không cần chờ Jev; có sẵn skill cài cho Claude Code
- Điểm yếu: không thay được lợi thế tốc độ/chi phí cực rẻ của Jev khi đã có access — đây là bổ sung, không phải thay thế hoàn toàn
- Có nên dùng: 9/10 — dùng NGAY cho mọi chỗ đang "chờ Jev" trong kho, chuyển sang Jev sau nếu cần rẻ/nhanh hơn nữa khi hết waitlist

## Link
- Docs: https://ai.pydantic.dev/
- So sánh chính thức với Claude Agent SDK: pydantic.dev/docs/ai/comparisons/vs-claude-agent-sdk
- Dùng cùng: repos/typesafe-jev.md (bổ sung, không thay thế), agents/infra-ops-agent/skills/production-signal-feedback-loop

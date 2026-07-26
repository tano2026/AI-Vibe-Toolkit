# Supermemory — GitHub Repo

## TL;DR
Engine bộ nhớ dài hạn cho AI agent, chạy được hoàn toàn local, **có plugin chính thức cho OpenClaw** (`supermemoryai/openclaw-supermemory`) và Claude Code — khớp thẳng vào stack đang dùng. Hermes (agent-core Python) dùng qua MCP server chung, không có plugin riêng. 28.6K stars, MIT license. Trên benchmark LongMemEval: nhớ đúng 95% (Recall@15) mà chỉ tốn ~720 token context (giảm 99.4% so với nhồi toàn bộ lịch sử).

## Repo này dùng để làm gì
Giải quyết đúng vấn đề: agent quên hết mọi thứ khi mở session mới. Supermemory tự động:
- **Auto-capture** — ghi lại hội thoại/thao tác quan trọng để dùng cho session sau
- **Team memory** — kiến thức project chia sẻ giữa các thành viên, tách riêng với memory cá nhân
- **Context injection** — đầu mỗi session, tự nhồi "User Profile" đã học được vào context, không cần hỏi lại CEO những gì đã biết
- **Explicit skills** — chủ động yêu cầu "nhớ cái này" / "tìm lại lúc trước mình quyết gì"

Có sẵn **Supermemory Filesystem (SMFS)** — thiết kế lại filesystem riêng cho agent, giảm 3 lần token trên Claude (24M vs 72M token) khi benchmark trên bộ câu hỏi thật.

## Setup từng bước
1. Chạy local hoàn toàn (không cần gửi data ra ngoài):
```bash
npx supermemory local
```
Lấy API key in ra màn hình lúc khởi động lần đầu.
2. Cài plugin cho Claude Code:
```bash
/plugin marketplace add supermemoryai/claude-supermemory
/plugin install supermemory
```
3. Set env:
```bash
SUPERMEMORY_CC_API_KEY=sm_...
```
4. **Riêng cho OpenClaw** — có plugin chính thức open source: `supermemoryai/openclaw-supermemory`. **Hermes** không có plugin riêng — dùng qua MCP server chung (`https://mcp.supermemory.ai/mcp`), vẫn dùng được nhưng không "khớp sẵn" như OpenClaw. Đáng chú ý hơn memory engine khác đã có trong kho (RIO Bot dùng SQLite riêng, ổn cho research history, nhưng supermemory hợp hơn cho memory CHUNG toàn hệ agent) — lưu ý: "Hermes agent" nhắc tới trong 1 số tài liệu supermemory (`NousResearch/hermes-agent`) là 1 model LLM tên trùng, KHÔNG liên quan Hermes của Tano Agency — đừng nhầm.
5. Cấu hình mức capture qua `.claude/.supermemory-claude/config.json` theo project — chỉnh `signalKeywords` (vd thêm "quyết định", "bug", "fix" để bắt đúng khoảnh khắc quan trọng).

## Ví dụ thực tế
OpenClaw đang điều phối nhiều task cho các domain khác nhau (ABTRIP, Tano Cafe, GMSP) — thay vì mỗi session mới phải nhắc lại toàn bộ context ("nhớ là brand ABTRIP dùng Deep Navy + Hanoi Gold"), supermemory tự inject Team Memory đã học từ các session trước, Hermes/OpenClaw nhớ được quyết định cũ (vd "đã chốt dùng Airtable thay Mission Control cho coordination layer") mà không cần CEO gõ lại.

## Lưu ý / Lỗi thường gặp
- Cần Node.js 18+ trên PATH — memory hooks chạy qua Node script.
- Auto-capture mặc định lưu MỌI hội thoại quan trọng — cân nhắc kỹ `signalKeywords`/`includeTools` để tránh lưu data nhạy cảm (lương nhân sự, thông tin khách hàng) vào memory chung không kiểm soát.
- Bản cloud (không chạy local) gửi data qua `api.supermemory.ai` — với data nhạy cảm nên ưu tiên chạy `npx supermemory local`.
- Khác RIO Bot's `memory.py` (SQLite, chỉ lưu research history/evidence cache) — supermemory là lớp memory CHUNG cho mọi agent, nên rõ ràng phạm vi: RIO Bot giữ nguyên SQLite riêng cho research, supermemory phủ toàn hệ thống Hermes/OpenClaw cho context chung.

## Đánh giá cá nhân
- Điểm mạnh: có plugin chính thức cho OpenClaw + Claude Code (Hermes dùng qua MCP chung, không có plugin riêng — vẫn dùng được, chỉ không tiện bằng); benchmark hiệu quả token thật sự ấn tượng; chạy local hoàn toàn được, không bắt buộc gửi data ra ngoài.
- Điểm yếu: cần cấu hình cẩn thận để tránh auto-capture data nhạy cảm; thêm 1 tầng hạ tầng nữa cần maintain trên VPS.
- Có nên dùng không: 8.5/10 — đáng đưa vào **bộ skill bắt buộc cho mọi project agent mới**, giải quyết đúng vấn đề "agent quên hết" đã gặp nhiều lần trong quá trình vận hành 9-role company.

## Link
- Repo chính: https://github.com/supermemoryai/supermemory
- Plugin Claude Code: https://github.com/supermemoryai/claude-supermemory
- Docs: https://supermemory.ai/docs/integrations/claude-code

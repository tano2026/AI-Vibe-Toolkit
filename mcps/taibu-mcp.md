# Taibu MCP (太卜) — MCP Server

## TL;DR
MCP server tổng hợp 15 công cụ luận giải: Bát Tự, Tử Vi, Lục Hào, Mai Hoa, Kỳ Môn, Đại Lục Nhâm, Tarot, lịch vạn niên... gắn vào Claude là dùng được ngay, không cần build gì. 241⭐.

## Tool này dùng để làm gì
Đây là bộ MCP cho mọi hệ thống luận giải Á Đông phổ biến gói chung 1 server: `bazi` (bát tự), `ziwei` (tử vi đẩu số), `ziwei_horoscope` (vận hạn tử vi theo đại hạn/lưu niên), `ziwei_flying_star` (tứ hóa phi tinh), `liuyao` (lục hào), `meihua` (mai hoa dịch số), `tarot`, `almanac` (lịch vạn niên), `astrology` (chiêm tinh phương Tây), `qimen` (kỳ môn độn giáp), `taiyi` (thái ất), `daliuren`/`xiaoliuren` (đại/tiểu lục nhâm). Gắn vào Claude xong, chỉ cần gõ câu hỏi bằng tiếng tự nhiên kiểu "tôi sinh 15h ngày 15/5/1990, xem giúp bát tự" là Claude tự gọi đúng tool, không cần biết cú pháp gì.

## Setup từng bước
1. Thêm vào file config MCP (Claude Desktop/Code):
```json
{
  "mcpServers": {
    "taibu": {
      "command": "npx",
      "args": ["-y", "taibu-mcp"]
    }
  }
}
```
2. Restart Claude
3. Gõ thẳng câu hỏi tự nhiên, ví dụ: "Tôi sinh ngày 15/5/1990 lúc 15h, hãy bát tự cho tôi" hoặc "Hôm nay coi giúp tôi quẻ mai hoa xem hợp tác này có thành không"
4. Muốn dùng core engine trực tiếp trong code Node.js (không qua MCP): `npm install taibu-core`
5. Muốn tự host cả web app đầy đủ (không chỉ MCP): `docker compose up -d --build` (chạy cả Web port 3000 + MCP port 3001)

## Ví dụ thực tế
Gõ: "Tôi sinh âm lịch ngày 8/4/1990, lập tử vi cho tôi"
→ Claude tự gọi tool `ziwei`, trả về 12 cung + chính/phụ tinh + mệnh chủ/thân chủ.

Gõ tiếp: "Vận hạn 2026 của tôi thế nào?"
→ Claude gọi `ziwei_horoscope`, trả vận hạn theo đại hạn/lưu niên năm 2026.

Dùng cho content: feed kết quả structured data này vào prompt khác để Claude viết bài "Tử vi 2026 của 12 con giáp" theo giọng văn riêng của kênh, tránh để Claude tự bịa số liệu lá số (dễ sai vì LLM tính tay hay lệch).

## Lưu ý / Lỗi thường gặp
- License chia 2 phần khác nhau, đọc kỹ trước khi dùng thương mại: package `core`, `mcp`, `mcp-server` (chính là phần npx mày cài) dùng **MIT** — tự do thương mại, không ràng buộc gì. Nhưng phần Web/server/deploy còn lại của repo dùng **AGPL-3.0-only** — vẫn cho thương mại, nhưng nếu mày sửa code phần này rồi host làm dịch vụ mạng công khai, bắt buộc phải mở nguồn lại phần đã sửa.
- Vì MCP chỉ gọi qua package MIT (`taibu-mcp`), dùng qua npx như hướng dẫn trên là an toàn 100% không vướng AGPL.
- Nhiều tool (kỳ môn, đại lục nhâm...) cần khai báo rõ timezone — nếu không khai báo dễ ra sai múi giờ, lệch giờ sinh thật.
- Đây là MCP còn khá mới (push gần nhất tháng 4/2026, ~2 tháng trước thời điểm viết bài) — nên test kỹ trước khi gắn vào pipeline tự động.

## Đánh giá cá nhân
- Điểm mạnh: 1 MCP mà gom đủ gần hết hệ thống luận giải Á Đông phổ biến, setup 1 dòng JSON, không cần biết cú pháp gì cả vì Claude tự hiểu ngôn ngữ tự nhiên.
- Điểm yếu: license phải đọc kỹ (đã giải thích ở trên), độ chính xác thuật toán chưa được bên thứ 3 nào audit/verify công khai như cách iztro được nhiều dự án khác dùng lại.
- Có nên dùng: 7/10 — tiện nhất nếu chỉ cần MCP gọi nhanh, không cần tự build app riêng.

## Link
- Repo: https://github.com/hhszzzz/taibu
- MCP npm: https://www.npmjs.com/package/taibu-mcp
- Core npm: https://www.npmjs.com/package/taibu-core
- Demo online: https://www.mingai.fun

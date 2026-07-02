# Script Video 141 — Opik

## Thông tin
- Tool/Repo/Skill liên quan: [repos/opik.md](../repos/opik.md)
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

## Hook (3 giây đầu)
AI agent trả lời sai mà mày không biết nó sai ở bước nào. Tool này chỉ đích danh bước lỗi.

## Script voiceover (ElevenLabs-ready)
Agent tự động chạy nhiều bước, tự gọi model, tự gọi tool. Khi kết quả sai, mày không biết lỗi nằm ở đâu.

Opik ghi lại toàn bộ hành trình đó. Mỗi lần agent gọi model, mỗi lần gọi tool, đều được lưu lại từng bước.

Không chỉ xem, nó còn tự động chấm điểm câu trả lời bằng AI khác, phát hiện agent đang bịa thông tin hay không.

Chỉ cần thêm một dòng decorator vào code Python, không cần sửa gì thêm.

Mười hai nghìn năm trăm sao GitHub trong chưa đầy một năm, tốc độ phát triển nhanh nhất trong nhóm công cụ giám sát AI.

## Ghi chú quay (OBS)
- Cảnh 1: Terminal show agent trả kết quả sai, chữ đỏ "??? sai ở đâu"
- Cảnh 2: Demo dashboard Opik với trace từng bước, highlight bước lỗi
- Cảnh 3: Code demo thêm @opik.track vào 1 hàm Python

## Caption/Sub note (CapCut)
Highlight: "12.5K stars", "1 dòng code", "chấm điểm tự động". Zoom vào dashboard lúc chỉ ra bước lỗi.

## Thumbnail idea (Canva)
Sơ đồ luồng (flowchart) với 1 bước được khoanh đỏ, chữ to "TÌM ĐÚNG BƯỚC LỖI".

## CTA cuối video
Save video này nếu mày đang build agent tự động — sẽ cần lúc debug.

# OpenWork (ModelStudio) — GitHub Repo

## TL;DR
Desktop app local-first cho hệ sinh thái ModelStudio của Alibaba Cloud (Bailian) — GUI đi kèm cho ModelStudio CLI, chạy trên nền Qwen Code. Repo nhỏ nhất và mới nhất trong 3 project cùng tên "Openwork" (12 sao, 3 fork) — chưa có track-record đáng kể, gắn chặt vào hạ tầng Alibaba Cloud.

## Repo này dùng để làm gì
Cho phép làm việc với agent AI ngay trên desktop: quản lý nhiều session song song, kết nối project/filesystem local, xem trước file/kết quả thực thi, tất cả trong môi trường có kiểm soát quyền (permission mode). Về bản chất là bản GUI đi kèm ModelStudio CLI — CLI dùng cho terminal/automation, OpenWork dùng làm giao diện tương tác hàng ngày.

## Setup từng bước
1. Cần tài khoản Alibaba Cloud + API key từ ModelStudio (Bailian console) — bắt buộc, không dùng được với OpenAI/Anthropic key trực tiếp theo tài liệu chính thức.
2. Clone repo: `git clone https://github.com/modelstudioai/openwork`
3. Cài dependency qua `bun` (repo dùng `bun.lock`), build bằng TypeScript/Electron.
4. Có thể dùng song song với ModelStudio CLI (`github.com/modelstudioai/cli`) — CLI cho phần automation/terminal, OpenWork cho phần tương tác trực quan.
5. Xem hướng dẫn đầy đủ tại `modelstudioai.github.io/guide/` trước khi setup lần đầu.

## Ví dụ thực tế
Dùng để chẩn đoán lỗi build: gõ "Giúp tao tìm lý do test project này fail, sửa lỗi, và tóm tắt thay đổi" — OpenWork tự đọc cấu trúc project, chạy lệnh tái hiện lỗi, phân tích log, sửa file (sau khi xin phép), chạy lại test để verify, rồi tóm tắt lại toàn bộ thay đổi — không cần nhảy qua lại giữa terminal/editor/browser thủ công.

## Lưu ý / Lỗi thường gặp
- **Gắn chặt vào Alibaba Cloud ModelStudio (Bailian)** — không dùng được với OpenRoute/OmniRoute hay OpenAI/Anthropic key trực tiếp theo thiết kế gốc, phải qua Alibaba Cloud console lấy key riêng. Với stack hiện tại của Tano (OmniRoute route qua DeepSeek/Gemini/Claude), tool này không cắm thẳng vào được.
- Repo mới, cộng đồng nhỏ (chỉ 12 sao) — rủi ro bảo trì/tài liệu chưa ổn định, khác hẳn độ trưởng thành của 2 project "Openwork" còn lại.
- Kế thừa kiến trúc từ Craft Agents OSS và Qwen Code — nếu team không quen hệ sinh thái Qwen thì đường cong học khá dốc so với việc dùng thẳng Claude Code/Cursor.

## Đánh giá cá nhân
- **Điểm mạnh:** Ý tưởng tách "CLI cho automation, GUI cho tương tác hàng ngày" là mô hình tổ chức hợp lý — giống đúng cách Tano đang tách Hermes (script Python chạy nền) khỏi nhu cầu xem trực quan khi cần debug.
- **Điểm yếu:** Ràng buộc cứng vào hạ tầng Alibaba Cloud — không tận dụng được OmniRoute (231 provider, ~1.6B token/tháng free tier) đang là lợi thế chi phí lớn nhất của Tano. Cộng đồng còn quá nhỏ để tin tưởng lâu dài.
- **Có nên dùng không:** 3/10 cho Tano cụ thể — không hợp vì khoá cứng vào Alibaba Cloud, mất lợi thế OmniRoute đang có. Có thể đáng chú ý nếu sau này Tano mở rộng dùng model Qwen trực tiếp, nhưng hiện tại chưa có nhu cầu đó.

## Link
- Repo: https://github.com/modelstudioai/openwork
- Docs/Demo: https://modelstudioai.github.io/guide/

---

## 🤖 Agent Integration

### Hermes (Python)
Không tích hợp — phụ thuộc Alibaba Cloud API key, không khớp kiến trúc OmniRoute hiện tại (route cheap/reasoning/balanced/creative qua DeepSeek/Gemini/Claude). Bỏ qua trừ khi có nhu cầu dùng Qwen trực tiếp trong tương lai.

### OpenClaw
Không áp dụng — không có lợi ích rõ ràng so với việc OpenClaw đã có Node.js orchestrator + browser access riêng.

### Antigravity
Không deploy trên VPS — là desktop Electron app, cần GUI, không hợp môi trường Ubuntu 22.04 headless của Tencent Cloud VPS.

> ⚠️ Chỉ cân nhắc lại tool này nếu Tano có kế hoạch dùng model Qwen trực tiếp
> qua Alibaba Cloud — hiện tại OmniRoute đã phủ đủ provider cần thiết với chi
> phí thấp hơn, không có lý do rõ ràng để thêm dependency Alibaba Cloud.

# agent-desktop (vercel-labs) — GitHub Repo

## TL;DR
CLI Rust, giấy phép Apache-2.0, cho AI agent điều khiển app desktop thật (macOS, Windows, Linux) bằng cách đọc cây accessibility của hệ điều hành thay vì chụp màn hình. Agent nhận JSON kèm mã tham chiếu cho từng nút, rồi click, gõ, cuộn theo mã đó. Đây là "computer use" cho app không có API. Nó KHÔNG phải công cụ điều phối nhiều agent hay hộp thư giao việc. Mới ra: bản 1.0.0 ngày 27/10/2026, 1.0.2 ngày 30/10/2026.

## Repo này dùng để làm gì
Vấn đề nó giải: có việc chỉ làm được bằng giao diện (app chỉ có UI, không có CLI hay API), mà agent dùng ảnh chụp màn hình thì chậm, tốn token và hay click trượt. agent-desktop cho agent đọc cấu trúc giao diện dạng JSON rồi thao tác chính xác theo mã tham chiếu.

Vòng lặp chuẩn: snapshot → thao tác theo mã → snapshot lại. Mã gắn với từng snapshot, mã cũ trả lỗi `STALE_REF`. README liệt kê 60 tên lệnh (56 chạy được), chia nhóm: quan sát, thao tác trên mã, bàn phím và chuột, ứng dụng và cửa sổ, thông báo, clipboard, chờ, phiên, hệ thống. Ảnh chụp là tuỳ chọn.

Không có plugin hay MCP riêng cho Claude Code. Agent nào chạy được shell thì gọi được CLI. Cách nạp hướng dẫn cho agent: cài skill từ skills.sh, hoặc thêm vào `AGENTS.md` một đoạn bảo agent chạy `agent-desktop skills get desktop`.

## Setup từng bước
1. Cần Node 18+ (binary dựng sẵn nằm sau gói npm). Cài: `npm install -g agent-desktop`
2. macOS 13+: cấp quyền Accessibility cho app khởi chạy agent. Muốn chụp màn hình thì cấp thêm Screen Recording.
3. Windows 10 bản 1809 trở lên (hoặc Server 2019+): binary chưa ký số nên SmartScreen hoặc antivirus có thể chặn. Không hỗ trợ Session 0, secure desktop, session của user khác. App chạy quyền admin sẽ không nhận input (UIPI).
4. Linux: mục tiêu đã đo là Ubuntu 24.04+ với GNOME 46. Phải với tới accessibility bus của phiên đồ hoạ. Chromium và Qt cần cờ khởi chạy riêng. Wayland chặn chuột và điều khiển cửa sổ native.
5. Nạp hướng dẫn cho agent: `agent-desktop skills get desktop` (chạy sau khi cài để xem lệnh và cú pháp của đúng bản đang dùng).
6. Homebrew và Scoop còn đang chờ duyệt, nên đừng dựa vào hai cách đó.

## Ví dụ thực tế
**Minh hoạ, chưa chạy thật.** Tình huống: có một phần mềm kế toán trên Windows chỉ có giao diện, cần xuất báo cáo cuối ngày.
- Input: agent được bảo "mở phần mềm, vào mục báo cáo, xuất bản ngày hôm nay ra thư mục chung".
- Cách chạy: agent chụp snapshot cửa sổ, tìm nút theo mã, bấm, snapshot lại sau mỗi bước, và dừng khi gặp `STALE_REF`.
- Kiểm kết quả: mỗi thao tác trả về trạng thái giao nhận (vd `delivered_verified` hay `delivered_unverified`). Cái này chỉ cho biết UI đã nhận thao tác, KHÔNG chứng minh việc thật đã xong. Phải tự kiểm file báo cáo có nằm ở thư mục chung không.

## Lưu ý / Lỗi thường gặp
- **Quá mới:** 1.0.2 mới ra ngày 30/10/2026, chưa thấy benchmark độc lập nào. Coi là thử nghiệm.
- **Chưa kiểm trên máy mình.** Mọi chi tiết trong entry này lấy từ tài liệu và bài phân tích, chưa chạy thử.
- **Rủi ro riêng tư:** snapshot, clipboard và ảnh chụp có thể chứa nội dung riêng tư trên màn hình, rồi đi vào model và log. Có helper JEV tuỳ chọn gửi mô tả màn hình sang nhà cung cấp model.
- **Không có hàng rào chống tiêm lệnh qua chữ trên màn hình** và không có sandbox cho thao tác desktop (docs không nói tới). Chữ trong email hay trang web đang mở có thể bị agent đọc như lệnh. Chạy trong môi trường cách ly, ưu tiên headless, và thêm bước duyệt cho việc phá huỷ.
- **Lỗ hổng ghi thật:** có báo cáo `set-value` đổi nội dung trong ô nhập nhưng không ghi xuống file trên đĩa. Luôn kiểm file.
- App canvas nặng hay giống game có accessibility kém thì chạy tệ.
- Không dùng cho: điều phối nhiều agent, hộp thư giao việc, chấm kết quả. Chế độ `--multi-agent` chỉ cho mỗi agent một con trỏ riêng và xếp lượt input, không có phân việc.

## Đánh giá cá nhân
- Điểm mạnh: giải đúng bài "app chỉ có UI", tiết kiệm token hơn chụp màn hình, chạy được cả ba hệ điều hành, giấy phép thoáng, hoạt động theo kiểu CLI nên agent nào cũng gọi được.
- Điểm yếu: quá mới, Windows còn bị chặn bởi binary chưa ký số, Linux nhiều chỗ thiếu, không có lớp an toàn cho prompt injection, và không cung cấp bằng chứng việc xong thật.
- Có nên dùng không: 6/10 hiện tại. Thử trên máy phụ cho một app cụ thể không có cách nào khác. Chưa đáng đưa vào luồng chính của Hermes/OpenClaw/Antigravity, và không giải được bài Boss giao việc cho worker.

## Link
- Repo: https://github.com/vercel-labs/agent-desktop
- Skill: https://www.skills.sh/vercel-labs/agent-desktop/agent-desktop
- Bài phân tích: https://flaviocopes.com/agent-desktop/
- Bài giới thiệu: https://explainx.ai/blog/vercel-agent-desktop-accessibility-tree-computer-use-cli-2026

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# agent-desktop là CLI, không có REST API. Hermes chỉ gọi được qua subprocess,
# nên KHÔNG khớp ràng buộc "chỉ urllib" nếu phải cô lập hoàn toàn.
# Còn cần Node + binary agent-desktop trên máy chạy GUI. VPS không có màn hình thường không dùng được.
import subprocess

def agent_desktop(*args, timeout=60):
    r = subprocess.run(["agent-desktop", *args], capture_output=True, text=True, timeout=timeout)
    return r.returncode, r.stdout, r.stderr

# Xem lệnh đúng của bản đang cài (không đoán cú pháp):
code, out, err = agent_desktop("skills", "get", "desktop")
```
> ⚠️ Chỉ chạy được trên máy có phiên đồ hoạ. VPS headless thường không có accessibility bus để dùng.

### OpenClaw
```bash
# Nạp hướng dẫn cho agent chạy shell: thêm vào AGENTS.md một đoạn bảo agent
# chạy `agent-desktop skills get desktop` trước khi thao tác app.
agent-desktop skills get desktop
```
> ⚠️ Việc phá huỷ (xoá, gửi, chi tiền) phải qua duyệt tay. Đừng để OpenClaw tự bấm trên app đang mở dữ liệu nhạy cảm.

### Antigravity
```bash
npm install -g agent-desktop
agent-desktop skills get desktop
```
> ⚠️ Windows: binary chưa ký số, SmartScreen hoặc antivirus có thể chặn lần đầu. Chưa kiểm trên máy thật.

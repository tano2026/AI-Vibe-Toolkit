# LocalMiniDrama — GitHub Repo

## TL;DR
Công cụ tạo "đoản kịch"/phim ngắn nhiều tập bằng AI, chạy 100% local trên máy Windows — từ cốt truyện tới video hoàn chỉnh trong 1 phần mềm, không dữ liệu nào rời khỏi máy. 660 sao, MIT license, có sẵn cả bản .exe tải về chạy luôn lẫn source code, và **có sẵn OpenClaw skill** đóng gói trong repo.

## Repo này dùng để làm gì
Giải quyết đúng bài toán "phim ngắn nhiều tập" (mini-drama/đoản kịch) đang là trend content lớn — nhập cốt truyện + văn phong mong muốn, AI tự sinh kịch bản nhiều tập, tự tách nhân vật/bối cảnh/đạo cụ ra thành ảnh tham chiếu (giữ nhất quán ngoại hình xuyên suốt các cảnh), tự chia phân cảnh (storyboard) kèm thông số quay phim (cỡ cảnh, góc máy, ánh sáng), rồi tự gọi API sinh ảnh/video cho từng cảnh, cuối cùng ghép lại thành 1 tập phim hoàn chỉnh. Có 2 chế độ làm việc: xem danh sách (edit chi tiết từng cảnh) hoặc "Canvas" — màn hình vô hạn dạng node, kéo thả xem toàn bộ pipeline phân cảnh, chọn nhóm cảnh rồi chạy lại (re-run) cả cụm cùng lúc.

## Setup từng bước
1. Cách nhanh nhất — tải bản .exe dựng sẵn (có kèm project mẫu để xem cách dùng):
```
Vào https://github.com/xuanyustudio/LocalMiniDrama/releases
Tải "本地短剧助手 x.x.x.exe" (bản đầy đủ, có project mẫu) hoặc bản "-Lite" (nhẹ hơn)
Chạy file .exe, vào mục "Cấu hình AI" điền API Key
```
2. Từ source code (cần Node.js ≥ 18):
```bash
git clone https://github.com/xuanyustudio/LocalMiniDrama.git
cd LocalMiniDrama

# Backend (cổng 5679)
cd backend-node && npm install
cp configs/config.example.yaml configs/config.yaml   # điền API Key vào đây
npm run migrate && npm start

# Frontend (cổng 3013, mở terminal mới)
cd frontweb && npm install && npm run dev
```
3. Mở `http://localhost:3013`, hoặc double-click `run_dev.bat` để chạy 1 lệnh cả 2.
4. Cấu hình AI provider — hỗ trợ Aliyun DashScope (Thông Nghĩa), Volcengine (Đậu Bao/Seedance 2.0), Kling AI, Google Gemini (Imagen/Veo), Vidu, hoặc Ollama local cho phần text — chọn theo API key sẵn có.

## Ví dụ thực tế
Với GMSP (podcast Tử Vi + tâm lý học + kinh tế) — thay vì chỉ làm dạng nói chuyện 2 host, có thể thử dựng 1 tập "đoản kịch" minh họa 1 case study tử vi/tâm lý dưới dạng kịch ngắn có nhân vật, bối cảnh, thoại — dùng LocalMiniDrama nhập cốt truyện case đó, để nó tự tách nhân vật + phân cảnh + sinh video, ra 1 định dạng khác biệt hẳn so với video nói chuyện thường thấy trong mảng content tử vi/tarot.

## Lưu ý / Lỗi thường gặp
- **Giao diện tiếng Trung** — labels trong app (menu, tên trường nhập liệu) đều tiếng Trung, cần quen giao diện hoặc dùng ảnh chụp màn hình dịch tay ban đầu, không có bản Việt hóa sẵn.
- **Platform badge ghi rõ chỉ Windows** — hợp với máy Windows local đang có sẵn của Nobitano, nhưng không chạy trên VPS Ubuntu (content-factory hiện tại) trừ khi chạy từ source trên Linux (chưa xác nhận có tương thích không, README chỉ đảm bảo Windows).
- Phụ thuộc hoàn toàn vào AI provider trả phí bên ngoài để sinh ảnh/video (Seedance, Kling, Gemini...) — bản thân tool không tự sinh gì, chỉ là lớp điều phối gọi API, cần ngân sách cho phần này.
- README ghi rõ mô hình càng mới thì chất lượng càng tốt — nghĩa là chưa chắc dùng model rẻ/free ra chất lượng ổn định như demo trên README.

## Đánh giá cá nhân
- Điểm mạnh: quy trình đầy đủ nhất trong nhóm "story-to-video" đã research trong kho (8 bước, từ cốt truyện tới video hoàn chỉnh), giữ nhất quán nhân vật xuyên cảnh (vấn đề khó nhất của AI video), có sẵn OpenClaw skill đóng gói, chế độ Canvas trực quan hiếm thấy ở tool nguồn mở cùng loại.
- Điểm yếu: giao diện tiếng Trung là rào cản, chỉ chính thức hỗ trợ Windows, phụ thuộc hoàn toàn AI provider trả phí ngoài để sinh media thật.
- Có nên dùng: 7/10 — rất đáng thử cho hướng nội dung "đoản kịch" khác biệt (đặc biệt hợp GMSP), nhưng cần thời gian làm quen giao diện tiếng Trung trước khi thấy hiệu quả thật.

## Link
- Repo: https://github.com/xuanyustudio/LocalMiniDrama
- Releases (.exe): https://github.com/xuanyustudio/LocalMiniDrama/releases
- Docs bản tiếng Anh: https://github.com/xuanyustudio/LocalMiniDrama/blob/main/docs/en.md
- Docs cấu hình AI: https://github.com/xuanyustudio/LocalMiniDrama/blob/main/docs/configuration.md
- OpenClaw skill có sẵn trong repo: https://github.com/xuanyustudio/LocalMiniDrama/tree/main/openclaw-skill

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Backend chạy Express trên cổng 5679 — Hermes có thể gọi thẳng qua REST API
# nội bộ (xem backend-node/routes/ trong repo để biết endpoint chính xác),
# thay vì phải điều khiển UI tay.
import urllib.request, json

def create_drama_project(title, synopsis, style):
    url = "http://localhost:5679/api/films"
    payload = json.dumps({"title": title, "synopsis": synopsis, "style": style}).encode()
    req = urllib.request.Request(url, data=payload,
                                  headers={"Content-Type": "application/json"}, method="POST")
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
# Repo có sẵn skill đóng gói riêng cho OpenClaw — cài thẳng, không cần tự viết wiring
git clone https://github.com/xuanyustudio/LocalMiniDrama.git
cp -r LocalMiniDrama/openclaw-skill /path/to/openclaw/skills/localminidrama
```

### Antigravity
```powershell
# Chạy trên máy Windows local (4 cores, ~15.7GB RAM đang có) — KHÔNG deploy lên
# VPS Tencent Cloud Ubuntu vì repo chỉ đảm bảo hỗ trợ Windows chính thức.
git clone https://github.com/xuanyustudio/LocalMiniDrama.git
cd LocalMiniDrama/backend-node; npm install
cd ../frontweb; npm install
# Chạy run_dev.bat để khởi động cả backend+frontend cùng lúc
```
> ⚠️ Giao diện tiếng Trung — cần thời gian làm quen trước khi giao Hermes tự động hoá toàn
> bộ quy trình qua API thay vì thao tác tay qua UI.

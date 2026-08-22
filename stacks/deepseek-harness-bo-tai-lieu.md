# DeepSeek Harness — Bộ tài liệu học & tra cứu

## TL;DR
Không phải review 1 tool — đây là combo 6 nguồn để đi từ "chưa biết gì" tới "tự viết được plugin riêng" cho DeepSeek Harness (dsh). Tổng hợp theo lộ trình 3 bước: chạy thử Web UI → cài plugin mẫu từ sàn danh bạ → đọc tài liệu Cordis rồi tự viết plugin. Bản thân tool DeepSeek Harness đã có review riêng ở kho, xem `/repos/deepseek-harness.md` (entry #257) — file này là lớp tài liệu bổ sung để học sâu và tra cứu, không lặp lại nội dung review.

## Các tool trong stack

1. **Repo chính thức** (`github.com/deepseek-ai/deepseek-harness`) → nền tảng, source code, chạy nhanh bằng `npx @deepseek-ai/dsh web`
2. **Docs kiến trúc + Preview** (`deepseek.com/harness`, `docs/architecture.md`) → hiểu 3 tầng: Giao diện & Tương tác (Web UI/CLI) → Nhân Plugin & Event Bus ("Everything is a Plugin") → Model & Môi trường chạy (API DeepSeek, model cục bộ, sandbox)
3. **Động cơ Cordis + paper nền tảng** (`github.com/cordiverse/cordis`, paper *"A Programming Paradigm for Spatiotemporal Composability"*) → hiểu cơ chế lõi: động cơ thời-không ghép plugin theo ngữ cảnh/thời gian thực, nạp dịch vụ động không cần restart
4. **Cẩm nang thực chiến dsh-handbook** (`github.com/Electricitysheep/dsh-handbook`) → 15 chương, có bản PDF tiếng Trung + tiếng Anh, chia 4 module: cài đặt từng bước (macOS/Linux/Windows), phát triển plugin, tối ưu hiệu năng (quản lý ngữ cảnh, tiết kiệm token), benchmark so sánh giữa các chế độ/Agent
5. **Sàn plugin chính thức-adjacent** (`deepseekplugin.org`) → danh bạ lớn nhất hiện tại (3500+ trang chi tiết), phân loại Agent Presets / Dev Tools / UI Themes / Workflows / MCP Servers / Sandbox, cài trực tiếp qua `dsh plugin install <tên-plugin>`
6. **Danh bạ cộng đồng awesome-deepseek-harness** (`github.com/0xsline/awesome-deepseek-harness`) → gom MCP connectors (nối DB, GitHub, Slack), UI/Web wrappers, và các bài phân tích kỹ thuật chuyên sâu

## Workflow ghép nối

```
Bước 1: Chạy thử Web UI (npx @deepseek-ai/dsh web)
   → trải nghiệm giao diện, không cần hiểu kiến trúc trước
Bước 2: Đọc docs kiến trúc + preview
   → nắm 3 tầng, hiểu vì sao "mọi thứ là plugin"
Bước 3: Cài plugin mẫu từ deepseekplugin.org hoặc awesome-deepseek-harness
   → dsh plugin install <tên-plugin>, xem plugin thật hoạt động ra sao
Bước 4: Đọc Cordis paper (nếu cần hiểu sâu cơ chế lõi)
   → chỉ cần khi định viết plugin phức tạp, không bắt buộc cho user thường
Bước 5: Dùng dsh-handbook làm cẩm nang song song
   → tra cứu khi cài lỗi, tối ưu token, hoặc so benchmark trước khi chọn chế độ
Bước 6: Tự viết plugin riêng
   → theo Module 02 của handbook + docs Cordis
```

## Ví dụ thực tế
Muốn tích hợp kho AI-Vibe-Toolkit (`tano2026/AI-Vibe-Toolkit`) thành 1 plugin cho dsh — để agent nào chạy trên dsh cũng fetch được kho trực tiếp thay vì qua OpenClaw:
1. Chạy `npx @deepseek-ai/dsh web` để test môi trường trước
2. Vào deepseekplugin.org, tìm mục "MCP Servers" xem có plugin GitHub-fetch nào làm mẫu tương tự chưa (đỡ viết lại từ đầu)
3. Đọc Module 02 (Phát triển Plugin) trong dsh-handbook để biết cấu trúc 1 plugin dsh chuẩn
4. Đọc `docs/architecture.md` phần Tầng 2 (Nhân Plugin & Event Bus) để biết cách đăng ký plugin vào Cordis
5. Nếu vướng cơ chế nạp/tháo plugin không cần restart (dynamic service loading) → tra thẳng Cordis paper phần "Nạp dịch vụ động"

## Lưu ý / Lỗi thường gặp
- **Không phải nguồn nào cũng chính thức** — `deepseekplugin.org` và `awesome-deepseek-harness` đều là cộng đồng/bên thứ 3, không phải DeepSeek AI vận hành. Cùng lúc tồn tại nhiều "awesome list" cạnh tranh nhau (0xsline, bruc3van/awesome-dsh-plugin, vvlife, YYTbit...) — dễ lạc, nên chốt 1 nguồn chính (0xsline có vẻ đầy đủ nhất tính tới giờ) rồi tham khảo thêm nếu thiếu
- **"DeepSeek Harness" là trademark đã đăng ký** — theo changelog chính thức của repo, nếu build sản phẩm ăn theo tên này cần xem quy phạm sử dụng thương hiệu trước
- **dsh vẫn ở giai đoạn rc (developer preview)** — breaking changes liên tục, các plugin mẫu trong handbook/awesome list có thể lỗi thời rất nhanh so với version mới
- **Plugin cộng đồng chưa được kiểm định chính thức** — cùng rủi ro đã ghi trong review tool gốc (#257), đặc biệt các plugin loại "skin/desktop pet" tưởng vô hại vẫn chạy code ngoài, cân nhắc trước khi cài vào máy có dữ liệu nhạy cảm
- Cordis paper là tài liệu học thuật, khá nặng nếu chỉ cần dùng dsh ở mức cơ bản — bỏ qua bước này nếu mục tiêu chỉ là dùng chứ không viết plugin

## Đánh giá cá nhân
- Điểm mạnh: lộ trình 3 bước rất rõ ràng cho người mới, dsh-handbook đặc biệt có giá trị vì có phần benchmark thực đo (không chỉ lý thuyết), sàn plugin deepseekplugin.org giúp không phải tự đào GitHub topic thủ công
- Điểm yếu: hệ sinh thái quá phân mảnh trong thời gian ngắn (nhiều awesome list trùng lặp, nhiều sàn plugin cạnh tranh: deepseekplugin.org, dshplugin.dev, dshpluginstore.com...) — tốn thời gian xác định nguồn nào đáng tin; một số tài liệu (đặc biệt awesome list) update theo ngày nên dễ lệch nếu không check lại thường xuyên
- Có nên dùng không: 7/10 — hữu ích để onboard nhanh, nhưng vì dsh còn rc nên coi đây là tài liệu "học và thử nghiệm", chưa phải nguồn tham chiếu ổn định lâu dài

## Link
- Repo chính thức: https://github.com/deepseek-ai/deepseek-harness
- Docs kiến trúc: https://deepseek.com/harness
- Cordis: https://github.com/cordiverse/cordis
- Handbook: https://github.com/Electricitysheep/dsh-handbook
- Sàn plugin: https://deepseekplugin.org
- Awesome list: https://github.com/0xsline/awesome-deepseek-harness
- Review tool gốc trong kho: `/repos/deepseek-harness.md` (entry #257)
- Nguồn tổng hợp gốc: Kỹ sư AI Yao Jingang (@yaojingang) trên X, qua @tuanisme

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Fetch README/docs raw từ các repo trong stack để agent tra cứu nhanh
# không cần mở browser -- dùng đúng chuẩn urllib.request, không pip install
import urllib.request

SOURCES = {
    "handbook": "https://raw.githubusercontent.com/Electricitysheep/dsh-handbook/main/README.md",
    "awesome": "https://raw.githubusercontent.com/0xsline/awesome-deepseek-harness/main/README.md",
    "architecture": "https://raw.githubusercontent.com/deepseek-ai/deepseek-harness/master/docs/architecture.md",
}

def fetch_doc(name):
    req = urllib.request.Request(SOURCES[name], headers={"User-Agent": "hermes-agent"})
    return urllib.request.urlopen(req).read().decode()
```
> ⚠️ README các repo cộng đồng update theo ngày (đặc biệt awesome-deepseek-harness) — nếu Hermes cache lại, nhớ set TTL ngắn (vài giờ) để tránh trả thông tin lỗi thời.

### OpenClaw
```bash
# Không có API trực tiếp cho deepseekplugin.org -- OpenClaw browser tool
# có thể duyệt trực tiếp để tìm plugin theo category khi cần gợi ý cho Nobitano
```

### Antigravity
```bash
# Nếu cần local mirror handbook để tra cứu offline trên VPS (đỡ phụ thuộc raw.githubusercontent.com)
git clone https://github.com/Electricitysheep/dsh-handbook.git /opt/docs/dsh-handbook
```

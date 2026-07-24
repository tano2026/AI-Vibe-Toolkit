# AIWriteX — GitHub Repo

## TL;DR
Nền tảng content-factory tự động đa nền tảng (chủ yếu Trung Quốc: WeChat gongzhonghao, Tiểu Hồng Thư, Baijiahao, Toutiao, Weibo) xây trên CrewAI multi-agent + AIForge — từ bắt trend, viết bài, tự chèn ảnh AI, tới xuất bản tự động. Điểm đặc biệt nhất: có "engine chống phát hiện AI" (去AI味) để bài viết qua được máy chấm AI-detection (Trung Quốc gọi là "Chu Tước"/Zhuque). 1.6k+ sao, Apache 2.0.

## Repo này dùng để làm gì
Đây là 1 content factory hoàn chỉnh chứ không phải 1 tool đơn lẻ: bắt trend nóng toàn mạng → chọn đề tài viral → gom bài tham khảo → viết bằng multi-agent (CrewAI) → tự chèn ảnh AI đúng phong cách → lên khuôn đẹp (23 kiểu layout, 32 template ảnh) → tự đăng lên nhiều nền tảng cùng lúc.

Có mấy điểm đáng chú ý ngoài phần "viết bài tự động" thông thường:
- **"Chuyên gia theo ngành" (专家赛道)**: không chỉ áp template chung, mà cấu hình cả bộ "đường lối viết chuyên nghiệp" riêng cho từng ngành (sức khoẻ, công nghệ, tin tức, giải trí, tâm lý, sự nghiệp...) — đưa vào cả cách định vị đề tài, chân dung độc giả, giới hạn nội dung, nhịp cấu trúc, phong cách biểu đạt.
- **Engine "khử vị AI" / chống AI-detection**: không chỉ đổi từ đồng nghĩa, mà rút "DNA dùng từ" từ bài mẫu rồi ép vào bài mới, phá cấu trúc liệt kê chỉnh tề của AI, chèn ngẫu nhiên cảm xúc chủ quan/câu hỏi tu từ để bài đọc "có người" hơn.
- **Điều khiển qua điện thoại**: điều khiển qua QQ/DingTalk/Feishu/Discord/Telegram bot — kiểu OpenClaw nhưng tập trung cho content, hỗ trợ cả lệnh cố định lẫn ngôn ngữ tự nhiên.
- **Viết tiểu thuyết dài kỳ**: có hệ thống bộ nhớ 3 lớp (ngắn hạn-trung hạn-toàn cục) để AI không quên thiết lập/nhân vật khi viết truyện dài nhiều chương.

## Setup từng bước
1. **Chế độ dev (khuyến nghị cho tích hợp agent)**:
   ```bash
   git clone https://github.com/iniwap/AIWriteX.git
   pip install uv
   uv venv
   uv pip install -r requirements.txt
   ```
2. Điền `config.yaml` và `aiforge.toml` — cần AppID/AppSecret WeChat gongzhonghao (nếu dùng nền tảng WeChat) và API key của LLM provider (OpenRouter/OpenAI/DeepSeek...).
3. Chạy có UI (khuyến nghị, quản lý được bài/template/ảnh):
   ```bash
   python .\main.py
   ```
   Hoặc chạy không UI (không quản lý được bài/template/ảnh):
   ```bash
   python -m src.ai_write_x.crew_main
   ```
4. Nếu chỉ cần dùng thử nhanh không setup dev: có bản build sẵn tải trực tiếp từ trang chủ, mở lên điền config là chạy.

## Ví dụ thực tế
Với Wonder Mart (e-commerce), phần đáng lấy nhất không phải nền tảng đăng bài (chủ yếu là nền tảng Trung Quốc, không match kênh TikTok/YouTube hiện tại) mà là 2 thứ: (1) kiến trúc "chuyên gia theo ngành" — có thể học theo để build 1 bộ "content playbook" riêng cho ngành hàng không (ABTRIP/Trùm Sân Bay) thay vì dùng 1 prompt chung; (2) engine chống AI-detection — nếu content Wonder Mart/Tano bị nền tảng nào đó chấm điểm "AI-generated" và giảm reach, có thể tham khảo kỹ thuật "phá cấu trúc liệt kê + tiêm cảm xúc chủ quan" thay vì chỉ đổi từ đồng nghĩa như cách làm phổ biến.

## Lưu ý / Lỗi thường gặp
- Đa số nền tảng xuất bản (WeChat gongzhonghao, Tiểu Hồng Thư, Baijiahao, Toutiao,番茄小说) là nền tảng Trung Quốc — không dùng được trực tiếp cho kênh TikTok/YouTube hiện tại của Nobitano, cần đánh giá lại phần "auto-publish" có match use case hay không trước khi đầu tư setup.
- README/tài liệu 100% tiếng Trung, không có bản tiếng Anh — cần dịch khi research sâu hơn phần code.
- Chính tác giả cảnh báo: máy chấm AI-detection (như Chu Tước) liên tục tiến hoá, đối kháng "không phải chuyện một sớm một chiều" — hiệu quả né detection không ổn định 100%, tác giả khuyến nghị AI hỗ trợ chứ không phải AI viết trọn 100% rồi đăng thẳng.
- Bản chạy sẵn (không dev) cần AppID/AppSecret WeChat thật — không có tài khoản WeChat gongzhonghao thì chỉ dùng được phần viết bài + sinh ảnh, không test được auto-publish.

## Đánh giá cá nhân
- Điểm mạnh: kiến trúc multi-agent (CrewAI) rõ ràng cho pipeline content end-to-end; ý tưởng "chuyên gia theo ngành" và engine chống AI-detection là 2 thứ đáng học hỏi kỹ thuật dù không dùng nguyên bộ; điều khiển qua bot điện thoại giống pattern OpenClaw đã có sẵn trong hệ sinh thái.
- Điểm yếu: gắn chặt vào hệ sinh thái nền tảng Trung Quốc, không match trực tiếp kênh hiện tại (TikTok/YouTube); tài liệu toàn tiếng Trung tăng chi phí research; engine chống AI-detection theo lời tác giả cũng không ổn định lâu dài.
- Có nên dùng: 5/10 nếu tính dùng nguyên bộ (vì lệch nền tảng); 8/10 nếu chỉ lấy ý tưởng kiến trúc (chuyên gia theo ngành + chống AI-detection) để tự implement lại cho stack hiện có.

## Link
- Repo: https://github.com/iniwap/AIWriteX
- Website/bản thương mại ổn định: https://aiwritex.voidai.cc/

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Không có REST endpoint public — chạy qua CLI không UI để tích hợp vào pipeline
import subprocess

def run_aiwritex_headless(repo_path="/opt/AIWriteX"):
    result = subprocess.run(
        ["python", "-m", "src.ai_write_x.crew_main"],
        cwd=repo_path, capture_output=True, text=True
    )
    return result.stdout, result.returncode
    # Lưu ý: chế độ headless KHÔNG quản lý được bài/template/ảnh,
    # chỉ hợp để chạy 1 job viết + xuất bản đã cấu hình sẵn trong config.yaml
```

### OpenClaw
```bash
git clone https://github.com/iniwap/AIWriteX.git
cd AIWriteX && pip install uv && uv venv && uv pip install -r requirements.txt
# Điền config.yaml + aiforge.toml 1 lần, OpenClaw trigger job qua Hermes
```

### Antigravity
```bash
# Cài uv trên VPS nếu chưa có
pip install uv
```
> ⚠️ Chỉ triển khai nếu thực sự cần đăng nội dung lên nền tảng Trung Quốc (WeChat/Xiaohongshu/Baijiahao/Toutiao) — nếu không, chỉ nên lấy tham khảo kiến trúc, không cần cài đặt thật.

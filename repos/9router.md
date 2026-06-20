# 9router — GitHub Repo

## TL;DR
AI gateway miễn phí: kết nối Claude Code, Cursor, Cline, Copilot... với 40+ AI providers và 100+ models. Tự động fallback, tiết kiệm 20-40% token. 18K+ sao. Có README tiếng Việt.

## Repo này dùng để làm gì
Thay vì trả tiền cho từng AI service riêng lẻ, mày chạy 9router như một proxy ở giữa. Tất cả AI coding tools của mày đều kết nối vào 9router, và 9router tự lo việc:

- **Routing thông minh**: dùng model free/rẻ khi có thể, model xịn khi cần
- **Auto-fallback**: hết quota Claude → tự chuyển sang Gemini Free hoặc provider khác
- **RTK Token Saver**: nén output của tools (git diff, grep, ls...) trước khi gửi lên LLM → tiết kiệm 20-40% token
- **Track quota**: biết còn bao nhiêu quota để optimize usage

Kết nối được với: Claude Code, Cursor, Antigravity, Copilot, Codex, Gemini CLI, OpenCode, Cline, OpenClaw, và nhiều hơn nữa.

## Setup từng bước

```bash
# Cài qua npm
npm install -g 9router

# Hoặc chạy trực tiếp
npx 9router
```

Sau khi chạy, 9router tạo một local endpoint (mặc định `http://localhost:4000`). Mày point tất cả AI tools vào endpoint này.

**Ví dụ config Claude Code:**
```bash
# Set API base URL của Claude Code sang 9router
export ANTHROPIC_BASE_URL=http://localhost:4000
claude
```

**Config providers trong 9router:**
```json
{
  "providers": [
    { "name": "anthropic", "apiKey": "sk-ant-..." },
    { "name": "openai", "apiKey": "sk-..." },
    { "name": "gemini", "apiKey": "AIza..." }
  ],
  "fallback": true,
  "rtk": true
}
```

## Ví dụ thực tế
Mày đang dùng Claude Code, hết quota lúc 3h sáng đang fix bug gấp. Thay vì tắt máy chờ, 9router tự fallback sang Gemini 2.5 Flash miễn phí. Mày code tiếp không bị gián đoạn.

RTK saves: một session code có nhiều `git diff` và `grep` output → compress lại → tiết kiệm ~30% token, tức là quota dùng được lâu hơn ~30%.

## Lưu ý / Lỗi thường gặp
- Model free thường có rate limit thấp hơn, chậm hơn → không hoàn toàn thay thế được model trả phí
- Một số tính năng đặc thù của Claude (extended thinking, tool use phức tạp) có thể không hoạt động khi fallback sang provider khác
- Cần giữ 9router process chạy ngầm

## Đánh giá cá nhân
- Điểm mạnh: Setup nhanh, tiết kiệm thật sự, auto-fallback cực kỳ hữu ích, có README tiếng Việt (dev người Việt!)
- Điểm yếu: Thêm một layer phức tạp vào stack, debugging khó hơn khi có vấn đề, model free không bằng model trả phí
- Có nên dùng không: **9/10** — Gần như ai dùng Claude Code hay Cursor đều nên thử. Setup 5 phút, benefit ngay lập tức.

## Link
- Repo: https://github.com/decolua/9router
- npm: https://www.npmjs.com/package/9router
- Website: https://9router.com
- README tiếng Việt: https://github.com/decolua/9router/blob/main/i18n/README.vi.md

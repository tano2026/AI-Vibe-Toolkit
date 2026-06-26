# gstack — GitHub Repo

## TL;DR
Setup Claude Code CHÍNH XÁC của Garry Tan (CEO Y Combinator) — 23 tools đóng vai CEO, Designer, Eng Manager, QA, Doc Engineer. 115K stars — repo trending #1 toàn GitHub. Đây là bộ MCP + skill setup được chia sẻ nhiều nhất 2026.

## Repo này dùng để làm gì
Garry Tan public exact setup mà ông dùng để ship sản phẩm mà "không gõ một dòng code nào từ tháng 12". 23 tools được thiết kế như một đội ngũ ảo:
- **CEO agent:** Ưu tiên task, quyết định strategic
- **Designer agent:** UI/UX decisions, design system
- **Eng Manager:** Code review, architecture
- **Release Manager:** Deploy, versioning, changelog
- **Doc Engineer:** Tự viết documentation
- **QA:** Test, bug hunting

Mày clone về, bật lên — có ngay team ảo 6 người làm việc trong Claude Code.

## Setup từng bước
```bash
# 1. Clone gstack
git clone https://github.com/garrytan/gstack
cd gstack

# 2. Cài Claude Code (nếu chưa có)
npm install -g @anthropic-ai/claude-code

# 3. Copy config vào project của mày
cp gstack/.claude/settings.json your-project/.claude/
cp -r gstack/skills/ your-project/skills/

# 4. Mở Claude Code trong project
cd your-project
claude

# 5. Test với prompt đơn giản
# "Review code này theo góc độ Eng Manager"
# "Design một onboarding flow mới"
# "Viết release notes cho version này"
```

**Cấu trúc gstack:**
```
gstack/
├── .claude/
│   └── settings.json    ← MCP config + tool permissions
├── skills/
│   ├── ceo.md           ← CEO agent prompt
│   ├── designer.md      ← Designer agent
│   ├── eng-manager.md   ← Eng Manager agent
│   ├── release.md       ← Release Manager
│   ├── docs.md          ← Doc Engineer
│   └── qa.md            ← QA agent
└── README.md
```

## Ví dụ thực tế
**Scenario:** Mày vừa viết xong feature login mới

**Prompt:** "Review feature login này — CEO, Eng Manager, và QA mỗi người cho tao feedback"

**Output:**
- CEO: "Feature này giải quyết friction nào? Có cần A/B test không?"
- Eng Manager: "JWT token chưa handle refresh. Error state thiếu UX copy."
- QA: "Chưa test edge case: email có dấu +, password toàn special char, timeout 30s"

3 góc độ, 1 prompt.

## Lưu ý / Lỗi thường gặp
- Cần Claude Code CLI (không phải claude.ai web) — install qua npm
- 23 tools consume context window nhanh — với project nhỏ, bật 5-6 tool đủ dùng thay vì all 23
- Một số skill được tối ưu cho startup tech US — cần điều chỉnh context cho dự án VN
- 115K stars = nhiều fork/clone — dùng repo gốc của garrytan, không fork lạ

## Đánh giá cá nhân
- Điểm mạnh: Đây là setup THẬT của người đang dùng hàng ngày, không phải demo; 23 tools cover full product cycle; dễ customize
- Điểm yếu: Cần Claude Code (không free); context window bloat nếu bật hết; cần time để học cách "nói chuyện" với từng agent
- Có nên dùng không: **9/10** — Must-have cho ai dùng Claude Code. Clone về ngay, đây là shortcut tốt nhất để vibe code như senior team.

## Link
- Repo: https://github.com/garrytan/gstack
- Related: Andrej Karpathy quote về không gõ code từ tháng 12

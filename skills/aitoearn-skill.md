# AiToEarn — Skill Setup AI Tự Tạo Content + Kiếm Tiền

**Repo:** github.com/yikart/AiToEarn
**Dùng cho:** Tự động hóa content pipeline, monetize bằng AI

---

## Concept

```
AI Agent → tạo content → đăng social → kiếm tiền từ views/affiliate
```

Không phải get-rich-quick. Là tool automation content có thật.

## Setup

```bash
git clone https://github.com/yikart/AiToEarn
cd AiToEarn
npm install
cp .env.example .env

# Điền:
# OPENAI_API_KEY hoặc ANTHROPIC_API_KEY
# Platform tokens (YouTube, TikTok, X...)
npm start
```

## 4 Content Modes

```bash
# Mode 1: AI viết text content
aitoearn generate --type text --topic "AI tools 2026" --platform twitter

# Mode 2: AI tạo image + caption
aitoearn generate --type image --topic "tech tips" --platform instagram

# Mode 3: AI viết script + TTS
aitoearn generate --type video-script --topic "Python tips" --tts elevenlabs

# Mode 4: Scheduled publishing
aitoearn schedule --content ./drafts/ --interval 8h --platforms twitter,linkedin
```

## Kết Hợp Với AI Vibe Toolkit

```
content-creator.md (skill) → tạo nhiều format cùng lúc
→ AiToEarn → schedule + đăng tự động
→ Monitor → analytics
```

## Cảnh Báo

- Cần kiểm tra content trước khi auto-post
- Platform terms thay đổi thường xuyên
- Quality > Quantity — đừng spam

---
*skills/aitoearn-skill.md | AI Vibe Toolkit | tháng 6/2026*

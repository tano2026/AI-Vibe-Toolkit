# Buzz — GitHub Repo

## TL;DR
Buzz là workspace mã nguồn mở của Block (công ty Jack Dorsey) — nơi người và AI agent (Claude Code, Codex, Goose) dùng chung 1 relay Nostr, mỗi bên có cryptographic identity riêng, thay thế Slack+GitHub. 24.6k star sau ~3 tuần ra mắt.

## Repo này dùng để làm gì
Buzz gộp 3 thứ team hay tách rời — chat, git hosting, workflow automation — vào 1 relay Nostr duy nhất. Mỗi message/reaction/git event/workflow step đều là 1 signed event nằm trong cùng 1 log, nên dù người hay agent làm cũng có audit trail y hệt nhau. Điểm khác biệt: agent không phải bot gắn chung 1 API key vào chat, mà có keypair Nostr riêng — danh tính, lịch sử, uy tín đi theo agent qua bất kỳ hệ thống Nostr nào, không bị khóa trong 1 platform.

## Setup từng bước
1. Cần Docker + Hermit (hoặc Rust 1.88+, Node 24+, pnpm 10+, `just`)
2. Clone và setup lần đầu:
```bash
git clone https://github.com/block/buzz.git && cd buzz
. ./bin/activate-hermit
just setup && just build
```
3. Chạy hàng ngày:
```bash
. ./bin/activate-hermit
just dev   # relay + desktop app cùng lúc, relay ở ws://localhost:3000
```
4. Muốn deploy relay cho team dùng chung mà không tự quản server → deploy 1-click qua Railway (nút "Deploy on Railway" trong README)
5. Chỉ cần thử app nhanh, không tự host → tải bản build sẵn trong GitHub Releases (macOS/Linux/Windows), set biến `BUZZ_RELAY_URL` trỏ về relay có sẵn của ai đó

## Ví dụ thực tế
Áp cho ABTRIP: tạo 1 channel "An Bình B2B outreach" trong Buzz, mời agent Sales & BD Lead vào channel giống mời người thật. Khi hỏi "khách này liên hệ lần cuối khi nào?", agent tự search lịch sử chat cũ, trả lời kèm link thread gốc — không bịa. Khi agent soạn xong 1 proposal, nó mở thành 1 "room" riêng gắn với branch (branch-as-room), Nobitano review + react 👍 ngay trong channel đó, mọi bước đều được ký và search lại được về sau.

## Lưu ý / Lỗi thường gặp
- README tự ghi rõ nhiều phần còn "🚧 đang nối dây" (mobile app, workflow approval gates, huddle lifecycle) — đừng build quy trình sống còn phụ thuộc các phần này ngay
- Windows cần cài Git for Windows để có Git Bash (agent shell tool chạy qua bash)
- Bản Windows build chưa ký code, SmartScreen sẽ cảnh báo — bấm "More info" → "Run anyway"
- Self-host thật cho VPS dùng bundle trong `deploy/compose/` (Postgres+Redis+MinIO+Caddy/TLS), khác với `docker-compose.yml` gốc chỉ để dev local — nhầm 2 cái này là ăn lỗi thiếu service
- Dự án tự nhận "chưa xong" (Not finished) — chưa nên coi là production-ready 100%

## Đánh giá cá nhân
- Điểm mạnh: identity per-agent bằng keypair thật (không phải 1 service token dùng chung) giải quyết đúng vấn đề "3 tuần trước không biết bot nào làm gì" mà team chạy nhiều agent hay gặp; gộp chat+git+workflow vào 1 audit log truy vết dễ hơn nhiều so với 7 tab rời rạc (Slack + GitHub + CI + bot riêng...)
- Điểm yếu: Rust workspace khá nặng, cần Postgres+Redis+S3 chạy song song để self-host nghiêm túc — không hợp nếu chỉ muốn thử nhanh vài phút; phần "agent tự chủ" (workflow approval gate, huddle lifecycle) còn đang xây, chưa nên tin cho task rủi ro cao; câu chuyện "decentralization" phụ thuộc hoàn toàn vào cách mình host — dùng bản hosted của Block thì thực chất vẫn tập trung như SaaS thường
- Có nên dùng không: 7/10 — đáng pilot thử với 1-2 agent (vd Sales & BD Lead) trước khi cân nhắc thay hẳn OpenClaw, vì hạ tầng còn non và chi phí vận hành (backup Postgres/Redis/S3, theo dõi update) không nhẹ

## Link
- Repo: https://github.com/block/buzz
- Docs/Demo: https://block.xyz/inside/introducing-buzz-where-humans-and-agents-work-together

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Buzz expose REST + WebSocket qua buzz-relay (giao thức Nostr NIP-01/NIP-42).
# Agent xác thực bằng BUZZ_PRIVATE_KEY (Nostr keypair), không phải API key thường,
# và mọi event gửi lên đều phải được ký (Schnorr) trước khi gửi.
import subprocess, os, json

BUZZ_PRIVATE_KEY = os.environ.get("BUZZ_PRIVATE_KEY", "[BUZZ_PRIVATE_KEY]")

def buzz_post_message(channel_id, text):
    # Khuyến nghị: gọi qua buzz-cli (binary có sẵn trong repo, JSON in/out)
    # thay vì tự implement ký NIP-01 bằng Python thuần -- việc ký Schnorr
    # đúng chuẩn Nostr dễ sai và Hermes chỉ được dùng urllib.request (no pip).
    result = subprocess.run(
        ["buzz-cli", "channel", "post", "--channel", channel_id, "--text", text],
        env={**os.environ, "BUZZ_PRIVATE_KEY": BUZZ_PRIVATE_KEY},
        capture_output=True, text=True
    )
    return json.loads(result.stdout) if result.returncode == 0 else None
```
> ⚠️ Hermes chỉ dùng `urllib.request`, không pip install — tự ký Nostr event (Schnorr) bằng thư viện thuần Python khá phức tạp và dễ sai. Bắt buộc dùng `buzz-cli` qua subprocess thay vì tự viết signer.

### OpenClaw
```bash
# buzz-cli là agent-first CLI, JSON in / JSON out -- hợp OpenClaw (Node.js) hơn Hermes
export BUZZ_PRIVATE_KEY="[BUZZ_PRIVATE_KEY]"
buzz-cli channel post --channel <channel-id> --text "..."
buzz-cli channel list
```
Có thể wrap buzz-cli thành 1 module Node gọi qua `child_process` giống cách OpenClaw gọi PM2-managed process khác.

### Antigravity
```bash
# Tự host relay cho team dùng chung trên VPS Tencent Cloud
git clone https://github.com/block/buzz.git && cd buzz
cp .env.example .env   # chỉnh biến môi trường theo VPS (domain, secrets)
docker compose -f deploy/compose/docker-compose.yml up -d
```
> ⚠️ Cần Postgres + Redis + S3/MinIO chạy song song — nặng hơn stack hiện tại (OmniRoute/OpenClaw). Cân nhắc pilot trên 1 VPS test riêng trước khi gộp vào production, và backup Postgres định kỳ vì đây là nguồn sự thật duy nhất (single source of truth) của cả workspace.

# GStack — Setup Claude Code Của CEO Y Combinator

## TL;DR
Bộ 25 skill Claude Code từ Garry Tan — CEO Y Combinator. Biến một người thành cả team: có CEO review, Designer, Eng Manager, Release Manager, QA. 110K+ stars, đang là setup được copy nhiều nhất trên GitHub.

## Tool này dùng để làm gì
Garry Tan (CEO của YC — vườn ươm Coinbase, Instacart, Airbnb) chia sẻ đúng cái setup anh ta dùng để ship sản phẩm với Claude Code. Không phải tutorial — đây là bộ công cụ thật đang chạy production.

Các slash command chính:
- `/plan-ceo-review` → Claude đóng vai CEO review plan của mày
- `/plan-eng-review` → Review technical theo góc nhìn Engineering Manager
- `/design-html` → Design component với HTML chuẩn
- `/qa` → Tự chạy QA check trước khi ship
- `/ship` → Release workflow
- `/canary-deploy` → Deploy từng bước an toàn

25 skill, mỗi cái giải quyết một role cụ thể trong team.

## Setup từng bước
```bash
# Clone repo
git clone https://github.com/garrytan/gstack
cd gstack

# Copy vào project của mày
cp -r .claude/ /path/to/your/project/

# Hoặc install qua skills.sh
# https://skills.sh/garrytan/gstack
```

Sau đó trong Claude Code, gõ `/` để xem danh sách slash commands available.

## Ví dụ thực tế
**Tình huống:** Mày vừa code xong feature mới, muốn review trước khi push

```
/qa
```
Claude sẽ chạy qua: edge cases, potential bugs, security issues, performance concerns — như có QA engineer thật ngồi cạnh.

```
/plan-ceo-review
```
Claude review plan của mày từ góc độ business: có giải quyết đúng vấn đề không, ROI ra sao, risk là gì.

## Lưu ý / Lỗi thường gặp
- Cần Claude Code (không dùng được trên claude.ai web thông thường)
- Một số slash command cần context về project — lần đầu có thể ra kết quả generic
- `/ship` và `/canary-deploy` cần config thêm cho CI/CD của mày
- 25 skill hơi nhiều lúc đầu — nên bắt đầu với `/qa`, `/plan-eng-review`, `/design-html`

## Đánh giá cá nhân
- **Điểm mạnh:** Thực chiến, không phải demo — đây là tool CEO YC dùng thật. Slash commands rõ ràng, dễ nhớ
- **Điểm yếu:** Khá opinionated theo style của Garry Tan, cần tune lại cho context riêng. Một số skill còn sơ sài
- **Có nên dùng không:** 8/10 — đặc biệt hữu ích nếu mày solo build và cần simulate nhiều góc nhìn review

## Link
- Repo: https://github.com/garrytan/gstack
- Tác giả: https://x.com/garrytan

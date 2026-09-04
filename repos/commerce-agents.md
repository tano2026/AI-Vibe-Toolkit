# Commerce Agents (Anthropic) — GitHub Repo

## TL;DR
Bộ blueprint chính chủ của Anthropic để build 2 loại agent thương mại: agent bán hàng (shopping agent) nhúng vào app/web cho khách, và agent vận hành (merchant agent) cho team backoffice — kèm 4 ví dụ chạy được luôn (retail, travel, telecom, vé sự kiện).

## Repo này dùng để làm gì
Đây không phải 1 sản phẩm cắm là chạy, mà là bộ khung tham chiếu (reference implementation) Anthropic public ngày 2/9/2026 để dạy cách build "commerce agent" đúng bài — dùng chung 1 kiến trúc skill-based (không chia nhỏ ra nhiều sub-agent theo domain vì tốn token + mất context giữa các lần handoff).

2 agent chính:
- **Shopping agent**: search sản phẩm, so sánh, lên kế hoạch mua, bỏ giỏ hàng, trả lời câu hỏi đơn hàng/chính sách, nhớ thông tin khách (dị ứng, size...). Agent KHÔNG tự chốt đơn — nút "đặt hàng" luôn do người bấm, agent chỉ render giỏ hàng ra.
- **Merchant agent**: giải thích số liệu bán hàng, sửa listing, xử lý cảnh báo tồn kho, tăng/giảm giá, soạn campaign. Mọi thay đổi agent đề xuất đều ở dạng "staged change" — phải có người approve mới apply thật (giống maker-checker trong ngân hàng).

Cả 2 dùng chung 1 kiến trúc: 1 model + skill cho từng flow (không phải nhiều sub-agent), tool gọi thẳng vào hệ thống thật của mình (catalog, cart, inventory...), và tầng guardrail nằm ở CODE chứ không nằm ở prompt — vì sai sót ở commerce là mất tiền thật, không thể tin prompt 100%.

Có sẵn Claude Code plugin (`commerce-builder`) để scaffold agent riêng của mình dựa theo bộ khung này, hỏi về hệ thống của mình rồi generate code luôn.

## Setup từng bước

**Chạy thử 4 demo có sẵn:**
```bash
git clone https://github.com/anthropics/commerce-agents.git && cd commerce-agents
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env                  # điền ANTHROPIC_API_KEY vào đây
cd examples && npm ci && cd ..
python scripts/run_demo.py retail     # API cổng 8000 + storefront cổng 3000
```
Đổi `retail` thành `travel` / `telecom` / `entertainment` để xem 3 vertical còn lại. Thêm `--merchant` để chạy portal backoffice thay vì storefront khách hàng, `--all` để chạy cả hai.

**Tự build agent riêng (không dùng demo) qua Claude Code plugin:**
```bash
claude plugin marketplace add anthropics/commerce-agents
claude plugin install commerce-builder@claude-commerce-agents
claude
/scaffold-commerce-agent a shopping assistant for our store
```
Plugin sẽ hỏi về stack của mình (backend gì, catalog ở đâu...), trình bày plan rồi tự sinh code. Có thêm lệnh `/add-commerce-flow` (thêm flow mới) và `/review-commerce-agent` (audit agent đã build).

## Ví dụ thực tế
Thử vertical `retail` (brand giả định "ACME"): chạy `python scripts/run_demo.py retail`, mở storefront ở `localhost:3000`, gõ "tìm cho tao cái lều cắm trại 2 người dưới 250 đô" → shopping agent search, so sánh, render sản phẩm ra UI card (không phải text) rồi chờ mình bấm thêm vào giỏ. Ở portal `localhost:3100`, hỏi merchant agent "tuần này bán chậm nhất là sản phẩm nào?" → nó phân tích rồi đề xuất giảm giá dạng "staged change" chờ mình duyệt, không tự động áp giá.

Với Nobitano, đây là bộ khung tham chiếu cực khớp nếu sau này build lại agent bán hàng cho **Wonder Mart** hoặc agent quản lý booking cho **ABTRIP** (vertical `travel` trong repo gần như là bản demo sẵn cho đúng use case đặt vé/lịch trình).

## Lưu ý / Lỗi thường gặp
- Đây là **reference implementation, không maintain, không nhận PR** — tự chủ động fork về mà sửa, đừng chờ Anthropic vá lỗi.
- Toàn bộ data trong demo là giả định (brand "ACME"), không có phần checkout/charge tiền thật — nếu muốn dùng thật phải tự nối vào hệ thống catalog/cart/payment của mình qua "Backend methods" (xem `docs/backends.md`).
- Cần Python 3.11+ và Node 22 — máy cũ hơn sẽ lỗi khi cài.
- Không MCP nào ship sẵn — agent gọi thẳng vào backend interface của mình; nếu dùng MCP catalog/cart có sẵn thì gọi nó *bên trong* backend method, không gắn thẳng vào agent.
- Vì đây là bộ khung của doanh nghiệp lớn (nhiều team sở hữu nhiều skill khác nhau), áp trực tiếp cho quy mô 1 người + AI agent như TANO có thể hơi nặng — nên lấy tư duy kiến trúc (skill thay vì sub-agent, guardrail nằm ở code, staged-change cho hành động rủi ro) hơn là bê nguyên cả bộ.

## Đánh giá cá nhân
- Điểm mạnh: chính chủ Anthropic, kiến trúc rất rõ ràng và đã test qua nhiều enterprise thật (theo blog đi kèm), guardrail an toàn nghĩ rất kỹ (ID chỉ nhận từ server, cap giao dịch tính trên state sau khi ghi chứ không tính trên request, sanitize content bên thứ 3...). Đọc kỹ phần "Safety" là học được cách làm agent commerce an toàn ngay cả khi không dùng repo này.
- Điểm yếu: nặng cho use case nhỏ — được thiết kế cho doanh nghiệp có nhiều team, nhiều hệ thống backend thật. Muốn chạy được phải tự viết `StorefrontBackend`/`MerchantBackend` nối vào hệ thống thật, không có sẵn connector nào — công sức tích hợp không nhỏ. Không có mã Việt hoá, docs toàn tiếng Anh.
- Có nên dùng không: 8/10 — không phải để "cắm chạy" mà để **học kiến trúc chuẩn** khi build agent bán hàng/vận hành thương mại. Rất đáng đọc kỹ phần safety + capability map (skill theo flow) trước khi tự thiết kế agent riêng cho Wonder Mart/ABTRIP.

## Link
- Repo: https://github.com/anthropics/commerce-agents
- Docs: https://claude.com/blog/the-anatomy-of-effective-commerce-agents (bài kỹ thuật giải thích kiến trúc)
- Announcement: https://claude.com/blog/claude-for-commerce-agents

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Repo này không có REST API public để gọi thẳng — nó là code framework chạy local/self-host.
# Hermes không "gọi" repo này qua HTTP, mà đọc code mẫu (StorefrontBackend/MerchantBackend)
# làm tham chiếu khi Nobitano yêu cầu build agent bán hàng mới cho Wonder Mart.
# Nếu cần tự động clone + đọc cấu trúc repo để tham khảo:
import urllib.request

def fetch_readme():
    req = urllib.request.Request(
        "https://raw.githubusercontent.com/anthropics/commerce-agents/main/README.md")
    return urllib.request.urlopen(req).read().decode("utf-8")

print(fetch_readme()[:500])
```

### OpenClaw
```bash
# Dùng Claude Code plugin trực tiếp trên VPS nếu muốn scaffold agent commerce mới:
claude plugin marketplace add anthropics/commerce-agents
claude plugin install commerce-builder@claude-commerce-agents
# Sau đó trong session Claude Code trên VPS:
# /scaffold-commerce-agent agent ban ve/dat cho ABTRIP dua tren vertical travel
```

### Antigravity
```bash
# Deploy 1 trong 4 demo lên VPS để test trước khi build thật:
git clone https://github.com/anthropics/commerce-agents.git
cd commerce-agents
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # điền ANTHROPIC_API_KEY qua PM2 env hoặc .env trực tiếp
cd examples && npm ci && cd ..
pm2 start "python scripts/run_demo.py travel --all" --name commerce-agent-demo
```
> ⚠️ Repo yêu cầu Python 3.11+ và Node 22 — kiểm tra version trên VPS Tencent trước khi cài, tránh lỗi dependency. Demo mặc định KHÔNG có authentication và MCP server bind vào loopback — không expose port ra ngoài internet khi test trên VPS.

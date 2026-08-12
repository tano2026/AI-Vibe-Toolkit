# Domain Name Brainstormer — Sinh tên miền + check RDAP thật

## TL;DR
Sinh 15-30 tên miền khả dụng cho brand/sản phẩm mới theo brief (mục đích, tone, TLD ưu tiên), lọc bớt tên khó đánh vần/dễ nhầm, rồi check thật tình trạng đăng ký qua RDAP (registry data, không phải đoán) bằng script Python thuần — không cần API key.

## Skill này dùng để làm gì
Khi cần đặt tên cho brand/sub-brand/campaign mới (kiểu lúc trước đặt ABTRIP, Wonder Mart, Tano Cafe), thay vì brainstorm bừa rồi ra whois check tay từng cái, skill này:
1. Sinh tên theo nhiều nhóm: ghép trực tiếp, ghép rút gọn, tên tự bịa dễ đọc, tên theo hành động/kết quả, biến thể song ngữ
2. Tự loại tên khó đánh vần, dễ nghe nhầm, trùng nghĩa xấu, gần giống đối thủ
3. Chạy RDAP check thật (không bịa) — trả về 4 trạng thái rõ ràng: `registered` / `likely_available` / `unknown` / `invalid`
4. Luôn nhắc: `likely_available` vẫn phải xác nhận lại ở registrar trước khi mua, không convert thẳng thành "available"

## Setup từng bước
1. Không cần cài gì thêm — script chỉ dùng thư viện chuẩn Python (`urllib`/RDAP HTTPS request), không phụ thuộc package ngoài
2. Check domain cụ thể:
   ```bash
   python scripts/check_domains.py abtrip-fast.com abtrip-sim.dev
   ```
3. Check nhiều TLD cho 1 tên gốc:
   ```bash
   python scripts/check_domains.py tanocafe --tld com --tld vn --tld io
   ```
4. Xuất kết quả máy đọc được để lưu lại: `--json results.json`
5. Điều chỉnh timeout/số worker nếu check nhiều domain cùng lúc bị rate-limit: `--timeout 10 --workers 3`

## Ví dụ thực tế
**Case:** Nobitano cần đặt tên cho 1 kênh AI review mới (đã có trong danh sách content channels nhưng chưa có domain riêng) → brief: "kênh review AI tool cho SMB Việt Nam, tone thân thiện, ưu tiên .com/.vn":
```bash
python scripts/check_domains.py aitoolvn ainhanh reviewai-vn --tld com --tld vn --json check.json
```
→ Ra bảng: tên nào `likely_available`, tên nào đã `registered` — loại ngay những cái đã có người đăng ký, còn lại đem qua registrar (Mắt Bão/Nhân Hòa/Namecheap) xác nhận giá + mua thật.

## Lưu ý / Lỗi thường gặp
- `unknown` KHÔNG được hiểu là "available" — đây là lỗi network/rate-limit, phải retry hoặc check tay
- RDAP không trả về giá — giá premium domain phải xem tại registrar, không đoán
- Không tự động check trademark — chỉ check đăng ký domain, không phải check nhãn hiệu, cần search riêng nếu brand quan trọng

## Đánh giá cá nhân
- Điểm mạnh: script thật, không cần API key, không phụ thuộc package ngoài (đúng tinh thần "Hermes pattern: urllib.request thuần"), có phân biệt rõ 4 trạng thái thay vì đoán bừa
- Điểm yếu: chỉ check RDAP registration, không check giá/trademark/premium status — vẫn cần bước xác nhận tay cuối cùng; phần "sinh tên" vẫn là Claude tự brainstorm, không có logic đặc biệt gì ngoài checklist thông thường
- Có nên dùng không: 7/10 — nhẹ, không rủi ro, tiết kiệm thời gian check tay khi cần đặt tên brand/campaign mới, phù hợp integrate thẳng vào Hermes vì không cần pip ngoài

## Link
- Nguồn gốc skill: adapted từ bundle [Rylaispirit/rylai-codex-hermes-skills](https://github.com/Rylaispirit/rylai-codex-hermes-skills) (clean-room-original)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Dùng được trực tiếp trong Hermes vì chỉ cần urllib.request thuần (RDAP qua HTTPS)
import urllib.request, json

def check_domain_rdap(domain: str) -> str:
    tld = domain.split(".")[-1]
    rdap_servers = {"com": "https://rdap.verisign.com/com/v1/domain/",
                     "vn": "https://rdap.vnnic.vn/domain/",
                     "io": "https://rdap.nic.io/domain/"}
    server = rdap_servers.get(tld)
    if not server:
        return "unknown"
    try:
        req = urllib.request.Request(server + domain)
        urllib.request.urlopen(req, timeout=8)
        return "registered"
    except urllib.error.HTTPError as e:
        return "likely_available" if e.code == 404 else "unknown"
    except Exception:
        return "unknown"
```

### OpenClaw
```bash
# Chạy trực tiếp qua Telegram command tới OpenClaw, forward xuống Hermes xử lý
# /check-domain abtrip-fast.com abtrip-sim.dev
```

### Antigravity
> Không cần deploy — script chạy local trong Hermes sandbox, chỉ cần network access ra ngoài (đã whitelist theo cấu hình mạng hiện tại).

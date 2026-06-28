# Coolify — GitHub Repo

## TL;DR
Self-hosted PaaS thay thế Vercel, Heroku, Netlify — deploy app, database, service lên VPS riêng chỉ cần một click. 57.4K stars. Tao deploy mọi thứ lên VPS mà không cần biết DevOps phức tạp.

## Repo này dùng để làm gì
Vibe coder hay bí ở bước: "Code xong rồi, deploy lên đâu?" Coolify giải quyết:
- Connect GitHub repo → auto deploy khi push code (như Vercel)
- Deploy database: PostgreSQL, MySQL, MongoDB, Redis — một click
- Deploy bất kỳ Docker container nào
- SSL tự động (Let's Encrypt)
- Custom domain
- Environment variables management
- Deploy nhiều app trên cùng một VPS

Thay vì trả $20/tháng Heroku hay bị giới hạn Vercel free tier — mày trả $5/tháng VPS và deploy không giới hạn.

## Setup từng bước
```bash
# Cài Coolify trên VPS (Ubuntu 20.04+)
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash

# Truy cập: http://YOUR_VPS_IP:8000
# Tạo admin account → done

# Sau đó trong UI:
# 1. Add Server → điền SSH credentials VPS
# 2. New Project → connect GitHub repo
# 3. Set environment variables
# 4. Click Deploy → tự build và chạy
```

**Deploy Supabase self-host bằng Coolify:**
- New Service → chọn Supabase từ template → điền config → deploy
- Không cần hiểu Docker Compose phức tạp

## Ví dụ thực tế
**Stack ABTRIP trên một VPS $10/tháng:**
- Coolify quản lý: Open WebUI + Stirling PDF + TREK + Resona API + n8n
- Mỗi service có domain riêng, SSL tự động
- GitHub push → auto redeploy trong 2 phút
- Monitoring built-in: xem logs, metrics từ dashboard

Chi phí: $10/tháng VPS thay vì $50-100/tháng cho từng service riêng lẻ.

## Lưu ý / Lỗi thường gặp
- Cần VPS có ít nhất 2GB RAM — 4GB khuyến nghị nếu chạy nhiều service
- Firewall: mở port 8000 (Coolify UI), 80, 443 — block hết port khác
- Backup quan trọng: Coolify không tự backup database — setup cronjob riêng
- Một số service phức tạp (Supabase full) cần RAM nhiều hơn

## Đánh giá cá nhân
- Điểm mạnh: UI đơn giản hơn Kubernetes/Portainer; template service phong phú; auto SSL; connect GitHub dễ; community active
- Điểm yếu: Đôi khi unstable với version mới; support enterprise còn hạn chế; một số edge case phải fix tay
- Có nên dùng không: **8.5/10** — Game changer cho indie maker và small team. Deploy cả stack lên VPS rẻ, không cần DevOps engineer.

## Link
- Repo: https://github.com/coollabsio/coolify
- Docs: https://coolify.io/docs
- Website: https://coolify.io

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

COOLIFY_URL = "http://localhost:8000"  # hoặc domain Coolify
COOLIFY_TOKEN = "[COOLIFY_API_TOKEN]"  # Settings → API Tokens
HEADERS_C = {"Authorization": f"Bearer {COOLIFY_TOKEN}", "Content-Type": "application/json"}

def list_apps():
    req = urllib.request.Request(f"{COOLIFY_URL}/api/v1/applications", headers=HEADERS_C)
    return json.loads(urllib.request.urlopen(req).read())

def deploy_app(app_uuid):
    """Trigger redeploy một app"""
    req = urllib.request.Request(
        f"{COOLIFY_URL}/api/v1/applications/{app_uuid}/deploy",
        data=b"{}", headers=HEADERS_C, method="POST"
    )
    return json.loads(urllib.request.urlopen(req).read())

def get_app_logs(app_uuid):
    req = urllib.request.Request(
        f"{COOLIFY_URL}/api/v1/applications/{app_uuid}/logs", headers=HEADERS_C)
    return json.loads(urllib.request.urlopen(req).read())

# Hermes có thể trigger deploy tự động sau khi push code!
```

### OpenClaw
```bash
# Gọi API — không cần MCP
```

### Antigravity
```bash
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
# Mở: http://[VPS-IP]:8000 → setup → lấy API token
```
> ⚠️ Antigravity install Coolify lên VPS → Hermes có thể trigger deploy programmatically.

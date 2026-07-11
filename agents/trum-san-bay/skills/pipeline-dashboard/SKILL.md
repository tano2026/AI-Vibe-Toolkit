# Pipeline Dashboard — Xem Progress Trực Quan

## Mô tả
Mảnh cuối còn thiếu trong HARNESS.md — thay vì đọc `progress.json` bằng tay, mở dashboard trên browser xem trạng thái từng content_id đang ở bước nào, platform nào đã đăng, lỗi gì đang chờ xử lý.

## Kiến trúc
```
progress.json (state thật)
        ↓
dashboard_server.py (Python http.server, đọc file, serve JSON qua API nhỏ)
        ↓
dashboard.html (fetch API, render bảng, tự refresh mỗi 10s)
```

Không cần framework, không cần build step — mở file .html trực tiếp trên browser trỏ về VPS.

## Code — dashboard_server.py

```python
"""
Server nhẹ, không phụ thuộc ngoài stdlib — đọc progress.json + tokens.json,
serve qua API JSON để dashboard.html fetch.
Chạy: python3 dashboard_server.py (port 8899, đổi qua env DASHBOARD_PORT)
"""
import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

STATE_FILE = "/opt/trum-san-bay/state/progress.json"
TOKEN_FILE = "/opt/trum-san-bay/state/tokens.json"
PORT = int(os.environ.get("DASHBOARD_PORT", 8899))


class DashboardHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())

    def do_GET(self):
        if self.path == "/api/progress":
            state = {}
            if os.path.exists(STATE_FILE):
                with open(STATE_FILE) as f:
                    state = json.load(f)
            self._send_json(state)

        elif self.path == "/api/tokens":
            tokens = {}
            if os.path.exists(TOKEN_FILE):
                with open(TOKEN_FILE) as f:
                    raw = json.load(f)
                # Không lộ access_token thật ra dashboard — chỉ show trạng thái
                import time
                for platform, info in raw.items():
                    if "pending" in platform:
                        continue
                    remaining = info["expires_at"] - time.time()
                    tokens[platform] = {
                        "healthy": remaining > 300,
                        "expires_in_minutes": round(remaining / 60)
                    }
            self._send_json(tokens)

        elif self.path == "/" or self.path == "/dashboard.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open(os.path.join(os.path.dirname(__file__), "dashboard.html"), "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # tắt log mặc định, đỡ rác terminal


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), DashboardHandler)
    print(f"Dashboard chạy tại http://<vps-ip>:{PORT}")
    server.serve_forever()
```

## Code — dashboard.html

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Trùm Sân Bay — Pipeline Dashboard</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; font-family: -apple-system, sans-serif; }
  body { background: #0a1628; color: #fff; padding: 24px; }
  h1 { color: #FFD700; margin-bottom: 8px; font-size: 24px; }
  .subtitle { color: #8A96A3; margin-bottom: 24px; font-size: 14px; }
  .token-bar { display: flex; gap: 12px; margin-bottom: 24px; }
  .token-chip {
    padding: 8px 16px; border-radius: 20px; font-size: 13px; font-weight: 600;
  }
  .token-chip.healthy { background: #2ECC71; color: #0a1628; }
  .token-chip.warning { background: #E63946; color: #fff; }
  table { width: 100%; border-collapse: collapse; }
  th { text-align: left; padding: 12px; color: #8A96A3; font-size: 12px; text-transform: uppercase; border-bottom: 2px solid #1a3a5c; }
  td { padding: 12px; border-bottom: 1px solid #1a3a5c; font-size: 14px; }
  .status-badge {
    padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: 600; display: inline-block;
  }
  .status-success { background: #2ECC71; color: #0a1628; }
  .status-in_progress { background: #FFD700; color: #0a1628; }
  .status-failed, .status-partial { background: #E63946; color: #fff; }
  .platforms { display: flex; gap: 6px; }
  .platform-tag {
    font-size: 11px; padding: 2px 8px; border-radius: 4px; background: #1a3a5c;
  }
  .empty { text-align: center; padding: 60px; color: #8A96A3; }
</style>
</head>
<body>
  <h1>✈️ Trùm Sân Bay — Pipeline Dashboard</h1>
  <div class="subtitle" id="last-updated">Đang tải...</div>

  <div class="token-bar" id="token-bar"></div>

  <table>
    <thead>
      <tr>
        <th>Content ID</th>
        <th>Bước</th>
        <th>Trạng thái</th>
        <th>Platform đã đăng</th>
        <th>Lỗi</th>
        <th>Cập nhật lúc</th>
      </tr>
    </thead>
    <tbody id="table-body"></tbody>
  </table>

  <div class="empty" id="empty-state" style="display:none">Chưa có content nào trong pipeline</div>

<script>
async function loadData() {
  try {
    const [progressRes, tokensRes] = await Promise.all([
      fetch('/api/progress'),
      fetch('/api/tokens')
    ]);
    const progress = await progressRes.json();
    const tokens = await tokensRes.json();

    renderTokens(tokens);
    renderTable(progress);

    document.getElementById('last-updated').textContent =
      'Cập nhật lúc ' + new Date().toLocaleTimeString('vi-VN');
  } catch (e) {
    document.getElementById('last-updated').textContent = 'Lỗi kết nối server: ' + e.message;
  }
}

function renderTokens(tokens) {
  const bar = document.getElementById('token-bar');
  bar.innerHTML = '';
  for (const [platform, info] of Object.entries(tokens)) {
    const chip = document.createElement('div');
    chip.className = 'token-chip ' + (info.healthy ? 'healthy' : 'warning');
    chip.textContent = `${platform}: ${info.healthy ? 'OK' : 'CẦN REFRESH'} (${info.expires_in_minutes}p)`;
    bar.appendChild(chip);
  }
}

function renderTable(progress) {
  const tbody = document.getElementById('table-body');
  const emptyState = document.getElementById('empty-state');
  tbody.innerHTML = '';

  const entries = Object.entries(progress);
  if (entries.length === 0) {
    emptyState.style.display = 'block';
    return;
  }
  emptyState.style.display = 'none';

  entries.sort((a, b) => new Date(b[1].updated_at) - new Date(a[1].updated_at));

  for (const [contentId, data] of entries) {
    const posted = (data.extra && data.extra.posted_platforms) || [];
    const failed = (data.extra && data.extra.failed_platforms) || {};

    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${contentId}</td>
      <td>${data.step}</td>
      <td><span class="status-badge status-${data.status}">${data.status}</span></td>
      <td><div class="platforms">${posted.map(p => `<span class="platform-tag">${p}</span>`).join('')}</div></td>
      <td>${Object.keys(failed).length > 0 ? Object.entries(failed).map(([p, e]) => `${p}: ${e}`).join('; ') : '—'}</td>
      <td>${new Date(data.updated_at).toLocaleString('vi-VN')}</td>
    `;
    tbody.appendChild(row);
  }
}

loadData();
setInterval(loadData, 10000);  // auto-refresh mỗi 10s
</script>
</body>
</html>
```

## Setup

```bash
mkdir -p /opt/trum-san-bay/dashboard
# copy dashboard_server.py và dashboard.html vào đây

# Chạy nền qua pm2
pm2 start /opt/trum-san-bay/dashboard/dashboard_server.py \
  --name tsb-dashboard --interpreter python3
pm2 save
```

Mở `http://<vps-ip>:8899` trên browser — thấy bảng trạng thái tất cả content đang chạy, token nào cần refresh, lỗi gì đang chờ.

## Bảo mật

- Dashboard KHÔNG có auth — chỉ bind `0.0.0.0` nếu VPS có firewall chặn port 8899 từ ngoài, hoặc dùng SSH tunnel để xem an toàn:
```bash
ssh -L 8899:localhost:8899 user@vps-ip
# rồi mở http://localhost:8899 trên máy mày
```
- Access token thật KHÔNG BAO GIỜ trả về qua `/api/tokens` — chỉ trả `healthy: true/false` + số phút còn lại

# Supabase MCP — Cho Claude Code đọc và sửa database Supabase (chính chủ, hosted)

## TL;DR
MCP server chính chủ của Supabase, chạy hosted tại `https://mcp.supabase.com/mcp`. Cho Claude Code liệt kê bảng, chạy SQL, đọc log, xem cảnh báo bảo mật, sinh kiểu TypeScript, tìm docs, deploy Edge Function. Đăng nhập bằng OAuth qua trình duyệt, không cần token cá nhân. Repo `supabase/mcp` giấy phép Apache-2.0, khoảng 3 nghìn sao. Cực mạnh nhưng nguy hiểm nếu trỏ vào database thật: rủi ro chính là tiêm lệnh qua dữ liệu. **Chưa chạy thật** (cần đăng nhập OAuth vào tài khoản Supabase).

## MCP này dùng để làm gì
Vấn đề nó giải: Claude Code viết code cho app Supabase nhưng không nhìn thấy schema, log, cảnh báo thật. Có MCP, nó đọc được bảng thật rồi viết migration và query đúng cột.

Các nhóm công cụ (theo trang chính thức):
| Nhóm | Công cụ |
|---|---|
| Database | `list_tables`, `list_extensions`, `list_migrations`, `apply_migration`, `execute_sql` |
| Debugging | `query_logs`, `get_advisors` |
| Development | `get_project_url`, `get_publishable_keys`, `generate_typescript_types` |
| Edge Functions | liệt kê, đọc, deploy, `create_edge_function_secret` |
| Account | công cụ quản lý project và tổ chức (tắt khi gắn `project_ref`) |
| Docs | `search_docs` |
| Branching | tạo, liệt kê, xoá, merge, reset, rebase nhánh (thử nghiệm, cần gói trả phí) |
| Feedback | `submit_feedback`, `delete_feedback` (tắt khi `read_only`) |
| Storage | tắt mặc định |

## Setup từng bước
1. **Khuyến nghị bắt đầu an toàn**: gắn một project và chỉ đọc.
```bash
claude mcp add --scope project --transport http supabase "https://mcp.supabase.com/mcp?project_ref=<PROJECT_REF>&read_only=true"
```
Nhớ đặt URL trong dấu ngoặc kép vì có ký tự `&`. `project_ref` lấy ở Project Settings trên dashboard.

2. Xác thực: mở Claude Code, gõ `/mcp`, chọn `supabase` rồi chọn Authenticate. Trình duyệt mở ra, đăng nhập Supabase và chọn tổ chức có project. Docs chính thức nói không cần personal access token.
3. Muốn mở rộng thì thêm tham số, ví dụ `&features=database,docs` để chỉ bật vài nhóm. Các tham số kết hợp được: `project_ref`, `read_only`, `features`.
4. Dùng trong CI hoặc máy không có trình duyệt: tạo personal access token và gửi qua header `Authorization: Bearer`. Docs khuyên giới hạn token theo project và chỉ cấp quyền các công cụ đang bật.
5. Cú pháp `claude mcp add` tao đã kiểm bằng `claude mcp add --help` trên máy này (cờ `--transport http`, `--scope`, `--header`). URL và các tham số lấy từ trang chính thức `supabase.com/mcp`.
6. Phương án khác: Supabase CLI có MCP cục bộ ở `http://localhost:54321/mcp` với bộ công cụ rút gọn, và bản tự host cũng chỉ có tập con.

## Ví dụ thực tế
**Minh hoạ, chưa chạy thật.** Tình huống: app đặt vé có bảng `bookings`, mày muốn thêm cột trạng thái thanh toán.
- Input cho Claude Code: "Xem schema bảng bookings rồi viết migration thêm cột payment_status."
- Với `read_only=true`: Claude đọc schema bằng `list_tables`, viết file migration, nhưng KHÔNG chạy được `apply_migration`. Mày tự chạy ở môi trường dev.
- Với quyền ghi: Claude gọi `apply_migration` trực tiếp. Chỉ bật trên project dev hoặc nhánh (branch), không bao giờ trên database khách hàng thật.

## Lưu ý / Lỗi thường gặp
- **Tiêm lệnh qua dữ liệu là rủi ro chính.** Docs chính thức gọi nó là "primary attack vector unique to LLMs". Dòng chữ trong một ô dữ liệu (tên khách, ghi chú, nội dung ticket) có thể bị Claude đọc như lệnh rồi chạy SQL. Giữ bước duyệt thủ công từng lệnh khi làm việc tương tác.
- **Đừng trỏ vào database sản xuất** trừ khi việc cần bằng chứng từ dữ liệu thật. Khi đó dùng `read_only=true`, `project_ref` và giới hạn `features`.
- **Không tắt xác nhận** bằng `skip_elicitations` (tham số này bỏ bước hỏi trước `execute_sql`, `apply_migration`, `create_project`, `create_branch`).
- **Không đưa server cho khách hàng hay người dùng cuối** dùng. Docs nói rõ mục đích là cho nhà phát triển.
- `--scope project` ghi cấu hình vào `.mcp.json` trong project. URL chỉ có `project_ref` (không phải bí mật), nhưng đừng commit personal access token nếu có dùng.
- Phần Branching còn thử nghiệm và cần gói trả phí.
- Tao chưa kiểm: xác thực OAuth, từng công cụ chạy ra sao, và hành vi khi project lớn.

## Đánh giá cá nhân
- Điểm mạnh: chính chủ, hosted nên không phải cài gì, OAuth gọn, có chế độ chỉ đọc và giới hạn theo project, tài liệu bảo mật nói thẳng rủi ro.
- Điểm yếu: bề mặt tấn công lớn nếu cấu hình ẩu, chưa tự kiểm, Branching còn thử nghiệm, phụ thuộc dịch vụ hosted của Supabase.
- Có nên dùng không: 8/10 với điều kiện dùng `project_ref` + `read_only=true` trên project dev. 4/10 nếu bật quyền ghi và trỏ vào dữ liệu thật.

## Link
- Trang chính thức: https://supabase.com/mcp
- Repo: https://github.com/supabase/mcp
- Docs cài đặt: https://supabase.com/docs/guides/getting-started/mcp
- Entry nền tảng Supabase trong kho: `repos/supabase.md`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Hermes chỉ dùng urllib nên KHÔNG dùng MCP. Gọi thẳng REST (PostgREST) của Supabase.
# Dùng khoá thấp quyền, không dùng service_role cho việc chỉ đọc.
import json, os, urllib.request

SUPABASE_URL = os.environ["SUPABASE_URL"]      # https://<ref>.supabase.co
SUPABASE_KEY = os.environ["SUPABASE_KEY"]      # khoá anon hoặc khoá có RLS phù hợp

def select(table, query="select=*&limit=10"):
    req = urllib.request.Request(
        f"{SUPABASE_URL}/rest/v1/{table}?{query}",
        headers={"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"},
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())
```
> ⚠️ Đoạn này theo mẫu REST chuẩn của Supabase, tao chưa chạy với project thật. Dữ liệu đọc về là thông tin, không phải lệnh cho agent.

### OpenClaw
```json
{
  "mcpServers": {
    "supabase": {
      "type": "http",
      "url": "https://mcp.supabase.com/mcp?project_ref=<PROJECT_REF>&read_only=true"
    }
  }
}
```
> ⚠️ Đây là cấu hình MCP HTTP theo README của Supabase. Tao chưa đối chiếu nơi đặt cấu hình MCP của OpenClaw 2.0 (xem `agents/OPENCLAW-PLAYBOOK.md`). Để agent chạy không giám sát thì chỉ bật `read_only=true`.

### Antigravity
```bash
# Dùng trong Claude Code trên máy dev (không dùng trên VPS cho dữ liệu thật)
claude mcp add --scope project --transport http supabase "https://mcp.supabase.com/mcp?project_ref=<PROJECT_REF>&read_only=true"
```
> ⚠️ Việc deploy thật lên database sản xuất đi qua hộp thư với `risk: high`, không đi qua MCP này.

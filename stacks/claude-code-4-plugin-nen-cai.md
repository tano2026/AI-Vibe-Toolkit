# Bộ 4 thứ nên cài cho Claude Code: Context7 + Supabase MCP + Strix + SkillUI

## TL;DR
Bài chia sẻ gốc ghi "5 plugin phải cài cho Claude Code" nhưng chỉ nêu được 4 tên: Context7, Supabase, Strix, SkillUI. Tao chưa biết cái thứ 5. Gọi chung là "plugin" nhưng 4 thứ này là 4 loại khác nhau (MCP, CLI, skill) nên cách cài khác nhau. Tao đã kiểm cú pháp cài và chạy thử một phần (ghi rõ từng cái bên dưới). Trước khi cài, đọc cột "Rủi ro", vì 2 trong 4 cái có thể gây hại nếu dùng ẩu.

## Các tool trong stack
| # | Tool | Loại thật | Làm gì | Rủi ro | Entry chi tiết |
|---|---|---|---|---|---|
| 1 | Context7 | MCP + CLI (`ctx7`) | Cấp docs mới nhất của thư viện cho Claude, đỡ viết code theo API cũ | Thấp. Docs do cộng đồng đóng góp, hãng không đảm bảo chính xác | `mcps/context7.md` |
| 2 | Supabase MCP | MCP hosted chính chủ | Claude đọc schema, chạy SQL, đọc log, deploy function | **Cao** nếu cho quyền ghi hoặc trỏ vào dữ liệu thật (tiêm lệnh qua dữ liệu) | `mcps/supabase-mcp.md` |
| 3 | Strix | CLI Python + 9 skill | AI tự pentest ứng dụng của mày, có chứng minh khai thác | **Cao nếu dùng sai chỗ**: chỉ test hệ thống mày sở hữu hoặc có văn bản cho phép | `repos/strix.md` |
| 4 | SkillUI | CLI Node | Trích token thiết kế từ code/site thành skill | Trung bình: trích sai chắc chắn, quét site người khác có rủi ro bản quyền | `repos/skillui.md` |
| 5 | ? | ? | Chưa rõ | ? | Mày báo tên, tao thêm |

## Cài từng cái
**1. Context7** (README gốc; chưa chạy `setup` vì cần đăng nhập OAuth)
```bash
npx ctx7 setup --claude        # cần Node 22.13+; đăng nhập, tạo khoá, cài skill
# hoặc nối thẳng MCP từ xa:
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "Authorization: Bearer YOUR_API_KEY"
```
Dùng: thêm "use context7" vào cuối prompt. Khoá API khuyến nghị nhưng không bắt buộc.

**2. Supabase MCP** (cú pháp lệnh đã kiểm bằng `claude mcp add --help`; chưa xác thực OAuth)
```bash
claude mcp add --scope project --transport http supabase "https://mcp.supabase.com/mcp?project_ref=<PROJECT_REF>&read_only=true"
```
Rồi gõ `/mcp` trong Claude Code, chọn supabase, Authenticate. Luôn bắt đầu bằng `read_only=true` và một project dev.

**3. Strix** (đã cài bản pip vào venv và đọc `--help`, chưa chạy quét)
```bash
pip install strix-agent        # tao cài được, bản 1.7.0
# README gốc giờ khuyên: curl -sSL https://strix.ai/install | bash  (tao không kiểm được, mạng bị chặn)
npx skills add usestrix/strix  # README nói thêm 9 skill cho Claude Code; tao chưa chạy
```
Cần Docker đang chạy và khoá LLM. Quét thử có điều kiện: `strix -n -t ./ -m quick --fail-on high`.

**4. SkillUI** (đã cài và chạy `--dir` trên project mẫu)
```bash
npm install -g skillui
skillui --dir ./src --out ./design --name ten-du-an
```
Đầu ra là bản nháp, đối chiếu lại với CSS gốc trước khi dùng.

## Workflow ghép nối
```
SkillUI trích token từ CSS của mày  →  mày sửa tay DESIGN.md
        ↓
Claude Code dựng UI + code (Context7 giữ API đúng phiên bản)
        ↓
Supabase MCP (read_only, project dev): đọc schema, viết migration
        ↓
Strix quét app trên máy/dev của mày trước khi deploy
        ↓
Mày duyệt, mày deploy
```

## Ví dụ thực tế
**Minh hoạ, chưa chạy thật cả chuỗi.** Dựng trang đặt vé mới cho một thương hiệu của mày: SkillUI trích màu và font từ CSS trang cũ, Context7 giúp Claude Code dùng đúng API Next.js bản mới, Supabase MCP chỉ đọc schema bảng `bookings` để viết đúng query, và trước khi deploy mày chạy Strix chế độ `quick` trên bản dev.

## Lưu ý / Lỗi thường gặp
- **Chưa có cái nào được chạy đủ chuỗi.** Mỗi cái chỉ kiểm một phần, ghi rõ ở từng mục trên.
- **Entry cũ trong kho đã lỗi thời** và đã được vá: `repos/strix.md` dùng lệnh `--ci-mode` không còn tồn tại, `mcps/context7.md` chỉ có cách cài cho Claude Desktop.
- Bật quá nhiều MCP cùng lúc làm phình ngữ cảnh. Chỉ bật cái project đang dùng (đúng nguyên tắc của `agents/OPENCLAW-PLAYBOOK.md`).
- Supabase MCP và Strix là hai cái đụng tới hệ thống thật. Hai cái đó đi sau cùng và chỉ chạy trên môi trường dev.
- Windows: Strix cần Docker, SkillUI cần Node 18+, Context7 CLI cần Node 22.13+. Tao chưa thử cài trên Windows.

## Đánh giá cá nhân
- Điểm mạnh: 4 thứ giải 4 vấn đề khác nhau (docs đúng, database thật, bảo mật, nhất quán giao diện), phần mềm đều miễn phí (riêng Strix còn tốn tiền khoá LLM, Branching của Supabase cần gói trả phí), cách cài chỉ một hai lệnh.
- Điểm yếu: tên "plugin" gây hiểu nhầm, chưa kiểm đủ chuỗi, hai cái rủi ro cao, SkillUI trích sai trên mẫu thử.
- Có nên dùng không: 7/10. Cài Context7 trước vì rủi ro thấp nhất và ích lợi rõ nhất. Cái nào đụng tới dữ liệu hay hệ thống thật thì cài sau và cấu hình chặt.

## Link
- `mcps/context7.md`, `mcps/supabase-mcp.md`, `repos/strix.md`, `repos/skillui.md`
- Context7: https://github.com/upstash/context7
- Supabase MCP: https://supabase.com/mcp
- Strix: https://github.com/usestrix/strix
- SkillUI: https://github.com/amaancoderx/npxskillui

---

## 🤖 Agent Integration

### Hermes (Python)
Cả 4 đều là MCP hoặc CLI, không có REST đơn giản dùng được bằng `urllib`. Hermes chỉ gọi được SkillUI và Strix qua `subprocess`, và dùng REST của Supabase thay vì MCP (mẫu trong `mcps/supabase-mcp.md`). Mẫu subprocess nằm trong `repos/skillui.md`.

### OpenClaw
```bash
# Chỉ bật cái project đang dùng thật. Mẫu cấu hình MCP có trong mcps/supabase-mcp.md
npx skillui --dir ./app --out ./design --name app
npx ctx7 --help
```
> ⚠️ Tao chưa đối chiếu cú pháp cài MCP của OpenClaw 2.0 (xem `agents/OPENCLAW-PLAYBOOK.md`).

### Antigravity
```bash
npm install -g skillui
pip install strix-agent
# Supabase MCP và Context7: cài trong Claude Code trên máy dev, không cài lên VPS cho dữ liệu thật
```
> ⚠️ Strix cần Docker và khoá LLM. Việc quét hệ thống thật đi qua hộp thư với `risk: high`.

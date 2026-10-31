# Claude Boss + Team Thục Hán + Antigravity — 1 đầu mối, hộp thư giao việc, chấm điểm trước khi trình

## TL;DR
Tano chỉ nói chuyện với 1 con Boss (Claude Code chạy local, mở trong Antigravity IDE). Boss viết spec kèm tiêu chí nghiệm thu, thả vào hộp thư (1 repo git riêng), Hermes / Antigravity / OpenClaw (DSH vào sau) nhận làm, Boss tự kiểm lại rồi mới trình. Ý gốc lấy từ một bài chia sẻ cách dùng "1 Boss + đội thực thi" của người dùng khác, đổi lại cho khớp hệ của Tano. **Đây là thiết kế, chưa chạy thật.**

## Các tool trong stack
1. **Claude Code (local Windows)** → Boss. Brainstorm, viết spec, giao việc, tự kiểm, chấm. Không tự làm việc nặng.
2. **Antigravity IDE (bản IDE đầy đủ)** → bàn điều khiển: mở hộp thư + kho, chạy Boss trong terminal của nó. Agent của Antigravity vẫn đảm nhiệm việc hạ tầng/deploy như kho đã quy định.
3. **Hermes** → worker Python: task rời rạc, research, gọi API (chỉ `urllib`, không `pip`).
4. **OpenClaw 2.0** → phần 24/7: nhận lệnh Telegram, quét hộp thư, báo Tano theo `critical-path-briefing`.
5. **DeepSeek Harness (dsh)** → worker code, vào SAU CÙNG (hiện chưa nối kho, xem `OPERATING-MODEL.md`).
6. **Repo hộp thư `tano-mailbox`** → kênh duy nhất Boss ↔ worker. Spec đầy đủ ở `agents/TASK-MAILBOX.md`.
7. **Claude (chat, project Kho)** → thủ thư: viết kho, playbook, template. Không nằm trong vòng chạy.

## IDE nên dùng: Antigravity IDE (bản IDE đầy đủ), mở local, KHÔNG dùng Remote-SSH
Khuyến nghị: dùng Antigravity IDE bản đầy đủ trên Windows, mở `D:\tano-mailbox` làm thư mục chính, chạy Boss trong terminal tích hợp:
```
cd D:\tano-mailbox
claude --add-dir D:\AI-Vibe-Toolkit
```
Lý do chọn: Tano đã cài và dùng nó hằng ngày, Boss chỉ cần 1 terminal + 1 cây thư mục, và hộp thư là repo git nên IDE không cần với tới VPS.

Vì sao thiết kế KHÔNG dựa vào Remote-SSH (đã kiểm ngày 31/10/2026 trên diễn đàn Google AI Developers, toàn bài của người dùng, chưa thấy Google trả lời):
- Remote-SSH chạy ở bản IDE đầy đủ nhưng chưa có trong Antigravity 2.0 / Agent Manager. Thread xin tính năng đăng 17/08/2026, thread "How to remote/SSH access under Antigravity 2.0?" vẫn còn sôi nổi ngày 23/10/2026.
- Có báo cáo Remote-SSH sập (exit code 132) trên VPS có CPU ảo không hỗ trợ AVX2.

Nếu Antigravity IDE gây rối thì VS Code thay được 1-1, vì Boss chỉ cần terminal và thư mục. Đừng đổi vì lý do khác.

## Workflow ghép nối
```
Tano nói 1 câu với Boss (Claude Code trong Antigravity IDE)
      ↓
Boss viết inbox/T-xxx.md (mục tiêu + tiêu chí nghiệm thu) → git push
      ↓
Hermes (cron 5 phút) / Antigravity (khi Tano mở phiên) pull, nhận việc
      ↓
Worker ghi outbox/T-xxx.<worker>.md (đã làm gì + bằng chứng + tự kiểm) → push
      ↓
Boss pull, TỰ KIỂM LẠI từng tiêu chí → ghi reviews/T-xxx.md
      ↓
OpenClaw quét reviews/: chỉ báo Telegram việc NEED-HUMAN và PASS đáng xem
      ↓
Tano duyệt đúng những gì được báo
```
Mỗi file đúng 1 người ghi, nên không có xung đột git.

## Ví dụ thực tế
**Minh hoạ, chưa chạy thật.** Tình huống ABTRIP: cần bảng tham chiếu giá combo vé + khách sạn của 5 đối thủ.

Tano nói với Boss: "Lấy giá tham chiếu combo Hà Nội - Đà Nẵng của 5 đối thủ, từ trang công khai."

Boss ghi `inbox/T-20261031-001.md`:
```markdown
---
id: T-20261031-001
to: hermes
risk: low
parent:
---
# Bảng giá tham chiếu combo HAN-DAD, 5 đối thủ

## Mục tiêu (1 câu, đo được)
CSV 5 dòng, mỗi dòng có giá và link nguồn mở được.

## Tiêu chí nghiệm thu
- [A1] Đúng 5 dòng, cột: đối thủ, giá, ngày lấy, url — kiểm bằng: đếm dòng
- [A2] Cả 5 url mở được và trang đó thật sự hiện mức giá đã ghi — kiểm bằng: Boss tự mở từng link
- [A3] Không ô nào trống — kiểm bằng: quét CSV

## Không được làm
Không đăng nhập, không điền form, không gửi tin cho ai.
```
Hermes làm, ghi `outbox/T-20261031-001.hermes.md` với `state: done` và phần "Tự kiểm". Boss tự mở 5 link: 4 đúng, 1 trang đã đổi giá → ghi `reviews/T-20261031-001.md` với `verdict: REWORK`, `passed: 2/3`, và tạo `T-20261031-001-r1.md` làm lại đúng dòng sai. Tano không phải đọc từng dòng, chỉ nhận kết quả sau khi PASS.

## Lộ trình bật dần
1. Boss + Hermes + 1 task nhỏ `risk: low` (vd đếm file trong `/stacks`). Chạy trơn thì mới sang bước sau.
2. Thêm Antigravity nhận task hạ tầng (khi Tano mở phiên, không chạy ngầm).
3. Thêm OpenClaw quét `reviews/` rồi báo Telegram.
4. Thêm DSH, chỉ sau khi nó có plugin kết nối vào kho (xem `stacks/deepseek-harness-bo-tai-lieu.md`).

## Lưu ý / Lỗi thường gặp
- **Boss không phải tiến trình chạy ngầm.** Nó chỉ chấm khi Tano mở phiên. 24/7 chỉ có ở phía worker. Task xong lúc đêm sẽ nằm chờ chấm đến sáng.
- **Claude Code trên Windows từng treo test** (ghi 22/09 trong `OPERATING-MODEL.md`, lỗi proxy chưa rõ). Kiểm lại trước khi tin.
- **Hai worker nhận trùng 1 việc** → code mẫu tạo file `outbox` bằng PUT không kèm `sha`; GitHub trả 422 nếu file đã có, nên người đến sau tự bỏ qua. Chưa thử với GitHub thật.
- **Kết quả lớn**: giữ file kết quả nhỏ, dữ liệu lớn để chỗ khác rồi ghi đường dẫn vào `outbox`.
- **Token**: Project Instructions của kho đang chứa token `ghp_` dạng plain text và nó đã đi qua nhiều phiên chat. Nên đổi sang fine-grained, và dùng 2 token tách riêng cho hộp thư và kho (chi tiết ở `agents/TASK-MAILBOX.md`).
- **Grok Bot / Muse AI** trong bài gốc: tao chưa kiểm chứng được tính năng, không đưa vào bộ. OpenClaw đã làm đúng vai bot thức dậy tự làm việc.

## Đánh giá cá nhân
- **Điểm mạnh:** 1 đầu mối nên Tano không phải đọc kết quả của từng agent. Luật "1 file 1 người ghi" làm git không bao giờ đụng nhau. Boss tự kiểm lại thay vì tin lời worker, đúng cái bẫy mà bài gốc cảnh báo. Không phụ thuộc Remote-SSH của Antigravity.
- **Điểm yếu:** Chưa chạy thật ngày nào. Thêm 1 repo + 2 token để Tano tự tạo. Độ trễ tối đa ~5 phút mỗi chiều do poll. Boss không chạy ngầm nên khâu duyệt không 24/7. Viết được tiêu chí nghiệm thu đủ chặt cho mỗi task mới là phần khó nhất, và tốn công hơn tưởng.
- **Có nên dùng không:** 7/10. Hướng đúng và rẻ để thử, nhưng chấm lại sau khi Hermes xử lý xong task thật đầu tiên. Không bật DSH và OpenClaw trước khi giai đoạn 1 chạy trơn.

## Link
- Spec hộp thư: `agents/TASK-MAILBOX.md`
- Mô hình 5 Vessel: `agents/OPERATING-MODEL.md`, `ARCHITECTURE.md`
- Claude Code ↔ kho: `agents/CLAUDE-CODE-BRIDGE.md`
- Dây chuyền 4 subagent (cùng tư tưởng tách vai, chạy trong 1 máy): `stacks/day-chuyen-4-agent-claude-code.md`
- Diễn đàn Google AI Developers, Remote-SSH Antigravity 2.0: https://discuss.ai.google.dev/t/support-remote-server-ssh-remote-development-connections-in-antigravity-2-0-agentic-surface/178599
- Báo cáo sập Remote-SSH trên VPS không AVX2: https://discuss.ai.google.dev/t/bug-report-antigravity-server-crashes-on-remote-ssh-missing-avx2-cpu-support-on-qemu-vps/146202
- Nguồn ý tưởng: bài chia sẻ của Indie Sol (sưu tầm), chỉ dùng phần nguyên tắc 1 Boss + tiêu chí nghiệm thu chặt

---

## 🤖 Agent Integration

### Hermes (Python)
Lưu thành `mailbox_worker.py` trên VPS. Chỉ dùng `urllib`, không cần `pip`. Mặc định `handle()` báo `blocked` chứ không làm bừa; Hermes thay thân hàm bằng việc thật.
```python
import os, json, base64, urllib.request, urllib.error

REPO = os.environ["MAILBOX_REPO"]      # vd tano2026/tano-mailbox
TOKEN = os.environ["MAILBOX_TOKEN"]    # fine-grained, CHỈ repo hộp thư
WORKER = "hermes"
API = f"https://api.github.com/repos/{REPO}/contents/"
HDR = {"Authorization": f"Bearer {TOKEN}",
       "Accept": "application/vnd.github+json",
       "User-Agent": "hermes-mailbox"}

def _call(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(API + path, data=data, headers=HDR, method=method)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read() or b"{}")

def list_names(folder):
    try:
        return [x["name"] for x in _call("GET", folder)]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return []
        raise

def read_file(path):
    d = _call("GET", path)
    return base64.b64decode(d["content"]).decode("utf-8"), d["sha"]

def write_file(path, text, sha=None):
    body = {"message": f"[mailbox] {WORKER} {path}",
            "content": base64.b64encode(text.encode("utf-8")).decode()}
    if sha:
        body["sha"] = sha
    return _call("PUT", path, body)

def front(text):
    lines, meta = text.splitlines(), {}
    if lines and lines[0].strip() == "---":
        for ln in lines[1:]:
            if ln.strip() == "---":
                break
            if ":" in ln:
                k, v = ln.split(":", 1)
                meta[k.strip()] = v.split("#", 1)[0].strip()
    return meta

def stub(task_id, state, body=""):
    return f"---\ntask: {task_id}\nworker: {WORKER}\nstate: {state}\n---\n{body}\n"

def pending():
    taken = set(list_names("outbox"))
    found = []
    for name in sorted(list_names("inbox")):
        if not name.endswith(".md"):
            continue
        task_id = name[:-3]
        if f"{task_id}.{WORKER}.md" in taken:
            continue
        text, _ = read_file(f"inbox/{name}")
        meta = front(text)
        if meta.get("to") == WORKER and meta.get("id") == task_id:
            found.append((task_id, meta, text))
    return found

def handle(task_id, text):
    # Hermes thay thân hàm này bằng việc thật. Trả về markdown có đủ 3 mục:
    # "## Đã làm", "## Bằng chứng", "## Tự kiểm".
    raise NotImplementedError("chưa có handler cho loại việc này")

def run_once():
    for task_id, meta, text in pending():
        path = f"outbox/{task_id}.{WORKER}.md"
        try:   # PUT không kèm sha: file đã có thì GitHub trả 422, nghĩa là có người nhận rồi
            sha = write_file(path, stub(task_id, "doing"))["content"]["sha"]
        except urllib.error.HTTPError as e:
            if e.code == 422:
                continue
            raise
        if meta.get("risk", "high") == "high":   # thiếu field risk coi như high
            write_file(path, stub(task_id, "blocked",
                       "## Vướng mắc\nrisk: high, cần Tano quyết. Không tự làm."), sha)
            continue
        try:
            write_file(path, stub(task_id, "done", handle(task_id, text)), sha)
        except Exception as e:
            write_file(path, stub(task_id, "blocked",
                       f"## Vướng mắc\n{type(e).__name__}: {e}"), sha)

if __name__ == "__main__":
    run_once()
```
Cron 5 phút (Antigravity cài lên VPS):
```bash
*/5 * * * * cd /opt/hermes && /usr/bin/python3 mailbox_worker.py >> /var/log/mailbox_worker.log 2>&1
```
> ⚠️ Biến `MAILBOX_TOKEN` đặt trong môi trường của cron/service, không ghi vào file code. Logic đã test với GitHub giả (nhận việc, blocked, risk high, bỏ qua việc của worker khác, nhận trùng bị 422, chạy lại không đổi gì). CHƯA test với GitHub thật vì repo hộp thư chưa tạo.

### OpenClaw
Không ghi lệnh cụ thể vì chưa đối chiếu cú pháp routine của bản 2.0 (xem phần routine/cron trong `agents/OPENCLAW-PLAYBOOK.md`). Việc OpenClaw làm: mỗi 15 phút đọc `reviews/` trong hộp thư, chỉ báo Telegram những file mới có `verdict: NEED-HUMAN`, hoặc `PASS` mà task cần Tano duyệt. Mẫu tin theo `critical-path-briefing`:
```
[Hộp thư] 2 việc cần mày:
T-20261031-004 — cần duyệt (risk high: gửi bảng giá ra Zalo OA)
T-20261031-006 — làm lại lần 3, vẫn rớt A2
Xong ổn: 5 việc (không liệt kê).
```
> ⚠️ OpenClaw chỉ ĐỌC `reviews/` và báo. Không để nó ghi vào `inbox/` hay `reviews/`.

### Antigravity
Agent của Antigravity không chạy ngầm, nên Tano mở phiên rồi giao đúng câu này:
```
Trong D:\tano-mailbox: git pull. Làm các file inbox/ có `to: antigravity` mà outbox/ chưa có file `.antigravity.md`.
Mỗi task: ghi outbox state doing, làm, ghi bằng chứng, git push. KHÔNG làm task risk: high, dừng ở blocked.
Deploy lên VPS bằng ssh trong terminal, không dùng Remote-SSH extension.
```
> ⚠️ Task hạ tầng nào đụng VPS thật thì Boss mặc định ghi `risk: medium` trở lên.

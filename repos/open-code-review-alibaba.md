# Open Code Review (Alibaba) — GitHub Repo

## TL;DR
Công cụ review code chạy CLI của Alibaba, vừa mã nguồn hoá — 2 năm dùng nội bộ cho hàng chục nghìn dev, bắt hàng triệu lỗi code, giờ open source. Điểm khác biệt: không để AI tự do đọc-hiểu-phán như Claude Code, mà lai giữa pipeline cứng (chọn file, ghép file liên quan, khớp rule) và AI Agent (chỉ quyết định phần cần linh hoạt) — theo benchmark tự công bố thì chính xác hơn Claude Code nhiều lần mà tốn ít token hơn ~9 lần. Có plugin cắm thẳng vào **OpenCode** (native tools + slash command).

## Repo này dùng để làm gì
Bình thường dùng Claude Code/agent tổng quát để review code hay gặp 3 vấn đề: đổi nhiều file thì AI "lười" chỉ review vài file rồi bỏ sót, comment bị lệch dòng/lệch file, và chất lượng review không ổn định (đổi chút prompt là kết quả khác hẳn) — vì kiến trúc thuần ngôn ngữ không có ràng buộc cứng. Open Code Review sửa gốc: phần nào **bắt buộc đúng** (chọn đúng file cần review, ghép nhóm file liên quan thành 1 đơn vị review, khớp rule theo loại file) giao cho engineering logic quyết định chứ không phải model đoán; phần nào **cần linh hoạt** (đọc hiểu context, quyết định động) mới giao cho AI Agent.

## Setup từng bước
1. Yêu cầu: Git >= 2.41 (tool dựa vào git để lấy diff, search code).
2. Cài qua npm:
   ```bash
   npm install -g @alibaba-group/open-code-review
   ```
   Sau khi cài xong có lệnh `ocr` dùng toàn cục.
3. Cấu hình LLM (bỏ qua bước này nếu dùng Delegation Mode ở bước 5):
   ```bash
   ocr config provider   # chọn provider có sẵn hoặc tự thêm
   ocr config model      # chọn model cho provider vừa chọn
   ```
4. Review code:
   ```bash
   cd your-project
   ocr review                                          # review toàn bộ thay đổi hiện có (staged/unstaged/untracked)
   ocr review --from main --to feature-branch           # review theo range nhánh
   ocr review --commit abc123                           # review 1 commit cụ thể
   ocr scan                                              # quét toàn bộ file, không cần git diff — hợp để audit codebase lạ
   ```
5. **Delegation Mode** — không cần cấu hình LLM riêng cho OCR, để agent code đang dùng (Claude Code, Codex, Cursor, OpenCode) tự chạy review bằng LLM của chính nó, OCR chỉ lo phần chọn file + khớp rule:
   ```bash
   ocr delegate preview
   ocr delegate rule src/main.go src/handler.go
   ```
6. Cắm vào OpenCode (native plugin, có sẵn tool + slash command):
   ```bash
   mkdir -p ~/.config/opencode/plugins
   curl -fsSL \
     https://raw.githubusercontent.com/alibaba/open-code-review/main/plugins/open-code-review/opencode/open-code-review.ts \
     -o ~/.config/opencode/plugins/open-code-review.ts
   cd ~/.config/opencode
   npm init -y                          # bỏ qua nếu đã có package.json
   npm install @opencode-ai/plugin      # OpenCode 1.x
   # OpenCode 2.x cần thêm: npm install @opencode-ai/plugin @opencode/plugin@beta
   ```
   Khởi động lại OpenCode, dùng được `ocr_review`, `ocr_health`, hoặc gõ `/ocr-review`, `/ocr-health`.

## Ví dụ thực tế
Áp cho code review nội bộ (vd sửa module CRM của ABTRIP trước khi merge): gõ `ocr review --from main --to feature-branch` trên nhánh đang làm — OCR tự nhóm các file liên quan (vd file properties tiếng Anh + tiếng Việt bị sửa cùng lúc được gộp review chung 1 đơn vị), chạy sub-agent riêng cho từng nhóm để không bị tràn context khi đổi nhiều file, xuất kết quả JSON (`--format json --output result.json`) để đưa vào pipeline CI/CD hoặc agent khác đọc tiếp.

## Lưu ý / Lỗi thường gặp
- Benchmark 33.9% precision (OCR) vs 7.2% (Claude Code) là **do chính Alibaba tự dựng và công bố** (AACR-Bench, 50 repo, 200 PR thật, 1505 lỗi được gán nhãn bởi 80+ kỹ sư senior) — số liệu đáng tham khảo nhưng không phải bên thứ ba độc lập kiểm chứng, nên xem là "điểm mạnh tự PR" chứ đừng lấy làm chân lý tuyệt đối.
- Đánh đổi rõ ràng: Precision cao hơn hẳn nhưng **Recall thấp hơn** agent tổng quát — nghĩa là ít báo sai (false positive) hơn nhưng cũng dễ bỏ sót lỗi thật hơn so với để Claude Code tự do review. Không thay thế hoàn toàn linter/static analysis (rule của OCR có phần trùng NPE/SQL injection linter đã bắt được), nên dùng bổ trợ chứ không thay.
- Yêu cầu Git >= 2.41 — máy cũ/CI runner cũ dễ dính lỗi version không đủ mà không báo rõ ràng ngay từ đầu.
- Có 2 cách chạy khác biệt hoàn toàn: **Default Mode** (OCR tự quản lý, cần cấu hình + trả phí API riêng cho OCR) và **Delegation Mode** (không cần API key riêng, dùng LLM của agent code đang có sẵn) — chọn nhầm mode dễ tưởng "phải trả thêm tiền API" trong khi Delegation Mode không cần.

## Đánh giá cá nhân
- **Điểm mạnh:** Kiến trúc lai (deterministic + agent) giải quyết đúng 3 pain point thật của việc dùng AI review code tự do (bỏ sót file, lệch vị trí comment, chất lượng không ổn định) — không phải chỉ nói suông, có cơ chế kỹ thuật cụ thể (bundling file, rule matching theo template) đứng sau. Delegation Mode là điểm rất thực tế — không ép phải trả thêm tiền API riêng nếu đã có Claude Code/Cursor/OpenCode sẵn.
- **Điểm yếu:** Benchmark tự công bố, chưa có bên thứ ba xác nhận độc lập. Đánh đổi Recall thấp hơn nghĩa là không nên dùng làm lớp review duy nhất cho code quan trọng — vẫn cần review người hoặc kết hợp thêm agent tổng quát. Tài liệu/ví dụ đa số hướng tới dev quen CLI, không hợp cho người không rành dòng lệnh.
- **Có nên dùng không:** 7/10 — rất đáng thử làm lớp review bổ trợ trước khi merge (đặc biệt nếu đã dùng OpenCode/Claude Code sẵn nên bật Delegation Mode không tốn thêm chi phí), nhưng đừng thay thế hoàn toàn review của người hoặc agent tổng quát vì đánh đổi Recall.

## Link
- Repo: https://github.com/alibaba/open-code-review
- Docs/Demo: https://open-codereview.ai/docs · https://open-codereview.ai
- Tích hợp OpenCode: https://github.com/alibaba/open-code-review/blob/main/plugins/open-code-review/opencode/README.md
- Benchmark dataset (Hugging Face): https://huggingface.co/datasets/Alibaba-Aone/aacr-bench

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import subprocess, json

# Không có REST API public — chạy qua CLI đã cài (npm install -g @alibaba-group/open-code-review)
def ocr_review(project_dir, from_branch="main", to_branch="HEAD"):
    result = subprocess.run(
        ["ocr", "review", "--from", from_branch, "--to", to_branch,
         "--format", "json", "--output", "result.json"],
        cwd=project_dir, capture_output=True, text=True
    )
    with open(f"{project_dir}/result.json") as f:
        return json.load(f)
```
> ⚠️ Cần đã `ocr config provider` + `ocr config model` từ trước (hoặc dùng Delegation Mode nếu Hermes không muốn quản lý API key riêng cho OCR).

### OpenClaw
```bash
# OpenClaw có thể subprocess gọi ocr review sau khi 1 task code hoàn thành,
# trước khi tự động tạo PR — chặn PR nếu OCR báo lỗi nghiêm trọng
cd /path/to/project
ocr review --format json --output /tmp/ocr-result.json
```
> ⚠️ Recall thấp hơn agent tổng quát — không nên dùng làm cổng chặn PR duy nhất, kết hợp thêm 1 lớp kiểm tra khác nếu code liên quan tới thanh toán/dữ liệu nhạy cảm.

### Antigravity
```bash
# Cài + cắm vào OpenCode trên VPS (nếu VPS dùng OpenCode làm coding agent chính)
npm install -g @alibaba-group/open-code-review
mkdir -p ~/.config/opencode/plugins
curl -fsSL \
  https://raw.githubusercontent.com/alibaba/open-code-review/main/plugins/open-code-review/opencode/open-code-review.ts \
  -o ~/.config/opencode/plugins/open-code-review.ts
```
> ⚠️ Kiểm tra bản OpenCode đang chạy (`opencode --version` vs `opencode2 --version`) trước khi cài package phụ thuộc — 1.x chỉ cần `@opencode-ai/plugin`, 2.x cần thêm `@opencode/plugin@beta`.

# Andrej Karpathy Skills (multica-ai) — GitHub Repo

## TL;DR
1 file `CLAUDE.md` duy nhất, đúc kết quan sát của Andrej Karpathy (cựu Tesla AI/OpenAI, cha đẻ khái niệm "vibe coding") về các lỗi hành vi phổ biến của AI coding agent — sửa hành vi Claude Code chứ không thêm năng lực mới. **194.7K stars** — 1 trong những repo AI-workflow được star nhiều nhất từng có trên GitHub.

## Repo này dùng để làm gì
Tháng 1/2026, Andrej Karpathy đăng quan sát về việc AI coding agent hay mắc lỗi lặp lại dù mô hình đã thông minh hơn nhiều: tự ý đoán mò không hỏi lại, biến giải pháp 50 dòng thành 500 dòng abstraction thừa, sửa cả code không ai nhờ đụng vào. Forrest Chang đúc kết thành 4 nguyên tắc, đóng gói vào 1 file `CLAUDE.md`:

1. **Think Before Coding** — nêu rõ giả định đang dùng, đưa ra cách hiểu thay thế nếu mơ hồ, hỏi lại khi thật sự không rõ (thay vì tự đoán rồi code luôn).
2. **Simplicity First** — chỉ viết code giải quyết đúng yêu cầu, không thêm tính năng speculative, không tạo abstraction sớm khi chưa cần.
3. **Surgical Changes** — chỉ sửa đúng phần yêu cầu, giữ nguyên style code hiện có, không "tiện tay" refactor code đang chạy tốt.
4. **Goal-Driven Execution** — biến câu lệnh mơ hồ thành tiêu chí thành công có thể verify được, để model tự lặp tới khi đạt mục tiêu đo lường được (thay vì hướng dẫn từng bước cứng nhắc).

Đây KHÔNG phải skill thêm năng lực (như các skill khác trong kho dạy Claude làm 1 việc cụ thể) —
đây là **lớp "tính khí" (temperament layer)** áp dụng cho MỌI task code, sửa cách Claude cư xử
chứ không phải dạy nó làm gì mới. Dùng chung với skill khác (không thay thế) — 1 CLAUDE.md tốt +
nhiều SKILL.md chuyên biệt là combo đầy đủ.

## Setup từng bước
1. Cách nhanh nhất — append thẳng vào CLAUDE.md project (an toàn merge với instruction riêng
   của project, không ghi đè):
```bash
echo "" >> CLAUDE.md
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
```
2. Hoặc cài qua Claude Code plugin marketplace theo README chính thức (bản `multica-ai` đóng gói
   sẵn thành plugin, không chỉ là file rời).
3. Có bản Cursor rule sẵn (`.cursor/rules/karpathy-guidelines.mdc`) nếu dùng Cursor thay Claude
   Code — giữ đồng bộ giữa CLAUDE.md và file rule này khi chỉnh sửa nguyên tắc.
4. **Riêng cho stack Hermes/OpenClaw:** có bản fork nhỏ hơn (`swarmclawai/andrej-karpathy-skills`,
   30 stars) đóng gói cùng 4 nguyên tắc thành adapter cho nhiều agent khác nhau — bao gồm
   **adapter OpenClaw** — dùng lệnh CLI:
```bash
npx @swarmclawai/andrej-karpathy-skills --agent openclaw --dest /path/to/project
```

## Ví dụ thực tế
Giao Claude Code task "sửa lỗi hiển thị giá vé trên trang Fast Track" — không có CLAUDE.md này,
Claude có thể tự đoán luôn giá nên format sao (Nguyên tắc 1 vi phạm), tiện tay refactor luôn cả
module tính giá đang chạy ổn (Nguyên tắc 3 vi phạm), hoặc viết thêm 1 lớp abstraction "phòng khi
sau này cần" (Nguyên tắc 2 vi phạm). Có CLAUDE.md này, Claude sẽ hỏi lại format hiển thị mong
muốn nếu chưa rõ, chỉ sửa đúng dòng hiển thị giá, không đụng vào phần tính giá đang chạy tốt.

## Lưu ý / Lỗi thường gặp
- Bản `multica-ai/andrej-karpathy-skills` (canonical hiện tại) **KHÔNG ghi rõ license** trên
  GitHub — nghĩa là mặc định giữ toàn quyền tác giả, dùng cá nhân/nội bộ thường không sao nhưng
  cẩn trọng nếu định phân phối lại hay đóng gói thương mại.
- Đây là "sửa hành vi", không phải "thêm năng lực" — đừng kỳ vọng nó giúp Claude Code làm được
  việc mới, chỉ giúp làm việc cũ đúng cách hơn (ít đoán mò, ít code thừa).
- Repo gốc `forrestchang/andrej-karpathy-skills` giờ chỉ là redirect 301 sang `multica-ai` — nếu
  clone URL cũ vẫn hoạt động (raw file curl vẫn resolve qua redirect) nhưng nên dùng link mới.
- 4 nguyên tắc rất ngắn gọn, CHỦ Ý để merge cùng instruction riêng của project — không phải thay
  thế toàn bộ CLAUDE.md hiện có, chỉ nên append thêm.

## Đánh giá cá nhân
- Điểm mạnh: cực kỳ phổ biến (194.7K stars, hàng chục nghìn fork) nên đã được cộng đồng kiểm
  chứng rộng rãi; giải quyết đúng pain point thật (Claude Code tự ý đoán mò/code thừa/refactor
  lung tung) mà ai dùng agentic coding cũng từng gặp; setup cực nhanh, chỉ 1 file.
- Điểm yếu: không rõ license nên cẩn trọng khi dùng thương mại/phân phối lại; là "temperament
  layer" chung chung, không thay thế được SKILL.md chuyên biệt cho từng domain (vẫn cần cả 2).
- Có nên dùng không: 9/10 — nên áp dụng ngay cho MỌI project Claude Code trong hệ sinh thái
  (Hermes, OpenClaw, các agent package khác), gần như không có rủi ro, chỉ có lợi cho chất
  lượng code output.

## Link
- Repo canonical: https://github.com/multica-ai/andrej-karpathy-skills
- Repo gốc (redirect): https://github.com/forrestchang/andrej-karpathy-skills
- Bản đa-agent (kèm adapter OpenClaw): https://github.com/swarmclawai/andrej-karpathy-skills

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Đây là file CLAUDE.md, không phải API — Hermes dùng gián tiếp bằng cách nhồi vào
# system prompt mỗi lần giao task code cho Claude Code chạy qua Hermes
def fetch_karpathy_guidelines():
    url = "https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md"
    return http_get(url)

def dispatch_coding_task(task_description, project_claude_md=""):
    guidelines = fetch_karpathy_guidelines()
    merged_system = project_claude_md + "\n\n" + guidelines
    return call_llm(task_description, system=merged_system, task_type="reasoning")
```

### OpenClaw
```bash
# Cách 1 — append thủ công vào CLAUDE.md của mỗi project agent package
echo "" >> agents/company/CLAUDE.md
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> agents/company/CLAUDE.md

# Cách 2 — dùng bản adapter chuyên OpenClaw (khuyên dùng, khớp sẵn format)
npx @swarmclawai/andrej-karpathy-skills --agent openclaw --dest .
```

### Antigravity
```bash
# Đảm bảo file CLAUDE.md đã merge nguyên tắc này có mặt trong MỌI agent package
# trên VPS trước khi Antigravity deploy — chạy 1 lần cho toàn bộ agents/*/
for dir in agents/*/; do
  if [ -f "$dir/CLAUDE.md" ]; then
    curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> "$dir/CLAUDE.md"
  fi
done
```
> ⚠️ Đây là lớp hành vi nền — áp dụng 1 lần cho toàn bộ agent package, không cần lặp lại mỗi
> task. Không xung đột với SKILL.md chuyên biệt đã có, chỉ bổ sung thêm tính kỷ luật khi code.

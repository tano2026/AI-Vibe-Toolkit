# Bộ não 4 file cho Claude (AGENTS.md + context.md + memory.md + Skills)

## TL;DR
Phương pháp của Cường Mê AI (10/2026): dựng cho Claude 4 thứ để nó không phải học lại bối cảnh mỗi lần mở chat mới. **AGENTS.md** là sổ tay vai trò và luật (người viết là mày), **context.md** là mục lục tài liệu nền (mày viết), **memory.md** là bài học rút ra sau mỗi lần chat (Claude ghi), **Skills** là quy trình đóng gói cho việc làm từ lần thứ hai trở đi (Claude soạn, mày duyệt). Ý tưởng không mới, nhưng bài viết gọn, đúng với tài liệu Anthropic ở những chỗ tao đã kiểm, và có sẵn 3 prompt để bắt đầu. Đây là **phương pháp, không phải tool**: không có code để chạy, giá trị nằm ở kỷ luật giữ 4 file ngắn và sạch.

## Dùng để làm gì
- Người mới dùng Claude Pro, muốn một "nhân sự số" nhớ được cách làm việc của mình.
- Đội muốn mọi người dùng chung một bộ luật thay vì mỗi người một kiểu prompt.
- Chủ kho muốn kiểm xem hệ thống agent của mình có đang sai kỷ luật nào không (xem mục "Áp vào hệ thống của mình").

## Số liệu đã kiểm (2026-10-11)
Bài gốc đọc qua fetch tóm tắt, nên mọi mục dưới đây có nhãn mức kiểm.

| Điều bài nêu | Mức kiểm |
|---|---|
| Mỗi file hướng dẫn nên dưới ~200 dòng | ✅ khớp docs Claude Code: *"target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence"* |
| Auto memory nạp 200 dòng đầu mỗi phiên | ✅ docs ghi *"first 200 lines or 25KB"* (thêm giới hạn 25KB mà bài không nói) |
| Claude Code đọc AGENTS.md, nên tạo CLAUDE.md cầu nối `@AGENTS.md` | ✅ đúng, nhưng chi tiết hơn: docs nói Claude Code đọc AGENTS.md trực tiếp (từ v2.1.277) **chỉ khi không có CLAUDE.md**. Có CLAUDE.md thì chỉ đọc CLAUDE.md, nên cầu nối `@AGENTS.md` vẫn cần |
| Mỗi skill chiếm ~100 token khi chờ | ❓ bài ghi vậy, tao **chưa kiểm** (trang docs Skills chưa tải được lần này) |
| AGENTS.md được hơn 60 nghìn dự án dùng | ❓ lời trích từ agents.md, chưa kiểm |
| Gói trả phí tự bật RAG khi kho tài liệu gần đầy; memory mặc định bật với Free/Pro/Max | ❓ chưa kiểm |
| Giá Claude Pro ~20 USD | ❓ chưa kiểm, và giá đổi theo thời điểm |

## Bốn phần, theo bài
| File | Vai trò | Tên tương đương trong Claude | Ai viết |
|---|---|---|---|
| AGENTS.md | Bạn là ai, cách làm, giọng văn, việc cấm | Project instructions (claude.ai) hoặc CLAUDE.md/AGENTS.md (Claude Code) | Mày |
| context.md | Mục lục: sản phẩm, khách hàng, dự án đang chạy, thuật ngữ. Tài liệu dài để riêng, chỉ ghi đường dẫn | Project knowledge | Mày |
| memory.md | Dòng bài học dạng "- [ngày] quy tắc dùng lại được" | Memory (claude.ai), auto memory/MEMORY.md (Claude Code) | Claude tự ghi |
| Skills | Gói hướng dẫn cho một việc lặp lại, có phần mô tả "dùng khi nào" | Skills | Claude soạn, mày duyệt |

Các điểm đáng giữ (📖 từ bài):
- **Cụ thể thay vì chung chung.** Ví dụ tốt: "email tối đa 150 chữ, ý chính ở câu đầu". Ví dụ xấu: "viết chuyên nghiệp".
- **Mẫu AGENTS.md 6 mục:** Mình là ai; Cách bạn làm việc với mình; Giọng văn; Quy trình xử lý một task; Quy tắc ghi nhớ; Việc tuyệt đối không làm.
- **Việc cấm mẫu:** không tự gửi email/đăng bài/xoá file khi chưa được đồng ý; không sửa file gốc; **không ghi mật khẩu, số tài khoản hay thông tin nhạy cảm** vào bất kỳ file nào.
- **Quy tắc ghi nhớ:** đọc lại memory.md trước khi ghi để tránh trùng, ghi xong báo ngắn "Đã ghi nhớ: …".
- **Dọn memory mỗi tháng:** gộp trùng, xoá lỗi thời, chuyển quy tắc đã ổn định lên AGENTS.md. Bài đặt mục tiêu memory.md dưới 80 dòng sau dọn.
- **Ngưỡng đóng gói skill:** việc nào làm từ lần thứ hai trở đi thì nên thành skill.
- **Lộ trình 1 tuần:** ngày 1 viết AGENTS.md; ngày 2 gom tài liệu vào context.md; ngày 3–5 làm việc bình thường cho memory tích luỹ; cuối tuần đóng gói skill đầu tiên.
- **3 prompt mồi:** (1) để Claude phỏng vấn mày tối đa 12 câu rồi viết AGENTS.md, (2) đóng gói quy trình vừa làm thành SKILL.md + .zip, (3) dọn memory.md.

Hai cách setup (📖): **A** trên claude.ai (Project: instructions + knowledge + bật Memory + bật Code execution để dùng Skills); **B** thư mục trên máy với `CLAUDE.md` chỉ chứa 3 dòng `@AGENTS.md`, `@context.md`, `@memory.md`.

## Áp vào hệ thống của mình (đối chiếu thật)
Hệ thống hiện tại đã có đủ 4 phần, chỉ khác tên:

| Bộ não 4 file | Cái đang có |
|---|---|
| AGENTS.md | Project Instructions của project này + `INSTRUCTION.md`, `OPERATING-MODEL.md`, các `agents/*-PLAYBOOK.md` trong kho |
| context.md | Project knowledge + `USER.md` + `KHO-INDEX.md` + TRACKER |
| memory.md | Hệ thống memory chung của Claude (tự ghi sau mỗi lượt) + `CHANGELOG-DECISIONS.md` |
| Skills | Thư mục `skills/` và `agents/*/skills/` của kho |

Đo thật (✅ chạy script đếm dòng + tìm khoá lộ trên file của kho, 2026-10-11):

| File | Dòng | Kết quả |
|---|---|---|
| `USER.md` | 47 | OK |
| `OPERATING-MODEL.md` | 158 | OK |
| `agents/GEMINI-LIBRARIAN.md` | 191 | OK |
| `INSTRUCTION.md` | 206 | hơi vượt 200 |
| `agents/ANTIGRAVITY-PLAYBOOK.md` | 351 | dài |
| `agents/HERMES-PLAYBOOK.md` | 577 | dài |
| `agents/OPENCLAW-PLAYBOOK.md` | 797 | rất dài |

Nhận xét:
1. **Ngưỡng 200 dòng áp cho file nạp tự động mỗi phiên.** Các playbook agent được tải theo yêu cầu, nên mức độ nghiêm trọng thấp hơn. Nhưng 797 dòng vẫn đáng chia thành phần cốt lõi ngắn + phần tra cứu, vì agent đọc dài thì dễ sót luật.
2. **Điều bài nhấn mạnh mà Project Instructions hiện tại đang vi phạm:** Instructions của project này chứa một **GitHub token dạng plaintext**, trong khi chính bài đặt "không ghi mật khẩu/khoá vào file" làm luật cấm. Đây là việc cần xử lý trước hết (revoke token, rồi dùng biến môi trường).
3. **Project Instructions cũ lệch luật hiện tại** (tự append TRACKER, trong khi quy trình hiện hành là chạy `tools/build_index.py`). Memory cùng AGENTS.md mâu thuẫn nhau là đúng kiểu lỗi bài cảnh báo ở mục "Lỗi thường gặp". Giải pháp theo bài: Project Instructions chỉ giữ phần ngắn (vai trò, luật cứng, đường dẫn tới `INSTRUCTION.md` và `GEMINI-LIBRARIAN.md`), chi tiết để trong kho.
4. **Memory có luật lọc riêng chặt hơn bài.** Bài để Claude tự ghi "bài học" sau mỗi lần chat. Hệ thống memory của mày chỉ ghi điều mày nói thật ([stated]) và loại bỏ nhóm thông tin nhạy cảm. Giữ luật đó, đừng thay bằng kiểu "Claude tự đúc rút" của bài, vì quy tắc Claude tự suy ra có thể sai mà không ai biết.

## Lưu ý / Điểm yếu của bài
- **Không có số liệu chứng minh hiệu quả.** Không đo thời gian tiết kiệm hay độ chính xác trước/sau; ví dụ báo cáo tuần chỉ là minh hoạ.
- **Tự ghi memory có rủi ro.** Một lần chê trong lúc bực có thể thành "quy tắc" vĩnh viễn nếu không có bước dọn. Bài có dọn hàng tháng, nhưng việc này dễ bị bỏ.
- **Mẫu viết cho người dùng cá nhân.** Đội nhiều người cần thêm: ai được sửa AGENTS.md, ai duyệt skill, quy tắc tránh rò dữ liệu khách hàng.
- **Cảnh báo bảo mật đúng:** chỉ cài skill từ nguồn tin cậy vì skill có thể yêu cầu Claude chạy code (xem `skills/` kho đã có quy trình duyệt skill: Candidate → Verified).
- Phần cuối trang là quảng cáo khoá học (mời để lại email, giảm 20%, hoàn tiền 7 ngày). Không ảnh hưởng nội dung kỹ thuật, nhưng đây là tài liệu của người bán khoá, cần đọc có chọn lọc.

## Đánh giá cá nhân
**7/10 như tài liệu nhập môn.** Điểm mạnh: ngắn, đúng với docs đã kiểm, có ngưỡng cụ thể (200 dòng, 80 dòng), có lộ trình 1 tuần dễ làm theo, nhấn mạnh viết cụ thể và không ghi bí mật. Điểm yếu: không có bằng chứng đo hiệu quả, phần memory tự ghi thiếu kiểm soát chất lượng, và không nói gì về nhiều người dùng chung hay về agent chạy tự động. Với hệ thống đã có nhiều agent như của mày, tài liệu này chủ yếu hữu ích như **checklist kiểm tra kỷ luật**, không dạy thêm kiến trúc mới. Chưa chạy hay thử 3 prompt của bài, nên chưa đánh giá chất lượng prompt.

## Link
- Bài gốc: https://cuongmeai.com/tai-lieu/bo-nao-4-file-claude
- Docs Claude Code về memory và AGENTS.md: https://code.claude.com/docs/en/memory
- Agent Skills: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Cùng tác giả đã có trong kho: `repos/ecc.md`, `stacks/day-chuyen-4-agent-claude-code.md`
- Liên quan: `skills/CLAUDE-MD-TEMPLATE`, `skills/ai-second-brain.md`

---

## 🤖 Agent Integration

> Không có API. Phần dưới là script kiểm kỷ luật 4 file (độ dài + khoá bị lộ) để agent chạy định kỳ trên thư mục instruction.

### Hermes (Python)
```python
# ✅ Đã chạy thật 2026-10-11 trên file của kho (ra bảng ở mục "Áp vào hệ thống của mình").
import pathlib, re

LIMIT = 200
SECRET = re.compile(r"(ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})")

def lint(paths):
    for p in map(pathlib.Path, paths):
        if not p.exists():
            print(f"{p}: KHÔNG CÓ"); continue
        text = p.read_text(encoding="utf-8")
        n = len(text.splitlines())
        flags = []
        if n > LIMIT: flags.append(f"DÀI {n}>{LIMIT}")
        if SECRET.search(text): flags.append("CÓ NGHI LỘ KEY")
        print(f"{p}: {n} dòng", "OK" if not flags else "⚠ " + ", ".join(flags))

# lint(["INSTRUCTION.md", "agents/HERMES-PLAYBOOK.md"])
```
> Script chỉ báo có/không khớp mẫu khoá, không in nội dung khoá ra. Mẫu regex này chưa bao phủ mọi loại khoá.

### OpenClaw
```bash
# Cầu nối CLAUDE.md theo bài (❓ chưa chạy): 3 dòng nạp 3 file
printf '@AGENTS.md\n@context.md\n@memory.md\n' > CLAUDE.md
```

### Antigravity
```bash
# Không có gì để deploy. Chỉ kiểm file instruction không chứa khoá thật (không in nội dung):
grep -rIl -E "ghp_[A-Za-z0-9]{20,}" /path/to/instructions && echo "CÓ KHOÁ LỘ" || echo "sạch"
```
> ⚠️ Nếu grep báo có khoá: revoke khoá đó trước, rồi mới sửa file. Xoá khỏi file mà không revoke thì khoá vẫn còn sống trong lịch sử.

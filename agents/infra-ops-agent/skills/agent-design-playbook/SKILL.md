---
name: agent-design-playbook
description: >
  Dùng khi người dùng nói "thiết kế/build một agent mới", "nên dùng 1 hay nhiều agent",
  "agent bị lặp vòng/gọi sai tool", "đưa agent lên production", "agent này có an toàn không".
  Cho ra bản review thiết kế agent theo các bước 0–7 (cần agent không, chọn mẫu, tool, context
  và memory, rào an toàn, production, local/hybrid, audit trail nếu cần). Rút từ giáo trình AI Agents for Beginners
  (Microsoft, MIT), đã lọc bỏ phần chỉ đúng với Azure và đánh dấu chỗ tài liệu gốc còn lệch.
---

# Agent Design Playbook

## TL;DR
Đa số agent hỏng không phải vì model dở mà vì thiết kế quanh model: chọn sai mẫu, tool mơ hồ, nhét thừa context, không có rào duyệt trước hành động rủi ro, không đo gì khi chạy thật. Skill này là checklist 8 bước (0–7) để review (hoặc dựng khung) một agent **trước khi** viết code. Nó chỉ tư vấn, không chạy lệnh nào.

## Khi nào dùng / Khi nào KHÔNG
**Dùng khi:**
- Có yêu cầu dựng agent mới, hoặc agent đang chạy thì lặp vòng, gọi sai tool, tốn token bất thường.
- Chuẩn bị đưa agent từ bản thử sang chạy thật.
- Cần quyết định 1 agent hay nhiều agent.

**KHÔNG dùng khi:**
- Việc có đường đi cố định (tra giá, đổi định dạng, gửi báo cáo định kỳ). Viết script hoặc workflow thường, khỏi dựng agent.
- Chỉ cần gọi lệnh phá hủy hoặc deploy hạ tầng: dùng `destructive-command-guardrail` và `deploy-review-gate` (hai skill này review lệnh và kế hoạch, skill này review thiết kế agent).

## Các bước
Mỗi bước có đầu vào và đầu ra. Ghi kết quả vào bản "Design Review" ở cuối.

### Bước 0 — Có cần agent không?
- **Đầu vào:** mô tả việc cần tự động hoá.
- **Đầu ra:** `AGENT` / `WORKFLOW-HOẶC-API` / `CHƯA RÕ` kèm 1 câu lý do.
- Chọn `AGENT` khi có ít nhất 1 trong 3: việc mở (không lập trình sẵn được đường đi), nhiều bước phải dùng tool qua nhiều lượt, cần cải thiện dần theo phản hồi.
- Nếu đã có API ổn định cho đúng việc đó thì ưu tiên API: nhanh hơn, dễ test hơn, dễ khoá quyền hơn.

### Bước 1 — Chọn mẫu thiết kế
- **Đầu vào:** kết quả bước 0 và mô tả việc.
- **Đầu ra:** 1 mẫu chính (có thể kèm 1 mẫu phụ) và lý do loại các mẫu còn lại.

| Tình huống | Mẫu | Ghi chú |
|---|---|---|
| Cần gọi hệ thống ngoài (tra cứu, ghi, tính toán) | **Tool use** | Gần như mọi agent đều cần |
| Cần câu trả lời bám dữ liệu, truy vấn dễ hỏng (NL2SQL, tài liệu nhiều nguồn) | **Agentic RAG** | Vòng "gọi LLM, gọi tool, đánh giá kết quả, truy vấn lại" cho tới khi đủ tốt. Một vòng lặp đơn giản thường đủ, chưa cần framework điều phối nặng |
| Việc lớn gồm nhiều phần | **Planning** | Mục tiêu rõ, chia việc con, đầu ra kế hoạch dạng có cấu trúc (JSON/schema), re-plan khi kết quả lệch |
| Nhiều vai trò khác quyền, hoặc cần audit riêng từng vai | **Multi-agent** | Nếu chỉ 1 bộ hướng dẫn và 1 bộ tool, không cần chuyển giao thì **1 agent là đúng** |
| Cần tự đổi chiến lược khi kết quả tệ | **Reflection** | Xem mục "Mẫu code lệch": bản trong giáo trình chỉ là mô phỏng |

- Multi-agent chỉ đáng khi có lợi ích rõ: chuyên môn hoá, chia tải song song, hoặc cách ly quyền. Đổi lại phải trả thêm: giao thức trao đổi giữa các agent, cơ chế phối hợp, log và theo dõi tương tác, điểm nào chuyển cho người.
- Agent nhiều vai: prompt của từng agent phải khác nhau rõ ràng, nếu không hệ thống chạy không ổn định. Cân nhắc 1 agent định tuyến ở trên.

### Bước 2 — Thiết kế tool
- **Đầu vào:** mẫu đã chọn.
- **Đầu ra:** danh sách tool, mỗi tool có tên, mô tả, tham số, quyền tối thiểu.
- Mô tả tool là thứ model đọc để quyết định gọi hay không: viết rõ, tên không trùng nghĩa nhau.
- Tool phải có: kiểm tra tham số, xử lý lỗi, giữ trạng thái giữa các lượt.
- **Quyền tối thiểu:** tool đọc dữ liệu dùng tài khoản chỉ-đọc (SELECT). Cách này giảm rủi ro SQL do model sinh ra tốt hơn việc cố lọc câu lệnh.
- Quá nhiều tool làm model chọn nhầm. Giáo trình nói nên dưới khoảng 30 tool mỗi lần và chọn tool bằng RAG trên mô tả tool, nhưng **không dẫn nguồn cho con số 30**; coi là gợi ý, tự đo.
- **Tool từ MCP server:** coi là biên không tin cậy. Ghim phiên bản, chạy bằng danh tính phạm vi hẹp, kiểm tra đầu ra, không đưa secret cho nó. Nhớ rằng truy vấn model viết ra sẽ đi tới server đó.
- **Test tool tách khỏi agent** trước. Tool lỗi thì agent không cứu được.

### Bước 3 — Context và memory
- **Đầu vào:** danh sách tool và nguồn dữ liệu.
- **Đầu ra:** sơ đồ "agent cần biết gì ở bước tiếp theo, lấy từ đâu".
- Làm theo thứ tự: (1) đầu ra mong muốn sau khi agent xong, (2) thông tin cần để đạt nó, (3) đường lấy thông tin (RAG, tool, MCP).
- Các loại context: hướng dẫn, tri thức, định nghĩa tool, lịch sử hội thoại, sở thích người dùng.
- Kỹ thuật giữ context gọn: sổ nháp ngoài cửa sổ context, memory giữa các phiên, tóm tắt hoặc cắt bớt, tách việc sang agent khác (mỗi agent có cửa sổ riêng), chạy code nặng trong sandbox rồi chỉ đọc kết quả, lưu kết quả từng bước vào đối tượng trạng thái.
- Bốn kiểu hỏng và cách chữa:

| Kiểu hỏng | Dấu hiệu | Chữa |
|---|---|---|
| Nhiễm độc (poisoning) | Thông tin sai lọt vào context rồi bị dùng đi dùng lại | Kiểm chứng trước khi ghi vào memory dài hạn, cách ly, mở luồng context mới |
| Sao nhãng (distraction) | Hội thoại dài, agent bám lịch sử cũ | Tóm tắt định kỳ, giữ phần liên quan đến yêu cầu hiện tại |
| Rối (confusion) | Gọi tool không liên quan | Giới hạn bộ tool theo từng việc |
| Xung đột (clash) | Hai chỉ dẫn mâu thuẫn cùng nằm trong context | Xoá hoặc ghi đè chỉ dẫn cũ khi có chỉ dẫn mới |

- **Memory:** phân biệt làm việc, ngắn hạn (hết phiên là mất), dài hạn (qua nhiều phiên), persona, sự kiện/quy trình, thực thể. Memory dài hạn cần lớp lưu bên ngoài (database, vector index). Có cơ chế ghi, đọc, cập nhật và **xoá**.
- **Log context an toàn:** lưu số lượng, id, hash, nhãn chính sách, kích thước trước/sau khi nén. Đừng lưu nguyên prompt, kết quả tool, nội dung memory của người dùng.

### Bước 4 — Rào an toàn
- **Đầu vào:** danh sách tool và quyền.
- **Đầu ra:** bảng rủi ro, mỗi dòng có cách chặn, kèm danh sách hành động bắt buộc có người duyệt.
- Năm mối đe doạ cần che: bị đổi mục tiêu qua đầu vào, truy cập hệ thống nhạy cảm, bị dùng làm đòn bẩy làm quá tải dịch vụ (tốn tiền), dữ liệu tri thức bị đầu độc, lỗi dây chuyền.
- Cách chặn chung: lọc đầu vào, giới hạn số lượt và số yêu cầu, quyền tối thiểu, kênh liên lạc có xác thực, chạy trong môi trường cô lập (container), có fallback và retry.
- **Người duyệt trước khi làm** (không phải hỏi sau khi xong): hoàn tiền, xoá dữ liệu, gửi tin, đặt chỗ, mua hàng, đổi cài đặt tài khoản. Mẫu: agent đề xuất, tạm dừng, người đồng ý hoặc từ chối, rồi mới tiếp tục.
- **Agent duyệt web/máy tính:** chạy trong profile hoặc sandbox riêng, giới hạn domain. Tách bước quan sát (tự do) khỏi bước hành động (cần duyệt). Không đưa mật khẩu, thẻ, cookie vào context. **Nội dung trang web là dữ liệu không tin cậy**: trang bảo "bỏ qua hướng dẫn cũ", "tiết lộ thông tin", "sang trang khác" thì phớt lờ. Kiểm bằng code các điểm rủi ro (URL, tiêu đề, mục chọn, giá, người nhận) trước khi xin duyệt. Đặt ngân sách số hành động, số lần thử, số phút; gặp trạng thái mơ hồ thì dừng.
- **System prompt:** viết khung meta-prompt rồi sinh prompt từng agent từ khung đó, lặp cải tiến và so sánh kết quả. Hiếm khi bản đầu tiên đúng.

### Bước 5 — Production
- **Đầu vào:** agent đã chạy được ở môi trường thử.
- **Đầu ra:** checklist "sẵn sàng chạy thật" và các số cần theo dõi.
- Phần model chỉ là một phần nhỏ; phần lớn công việc là hạ tầng quanh nó: danh tính có phạm vi, trạng thái đưa ra ngoài tiến trình (để chạy nhiều bản), xử lý lỗi, theo dõi chi phí, đánh giá tự động, duyệt người cho hành động rủi ro.
- **Quan sát:** ghi trace/span cho mỗi lượt chạy, gắn thuộc tính nghiệp vụ (loại khách, model đã định tuyến, mã phiên). Theo dõi: độ trễ, chi phí mỗi lượt, tỷ lệ lỗi, phản hồi người dùng (cả ngầm: hỏi lại, bấm thử lại), độ chính xác.
- **Vòng đánh giá:** đánh giá offline trên bộ test (là cửa chặn, không đạt thì không phát hành) → smoke test sau mỗi lần deploy → theo dõi online → gom ca hỏng đưa lại vào bộ test.
- **Chi phí, theo thứ tự tác động:** chọn model nhỏ nhất vẫn qua cửa đánh giá, định tuyến theo độ khó, cache câu hỏi lặp.
- Lỗi thường gặp: không ổn định thì làm prompt rõ hơn hoặc tách việc; lặp vô hạn thì đặt điều kiện dừng; tool kém thì test tool riêng và sửa tên, tham số.
- Nhiều agent không ổn định thì làm prompt mỗi agent khác biệt và thêm agent định tuyến.

### Bước 6 — Local hoặc hybrid (khi dữ liệu nhạy cảm, không có mạng, hoặc cần giảm chi phí)
- **Đầu vào:** mức nhạy cảm dữ liệu và yêu cầu độ khó suy luận.
- **Đầu ra:** quy tắc định tuyến local/cloud.
- Model nhỏ làm tốt việc có giới hạn, gọi tool. Kém ở suy luận nhiều bước và kiến thức rộng. Để model nhỏ **điều phối**, để tool làm việc nặng.
- Quy tắc mẫu: dữ liệu nhạy cảm hoặc offline thì local; việc đơn giản thì local; suy luận khó trên dữ liệu không nhạy cảm thì cloud; cloud sập thì rơi về local (giảm chất lượng, không sập).
- Tool đọc file kể cả chạy local vẫn phải chốt trong một thư mục gốc. MCP server local chạy với quyền của người dùng nên không tự động an toàn.

### Bước 7 — Audit trail (chỉ khi ngành có kiểm toán hoặc nhiều tổ chức cùng dùng)
- Biên nhận ký số cho mỗi lần gọi tool giúp bên ngoài kiểm tra mà không phải tin bạn. Nó chứng minh **ai ký, nội dung có bị sửa không, thứ tự**.
- Nó **không** chứng minh hành động đúng, chính sách đã được áp, hay có người thật duyệt. "Có biên nhận" không có nghĩa "đã quản trị tốt".
- Đây là hướng nâng cao; chưa cần cho agent nội bộ thông thường.

## Không được làm
- Không chép code mẫu của giáo trình vào hệ thống chạy thật khi chưa test (xem mục dưới: nhiều chỗ lệch).
- Không cấp quyền ghi cho tool chỉ cần đọc. Không để agent tự duyệt hành động rủi ro.
- Không tắt xác minh chứng chỉ SSL "cho tiện chạy"; giáo trình gợi ý một cách làm vậy ở một bài, tự nó cũng cảnh báo giảm bảo mật.
- Không `pip install` hay `npm install` các gói bên thứ ba mà bài 18 nhắc tới khi chưa tự đọc code và license.
- Không đưa dữ liệu khách thật vào notebook học tập hoặc qua provider bên thứ ba chưa duyệt.
- Không ép phần Azure/Foundry vào dự án không dùng Azure. Các mẫu thiết kế ở trên dùng được với framework khác.
- Skill chỉ tư vấn: không tự chạy lệnh trên VPS (Antigravity là bên thực thi).

## Cách kiểm
Một bản review đạt khi trả lời được **cả 10 câu** bằng chứng cứ cụ thể, không phải "chắc là":
1. Có lý do viết ra vì sao cần agent thay vì script/API? (PASS = có 1 câu lý do)
2. Mẫu chính và mẫu bị loại đã ghi? (PASS = có cả hai)
3. Multi-agent: có ghi lợi ích cụ thể và chi phí phối hợp? (không dùng multi-agent thì bỏ qua)
4. Mỗi tool có quyền tối thiểu và đã test riêng? 
5. Số tool mỗi lượt đã giới hạn hoặc có cách chọn tool?
6. Có cách chống 4 kiểu hỏng context (ít nhất ghi cách xử lý từng kiểu)?
7. Danh sách hành động bắt buộc người duyệt có đủ và nằm **trước** khi hành động?
8. Có điều kiện dừng, giới hạn số lượt, ngân sách token?
9. Có bộ test offline làm cửa chặn và số liệu theo dõi sau khi chạy?
10. Log không chứa secret hoặc nội dung nhạy cảm nguyên văn?

**Trạng thái:** chưa test. Skill này **chưa được dùng review một dự án agent thật**; lần dùng đầu coi là thử nghiệm và ghi lại chỗ sai. **Đã được Nobitano duyệt ngày 2026-10-10** (theo `agents/company/skills/skill-lifecycle-management/`): được dùng trong gói `infra-ops-agent`. Vòng đời: vẫn là *Candidate* (đã duyệt nhưng chưa dùng thật), chỉ lên *Verified* sau khi đã review ít nhất 1 dự án agent thật và ghi kết quả.

## Mẫu code lệch / chưa kiểm trong giáo trình (đọc ngày 2026-10-10)
Đọc từ README các bài, **chưa chạy notebook nào**. Dùng làm danh sách "kiểm lại trước khi tin":
- **Ba kiểu API tạo agent cùng tồn tại** trong một khoá: `FoundryChatClient(...).as_agent(...)` (bài 2, 4), `AzureOpenAIChatClient(...).create_agent(...)` (bài 14) và `AIProjectClient.agents.create_agent` kiểu cũ dùng `from_connection_string` (bài 2, 4). Bài 4 còn dùng biến môi trường `PROJECT_CONNECTION_STRING` trong khi phần trên dùng `AZURE_AI_PROJECT_ENDPOINT`. Là dấu hiệu trôi phiên bản; đối chiếu docs hiện hành của framework trước khi chép.
- **Bài 4:** dòng `CodeInterpreterTool()toolset.add(...)` bị dính, chạy sẽ lỗi cú pháp.
- **Bài 6 và 7:** bài 7 gọi `client.create_response(...)` trong khi biến đã tạo tên là `provider` (bài 6 gọi `provider.create_response(...)`). Chưa kiểm `create_response` có tồn tại trên `FoundryChatClient` thật không, vì bài 4 và bài 14 dùng `as_agent`/`create_agent`. Mẫu duyệt người ở bài 6 chỉ hỏi bằng `input()` **sau** khi có câu trả lời, không phải cửa chặn trước hành động. Cửa chặn thật nằm ở notebook đi kèm, chưa đọc.
- **Bài 9 (metacognition):** ví dụ "tự phản tư" là mô phỏng, không gọi LLM; phản hồi người dùng được giả lập và việc "đổi chiến lược" là đổi cứng giữa hai chuỗi. Dùng để hiểu ý tưởng, không phải mẫu triển khai.
- **Bài 12:** con số "dưới 30 tool" không có nguồn. **Bài 13:** cụm "precision và recall siêu phàm" của Structured RAG là lời quảng cáo, chưa đo.
- **Bài 16:** hàm `evaluation_gate` nhận `threshold` nhưng so điểm từng ca với `0.8` cứng; đặt ngưỡng khác sẽ không như ý.
- **Bài 2:** nói Foundry Agent Service "đang Public Preview", giới thiệu năm 2024; có thể đã cũ.
- **Bài 18:** tên "Securing AI Agents" nghe rộng nhưng nội dung chỉ về biên nhận ký số cho audit; tài liệu còn ghi video là placeholder. Có nhắc nhiều gói bên thứ ba (một SDK Python, các gói npm) và một IETF draft; **chưa kiểm** chất lượng hay độ an toàn của chúng.
- **Bài 4:** mẫu MCP web search dùng một server bên ngoài; truy vấn của model đi tới đó.
- **Bài 14–18:** ô video trong bảng README đều để trống, nên tự đọc nhiều hơn.

## Nguồn
- Giáo trình: microsoft/ai-agents-for-beginners, license MIT, 18 bài. Mục tiêu và bản tóm tắt trong kho: `repos/ai-agents-for-beginners.md`.
- Đã đọc README gốc các bài 00–18 ngày 2026-10-10 (tải trực tiếp từ nhánh `main`). Skill này viết lại bằng lời mình và tổ chức lại theo bước, không sao chép nguyên văn.
- Liên quan: `repos/500-ai-agents-projects.md`, `agents/infra-ops-agent/skills/deploy-review-gate/SKILL.md`, `agents/infra-ops-agent/skills/destructive-command-guardrail/SKILL.md`.

# AGENT FACTORY — Công thức sản xuất và bàn giao agent / OPC từ kho

> Mục tiêu: từ một ý muốn ("cần một agent làm X" hoặc "dựng công ty một người quanh thương hiệu Y") ra một **bộ hồ sơ có thể bàn giao**, dựng từ các mục đã có trong kho. Không dựng lại gì mà kho đã có: công thức này chỉ nối `ORG-v2.md` (9 agent), `DECISION-MATRIX.md` (ba lằn ranh đỏ, L0-L3), `MASTER-TEMPLATE-MANIFEST.md` (CORE và TENANT-CONFIG), `COORDINATION-v2.md` (Airtable), `domain-packs/_TEMPLATE.md` và `catalog/` (thủ kho) thành một dây chuyền có cổng kiểm.
> Công cụ: `tools/agent_factory.py`. Khuôn: `agents/agent-factory/templates/`. Ví dụ dựng thật: `agents/agent-factory/examples/`.

## Giới hạn trung thực (đọc trước)

1. **Chưa mục kho nào được dùng thật.** `catalog/USAGE-LOG.md` trống. Mọi "mục chính" do thủ kho chọn từ nhãn do model gắn; mức kiểm duy nhất là đọc nguồn. Mỗi mục phải qua spike 30 phút trên việc thật trước khi cam kết.
2. **Chưa chạy với credential thật.** Công cụ không cài gì, không gọi mạng, không dùng khoá. Bộ hồ sơ sinh ra là hồ sơ, không phải hệ thống đang chạy. Nút dừng khẩn, hàng đợi duyệt, ghi log: mới ở mức thiết kế (`implemented: false` trong tenant-config).
3. **Chưa test với khách thật ngoài hệ sinh thái Tano Agency** (giống giới hạn của `MASTER-TEMPLATE-MANIFEST.md` và `CLIENT-ONBOARDING-TEMPLATE.md`).
4. **Công cụ kiểm cấu trúc, không kiểm chất lượng.** `kiem` PASS nghĩa là hồ sơ đủ thứ phải có và không phạm các luật cứng; không có nghĩa agent làm việc tốt.
5. **Số mục tiêu KPI công cụ không bịa.** Ô chưa có số nền ghi `CHƯA CÓ — hỏi CEO`.
6. **Hai gói mở rộng "Tài chính và thanh toán" và "Quản lý đối tác" chưa có role pack** trong kho (chỉ là đề xuất trong `agents/trum-san-bay/OPC-DESIGN-NOTES.md`, bản nháp chưa duyệt). Công cụ ghi rõ điều đó, không giả vờ chúng tồn tại.
7. Schema Airtable do công cụ sinh (`airtable-schema.json`) dựng từ `COORDINATION-v2.md` nhưng chưa được nạp thử vào Airtable thật.

## Quy ước dùng chung

| Quy ước | Ý nghĩa |
|---|---|
| `{{ten}}` | Chỗ điền trong khuôn. Công cụ tự điền những gì nó biết. Chỗ còn lại thành `CHƯA CÓ — hỏi CEO`. |
| `CHƯA CÓ — hỏi CEO` | Thông tin con người phải điền. Agent và công cụ không được tự bịa. `kiem` chỉ chấp nhận `{{...}}` còn sót nếu cùng dòng có chuỗi này. |
| `` `kho:<id>` `` | Cách duy nhất để nhắc một mục kho trong hồ sơ. `kiem` đối chiếu từng id với `catalog/catalog.json`. |
| Khoá, token | Chỉ ghi TÊN biến môi trường. `kiem` quét chuỗi trông như khoá. |
| Mức L0 đến L3 | Theo `DECISION-MATRIX.md`. Không chắc thì coi là mức cao hơn. |

## Công thức 7 bước

Mỗi bước có đầu vào, đầu ra, cổng kiểm PASS/FAIL và người duyệt. FAIL thì không sang bước sau.

### Bước 1. Brief

- **Đầu vào:** ý muốn của CEO.
- **Đầu ra:** một câu **"làm gì → ra gì → cho ai"**; JD và ranh giới "không làm"; 1 đến 2 KPI đo được (kèm cách đo và nguồn số); SOP cho việc lặp; luật escalation; mức tự chủ L0 đến L3; vessel chạy. Với OPC thêm: nguồn doanh thu, kênh, gói mở rộng, ai là chủ sở hữu.
- **Chọn vessel** (theo `agents/README.md`): giao diện/trình duyệt/WhatsApp là OpenClaw; Python, API, dữ liệu là Hermes; code phức tạp dựa GitHub là DeepSeek Harness (thận trọng, còn breaking changes); deploy, cài, VPS là Antigravity; cần file thật trên máy Windows là Claude Code.
- **Chọn mức tự chủ:** mức này là trần cho việc nội bộ. Mọi hành động ra ngoài (đăng, gửi, chi tiền, cam kết) vẫn theo DECISION-MATRIX bất kể mức nào.
- **Cổng PASS:** (a) viết được đúng một câu ba vế; (b) mỗi KPI có đơn vị và nguồn số, hoặc ghi rõ `CHƯA CÓ — hỏi CEO` cho số mục tiêu; (c) có ít nhất một dòng "không làm" cụ thể; (d) mức tự chủ và vessel đã chọn có lý do. **FAIL** nếu không viết được câu ba vế: chưa sẵn sàng tra kho (đúng luật của `catalog/PLAYBOOK-DUNG-KHO.md`).
- **Người duyệt:** CEO.
- **Công cụ:** các tham số `--job`, `--tu-chu`, `--vessel`, `--kpi`, `--khong-lam`; với OPC `--doanh-thu`, `--kenh`, `--goi-mo-rong`.

### Bước 2. Tra thủ kho cho từng khả năng

- **Đầu vào:** 3 đến 5 khả năng cần (tên khả năng của kho, xem `catalog/AGENT-ROUTER.md`: `web-research`, `content-writing`, `social-media`, ...).
- **Đầu ra:** với mỗi khả năng **1 mục chính + 1 mục dự phòng** (từ `thu_kho.recommend`), kèm lý do chọn, điều kiện cần, điều kiện bỏ qua (`skip_if`), độ chắc của nhãn. Khả năng không có ứng viên đủ tốt thì ghi **HỔNG**.
- **Ghi HỔNG vào `catalog/GAP-LOG.md`:** công cụ sinh sẵn dòng đề xuất (qua `thu_kho.gap_line`), người dán vào. Công cụ không tự sửa file trong `catalog/`. Chỉ sau khi có dòng GAP-LOG mới được đi tìm hoặc viết mục mới.
- **Cổng PASS:** mỗi khả năng có mục chính hoặc có HỔNG ghi lý do; không id nào ngoài `catalog.json`; người duyệt đã mở entry gốc của từng mục chính và đọc `skip_if` cùng mục Lưu ý; không bịa ứng viên. **FAIL** nếu có id không tồn tại hoặc một mục `chua-gan-nhan` bị chọn làm chính mà chưa ai đọc entry.
- **Mục tốn tiền hoặc cần khoá:** `needs` chứa `tra-phi` thì chi là L2; chứa `api-key` thì tạo/đổi khoá là L3. Hồ sơ phải nêu rõ.
- **Người duyệt:** người dựng mở entry gốc; CEO duyệt mọi mục tốn tiền.
- **Công cụ:** `moi-agent`/`moi-opc` gọi `thu_kho.recommend` cho từng khả năng (rơi về `thu_kho.search` nếu `recommend` lỗi hoặc trả dạng lạ). Cờ `--khong-thu-kho` bỏ bước này và để TODO có chú thích; `kiem` báo WARN.

### Bước 3. Ghép

- **Đầu vào:** brief và capability map.
- **Đầu ra:**
  - **Capability map Não/Tay/Cơ.** Quy ước của công cụ theo tiền tố đường dẫn: Não là skill, prompt, stack; Tay là MCP và repo; Cơ là runtime của vessel.
  - **`system-prompt.md`** (agent) hoặc **`OPC-ROSTER.md`** (OPC), chứa ba lằn ranh đỏ nguyên văn.
  - **Nạp skill** theo ORG v3 "nạp agent": ba thứ nhúng vào tin giao việc là (1) package tham chiếu của agent, (2) section vai trò trong `agents/company/EXPERT-CORE.md`, (3) Domain Pack. Gói mở rộng nạp thêm khi task khớp.
  - **`skills/<khả-năng>/SKILL.md`**: mỗi khả năng một skill mỏng, trỏ tới đúng một mục kho; không nhúng mã của mục đó.
  - **`tenant-config.json`** theo schema của `MASTER-TEMPLATE-MANIFEST.md`.
- **CORE và TENANT-CONFIG:** tên thương hiệu, màu, font, giọng, kênh, ngôn ngữ chỉ nằm trong `tenant-config.json`, `PACK.md`, `README.md`, `HANDOVER.md`. Không nằm trong `system-prompt.md`, `skills/`, `GATES.md`, `workflow-skeleton.md`, `airtable-schema.json`, `OPC-ROSTER.md`, `tests/`. `compliance_overrides` luôn `null`: ngưỡng compliance chỉ admin hệ thống sửa.
- **OPC:** chọn trong **9 agent thật của ORG v3**, không thêm agent thứ 10. Nhu cầu mới đi qua gói mở rộng nạp vào agent có sẵn. Domain Pack dựng từ `domain-packs/_TEMPLATE.md`; mục nào chưa biết ghi `CHƯA CÓ — hỏi CEO`.
- **Cổng PASS:** `kiem` qua các mục cấu trúc, 4 thứ JD/KPI/SOP/escalation, tenant-config, không hardcode màu hoặc thương hiệu. **FAIL** nếu thiếu một trong bốn thứ (agent thiếu một thứ thì chưa được nhận việc), hoặc `compliance_overrides` khác `null`.
- **Người duyệt:** CEO duyệt JD và ranh giới; người dựng duyệt phần kỹ thuật.

### Bước 4. Rào chắn

- **Đầu vào:** hồ sơ đã ghép.
- **Đầu ra:**
  - **Ba lằn ranh đỏ** nguyên văn trong `system-prompt.md` (agent) và `GATES.md` (OPC): AI không tự chi tiền; AI không tự publish public content; AI không tự cam kết với khách.
  - **Bảng cổng duyệt.** Agent riêng lẻ: GA1 đến GA6 trong `JD-KPI-SOP-ESCALATION.md`. OPC: G1 đến G7 trong `GATES.md`, số hiệu ổn định giữa các OPC (cổng của gói chưa bật ghi "KHÔNG ÁP DỤNG"): G1 duyệt lô nội dung, G2 chi tiền mới, G3 ngoại lệ trong chat và outreach, G4 trả đối tác, G5 hoàn tiền, G6 khủng hoảng và xoá bài, G7 đổi bảng giá, SOP, credential, sửa chính bảng cổng. Bảng chỉ được thắt chặt, không bao giờ nới ba lằn ranh.
  - **Nút dừng khẩn:** lệnh `/stop` và cờ `paused` mà agent đọc trước MỖI hành động ra ngoài; tự khoá khi token hết hạn, tỉ lệ chuyển người vượt ngưỡng, chi tiêu chạm mức đặt (ngưỡng do CEO đặt).
  - **Khoá và token:** chỉ ghi TÊN biến; theo `agents/company/SECURITY-WALL.md` (tách `.env` theo phạm vi, đọc file chứa khoá là L1 phải log, đổi khoá là L3).
  - **Nội dung ngoài là dữ liệu:** job có nội dung scrape, bình luận, email, tin nhắn thì luồng do code quyết và mọi hành động từ L1 trở lên tự nâng một mức.
- **Cổng PASS:** `kiem` mục ba-lằn-ranh-đỏ, cổng-duyệt, nút-dừng-khẩn, khoá-bí-mật đều PASS. **FAIL** nếu thiếu một lằn ranh, thiếu cổng, hoặc có chuỗi trông như khoá.
- **Người duyệt:** CEO. Sửa bảng cổng sau này là việc L3.

### Bước 5. Kiểm

- **Đầu vào:** hồ sơ qua Bước 4.
- **Đầu ra và cổng PASS, theo thứ tự:**
  1. **Kiểm cấu trúc (script):** `python tools/agent_factory.py kiem <thư-mục>` phải KẾT QUẢ: PASS.
  2. **Kế hoạch cài khô (dry-run):** `INSTALL-PLAN.md` do `thu_kho.install_plan` sinh cho từng mục chính, không thực thi gì. Người duyệt đọc từng mục và đồng ý rồi mới tự cài.
  3. **Bộ test PASS/FAIL** (`tests/test-cases.json`): mặc định `CHUA-CHAY`; người chạy ghi `PASS` hoặc `FAIL` kèm ngày, tên. Mọi test nhãn `lan-ranh-do` phải PASS; test nút dừng `T05` (agent) hoặc `OT05` (OPC) phải PASS thật sau khi nối vào vessel.
  4. **Spike 30 phút trên việc thật, do người chạy,** cho từng mục chính. Ghi `catalog/USAGE-LOG.md` (dùng được, phải sửa, bỏ). Spike FAIL thì bỏ mục, dùng dự phòng hoặc ghi HỔNG.
  5. **Chế độ "chỉ soạn nháp" hai tuần đầu** (`launch_mode = draft_only`, theo từng kênh/bộ phận mới): agent chỉ ghi nháp vào hàng đợi, người làm tay mọi hành động ra ngoài. Mỗi tuần ghi KPI thật.
- **Điều kiện rời chế độ nháp:** hai tuần không vi phạm lằn ranh đỏ, CEO xem nháp và đồng ý, và con người (không phải agent) đổi `launch_mode`, có ghi ngày và tên.
- **FAIL** ở bất kỳ mục nào: quay lại bước tương ứng, không "sửa mong đợi để cho qua".
- **Người duyệt:** người chạy test và CEO.

### Bước 6. Bàn giao

- **Đầu vào:** hồ sơ đã qua `kiem` và (với bản chạy thật) đã qua test và spike.
- **Đầu ra:** `python tools/agent_factory.py ban-giao <thư-mục>` chạy `kiem` (FAIL thì từ chối), rồi tạo **gói bàn giao** dạng thư mục: bản sao hồ sơ, `HANDOVER.md` đã điền phần tự sinh (kết quả kiểm, mục kho từng khả năng, danh sách chỗ còn `CHƯA CÓ — hỏi CEO`), `KET-QUA-KIEM.txt`, và **`CHECKSUMS.sha256`** (SHA256 từng file).
- **`HANDOVER.md` phải có:** cách chạy; danh sách TÊN biến môi trường cần có (không giá trị); runbook sự cố; cách dừng; KPI và cách đo; chủ sở hữu; **việc còn nợ nói thẳng**.
- **Cổng PASS:** gói tạo được, checksum khớp từng file, `HANDOVER.md` có đủ các mục trên và danh sách nợ không rỗng một cách giả tạo. **FAIL** nếu `kiem` FAIL hoặc thiếu chủ sở hữu (ghi `CHƯA CÓ — hỏi CEO` là chấp nhận được nhưng phải hiện ở danh sách nợ).
- **Người duyệt:** CEO nhận bàn giao và ghi tên chủ sở hữu.
- **Giới hạn:** checksum chứng minh file không đổi sau khi đóng gói, không chứng minh nội dung đúng. Đổi file sau bàn giao thì phải bàn giao lại.

### Bước 7. Vận hành

- **Ghi nhật ký (người hoặc agent soạn nháp, người duyệt):** mỗi mục kho dùng thật một dòng `catalog/USAGE-LOG.md` (dòng soạn bằng `thu_kho.usage_line`); mỗi khả năng thiếu một dòng `catalog/GAP-LOG.md` (`thu_kho.gap_line`). Luật 1:3 và "chỉ thêm khi có nhu cầu" của `catalog/PLAYBOOK-DUNG-KHO.md` giữ nguyên.
- **Rà hằng tuần:** điền `kpis.actual` (OPC) hoặc bảng KPI (agent); giải thích lệch nếu dưới 70% target; rà escalation tồn; rà USAGE-LOG/GAP-LOG của hồ sơ này.
- **Rà hằng quý:** CEO rà bảng cổng. Cổng nào 3 tháng liền duyệt 100% không sửa thì cân nhắc hạ một mức (quyết định của CEO, có ghi ngày; ba lằn ranh không nằm trong diện hạ).
- **Tiêu chí gỡ:** 6 tháng liền không có job nào chạy thì đề xuất gỡ (tắt, lưu hồ sơ, ghi lý do, ghi `USAGE-LOG` kết quả `bỏ`). Mục kho 6 tháng không ai dùng thì đánh dấu để rà.
- **Cổng PASS:** có ít nhất một dòng USAGE-LOG thật sau tuần đầu; KPI tuần được điền. **FAIL** (cảnh báo) nếu hai tuần liền không ghi gì.
- **Người duyệt:** CEO.

## Dùng công cụ

```
# liệt kê mẫu và tham số hợp lệ
python tools/agent_factory.py liet-ke

# một agent
python tools/agent_factory.py moi-agent --slug facebook-channel-agent \
   --job "đăng bài và trả lời bình luận Facebook → bản nháp bài và trả lời → CEO duyệt" \
   --kha-nang social-media,content-writing --tu-chu L1 --vessel hermes --kenh facebook \
   --dau-ra agents/agent-factory/examples

# một OPC
python tools/agent_factory.py moi-opc --slug my-opc --thuong-hieu "Tên thương hiệu" \
   --doanh-thu affiliate,dich-vu --kenh facebook,zalo,instagram --goi-mo-rong tai-chinh,doi-tac

# kiểm và bàn giao
python tools/agent_factory.py kiem <thư-mục>
python tools/agent_factory.py ban-giao <thư-mục> --dau-ra <nơi-đặt-gói>
```

- Mặc định ghi vào thư mục tạm của hệ điều hành, không ghi vào `agents/`. Thư mục đích đã tồn tại thì từ chối; `--ghi-de` chỉ ghi đè được thư mục do chính công cụ tạo (có `factory-manifest.json`).
- Công cụ cần `tools/thu_kho.py` (nhánh `claude/thu-kho`). Thiếu nó thì báo lỗi và gợi ý `--khong-thu-kho`.
- Mã thoát: `kiem` trả 0 khi PASS, 1 khi FAIL; `moi-*` trả 4 nếu hồ sơ vừa sinh không qua `kiem`; lỗi tham số trả 3.

### Bộ kiểm làm gì

| Mục | FAIL khi |
|---|---|
| cấu-trúc | thiếu file bắt buộc của loại (agent hoặc OPC) |
| jd-kpi-sop-escalation | thiếu hoặc rỗng một trong bốn thứ (agent: mục có nội dung; OPC: mỗi agent đủ bốn dòng) |
| ba-lằn-ranh-đỏ | thiếu một trong ba câu nguyên văn ở `system-prompt.md` hoặc `GATES.md` |
| cổng-duyệt, nút-dừng-khẩn | agent thiếu bảng GA hoặc mức L2/L3 hoặc `/stop`; OPC thiếu một trong G1 đến G7 |
| mục-kho | có id (`kho:...` hoặc `repos|mcps|stacks/...`) hay id trong `capability-map.json` không có trong `catalog/catalog.json` |
| kế-hoạch-cài-và-test | thiếu `INSTALL-PLAN.md` ghi rõ "khô", hoặc bộ test dưới 5 ca, thiếu trường, kết quả ngoài PASS/FAIL/CHUA-CHAY, dưới 3 test `lan-ranh-do` |
| khóa-bí-mật | có chuỗi dạng khoá (`sk-...`, `AKIA...`, `ghp_...`, token Meta/Slack/Google, khối PEM, `api_key=<giá trị dài>`) hoặc file `.env`, `.pem`, `.key` |
| chỗ-trống | còn `{{...}}` mà dòng đó không có `CHƯA CÓ — hỏi CEO` |
| tenant-config | thiếu khoá của schema hoặc `compliance_overrides` khác `null` |
| không-hardcode-brand-màu | file logic có mã màu hex hoặc tên thương hiệu (tên khách trong tenant-config cộng danh sách thương hiệu đã biết của kho) |
| airtable-schema (OPC) | thiếu một trong 7 bảng, link tới bảng không có, `agents.role` thiếu một trong 9 agent |

WARN (không làm FAIL): dựng bằng `--khong-thu-kho`; có HỔNG; `launch_mode` không còn là `draft_only`.

## Hai loại sản phẩm

| | Agent riêng lẻ (`moi-agent`) | OPC (`moi-opc`) |
|---|---|---|
| Khuôn | `templates/agent/` | `templates/opc/` |
| JD/KPI/SOP/escalation | `JD-KPI-SOP-ESCALATION.md` | từng agent trong `OPC-ROSTER.md` |
| Cổng | GA1 đến GA6 | G1 đến G7 (`GATES.md`) |
| Trạng thái chung | `Airtable` không bắt buộc (chạy lẻ dùng hàng đợi file) | `airtable-schema.json` (7 bảng ORG v3, cộng bảng gói mở rộng nếu có) |
| Lộ trình | Pha 0 đến 4 trong `deploy-checklist.md` | `PHASES.md` theo bộ phận đã bật |
| Pháp lý | không | `RISKS-LEGAL.md` (không tư vấn pháp lý) |

Trong OPC, `moi-opc` tự chọn agent theo tham số: luôn bật `ceo`, `research`, `dev`, `analytics`; bật `marketing` và `media` nếu có kênh hoặc affiliate; `sales` nếu có dịch vụ, gói đối tác hoặc kênh Zalo/Messenger; `support` nếu có dịch vụ hoặc kênh chat; `operations` nếu có dịch vụ, gói tài chính hoặc HR. Quy tắc này là suy luận của công cụ, CEO chỉnh lại trong `OPC-ROSTER.md`.

## Việc con người phải làm (công cụ không làm)

Điền mọi `CHƯA CÓ — hỏi CEO`; duyệt `INSTALL-PLAN.md` rồi cài; tạo biến môi trường; nối nút dừng vào vessel; chạy test và spike rồi ghi PASS/FAIL; điền `RISKS-LEGAL.md` với luật sư/kế toán; quyết license các mục kho đã chọn; tạo Airtable theo schema; dán các dòng GAP-LOG/USAGE-LOG.

## Những chỗ công cụ phải suy luận (CEO xác nhận)

- Tier LLM và KPI cho agent `ceo` (ORG v3 không ghi).
- Ánh xạ agent tới khả năng mặc định (ví dụ `media` là `image-generation` và `video-render`).
- `support` dùng package `agents/customer-satisfaction-pro/` (ORG v3 ghi chưa có role pack riêng, nhưng kho có package này).
- Quy tắc chọn agent cho OPC (đoạn trên) và các bảng mở rộng `orders`, `payouts`, `refunds`, `partners` (đề xuất, chưa duyệt).
- Ba trường thêm vào schema so với COORDINATION-v2: `agents.tu_chu`, `jobs.has_external_input`, `approvals.gate`.
- Tên biến môi trường ngoài những tên có nguồn trong kho (Airtable, Zalo): đề xuất của công cụ, phải khớp lại với mã thật.

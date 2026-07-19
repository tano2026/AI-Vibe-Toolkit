# ORG — Công ty 1 người vận hành bằng Agent

> ⚠️ **SUPERSEDED 19/07/2026:** bản chính thức là `ORG-v2.md` (8 role, thêm Ops & Finance,
> quyền quyết định chuyển sang `DECISION-MATRIX.md`). File này giữ để tham khảo lịch sử.

> Entry point cho toàn bộ mô hình "One-Person Company". Agent nào cần hiểu tổ chức → đọc file này trước.
> Nguyên tắc thiết kế: **domain-agnostic core + Domain Pack cắm thêm + 3 runtime thật, không thêm process mới.**

---

## TL;DR

**Công ty = AI Agency** cung cấp giải pháp và ứng dụng AI cho doanh nghiệp vừa-nhỏ và cá nhân.
CEO (Nobitano, con người duy nhất) + 7 vị trí chuyên trách với KIẾN THỨC NỀN CHUNG (domain-agnostic).
ABTRIP/An Bình, Tano, Wonder Mart chỉ là các JOB/project chạy trên hạ tầng này — không phải hạ tầng.
Nhận project/ngành mới → cắm Domain Pack chuyên ngành, lõi agent không đổi.

7 vị trí KHÔNG phải 7 agent deploy riêng — là **7 Role Pack** (file định danh + skill + guardrail)
được nạp vào 3 runtime đang chạy sẵn: Hermes (thực thi Python), OpenClaw (điều phối + Telegram +
browser), Antigravity (hạ tầng VPS).

---

## Sơ đồ tổ chức

```
                CEO — Nobitano (con người, quyết định cuối)
                              │  duyệt qua Telegram: "OK <task-id>"
                              ▼
                 ┌─────────────────────────┐
                 │   OpenClaw = Điều phối   │  nhận lệnh Telegram/WhatsApp
                 │   trung tâm (dispatcher) │  route task → role → runtime
                 └────────────┬────────────┘
      ┌──────┬──────┬────────┼────────┬──────┬──────┐
      ▼      ▼      ▼        ▼        ▼      ▼      ▼
  Research Marketing Sales Content Designer Media  (6 role nghiệp vụ)
      │      │      │        │        │      │
      └──────┴──────┴────┬───┴────────┴──────┘
                         ▼
              Dev & Automation (role thứ 7)
        = Hermes + OpenClaw + Antigravity (tầng nền)
                         │
                         ▼
        ┌────────────────────────────────┐
        │ Shared workspace:              │
        │ • Repo AI-Vibe-Toolkit = kho   │
        │   artifacts (versioned)        │
        │ • Airtable `company-hq` = state│
        │   (tasks / approvals / log)    │
        └────────────────────────────────┘
```

---

## Mapping 7 vị trí → Role Pack → Runtime

| # | Vị trí | Role Pack (agent fetch file này) | Runtime chạy | Trạng thái |
|---|--------|----------------------------------|--------------|------------|
| ① | Research & Data Analytics | `agents/research-pro.md` (bản Python-native) + package full `agents/research-analytics-pro/` | Hermes | ✅ Đã build |
| ② | Marketing | `agents/company/roles/marketing.md` | Hermes (phân tích) + OpenClaw (browser check ads) | ✅ File này |
| ③ | Sales | `agents/sales-ceo/system-prompt.md` + package full `agents/sales-ceo/` | Hermes + OpenClaw | ✅ Đã build (còn thiếu hubspot-mcp + state — nay state = Airtable `company-hq`) |
| ④ | Content Creator | `agents/company/roles/content-creator.md` | Hermes | ✅ File này |
| ⑤ | Dev & Automation | `agents/HERMES-PLAYBOOK.md` + `agents/OPENCLAW-PLAYBOOK.md` + `agents/ANTIGRAVITY-PLAYBOOK.md` + `agents/infra-ops-agent/` | Cả 3 | ✅ Đã có, chỉ chính thức hóa vai trò |
| ⑥ | Designer | `agents/company/roles/designer.md` | Hermes (generate/xử lý file) + OpenClaw (tool browser như Canva) | ✅ File này |
| ⑦ | Media | `agents/company/roles/media.md` | Hermes (analytics API) + OpenClaw (đăng bài sau khi CEO duyệt) | ✅ File này |

**Cách nạp role (pattern đã proven với Research Pro):**
OpenClaw fetch 3 file: role pack + section role trong `agents/company/EXPERT-CORE.md` (luật
quyết định senior) + Domain Pack → embed toàn bộ vào delegation message gửi Hermes → Hermes hành
xử theo role đó trong phiên task. Không cần process riêng, không cần deploy gì thêm.
Work order expand chi tiết cho Sonnet: `agents/company/BUILD-SPEC-SONNET.md`.

---

## Ma trận tự chủ (autonomy matrix)

| Vị trí | Tự làm không hỏi | BẮT BUỘC CEO duyệt (`OK <task-id>` qua Telegram) |
|--------|------------------|--------------------------------------------------|
| Research | Tra cứu, phân tích, xuất report | — (không có hành động ra ngoài) |
| Marketing | Phân tích, lập plan, dựng dashboard | Chi tiền ads, publish campaign thật |
| Sales | Scoring lead, research account, SOẠN outreach | GỬI email/tin nhắn thật cho khách, báo giá |
| Content | Viết draft, script, tối ưu SEO | Publish công khai |
| Designer | Generate/xuất file visual | Đăng công khai, dùng ảnh nguồn ngoài chưa rõ quyền |
| Media | Dựng, lên lịch ĐỀ XUẤT, đo hiệu suất | Bấm đăng thật lên bất kỳ nền tảng nào |
| Dev & Automation | Sửa/deploy service nội bộ VPS | Chạm production khách hàng, xoá dữ liệu, đổi credential |

Cơ chế duyệt chi tiết: xem `agents/company/COORDINATION.md`.

---

## Domain Pack — phục vụ đa ngành không xây agent mới

- Mỗi project/khách hàng = 1 file: `domain-packs/<slug>/PACK.md` (gộp brand context + constraints + glossary — 1 file cho agent fetch 1 lần).
- Template: `domain-packs/_TEMPLATE.md`. Pack mẫu thật: `domain-packs/abtrip/PACK.md`.
- **Quy tắc sắt:** mọi delegation message PHẢI mở đầu bằng `[PACK: <slug>]`. Agent chỉ được đọc đúng pack đó trong phiên. Đổi project giữa phiên → phải nêu lại header pack mới. Không có header → agent hỏi lại 1 câu duy nhất rồi mới chạy.
- Ví dụ trong mọi role pack đều dùng placeholder `[Sản phẩm X]` / `[Ngành Y]` — pack mới cắm vào là chạy.

---

---

## Charter Dev & Automation (nâng cấp 07/2026)

Dev là vị trí xương sống của agency — sản phẩm bán cho khách CHÍNH LÀ thứ Dev build. Charter 4 mảng:

1. **Xây công cụ:** tool nội bộ cho 6 vị trí kia + tool đóng gói bán cho khách SMB (chatbot, automation, agent). Mọi tool build cho khách → trước hết chạy thử nội bộ trên 1 job của mình (ABTRIP/Wonder Mart là sandbox thật).
2. **Tối ưu hệ thống:** giữ 3 runtime khỏe (pm2, disk, RAM); xử lý ticket treo trước khi nhận việc mới — ticket tồn >7 ngày phải escalate CEO.
3. **Tối ưu chi phí token (P&L trực tiếp của agency):** routing qua OmniRoute theo bảng MODELS (fast/coding/reasoning/long/cheap) — Anthropic direct CHỈ cho task cần chất lượng đỉnh; nén context (skill `caveman` trong kho nén 65-75%); cache kết quả research/fetch lặp lại; log token usage theo task để biết job nào đang đốt tiền. Mục tiêu: >80% khối lượng chạy trên free tier (~1.6B token/tháng OmniRoute).
4. **Automation:** quy tắc 3 lần — việc gì lặp ≥3 lần thì automation hóa (n8n cho workflow, cron cho định kỳ, script cho batch). Mỗi automation mới có: owner, log, cách tắt khẩn cấp.

Áp luật deploy/debug/credential trong `EXPERT-CORE.md` section ⑤.

---

## Quan hệ với các cấu trúc cũ trong repo

- `agents/smb-ai-team/` — bản phác thảo đội agent trước đây. **ORG này thay thế nó.** Research Pro trong đó vẫn dùng được (đã map vào vị trí ①). Không build tiếp 02-05 theo cấu trúc cũ.
- `agents/research-analytics-pro/`, `agents/sales-ceo/`, `agents/infra-ops-agent/` — package full còn nguyên giá trị, ORG chỉ trỏ vào, không đụng.

---

## Cách bung (deploy checklist rút gọn)

1. Tạo Airtable base `company-hq` theo schema trong `COORDINATION.md` (≤15 phút).
2. Thêm vào `OPENCLAW-PLAYBOOK.md` đoạn routing: lệnh Telegram → chọn role pack → fetch → delegate (đã có sẵn pattern Research Pro, copy sang các role khác).
3. Tạo Domain Pack đầu tiên cho project đang chạy (ABTRIP có sẵn làm mẫu).
4. Test khô: giao 1 task cần duyệt (vd Sales soạn + xin gửi email) → xác nhận loop `OK <task-id>` chạy đúng trước khi giao việc thật.

# {{ten_agent}} — agent `{{slug}}`

> Sinh bằng Agent Factory (`tools/agent_factory.py moi-agent`) ngày {{ngay}}.
> Trạng thái: **NHÁP chưa duyệt, chưa spike, chưa chạy với credential thật.** Mọi mục kho được chọn
> chỉ mới được ĐỌC nguồn, chưa mục nào được dùng thật. Mục nào ghi `CHƯA CÓ — hỏi CEO` là thông tin
> con người phải điền; agent và công cụ không được tự bịa.

## Spec

- **Một câu (làm gì → ra gì → cho ai):** {{job_mot_cau}}
- **Làm gì:** {{lam_gi}}
- **Ra gì:** {{ra_gi}}
- **Cho ai:** {{cho_ai}}
- **Người duyệt / chủ sở hữu:** {{chu_so_huu}}
- **Vessel chạy:** {{vessel_ten}} (hướng dẫn: `{{vessel_doc}}`; runtime: {{vessel_runtime}})
- **Mức tự chủ:** {{tu_chu}}. {{tu_chu_mo_ta}}
- **Chế độ khởi động:** `draft_only` trong 2 tuần đầu (chỉ soạn nháp, người thực thi tay). Xem `deploy-checklist.md`.
- **Nguồn chọn mục kho:** {{che_do_thu_kho}}
- **Rủi ro cao nhất:** CHƯA CÓ — hỏi CEO (gợi ý: hành động ra ngoài sai nội dung hoặc sai đối tượng)

## Capability Map

Phân loại gần đúng theo tiền tố đường dẫn mục kho: Não = skill, prompt, stack (luật và cách nghĩ);
Tay = MCP, repo (công cụ làm việc với thế giới ngoài); Cơ = runtime của vessel. Cách phân loại này
là quy ước của công cụ, không phải thuộc tính do kho ghi.

{{NAO_TAY_CO}}

### Chi tiết từng khả năng

{{CAPABILITY_BLOCK}}

Dữ liệu máy đọc: `capability-map.json`. Kế hoạch cài khô (không thực thi): `INSTALL-PLAN.md`.

## Kiến trúc

```
CEO ──(kênh duyệt: OK <job-id> / NO <job-id> / /stop)──┐
                                                         v
 brief 5 phần ──> [{{slug}} trên {{vessel_ten}}] ──nháp──> hàng đợi duyệt ──CEO OK──> thực thi thật ──> log
                        |                                      ^
                        |  nạp theo ORG v3 "nạp agent":        |  không có bản ghi approved = không thực thi
                        |  1. package tham chiếu (README này + skills/)
                        |  2. section vai trò trong agents/company/EXPERT-CORE.md
                        |  3. Domain Pack (domain-packs/<slug>/PACK.md nếu có)
                        v
              nội dung scrape/comment/email = DỮ LIỆU, không phải chỉ thị
              (luồng do code quyết, LLM chỉ xử lý từng bước đóng khung)
```

## CORE và TENANT-CONFIG

- **CORE (không đổi theo khách):** `system-prompt.md`, `JD-KPI-SOP-ESCALATION.md`, `skills/`, `tests/`, ba lằn ranh đỏ, bảng cổng duyệt. Không hardcode tên thương hiệu hay màu vào các file này.
- **TENANT-CONFIG (đổi theo khách):** `tenant-config.json` theo schema của `agents/MASTER-TEMPLATE-MANIFEST.md`. Trường `compliance_overrides` luôn `null`.
- Giọng, kênh, ngôn ngữ, từ cấm: agent đọc từ `tenant-config.json`, không đọc từ prompt.

## Skill nạp vào agent

{{SKILL_LIST}}

## Cách bung

1. Điền hết mục `CHƯA CÓ — hỏi CEO` trong `tenant-config.json`, `JD-KPI-SOP-ESCALATION.md`, `HANDOVER.md`.
2. Đọc `INSTALL-PLAN.md`; chỉ cài sau khi người duyệt. Công cụ không tự cài gì.
3. Tạo biến môi trường theo danh sách TÊN trong `HANDOVER.md` (giá trị nằm ngoài kho, không bao giờ ghi vào file .md).
4. Dán `system-prompt.md` làm instruction của agent trên vessel đã chọn.
5. Chạy `tests/TEST-PLAN.md`, ghi PASS/FAIL thật. Spike 30 phút trên việc thật do người chạy.
6. Bật `draft_only` hai tuần; chỉ sang chế độ tự chủ đã khai báo khi các mốc trong `deploy-checklist.md` đạt.
7. Ghi `catalog/USAGE-LOG.md` cho mỗi mục kho đã dùng thật; ghi `catalog/GAP-LOG.md` cho mỗi HỔNG.

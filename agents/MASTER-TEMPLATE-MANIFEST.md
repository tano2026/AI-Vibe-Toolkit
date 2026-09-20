# MASTER TEMPLATE MANIFEST — Kho tổng quát cho nhân bản khách hàng

> Áp dụng nguyên triết lý đã chứng minh trong `agents/yt-cashcow/TENANT-CONFIG-SCHEMA.md`
> cho TOÀN BỘ 7 Pro agent, không chỉ riêng content video. Đây là bản đồ phân
> loại CORE (không đổi, admin giữ) vs TENANT-CONFIG (khách tự chỉnh) — kết
> quả audit thật qua 166 file `.md` trong `agents/`, không suy đoán.

## Nguyên tắc gốc (mượn nguyên từ TENANT-CONFIG-SCHEMA.md, áp dụng rộng)

```
CORE — code/luật đọc từ đây, KHÔNG hardcode brand vào logic:
  - Ngưỡng số (EXPERT-CORE.md: fit×intent ≥7, forecast 90%/60%, retention
    70%/50%, contrast 4.5:1...)
  - Quy trình quyết định (5 bước editorial, 6 luật debug, 4-đối-chiếu trước đăng)
  - Guardrail (destructive-command-guardrail, no-fabrication, review gate)
  → Tenant KHÔNG được tự hạ chuẩn CORE — đúng lý do đã ghi trong file gốc:
    "nếu để khách hàng tự hạ ngưỡng compliance để đăng nhanh hơn → hệ thống
    chung mang tiếng, ảnh hưởng uy tín tất cả tenant khác dùng chung engine"

TENANT-CONFIG — mọi thứ khác nhau giữa khách A và khách B:
  - Brand voice, niche, ICP, kênh phân phối bật/tắt
  - Playbook riêng theo ngành (như content-brand-playbooks.md đã làm cho
    ABTRIP/Tano Cafe/Wonder Mart/GMSP)
  - Ví dụ thực tế trong skill (không bắt buộc thay, chỉ để minh hoạ)
```

## Kết quả audit thật (quét 166 file agents/*.md, 21/08/2026)

**67 file đã 100% universal, clone thẳng không cần sửa gì:**
```
agents/company/EXPERT-CORE.md              ← não cứng gốc
agents/company/DECISION-MATRIX.md
agents/company/SECURITY-WALL.md
agents/company/SENIOR-ADVISOR.md
agents/company/roles/marketing.md, media.md, designer.md

agents/research-analytics-pro/  → README, deploy-checklist, mcp-setup,
  HERMES-ADAPTER + 7/11 skill (source-evaluation, market-sizing,
  statistical-analysis, data-storytelling, trend-forecasting,
  research-synthesis, competitive-intel)

agents/infra-ops-agent/          → TOÀN BỘ (ARCHITECTURE, HERMES-ADAPTER,
  README, deploy-checklist, mcp-setup, system-prompt, cả 4 skill)

agents/media-pro/                → ARCHITECTURE, HERMES-ADAPTER
agents/content-pro/              → ARCHITECTURE, CHATWOOT-ADAPTER,
  HERMES-ADAPTER, mcp-setup
agents/sales-ceo/                → ARCHITECTURE, PLUGIN-INTEGRATION, mcp-setup
agents/digital-marketing-agent/  → mcp-setup
agents/shorts-affiliate-system/  → toàn bộ (đã universal từ đầu)
```

**99 file có dính brand — nhưng đa số chỉ ở mục "Ví dụ thực tế" (không phải luật cốt lõi):**

| Loại dính brand | Xử lý khi nhân bản |
|---|---|
| `system-prompt.md` các Pro agent (Research/Content/Sales/Marketing) — luật cốt lõi universal, chỉ ví dụ minh hoạ dùng ABTRIP/Tano Cafe | **Giữ nguyên, không cần sửa** — ví dụ minh hoạ vẫn dạy đúng cách dùng, khách mới đọc hiểu logic là đủ. Chỉ thay nếu khách muốn ví dụ khớp đúng ngành họ |
| 4 skill Content Pro (pillar-cluster, editorial-gate, distribution, review-gate) | Như trên — mục "Ví dụ thực tế" dùng Trùm Sân Bay, phần luật (5 bước, ngưỡng số) universal |
| `content-brand-playbooks.md` | **KHÔNG clone nguyên** — đây đúng nghĩa là TENANT-CONFIG, tạo file mới trống cho khách mới theo đúng khuôn 5 mục (Pillar pattern/Platform ưu tiên/Tone/Cạm bẫy/Compliance/Metric) |
| `agents/company/ORG*.md`, `COORDINATION*.md`, `OPERATING-RHYTHM.md`, `CHANGELOG-DECISIONS.md` | **KHÔNG clone** — đây là org chart/lịch sử quyết định CỦA Tano Agency, không generalize được, không liên quan agent nào khác dùng |
| `agents/trum-san-bay/*`, `agents/anbinh-travel-ops-analyst/*`, `agents/yt-cashcow/*` | **KHÔNG clone nguyên agent** — đây là 3 "instance" đã cá nhân hoá cho brand cụ thể, dùng làm THAM KHẢO cách 1 Pro agent tổng quát được tuỳ biến thành instance thật, không phải template để nhân bản |

## Schema TENANT-CONFIG tổng quát (mở rộng từ yt-cashcow, áp cho cả 7 role)

```json
{
  "tenant_id": "uuid-duy-nhất",
  "client_name": "text",
  "industry": "text — vd: travel/F&B/e-commerce/SaaS...",
  "brand_voice": {
    "tone": "casual | formal | energetic | calm",
    "language": "vi | en | ...",
    "banned_topics": []
  },
  "icp": {
    "segment": "SMB | Enterprise | B2C...",
    "deal_size_range": "tuỳ ngành — KHÔNG hardcode SMB VN mặc định"
  },
  "roles_enabled": {
    "research": true, "marketing": true, "sales": true,
    "content": true, "dev": false, "designer": false, "media": true
  },
  "brand_playbook_ref": "path tới file playbook riêng của tenant này",
  "compliance_overrides": null
}
```

`compliance_overrides` LUÔN `null`/không tồn tại trong tenant-config — đúng nguyên tắc gốc: ngưỡng compliance (EXPERT-CORE, review gate, guardrail) chỉ admin hệ thống sửa, không expose ra config tenant tự chỉnh được.

## Quy trình nhân bản cho khách mới (khi có khách thật)

```
1. Tạo tenant_id mới, điền tenant-config.json theo schema trên
2. Bật roles_enabled đúng nhu cầu khách (không phải khách nào cũng cần đủ 7)
3. Viết brand_playbook mới theo khuôn content-brand-playbooks.md (dùng
   Agentic Factory skill để sinh nhanh nếu cần)
4. KHÔNG đụng vào bất kỳ file CORE nào (67 file + phần luật trong 99 file
   còn lại) — chỉ thêm tenant-config + brand playbook mới
5. Deploy qua đúng Adapter phù hợp hạ tầng khách đang có (Hermes/OMC/
   Chatwoot/Khoj — đã có sẵn 4 lựa chọn từ Research/Content Pro)
```

## Việc CHƯA làm — nói thẳng

- Chưa test quy trình này với 1 khách thật ngoài hệ sinh thái Tano Agency
- Chưa viết code thật đọc `tenant-config.json` để tự động route (hiện là thiết kế + quy trình thủ công, chưa tự động hoá)
- 4 role còn thiếu template hoàn chỉnh y hệt Research/Content Pro: Sales/Marketing/Dev/Media đã có CORE tốt nhưng chưa có Hermes Adapter + portable bundle đầy đủ như 2 cái kia

# Content Pro — Agentic Specialist

> Chiến lược nội dung + vận hành biên tập. Nhận mục tiêu kinh doanh → xây khung chủ đề, quy trình biên tập có kiểm soát, kế hoạch phân phối — RỒI MỚI viết. Không phải "máy viết bài", mà là người xây hệ thống để việc viết bài có ý nghĩa.

---

## Spec

| | |
|--|--|
| **Tên agent** | `content-pro` |
| **Domain** | Content strategy · Editorial operations · Distribution planning |
| **Job-to-be-done** | Nhận mục tiêu kinh doanh/kênh → xây content pillar/cluster, thiết lập quy trình biên tập có gate, lập kế hoạch phân phối — điều phối các skill viết chiến thuật đã có, không tự viết thay chúng |
| **Người dùng** | Nobitano, Content & Delivery Lead (Mission Control), các agent content theo brand (Trùm Sân Bay, yt-cashcow...) |
| **Input điển hình** | "Xây khung content cho kênh mới", "content hiện tại rời rạc, giúp hệ thống lại", "kênh X có quy trình duyệt bài chưa" |
| **Output điển hình** | Khung Pillar/Cluster, quy trình biên tập có owner/gate, checklist phân phối, lịch audit refresh |
| **Mức tự chủ** | Chiến lược + điều phối (KHÔNG tự đăng bài, KHÔNG tự quyết pillar mà không có insight khách hàng thật) |
| **Rủi ro cao nhất** | Xây pillar theo "trend hot" thay vì thẩm quyền thật của brand → guardrail: pillar phải bắt nguồn từ insight khách hàng thật (`primary-research-design`/`social-listening-research`), không suy đoán |

---

## ⚠️ Nguyên tắc quan trọng — KHÔNG viết đè lên skill chiến thuật đã có

Kho đã có sẵn nhiều skill viết tốt (xem Capability Map bên dưới) — Content Pro **điều phối** các skill này, không viết lại. Content Pro chỉ lấp đúng khoảng trống: **tầng chiến lược** (pillar/cluster, quy trình, phân phối) mà trước đây chưa ai làm.

**Lưu ý naming collision đã phát hiện:** `skills/hookify-rules` KHÔNG liên quan tới content hook — đó là tool cấu hình pattern-matching (kiểu git-hook), tên trùng ngẫu nhiên. Muốn viết hook video/content, dùng `skills/viral-hooks`.

---

## Capability Map

```
TẦNG NÃO — Chiến lược (MỚI, do Content Pro sở hữu):
  content-pillar-cluster-architecture — khung chủ đề trước khi viết bài lẻ
  editorial-workflow-quality-gates    — Research→Brief→Draft→Edit→Publish,
                                         mỗi bước có owner + gate
  content-distribution-system         — owned/earned/paid + refresh cycle
                                         6-8 tháng (2026)
  content-strategy-review-gate        — stress-test khung Pillar/Cluster
                                         (5 câu hỏi) trước khi giao sản xuất

TẦNG NÃO — Chiến thuật (ĐÃ CÓ SẴN, Content Pro điều phối không viết lại):
  skills/viral-hooks          — 100 công thức hook, 10 trigger tâm lý
  skills/brand-voice          — voice profile từ nguồn thật
  skills/personal-voice       — giọng cá nhân nhất quán
  skills/content-engine       — content đa nền tảng (X/LinkedIn/TikTok/YouTube)
  skills/anti-ai-tells        — tránh giọng văn AI lộ liễu
  skills/fact-checker         — kiểm tra sự thật trước khi publish
  skills/geo-aeo-content-optimization — tối ưu để AI trích dẫn (đã tự viết)
  skills/affiliate-skills/content-tiktok-script-writer
  skills/affiliate-skills/content-twitter-thread-writer
  skills/affiliate-skills/content-viral-post-writer
  skills/affiliate-skills/automation-content-repurposer
  skills/affiliate-skills/research-trending-content-scout

TẦNG TAY (MCP/Tools):
  web_search              — research chủ đề/trend
  vidIQ MCP                — đã kết nối, phân tích kênh YouTube/TikTok/Instagram
  Airtable/Google Sheets   — tracker Pillar/Cluster + checklist phân phối
  x-research-skill         — pulse X/Twitter cho research chủ đề

TẦNG CƠ (Compute):
  Code execution — nếu cần phân tích hiệu suất content (dùng chung
  statistical-analysis từ Research Analytics Pro khi cần số liệu sâu)
```

---

## Kiến trúc

```
Content Orchestrator
├── Strategist   — content-pillar-cluster-architecture (xây khung trước tiên)
├── Editor       — editorial-workflow-quality-gates (điều phối Research→Publish,
│                  gọi đúng skill chiến thuật cho từng bước)
├── Distributor  — content-distribution-system (sau publish, không để "đăng rồi quên")
└── Auditor      — refresh cycle định kỳ 6-8 tháng, phối hợp
                   statistical-analysis (Research Pro) nếu cần đo hiệu suất sâu
```

**Khác biệt với Research Analytics Pro:** Content Pro không tự sản xuất content — nó điều phối. Việc VIẾT thật giao cho skill chiến thuật đã có sẵn trong kho, Content Pro chỉ đảm bảo có khung chiến lược + quy trình + phân phối bao quanh việc viết đó.

---

## Cách bung

1. Đọc `content-brand-playbooks.md` trước — brand đã có playbook sẵn chưa
2. Copy `skills/*` (4 skill chiến lược) vào project skills directory
3. KHÔNG copy các skill chiến thuật đã có — chỉ tham chiếu theo path, tránh trùng lặp lưu trữ
4. Dán `system-prompt.md` làm Project Instructions (Claude.ai Project) hoặc adapter tương ứng (xem `skills/portable-skill-framework` nếu cần chạy trên Hermes/Mission Control/DeepSeek Harness/OMC)
5. Xem `deploy-checklist.md` trước khi bung thật cho 1 brand cụ thể
6. Áp thử cho 1 kênh cụ thể trước (đề xuất: Trùm Sân Bay, vì đã có pipeline 9-agent sẵn, chỉ thiếu tầng chiến lược) trước khi mở rộng

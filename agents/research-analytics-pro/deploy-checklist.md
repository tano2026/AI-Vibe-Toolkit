# Deploy Checklist — Research Analytics Pro

Làm đúng thứ tự này trước khi giao việc thật cho agent.

---

## Phase 1 — Setup (30 phút)

- [ ] **Copy skills** vào project
  ```bash
  cp -r skills/ .claude/skills/research-analytics-pro/
  ```

- [ ] **Bật MCP Tier 1** (3 cái bắt buộc)
  - [ ] Brave Search MCP → test: `/brave_web_search "AI market Vietnam 2026"`
  - [ ] Firecrawl MCP → test: `/firecrawl_scrape url="https://example.com"`
  - [ ] MarkItDown MCP → test: upload 1 file PDF nhỏ, kiểm tra output markdown

- [ ] **Dán system-prompt.md** vào Project Instructions của Claude project

- [ ] **Tạo thư mục output**
  ```bash
  mkdir research-outputs
  ```

---

## Phase 2 — Test 3 case trước khi dùng thật

### Test Case 1 — Quick Fact (L0, kiểm tra search cơ bản)
```
Input: "Thị trường AI Việt Nam 2025 trị giá bao nhiêu?"
Expected output:
  ✅ Có số liệu + nguồn cụ thể (không bịa)
  ✅ Nếu không tìm được → nói rõ "không tìm được số chính xác" + estimation logic
  ✅ Trả lời trong <2 phút
  ❌ FAIL nếu: claim số không có nguồn, hoặc bịa nguồn
```

### Test Case 2 — Research Report (L2, kiểm tra multi-source)
```
Input: "Phân tích thị trường SaaS cho SME ở Đông Nam Á — ai đang lead, trend gì, cơ hội nào"
Expected output:
  ✅ Có ≥3 nguồn độc lập được trích dẫn
  ✅ Có section rõ ràng: players, trends, opportunities
  ✅ Source reliability được label
  ✅ Kết bằng ≥3 khuyến nghị hành động cụ thể
  ❌ FAIL nếu: chỉ 1 nguồn, không có khuyến nghị, hoặc dump data không có insight
```

### Test Case 3 — File Upload + Analysis (kiểm tra MarkItDown)
```
Input: Upload 1 file Excel/PDF báo cáo ngành + "Phân tích file này và cho tao biết 3 insight quan trọng nhất"
Expected output:
  ✅ Đọc được nội dung file
  ✅ Identify đúng loại data trong file
  ✅ Ra ≥3 insight có số liệu từ file
  ❌ FAIL nếu: không đọc được file, hoặc hallucinate nội dung không có trong file
```

---

## Phase 3 — Tuning nếu test fail

| Vấn đề | Fix |
|--------|-----|
| Agent bịa số | Thêm vào system-prompt: "Trước khi cite bất kỳ số nào, kiểm tra lại trong web search output mày đã nhận được" |
| Output quá dài/dump data | Trigger skill `data-storytelling` rõ hơn trong prompt |
| Không triangulate nguồn | Thêm explicit instruction: "Mày KHÔNG ĐƯỢC claim số liệu nếu chỉ có 1 nguồn" |
| Slow / tốn token | Xem `skills/token-efficient-research.md` → áp Rule 1-3 |
| Không nhớ context cũ | Enable Mem0 (Tier 3) |

---

## Phase 4 — Enable Power-ups (optional)

- [ ] **x-research-skill** → bật nếu cần research Twitter/X
- [ ] **Mem0** → bật nếu dùng agent regular, muốn nó nhớ context
- [ ] **Sequential Thinking MCP** → bật nếu hay giao task L3-L4
- [ ] **Google TimesFM** → bật nếu có historical time-series data cần forecast

---

## Checklist maintenance (hàng tháng)

- [ ] Check Brave Search API usage → upgrade nếu gần limit
- [ ] Review research outputs → có pattern nào agent hay sai không?
- [ ] Update system-prompt nếu tìm ra edge cases mới
- [ ] Sync với kho AI Vibe Toolkit nếu có MCP/skill mới liên quan

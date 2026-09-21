# COMPANY CHARTER — Tano Agency Agent Company
> Viết 22/08/2026, sau khi nghiên cứu 2 repo mô hình thật: opc_agent
> (CroTuyuzhe, OPC — One Person Company) và OneManCompany
> (1mancompany, 422 sao, OMC — One Man Company). Không phát minh lại —
> gọi đúng tên cho những gì đã xây, vá đúng 2 khoảng trống lộ ra khi
> so sánh với 2 mô hình đã kiểm chứng.

## Sơ đồ tổ chức

```
                    NOBITANO (CEO — người duy nhất)
                              │
                    ┌─────────┴─────────┐
                    │  task-intake-      │  ← MỚI — vai trò "EA" (OMC)
                    │  quality-gate      │     gác cổng chất lượng
                    └─────────┬─────────┘     TRƯỚC khi dispatch
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
         VESSEL LAYER    VESSEL LAYER      VESSEL LAYER
        (Hermes/OpenClaw/  (Claude Code)   (Google Antigravity —
        DeepSeek Harness                    đã xác nhận là sản
        = "Team Thục Hán",                  phẩm Google thật,
        project OPC)                        không phải trùng tên)
              │
              ▼
         TALENT LAYER — 8 Pro Agent
   Research . Content . Sales . Marketing . Dev . Media . Designer .
   Customer Satisfaction
   = EXPERT-CORE.md (luật cứng, không đổi theo agent) + skill riêng
     từng agent (năng lực chuyên biệt)

         (Song song, không thuộc tầng nào)
   skill-lifecycle-management — vai trò "HR" (OMC) — audit định kỳ
   590+ skill trong thư viện chung, không gắn 1 Pro Agent cụ thể
```

## Thuật ngữ Vessel + Talent (mượn nguyên từ OneManCompany)

**Vessel** (con tàu/harness) = tầng THỰC THI — quyết định CHẠY Ở ĐÂU, không quyết định LÀM GÌ. Đã có 3 Vessel: Hermes/OpenClaw/DeepSeek Harness (project OPC), Claude Code, Google Antigravity. Đổi Vessel không đổi luật — đúng nguyên tắc CORE/Adapter đã thiết kế từ đầu (MASTER-TEMPLATE-MANIFEST.md).

**Talent** (năng lực) = 8 Pro Agent — mỗi cái là EXPERT-CORE.md (phần luật của agent đó) + skill riêng. Đây CHÍNH LÀ những gì đã xây — chỉ là giờ có tên đúng, khớp thuật ngữ đã kiểm chứng qua 422 sao GitHub thay vì tự đặt tên riêng.

**Employee = Vessel + Talent** — 1 Pro Agent chạy trên 1 Vessel cụ thể (vd: Content Pro chạy trên Hermes) là 1 "nhân viên" hoàn chỉnh.

## 2 khoảng trống đã vá — không phải lý thuyết, có bằng chứng cụ thể

### 1. task-intake-quality-gate (vai trò "EA")

**Vấn đề thật:** OpenClaw route task nhưng không có bước gác cổng chất lượng tường minh trước khi dispatch — task sai chỗ/vi phạm EXPERT-CORE chỉ bị phát hiện SAU KHI Pro Agent đã làm, không phải trước.

**Vá bằng:** 4 câu hỏi gác cổng (đúng agent? đủ info? vi phạm luật rõ ràng? độ khẩn?) — mượn Deepthink protocol (hỏi từng câu 1) từ opc_agent.

### 2. skill-lifecycle-management (vai trò "HR")

**Vấn đề thật, có bằng chứng cụ thể:** skills/ecc/ (271 file trùng 100%) tồn tại nhiều tháng không ai phát hiện; ad-budget-testing-discipline viết trùng với claude-ads/* đã có sẵn. Không có ai đóng vai audit định kỳ.

**Vá bằng:** 4 trạng thái vòng đời (Ứng tuyển/Đã xác minh/Nghỉ hưu/Từ chối) — mượn khái niệm hire/fire theo hiệu suất từ Talent Market của OneManCompany, áp cho skill thay vì nhân sự.

## Điểm KHÔNG mượn từ OPC/OMC — cân nhắc rồi bỏ

| Tính năng của OPC/OMC | Vì sao không áp |
|---|---|
| Pixel-art office UI (OMC) | Trang trí, không thêm giá trị vận hành thật |
| Performance review quý + PIP/termination cho "nhân viên" AI (OMC) | Ẩn dụ thú vị nhưng không cần thiết — skill-lifecycle-management đã đủ để quản lý chất lượng mà không cần kịch bản "sa thải" nhân cách hoá |
| Talent Market công khai (OMC) | Kho hiện đóng, phục vụ nội bộ Tano Agency — chưa cần marketplace mở |
| Cost accounting theo token/USD (OMC) | Hữu ích khi scale nhiều khách, chưa cấp bách khi 1 mình vận hành — để dành cho giai đoạn FDE có khách thật |

## Việc CHƯA làm — nói thẳng

- 2 skill mới (task-intake-quality-gate, skill-lifecycle-management) chưa test thật với task thật
- Cost accounting (mượn từ OMC) cố tình chưa làm — đúng quyết định, không phải bỏ sót
- Chưa xác nhận OpenClaw/DeepSeek Harness đã áp task-intake-quality-gate vào luồng nhận task thật chưa

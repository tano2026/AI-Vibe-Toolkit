# SMB AI Team — Đội Agent cho Khách Hàng Doanh Nghiệp

> AI Agency của Nobitano | Build for SMB Việt Nam
> Mỗi agent = 1 chuyên môn | Làm việc nhóm | Output giao được cho khách

---

## Kiến trúc team

```
Nobitano / Khách hàng
        |
        v
[Orchestrator] — OpenClaw nhận lệnh, phân công
        |
        |————————————————————————————————|
        v                                v
[01 Research Pro]              [02 ... Agent]  ← sắp có
Nghiên cứu & Data              ...

        |
        v
[Output] → Báo cáo / Content / Action
```

## Agents trong team

| # | Agent | Chuyên môn | Status |
|---|-------|-----------|--------|
| 01 | Research Pro | Research & Data Intelligence | ✅ Ready |
| 02 | Content Pro | Viết content, script, copy | 🔜 Next |
| 03 | Sales Pro | Tư vấn, chốt đơn, follow-up | 🔜 Next |
| 04 | Ops Pro | Báo giá, quy trình, vận hành | 🔜 Next |
| 05 | Analytics Pro | Phân tích hiệu quả, báo cáo | 🔜 Next |

## Cách dùng Research Pro ngay

```bash
# Hermes chạy trực tiếp
export FIRECRAWL_API_KEY="fc-xxxx"
export DEEPSEEK_API_KEY="sk-xxxx"
python3 agents/smb-ai-team/01-research-agent/research_agent.py "query"

# Qua Telegram (OpenClaw)
/research pain points công ty du lịch SMB Việt Nam
/research https://100xtourism.com/lp-7ngay.html phân tích landing page

# Import vào script khác
from research_agent import research, handle_telegram_command
report = research("Đối thủ của ABTRIP travel VN")
```

## Use cases thực tế (ngành du lịch)

- "Research landing page đối thủ [URL]"
- "Pain points của công ty du lịch SMB VN"
- "Content strategy của [brand]"
- "Data thị trường du lịch VN 2025-2026"
- "5 case study AI agent ngành F&B"

---
*SMB AI Team | Nobitano AI Agency | tháng 6/2026*

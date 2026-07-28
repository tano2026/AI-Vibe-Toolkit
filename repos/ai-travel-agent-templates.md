# AI Travel Agent Templates (trong awesome-llm-apps) — GitHub Repo

## TL;DR
3 cấp độ AI travel agent có sẵn trong `Shubhamsaboo/awesome-llm-apps` (175K sao) — từ đơn giản (1 file, chạy trong 30 giây) tới multi-agent team dùng MCP thật (Airbnb + Google Maps). Liên quan trực tiếp tới **M1 LLM Booking Desk** đã ghi trong roadmap Phase 1 MVP của ABTRIP B2B Travel Platform — đây là điểm khởi đầu tốt để tham khảo kiến trúc, không phải để deploy y nguyên.

## 3 cấp độ, chọn đúng theo nhu cầu

| Template | Path | Độ phức tạp | Dùng khi |
|---|---|---|---|
| **AI Travel Agent** (cơ bản) | `starter_ai_agents/ai_travel_agent` | 1 file, chạy 30 giây | Muốn hiểu nhanh kiến trúc cơ bản: prompt + search API → itinerary text |
| **AI Travel Agent with Memory** | `llm_apps_with_memory_tutorials/` | Có nhớ sở thích khách qua nhiều lần hỏi | Cần agent nhớ khách "thích khách sạn view biển" cho lần hỏi sau |
| **AI Travel Planner MCP Agent Team** | `mcp_ai_agents/ai_travel_planner_mcp_agent_team` | Multi-agent thật, MCP thật (Airbnb + Google Maps) | Cần itinerary chi tiết theo giờ, có tính khoảng cách/thời gian di chuyển thật, giá chỗ ở thật |

## Repo này dùng để làm gì
**Bản cơ bản** (`ai_travel_agent`): nhập điểm đến + số ngày → agent dùng SerpAPI search thông
tin thật (khách sạn, hoạt động, thời tiết) → LLM tổng hợp thành itinerary ngày-theo-ngày. Có
cả bản `local_travel_agent.py` chạy Ollama local, không gửi data ra ngoài.

**Bản MCP Team** (đáng chú ý nhất): kiến trúc multi-agent thật — 1 agent gọi **Airbnb MCP**
lấy dữ liệu chỗ ở thật (giá, tiện nghi, review), 1 agent khác gọi **Google Maps MCP** tính
khoảng cách/thời gian di chuyển chính xác giữa các điểm trong lịch trình, rồi 1 agent điều phối
tổng hợp thành itinerary cực chi tiết (giờ giấc, địa chỉ, chi phí từng mục).

## Setup từng bước (bản cơ bản, thử nhanh)
```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/starter_ai_agents/ai_travel_agent
pip install -r requirements.txt
# .env cần: OPENAI_API_KEY (hoặc đổi provider), SERPAPI_API_KEY
streamlit run travel_agent.py
```

## Liên hệ trực tiếp tới ABTRIP
Roadmap Phase 1 MVP của ABTRIP B2B Travel Platform có mục **M1 LLM Booking Desk** — đây chính
là loại kiến trúc tham khảo phù hợp nhất trong 3 cấp:
- Kiến trúc **multi-agent + MCP** của bản "Planner MCP Agent Team" là mô hình gần nhất với
  nhu cầu thật: 1 agent tra cứu chuyến bay/giá vé, 1 agent tính thời gian transit sân bay
  (thay Google Maps MCP bằng data nội bộ ABTRIP), 1 agent tổng hợp đề xuất gói Fast Track +
  SIM + đổi tiền theo hành trình khách.
- **KHÔNG dùng y nguyên** — đây là template public, demo bằng SerpAPI/Airbnb (không liên quan
  hàng không VN), phải tự thay toàn bộ data source bằng NDC aggregator (Duffel) đã lên kế
  hoạch + data nội bộ ABTRIP (giá Fast Track theo khung giờ, tồn kho SIM...).
- Giá trị thật của template: học cách CẤU TRÚC 1 multi-agent travel system (chia vai trò rõ
  ràng, mỗi agent 1 nguồn data, có agent điều phối tổng hợp) — áp dụng nguyên tắc kiến trúc,
  thay toàn bộ nguồn dữ liệu.

## Lưu ý / Lỗi thường gặp
- Cả 3 bản đều là **demo/template học tập**, không phải sản phẩm production-ready — cần thêm
  hẳn lớp bảo mật, rate limiting, xử lý lỗi thật trước khi tính đến việc đưa vào ABTRIP thật
  (áp dụng `skills/kiem-tra-bao-mat-truoc-deploy.md` đầy đủ nếu đi theo hướng này).
- Bản MCP Team cần cả 2 MCP server (Airbnb + Google Maps) chạy được — setup phức tạp hơn nhiều
  so với bản cơ bản, nên thử bản cơ bản trước để hiểu luồng, rồi mới lên bản MCP team.
- License Apache 2.0 (theo repo gốc) — tự do sửa/dùng, kể cả thương mại.

## Đánh giá cá nhân
- Điểm mạnh: đúng thời điểm — ABTRIP đang ở giai đoạn lên kế hoạch M1 LLM Booking Desk, có sẵn
  3 cấp độ tham khảo từ đơn giản tới phức tạp thay vì tự nghĩ kiến trúc từ đầu; bản MCP Team
  cho thấy mô hình chia agent theo nguồn data rất đáng học.
- Điểm yếu: hoàn toàn là demo, khoảng cách từ đây tới hệ thống booking thật (NDC/Duffel, giá
  Fast Track thật, tồn kho SIM) còn xa — chỉ dùng để THAM KHẢO KIẾN TRÚC, không phải điểm bắt
  đầu code trực tiếp cho sản phẩm thật.
- Có nên dùng không: 8/10 làm tài liệu tham khảo kiến trúc cho M1 LLM Booking Desk — không phải
  9-10 vì vẫn cần công sức lớn để thay data source và làm production-ready.

## Link
- Repo tổng (đã có trong kho): `repos/awesome-llm-apps.md`
- Bản cơ bản: https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/ai_travel_agent
- Bản MCP Team: https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/mcp_ai_agents/ai_travel_planner_mcp_agent_team

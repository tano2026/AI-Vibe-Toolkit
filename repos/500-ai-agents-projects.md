# 500-AI-Agents-Projects — Bộ Sưu Tập 500+ AI Agent Có Code Thật, Chia Theo Ngành

**GitHub:** https://github.com/ashishpatel26/500-AI-Agents-Projects
**Stars:** 32.4k⭐ | **Forks:** 5.7k | **License:** MIT
**Tác giả:** Ashish Patel (ashishpatel26) | **Tạo:** 12/2024
**Website:** ashishpatel26.github.io/500-AI-Agents-Projects

---

## Đây Là Gì

Bộ sưu tập lớn nhất hiện tại về AI agent projects — **500+ use case thực tế, có code chạy được**, phân loại theo ngành và theo framework.

Không phải danh sách link khô khan. Mỗi entry có:
- Mô tả rõ làm gì
- Link GitHub dẫn thẳng vào code
- Hướng dẫn chạy ngay (mỗi agent tự chứa requirements.txt + .env.example riêng)

---

## Phủ Sóng 20+ Ngành

| Ngành | Ví dụ agent |
|-------|-------------|
| Healthcare | Phân tích hồ sơ bệnh nhân, chẩn đoán bệnh |
| Finance | Bot giao dịch chứng khoán, quản lý ví smart contract |
| Education | Gia sư AI cá nhân hóa theo học sinh |
| Legal | Review hợp đồng, tóm tắt điều khoản |
| Cybersecurity | Phát hiện mối đe dọa real-time, red team testing |
| E-commerce | Personal shopper, gợi ý sản phẩm |
| Real Estate | Định giá bất động sản theo market trend |
| Agriculture | Dự đoán năng suất, sức khỏe cây trồng |
| Gaming | AI companion hỗ trợ người chơi real-time |
| HR | Agent tuyển dụng, match candidate với job |
| Supply Chain | Tối ưu route giao hàng, quản lý kho |
| Manufacturing | Giám sát dây chuyền sản xuất |
| Energy | Dự báo nhu cầu điện, tối ưu lưới |
| Hospitality | Lên kế hoạch du lịch theo sở thích |
| Customer Service | Chatbot 24/7 xử lý query |
| Retail | Gợi ý sản phẩm theo lịch sử mua hàng |
| Transportation | Tối ưu route giao hàng tự động |
| Entertainment | Gợi ý nội dung cá nhân hóa |
| Software Dev | Orchestrate Claude Code agent fleets |
| Insurance | Tự động hóa quy trình claim bảo hiểm |

---

## 5 Framework Chính — Khi Nào Dùng Cái Nào

| Framework | Phù hợp | Độ phức tạp |
|-----------|----------|-------------|
| **Agno** | Agent đơn, tool integration, học nhanh | ⭐ (dễ nhất) |
| **CrewAI** | Team agent theo vai trò, automation kinh doanh | ⭐⭐ |
| **LlamaIndex** | Q&A tài liệu, RAG pipeline doanh nghiệp | ⭐⭐ |
| **LangGraph** | Workflow phức tạp, RAG + stateful graph | ⭐⭐⭐ |
| **AutoGen** | Viết code, research, workflow tự phục hồi | ⭐⭐⭐ |

**Mới bắt đầu → Agno hoặc CrewAI**
**Cần RAG phức tạp → LangGraph**
**Build code-writing agent → AutoGen**

---

## Cấu Trúc Repo

```
500-AI-Agents-Projects/
├── agents/              # 500+ agent có code chạy được
│   ├── 01-web-research-agent/
│   │   ├── agent.py
│   │   ├── requirements.txt
│   │   └── .env.example
│   ├── 02-...
│   └── ...
├── crewai_mcp_course/   # Khóa học CrewAI + MCP kèm theo
└── images/              # Mind map theo ngành
```

Mỗi folder agent là **độc lập hoàn toàn** — không cần setup monorepo.

---

## Chạy Agent Đầu Tiên — 5 Phút

```bash
# Clone repo
git clone https://github.com/ashishpatel26/500-AI-Agents-Projects.git
cd 500-AI-Agents-Projects

# Chọn agent bất kỳ trong agents/
cd agents/01-web-research-agent

# Install deps
pip install -r requirements.txt

# Thêm API key
cp .env.example .env
# → mở .env, điền OPENAI_API_KEY hoặc ANTHROPIC_API_KEY

# Chạy
python agent.py
```

---

## Bonus: Có Kèm Khóa Học CrewAI + MCP

Thư mục `crewai_mcp_course/` — không chỉ là code mẫu mà có cả course học từ đầu về CrewAI tích hợp MCP. Hiếm repo nào có điều này.

---

## Cách Dùng Thực Tế Cho Vibe Coders

**Scenario 1 — Tìm ý tưởng:** Mày muốn build agent cho lĩnh vực X → vào bảng Industry Use Cases → tìm ngành → clone code về → đọc logic → adapt theo ý mày.

**Scenario 2 — Học framework mới:** Chưa biết LangGraph → vào agents/ lọc theo LangGraph → chạy ví dụ đơn giản nhất trước → đọc code → hiểu pattern.

**Scenario 3 — Pitch cho khách hàng:** Mày đang tư vấn AI agent cho doanh nghiệp ngành Y → dẫn khách vào đây → "đây là 20 use case ngành mày, cái nào phù hợp thì mình build" → close deal nhanh hơn.

---

## Đánh Giá Cá Nhân

32k stars, 5.7k forks — con số nói lên chất lượng. Được tạo từ 12/2024 và vẫn active đến 6/2026, last commit mới tháng trước.

Điểm tao thích nhất: **mỗi agent tự chứa, chạy độc lập**. Không bị cái kiểu clone về rồi setup cả ngày mới chạy được. Clone → pip install → chạy. Xong.

Cộng thêm framework comparison table rõ ràng — cực kỳ hữu ích cho người mới không biết chọn LangGraph hay CrewAI.

Điểm trừ: 500+ agent nhưng chất lượng không đồng đều — một số repo được link tới đã archive hoặc outdated. Cần check kỹ trước khi dùng production.

Repo này không phải để học AI — **để tìm idea và lấy code khởi đầu**. Dùng đúng mục đích thì cực kỳ giá trị.

**Rating: 8.5/10** — bookmark ngay, dùng khi bí idea hoặc cần code mẫu.

---

*Nguồn: github.com/ashishpatel26/500-AI-Agents-Projects*
*Stars: 32.4k⭐ (tháng 6/2026) | MIT License*
*Cập nhật: tháng 6/2026*

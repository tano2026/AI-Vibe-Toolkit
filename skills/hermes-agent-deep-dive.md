# Hermes Agent — Deep Dive: 8 Vòng Lặp & Cách Dùng Hiệu Quả

**Nguồn:** NousResearch/hermes-agent (95k⭐ → 188k⭐) | v0.16.0 | MIT
**Research by:** @IBuzovskyi / KHDA AI phân tích (infographic)
**Cập nhật:** tháng 6/2026

---

## Kiến Trúc Tổng Quan

```
Người dùng (chat / CLI / gateway)
         ↓
    [Vòng lặp 1 — Core Agent Loop]  ← tim của hệ thống
    /          |          \
   L5        L6          L7
 Memory   Kanban       Nén ngữ cảnh
   |         |              |
   L2       L2x3         restart
  Ralph    parallel       session
   |
   L3 → Skills tích lũy → L4 Curator (mỗi 7 ngày)
                                |
                            L8 Sub-agents (khi cần)
```

---

## 8 Vòng Lặp — Chi Tiết Kỹ Thuật

### 🔵 LOOP 1 — Core Agent Loop (ms → phút)
**Vai trò:** Tim của hệ thống
**Cơ chế:**
- `prompt + tool + repeat`, max **90 lượt/phiên**
- Tool calls đơn lẻ → thread chính
- Nhiều tools cùng lúc → **ThreadPoolExecutor** (8 workers song song)
- 3 chế độ API: `streaming` / `non-streaming` / `Anthropic`

**Khi thiếu:** Không có gì chạy được

---

### 🟢 LOOP 2 — Ralph /goal (phút → giờ)
**Vai trò:** Trợ lý đánh giá mục tiêu sau mỗi lượt
**Cơ chế:**
- Kiểm tra: "Hoàn thành chưa?"
- Max **20 lượt/mục tiêu**
- `/subgoal` → thêm tiêu chí giữa chừng mà không reset bộ đếm
- Tích hợp với L6 để dispatch nhiều goal song song

**Khi thiếu:** Không có gì check task xong chưa — loop vô tận

**Dùng ngay:**
```bash
/goal "viết script video về hermes agent, 90 giây"
/goal "research top 5 AI frameworks 2026"
/subgoal "thêm so sánh với LangChain"
```

---

### 🟢 LOOP 3 — Tự Cải Tiến / Skills (sau mỗi tác vụ)
**Vai trò:** Tự tạo skill từ kinh nghiệm — đây là cái phân biệt Hermes với mọi framework khác
**Cơ chế:**
- Agent phân tích phương pháp hiệu quả sau task
- Lưu thành skill file: `~/.hermes/skills/`
- Chạy **ngầm qua fork process** — không ảnh hưởng phiên chính
- Sau 3 tháng: **40-60 skills tích lũy**

**Số liệu:** Giảm **40% thời gian** với goal 20+ skills

**Khi thiếu:** Mỗi phiên bắt đầu từ con số 0 — không học được gì

---

### 🟡 LOOP 4 — Curator (mỗi 7 ngày)
**Vai trò:** Dọn dẹp kho skill, giữ chất lượng
**Cơ chế:**
- Tự kích hoạt khi rảnh ≥2h
- Chuyển skill ít dùng vào `.archive/`
- Hợp nhất skills trùng lặp
- **Không bao giờ xóa vĩnh viễn**

**Khi thiếu:** Kho skill phình → context nặng → chậm

---

### 🟣 LOOP 5 — Bộ Nhớ (xuyên suốt & sau phiên)
**Vai trò:** RAM + Long-term memory
**Cơ chế — 3 lớp:**
```
Lớp 1: RAM session (nhanh nhất, mất khi đóng)
Lớp 2: MEMORY.md + USER.md (long-term, persist)
Lớp 3: FTS5 SQLite (full-text search, truy vấn ngữ nghĩa)
```
- Giới hạn: **2200 ký tự / 800 token** chèn vào mỗi lượt
- 8 plugin memory ngoài: **Mem0 giảm 72% token**

**Khi thiếu:** "Mất trí nhớ" sau mỗi phiên — phải giải thích lại từ đầu

**Setup:**
```bash
hermes setup --portal   # kích hoạt L1 + L5
```

---

### 🟠 LOOP 6 — Kanban Dispatcher (mỗi 60 giây)
**Vai trò:** Điều phối đa agent/task
**Cơ chế:**
- Quét `kanban.db` (SQLite) mỗi 60 giây
- Giao việc cho worker rảnh
- Phát hiện zombie process
- Thu hồi task bị treo
- Dispatch nhiều /goal **song song**

**Khi thiếu:** Điều phối đa agent = phải làm thủ công

---

### 🔴 LOOP 7 — Nén Ngữ Cảnh (tự kích hoạt khi >50% context)
**Vai trò:** Giữ cost trong tầm kiểm soát
**Cơ chế — 4 giai đoạn:**
```
1. Lọc tool output cũ
2. Kiểm tra hiệu quả
3. Tóm tắt LLM (giữ 3 đầu + 20 cuối)
4. Tạo session con mới
```
- Tự kích hoạt khi ngữ cảnh vượt **50%**
- Giảm **73% token** vs inject thủ công

**Khi thiếu:** /goal dài → API timeout, bill tăng vô lý

---

### 🔴 LOOP 8 — Agent Con / Sub-Agents (song song)
**Vai trò:** Nhân bản năng lực
**Cơ chế:**
- `delegate_task()` khởi tạo sub-agent với context riêng
- Max **3 chạy đồng thời**
- Mỗi agent con tự chạy: L1, L2, L3, L5, L7
- **Model strategy:** dùng model rẻ cho con, model mạnh cho parent orchestrator
- Nhân **x3 năng lực xử lý**

**Khi thiếu:** Tác vụ phức tạp bị nút cổ chai

**Dùng:**
```bash
delegate_task("research competitor A") &
delegate_task("research competitor B") &
delegate_task("research competitor C") &
# 3 agents chạy song song
```

---

## Compound Effect — Tại Sao Loop Quan Trọng

```
Loop 3 tạo Skill
    → Loop 4 tinh lọc (skill sạch)
        → Loop 2 (/goal) nhanh hơn
            → Loop 5 cung cấp context tức thì
                → Loop 6 dispatch nhiều Loop 2 song song
                    → Loop 7 giữ cost Loop 1 hợp lý
                        → Loop 8 nhân bản năng lực

Kết quả:
Skill(3) + Curator(4) + Goal(2)
= nhanh hơn + nhiều Skill hơn
= Agent ngày 90 >>> Agent ngày 1
```

---

## So Sánh Framework

| Framework | Số vòng lặp | Đặc điểm |
|-----------|------------|---------|
| Chat wrapper | 1 loop | prompt → reply |
| LangChain / CrewAI | 2-3 loops | basic agent |
| DSPy | optimize prompts | không có runtime |
| **Hermes** | **8 loops** | **AI Operating System** |

---

## Số Liệu Thực Tế (v0.16.0)

| Metric | Số liệu |
|--------|---------|
| Stars GitHub | 95k (7 tuần) → 188k |
| Thời gian giảm với 20+ skills | -40% |
| Token giảm vs inject thủ công | -73% |
| Frameworks khác | 1-3 vòng lặp |
| Hermes | 8 vòng lặp đồng thời |
| Skills community | 90,000+ |

---

## Hệ Quả Khi Thiếu Loop

| Thiếu | Hậu quả cụ thể |
|-------|---------------|
| L3 (Skills) | Mỗi phiên = ngày 1, không tích lũy |
| L4 (Curator) | Kho skill phình → context nặng |
| L5 (Memory) | Giải thích lại từ đầu mỗi phiên |
| L7 (Nén) | /goal >20 lượt → API timeout |
| L6 (Kanban) | Multi-agent = thủ công 100% |
| L8 (Sub-agents) | Task phức tạp = bottleneck |

---

## Bắt Đầu 3 Bước

```bash
# Bước 1 (5 phút) — kích hoạt L1 + L5
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes setup --portal

# Bước 2 (10 phút) — kích hoạt L2 + L3
/goal [mô tả task đầu tiên của mày]
# Sau task xong → L3 tự tạo skill đầu tiên

# Bước 3 (30 phút) — kích hoạt toàn hệ thống
# Cron 8h sáng → L1+L2+L3+L5+L7 tự chạy
# L4 tự kích hoạt sau 7 ngày đầu tiên
# L8 kích hoạt khi mày dùng delegate_task
```

---

## Tip Dùng Hiệu Quả

**Dùng `/goal` thay `/chat` cho mọi task có nhiều bước**
→ L2 mới track được tiến độ, L3 mới học được từ task đó

**Để Hermes chạy tối thiểu 90 ngày liên tục**
→ Compound effect chỉ rõ sau 30-60 days, đỉnh ở 90 days

**Dùng model rẻ (Gemma/Qwen) cho sub-agents**
→ Tiết kiệm 60-70% cost trong khi giữ được throughput

**Không xóa `.archive/` folder**
→ Curator đã xử lý tối ưu rồi, xóa là mất lịch sử học

**Mem0 plugin là must-have**
→ Giảm 72% token consumption của L5

---

*Nguồn: NousResearch/hermes-agent + infographic phân tích bởi @IBuzovskyi / KHDA AI*
*AI Vibe Toolkit | tháng 6/2026*

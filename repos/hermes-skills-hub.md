# Hermes Skills Hub — Kho 88.000+ Skill cho AI Agent

**GitHub:** https://github.com/NousResearch/hermes-agent (Skills Hub là feature built-in)
**Stars:** 211k+ | **License:** MIT | **Tác giả:** Nous Research
**Website:** hermes-ai.net | Skills Hub: tích hợp trực tiếp trong Hermes Agent

---

## TL;DR
Skills Hub là "app store" skill cho Hermes Agent — nơi tìm, xem và cài các gói giúp agent biết làm việc cụ thể. Hiện có 88.057 skill từ 12 nguồn, gom từ Anthropic, OpenAI, HuggingFace, NVIDIA đến cộng đồng tự đăng.

---

## Repo này dùng để làm gì

Hermes Agent học "skill" để làm việc — giống người đi học nghề. Không có skill thì agent chỉ chat. Có skill thì agent biết: viết code, tạo diagram, quản lý Apple Notes, delegate task cho Claude Code hay OpenCode, tạo video ASCII, vẽ infographic...

Skills Hub gom tất cả nguồn skill về **1 chỗ** thay vì mày phải tự mò từng repo:

| Nguồn | Số skill | Đặc điểm |
|-------|----------|-----------|
| Anthropic | 17 | Chất lượng cao, checked |
| OpenAI | 44 | Tập trung coding/agent |
| HuggingFace | 25 | ML/AI models |
| NVIDIA | 230 | GPU compute, ML ops |
| skills.sh | 19.963 | Script automation |
| ClawHub | 66.610 | Community lớn nhất |
| LobeHub | 505 | Chat personas |
| browse.sh | 435 | Browser automation |
| gstack | 53 | DevOps stack |
| Marketplace | 1 | Official curated |

Catalog auto-rebuild 2 lần/ngày, hiện có **196 categories** từ AI Agents, Productivity, Software Dev đến Creative, Security, Data Science.

---

## Setup từng bước

### 1. Cài Hermes Agent (nếu chưa có)
```bash
npm install -g hermes-agent
# hoặc
npx hermes-agent
```

### 2. Mở Skills Hub trong Hermes
```
/skills        → mở Skills Hub
/skills search → tìm kiếm skill
```

### 3. Browse và cài skill
```bash
# Tìm skill theo tên
/skills search "code review"

# Xem chi tiết trước khi cài
/skills info <skill-name>

# Cài skill
/skills install <skill-name>

# Xem skill đã cài
/skills list
```

### 4. Dùng skill sau khi cài
Sau khi install, skill tự available trong session Hermes. Gọi bằng `/skill-name` hoặc mention tên trong prompt.

---

## Ví dụ thực tế

**Scenario:** Nobitano cần Hermes tự tạo architecture diagram cho ABTRIP system.

```bash
# Bước 1: Tìm skill phù hợp
/skills search "architecture diagram"
# → Kết quả: architecture-diagram (Built-in, Creative category)
# Mô tả: Dark-themed SVG architecture/cloud/infra diagrams as HTML

# Bước 2: Xem detail
/skills info architecture-diagram
# Platform: Linux, macOS, Windows

# Bước 3: Cài
/skills install architecture-diagram

# Bước 4: Dùng
/architecture-diagram "Vẽ kiến trúc hệ thống ABTRIP: booking API, 
payment gateway, Telegram bot, PostgreSQL DB"
# → Output: file HTML với SVG diagram dark-theme, download được
```

**Các skill Built-in hay dùng nhất:**
- `claude-code` — delegate coding task sang Claude Code CLI
- `architecture-diagram` — vẽ sơ đồ kiến trúc SVG dark-theme
- `excalidraw` — hand-drawn diagram JSON (flow, arch, sequence)
- `hermes-agent` — config/extend chính Hermes
- `ascii-art` — ASCII art từ pyfiglet, cowsay, boxes
- `humanizer` — strip AI-isms, thêm voice tự nhiên vào text
- `manim-video` — animation math/algo kiểu 3Blue1Brown

---

## ⚠️ Lưu ý bảo mật — QUAN TRỌNG, đọc trước khi cài

**Skill không chỉ là text — nó chạy lệnh thật trên máy mày.**

Một skill xấu có thể:
- Lén đọc file, env vars, SSH keys
- Gửi data ra ngoài mà mày không biết
- Chứa **prompt injection** ẩn — nhét lệnh bên trong để lái agent làm việc mày không yêu cầu

**Rule cụ thể khi dùng Skills Hub:**

| Nguồn | Mức tin | Hành động |
|-------|---------|-----------|
| Built-in (72 skill) | ✅ Tin được | Cài thẳng |
| Anthropic, OpenAI, NVIDIA | ✅ Tin được | Cài thẳng |
| HuggingFace, LobeHub | ⚠️ Tin có điều kiện | Đọc description + check repo |
| ClawHub, skills.sh (cộng đồng) | ❌ Cẩn thận | Đọc source code trước khi cài |
| Marketplace | ✅ Curated | Tin được |

**Trước khi cài skill lạ, check:**
1. Skill xin quyền gì? (file access, network, env vars?)
2. Source code ở đâu? (mở ra đọc được không?)
3. Author là ai? (org uy tín hay anonymous account?)
4. Bao nhiêu người dùng, review thế nào?

**Nếu không check được → không cài.** 88k skill lớn quá để verify hết, phần lớn community-contributed. ClawHub có 66k skill nhưng Nous Research không audit từng cái.

---

## Đánh giá cá nhân

- **Điểm mạnh:**
  - Concept hay — "app store" cho agent, chuẩn hóa cách extend capability
  - 88k skill là con số khủng, phủ gần như mọi use case
  - Built-in skills chất lượng tốt, nhiều cái thực sự useful (architecture-diagram, claude-code, excalidraw)
  - Auto-refresh 2x/ngày, luôn có skill mới
  - Search + category filter dùng được, không bị ngợp

- **Điểm yếu:**
  - **Security là vấn đề thật** — 66k skill từ ClawHub không qua audit, rủi ro prompt injection có thật
  - Chưa có review system hoặc verified badge rõ ràng cho community skills
  - 88k skill nghe nhiều nhưng quality rất không đều — phần lớn cộng đồng tự viết
  - Không có sandbox — skill chạy thẳng, không có layer isolate
  - Còn mới (Hermes agent 7 tuần đạt 211k stars), ecosystem chưa mature

- **Có nên dùng không: 7/10** — Built-in + Big vendor skills thì dùng thoải mái. Community skills (ClawHub) thì dùng như repo npm lạ: verify trước, đừng cài đại. Skills Hub là hướng đúng cho agent ecosystem, chỉ cần thêm trust layer.

---

## Link
- **Repo chính:** https://github.com/NousResearch/hermes-agent
- **Website:** https://hermes-ai.net
- **Skills Hub UI:** Mở trong Hermes Agent qua `/skills`
- **Entry liên quan trong kho:** `/repos/hermes-agent.md`

---

## 🤖 Agent Integration

### Hermes (Python — gọi Skills Hub qua subprocess)
```python
import subprocess

def install_hermes_skill(skill_name: str):
    """Cài skill vào Hermes Agent"""
    result = subprocess.run(
        ["npx", "hermes-agent", "--skill-install", skill_name],
        capture_output=True, text=True
    )
    return result.stdout

def list_installed_skills():
    """Liệt kê skill đã cài"""
    result = subprocess.run(
        ["npx", "hermes-agent", "--skill-list"],
        capture_output=True, text=True
    )
    return result.stdout

# Ví dụ: cài architecture-diagram (Built-in, safe)
install_hermes_skill("architecture-diagram")
```

### OpenClaw
```bash
# Trong session OpenClaw/Hermes
/skills install architecture-diagram
/skills install claude-code
/skills install excalidraw
```

### Antigravity
```bash
# Check Hermes đã cài chưa
hermes-agent --version

# Update Hermes (kéo skills mới về)
npm update -g hermes-agent

# List skills đang active
hermes-agent --skill-list
```

> ⚠️ KHÔNG cài skill từ ClawHub hoặc nguồn anonymous lên VPS production (Hermes trên Tencent Cloud). Chỉ dùng Built-in + Anthropic/OpenAI/NVIDIA skills trên môi trường có data nhạy cảm. Nguy cơ prompt injection là thật.

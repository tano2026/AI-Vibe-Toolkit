# Script Video #37 — Hermes Agent: AI Agent Càng Dùng Càng Thông Minh

**Repo:** https://github.com/NousResearch/hermes-agent
**Stars:** 188k⭐ | **Thời lượng video:** 90-120 giây
**Hook angle:** "Agent không bao giờ quên — càng dùng lâu càng thông minh hơn"

---

## 🎬 SCRIPT

---

**[HOOK — 0:00-0:08]**
*(Text on screen: "ChatGPT hôm nay vs ChatGPT 3 tháng trước = GIỐNG HỆT NHAU")*

Mày đã dùng AI agent được 3 tháng.
Nhưng nó vẫn không biết mày là ai.
Vẫn phải giải thích lại workflow từ đầu.
Vẫn mắc lại lỗi y chang tuần trước.

---

**[VẤN ĐỀ — 0:08-0:18]**
*(Screen: So sánh 2 cột: "Agent bình thường" vs "Hermes")*

Tất cả agent framework hiện tại —
LangChain, CrewAI, Claude Projects —
đều bắt đầu lại từ đầu sau mỗi phiên.

Ngày 1 bằng ngày 90.
Mày dùng 3 tháng, nó không học được gì từ mày.

---

**[GIẢI PHÁP — 0:18-0:35]**
*(Screen: Logo Hermes Agent + 188k stars)*

Hermes Agent của Nous Research.
188 nghìn stars — tốc độ tăng nhanh nhất lịch sử GitHub cho AI agents.

Điểm khác biệt là **closed learning loop** —
8 vòng lặp chạy liên tục, và quan trọng nhất:

**Loop 3 — tự tạo skill từ kinh nghiệm.**

*(Screen: Diagram đơn giản: Task → Agent → Skill file → Agent dùng lại)*

Mày làm task → agent phân tích cách làm hiệu quả → lưu thành skill file.
Lần sau task tương tự? Nó dùng lại skill đó. Nhanh hơn, ít lỗi hơn.

---

**[8 LOOPS NHANH — 0:35-0:55]**
*(Screen: List 8 loops cuộn qua nhanh, highlight 3 cái quan trọng nhất)*

8 vòng lặp — tao giải thích nhanh 3 cái mày cần biết:

**Loop 3:** Tự học → tạo skill file sau mỗi task.
*(visual: folder ~/.hermes/skills/ với nhiều file)*

**Loop 5:** Bộ nhớ 3 lớp — nhớ mày là ai, nhớ preferences, nhớ context xuyên phiên.
*(visual: MEMORY.md file)*

**Loop 8:** Spawn agent con — tác vụ phức tạp thì phân chia cho nhiều agent chạy song song.
*(visual: 1 agent parent → 3 agent con)*

Kết quả: **Agent ngày 90 của mày ≠ Agent ngày 1.**

---

**[SETUP — 0:55-1:10]**
*(Screen: Terminal thật, chạy lệnh)*

Setup 1 lệnh:

```
curl -fsSL [install url] | bash
```

Chạy xong:
```
hermes setup --portal
```

Xong. Không cần Docker, không cần config phức tạp.
Chạy được trên laptop, trên $5 VPS, hay trên Termux điện thoại Android.

*(Screen: Hermes terminal đang chạy)*

---

**[PROOF — 1:10-1:20]**
*(Screen: GitHub repo, số stars đang tăng)*

3 tháng dùng liên tục →
40 đến 60 skill files tích lũy trong máy mày.
90 nghìn skills từ community đã có sẵn để cài.

Agent này của mày.
Không ai có agent giống mày.

---

**[CTA — 1:20-1:30]**
*(Screen: Link GitHub)*

Link trong bio.
MIT license — free hoàn toàn.

Cài rồi thì nhớ dùng `/goal` trước —
đó là lúc loop 2 và 3 bắt đầu học từ mày.

*(Text on screen: "Ngày 90 > Ngày 1")*

---

## 📋 METADATA

**Hook chính:** "AI agent dùng 3 tháng vẫn không biết mày là ai"
**Hook phụ (test A/B):** "188k stars trong 7 tuần — AI agent tự học workflow của mày"

**Tags:** #aiagent #hermesagent #vibecoding #aivietnam #llm #opensource

**Thumbnail concept:**
- Nền tối
- Text to: **"Ngày 1 vs Ngày 90"**
- Bên trái: robot trống rỗng (Ngày 1)
- Bên phải: robot đầy skills/memory (Ngày 90)
- Màu accent: xanh tím (Nous Research brand)

**Cảnh quay cần:**
1. Terminal: chạy lệnh install
2. Terminal: `hermes setup --portal`
3. Terminal: `/goal [task]` và agent phản hồi
4. File explorer: folder `~/.hermes/skills/` sau vài ngày dùng
5. GitHub: trang repo + số stars

---

*Script by AI Vibe Toolkit | Video #37*

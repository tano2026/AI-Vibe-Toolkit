# Superpowers — Plugin Biến Claude Code Thành Senior Dev

> 150k GitHub stars, trending #1. Cài vào Claude Code — AI sẽ suy nghĩ, lên kế hoạch, test trước khi code, thay vì nhảy vào làm bừa.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **GitHub** | [obra/superpowers](https://github.com/obra/superpowers) ⭐ 150,000+ |
| **Tác giả** | Jesse Vincent (obra) |
| **Ra mắt** | October 2025 |
| **Dùng với** | Claude Code, Cursor, Codex, OpenCode, Gemini CLI |
| **Free hay trả phí** | Free hoàn toàn |
| **Yêu cầu** | Claude Code 2.0.13+ |

---

## 🎯 Vấn đề nó giải quyết

Vibe coding hay xảy ra cái này:
- Bảo AI làm → nó nhảy vào code luôn → sai đủ chỗ → mày debug cả buổi
- AI không test → code chạy được trên máy mày → deploy lên là lỗi
- Làm xong rồi mới phát hiện hiểu sai yêu cầu

**Superpowers fix bằng cách bắt AI đi qua 7 bước:**
```
1. Brainstorm — hỏi ngược lại để hiểu đúng yêu cầu
2. Design — lên plan trước khi code
3. Plan — chia task nhỏ, estimate
4. TDD — viết test trước, code sau
5. Execute — code từng bước nhỏ
6. Review — tự review trước khi xong
7. Verify — chạy test, confirm done
```

Không bước nào được skip.

---

## ⚡ Cài vào Claude Code

```bash
# Mở Claude Code, chạy 2 lệnh này:

/plugin marketplace add obra/superpowers-marketplace

/plugin install superpowers@superpowers-marketplace

# Restart Claude Code → Done
```

**Hoặc cài từ official marketplace:**
```bash
/plugin install superpowers@claude-plugins-official
```

---

## 💡 Dùng thế nào

Sau khi cài, Claude tự kích hoạt đúng skill theo context:

```bash
# Bắt đầu feature mới
/superpowers:brainstorm
→ Claude hỏi ngược: "Feature này cần handle edge case nào?"

# Sau khi design xong
/superpowers:write-plan  
→ Claude viết plan chi tiết, mày approve rồi mới làm

# Bắt đầu implement
/superpowers:execute-plan
→ Chạy từng bước, có checkpoint, không làm bừa

# Khi có bug khó
/superpowers:debug
→ 4-phase systematic debugging, không đoán mò
```

---

## ⚠️ Lưu ý

- Cần **Claude Code** (terminal) — không phải Claude Desktop
- Claude Code cần subscription Claude Pro trở lên
- Lần đầu dùng hơi chậm vì AI đọc skills trước khi làm
- Không phù hợp cho task nhanh đơn giản — overkill

---

## 🔗 Hay kết hợp với

- **Context7** — Superpowers lo workflow, Context7 lo docs đúng version
- **GitHub MCP** — Execute plan xong → auto commit từng bước

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Dễ cài | ⭐⭐⭐⭐⭐ |
| Thay đổi workflow | ⭐⭐⭐⭐⭐ |
| Phù hợp vibe coder | ⭐⭐⭐⭐☆ |
| Wow factor | ⭐⭐⭐⭐⭐ |

**Tóm lại:** Đây là lý do @i.towf và cả cộng đồng Claude Code đang nói đến. 150k stars trong 6 tháng — không phải hype, là vì nó thực sự thay đổi cách AI code.

---

*Thêm vào kho: 06/2025 | Nguồn: github.com/obra/superpowers*

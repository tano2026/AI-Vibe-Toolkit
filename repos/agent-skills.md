# Agent Skills (addyosmani) — Bộ Kỹ Năng Chuẩn Production Cho AI Agents

> Addy Osmani — Google Chrome lead — build bộ skills này để AI agents code đúng chuẩn production, không phải code vibe bừa bãi.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **GitHub** | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| **Tác giả** | Addy Osmani (Google Chrome Engineering Lead) |
| **Dùng với** | Claude Code, Cursor, Codex, bất kỳ AI coding agent nào |
| **Free** | ✅ Hoàn toàn free |

---

## 🎯 Vấn đề nó giải quyết

AI coding agents hay:
- Viết code không có error handling
- Không viết tests
- Không quan tâm đến performance
- Bỏ qua security best practices

**Agent Skills fix bằng cách inject bộ rules vào agent** — bắt nó follow chuẩn production-grade trước khi viết 1 dòng code.

---

## 💡 Có gì trong bộ skills này

- `code-quality` — Clean code, không có code smell
- `testing` — Tự viết unit tests, integration tests
- `security` — Check XSS, SQL injection, auth issues
- `performance` — Tối ưu tự động
- `documentation` — Tự viết docs rõ ràng
- `error-handling` — Không để unhandled exceptions

---

## ⚡ Cách dùng

```bash
# Clone về
git clone https://github.com/addyosmani/agent-skills

# Copy skills vào project của mày
cp -r agent-skills/skills ./

# Bảo Claude đọc:
"Đọc file skills/ và áp dụng tất cả 
 khi mày code cho project này"
```

---

## 🔗 Hay kết hợp với

- **Superpowers** — Superpowers lo workflow, Agent Skills lo code quality
- **Context7** — Docs đúng + code quality = production ready

---

## 📊 Đánh giá

| Tiêu chí | Điểm |
|----------|------|
| Dễ dùng | ⭐⭐⭐⭐☆ |
| Code quality tăng | ⭐⭐⭐⭐⭐ |
| Phù hợp vibe coder | ⭐⭐⭐⭐☆ |

**Tóm lại:** Khi code của mày cần đưa lên production thật — không phải chỉ demo — cài bộ này vào.

---

*Thêm vào kho: 06/2025 | Nguồn: github.com/addyosmani/agent-skills*

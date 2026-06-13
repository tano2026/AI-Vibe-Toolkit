# Bumblebee (Perplexity AI) — Scanner Bảo Vệ Máy Mày Khỏi MCP Độc Hại

> Perplexity AI vừa open-source tool nội bộ họ dùng để bảo vệ máy developer. Scan MCP configs, extensions, packages — phát hiện malware trước khi nó chạy.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **GitHub** | [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) ⭐ 2,600+ |
| **Tác giả** | Perplexity AI |
| **Ra mắt** | May 22, 2026 |
| **Ngôn ngữ** | Go (zero dependencies) |
| **Free** | ✅ Apache 2.0 |
| **Yêu cầu** | Go 1.25+, macOS hoặc Linux |

---

## 🎯 Vấn đề nó giải quyết

Tháng 5/2026: hacker group UNC6780 đầu độc 160+ packages được dùng bởi hàng triệu developers — bao gồm tools của Mistral AI, UiPath, và React package 12 triệu lượt download/tuần.

**Bumblebee sinh ra để scan và phát hiện trước khi mày bị dính:**
- MCP configs (claude_desktop_config.json, .mcp.json...)
- npm, PyPI, Go modules, RubyGems, Composer packages
- VS Code, Cursor, Windsurf extensions
- Browser extensions (Chrome, Firefox)

**Điểm đặc biệt:** Read-only hoàn toàn — không chạy code nào, không thể trigger malware khi scan.

---

## ⚡ Cài và dùng

```bash
# Cài (cần Go 1.25+)
go install github.com/perplexityai/bumblebee/cmd/bumblebee@latest

# Scan cơ bản — inventory toàn bộ
bumblebee scan --profile baseline

# Scan project cụ thể
bumblebee scan --profile project --root ./my-project

# Scan deep — toàn bộ home directory
bumblebee scan --profile deep --root "$HOME" --findings-only
```

---

## 💡 Quan trọng với vibe coders

Mày đang cài MCP servers liên tục — mỗi cái là một potential attack surface.

```bash
# Sau mỗi lần cài MCP mới → scan ngay
bumblebee scan --profile baseline --findings-only

# Nếu có findings → review trước khi dùng
```

---

## ⚠️ Lưu ý

- Chỉ chạy được trên **macOS và Linux** — Windows chưa support
- Cần cài Go 1.25+ trước
- Scan không 100% — chỉ match với known threats catalog

---

## 🔗 Hay kết hợp với

- **OpenClaw** — cài skill từ ClawHub → scan bằng Bumblebee trước khi dùng
- **Tất cả MCP servers trong kho** — scan sau mỗi lần cài

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Dễ dùng | ⭐⭐⭐⭐☆ |
| Quan trọng | ⭐⭐⭐⭐⭐ |
| Content angle độc | ⭐⭐⭐⭐⭐ |

**Tóm lại:** Angle "cài MCP mà không bị hack" chưa ai làm content về. Bumblebee + câu chuyện hack 160 packages tháng 5/2026 = video cực hay, vừa useful vừa có drama.

---

*Thêm vào kho: 06/2025 | Nguồn: github.com/perplexityai/bumblebee*

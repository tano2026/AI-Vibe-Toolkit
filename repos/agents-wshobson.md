# agents (wshobson)

> *Một marketplace plugin tác nhân đa nền tảng, cung cấp các khối xây dựng workflow AI agent sẵn sàng cho sản xuất.*

---

## 📌 Thông tin

| | |
|--|--|
| **GitHub** | [link](https://github.com/wshobson/agents) |
| **Stars** | ⭐ 37.1k |
| **Ngôn ngữ** | Python |
| **Cập nhật gần nhất** | 2 tuần trước |
| **License** | MIT License |

---

## 🎯 Dùng để làm gì

`wshobson/agents` là một "chợ" plugin tác nhân AI khổng lồ, được thiết kế để tích hợp vào các môi trường trợ lý mã hóa AI như Claude Code, OpenAI Codex CLI, Cursor, OpenCode, GitHub Copilot và Gemini CLI. Thay vì là một công cụ độc lập, nó cung cấp một bộ sưu tập phong phú gồm các plugin, agent, skill và lệnh được tối ưu hóa để thực hiện các tác vụ cụ thể. Người dùng có thể "thuê" các "đội ngũ" AI này miễn phí để tăng tốc quy trình phát triển, tự động hóa các tác vụ phức tạp và tối ưu hóa việc sử dụng token bằng cách chỉ cài đặt những gì cần thiết.

---

## 🚀 Bắt đầu nhanh

Để sử dụng các plugin từ marketplace này, bạn cần tích hợp nó vào môi trường AI coding assistant mà bạn đang dùng (ví dụ: Claude Code, Gemini CLI).

```bash
# Bước 1: Thêm Marketplace
# Lệnh này giúp các plugin của 'agents' có sẵn để cài đặt, nhưng chưa tải bất kỳ agent hay tool nào vào ngữ cảnh của bạn.
/plugin marketplace add wshobson/agents

# Bước 2: Cài đặt các Plugin cụ thể
# Duyệt qua các plugin có sẵn bằng lệnh /plugin, sau đó cài đặt những plugin bạn cần. 
# Mỗi plugin được cài đặt chỉ tải các agent và lệnh cụ thể của nó vào ngữ cảnh của Claude/Gemini.
/plugin install python-development

# Hoặc cài đặt các plugin khác tùy theo nhu cầu, ví dụ:
/plugin install backend-development
/plugin install debugging-toolkit
```

*(Lưu ý: Các lệnh trên là ví dụ, cú pháp chính xác có thể thay đổi tùy thuộc vào môi trường trợ lý AI bạn đang sử dụng. Tham khảo tài liệu trên GitHub để biết hướng dẫn chi tiết cho từng nền tảng cụ thể.)*

---

## 💡 Tại sao repo này hay

- **Hệ sinh thái Plugin đa dạng:** Cung cấp một bộ sưu tập khổng lồ gồm 84 plugin, 192 agent, 156 skill và 102 lệnh, bao trùm nhiều lĩnh vực phát triển.
- **Kiến trúc module, tối ưu token:** Thiết kế theo module cho phép bạn chỉ cài đặt và tải những plugin cần thiết, giúp tiết kiệm chi phí token và giữ ngữ cảnh gọn gàng.
- **Workflow thông minh:** Bao gồm các trình điều phối workflow phức tạp để xử lý các tác vụ đa agent từ phát triển full-stack, tăng cường bảo mật đến quản lý sự cố.
- **Hỗ trợ Agent Teams:** Cho phép các workflow song song, ví dụ như đánh giá code, debug, và phát triển tính năng với sự tham gia của nhiều agent cùng lúc.
- **Luôn được cập nhật:** Repo được duy trì tích cực và cập nhật để tương thích với các mô hình AI mới nhất như Claude Opus 4.6, Sonnet 4.6 và Haiku 4.5.

---

## ⚠️ Cần biết trước

- **Không phải công cụ độc lập:** Đây là một marketplace plugin cho các môi trường AI coding assistant hiện có, không phải một công cụ để clone và chạy độc lập.
- **Phụ thuộc vào nền tảng:** Các lệnh cài đặt và cách sử dụng chính sẽ phụ thuộc vào khả năng và giao diện của trợ lý AI mà bạn tích hợp (ví dụ: Claude Code, Gemini CLI).
- **Tài liệu chi tiết:** Để hiểu rõ hơn về cách tích hợp và sử dụng cho từng nền tảng cụ thể, bạn cần tham khảo file `docs/harnesses.md` và các tài liệu khác trong repository.

---

## 🔗 Tài nguyên liên quan

- [Toàn bộ tài liệu (docs)](https://github.com/wshobson/agents/tree/main/docs)
- [Danh mục Plugin chi tiết](https://github.com/wshobson/agents/blob/main/docs/plugins.md)
- [Danh mục Agent chi tiết](https://github.com/wshobson/agents/blob/main/docs/agents.md)

---

*Phát hiện bởi: tano2026 | Ngày thêm vào kho: [ngày]*
# MCP Setup — Infra Ops Agent

## Không cần MCP mới bắt buộc

Agent này chủ yếu dùng skill + đọc playbook có sẵn trong `/agents/`, không cần connector
ghi/gửi nào (đúng nguyên tắc: agent chỉ tư vấn, không tự thực thi).

## Nên có sẵn (đã có trong kho)

| MCP | Vai trò | File kho |
|---|---|---|
| GitHub API (đã dùng cho kho) | đọc playbook Antigravity/Hermes/OpenClaw trước khi ra khuyến nghị | — |
| Context7 | tránh bịa API khi viết script deploy MCP server mới | `/mcps/context7.md` |

## Không bao giờ bật

- Bất kỳ MCP có quyền SSH/exec trực tiếp lên VPS production cho agent này — quyền đó
  thuộc về Antigravity, không phải Infra Ops Agent. Agent chỉ soạn, không tự chạy.
- Quyền write trực tiếp vào file hệ thống VPS (chỉ đề xuất lệnh, không tự thực thi).

# Infra Ops Agent — VPS/Agent-Fleet Operations Specialist

Agent chuyên vận hành hạ tầng cho 3 agent Hermes/OpenClaw/Antigravity chạy trên VPS
Tencent Cloud — deploy, debug, security audit, cost/capacity — nhưng KHÔNG tự SSH/chạy
lệnh thật. Agent này chỉ soạn plan + script + rủi ro, Antigravity là bên thực thi.

## Spec

- **Domain:** Infrastructure Operations cho AI Agent VPS (Tencent Cloud, CentOS/RHEL)
- **Job-to-be-done:** Nhận 1 vấn đề vận hành (deploy, lỗi, security, chi phí) → ra
  plan/script/checklist cụ thể + rủi ro rõ, để Antigravity thực thi thật trên VPS
- **Người dùng:** Nobitano trực tiếp, hoặc Antigravity tự đọc kho khi cần quyết định
  trước khi chạy lệnh có rủi ro
- **Input điển hình:**
  - "Deploy CubeSandbox lên VPS, cần check gì trước"
  - "Antigravity báo CPU 90%, chẩn đoán sao"
  - "Audit security VPS trước khi mở port mới"
  - "Tối ưu chi phí Tencent Cloud, đang tốn bao nhiêu"
  - "MCP server mới cần setup gì trên VPS"
- **Output điển hình:** Deploy checklist, diagnosis report, security audit report,
  cost/capacity report, rollback plan
- **Mức tự chủ:** Tra cứu + Phân tích + Soạn script. KHÔNG tự SSH, KHÔNG tự chạy lệnh
  trên VPS thật — mọi lệnh chỉ là đề xuất, Antigravity/Nobitano confirm rồi mới chạy.
- **Rủi ro cao nhất:** Lệnh sai làm sập VPS production hoặc mở lỗ hổng security →
  **guardrail**: mọi lệnh có tính phá hủy (rm, drop, kill, iptables flush, chmod 777...)
  PHẢI được flag rõ trong output, kèm rollback plan, không bao giờ đưa vào script "chạy
  liền" mà không có bước xác nhận.

## Capability Map

**Não (Skills — đa số đã có sẵn trong kho):**
| Skill | Vai trò |
|---|---|
| `deployment-patterns` (kho có sẵn) | CI/CD, containerization, health check, rollback |
| `security-review` (kho có sẵn) | checklist security khi thêm auth/API/secrets |
| `security-scan` (kho có sẵn) | scan config agent (.claude/, MCP, hooks) tìm lỗ hổng |
| `terminal-ops` (kho có sẵn) | evidence-first: chạy lệnh kèm proof đã verify |
| `openclaw-ops` (kho có sẵn) | vận hành/maintain OpenClaw gateway |
| `enterprise-agent-ops` (kho có sẵn) | observability + lifecycle cho agent chạy 24/7 |
| `automation-audit-ops` (kho có sẵn) | audit job/hook/MCP nào live/broken/dư thừa |
| `cost-tracking` (kho có sẵn) | track chi phí token/usage |
| `architecture-decision-records` (kho có sẵn) | ghi lại quyết định hạ tầng + lý do |
| `mcp-server-patterns` (kho có sẵn) | build/debug MCP server mới |
| `destructive-command-guardrail` (mới viết) | chặn/flag lệnh phá hủy trước khi đưa ra |
| `tencent-vps-capacity-cost` (mới viết) | capacity planning + cost riêng Tencent Cloud |

**Tay:**
| Tool | Vai trò |
|---|---|
| Đọc `agents/ANTIGRAVITY-PLAYBOOK.md`, `agents/HERMES-PLAYBOOK.md`, `agents/OPENCLAW-PLAYBOOK.md` | context vận hành hiện tại |
| Web search/GitHub API (kho có sẵn) | tra lỗi, doc tool mới |

**Cơ:**
| Việc | Trang bị |
|---|---|
| Phân tích log/metric | Code execution |
| Báo cáo cost/capacity | xlsx |

## Kiến trúc

Xem `ARCHITECTURE.md`.

## Cách bung

1. Copy `skills/*` vào skills directory.
2. Dán `system-prompt.md` làm system/project instruction.
3. Agent này CHỈ tư vấn — không gắn quyền SSH/exec thật. Antigravity vẫn là bên duy nhất
   chạy lệnh trên VPS, theo đúng phân công trong Project Instructions.
4. Chạy test case trong `deploy-checklist.md`.

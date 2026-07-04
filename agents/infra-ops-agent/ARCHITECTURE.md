# Architecture — Infra Ops Agent

```
                    Infra Ops Orchestrator
              (phân loại: deploy / debug / security / cost)
                              |
        +---------------------+---------------------+
        |                     |                     |
    COLLECTOR             VALIDATOR              EXECUTOR
  (đọc playbook +      (chấm rủi ro/destructive   (soạn script/plan
   log/metric hiện tại)  command guardrail)         cụ thể)
        |                     |                     |
  đọc HERMES/OPENCLAW/   destructive-command-   deployment-patterns
  ANTIGRAVITY-PLAYBOOK    guardrail              terminal-ops
  automation-audit-ops    security-review        mcp-server-patterns
                           security-scan          tencent-vps-capacity-cost
        |                     |                     |
        +---------------------+---------------------+
                              |
                       SYNTHESIZER
        (architecture-decision-records: ghi lại quyết định + lý do)
                              |
              Output: plan/script/checklist + rủi ro
           (KHÔNG tự SSH/chạy — Antigravity thực thi thật)
```

## Luồng theo loại task

### Loại 1 — Deploy service mới (VD: "deploy CubeSandbox")
```
Collector (đọc ANTIGRAVITY-PLAYBOOK + note đã có, VD: cần check lsmod kvm trước)
  → Validator (security-review + destructive-command-guardrail nếu script có bước xóa/ghi đè)
  → Executor (deployment-patterns: viết checklist deploy + rollback plan)
  → Synthesizer → Output: deploy checklist đầy đủ, kèm rủi ro, giao Antigravity chạy
```

### Loại 2 — Debug/chẩn đoán (VD: "CPU 90%, sao rồi")
```
Collector (metric/log hiện có, đọc automation-audit-ops xem job nào đang chạy)
  → Validator (không có bước phá hủy → bỏ guardrail)
  → Executor (terminal-ops: đề xuất lệnh chẩn đoán, evidence-first)
  → Synthesizer → Output: chẩn đoán + lệnh kiểm tra đề xuất (không tự chạy)
```

### Loại 3 — Security audit (VD: "audit trước khi mở port mới")
```
Collector → Validator (security-scan + security-review: full checklist)
  → Synthesizer → Output: báo cáo lỗ hổng + mức độ nghiêm trọng, không tự sửa
```

### Loại 4 — Cost/capacity (VD: "tối ưu chi phí Tencent Cloud")
```
Collector (cost-tracking: số liệu hiện có)
  → Executor (tencent-vps-capacity-cost: benchmark, đề xuất resize/scale)
  → Synthesizer → Output: báo cáo cost + khuyến nghị, kèm rủi ro nếu downsize sai
```

## Guardrail cứng

1. Mọi lệnh có tính phá hủy (rm -rf, DROP, kill -9 process core, iptables -F,
   chmod 777, systemctl stop trên service production) → PHẢI chạy qua
   `destructive-command-guardrail` trước, kèm rollback plan rõ ràng trong output.
2. Agent KHÔNG có quyền SSH/exec thật — chỉ soạn script/plan. Antigravity là bên
   DUY NHẤT thực thi trên VPS, đúng theo phân công gốc trong Project Instructions.
3. Quyết định hạ tầng quan trọng (đổi kiến trúc, thêm node, đổi provider) →
   ghi lại bằng `architecture-decision-records`, không quyết định ngầm không lưu vết.
4. Không bịa thông số benchmark/cost — nếu không có data thật từ VPS, nói rõ "chưa có
   số liệu, cần Antigravity cung cấp log/metric trước".

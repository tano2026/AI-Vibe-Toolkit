---
name: destructive-command-guardrail
description: >
  Chặn/flag lệnh có tính phá hủy (xóa data, kill process, đổi firewall, ghi đè quyền)
  trước khi đưa vào bất kỳ script/plan nào cho VPS. Dùng khi soạn lệnh deploy/debug/
  cleanup có khả năng gây mất data hoặc sập service production.
---

# Destructive Command Guardrail

## TL;DR
Bất kỳ lệnh nào có thể gây mất data hoặc sập service phải được flag rõ + có rollback
plan TRƯỚC khi đưa vào output — không âm thầm nhúng vào 1 script dài rồi để lẫn.

## Khi nào dùng
- Soạn script deploy có bước xóa/ghi đè container, volume, config cũ
- Đề xuất lệnh cleanup (dọn log, xóa image cũ, prune docker)
- Đề xuất đổi firewall/iptables, security group
- Đề xuất kill process, restart service production

## Danh sách pattern lệnh phá hủy (không đầy đủ, mở rộng khi gặp case mới)

| Nhóm | Ví dụ pattern | Rủi ro |
|---|---|---|
| Xóa file/data | `rm -rf`, `DROP TABLE`, `DROP DATABASE`, `docker volume rm` | Mất data không phục hồi được |
| Firewall/network | `iptables -F`, `ufw disable`, mở port ra ngoài không giới hạn IP | Mở lỗ hổng an ninh |
| Process/service | `kill -9` process core, `systemctl stop` service production | Sập dịch vụ đang chạy |
| Quyền | `chmod 777`, `chown -R` sai user | Lỗ hổng quyền truy cập |
| Ghi đè | `git push --force`, `terraform destroy`, overwrite config không backup | Mất lịch sử/config cũ |

## Quy trình

### 1. Quét lệnh trước khi đưa vào output
Nếu script/plan có bất kỳ pattern ở bảng trên → dừng, không đưa thẳng vào.

### 2. Format bắt buộc khi có lệnh phá hủy
```
⚠️ Lệnh phá hủy: [lệnh cụ thể]
Vì sao cần:      [lý do phải chạy lệnh này]
Rủi ro:          [điều gì mất nếu chạy sai/chạy nhầm môi trường]
Rollback plan:   [cách khôi phục nếu có sự cố — backup trước, snapshot, v.v.]
Cần confirm từ:  Nobitano/Antigravity trước khi chạy — KHÔNG tự thực thi
```

### 3. Luôn đề xuất bước backup/snapshot trước lệnh phá hủy
VD: trước `rm -rf /data/old`, đề xuất `tar -czf backup.tar.gz /data/old` trước.

## Ví dụ thực tế
User: "Dọn container cũ trên VPS cho gọn"
→ Agent không tự viết `docker system prune -af` trần trụi, mà:
```
⚠️ Lệnh phá hủy: docker system prune -af
Vì sao cần: dọn image/container không dùng để nhẹ disk
Rủi ro: xóa luôn image đang cần nếu container liên quan đang stop tạm, không phải bỏ hẳn
Rollback plan: chạy `docker system df` trước để xem sẽ mất gì, backup image quan trọng
  bằng `docker save` trước khi prune
Cần confirm từ: Antigravity chạy sau khi Nobitano xác nhận danh sách container an toàn
```

## Lưu ý / Lỗi thường gặp
- Đừng chỉ dựa vào tên lệnh để đánh giá — `rm -rf ./tmp/` khác hoàn toàn `rm -rf /`,
  vẫn phải đọc kỹ path/scope trước khi flag mức độ rủi ro.
- Đừng quên lệnh phá hủy "ẩn" trong flag, VD: `git push --force` không có chữ "rm"
  nhưng vẫn phá hủy lịch sử.

## Đánh giá cá nhân
- Điểm mạnh: buộc dừng lại suy nghĩ trước khi thả lệnh nguy hiểm vào script tự động.
- Điểm yếu: danh sách pattern không thể đầy đủ 100% — vẫn cần agent tự suy luận với
  lệnh lạ chưa từng gặp, không chỉ match cứng theo bảng.
- Có nên dùng không: 9/10 — bắt buộc cho mọi agent có quyền soạn script chạy trên VPS
  production.

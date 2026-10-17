# Test plan — `{{slug}}`

> Bộ test PASS/FAIL. Cột "Kết quả" mặc định `CHUA-CHAY`. Chỉ con người chạy thật mới đổi thành `PASS` hoặc `FAIL`,
> kèm ngày và tên người chạy trong `test-cases.json`. Test mang nhãn `lan-ranh-do` phải PASS trước khi rời `draft_only`.

{{TEST_TABLE}}

## Cách chạy

1. Dựng agent theo `deploy-checklist.md` Pha 1.
2. Với từng test: đưa "đầu vào" cho agent, so với "mong đợi", ghi kết quả vào `test-cases.json` (`ket_qua`, `nguoi_chay`, `ngay`).
3. Test thất bại: ghi escalation, sửa, chạy lại. Không đổi "mong đợi" để cho qua.

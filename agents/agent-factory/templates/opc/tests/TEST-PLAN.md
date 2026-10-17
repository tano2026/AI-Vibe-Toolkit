# Test plan — OPC `{{slug}}`

> Bộ test PASS/FAIL của OPC. Mặc định `CHUA-CHAY`. Chỉ con người chạy thật mới ghi `PASS` hoặc `FAIL` (kèm ngày và tên người chạy trong `test-cases.json`).
> Test `lan-ranh-do` phải PASS trước khi bộ phận liên quan rời `draft_only`.

{{TEST_TABLE}}

## Cách chạy

1. Dựng Airtable và agent theo `HANDOVER.md`.
2. Với từng test: đưa đầu vào, so với mong đợi, ghi kết quả vào `test-cases.json`.
3. Thất bại: ghi escalation, sửa, chạy lại. Không sửa "mong đợi" để cho qua.

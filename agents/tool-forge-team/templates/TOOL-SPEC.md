# TOOL-SPEC — {{tên tool}}

> Claude viết, chủ đọc nhanh và nói OK. Hai tay làm song song chỉ dựa vào file này. Chỗ chưa biết ghi `CHƯA CÓ — hỏi CEO`, không bịa.

- **Task id:** TF-{{ngày}}-{{nn}}-{{slug}}
- **Ngày:** {{lấy từ hệ thống}}
- **Mức:** A / B / C — lý do một câu: {{...}}

## 1. Một câu

**{{làm gì}} → {{ra gì}} → {{cho ai}}**

## 2. Vấn đề thật

{{việc gì đang tốn thời gian; ai làm; bao lâu một lần; sai ở đâu}}

## 3. Đầu vào

| Nguồn | Dạng | Ví dụ giả |
|---|---|---|
| {{vd: text dán từ GDS}} | {{text/CSV/PDF/ảnh}} | {{...}} |

## 4. Đầu ra

{{dạng dùng ngay được: báo giá, bảng, nội dung đăng, CSV...}}

## 5. Hợp đồng giao diện JSON (luật cho cả hai tay)

Đầu vào logic:
```json
{ "truong_1": "kieu", "truong_2": 0 }
```
Đầu ra logic:
```json
{ "ket_qua": "kieu", "diem": 0, "ket_luan": "GO|HOLD|NO-GO", "ly_do": ["..."] }
```
Lỗi:
```json
{ "loi": "thông báo tiếng Việt", "truong": "tên trường sai" }
```

## 6. Công thức (chữ thường, chép được vào Excel)

| Tên | Công thức | Nguồn / trạng thái |
|---|---|---|
| {{...}} | {{vd: EV1000 = 1000 × CTR × CVR × hoa_hồng_ròng}} | {{lấy từ tài liệu / GIẢ ĐỊNH, chưa kiểm chứng}} |

## 7. Ngưỡng và trọng số (vào `config.json`, chỉnh được)

| Khoá | Giá trị | Thị trường | Trạng thái |
|---|---|---|---|
| {{...}} | {{...}} | VN / chung | đề xuất, chưa kiểm chứng / có nguồn: {{...}} |

## 8. Ca kiểm (tính tay được; tối thiểu 3, gồm 1 GO, 1 NO-GO, 1 sát ngưỡng)

| # | Đầu vào (dữ liệu giả) | Kết quả mong đợi | Cách tính tay |
|---|---|---|---|
| 1 | {{...}} | {{...}} | {{...}} |

## 9. Tool KHÔNG làm

- {{ít nhất một dòng cụ thể}}

## 10. Dữ liệu và bảo mật

- Có dữ liệu nhạy cảm không: {{có/không; loại gì}}
- Lưu ở đâu, xoá thế nào: {{...}}
- Gọi LLM: {{có/không; phần nào; trần số lần/chi phí}}
- Gói ngoài được phép dùng: {{danh sách; giấy phép nếu mức C}}
- Tên biến môi trường cần (không giá trị): {{...}}

## 11. Giao việc

| Tay | Vùng | Việc |
|---|---|---|
| DSH | `logic/` | {{...}} (mức A: bỏ dòng này) |
| Antigravity | `ui/`, `deploy/` | {{...}} |

## 12. Giả định đã tự chọn

- {{...}}

## 13. Liên quan kho

- {{mục kho đã có liên quan, dùng `kho:<id>` hoặc đường dẫn; ghi "đã tra Thủ Kho, ngày ..."}}
